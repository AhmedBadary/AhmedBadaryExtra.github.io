---
layout: NotesPage
title: ASR <br /> Research Papers
permalink: /work_files/research/dl/nlp/speech_research
prevLink: /work_files/research/dl/nlp.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Deep Speech](#content1)
  {: .TOC1}
  * [Towards End-to-End Speech Recognition with Recurrent Neural Networks](#content2)
  {: .TOC2}
  * [Attention-Based Models for Speech Recognition](#content3)
  {: .TOC3}
  * [A Neural Transducer](#content4)
  {: .TOC4}
  * [Deep Speech 2](#content5)
  {: .TOC5}
  * [Listen, Attend and Spell (LAS)](#content6)
  {: .TOC6}
  * [State of the Art Speech Recognition w/ Sequence Modeling](#content7)
  {: .TOC7}
  * [Very Deep Convolutional Networks for End-To-End Speech Recognition](#content8)
  {: .TOC8}
</div>

***
***

## Deep Speech 
{: #content1}

1. **Introduction:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    :   This paper takes a first attempt at an End-to-End system for ASR.  

2. **Structure:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}    
    :   * __Input__: vector of speech spectrograms  
            * An *__utterance__* $$x^{(i)}$$: is a time-series of length $$T^{(i)}$$ composed of time-slices where each is a vector of audio (spectrogram) features $$x_{t,p}^{(i)}, t=1,...,T^{(i)}$$, where $$p$$ denotes the power of the p'th frequency bin in the audio frame at time $$t$$.  
        * __Output__: English text transcript $$y$$  
    :   * __Goal__:  
            The goal of the RNN is to convert an input sequence $$x$$ into a sequence of character probabilities for the transcription $$y$$, with $$\tilde{y}_t = P(c_t\vert x)$$, where $$c_t \in \{\text{a, b, c, } \ldots \text{,  z, space,  apostrophe, blank}\}$$.
                
3. **Strategy:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    :   The goal is to replace the multi-part model with a single RNN network that captures as much of the information needed to do transcription in a single system.  

4. **Solves:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    :   * Previous models only used DNNs as a single component in a complex pipeline.  
            NNs are trained to classify __individual frames of acoustic data__, and then, their output distributions are reformulated as emission probabilities for a HMM.  
            In this case, the objective function used to train the networks is therefore substantially different from the true performance measure (sequence-level transcription accuracy.  
            This leads to problems where one system might have an improved accuracy rate but the overall transcription accuracy can still decrease.  
        *  An additional problem is that the frame-level training targets must be inferred from the alignments determined by the HMM. This leads to an awkward iterative procedure, where network retraining is alternated with HMM re-alignments to generate more accurate targets.  

5. **Key Insights:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  
    :   * As an __End-to-End__ model, this system avoids the problems of __multi-part__ systems that lead to inconsistent training criteria and difficulty of integration.   
            The network is trained directly on the text transcripts: no phonetic representation (and hence no pronunciation dictionary or state tying) is used.  
        * Using __CTC__ objective, the system is able to better approximate and solve the alignment problem avoiding HMM realignment training.  
            Since CTC integrates out over all possible input-output alignments, no forced alignment is required to provide training targets.  
        * The Dataset is augmented with newly synthesized data and modified to include all the variations and effects that face ASR problems.    
            This greatly increases the system performance on particularly noisy/affected speech.  

6. **Preparing Data (Pre-Processing):**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}  
    :   The paper uses __spectrograms__ of power normalized audio clips as features.  
    :   ![img](/main_files/dl/nlp/speech_research/2.png){: width="60%"}    

7. **Architecture:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}  
    :   The system is composed of:  
        * An __RNN__:    
            * 5 layers of __hidden units__:  
                * 3 Layer of __Feed-forward Nets__:  
                    * For the __input layer__, the output depends on the spectrogram frame $$x_t$$ along with a context of $$C$$ frames on each side.  
                        > $$C \in \{5, 7, 9\}$$  
                    * The non-recurrent layers operate on independent data for each time step:  
                        $$h_t^{(l)} = g(W^{(l)} h_{(t)}^{(l-1)} + b^{(l)}),$$  
                        where $$g(z) = \min \{\max \{0, z\}, 20\}$$ is the *clipped RELU*.    
                * 2 layers of __Recurrent Nets__:  
                    * 1 layer of a __Bi-LSTM__:  
                        * Includes two sets of hidden units: 
                            A set with forward recurrence $$h^{(f)}$$  
                            A set with backward recurrence $$h^{(b)}$$:  
                            $$h_t^{(f)} = g(W^{(4)}h_t^{(3)} + W_r^{(b)} h_{t-1}^{(b)} + b ^{(4)}) \\ 
                            h_t^{(b)} = g(W^{(4)}h_t^{(3)} + W_r^{(b)} h_{t+1}^{(b)} + b ^{(4)})$$  
                            > Note that $$h^{(f)}$$ must be computed sequentially from $$t = 1$$ to $$t = T^{(i)}$$ for the i’th utterance, while the units $$h^{(b)}$$ must be computed sequentially in reverse from $$t = T^{(i)}$$ to $$t = 1$$.  
                    * 1 layer of __Feed-forward Nets__:   
                        * The fifth (non-recurrent) layer takes both the forward and backward units as inputs:  
                            $$h_t^{(5)} = g(W ^{(5)}h_t ^{(4)} + b ^{(5)}),$$  
                            where $$h_t^{(4)} = h_t^{(f)} + h_t^{(b)}$$ 
            * An __Output__ layer made of a standard __softmax function__ that yields the predicted character probabilities for each time-slice $$t$$ and character $$k$$ in the alphabet:   
                $$\displaystyle{h _{(t,k)} ^{(6)} = \hat{y} _{(t,k)} = P(c_t = k \vert x) = \dfrac{\exp (W_k ^{(6)} h_t ^{(5)} + b_k ^{(6)})}{\sum_j \exp (W_j ^{(6)}h_t ^{(5)} + b_j ^{(6)})}},$$  
                where $$W_k ^{(6)}$$ and $$b_k ^{(6)}$$ denote the k'th column of the weight matrix and k'th bias.  
        * A *__CTC__* __Loss Function__ $$\mathcal{L}(\hat{y}, y)$$  
        * An *__N-gram Language Model__* 
        * A __combined Objective Function__:  
    :   $$Q(c) = \log (P(x \vert x)) + \alpha \log (P_{\text{LM}}(c) + \beta \text{word_count}(c))$$   
    :   ![img](/main_files/dl/nlp/speech_research/1.png){: width="80%"}    

8. **Algorithm:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18}  
    :   * Given the output $$P(c \vert x)$$ of the RNN: perform a __search__ to find the sequence of characters $$c_1, c_2, ...$$ that is most probable according to both:  
            1. The RNN Output
            2. The Language Model  
        * We maximize the combined objective:  
            $$Q(c) = \log (P(x \vert x)) + \alpha \log (P_{\text{LM}}(c) + \beta \text{word_count}(c))$$  
            where the term $$P_{\text{lm}} denotes the probability of the sequence $$c$$ according to the N-gram model.  
        * The objective is maximized using a highly optimized __beam search__ algorithm  
            > beam size: 1000-8000

9. **Training:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents19}  
    :   * The gradient of the CTC Loss $$\nabla_{\hat{y}} \mathcal{L}(\hat{y}, y)$$ with respect to the net outputs given the ground-truth character sequence $$y$$ is computed
    :   * Nesterov’s Accelerated gradient
        * Nesterov Momentum
        * Annealing the learning rate by a constant factor
        * Dropout  
        * Striding -- shortening the recurrent layers by taking strides of size $$2$$.  
            The unrolled RNN will have __half__ as many steps.  
            > similar to a convolutional network with a step-size of 2 in the first layer.  

10. **Parameters:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents110}  
    :   * __Momentum__: $$0.99$$ 
        * __Dropout__: $$5-10 \%$$ (FFN only)   
        * __Trade-Off Params__: use cross-validation for $$\alpha, \beta$$  

11. **Issues/The Bottleneck:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents111}  
    :   

12. **Results:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents112}  
    :   * __SwitchboardHub5’00__  (
    WER): 
            * Standard: $$16.0\%$$  
            * w/Lexicon of allowed words: $$21.9\%$$ 
            * Trigram LM: $$8.2\%$$ 
            * w/Baseline system: $$6.7\%$$

13. **Discussion:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents113}  
    :   * __Why avoid LSTMs__:  
            One disadvantage of LSTM cells is that they require computing and storing multiple gating neuron responses at each step.  
            Since the forward and backward recurrences are sequential, this small additional cost can become a computational bottleneck.  
    :   * __Why a homogeneous model__:  
             By using a homogeneous model we have made the computation of the recurrent activations as efficient as possible: computing the ReLu outputs involves only a few highly optimized BLAS operations on the GPU and a single point-wise nonlinearity.

14. **Further Development:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents114}  
    :   

