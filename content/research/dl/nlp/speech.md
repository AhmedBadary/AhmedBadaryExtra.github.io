---
layout: NotesPage
title: ASR <br /> Automatic Speech Recognition
permalink: /work_files/research/dl/nlp/speech
prevLink: /work_files/research/dl/nlp.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Introduction to Speech Recognition](#content8)
  {: .TOC8}
  * [The Methods and Models of Speech Recognition](#content9)
  {: .TOC9}
  * [Transitioning into Deep Learning](#content1)
  {: .TOC1}
  * [Connectionist Temporal Classification](#content2)
  {: .TOC2}
  * [LAS - Seq2Seq with Attention](#content3)
  {: .TOC3}
  * [Online Seq2Seq Models](#content4)
  {: .TOC4}
  * [Real-World Applications](#content6)
  {: .TOC6}
  * [Building ASR Systems](#content11)
  {: .TOC11}
</div>

***
***

<button>ASR Youtube Tutorials</button>{: .showText value="show" onclick="showTextPopHide(event);"}
- [How to Make a Simple Tensorflow Speech Recognizer - YouTube](https://www.youtube.com/watch?v=u9FPqkuoEJ8&t=0s)
- [Almost Unsupervised Text to Speech and Automatic Speech Recognition - YouTube](https://www.youtube.com/watch?v=UXpHzPrDJ2w&t=0s)
- [13. Speech Recognition with Convolutional Neural Networks in Keras/TensorFlow (2019) - YouTube](https://www.youtube.com/watch?v=Qf4YJcHXtcY&t=0s)
- [TensorFlow and Neural Networks for Speech Recognition - YouTube](https://www.youtube.com/watch?v=0y4LaZbdGvQ&t=0s)
- [DSP Background - Deep Learning for Audio Classification p.1 - YouTube](https://www.youtube.com/watch?v=Z7YM-HAz-IY&t=0s)
- [The PyTorch-Kaldi Toolkit - YouTube](https://www.youtube.com/watch?v=VDQaf0SS4K0&t=0s)
- [Almost Unsupervised Text to Speech and Automatic Speech Recognition](https://arxiv.org/pdf/1905.06791.pdf)  
{: hidden=""}


## Introduction to Speech
{: #content8}

1. **Probabilistic Speech Recognition:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents81}  
    :   Statistical ASR has been introduced/framed by __Frederick Jelinek__ in his famous paper [Continuous Speech Recognition by Statistical Methods](http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=1454428) who framed the problem as an _information theory_ problem.  
    :   We can view the problem of __ASR__ as a __*sequence labeling*__ problem, and, so, use statistical models (such as HMMs) to model the conditional probabilities between the states/words by viewing speech signal as a piecewise stationary signal or a short-time stationary signal. 
    :   * __Representation__: we _represent_ the _speech signal_ as an *__observation sequence__* $$o = \{o_t\}$$  
        * __Goal__: find the most likely _word sequence_ $$\hat{w}$$   
        * __Set-Up__:  
            * The system has a set of discrete states
            * The transitions from state to state are markovian and are according to the transition probabilities  
                > __Markovian__: Memoryless  
            * The _Acoustic Observations_ when making a transition are conditioned on _the state alone_ $$P(o_t \vert c_t)$$
            * The _goal_ is to _recover the state sequence_ and, consequently, the _word sequence_  

2. **Speech Problems and Considerations:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents82}  
    :   * __ASR__:  
            * _Spontaneous_ vs _Read_ speech
            * _Large_ vs _Small_ Vocabulary
            * _Continuous_ vs _Isolated_ Speech  
                > Continuous Speech is harder due to __*Co-Articulation*__   
            * _Noisy_ vs _Clear_ input
            * _Low_ vs _High_ Resources 
            * _Near-field_ vs _Far-field_ input
            * _Accent_-independence 
            * _Speaker-Adaptive_ vs _Stand-Alone_ (speaker-independent) 
            * The cocktail party problem 
        * __TTS__:  
            * Low Resource
            * Realistic prosody
        * __Speaker Identification__
        * __Speech Enhancement__
        * __Speech Separation__       

3. **Acoustic Representation:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents83}  
    :   __What is speech?__{: style="color: red"}  
        * Waves of changing air pressure - Longitudinal Waves (consisting of compressions and rarefactions)
        * Realized through excitation from the vocal cords
        * Modulated by the vocal tract and the articulators (tongue, teeth, lips) 
        * Vowels are produced with an open vocal tract (stationary)
            > parametrized by position of tongue
        * Consonants are constrictions of vocal tract
        * They get __converted__ to _Voltage_ with a microphone
        * They are __sampled__ (and quantized) with an _Analogue to Digital Converter_ 
    :   __Speech as waves:__{: style="color: red"}  
        * Human hearing range is: $$~50 HZ-20 kHZ$$
        * Human speech range is: $$~85 HZ-8 kHZ$$
        * Telephone speech sampling is $$8 kHz$$ and a bandwidth range of $$300 Hz-4 kHz$$ 
        * 1 bit per sample is intelligible
        * Contemporary Speech Processing mostly around 16 khz 16 bits/sample  
            > A lot of data to handle
    :   __Speech as digits (vectors):__{: style="color: red"}  
        * We seek a *__low-dimensional__* representation to ease the computation  
        * The low-dimensional representation needs to be __invariant to__:  
            * Speaker
            * Background noise
            * Rate of Speaking
            * etc.
        * We apply __Fourier Analysis__ to see the energy in different frequency bands, which allows analysis and processing
            * Specifically, we apply _windowed short-term_ *__Fast Fourier Transform (FFT)__*  
                > e.g. FFT on overlapping $$25ms$$ windows (400 samples) taken every $$10ms$$  
        ![img](/main_files/dl/nlp/12/16.png){: width="70%"}  
        > Each frame is around 25ms of speech  
        * FFT is still too high-dimensional  
            * We __Downsample__ by local weighted averages on _mel scale_ non-linear spacing, an d take a log:  
                $$ m = 1127 \ln(1+\dfrac{f}{700})$$  
            * This results in *__log-mel features__*, $$40+$$ dimensional features per frame    
                > Default for NN speech modelling  
    :   __Speech dimensionality for different models:__{: style="color: red"}  
        * __Gaussian Mixture Models (GMMs)__: 13 *__MFCCs__*  
            * *__MFCCs - Mel Frequency Cepstral Coefficients__*: are the discrete cosine transformation (DCT) of the mel filterbank energies \| Whitened and low-dimensional.  
                They are similar to _Principle Components_ of log spectra.  
            __GMMs__ used local differences (deltas) and second-order differences (delta-deltas) to capture the dynamics of the speech $$(13 \times 3 \text{ dim})$$
        * __FC-DNN__: 26 stacked frames of *__PLP__*  
            * *__PLP - Perceptual Linear Prediction__*: a common alternative representation using _Linear Discriminant Analysis (LDA)_  
                > Class aware __PCA__    
        * __LSTM/RNN/CNN__: 8 stacked frames of *__PLP__*  
    :   __Speech as Communication:__{: style="color: red"}      
        * Speech Consists of sentences (in ASR we usually talk about "utterances")  
        * Sentences are composed of words 
        * Minimal unit is a "phoneme" Minimal unit that distinguishes one word from another.
            * Set of 40-60 distinct sounds.
            * Vary per language 
            * Universal representations: 
                * *__IPA__* : international phonetic alphabet
                * *__X-SAMPA__* : (ASCII) 
        * *__Homophones__* : distinct words with the same pronunciation. (e.g. "there" vs "their") 
        * *__Prosody__* : How something is said can convey meaning. (e.g. "Yeah!" vs "Yeah?")  

9. **Microphones and Speakers:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents89}  
    :   * __Microphones__:  
            * Their is a _Diaphragm_ in the Mic
            * The Diaphragm vibrates with air pressure
            * The diaphragm is connected to a magnet in a coil
            * The magnet vibrates with the diaphragm
            * The coil has an electric current induced by the magnet based on the vibrations of the magnet
    :   * __Speakers__:  
            * The electric current flows from the sound-player through a wire into a coil
            * The coil has a metal inside it
            * The metal becomes magnetic and vibrates inside the coil based on the intensity of the current 
            * The magnetized metal is attached to a cone that produces the sound


4. **(Approximate) History of ASR:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents84}  
    * 1960s Dynamic Time Warping 
    * 1970s Hidden Markov Models 
    * Multi-layer perceptron 1986 
    * Speech recognition with neural networks 1987-1995 
    * Superseded by GMMs 1995-2009 
    * Neural network features 2002— 
    * Deep networks 2006— (Hinton, 2002) 
    * Deep networks for speech recognition:
        * Good results on TIMIT (Mohamed et al., 2009) 
        * Results on large vocabulary systems 2010 (Dahl et al., 2011) * Google launches DNN ASR product 2011
        * Dominant paradigm for ASR 2012 (Hinton et al., 2012) 
    * Recurrent networks for speech recognition 1990, 2012 - New models (CTC attention, LAS, neural transducer) 

5. **Datasets:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents85}  
    * __TIMIT__: 
        * Hand-marked phone boundaries are given 
        * 630 speakers $$\times$$ 10 utterances 
    * __Wall Street Journal (WSJ)__ 1986 Read speech. WSJO 1991, 30k vocab 
    * __Broadcast News (BN)__ 1996 104 hours 
    * __Switchboard (SWB)__ 1992. 2000 hours spontaneous telephone speech -  500 speakers 
    * __Google voice search__ - anonymized live traffic 3M utterances 2000 hours hand-transcribed 4M vocabulary. Constantly refreshed, synthetic reverberation + additive noise 
    * __DeepSpeech__ 5000h read (Lombard) speech + SWB with additive noise. 
    * __YouTube__ 125,000 hours aligned captions (Soltau et al., 2016) 

5. **Development:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents85}  
    ![img](/main_files/dl/nlp/12/17.png){: width="75%"}    

*** 

## The Methods and Models of Speech Recognition
{: #content9}

1. **Probabilistic Speech Recognition:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents91}  
    :   Statistical ASR has been introduced/framed by __Frederick Jelinek__ in his famous paper [Continuous Speech Recognition by Statistical Methods](http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=1454428) who framed the problem as an _information theory_ problem.  
    :   We can view the problem of __ASR__ as a _sequence labeling_ problem, and, so, use statistical models (such as HMMs) to model the conditional probabilities between the states/words by viewing speech signal as a piecewise stationary signal or a short-time stationary signal. 
    :   * __Representation__: we _represent_ the _speech signal_ as an *__observation sequence__* $$o = \{o_t\}$$  
        * __Goal__: find the most likely _word sequence_ $$\hat{w}$$   
        * __Set-Up__:  
            * The system has a set of discrete states
            * The transitions from state to state are markovian and are according to the transition probabilities  
                > __Markovian__: Memoryless  
            * The _Acoustic Observations_ when making a transition are conditioned on _the state alone_ $$P(o_t \vert c_t)$$
            * The _goal_ is to _recover the state sequence_ and, consequently, the _word sequence_  
                
2. **Fundamental Equation of Speech Recognition:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents92}  
    :   We set the __decoders output__ as the *__most likely sequence__* $$\hat{w}$$ from all the possible sequences, $$\mathcal{S}$$, for an observation sequence $$o$$:  
    :   $$\begin{align}
            \hat{w} & = \mathrm{arg } \max_{w \in \mathcal{S}} P(w \vert o) & (1) \\
            & = \mathrm{arg } \max_{w \in \mathcal{S}} P(o \vert w) P(w) & (2)
            \end{align}
        $$  
    :   The __Conditional Probability of a sequence of observations given a sequence of (predicted) word__ is a _product (or sum of logs)_ of an __Acoustic Model__ ($$p(o \vert w)$$)  and a __Language Model__ ($$p(w)$$)  scores.
    :   The __Acoustic Model__ can be written as the following product:    
    :   $$P(o \vert w) = \sum_{d,c,p} P(o \vert c) P(c \vert p) P(p \vert w)$$ 
    :   where $$p$$ is the __phone sequence__ and $$c$$ is the __state sequence__.  

3. **Speech Recognition as Transduction:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents93}  
    :   The problem of speech recognition can be seen as a transduction problem - mapping different forms of energy to other forms (representations).  
        Basically, we are going from __Signal__ to __Language__.  
        ![img](/main_files/dl/nlp/12/6.png){: width="60%"}    

4. **Gaussian Mixture Models:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents94}  
    :   * Dominant paradigm for ASR from 1990 to 2010 
        * Model the probability distribution of the acoustic features for each state.  
            $$P(o_t \vert c_i) = \sum_j w_{ij} N(o_t; \mu_{ij}, \sigma_{ij})$$   
        * Often use diagonal covariance Gaussians to keep number of parameters under control. 
        * Train by the E-M (Expectation Maximization) algorithm (Dempster et al., 1977) alternating:  
            * __M__: forced alignment computing the maximum-likelihood state sequence for each utterance 
            * __E__: parameter $$(\mu , \sigma)$$ estimation  
        * Complex training procedures to incrementally fit increasing numbers of components per mixture:  
            * More components, better fit - 79 parameters component. 
        * Given an alignment mapping audio frames to states, this is parallelizable by state.   
        * Hard to share parameters/data across states.  
    :   __Forced Alignment:__  
        * Forced alignment uses a model to compute the maximum likelihood alignment between speech features and phonetic states. 
        * For each training utterance, construct the set of phonetic states for the ground truth transcription. 
        * Use Viterbi algorithm to find ML monotonic state sequence 
        * Under constraints such as at least one frame per state. 
        * Results in a phonetic label for each frame. 
        * Can give hard or soft segmentation.  
        ![img](/main_files/dl/nlp/12/7.png){: width="60%"}  
    * <button>Algorithm/Training</button>{: .showText value="show"
     onclick="showTextPopHide(event);"}
    ![formula](/main_files/dl/nlp/12/8.png){: width="70%" hidden=""}   
    * __Decoding:__   
        ![img](/main_files/dl/nlp/12/9.png){: width="20%"}  
        * Speech recognition Unfolds in much the same way.
        *  Now we have a graph instead of a straight-through path.
        *  Optional silences between words Alternative pronunciation paths.
        *  Typically use max probability, and work in the log domain.
        *  Hypothesis space is huge, so we only keep a "beam" of the best paths, and can lose what would end up being the true best path.   

5. **Neural Networks in ASR:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents95}  
    :   * __Two Paradigms of Neural Networks for Speech__:  
            * Use neural networks to compute nonlinear feature representations:      
                * "Bottleneck" or "tandem" features (Hermansky et al., 2000)
                * Low-dimensional representation is modelled conventionally with GMMs.
                * Allows all the GMM machinery and tricks to be exploited. 
                * _Bottleneck features_ outperform _Posterior features_ (Grezl et al. 2017)
                * Generally, __DNN features + GMMs__ reach the same performance as hybrid __DNN-HMM__ systems but are much more _complex_
            * Use neural networks to estimate phonetic unit probabilities  

6. **Hybrid Networks:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents96}  
    :   * Train the network as a classifier with a softmax across the __phonetic units__  
        * Train with __cross-entropy__
        * Softmax:   
    :   $$y(i) = \dfrac{e^{\psi(i, \theta)}}{\sum_{j=1}^N e^{\psi(j, \theta)}}$$ 
    :   * We _converge to/learn_ the __posterior probability across phonetic states__:  
    :   $$P(c_i \vert o_t)$$   
    :   * We, then, model $$P(o \vert c)$$ with a __Neural-Net__ instead of a __GMM__:   
            > We can ignore $$P(o_t)$$ since it is the same for all decoding paths   
    :   $$\begin{align}
            P(o \vert c) & = \prod_t P(o_t \vert c_t) & (3) \\
            P(o_t \vert c_t) & = \dfrac{P(c_t \vert o_t) P(o_t)}{P(c_t)} & (4) \\
            & \propto \dfrac{P(c_t \vert o_t)}{P(c_t)} & (5) \\
            \end{align}
        $$  
    :   * The __log scaled posterior__  from the last term:  
    :   $$\log P(o_t \vert c_t) = \log P(c_t \vert o_t) - \alpha \log P(c_t)$$ 
    :   * Empirically, a *__prior smoothing__* on $$\alpha$$ $$(\alpha \approx 0.8)$$ works better 
    :   * __Input Features__:  
            * NN can handle high-dimensional, correlated, features
            * Use (26) stacked filterbank inputs (40-dim mel-spaced filterbanks)
    :   * __NN Architectures for ASR__:  
            * *__Fully-Connected DNN__*  
            * *__CNNs__*: 
                * Time delay neural networks: 
                    * Waibel et al. (1989) 
                    * Dilated convolutions (Peddinti et al., 2015)  
                        > Pooling in time results in a loss of information.  
                        > Pooling in frequency domain is more tolerable  
                * CNNs in time or frequency domain:
                    * Abdel-Hamid et al. (2014)
                    * Sainath et al. (2013) 
                * Wavenet (van den Oord et al., 2016) 
            * *__RNNs__* :  
                * RNN (Robinson and Fallside, 1991) 
                * LSTM Graves et al. (2013)
                * Deep LSTM-P Sak et al. (2014b)
                * CLDNN (Sainath et al , 2015a)
                * GRU. DeepSpeech 1/2 (Amodei et al., 2015)

                * __Tips__ :
                    * Bidirectional (Schuster and Paliwal, 1997) helps, but introduces latency. 
                    * Dependencies not long at speech frame rates (100Hz).
                    * Frame stacking and down-sampling help. 

7. **Sequence Discriminative Training:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents97}  
    ![img](/main_files/dl/nlp/12/11.png){: width="80%"}  
    * Conventional training uses Cross-Entropy loss — Tries to maximize probability of the true state sequence given the data. 
    * We care about Word Error Rate of the complete system. 
    * Design a loss that's differentiable and closer to what we care about. 
    * Applied to neural networks (Kingsbury, 2009) 
    * Posterior scaling gets learnt by the network. 
    * Improves conventional training and CTC by $$\approx 15%$$ relative. 
    * bMMI, sMBR(Povey et al., 2008)  
    ![img](/main_files/dl/nlp/12/10.png){: width="70%"}  


8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents98}  
    :   

***

## Transitioning into Deep Learning
{: #content1}  

1. **Classical Approach:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    :   Classically, _Speech Recognition_ was developed as a big machine incorporating different models from different fields.  
        The models were _statistical_ and they started from _text sequences_ to _audio features_.  
        Typically, a _generative language model_ is trained on the sentences for the intended language, then, to make the features, _pronunciation models_, _acoustic models_, and _speech processing models_ had to be developed. Those required a lot of feature engineering and a lot of human intervention and expertise and were very fragile.
    :   ![img](/main_files/dl/nlp/12/1.png){: width="100%"}  
    :   __Recognition__ was done through __*Inference*__: Given audio features $$\mathbf{X}=x_1x_2...x_t$$ infer the most likely tedxt sequence $$\mathbf{Y}^\ast=y_1y_2...y_k$$ that caused the audio features.
    :   $$\displaystyle{\mathbf{Y}^\ast =\mathrm{arg\,min}_{\mathbf{Y}} p(\mathbf{X} \vert \mathbf{Y}) p(\mathbf{Y})}$$

2. **The Neural Network Age:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    :   Researchers realized that each of the (independent) components/models that make up the ASR can be improved if it were replaced by a _Neural Network Based Model_.  
    :   ![img](/main_files/dl/nlp/12/2.png){: width="100%"}  

3. **The Problem with the component-based System:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    :   * Each component/model is trained _independently_, with a different _objective_  
        * Errors in one component may not behave well with errors in another component

4. **Solution to the Component-Based System:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    :   We aim to train models that encompass all of these components together, i.e. __End-to-End Model__:  
        * __Connectionist Temporal Classification (CTC)__
        * __Sequence-to-Sequence Listen Attend and Spell (LAS)__
                    
5. **End-to-End Speech Recognition:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  
    :   We treat __End-to-End Speech Recognition__ as a _modeling task_.
    :   Given __Audio__ $$\mathbf{X}=x_1x_2...x_t$$ (audio/processed spectogram) and corresponding output text $$\mathbf{Y}=y_1y_2...y_k$$  (transcript), we want to learn a *__Probabilistic Model__* $$p(\mathbf{Y} \vert \mathbf{X})$$ 

6. **Deep Learning - What's new?**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}  
    :    * __Algorithms__:  
            * Direct modeling of context-dependent (tied triphone states) through the DNN  
            * Unsupervised Pre-training
            * Deeper Networks
            * Better Architectures  
        * __Data__:  
            * Larger Data
        * __Computation__:  
                * GPUs
                * TPUs
        * __Training Criterion__:  
            * Cross-Entropy -> MMI Sequence -level
        * __Features__:  
            * Mel-Frequency Cepstral Coefficients (MFCC) -> FilterBanks
        * __Training and Regularization__:  
            * Batch Norm
            * Distributed SGD
            * Dropout
        * __Acoustic Modelling__:  
            * CNN
            * CTC
            * CLDNN
        * __Language Modelling__:  
            * RNNs
            * LSTM
        * __DATA__:  
            * More diverse - Noisy, Accents, etc.  

***

## Connectionist Temporal Classification
{: #content2}

1. **Motivation:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    :   * RNNs require a _target output_ at each time step 
        * Thus, to train an RNN, we need to __segment__ the training output (i.e. tell the network which label should be output at which time-step) 
        * This problem usually arises when the timing of the input is variable/inconsistent (e.g. people speaking at different rates/speeds)

2. **Connectionist Temporal Classification (CTC):**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}  
    :   __CTC__ is a type of _neural network output_ and _associated scoring function_, for training recurrent neural networks (RNNs) such as LSTM networks to tackle sequence problems where the _timing is variable_.  
    :   Due to time variability, we don't know the __alignment__ of the __input__ with the __output__.  
        Thus, CTC considers __all possible alignments__.  
        Then, it gets a __closed formula__ for the __probability__ of __all these possible alignments__ and __maximizes__ it.

8. **Structure:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents28}  
    * __Input__:  
        A sequence of _observations_
    * __Output__:  
        A sequence of _labels_


3. **Algorithm:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}  
   ![img](/main_files/dl/nlp/12/3.png){: width="80%"}  
    1. Extract the (*__LOG MEL__*) _Spectrogram_ from the input  
        > Use raw audio iff there are multiple microphones
    2. Feed the _Spectogram_ into a _(bi-directional) RNN_
    3. At each frame, we apply a _softmax_ over the entire vocabulary that we are interested in (plus a _blank token_), producing a prediction _log probability_ (called the __score__) for a _different token class_ at that time step.   
        * Repeated Tokens are duplicated
        * Any original transcript is mapped to by all the possible paths in the duplicated space
        * The __Score (log probability)__ of any path is the sum of the scores of individual categories at the different time steps
        * The probability of any transcript is the sum of probabilities of all paths that correspond to that transcript
        * __Dynamic Programming__ allopws is to compute the log probability $$p(\mathbf{Y} \vert \mathbf{X})$$ and its gradient exactly.  
    ![img](/main_files/dl/nlp/12/4.png){: width="80%"}  

10. **The Math:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents210}  
    :   Given a length $$T$$ input sequence $$x$$, the output vectors $$y_t$$ are normalized with the __Softmax__ function, then interpreted as the probability of emitting the label (or blank) with index $$k$$ at time $$t$$: 
    :   $$P(k, t \vert x) = \dfrac{e^{(y_t^k)}}{\sum_{k'} e^{(y_t^{k'})}}$$ 
    :   where $$y_t^k$$ is element $$k$$ of $$y_t$$.  
    :   A __CTC alignment__ $$a$$ is a length $$T$$ sequence of blank and label indices.  
        The probability $$P(a \vert x)$$ of 
        $$a$$ is the product of the emission probabilities at every time-step:  
    :   $$P(a \vert x) = \prod_{t=1}^T P(a_t, t \vert x)$$ 
    :   Denoting by $$\mathcal{B}$$ an operator that removes first the repeated labels, then the blanks from alignments, and observing that the total probability of an output transcription $$y$$ is equal to the sum of the probabilities of the alignments corresponding to it, we can write:  
    :   $$P(y \vert x) = \sum_{a \in \mathcal{B}^{-1}(y)} P(a \vert x)\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:(*)$$ 
    :   Given a target transcription $$y^\ast$$, the network can then be trained to minimise the __CTC objective function__:  
    :   $$\text{CTC}(x) = - \log P(y^\ast \vert x)$$ 


