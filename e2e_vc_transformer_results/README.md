# Sample results from "Vocoder-free End-to-End Voice Conversion with Transformer Network"


#### Authors: June-Woo Kim, Ho-Young Jung, Minho Lee

#### Abstract: Mel-frequency filter bank (MFB) based approaches have the advantage of higher learning speeds compared to using the raw spectrum due to a smaller number of features. However, speech generators with the MFB approach require an additional computationally expensive vocoder for the training process. The pre- and post-processing needed by the MFB and the vocoder is not essential to convert human voices, because it is possible to use only the raw spectrum to generate different style of voices with clear pronunciation. In this paper, we introduce a vocoder-free end-to-end voice conversion method using a transformer network to alleviate the computational burden from additional pre- and post-processing. Our transformer-based architecture, which does not have any CNN or RNN layers, has shown the benefit of learning fast while solving the limitation of sequential computation of the conventional RNN. For this reason, our model is a fast and effective approach to convert realistic voices using raw spectra in a parallel manner to generate different style of voices with clear pronunciation. Furthermore, we can get an adapted MFB for speech recognition by multiplying the converted magnitude with the phase information, and therefore our conversion model is also suitable for speaker adaptation. We perform our voice conversion experiments on TIDIGITS-dataset using the naturalness, similarity, and clarity with Mean Opinion Score as metrics.


## The first column is source voice, second is target voice, and last is converted voice.

## First domain voice : Girl

### Source: Girl, Target: Man, Result: Converted Man

#### Saying 'Three'

<audio controls="controls">
  Girl to Man (source)
  <source type="audio/wav" src="./conversion_results/G2M_S1(three).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Girl to Man (target)
  <source type="audio/wav" src="./conversion_results/G2M_T1(three).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Girl to Man (predict)
  <source type="audio/wav" src="./conversion_results/G2M_P1(three).wav"></source>
  <p>predict.</p>
</audio>

#### Saying 'Seven'

<audio controls="controls">
  Girl to Man (source)
  <source type="audio/wav" src="./conversion_results/G2M_S2(seven).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Girl to Man (target)
  <source type="audio/wav" src="./conversion_results/G2M_T2(seven).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Girl to Man (predict)
  <source type="audio/wav" src="./conversion_results/G2M_P2(seven).wav"></source>
  <p>predict.</p>
</audio>

#### Saying 'Nine'

<audio controls="controls">
  Girl to Man (source)
  <source type="audio/wav" src="./conversion_results/G2M_S3(nine).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Girl to Man (target)
  <source type="audio/wav" src="./conversion_results/G2M_T3(nine).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Girl to Man (predict)
  <source type="audio/wav" src="./conversion_results/G2M_P3(nine).wav"></source>
  <p>predict.</p>
</audio>

#### Saying 'Zero'

<audio controls="controls">
  Girl to Man (source)
  <source type="audio/wav" src="./conversion_results/G2M_S4(zero).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Girl to Man (target)
  <source type="audio/wav" src="./conversion_results/G2M_T4(zero).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Girl to Man (predict)
  <source type="audio/wav" src="./conversion_results/G2M_P4(zero).wav"></source>
  <p>predict.</p>
</audio>

### Source: Girl, Target: Woman, Result: Converted Woman



#### Saying 'Two'

<audio controls="controls">
  Girl to Woman (source)
  <source type="audio/wav" src="./conversion_results/G2W_S1(two).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Girl to Woman (target)
  <source type="audio/wav" src="./conversion_results/G2W_T1(two).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Girl to Woman (predict)
  <source type="audio/wav" src="./conversion_results/G2W_P1(two).wav"></source>
  <p>predict.</p>
</audio>

#### Saying 'Five'

<audio controls="controls">
  Girl to Woman (source)
  <source type="audio/wav" src="./conversion_results/G2W_S2(five).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Girl to Woman (target)
  <source type="audio/wav" src="./conversion_results/G2W_T2(five).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Girl to Woman (predict)
  <source type="audio/wav" src="./conversion_results/G2W_P2(five).wav"></source>
  <p>predict.</p>
</audio>

#### Saying 'Eight'

<audio controls="controls">
  Girl to Woman (source)
  <source type="audio/wav" src="./conversion_results/G2W_S3(eight).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Girl to Woman (target)
  <source type="audio/wav" src="./conversion_results/G2W_T3(eight).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Girl to Woman (predict)
  <source type="audio/wav" src="./conversion_results/G2W_P3(eight).wav"></source>
  <p>predict.</p>
</audio>

#### Saying 'Oh'