***

## Towards End-to-End Speech Recognition with Recurrent Neural Networks
{: #content2}

1. **Introduction:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    :   This paper presents an ASR system that directly transcribes audio data with text, __without__ requiring an _intermediate phonetic representation_.

2. **Structure:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}    
    :   * __Input__: 
        * __Output__:  
                

3. **Strategy:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}  
    :   The goal of this paper is a system where as much of the speech pipeline as possible is replaced by a single recurrent neural network (RNN) architecture.  
        The language model, however, will be lacking due to the limitation of the audio data to learn a strong LM. 

4. **Solves:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}  
    :   * First attempts used __RNNs__ or standard __LSTMs__. These models lacked the complexity that was needed to capture all the models required for ASR. 

5. **Key Insights:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}  
    :   * The model uses Bidirectional LSTMs to capture the nuances of the problem.  
        * The system uses a new __objective function__ that trains the network to directly optimize the __WER__.  

6. **Preparing the Data (Pre-Processing):**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents26}  
    :   The paper uses __spectrograms__ as a minimal preprocessing scheme.  

7. **Architecture:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents27}  
    :   The system is composed of:  
        * A __Bi-LSTM__  
        * A __CTC output layer__  
        * A __combined objective function__:  
            The new objective function at allows an RNN to be trained to optimize the expected value of an arbitrary loss function defined over output transcriptions (such as __WER__).  
            Given input sequence $$x$$, the distribution $$P(y\vert x)$$ over transcriptions sequences $$y$$ defined by CTC, and a real-valued transcription loss function $$\mathcal{L}(x, y)$$, the expected transcription loss $$\mathcal{L}(x)$$ is defined:  
            <p>$$\begin{align}
                \mathcal{L}(x) &= \sum_y P(y \vert x)\mathcal{L}(x,y) \\ 
                &= \sum_y \sum_{a \in \mathcal{B}^{-1}(y)} P(a \vert x)\mathcal{L}(x,y) \\
                &= \sum_a P(a \vert x)\mathcal{L}(x,\mathcal{B}(a))
                \end{align}$$</p>  
        <button>Show Derivation</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![Approximation and Differentiation](/main_files/dl/nlp/speech_research/3.png){: hidden="" width="80%"}