11. **Intuition:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents211}  
    :   The above 'integrating out' over possible alignments eq. $$(*)$$ is what allows the network to be trained with unsegmented data.   
        The intuition is that, because we don’t know where the labels within a particular transcription will occur, we sum over all the places where they could occur can be efficiently evaluated and differentiated using a dynamic programming algorithm.


5. **Analysis:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}  
    :   The _ASR_ model consists of an __RNN__ plus a __CTC__ layer.    
        Jointly, the model learns the __pronunciation__ and __acoustic__ model _together_.  
        However, a __language model__ is __not__ learned, because the RNN-CTC model makes __strong conditional independence__ assumptions (similar to __HMMs__).  
        Thus, the RNN-CTC model is capable of mapping _speech acoustics_ to _English characters_ but it makes many _spelling_ and _grammatical_ mistakes.  
        Thus, the bottleneck in the model is the assumption that the _network outputs_ at _different times_ are __conditionally independent__, given the _internal state_ of the network. 

4. **Improvements:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}  
    :   * Add a _language model_ to CTC during training time for _rescoring_.
           This allows the model to correct spelling and grammar.
        * Use _word targets_ of a certain vocabulary instead of characters 

7. **Applications:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents27}  
    :   * on-line Handwriting Recognition
        * Recognizing phonemes in speech audio  
        * ASR