<audio controls="controls">
  Girl to Woman (source)
  <source type="audio/wav" src="./conversion_results/G2W_S4(oh).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Girl to Woman (target)
  <source type="audio/wav" src="./conversion_results/G2W_T4(oh).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Girl to Woman (predict)
  <source type="audio/wav" src="./conversion_results/G2W_P4(oh).wav"></source>
  <p>predict.</p>
</audio>

### Source: Girl, Target: Boy, Result: Converted Boy

#### Saying 'Four'

<audio controls="controls">
  Girl to Boy (source)
  <source type="audio/wav" src="./conversion_results/G2B_S1(four).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Girl to Boy (target)
  <source type="audio/wav" src="./conversion_results/G2B_T1(four).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Girl to Boy (predict)
  <source type="audio/wav" src="./conversion_results/G2B_P1(four).wav"></source>
  <p>predict.</p>
</audio>

#### Saying 'Five'

<audio controls="controls">
  Girl to Boy (source)
  <source type="audio/wav" src="./conversion_results/G2B_S2(five).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Girl to Boy (target)
  <source type="audio/wav" src="./conversion_results/G2B_T2(five).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Girl to Boy (predict)
  <source type="audio/wav" src="./conversion_results/G2B_P2(five).wav"></source>
  <p>predict.</p>
</audio>

#### Saying 'Six'

<audio controls="controls">
  Girl to Boy (source)
  <source type="audio/wav" src="./conversion_results/G2B_S3(six).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Girl to Boy (target)
  <source type="audio/wav" src="./conversion_results/G2B_T3(six).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Girl to Boy (predict)
  <source type="audio/wav" src="./conversion_results/G2B_P3(six).wav"></source>
  <p>predict.</p>
</audio>

#### Saying 'Eight'

<audio controls="controls">
  Girl to Boy (source)
  <source type="audio/wav" src="./conversion_results/G2B_S4(eight).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Girl to Boy (target)
  <source type="audio/wav" src="./conversion_results/G2B_T4(eight).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Girl to Boy (predict)
  <source type="audio/wav" src="./conversion_results/G2B_P4(eight).wav"></source>
  <p>predict.</p>
</audio>

## Second domain voice : Boy

### Source: Boy, Target: Man, Result: Converted Man

#### Saying 'Four'

<audio controls="controls">
  Boy to Man (source)
  <source type="audio/wav" src="./conversion_results/B2M_S1(four).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Boy to Man (target)
  <source type="audio/wav" src="./conversion_results/B2M_T1(four).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Boy to Man (predict)
  <source type="audio/wav" src="./conversion_results/B2M_P1(four).wav"></source>
  <p>predict.</p>
</audio>

#### Saying 'Six'

<audio controls="controls">
  Boy to Man (source)
  <source type="audio/wav" src="./conversion_results/B2M_S2(six).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Boy to Man (target)
  <source type="audio/wav" src="./conversion_results/B2M_T2(six).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Boy to Man (predict)
  <source type="audio/wav" src="./conversion_results/B2M_P2(six).wav"></source>
  <p>predict.</p>
</audio>

#### Saying 'Nine'

<audio controls="controls">
  Boy to Man (source)
  <source type="audio/wav" src="./conversion_results/B2M_S3(nine).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Boy to Man (target)
  <source type="audio/wav" src="./conversion_results/B2M_T3(nine).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Boy to Man (predict)
  <source type="audio/wav" src="./conversion_results/B2M_P3(nine).wav"></source>
  <p>predict.</p>
</audio>

#### Saying 'Oh'

<audio controls="controls">
  Boy to Man (source)
  <source type="audio/wav" src="./conversion_results/B2M_S4(oh).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Boy to Man (target)
  <source type="audio/wav" src="./conversion_results/B2M_T4(oh).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Boy to Man (predict)
  <source type="audio/wav" src="./conversion_results/B2M_P4(oh).wav"></source>
  <p>predict.</p>
</audio>

### Source: Boy, Target: Woman, Result: Converted Woman

#### Saying 'One'

<audio controls="controls">
  Boy to Woman (source)
  <source type="audio/wav" src="./conversion_results/B2W_S1(one).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Boy to Woman (target)
  <source type="audio/wav" src="./conversion_results/B2W_T1(one).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Boy to Woman (predict)
  <source type="audio/wav" src="./conversion_results/B2W_P1(one).wav"></source>
  <p>predict.</p>
</audio>

#### Saying 'Two'