8. **Algorithm:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents28}  
    :   

9. **Issues/The Bottleneck:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents29}  
    :   

10. **Results:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents210}  
    :   * __WSJC__ (
    WER): 
            * Standard: $$27.3\%$$  
            * w/Lexicon of allowed words: $$21.9\%$$ 
            * Trigram LM: $$8.2\%$$ 
            * w/Baseline system: $$6.7\%$$

***

## Attention-Based Models for Speech Recognition
{: #content3}

1. **Introduction:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}  
    :   This paper introduces and extends the attention mechanism with features needed for ASR. It adds location-awareness to the attention mechanism to add robustness against different lengths of utterances.  

2. **Motivation:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}    
    :   Learning to recognize speech can be viewed as learning to generate a sequence (transcription) given another sequence (speech).  
        From this perspective it is similar to machine translation and handwriting synthesis tasks, for which attention-based methods have been found suitable. 
    :   __How ASR differs:__  
        Compared to _Machine Translation_, speech recognition differs by requesting much longer input sequences which introduces a challenge of distinguishing similar speech fragments in a single utterance.  
        > thousands of frames instead of dozens of words   
    :   It is different from _Handwriting Synthesis_, since the input sequence is much noisier and does not have a clear structure.  

2. **Structure:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}    
    :   * __Input__: $$x=(x_1, \ldots, x_{L'})$$ is a sequence of feature vectors  
            * Each feature vector is extracted from a small overlapping window of audio frames
        * __Output__: $$y$$ a sequence of __phonemes__   

3. **Strategy:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}  
    :   The goal of this paper is a system, that uses attention-mechanism with location awareness, whose performance is comparable to that of the conventional approaches.   
    :   * For each generated phoneme, an attention mechanism selects or weighs the signals produced by a trained feature extraction mechanism at potentially all of the time steps in the input sequence (speech frames).  
        * The weighted feature vector then helps to condition the generation of the next element of the output sequence.  
        * Since the utterances in this dataset are rather short (mostly under 5 seconds), we measure the ability of the considered models in recognizing much longer utterances which were created by artificially concatenating the existing utterances.

4. **Solves:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents34}  
    :   * __Problem__:  
            The [attention-based model proposed for NMT](https://arxiv.org/abs/1409.0473) demonstrates vulnerability to the issue of similar speech fragments with __longer, concatenated utterances__.  
            The paper argues that  this model adapted to track the absolute location in the input sequence of the content it is recognizing, a strategy feasible for short utterances from the original test set but inherently unscalable.  
        * __Solution__:  
            The attention-mechanism is modified to take into account the location of the focus from the previous step and the features of the input sequence by adding as inputs to the attention mechanism auxiliary *__Convolutional Features__* which are extracted by convolving the attention weights from the previous step with trainable filters.  

5. **Key Insights:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents35}  
    :   * Introduces attention-mechanism to ASR
        * The attention-mechanism is modified to take into account:  
            * location of the focus from the previous step  
            * features of the input sequence
        * Proposes a generic method of adding location awareness to the attention mechanism
        * Introduce a modification of the attention mechanism to avoid concentrating the attention on a single frame  