9. **Tips:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents29}  
    :   * Continuous realignment - no need for a bootstrap model
        * Always use soft targets
        * Don't scale by the posterior
        * Produces similar results to conventional training
        * Simple to implement in the __FST__ framework 
        * CTC could learn to __delay__ output on its own in order to improve accuracy:  
            * In-practice, tends to align transcription closely
            * This is especially problematic for English letters (spelling)
            * __Sol__:  
                bake limited context into model structure; s.t. the model at time-step $$T$$ can see only some future frames. 
                * Caveat: may need to compute upper layers quickly after sufficient context arrives.  
                Can be easier if context is near top.   

***

## LAS - Seq2Seq with Attention
{: #content3}

1. **Motivation:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}  
    :   The __CTC__ model can only make predictions based on the data; once it has made a prediction for a given frame, it __cannot re-adjust__ the prediction.  
    :   Moreover, the _strong independence assumptions_ that the CTC model makes doesn't allow it to learn a _language model_.   

2. **Listen, Attend and Spell (LAS):**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}  
    :   __LAS__ is a neural network that learns to transcribe speech utterances to characters.  
        In particular, it learns all the components of a speech recognizer jointly.
    :   ![img](/main_files/dl/nlp/12/5.png){: width="80%"}  
    :   The model is a __seq2seq__ model; it learns a _conditional probability_ of the next _label/character_ given the _input_ and _previous predictions_ $$p(y_{i+1} \vert y_{1..i}, x)$$.  
    :   The approach that __LAS__ takes is similar to that of __NMT__.     
        Where, in translation, the input would be the _source sentence_ but in __ASR__, the input is _the audio sequence_.  
    :   __Attention__ is needed because in speech recognition tasks, the length of the input sequence is very large; for a 10 seconds sample, there will be ~10000 frames to go through.      

