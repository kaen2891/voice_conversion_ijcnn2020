import tensorflow as tf
import numpy as np
import argparse
import os
import sys
import pickle
import matplotlib.pyplot as plt
import librosa
import librosa.display
import model
import time
from datetime import datetime
import matplotlib

matplotlib.use('Agg')
import numpy as np
import librosa
import librosa.display
import soundfile as sf
import os

parser = argparse.ArgumentParser()

parser.add_argument('--num_enc', type=int, default='6', help='number of encoder layers')
parser.add_argument('--num_dec', type=int, default='6', help='number of decoder layers')
parser.add_argument('--d_model', type=int, default='256', help='number of hidden size(frequency sizes)')
parser.add_argument('--num_heads', type=int, default='8', help='number of multihead attention')
parser.add_argument('--dff', type=int, default='1024', help='number of feed forward network size')
parser.add_argument('--max_sequence_length', type=int, default='444', help='number of max sequence size')
parser.add_argument('--dropout_rate', type=float, default='0.1', help='number of max sequence size')
parser.add_argument('--hop', type=int, default='256', help='number of noverlap')
parser.add_argument('--ckpt', type=str, default='1', help='check point path')
parser.add_argument('--enc_inp', type=str, default='/dir/source_dataset/', help='encoder input directory')
parser.add_argument('--enc_phase_inp', type=str, default='/dir/source_phase_dataset/', help='encoder input phase directory')
parser.add_argument('--tar_inp', type=str, default='/dir/real_dataset/', help='real input for compare results')
parser.add_argument('--tar_phase_inp', type=str, default='/dir/real_phase_dataset/', help='real phase input for compare results')
parser.add_argument('--gpus', type=str, default='0', help='using gpu number')
args = parser.parse_args()

os.environ['CUDA_VISIBLE_DEVICES'] = args.gpus

config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.compat.v1.Session(config=config)


def recover(concat, for_save, name):
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(librosa.amplitude_to_db(concat, ref=np.max), y_axis='hz', x_axis='time', sr=16000,
                             hop_length=args.hop)
    plt.title(name)
    plt.colorbar(format='%+2.0f dB')
    plt.tight_layout()
    
    fig_save_dir = for_save + '/fig/'
    if not os.path.exists(fig_save_dir):
        os.makedirs(fig_save_dir)
    plt.savefig(fig_save_dir + name + '.png')

    make_wav = librosa.istft(concat, hop_length=args.hop)
    wav_save_dir = for_save + '/wav/'
    if not os.path.exists(wav_save_dir):
        os.makedirs(wav_save_dir)
    sf.write(wav_save_dir + name + '.wav', make_wav, 16000, format='WAV', endian='LITTLE', subtype='PCM_16')
    print("{}th done", name)
    plt.cla()
    plt.close()


def plot_attention_weights(attention, layer, cnt, find_zero, set):
    fig = plt.figure(figsize=(16, 8))

    attention = tf.squeeze(attention[layer], axis=0)    
    attention = attention[:, :, :find_zero]

    for head in range(attention.shape[0]):
        ax = fig.add_subplot(2, 4, head + 1)

        # plot the attention weights
        ax.matshow(attention[head], cmap='viridis')  # for now

        fontdict = {'fontsize': 12}

        ax.set_title(' Encoder time step ', fontdict=fontdict)
        ax.set_ylabel(' Decoder time step', fontdict=fontdict)
        # ax.set_xlabel('Head {}'.format(head + 1))
        # plt.title('Head {}'.format(head + 1))
        ax.set_xlabel('Head {}'.format(head + 1))

    plt.tight_layout()

    cnt = str(cnt)
    save_dir = './attn_map/ckpt={}/{}'.format(args.ckpt, set)
    others = 'spec,cnt={}'.format(cnt)
    save_dir = os.path.join(save_dir, others)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    plt.savefig(save_dir + '/' + layer + '.png')
    plt.cla()
    plt.close()
    # plt.show()


def create_padding_mask_text(seq):
    seq = tf.cast(tf.math.equal(seq, 0), tf.float32)

    # add extra dimensions to add the padding
    # to the attention logits.
    return seq[:, tf.newaxis, tf.newaxis, :]  # (batch_size, 1, 1, seq_len)


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
    enc_padding_mask = create_padding_mask_spec(inp_spec)
    dec_padding_mask = create_padding_mask_spec(inp_spec)
    
    look_ahead_mask = create_look_ahead_mask(tf.shape(tar_spec)[1])  # max_seq_len, max_seq_len
    dec_target_padding_mask = create_padding_mask_spec(tar_spec)  # batch_size, 1, 1, max_seq_len

    combined_mask = tf.maximum(dec_target_padding_mask, look_ahead_mask)  # batch_size, 1, 1, max_seq_len

    return enc_padding_mask, combined_mask, dec_padding_mask