7. **Attention-based Recurrent Sequence Generator (ARSG):**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents37}  
    :   is a recurrent neural network that stochastically generates an output sequence $$(y_1, \ldots, y_T)$$ from an input $$x$$.  
    In practice, $$x$$ is often processed by an __encoder__ which outputs a sequential input representation $$h = (h_1, \ldots, h_L)$$ more suitable for the attention mechanism to work with.  
    :   The __Encoder__: a deep bidirectional recurrent network.  
        It forms a sequential representation h of length $$L = L'$$.  
    :   __Structure:__{: style="color: red"}    
        * *__Input__*: $$x = (x_1, \ldots, x_{L'})$$ is a sequence of feature vectors   
            > Each feature vector is extracted from a small overlapping window of audio frames.  
        * *__Output__*: $$y$$ is a sequence of phonemes
    :   __Strategy:__{: style="color: red"}    
        At the $$i$$-th step an ARSG generates an output $$y_i$$ by focusing on the relevant elements of $$h$$:  
    :   $$\begin{align}
        \alpha_i &= \text{Attend}(s_{i-1}, \alpha _{i-1}), h) & (1) \\
        g_i &= \sum_{j=1}^L \alpha_{i,j} h_j & (2) //
        y_i &\sim \text{Generate}(s_{i-1}, g_i) & (3)  
        \end{align}$$
    :   where $$s_{i−1}$$ is the $$(i − 1)$$-th state of the recurrent neural network to which we refer as the __generator__, $$\alpha_i \in \mathbb{R}^L$$ is a vector of the _attention weights_, also often called the __alignment__; and $$g_i$$ is the __glimpse__.  
        The step is completed by computing a *__new generator state__*:  
    :   $$s_i = \text{Recurrency}(s_{i-1}, g_i, y_i)$$  
    :   where the _Recurrency_ is an RNN.  
    :   ![img](/main_files/dl/nlp/speech_research/4.png){: width="100%"}  

12. **Attention-mechanism Types and Speech Recognition:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents312}  
    :   __Types of Attention:__{: style="color: red"}      
        * (Generic) Hybrid Attention: $$\alpha_i = \text{Attend}(s_{i-1}, \alpha_{i-1}, h)$$  
        * Content-based Attention: $$\alpha_i = \text{Attend}(s_{i-1}, h)$$   
            In this case, Attend is often implemented by scoring each element in h separately and normalizing the scores:  
            $$e_{i,j} = \text{Score}(s_{i-1}, h_j) \\$$ 
              $$\alpha_{i,j} = \dfrac{\text{exp} (e_{i,j}) }{\sum_{j=1}^L \text{exp}(e_{i,j})}$$  
            * __Limitations__:  
                The main limitation of such scheme is that identical or very similar elements of $$h$$ are scored equally regardless of their position in the sequence.  
                Often this issue is partially alleviated by an encoder such as e.g. a BiRNN or a deep convolutional network that encode contextual information into every element of h . However, capacity of h elements is always limited, and thus disambiguation by context is only possible to a limited extent.  
        * Location-based Attention: $$\alpha_i = \text{Attend}(s_{i-1}, \alpha_{i-1})$$   
            a location-based attention mechanism computes the alignment from the generator state and the previous alignment only.  
            * __Limitations__:  
                the model would have to predict the distance between consequent phonemes using $$s_{i−1}$$ only, which we expect to be hard due to large variance of this quantity.  
    :   Thus, we conclude that the __*Hybrid Attention*__ mechanism is a suitable candidate.  
        Ideally, we need an attention model that uses the previous alignment $$\alpha_{i-1}$$ to select a short list of elements from $$h$$, from which the content-based attention, will select the relevant ones without confusion.  

6. **Preparing the Data (Pre-Processing):**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents36}  
    :   The paper uses __spectrograms__ as a minimal preprocessing scheme.  

7. **Architecture:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents37}  
    :   Start with the __ARSG__-based model:  
        * __Encoder__: is a __Bi-RNN__  
        <p>$$e_{i,j} = w^T \tanh (Ws_{i-1} + Vh_j + b)$$</p>
        * __Attention__: Content-Based Attention extended for _location awareness_  
            <p>$$e_{i,j} = w^T \tanh (Ws_{i-1} + Vh_j + Uf_{i,j} + b)$$</p>
    :   __Extending the Attention Mechanism:__  
        Content-Based Attention extended for _location awareness_ by making it take into account the alignment produced at the previous step.  
        * First, we extract $$k$$ vectors $$f_{i,j} \in \mathbb{R}^k$$ for every position $$j$$ of the previous alignment $$\alpha_{i−1}$$ by convolving it with a matrix $$F \in \mathbb{R}^{k\times r}$$:  
            <p>$$f_i = F * \alpha_{i-1}$$</p>
        * These additional vectors $$f_{i,j} are then used by the scoring mechanism $$e_{i,j}$$:  
            <p>$$e_{i,j} = w^T \tanh (Ws_{i-1} + Vh_j + Uf_{i,j} + b)$$</p>  

                
            