3. **Structure:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}  
    :   The model has two components:  
        * __A listener__: a _pyramidal RNN **encoder**_ that accepts _filter bank spectra_ as inputs
        * __A Speller__: an _attention_-based _RNN **decoder**_ that emits _characters_ as outputs 
    :   * __Input__:  
            
        * __Output__: 

6. **Limitations:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents36}  
    :   * Not an online model - input must all be received before transcripts can be produced
        * Attention is a computational bottleneck since every output token pays attention to every input time step
        * Length of input has a big impact on accuracy

***

## Online Seq2Seq Models
{: #content4}

1. **Motivation:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents41}  
    :   * __Overcome limitations of seq2seq__:  
            * No need to wait for the entire input sequence to arrive
            * Avoids the computational bottleneck of Attention over the entire sequence
        * __Produce outputs as inputs arrive__:  
            * Solves this problem: When has enough information arrived that the model is confident enough to output symbols 

2. **A Neural Transducer:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents42}  
    :    Neural Transducer is a more general class of seq2seq learning models. It avoids the problems of offline seq2seq models by operating on local chunks of data instead of the whole input at once. It is able to make predictions _conditioned on partially observed data and partially made predictions_.    


*** 

## Real-World Applications
{: #content6}

1. **Siri:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents61}  
    :   * __Siri Architecture__:  
            ![img](/main_files/dl/nlp/12/12.png){: width="80%"}  
            * Start with a __Wave Form__
            * Pass the wave form through an ASR system
            * Then use a Natural Language Model to re-adjust the labels
            * Output Words
            * Based on the output, do some action or save the output, etc.
    :   * __"Hey Siri" DNN__:  
            ![img](/main_files/dl/nlp/12/13.png){: width="80%"}  
            * Much smaller DNN than for the full Vocab. ASR
            * Does _Binary Classification_ - Did the speaker say "hey Siri" or not?  
            * Consists of 5 Layers
            * The layers have few parameters
            * It has a __Threshold__ at the end  
            * So fast 
            * Capable of running on the __Apple Watch!__
    :   * __Two-Pass Detection__:  
            * *__Problem__*:  
                    A big problem that arises in the _always-on voice_, is that it needs to run 24/7. 
            * *__Solution__*:  
                ![img](/main_files/dl/nlp/12/14.png){: width="90%"}    
                We use a __Two-Pass Detection__ system:  
                * There are two processors implemented in the phone:  
                    * __Low-Compute Processor:__{: style="color: red"}  
                        * Always __ON__
                        * Given a threshold value of confidence over binary probabilities the Processor makes the following decision: "Should I wake up the Main Processor"  
                        * Low power consumption
                    * __Main Processor:__{: style="color: red"}  
                        * Only ON if woken up by the _low-compute_ processor 
                        * Runs a much larger DNN   
                        * High power consumption
    :   * __Computation for DL__:   
            ![img](/main_files/dl/nlp/12/15.png){: width="90%"}  