<audio controls="controls">
  Boy to Woman (source)
  <source type="audio/wav" src="./conversion_results/B2W_S2(two).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Boy to Woman (target)
  <source type="audio/wav" src="./conversion_results/B2W_T2(two).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Boy to Woman (predict)
  <source type="audio/wav" src="./conversion_results/B2W_P2(two).wav"></source>
  <p>predict.</p>
</audio>

#### Saying 'Four'

<audio controls="controls">
  Boy to Woman (source)
  <source type="audio/wav" src="./conversion_results/B2W_S3(four).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Boy to Woman (target)
  <source type="audio/wav" src="./conversion_results/B2W_T3(four).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Boy to Woman (predict)
  <source type="audio/wav" src="./conversion_results/B2W_P3(four).wav"></source>
  <p>predict.</p>
</audio>

#### Saying 'Eight'

<audio controls="controls">
  Boy to Woman (source)
  <source type="audio/wav" src="./conversion_results/B2W_S4(eight).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Boy to Woman (target)
  <source type="audio/wav" src="./conversion_results/B2W_T4(eight).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Boy to Woman (predict)
  <source type="audio/wav" src="./conversion_results/B2W_P4(eight).wav"></source>
  <p>predict.</p>
</audio>

### Source: Boy, Target: Girl, Result: Converted Girl

#### Saying 'Two'

<audio controls="controls">
  Boy to Girl (source)
  <source type="audio/wav" src="./conversion_results/B2G_S1(two).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Boy to Girl (target)
  <source type="audio/wav" src="./conversion_results/B2G_T1(two).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Boy to Girl (predict)
  <source type="audio/wav" src="./conversion_results/B2G_P1(two).wav"></source>
  <p>predict.</p>
</audio>

#### Saying 'Five'

<audio controls="controls">
  Boy to Girl (source)
  <source type="audio/wav" src="./conversion_results/B2G_S2(five).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Boy to Girl (target)
  <source type="audio/wav" src="./conversion_results/B2G_T2(five).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Boy to Girl (predict)
  <source type="audio/wav" src="./conversion_results/B2G_P2(five).wav"></source>
  <p>predict.</p>
</audio>

#### Saying 'Eight'

<audio controls="controls">
  Boy to Girl (source)
  <source type="audio/wav" src="./conversion_results/B2G_S3(eight).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Boy to Girl (target)
  <source type="audio/wav" src="./conversion_results/B2G_T3(eight).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Boy to Girl (predict)
  <source type="audio/wav" src="./conversion_results/B2G_P3(eight).wav"></source>
  <p>predict.</p>
</audio>

#### Saying 'Zero'

<audio controls="controls">
  Boy to Girl (source)
  <source type="audio/wav" src="./conversion_results/B2G_S4(zero).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Boy to Girl (target)
  <source type="audio/wav" src="./conversion_results/B2G_T4(zero).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Boy to Girl (predict)
  <source type="audio/wav" src="./conversion_results/B2G_P4(zero).wav"></source>
  <p>predict.</p>
</audio>

## Third domain voice : Woman

### Source: Woman, Target: Man, Result: Converted Man

#### Saying 'One'

<audio controls="controls">
  Woman to Man (source)
  <source type="audio/wav" src="./conversion_results/W2M_S1(one).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Woman to Man (target)
  <source type="audio/wav" src="./conversion_results/W2M_T1(one).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Woman to Man (predict)
  <source type="audio/wav" src="./conversion_results/W2M_P1(one).wav"></source>
  <p>predict.</p>
</audio>

#### Saying 'Two'

<audio controls="controls">
  Woman to Man (source)
  <source type="audio/wav" src="./conversion_results/W2M_S2(two).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Woman to Man (target)
  <source type="audio/wav" src="./conversion_results/W2M_T2(two).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Woman to Man (predict)
  <source type="audio/wav" src="./conversion_results/W2M_P2(two).wav"></source>
  <p>predict.</p>
</audio>

#### Saying 'Three'

<audio controls="controls">
  Woman to Man (source)
  <source type="audio/wav" src="./conversion_results/W2M_S3(three).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Woman to Man (target)
  <source type="audio/wav" src="./conversion_results/W2M_T3(three).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Woman to Man (predict)
  <source type="audio/wav" src="./conversion_results/W2M_P3(three).wav"></source>
  <p>predict.</p>
</audio>

#### Saying 'Nine'

<audio controls="controls">
  Woman to Man (source)
  <source type="audio/wav" src="./conversion_results/W2M_S4(nine).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Woman to Man (target)
  <source type="audio/wav" src="./conversion_results/W2M_T4(nine).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Woman to Man (predict)
  <source type="audio/wav" src="./conversion_results/W2M_P4(nine).wav"></source>
  <p>predict.</p>