8. **Algorithm:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents38}  
    :   

9. **Issues/The Bottleneck:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents39}  
    :   

<!-- 10. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents310}  
    :    -->

***

## A Neural Transducer
{: #content4}

<!-- 1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents41}  
    :   

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents42}  
    :   

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents43}  
    :   

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents44}  
    :   

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents45}  
    :   

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents46}  
    :   

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents47}  
    :   

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents48}  
    :   --> 

***

## Deep Speech 2
{: #content5}

1. **Introduction:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents51}  
    :   This paper improves on the previous attempt at an End-to-End system for ASR. It increases the complexity of the architecture and is able to achieve high accuracy on two different languages -- English and Chinese.   

2. **Structure:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents52}    
    :   * __Input__: vector of speech spectrograms  
            * An *__utterance__* $$x^{(i)}$$: is a time-series of length $$T^{(i)}$$ composed of time-slices where each is a vector of audio (spectrogram) features $$x_{t,p}^{(i)}, t=1,...,T^{(i)}$$, where $$p$$ denotes the power of the p'th frequency bin in the audio frame at time $$t$$.  
        * __Output__: English text transcript $$y$$  
    :   * __Goal__:  
            The goal of the RNN is to convert an input sequence $$x$$ into a sequence of character probabilities for the transcription $$y$$, with $$\tilde{y}_t = P(c_t\vert x)$$, where $$c_t \in \{\text{a, b, c, } \ldots \text{,  z, space,  apostrophe, blank}\}$$.
                
3. **Strategy:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents53}  
    :   The goal is to replace the multi-part model with a single RNN network that captures as much of the information needed to do transcription in a single system.  

4. **Solves:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents54}  
    :   * Previous models only used DNNs as a single component in a complex pipeline.  
            NNs are trained to classify __individual frames of acoustic data__, and then, their output distributions are reformulated as emission probabilities for a HMM.  
            In this case, the objective function used to train the networks is therefore substantially different from the true performance measure (sequence-level transcription accuracy.  
            This leads to problems where one system might have an improved accuracy rate but the overall transcription accuracy can still decrease.  
        *  An additional problem is that the frame-level training targets must be inferred from the alignments determined by the HMM. This leads to an awkward iterative procedure, where network retraining is alternated with HMM re-alignments to generate more accurate targets.  

5. **Key Insights:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents55}  
    :   * As an __End-to-End__ model, this system avoids the problems of __multi-part__ systems that lead to inconsistent training criteria and difficulty of integration.   
            The network is trained directly on the text transcripts: no phonetic representation (and hence no pronunciation dictionary or state tying) is used.  
        * Using __CTC__ objective, the system is able to better approximate and solve the alignment problem avoiding HMM realignment training.  
            Since CTC integrates out over all possible input-output alignments, no forced alignment is required to provide training targets.  
        * The Dataset is augmented with newly synthesized data and modified to include all the variations and effects that face ASR problems.    
            This greatly increases the system performance on particularly noisy/affected speech.  

6. **Preparing Data (Pre-Processing):**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents56}  
    :   The paper uses __spectrograms__ as a minimal preprocessing scheme.  
    :   ![img](/main_files/dl/nlp/speech_research/2.png){: width="60%"}    