***

## Building ASR Systems
{: #content11}

1. **Pre-Processing:**{: style="color: SteelBlue"}{: .bodyContents11 #bodyContents111}  
    :   A __Spectrogram__ is a visual representation of the spectrum of frequencies of sound or other signal as they vary with time.
        * Take a small window (~20 ms) of waveform  
        * Compute __FFT__ and take magnitude (i.e. prower)  
            > Describes Frequency content in local window  
    :   ![img](/main_files/dl/nlp/12/18.png){: width="80%"}  
    :   * Concatenate frames from adjacent windows to form the "spectrogram"  
        ![img](/main_files/dl/nlp/12/19.png){: width="80%"}  

2. **Acoustic Model:**{: style="color: SteelBlue"}{: .bodyContents11 #bodyContents112}  
    :   An __Acoustic Model__ is used in automatic speech recognition to represent the relationship between an audio signal and the phonemes or other linguistic units that make up speech.  
    :   __Goal__: create a neural network (DNN/RNN) from which we can extract transcriptions, $$y$$ - by training on labeled pairs $$(x, y^\ast)$$.  

3. **Network (example) Architecture:**{: style="color: SteelBlue"}{: .bodyContents11 #bodyContents113}  
    :   __RNN to predict graphemes (26 chars + space + blank)__:  
        * Spectrograms as inputs
        * 1 Layer of Convolutional Filters
        * 3 Layers of Gated Recurrent Units
            * 1000 Neurons per Layer
        * 1 Fully-Connected Layer to predict $$c$$
        * Batch Normalization
        * *__CTC__* __Loss Function__  (Warp-CTC) 
        * SGD+Nesterov Momentum Optimization/Training
        ![img](/main_files/dl/nlp/12/20.png){: width="50%"}  

4. **Incorporating a Language Model:**{: style="color: SteelBlue"}{: .bodyContents11 #bodyContents114}  
    :   Incorporating a Language Model helps the model learn:  
        * Spelling 
        * Grammar
        * Expand Vocabulary
    :   __Two Ways__:  
        1. Fuse the __Acoustic Model__ with the language model $$p(y)$$  
        2. Incorporate linguistic data: 
            * Predict Phonemes + Pronunciation Lexicon + LM  

5. **Decoding with Language Models:**{: style="color: SteelBlue"}{: .bodyContents11 #bodyContents115}  
    :   * Given a word-based LM of form $$p(w_{t+1} \vert w_{1:t})$$  
        * Use __Beam Search__ to maximize _(Hannun et al. 2014)_:  
    :   $$\mathrm{arg } \max_{w} p(w \vert x)\: p(w)^\alpha \: [\text{length}(w)]^\beta$$  
    :   > * $$p(w \vert x) = p(y \vert x)$$ for characters that make up $$w$$.  
        > * We tend to penalize long transcriptions due to the multiplicative nature of the objective, so we trade off (re-weight) with $$\alpha , \beta$$  
    :   * Start with a set of candidate transcript prefixes, $$A = {}$$  
        * __For $$t = 1 \ldots T$$__:   
            * __For Each Candidate in $$A$$, consider__:  
                1. Add blank; don't change prefix; update probability using the AM. 
                2. Add space to prefix; update probability using LM. 
                3. Add a character to prefix; update probability using AM. Add new candidates with updated probabilities to $$A_{\text{new}}$$   
            * $$A := K$$ most probable prefixes in $$A_{\text{new}}$$  
    :   <button>Algorithm Description</button>{: .showText value="show"
     onclick="showTextPopHide(event);"}
        ![formula](/main_files/dl/nlp/12/21.png){: width="100%" hidden=""}  

6. **Rescoring with Neural LM:**{: style="color: SteelBlue"}{: .bodyContents11 #bodyContents116}  
    :   The output from the RNN described above consists of a __big list__ of the __top $$k$$ transcriptions__ in terms of probability.  
        We want to re-score these probabilities based on a strong LM.   
        * It is Cheap to evaluate $$p(w_k \vert w_{k-1}, w_{k-2}, \ldots, w_1)$$ NLM on many sentences  
        * In-practice, often combine with N-gram trained from big corpora  

7. **Scaling Up:**{: style="color: SteelBlue"}{: .bodyContents11 #bodyContents117}  
    :   * __Data__:  
            * Transcribing speech data isn't cheap, but not prohibitive  
                * Roughly 50¢ to $1 per minute
            * Typical speech benchmarks offer 100s to few 1000s of hours:  
                * LibriSpeech (audiobooks)  
                * LDC corpora (Fisher, Switchboard, WSJ) ($$)  
                * VoxForge  
            * Data is very Application/Problem dependent and should be chosen with respect to the problem to be solved
            * Data can be collected as "read"-data for <$10 -- Make sure the data to be read is scripts/plays to get a conversationalist response
            * Noise is __additive__ and can be incorporated  
    :   * __Computation__:  
            * How big is 1 experiment?{: style="color: red"}  
                $$\geq (\# \text{Connections}) \cdot (\# \text{Frames}) \cdot (\# \text{Utterances}) \cdot (\# \text{Epochs}) \cdot 3 \cdot 2 \:\text{ FLOPs}$$   
                E.g. for DS2 with 10k hours of data:  
                $$100*10^6 * 100 * 10^6*20 * 3 * 2 = 1.2*10^{19} \:\text{ FLOPs}$$  
                ~30 days (with well-optimized code on Titan X)  
            * Work-arounds and solutions:{: style="color: red"}  
                * More GPUs with data parallelism:  
                    * Minibatches up to 1024 
                    * Aim for $$\geq 64$$ utterances per GPU 
                ~$$< 1$$-wk training time (~8 Titans)
            * How to use more GPUs?{: style="color: red"}  

                * Synch. SGD
                * Asynch SGD 
                * Synch SGD w/ backup workers
            * __Tips and Tricks__:  
                * Make sure the code is _optimized_ single-GPU.  
                    A lot of off-the-shelf code has inefficiencies.  
                    E.g. Watch for bad GEMM sizes.
                * Keep similar-length utterances together:  
                    The input must be block-sized and will be padded; thus, keeping similar lengths together reduces unnecessary padding.
    :   * __Throughput__:  
            * Large DNN/RNN models run well on GPUs, ONLY, if the batch size is high enough.  
                Processing 1 audio stream at a time is inefficient.  
                *__Performance for K1200 GPU__*:  
                | __Batch Size__ | __FLOPs__ | __Throughput__ |
                | 1 | 0.065 TFLOPs | 1x | 
                | 10 | 0.31 TFLOPs | 5x | 
                | 32 | 0.92 TFLOPs | 14x |  
            * Batch packets together as data comes in:  
                * Each packet (Arrow) of speech data ~ 100ms  
                    ![img](/main_files/dl/nlp/12/21.png){: width="80%"}  
                * Process packets that arrive at similar times in parallel (from    multiple users)  
                    ![img](/main_files/dl/nlp/12/22.png){: width="80%"}  