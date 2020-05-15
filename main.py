# -*- coding:utf-8 -*-
import tensorflow as tf
import numpy as np
import argparse
import os
import sys
import matplotlib.pyplot as plt
from datetime import datetime
import model
import time
import librosa
import librosa.display
import soundfile as sf
import matplotlib

matplotlib.use('Agg')

parser = argparse.ArgumentParser()

parser.add_argument('--num_enc', type=int, default='6', help='number of encoder layers')
parser.add_argument('--num_dec', type=int, default='6', help='number of decoder layers')
parser.add_argument('--d_model', type=int, default='256', help='number of hidden size (frequency sizes)')
parser.add_argument('--num_heads', type=int, default='8', help='number of multihead attentions')
parser.add_argument('--dff', type=int, default='1024', help='number of feed forward network sizes')
parser.add_argument('--max_sequence_length', type=int, default='438', help='number of max sequence size')
parser.add_argument('--dropout_rate', type=float, default='0.1', help='number of max sequence size')
parser.add_argument('--lr', type=float, default='0', help='initial learning rate')
parser.add_argument('--hop', type=int, default='256', help='number of noverlap')
parser.add_argument('--ckpt', default='0', help='check point path')
parser.add_argument('--batch_size', type=int, default='64', help='number of batch sizes')
parser.add_argument('--epochs', type=int, default='1000', help='number of epochs')
parser.add_argument('--gpus', type=str, default='0', help='using gpu number')
parser.add_argument('--enc_inp', type=str, default='/dir/source_dataset/', help='encoder input directory')
parser.add_argument('--dec_inp', type=str, default='/dir/sos_target_dataset/', help='decoder input directory')
parser.add_argument('--tar_inp', type=str, default='/dir/target_eos_dataset/', help='real input for calculate loss')
#parser.add_argument('--infor', type=str, default='check', help='option')
args = parser.parse_args()

os.environ['CUDA_VISIBLE_DEVICES'] = args.gpus

# For use tf ver 1.0. This is for checking the GPU memory while training.
config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.compat.v1.Session(config=config)


def plot_attention_weights(attention, layer, cnt, find_zero, find_zero_tar):
    fig = plt.figure(figsize=(16, 8))

    attention = attention[layer]
    attention = attention[0]
    attention = attention[:, :find_zero_tar, :find_zero]

    for head in range(attention.shape[0]):
        ax = fig.add_subplot(2, 4, head + 1)

        # plot the attention weights
        ax.matshow(attention[head], cmap='viridis')  

        fontdict = {'fontsize': 12}

        ax.set_title(' Encoder time step ', fontdict=fontdict)
        ax.set_ylabel(' Decoder time step', fontdict=fontdict)
        ax.set_xlabel('Head {}'.format(head + 1))

    plt.tight_layout()

    cnt = str(cnt)
    save_dir = './attn_map/train/ckpt={}/'.format(args.ckpt)
    others = 'spec,epoch={}'.format(cnt)
    save_dir = os.path.join(save_dir, others)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    plt.savefig(save_dir + '/' + layer + '.png')
    plt.cla()
    plt.close()

def create_padding_mask_spec(seq):
    seq = tf.cast(tf.not_equal(seq, 0), tf.float32)
    seq = tf.cast(tf.reduce_max(seq, axis=-1), tf.float32)
    seq = tf.cast(tf.not_equal(seq, 1), tf.float32)
    # add extra dimensions to add the padding
    # to the attention logits.
    return seq[:, tf.newaxis, tf.newaxis, :]  # (batch_size, 1, 1, seq_len)


def create_look_ahead_mask(size):
    mask = 1 - tf.linalg.band_part(tf.ones((size, size)), -1, 0)
    
    return mask  # (seq_len, seq_len)