7. **Architecture:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents57}  
    :   The system is composed of:  
        * An __RNN__:    
            * 5 layers of __hidden units__:  
                * 3 Layer of __Feed-forward Nets__:  
                    * For the __input layer__, the output depends on the spectrogram frame $$x_t$$ along with a context of $$C$$ frames on each side.  
                        > $$C \in \{5, 7, 9\}$$  
                    * The non-recurrent layers operate on independent data for each time step:  
                        $$h_t^{(l)} = g(W^{(l)} h_{(t)}^{(l-1)} + b^{(l)}),$$  
                        where $$g(z) = \min \{\max \{0, z\}, 20\}$$ is the *clipped RELU*.    
                * 2 layers of __Recurrent Nets__:  
                    * 1 layer of a __Bi-LSTM__:  
                        * Includes two sets of hidden units: 
                            A set with forward recurrence $$h^{(f)}$$  
                            A set with backward recurrence $$h^{(b)}$$:  
                            $$h_t^{(f)} = g(W^{(4)}h_t^{(3)} + W_r^{(b)} h_{t-1}^{(b)} + b ^{(4)}) \\ 
                            h_t^{(b)} = g(W^{(4)}h_t^{(3)} + W_r^{(b)} h_{t+1}^{(b)} + b ^{(4)})$$  
                            > Note that $$h^{(f)}$$ must be computed sequentially from $$t = 1$$ to $$t = T^{(i)}$$ for the i’th utterance, while the units $$h^{(b)}$$ must be computed sequentially in reverse from $$t = T^{(i)}$$ to $$t = 1$$.  
                    * 1 layer of __Feed-forward Nets__:   
                        * The fifth (non-recurrent) layer takes both the forward and backward units as inputs:  
                            $$h_t^{(5)} = g(W ^{(5)}h_t ^{(4)} + b ^{(5)}),$$  
                            where $$h_t^{(4)} = h_t^{(f)} + h_t^{(b)}$$ 
            * An __Output__ layer made of a standard __softmax function__ that yields the predicted character probabilities for each time-slice $$t$$ and character $$k$$ in the alphabet:   
                $$\displaystyle{h _{(t,k)} ^{(6)} = \hat{y} _{(t,k)} = P(c_t = k \vert x) = \dfrac{\exp (W_k ^{(6)} h_t ^{(5)} + b_k ^{(6)})}{\sum_j \exp (W_j ^{(6)}h_t ^{(5)} + b_j ^{(6)})}},$$  
                where $$W_k ^{(6)}$$ and $$b_k ^{(6)}$$ denote the k'th column of the weight matrix and k'th bias.  
        * A *__CTC__* __Loss Function__ $$\mathcal{L}(\hat{y}, y)$$  
        * An *__N-gram Language Model__* 
        * A __combined Objective Function__:  
    :   $$Q(c) = \log (P(x \vert x)) + \alpha \log (P_{\text{LM}}(c) + \beta \text{word_count}(c))$$   
    :   ![img](/main_files/dl/nlp/speech_research/1.png){: width="80%"}    
8. **Algorithm:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents58}  
    :   * Given the output $$P(c \vert x)$$ of the RNN: perform a __search__ to find the sequence of characters $$c_1, c_2, ...$$ that is most probable according to both:  
            1. The RNN Output
            2. The Language Model  
        * We maximize the combined objective:  
            $$Q(c) = \log (P(x \vert x)) + \alpha \log (P_{\text{LM}}(c) + \beta \text{word_count}(c))$$  
            where the term $$P_{\text{lm}} denotes the probability of the sequence $$c$$ according to the N-gram model.  
        * The objective is maximized using a highly optimized __beam search__ algorithm  
            > beam size: 1000-8000

9. **Training:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents59}  
    :   * The gradient of the CTC Loss $$\nabla_{\hat{y}} \mathcal{L}(\hat{y}, y)$$ with respect to the net outputs given the ground-truth character sequence $$y$$ is computed
    :   * Nesterov’s Accelerated gradient
        * Nesterov Momentum
        * Annealing the learning rate by a constant factor
        * Dropout  
        * Striding -- shortening the recurrent layers by taking strides of size $$2$$.  
            The unrolled RNN will have __half__ as many steps.  
            > similar to a convolutional network with a step-size of 2 in the first layer.  

10. **Parameters:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents510}  
    :   * __Momentum__: $$0.99$$ 
        * __Dropout__: $$5-10 \%$$ (FFN only)   
        * __Trade-Off Params__: use cross-validation for $$\alpha, \beta$$  

11. **Issues/The Bottleneck:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents511}  
    :   

12. **Results:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents512}  
    :   * __SwitchboardHub5’00__  (
    WER): 
            * Standard: $$16.0\%$$  
            * w/Lexicon of allowed words: $$21.9\%$$ 
            * Trigram LM: $$8.2\%$$ 
            * w/Baseline system: $$6.7\%$$

13. **Discussion:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents513}  
    :   * __Why avoid LSTMs__:  
            One disadvantage of LSTM cells is that they require computing and storing multiple gating neuron responses at each step.  
            Since the forward and backward recurrences are sequential, this small additional cost can become a computational bottleneck.  
    :   * __Why a homogeneous model__:  
            By using a homogeneous model we have made the computation of the recurrent activations as efficient as possible: computing the ReLu outputs involves only a few highly optimized BLAS operations on the GPU and a single point-wise nonlinearity.

14. **Further Development:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents514}  
    :   

*** 

## Listen, Attend and Spell (LAS)
{: #content6}

1. **Introduction:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents61}  
    :   This paper presents a a neural network that learns to transcribe speech utterances to characters.  Unlike traditional DNN-HMM models, this model learns all the components of a speech recognizer jointly.  
    :   The system has two components: a listener and a speller.  
    :   __LAS__ is based on the sequence to sequence learning framework with attention.  