</audio>

### Source: Woman, Target: Boy, Result: Converted Boy

#### Saying 'Four'

<audio controls="controls">
  Woman to Boy (source)
  <source type="audio/wav" src="./conversion_results/W2B_S1(four).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Woman to Boy (target)
  <source type="audio/wav" src="./conversion_results/W2B_T1(four).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Woman to Boy (predict)
  <source type="audio/wav" src="./conversion_results/W2B_P1(four).wav"></source>
  <p>predict.</p>
</audio>

#### Saying 'Six'

<audio controls="controls">
  Woman to Boy (source)
  <source type="audio/wav" src="./conversion_results/W2B_S2(six).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Woman to Boy (target)
  <source type="audio/wav" src="./conversion_results/W2B_T2(six).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Woman to Boy (predict)
  <source type="audio/wav" src="./conversion_results/W2B_P2(six).wav"></source>
  <p>predict.</p>
</audio>

#### Saying 'Nine'

<audio controls="controls">
  Woman to Boy (source)
  <source type="audio/wav" src="./conversion_results/W2B_S3(nine).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Woman to Boy (target)
  <source type="audio/wav" src="./conversion_results/W2B_T3(nine).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Woman to Boy (predict)
  <source type="audio/wav" src="./conversion_results/W2B_P3(nine).wav"></source>
  <p>predict.</p>
</audio>

#### Saying 'Zero'

<audio controls="controls">
  Woman to Boy (source)
  <source type="audio/wav" src="./conversion_results/W2B_S4(zero).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Woman to Boy (target)
  <source type="audio/wav" src="./conversion_results/W2B_T4(zero).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Woman to Boy (predict)
  <source type="audio/wav" src="./conversion_results/W2B_P4(zero).wav"></source>
  <p>predict.</p>
</audio>

### Source: Woman, Target: Girl, Result: Converted Girl

#### Saying 'Four'

<audio controls="controls">
  Woman to Girl (source)
  <source type="audio/wav" src="./conversion_results/W2G_S1(four).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Woman to Girl (target)
  <source type="audio/wav" src="./conversion_results/W2G_T1(four).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Woman to Girl (predict)
  <source type="audio/wav" src="./conversion_results/W2G_P1(four).wav"></source>
  <p>predict.</p>
</audio>

#### Saying 'Five'

<audio controls="controls">
  Woman to Girl (source)
  <source type="audio/wav" src="./conversion_results/W2G_S2(five).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Woman to Girl (target)
  <source type="audio/wav" src="./conversion_results/W2G_T2(five).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Woman to Girl (predict)
  <source type="audio/wav" src="./conversion_results/W2G_P2(five).wav"></source>
  <p>predict.</p>
</audio>

#### Saying 'Six'

<audio controls="controls">
  Woman to Girl (source)
  <source type="audio/wav" src="./conversion_results/W2G_S3(six).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Woman to Girl (target)
  <source type="audio/wav" src="./conversion_results/W2G_T3(six).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Woman to Girl (predict)
  <source type="audio/wav" src="./conversion_results/W2G_P3(six).wav"></source>
  <p>predict.</p>
</audio>

#### Saying 'Zero'

<audio controls="controls">
  Woman to Girl (source)
  <source type="audio/wav" src="./conversion_results/W2G_S4(zero).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Woman to Girl (target)
  <source type="audio/wav" src="./conversion_results/W2G_T4(zero).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Woman to Girl (predict)
  <source type="audio/wav" src="./conversion_results/W2G_P4(zero).wav"></source>
  <p>predict.</p>
</audio>

## Fourth domain voice : Man

### Source: Man, Target: Woman, Result: Converted Woman

#### Saying 'Three'

<audio controls="controls">
  Man to Woman (source)
  <source type="audio/wav" src="./conversion_results/M2W_S1(three).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Man to Woman (target)
  <source type="audio/wav" src="./conversion_results/M2W_T1(three).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Man to Woman (predict)
  <source type="audio/wav" src="./conversion_results/M2W_P1(three).wav"></source>
  <p>predict.</p>
</audio>

#### Saying 'Five'

<audio controls="controls">
  Man to Woman (source)
  <source type="audio/wav" src="./conversion_results/M2W_S2(five).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Man to Woman (target)
  <source type="audio/wav" src="./conversion_results/M2W_T2(five).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Man to Woman (predict)
  <source type="audio/wav" src="./conversion_results/M2W_P2(five).wav"></source>
  <p>predict.</p>