def create_masks(inp_spec, tar_spec):
    # Encoder padding mask
    enc_padding_mask = create_padding_mask_spec(inp_spec)

    # Used in the 2nd attention block in the decoder.
    # This padding mask is used to mask the encoder outputs.    
    dec_padding_mask = create_padding_mask_spec(inp_spec)
    
    # Used in the 1st attention block in the decoder.
    # It is used to pad and mask future tokens in the input received by the decoder.
    look_ahead_mask = create_look_ahead_mask(tf.shape(tar_spec)[1])  # max_seq_len, max_seq_len
    dec_target_padding_mask = create_padding_mask_spec(tar_spec)  # batch_size, 1, 1, max_seq_len    
    combined_mask = tf.maximum(dec_target_padding_mask, look_ahead_mask)  # batch_size, 1, 1, max_seq_len

    return enc_padding_mask, combined_mask, dec_padding_mask

loss_object_l1 = tf.keras.losses.MeanAbsoluteError(reduction='none')
loss_object_mse = tf.keras.losses.MeanSquaredError(reduction='none')

def loss_function(real, pred):
    mask = tf.cast(tf.math.equal(real, 0), tf.float32)
    mask = tf.cast(tf.logical_not(tf.cast(tf.reduce_min(mask, axis=-1), tf.bool)), tf.float32)
    
    l1 = loss_object_l1(real, pred, sample_weight=mask)
    mse = loss_object_mse(real, pred, sample_weight=mask)    
    final_loss = (l1 * 0.5) + (mse * 0.5)
    
    return tf.reduce_mean(final_loss)

def input_fn(spec_inp, spec_dec, spec_tar, BATCH_SIZE, BUFFER_SIZE):
    dataset = tf.data.Dataset.from_tensor_slices((spec_inp, spec_dec, spec_tar))
    dataset = dataset.cache()

    train_dataset = dataset.shuffle(BUFFER_SIZE).batch(BATCH_SIZE)

    train_dataset = train_dataset.prefetch(tf.data.experimental.AUTOTUNE)
    return train_dataset