2. **Structure:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents62}    
    :   * __Input__: $$\mathbb{x} = (x_1, \ldots, x_T)$$ a sequence of filter bank spectra (acoustic) features
            
        * __Output__: $$\mathbb{y} = (\text{<sos>}, y_1, \ldots, y_S, \text{<eos>}), y_i \in \{\text{a, b, c, · · · , z, 0, · · · , 9, <spacei,<comma>,<period>,<apostrophe>,<unk> }\}$$ the output sequence of characters  
    :   * __Goal__:  
            The goal of the RNN is to convert an input sequence $$x$$ into a sequence of character probabilities for the transcription $$y$$, with $$\tilde{y}_t = P(c_t\vert x)$$, where $$c_t \in \{\text{a, b, c, } \ldots \text{,  z, space,  apostrophe, blank}\}$$.
                
3. **Strategy:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents63}  
    :   __LAS__ is based on the sequence to sequence learning framework with attention.  
    :   * We want to model each character output $$y_i$$ as a conditional distribution over the previous characters $$y_{\leq i+1}$$ and the input signal $$\mathbb{x}$$ using the chain rule:  
        <p>$$P(\mathbb{y} \vert \mathbb{x}) = \prod_i P(y_i \vert \mathbb{x}, y_{\leq i+1}) \:\:\:\: (1)$$</p>
        * 

4. **Solves:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents64}  
    :   * __CTC__:  
            CTC assumes that the label outputs are conditionally independent of each other
        * __Seq2Seq__:  
            the sequence to sequence approach has only been applied to phoneme sequences, and not trained end-to-end for speech recognition. 
        * 

5. **Key Insights:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents65}  
    :   * Use a pyramidal RNN model for the listener, which reduces the number of time steps that the attention model has to extract relevant information from.  
        The pyramid structure also reduces the computational complexity.    
        * Character-based transcription allows the handling of rare and OOV words automatically  
        * Attention 

77. **The Model:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents677}  
:   __Listen__:  
    Uses a __Bi-directional LSTM__ with a pyramid structure.  
    > The pyramid structure is needed to reduce the length $$U$$ of $$\mathbf{h}$$, from $$T$$ , the length of the input $$\mathbb{h}$$ , because the input speech signals can be hundreds to thousands of frames long.  
    * __Pyramidal LSTM__:  
        The output at the i-th time step, from the j-th layer is changed from:  
        <p>$$h_i^j = \text{BLSTM}(h_{i-1}^j, h_{i}^{j-1})$$</p>  
        to, instead, we concatenate the outputs at consecutive steps of each layer before feeding it to the next layer:     
        <p>$$h_i^j = \text{pBLSTM}(h_{i-1}^j, \left[h_{2i}^{j-1}, h_{2i+1}^{j-1}\right])$$</p>  
        > In the model, we stack 3 pBLSTMs on top of the bottom BLSTM layer to reduce the time resolution $$2^3 = 8$$ times.  
:   __Attend and Spell:__  
    The function is computed using an __attention-based LSTM transducer__.  
    At every output step, the transducer produces a probability distribution over the next character conditioned on all the characters seen previously.  
    The __distribution__ for $$y_i$$ is a function of the decoder state $$s_i$$ and context $$c_i$$.  
    The __decoder state__ $$s_i$$ is a function of the previous state $$s_{i−1}$$, the previously emitted character $$y_{i−1}$$ and context $$c_{i−1}$$.  
    The __context vector__ $$c_i$$ is produced by an attention mechanism:  
    <p>$$ c_i = \text{AttentionContext}(s_i, \mathbf{h}) \\
        s_i = \text{RNN}(s_{i-1}, y_{i-1}, c_{i-1}) \\
    P(y_i \vert \mathbf{x}, y_{\leq i+1}) = \text{CharacterDistribution}(s_i, c_i)$$  </p>  
    where __CharacterDistribution__ is an __MLP__ with softmax outputs over characters, and __RNN__ is a 2 layer LSTM.  
    The __Attention__ Mechanism:  
    At each step $$i$$, the attention mechanism, _AttentionContext_ generates a context vector $$c_i$$ encapsulating the information in the acoustic signal needed to generate the next character.  
    The attention model is __content based__ - the contents of the decoder state $$s_i$$ are matched to the contents of $$h_u$$ representing time step $$u$$ of $$\mathbf{h}$$ to generate an attention vector $$\alpha_i$$.  
    $$\alpha_i$$ is used to linearly blend vectors $$h_u$$ to create $$c_i$$.  
    Specifically, at each decoder timestep $$i$$ , the AttentionContext function computes the scalar energy
    $$e_{i,u}$$ for each time step $$u$$ , using vector $$h_u \in h$$ and $$s_i$$.  
    The scalar energy $$e_{i,u}$$ is converted into a
    probability distribution over times steps (or attention) $$\alpha_i$$  using a softmax function. This is used to create the context vector $$c_i$$  by linearly blending the listener features, $$h_u$$, at different time steps:  
    <p>  
    $$\begin{align}
        e_{i,u} &= <\phi(s_i), \psi(h_u)> \\
        \alpha_{i,u} &= \dfrac{\exp(e_{i,u})}{\sum_u \exp(e_{i,u})} \\
        c_i &= \sum_u \alpha_{i,u}h_u 
        \end{align}
        $$ 
    </p>  
    where $$\phi$$ and $$\psi$$ are __MLP__ Networks.  
    On convergence, the $$\alpha_i$$  distribution is typically very sharp, and focused on only a few frames of $$\mathbf{h}$$ ; $$c_i$$ can be seen as a continuous bag of weighted features of $$\mathbf{h}$$.  