</audio>

#### Saying 'Seven'

<audio controls="controls">
  Man to Woman (source)
  <source type="audio/wav" src="./conversion_results/M2W_S3(seven).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Man to Woman (target)
  <source type="audio/wav" src="./conversion_results/M2W_T3(seven).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Man to Woman (predict)
  <source type="audio/wav" src="./conversion_results/M2W_P3(seven).wav"></source>
  <p>predict.</p>
</audio>

#### Saying 'Oh'

<audio controls="controls">
  Man to Woman (source)
  <source type="audio/wav" src="./conversion_results/M2W_S4(oh).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Man to Woman (target)
  <source type="audio/wav" src="./conversion_results/M2W_T4(oh).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Man to Woman (predict)
  <source type="audio/wav" src="./conversion_results/M2W_P4(oh).wav"></source>
  <p>predict.</p>
</audio>

### Source: Man, Target: Boy, Result: Converted Boy

#### Saying 'One'

<audio controls="controls">
  Man to Boy (source)
  <source type="audio/wav" src="./conversion_results/M2B_S1(one).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Man to Boy (target)
  <source type="audio/wav" src="./conversion_results/M2B_T1(one).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Man to Boy (predict)
  <source type="audio/wav" src="./conversion_results/M2B_P1(one).wav"></source>
  <p>predict.</p>
</audio>

#### Saying 'Three'

<audio controls="controls">
  Man to Boy (source)
  <source type="audio/wav" src="./conversion_results/M2B_S2(three).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Man to Boy (target)
  <source type="audio/wav" src="./conversion_results/M2B_T2(three).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Man to Boy (predict)
  <source type="audio/wav" src="./conversion_results/M2B_P2(three).wav"></source>
  <p>predict.</p>
</audio>

#### Saying 'Six'

<audio controls="controls">
  Man to Boy (source)
  <source type="audio/wav" src="./conversion_results/M2B_S3(six).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Man to Boy (target)
  <source type="audio/wav" src="./conversion_results/M2B_T3(six).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Man to Boy (predict)
  <source type="audio/wav" src="./conversion_results/M2B_P3(six).wav"></source>
  <p>predict.</p>
</audio>

#### Saying 'Seven'

<audio controls="controls">
  Man to Boy (source)
  <source type="audio/wav" src="./conversion_results/M2B_S4(seven).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Man to Boy (target)
  <source type="audio/wav" src="./conversion_results/M2B_T4(seven).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Man to Boy (predict)
  <source type="audio/wav" src="./conversion_results/M2B_P4(seven).wav"></source>
  <p>predict.</p>
</audio>

### Source: Man, Target: Girl, Result: Converted Girl

#### Saying 'Three'

<audio controls="controls">
  Man to Girl (source)
  <source type="audio/wav" src="./conversion_results/M2G_S1(three).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Man to Girl (target)
  <source type="audio/wav" src="./conversion_results/M2G_T1(three).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Man to Girl (predict)
  <source type="audio/wav" src="./conversion_results/M2G_P1(three).wav"></source>
  <p>predict.</p>
</audio>

#### Saying 'Five'

<audio controls="controls">
  Man to Girl (source)
  <source type="audio/wav" src="./conversion_results/M2G_S2(five).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Man to Girl (target)
  <source type="audio/wav" src="./conversion_results/M2G_T2(five).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Man to Girl (predict)
  <source type="audio/wav" src="./conversion_results/M2G_P2(five).wav"></source>
  <p>predict.</p>
</audio>

#### Saying 'Oh'

<audio controls="controls">
  Man to Girl (source)
  <source type="audio/wav" src="./conversion_results/M2G_S3(oh).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Man to Girl (target)
  <source type="audio/wav" src="./conversion_results/M2G_T3(oh).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Man to Girl (predict)
  <source type="audio/wav" src="./conversion_results/M2G_P3(oh).wav"></source>
  <p>predict.</p>
</audio>

#### Saying 'Zero'

<audio controls="controls">
  Man to Girl (source)
  <source type="audio/wav" src="./conversion_results/M2G_S4(zero).wav"></source>
  <p>source.</p>
</audio>

<audio controls="controls">
  Man to Girl (target)
  <source type="audio/wav" src="./conversion_results/M2G_T4(zero).wav"></source>
  <p>target.</p>
</audio>

<audio controls="controls">
  Man to Girl (predict)
  <source type="audio/wav" src="./conversion_results/M2G_P4(zero).wav"></source>
  <p>predict.</p>
</audio>

--------------------------------------------------------------------------------------