def main():
    # load dataset here

    spec_enc_inp = np.load(args.enc_inp)
    spec_enc_inp = spec_enc_inp.astype('float32')
    
    spec_dec_inp = np.load(args.dec_inp)
    spec_dec_inp = spec_dec_inp.astype('float32')
    
    spec_tar_inp = np.load(args.tar_inp)
    spec_tar_inp = spec_tar_inp.astype('float32')
    

    spec_enc_inp = spec_enc_inp[:, :-1, :] # batch, d_model, seq_len
    spec_dec_inp = spec_dec_inp[:, :-1, :] # batch, d_model, seq_len
    spec_tar_inp = spec_tar_inp[:, :-1, :] # batch, d_model, seq_len

    enc_inp_spec = np.transpose(spec_enc_inp, (0, 2, 1)) # batch, seq_len, d_model 
    dec_inp_spec = np.transpose(spec_dec_inp, (0, 2, 1)) # batch, seq_len, d_model
    tar_inp_spec = np.transpose(spec_tar_inp, (0, 2, 1)) # batch, seq_len, d_model
    
    print("enc_inp_spec shape {} dec_inp_spec shape {} tar_inp_spec shape {}".format(np.shape(enc_inp_spec), np.shape(dec_inp_spec), np.shape(tar_inp_spec)))

    ckpt_path = args.ckpt

    batch_size = args.batch_size
    buffer_size = 80
    EPOCHS = args.epochs

    train_dataset = input_fn(enc_inp_spec, dec_inp_spec, tar_inp_spec, batch_size, buffer_size)

    train_loss = tf.keras.metrics.Mean(name='train_loss')    
    
    transformer = model.Transformer(args.num_enc, args.num_dec, args.d_model, args.num_heads, args.dff, args.max_sequence_length, rate=args.dropout_rate)    
    
    if args.lr == 0:
        lr_schedule = model.CustomSchedule(args.d_model)
        print("lr is {}. Using schedule sampling learning rate".format(args.lr))
    else:
        initial_learning_rate = args.lr
        
        lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(
        initial_learning_rate,
        decay_steps=4000,
        decay_rate=0.96,
        staircase=True)
        print("lr is not schedule! We use {}".format(args.lr))

    optimizer = tf.keras.optimizers.Adam(lr_schedule, beta_1=0.9, beta_2=0.98, epsilon=1e-9)

    checkpoint_path = "./checkpoints{}/train".format(args.ckpt)

    ckpt = tf.train.Checkpoint(transformer=transformer, optimizer=optimizer)
    ckpt_manager = tf.train.CheckpointManager(ckpt, checkpoint_path, max_to_keep=None)

    # writer = tf.summary.create_file_writer("/tmp/mylogs/eager")
    logdir = "logs/scalars{}/".format(args.ckpt) + datetime.now().strftime("%Y%m%d-%H%M%S")

    file_writer = tf.summary.create_file_writer(logdir + "/metrics")
    file_writer.set_as_default()

    if ckpt_manager.latest_checkpoint:
        ckpt.restore(ckpt_manager.latest_checkpoint)
        print('Latest checkpoint restored!!')

    train_step_signature = [
        tf.TensorSpec(shape=(None, None, None), dtype=tf.float32),
        tf.TensorSpec(shape=(None, None, None), dtype=tf.float32),
        tf.TensorSpec(shape=(None, None, None), dtype=tf.float32),
    ]

    @tf.function(input_signature=train_step_signature)
    def train_step(inp_spec, dec_spec, tar_spec):
        enc_padding_mask, combined_mask, dec_padding_mask = create_masks(inp_spec, dec_spec)

        with tf.GradientTape() as tape:
            predict_spec, attention_weight = transformer(inp_spec, dec_spec, True, enc_padding_mask, combined_mask, dec_padding_mask)
            
            loss = loss_function(tar_spec, predict_spec)

        gradient = tape.gradient(loss, transformer.trainable_variables)
        optimizer.apply_gradients(zip(gradient, transformer.trainable_variables))

        train_loss(loss)

        return predict_spec, attention_weight


    for epoch in range(EPOCHS):
        start = time.time()
        
        train_loss.reset_states()        

        # inp -> man, tar -> woman
        for (batch, (inp_spec, dec_spec, tar_spec)) in enumerate(train_dataset):

            name_before = 'before_predict_epoch={}'.format(int(epoch))
            result_before = inp_spec[0]
            result_before = np.transpose(result_before, (1, 0))

            result, attention_weight = train_step(inp_spec, dec_spec, tar_spec)

            if batch % 20 == 0:
                print('Epoch {} Batch {} Loss {:.4f} '.format(epoch + 1, batch, train_loss.result()))

        if (epoch + 1) % 20 == 0:
            ckpt_save_path = ckpt_manager.save()
            print('Saving checkpoint for epoch {} at {}'.format(epoch + 1,
                                                                ckpt_save_path))

        print('Epoch {} Loss {:.4f}'.format(epoch + 1, train_loss.result()))

        tf.summary.scalar('loss', data=train_loss.result(), step=epoch)

        print('Time taken for 1 epoch: {} secs\n'.format(time.time() - start))

        if epoch % 20 == 0:
            spec_t = inp_spec[0]
            spec_t = spec_t.numpy()
            spec_t = spec_t.T

            spec_tar = dec_spec[0]
            spec_tar = spec_tar.numpy()
            spec_tar_t = spec_tar.T
            
            idx_spec = np.argwhere(np.diff(np.r_[False, spec_t[0], False]))            
            idx_tar = np.argwhere(np.diff(np.r_[False, spec_tar_t[0], False]))
            
            find_zero_spec = np.squeeze(idx_spec)            
            find_zero_spec_tar = np.squeeze(idx_tar)
            
            zero_cnt = find_zero_spec[-1]            
            zero_cnt_tar = find_zero_spec_tar[-1]
            

            for x in range(6):
                plot = 'decoder_layer{}_block2'.format(x + 1)

                plot_attention_weights(attention_weight, plot, epoch, zero_cnt, zero_cnt_tar)  # spec plot attention weights

        if epoch % 5 == 0: # Get results from trainset every 5 epochs
            epc = int(epoch)
            name_after = 'after_predict_epoch={}'.format(epc)
            result_after = result[0]
            result_after = np.transpose(result_after, (1, 0))

            # The dataset before training (original input)
            plt.figure(figsize=(10, 4))
            librosa.display.specshow(librosa.amplitude_to_db(result_before, ref=np.max), y_axis='hz', x_axis='time',
                                     sr=16000, hop_length=args.hop)
            plt.title(name_before)
            plt.colorbar(format='%+2.0f dB')
            plt.tight_layout()
            fig_save_dir = './result/' + ckpt_path + '_fig/'
            if not os.path.exists(fig_save_dir):
                os.makedirs(fig_save_dir)
            plt.savefig(fig_save_dir + name_before + '.png')
            plt.cla()
            plt.close()

            make_wav = librosa.istft(result_before, hop_length=args.hop)
            wav_save_dir = './result/' + ckpt_path + '_wav/'
            if not os.path.exists(wav_save_dir):
                os.makedirs(wav_save_dir)
            sf.write(wav_save_dir + name_before + '.wav', make_wav, 16000, format='WAV', endian='LITTLE',
                     subtype='PCM_16')

            # Results after training from trainset (y_hat)
            plt.figure(figsize=(10, 4))
            librosa.display.specshow(librosa.amplitude_to_db(result_after, ref=np.max), y_axis='hz', x_axis='time',
                                     sr=16000, hop_length=args.hop)
            plt.title(name_after)
            plt.colorbar(format='%+2.0f dB')
            plt.tight_layout()
            plt.savefig(fig_save_dir + name_after + '.png')
            plt.cla()
            plt.close()

            make_wav = librosa.istft(result_after, hop_length=args.hop)
            sf.write(wav_save_dir + name_after + '.wav', make_wav, 16000, format='WAV', endian='LITTLE',
                     subtype='PCM_16')

            # Real input (source)
            save_tar = tar_spec[0]
            save_tar = np.transpose(save_tar, (1, 0))
            plt.figure(figsize=(10, 4))
            librosa.display.specshow(librosa.amplitude_to_db(save_tar, ref=np.max), y_axis='hz', x_axis='time',
                                     sr=16000, hop_length=args.hop)
            real_name = 'real_epoch={}'.format(epc_before)
            plt.title(real_name)
            plt.colorbar(format='%+2.0f dB')
            plt.tight_layout()
            fig_save_dir = './result/' + ckpt_path + '_fig/'
            if not os.path.exists(fig_save_dir):
                os.makedirs(fig_save_dir)
            plt.savefig(fig_save_dir + real_name + '.png')
            plt.cla()
            plt.close()

            make_wav = librosa.istft(save_tar, hop_length=args.hop)

            wav_save_dir = './result/' + ckpt_path + '_wav/'
            if not os.path.exists(wav_save_dir):
                os.makedirs(wav_save_dir)
            sf.write(wav_save_dir + real_name + '.wav', make_wav, 16000, format='WAV', endian='LITTLE',
                     subtype='PCM_16')

            # Numpy file before training
            np_save_dir = './result/' + ckpt_path + '_np_file/'
            if not os.path.exists(np_save_dir):
                os.makedirs(np_save_dir)
            np.save(np_save_dir + name_before, result_before)

            # Numpy file after training trainset
            np_save_dir = './result/' + ckpt_path + '_np_file/'
            if not os.path.exists(np_save_dir):
                os.makedirs(np_save_dir)
            np.save(np_save_dir + name_after, result_after)

            # Real Numpy file (source)
            np_save_dir = './result/' + ckpt_path + '_np_file/'
            if not os.path.exists(np_save_dir):
                os.makedirs(np_save_dir)
            real_name = 'y_real_epoch={}'.format(epc)

            np.save(np_save_dir + real_name, save_tar)


if __name__ == '__main__':
    main()