6. **Preparing Data (Pre-Processing):**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents66}  

7. **Architecture:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents67}
    :   ![img](/main_files/dl/nlp/speech_research/5.png){: width="60%"}  
    :   * __Encoder (listener):__  
            An __acoustic model__ encoder, whose key operation is ```Listen```.  
            It converts low level speech signals into higher level features.  
            * __(pyramidal) RNN__:  
                * __Bi-Directional LSTM__:  
                            
                    * *__Structure__*:  
                        * *__Input:__* original signal $$ \mathbb{x}$$ 
                        * *__Output:__* a high level representation $$\mathbf{h} = (h_1, ]ldots, h_U)$$, with $$U \leq T$$   
                        
        * __Decoder (speller)__:  
            The speller is an _attention-based_ __character decoder__, whose key operation is ```AttendAndSpell```.  
            It converts the higher level features into output utterances by specifying a probability distribution over sequences of characters using the attention mechanism.  
            * __RNN__:  
                * *__Structure__*:  
                    * *__Input:__* features $$ \mathbf{h}$$ 
                    * *__Output:__* a probability distribution over character sequences:   $$\mathbf{h} = (h_1, ]ldots, h_U)$$, with $$U \leq T$$
    
8. **Algorithm:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents68}  
    :   

9. **Training:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents69}  
    :   * The gradient of the CTC Loss $$\nabla_{\hat{y}} \mathcal{L}(\hat{y}, y)$$ with respect to the net outputs given the ground-truth character sequence $$y$$ is computed
    :   * Nesterov’s Accelerated gradient
        * Nesterov Momentum
        * Annealing the learning rate by a constant factor
        * Dropout  
        * Striding -- shortening the recurrent layers by taking strides of size $$2$$.  
            The unrolled RNN will have __half__ as many steps.  
            > similar to a convolutional network with a step-size of 2 in the first layer.  

99. **Inference (Decoding and Rescoring):**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents699}  


10. **Parameters:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents610}  
    :   * __Momentum__: $$0.99$$ 
        * __Dropout__: $$5-10 \%$$ (FFN only)   
        * __Trade-Off Params__: use cross-validation for $$\alpha, \beta$$  


11. **Issues/The Bottleneck:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents611}  
    :   

12. **Results:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents612}  
    :   * __SwitchboardHub5’00__  (
    WER): 
            * Standard: $$16.0\%$$  
            * w/Lexicon of allowed words: $$21.9\%$$ 
            * Trigram LM: $$8.2\%$$ 
            * w/Baseline system: $$6.7\%$$

13. **Discussion:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents613}  
    :   * Without the attention mechanism, the model overfits the training data significantly, in spite of our large training set of three million utterances - it memorizes the training transcripts without paying attention to the acoustics.  
        * Without the pyramid structure in the encoder side, our model converges too slowly - even after a month of training, the error rates were significantly higher than the errors reported
        * To reduce the overfitting of the speller to the training transcripts, use a sampling trick during training

14. **Further Development:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents614}  
    :   

***
<!-- 
## Seven
{: #content7}

1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents7 #bodyContents71}  
    :   

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents7 #bodyContents72}  
    :   

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents7 #bodyContents73}  
    :   

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents7 #bodyContents74}  
    :   

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents7 #bodyContents75}  
    :   

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents7 #bodyContents76}  
    :   

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents7 #bodyContents77}  
    :   

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents7 #bodyContents78}  
    :   

## Eight
{: #content8}

1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents81}  
    :   

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents82}  
    :   

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents83}  
    :   

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents84}  
    :   

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents85}  
    :   

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents86}  
    :   

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents87}  
    :   

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents88}  
    :   

## Nine
{: #content9}

1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents91}  
    :   

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents92}  
    :   

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents93}  
    :   

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents94}  
    :   

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents95}  
    :   

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents96}  
    :   

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents97}  
    :   

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents98}  
    :   

## Ten
{: #content10}

1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents10 #bodyContents101}  
    :   

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents10 #bodyContents102}  
    :   

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents10 #bodyContents103}  
    :   

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents10 #bodyContents104}  
    :   

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents10 #bodyContents105}  
    :   

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents10 #bodyContents106}  
    :   

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents10 #bodyContents107}  
    :   

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents10 #bodyContents108}  
    :   

 -->