def evaluate(inp_spectrogram, transformer):
    # encoder input spec
    encoder_input_spec = tf.expand_dims(inp_spectrogram, 0)  # [1, seq_len, d_model]
    # decoder input spec ==> using only sos token in test phase
    decoder_input_spec = np.load('./sos_token.npy')    
    decoder_input_spec = decoder_input_spec[1:, :]  # [d_model, 1]
    decoder_input_spec = np.transpose(decoder_input_spec, (1, 0))  # [1, d_model]
    decoder_input_spec = tf.cast(decoder_input_spec, dtype=tf.float32)
    
    decoder_eos = np.load('./eos_token.npy')
    decoder_eos = decoder_eos[1:, :] # [d_model, 1]
    decoder_eos = np.transpose(decoder_eos, (1, 0))  # [1, d_model]
    decoder_eos = tf.cast(decoder_eos, dtype=tf.float32)
    decoder_eos = tf.expand_dims(decoder_eos, 0)
    
    output_spec = tf.expand_dims(decoder_input_spec, 0)  # [1, 1, d_model]        

    for i in range(args.max_sequence_length - 1):  
        enc_padding_mask, combined_mask, dec_padding_mask = create_masks(encoder_input_spec, output_spec)  # check

        predict_spec, attention_weights_spec = transformer(encoder_input_spec, output_spec, False, enc_padding_mask, combined_mask, dec_padding_mask)
        predict_spec = predict_spec[:, -1:, :]  # (batch_size, 1, d_model)        
        output_spec = tf.concat([output_spec, predict_spec], axis=1)        
        
        if np.array_equal(predict_spec, decoder_eos) == True:            
            return tf.squeeze(output_spec, axis=0), attention_weights_spec
        
        print("{}th iter, output_spec shape {}".format(i, output_spec.shape))

    return tf.squeeze(output_spec, axis=0), attention_weights_spec


def main():
    checkpoint_path = "./checkpoints{}/train".format(args.ckpt)
            
    transformer = model.Transformer(args.num_enc, args.num_dec, args.d_model, args.num_heads, args.dff, args.max_sequence_length, rate=args.dropout_rate)
    ckpt = tf.train.Checkpoint(transformer=transformer)
    ckpt_manager = tf.train.CheckpointManager(ckpt, checkpoint_path, max_to_keep=5)
    #this_model = ckpt.restore(ckpt_manager.latest_checkpoint)
    
    # source magniutde of the STFT
    X_spec = np.load(args.enc_inp) # (batch, d_model, seq_len)
    X_spec = np.transpose(X_spec, (0, 2, 1))  # (batch, seq_len, d_model)
    X_spec = X_spec[:, :, :-1]  # (batch, seq_len, d_model - 1)

    # real magniutde of the STFT. This is from target speaker. Only using for listening to compare target and predict.
    Y_spec = np.load(args.tar_inp)    
    Y_spec = Y_spec[:, :-1, 1:]  # (batch, d_model, seq)

    # test phase of the STFT
    X_phase = np.load(args.enc_phase_inp)
    X_phase = X_phase[:, :-1, :]  # (batch, d_model, seq)

    # real phase of the STFT. This is from target speaker. Only using for listening to compare target and predict.
    Y_phase = np.load(args.tar_phase_inp)
    Y_phase = Y_phase[:, :-1, 1:]  # (batch, d_model, seq)
    
    
    name = 'ckpt={}'.format(args.ckpt)

    save_dir = './result/'
    for i in range(len(X_spec)):
        
        inp_spec = X_spec[i]  # max_seq_len, d_model
        inp_pha = X_phase[i]  # d_model, seq_len
        
        predict_spec, attention_weights = evaluate(inp_spec, transformer)
        print("after predict, spec shape {}".format(np.shape(predict_spec)))

        # for make attention alignment map
        spec_t = inp_spec.T  # d_model, seq_len
        idx_spec = np.argwhere(np.diff(np.r_[False, spec_t[0], False]))
        find_zero_spec = np.squeeze(idx_spec)
        zero_cnt = find_zero_spec[-1]

        for x in range(6):

            plot = 'decoder_layer{}_block2'.format(x + 1)
            plot_attention_weights(attention_weights, plot, i + 1, zero_cnt)  # spec plot

        predict_spec = predict_spec[1:, :]  # (seq_len, d_model)
        predict_spec = np.transpose(predict_spec, (1, 0))  # (d_model, seq_len)

        # y_hat wav, fig save
        concat = predict_spec * inp_pha
        save_name = name + '_{}th'.format(i)
        for_save = os.path.join(save_dir, name)
        if not os.path.exists(for_save):
            os.makedirs(for_save)
        recover(concat, for_save, save_name)

        np_save_dir = 'np_file'
        np_dir = os.path.join(for_save, np_save_dir)
        if not os.path.exists(np_dir):
            os.makedirs(np_dir)
        # y_hat np file save
        save_np = '{}th_predict.result'.format(i)
        np_final_predict = os.path.join(np_dir, save_np)
        np.save(np_final_predict, concat)

        ########### check #######, x_real plot
        # x_real np file save
        x_real = inp_spec.T * X_phase[i]
        save_np_x_real = '{}th_x_real.result'.format(i)
        np_final_x_real = os.path.join(np_dir, save_np_x_real)
        np.save(np_final_x_real, x_real)

        # x_real wav, fig file save
        save_name_real = 'x_real_' + name + '_{}th'.format(i)
        for_save_real = os.path.join(save_dir, name)
        if not os.path.exists(for_save_real):
            os.makedirs(for_save_real)
        # np.save(for_save_real, real)
        recover(x_real, for_save_real, save_name_real)

        # y_real np file save
        y_real = Y_spec[i] * Y_phase[i]
        save_np_y_real = '{}th_y_real.result'.format(i)
        np_final_y_real = os.path.join(np_dir, save_np_y_real)
        np.save(np_final_y_real, y_real)

        # y_real wav, fig file save
        save_name_real = 'y_real_' + name + '_{}th'.format(i)
        for_save_real = os.path.join(save_dir, name)
        if not os.path.exists(for_save_real):
            os.makedirs(for_save_real)
        recover(y_real, for_save_real, save_name_real)


if __name__ == '__main__':
    main()
