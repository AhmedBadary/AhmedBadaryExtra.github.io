---
layout: NotesPage
title: Deep Learning <br /> Research Papers
permalink: /work_files/research/dl/nlp/nlp_research
prevLink: /work_files/research/dl/nlp.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Sequence to Sequence Learning with Neural Network](#content1)
  {: .TOC1}
  * [Towards End-to-End Speech Recognition with Recurrent Neural Networks](#content2)
  {: .TOC2}
  * [Attention-Based Models for Speech Recognition](#content3)
  {: .TOC3}
  * [Attention Is All You Need](#content4)
  {: .TOC4}
<!--   * [5](#content5)
  {: .TOC5}
  * [6](#content6)
  {: .TOC6}
  * [7](#content7)
  {: .TOC7}
  * [8](#content8)
  {: .TOC8} -->
</div>

***
***

## Sequence to Sequence Learning with Neural Network
{: #content1}

1. **Introduction:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    This paper presents a general end-to-end approach to sequence learning that makes minimal assumptions (Domain-Independent) on the sequence structure.  
    It introduces __Seq2Seq__. 

2. **Structure:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}    
    * __Input__: sequence of input vectors  
    * __Output__: sequence of output labels
                
3. **Strategy:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    The idea is to use one LSTM to read the input sequence, one time step at a time, to obtain large fixed dimensional vector representation, and then to use another LSTM to extract the output sequence from that vector.  
    The second LSTM is essentially a recurrent neural network language model except that it is __conditioned__ on the __input sequence__.

4. **Solves:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    * Despite their flexibility and power, DNNs can only be applied to problems whose inputs and targets can be sensibly encoded with vectors of fixed dimensionality. It is a significant limitation, since many important problems are best expressed with sequences whose lengths are not known a-priori.  
        The RNN can easily map sequences to sequences whenever the alignment between the inputs the outputs is known ahead of time. However, it is not clear how to apply an RNN to problems whose input and the output sequences have different lengths with complicated and non-monotonic relationship.  


5. **Key Insights:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  
    * Uses LSTMs to capture the information present in a sequence of inputs into one vector of features that can then be used to decode a sequence of output features  
    * Uses two different LSTM, for the encoder and the decoder respectively  
    * Reverses the words in the source sentence to make use of short-term dependencies (in translation) that led to better training and convergence 

6. **Preparing Data (Pre-Processing):**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}  
    :   
                    

7. **Architecture:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}  
    :   * __Encoder__:  
            * *__LSTM:__* 
                * 4 Layers:    
                    * 1000 Dimensions per layer
                    * 1000-dimensional word embeddings
        * __Decoder__:  
            * *__LSTM:__* 
                * 4 Layers:    
                    * 1000 Dimensions per layer
                    * 1000-dimensional word embeddings
        * An __Output__ layer made of a standard __softmax function__  
            > over 80,000 words  
        * __Objective Function__:  
            <p>$$\dfrac{1}{\vert \mathbb{S} \vert} \sum_{(T,S) \in \mathbb{S}} \log p(T \vert S)
            $$</p>  
            where $$\mathbb{S}$$ is the training set.  
                
8. **Algorithm:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18}  
:   * Train a large deep LSTM 
    * Train by maximizing the log probability of a correct translation $$T$$  given the source sentence $$S$$  
    * Produce translations by finding the most likely translation according to the LSTM:   
        <p>$$\hat{T} = \mathrm{arg } \max_{T} p(T \vert S)$$</p>
    * Search for the most likely translation using a simple left-to-right beam search decoder which maintains a small number B of partial hypotheses  
        > A __partial hypothesis__ is a prefix of some translation  
    * At each time-step we extend each partial hypothesis in the beam with every possible word in the vocabulary  
        > This greatly increases the number of the hypotheses so we discard all but the $$B$$  most likely hypotheses according to the model’s log probability  
    * As soon as the “<EOS>” symbol is appended to a hypothesis, it is removed from the beam and is added to the set of complete hypotheses  
    *

9. **Training:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents19}  
    :   * SGD
        * Momentum 
        * Half the learning rate every half epoch after the 5th epoch
        * Gradient Clipping  
            > enforce a hard constraint on the norm of the gradient
        * Sorting input

10. **Parameters:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents110}  
    :   * __Initialization__ of all the LSTM params with __uniform distribution__ $$\in [-0.08, 0.08]$$  
        * __Learning Rate__: $$0.7$$ 
        * __Batches__: $$28$$ sequences
        * __Clipping__: 
    :   $$g = 5g/\|g\|_2 \text{ if } \|g\|_2 > 5 \text{ else } g$$ 
                  

11. **Issues/The Bottleneck:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents111}  
    :   * The decoder is __approximate__  
        * The system puts too much pressure on the last encoded vector to capture all the (long-term) dependencies

12. **Results:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents112}  
    :   

13. **Discussion:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents113}  
    :   * Sequence to sequence learning is a framework that attempts to address the problem of learning variable-length input and output sequences. It uses an encoder RNN to map the sequential variable-length input into a fixed-length vector. A decoder RNN then uses this vector to produce the variable-length output sequence, one token at a time. During training, the model feeds the groundtruth labels as inputs to the decoder. During inference, the model performs a beam search to generate suitable candidates for next step predictions.

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

10. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents310}  
    :   

***

## Attention Is All You Need
{: #content4}

1. **Introduction:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents41}  
    This paper introduces the __Transformer__ network architecture.  
    The model relies completely on __Attention__ and disregards _recurrence/convolutions_ completely.

2. **Motivation:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents42}  
    Motivation for __Dropping__:
    * __Recurrent Connections__:  
        * <span>Complex</span>{: style="color: purple"} 
        * Tricky to <span>Train</span>{: style="color: purple"} and <span>Regularize</span>{: style="color: purple"} 
        * <span>Capturing __long-term dependencies__ is _limited_ and _hard_ to *__parallelize__*</span>{: style="color: purple"}  
        * __Sequence-aligned states__ in RNN are *wasteful*.  
        * Hard to model __hierarchical-like domains__ such as languages.  
    * __Convolutional Connections__:  
        * Convolutional approaches are sometimes effective (more on this)  
        * But they tend to be <span>memory-intensive</span>{: style="color: purple"}.  
        * <span>__Path length__ between _positions_ can be __logarithmic__ when using</span>{: style="color: purple"} __dilated convolutions__; and __Left-padding__ (for text). (autoregressive CNNs WaveNet, ByteNET)  
            * However, __Long-distance dependencies require many layers__.   
        * Modeling long-range dependencies with CNNs requires either:  
            * __Many Layers:__ likely making training harder   
            * __Large Kernels__: at large parameter/computational cost  


    Motivation for __Transformer__:  
    It gives us the <span>__shortest possible path__ through the network _between any two **input-output locations**_</span>{: style="color: purple"}.  

    Motivation in __NLP__:  
    The following quote:  
    <span>“You can’t cram the meaning of a whole %&!$# sentence into a single $&!#* vector!”</span>{: style="color: purple"} - ACL 2014
    <br>

22. **Idea:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents422}  
    <span>Why not use __Attention__ for *__Representations?__*</span>{: style="color: purple"}  

    * __Self-Attention:__ You try to represent (re-express) yourself (the word_i) as a weighted combination of your entire neighborhood  
    * __FFN Layers:__ they compute new features for the representations from the attention weighted combination  
    * __Residual Connections:__ Residuals carry/propagate <span>positional information</span>{: style="color: purple"} about the inputs to higher layers, among other info.   
    * __Attention-Layer__:  
        * Think of as a feature detector.  
    <br>

3. **From Attention to Self-Attention:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents43}  
    __The Encoder-Decoder Architecture:__{: style="color: red"}  
    For a fixed target output, $$t_j$$, all hidden state source inputs are taken into account to compute the cosine similarity with the source inputs $$s_i$$, to generate the $$\theta_i$$’s (attention weights) for every source input $$s_i$$.  

4. **Strategy:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents44}  
    The idea here is to <span>learn a context vector</span>{: style="color: purple"} (say $$U$$), which gives us <span>__global level information__ on all the inputs</span>{: style="color: purple"} and tells us about the most important information.  
    E.g. This could be done by taking a cosine similarity of this context vector $$U$$  w.r.t the input hidden states from the fully connected layer. We do this for each input $$x_i$$ and thus obtain a $$\theta_i$$ (attention weights).  

    __The Goal(s):__{: style="color: red"}  
    {: #lst-p}
    * __Parallelization of Seq2Seq:__ RNN/CNN handle sequences word-by-word sequentially which is an obstacle to parallelize.  
        Transformer achieves parallelization by replacing recurrence with attention and encoding the symbol position in the sequence.  
        This, in turn, leads to a significantly shorter training time.  
    * __Reduce sequential computation__: Constant $$\mathcal{O}(1)$$ number of operations to learn dependency between two symbols independently of their position/distance in sequence.  

    The Transformer reduces the number of sequential operations to relate two symbols from input/output sequences to a constant $$\mathcal{O}(1)$$ number of operations.  
    It achieves this with the __multi-head attention__ mechanism that allows it to <span>model dependencies regardless of their distance in input or output sentence</span>{: style="color: purple"} (by counteracting reduced effective resolution due to averaging the attention-weighted positions).  

6. **Architecture:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents46}  
    ![img](/main_files/research/1.png){: width="48%"}  \\
    The Transformer follows a __Encoder-Decoder__ architecture using __stacked self-attention__ and __point-wise, fully connected layers__ for both the encoder and decoder, shown in the left and right halves of Figure 1, respectively:  

    __Encoder:__  
    The encoder is composed of a stack of $$N = 6$$ identical layers. Each layer has two sub-layers. The first is a __multi-head self-attention mechanism__, and the second is a simple, __positionwise fully connected feed-forward network__. We employ a residual connection around each of the two sub-layers, followed by layer normalization. That is, the output of each sub-layer is $$\text{LayerNorm}(x + \text{Sublayer}(x))$$, where $$\text{Sublayer}(x)$$ is the function implemented by the sub-layer itself. To facilitate these residual connections, all sub-layers in the model, as well as the embedding layers, produce outputs of dimension $$d_{\text{model}} = 512$$.  
    
    __Decoder:__  
    The decoder is also composed of a stack of $$N = 6$$ identical layers. In addition to the two sub-layers in each encoder layer, the decoder inserts a third sub-layer, which performs __multi-head attention over the output of the encoder stack__. Similar to the encoder, we employ residual connections around each of the sub-layers, followed by layer normalization. We also modify the self-attention sub-layer in the decoder stack to prevent positions from attending to subsequent positions. This masking, combined with fact that the output embeddings are offset by one position, ensures that the predictions for position $$i$$ can depend only on the known outputs at positions less than $$i$$.  
    \\
    The __Encoder__ maps an input sequence of symbol representations $$(x_1, \ldots, x_n)$$ to a sequence of continuous representations $$z = (z_1, ..., z_n)$$.  
    Given $$z$$, the decoder then generates an output sequence $$(y_1, ..., y_m)$$ of symbols one element at a time. At each step the model is auto-regressive, consuming the previously generated symbols as additional input when generating the next.  

7. **The Model - Attention:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents47}  
    __Formulation:__{: style="color: red"}
    Standard attention with _queries_ and _key_, _value_ pairs.  
    * __Scaled Dot-Product Attention__:  
        ![img](/main_files/research/3.png){: width="28%"}  \\
        Given: (1) Queries $$\vec{q} \in \mathbb{R}^{d_k}$$  (2) Keys $$\vec{k} \in \mathbb{R}^{d_k}$$  (3) Values $$\vec{v} \in \mathbb{R}^{d_v}$$  
        Computes the dot products of the queries with all keys; scales each by $$\sqrt{d_k}$$; and normalizes with a _softmax_ to obtain the weights $$\theta_i$$s on the values.  
        For a given query vector $$\vec{q} = \vec{q}_j$$ for some $$j$$:  
        <p>$${\displaystyle \vec{o} = \sum_{i=0}^{d_k} \text{softmax} (\dfrac{\vec{q}^T \: \vec{k}_i}{\sqrt{d_k}}) \vec{v}_i
        = \sum_{i=0}^{d_k} \theta_i \vec{v}_i}$$</p>  
        In practice, we compute the attention function on a set of queries simultaneously, in matrix form (stacked row-wise):  
        <p>$${\displaystyle \text{Attention}(Q, K, V) = O = \text{softmax} (\dfrac{QK^T}{\sqrt{d_k}}) V } \tag{1}$$</p>  
        __Motivation__: We suspect that for large values of $$d_k$$, the dot products grow large in magnitude, pushing the softmax function into regions where it has extremely small gradients. To counteract this effect, we scale the dot products by $$\sqrt{\dfrac{1}{d_k}}$$.  
    * __Multi-Head Attention__:  
        ![img](/main_files/research/2.png){: width="28%"}  \\
        Instead of performing a single attention function with $$d_{\text{model}}$$-dimensional keys, values and queries; linearly project the queries, keys and values $$h$$ times with different, learned linear projections to $$d_k, d_k$$ and $$d_v$$ dimensions, respectively. Then, attend (apply $$\text{Attention}$$ function) on each of the projected versions, _in parallel_, yielding $$d_v$$-dimensional output values. The final values are obtained by _concatenating_ and _projecting_ the $$d_v$$-dimensional output values from each of the attention-heads.  
        <p>$$\begin{aligned} \text {MultiHead}(Q, K, V) &=\text {Concat}\left(\text {head}_ {1}, \ldots, \text {head}_ {h}\right) W^{O} \\ \text { where head}_ {i} &=\text {Attention}\left(Q W_{i}^{Q}, K W_{i}^{K}, V W_{i}^{V}\right) \end{aligned}$$</p>  
        Where the projections are parameter matrices $$ W_{i}^{Q} \in \mathbb{R}^{d_{\text {model}} \times d_{k}}, W_{i}^{K} \in $$ $$\mathbb{R}^{d_{\text {model}} \times d_{k}},$$ $$W_{i}^{V} \in \mathbb{R}^{d_{\text {model}} \times d_{v}} $$ and $$W^O \in \mathbb{R}^{hd_v \times d_{\text {model}}}$$.  
        This paper choses $$h = 8$$ parallel attention layers/_heads_.  
        For each, they use $$d_k=d_v=d_{\text{model}}/h = 64$$.  
        The reduced dimensionality of each head, allows the total computation cost to be similar to that of a single head w/ full dimensionality.   

        __Motivation:__ Multi-head attention allows the model to jointly attend to information from different representation subspaces at different positions. With a single attention head, averaging inhibits this.  
    

    __Applications of Attention in the Model:__{: style="color: red"}  
    The Transformer uses multi-head attention in three different ways:  
    {: #lst-p}
    * __Encode-Decoder Attention Layer__ (standard layer):  
        * The *__queries__* come from: the _previous decoder layer_
        * The memory *__keys__* and *__values__* come from: the _output of the encoder_   

        This allows every position in the decoder to attend over all positions in the input sequence.  
    * __Encoder Self-Attention__:  
        The encoder contains self-attention layers.  
        * Both, The *__queries__*, and *__keys__* and *__values__*, come from: the _encoders output of previous layer_  

        Each position in the encoder can attend to all positions in the previous layer of the encoder.
    * __Decoder Self-Attention__:  
        The decoder, also, contains self-attention layers.  
        * Both, The *__queries__*, and *__keys__* and *__values__*, come from: the _decoders output of previous layer_  

        However, self-attention layers in the decoder allow each position in the decoder to attend to all positions in the decoder _up to_, and including, that _position_. Since, we need to prevent *__leftward information flow__* in the decoder to preserve the *__auto-regressive__* property.  
        This is implemented inside of scaled dot-product attention by masking out (setting to $$-\infty$$ ) all values in the input of the softmax which correspond to illegal connections.  


8. **The Model - Position-wise Feed-Forward Network (FFN):**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents48}  
    In addition to attention sub-layers, each of the layers in our encoder and decoder contains a fully connected feed-forward network, which is applied to each position separately and identically.  
    It consists of *__two linear transformations__* with a *__ReLU__* activation in between:  
    <p>$$\text{FFN}(x) = \max(0, xW_1 + b_1)W_2 + b_2 \tag{2}$$</p>  
    While the __linear transformations__ are the _same_ across different positions, they use _different parameters_ from layer to layer.  
    > Equivalently, we can describe this as, __two convolutions__ with __kernel-size__ $$= 1$$  

    __Dimensional Analysis__:  
    {: #lst-p}
    * Input/Output: $$\in \mathbb{R}^{d_\text{model} = 512} $$  
    * Inner-Layer: $$\in \mathbb{R}^{d_{ff} = 2048} $$  


9. **The Model - Embeddings and Softmax:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents49}  
    Use _learned embeddings_ to convert the __input tokens__ and __output tokens__ to __vectors__ $$\in \mathbb{R}^d_{\text{model}}$$.  
    Use the usual _learned linear transformation_ and _softmax_ to convert __decoder output__ to __predicted next-token probabilities__.  

    The model *__shares__* the same __weight matrix__ between the two embedding layers and the pre-softmax linear transformation.  
    In the embedding layers, multiply those weights by $$\sqrt{d_{\text{model}}}$$.  

10. **The Model - Positional Encoding:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents410}  
    __Motivation:__  
    Since the model contains no recurrence and no convolution, in order for the model to make use of the order of the sequence, we must inject some information about the relative or absolute position of the tokens in the sequence.  

    __Positional Encoding:__  
    A way to add positional information to an embedding.  
    There are many choices of positional encodings, learned and fixed. _[Gehring et al. 2017]_  
    The positional encodings have the same dimension $$d_{\text{model}}$$ as the embeddings, so that the two can be summed.  

    __Approach:__  
    Add "positional encodings" to the input embeddings at the bottoms of the encoder and decoder stacks.  
    Use __sine__ and __cosine__ functions of different frequencies:  
    <p>$$ \begin{aligned} P E_{(\text{pos}, 2 i)} &=\sin \left(\text{pos} / 10000^{2 i / d_{\mathrm{model}}}\right) \\ P E_{(\text{pos}, 2 i+1)} &=\cos \left(\text{pos}/ 10000^{2 i / d_{\mathrm{model}}}\right) \end{aligned} $$</p>  
    where $$\text{pos}$$ is the position and $$i$$ is the dimension.  
    That is, each dimension of the positional encoding corresponds to a sinusoid. The wavelengths form a geometric progression from $$2\pi$$ to $$10000 \cdot 2\pi$$.  

    __Motivation__:  
    We chose this function because we hypothesized it would allow the model to easily learn to attend by relative positions, since for any fixed offset $$k$$, $$PE_{pos + k}$$ can be represented as a linear function of $$P E_{pos}$$. 

    __Sinusoidal VS Learned:__ We chose the sinusoidal version (instead of _learned positional embeddings_, with similar results) because it may allow the model to extrapolate to sequence lengths longer than the ones encountered during training.  


11. **Training Tips & Tricks:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents411}  
    * __Layer Normalization:__ Help ensure that layers remain in reasonable range  
    * __Specialized Training Schedule:__ Adjust default learning rate of the Adam optimizer  
    * __Label Smoothing:__ Insert some uncertainty in the training process  
    * __Masking (for decoder attention):__ for Efficient Training using matrix-operations
    <br>

12. **Why Self-Attention? (as opposed to Conv/Recur. layers):**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents412}  
    ![img](/main_files/dl/nlp/speech_research/6.png){: width="80%"}  \\
    __Total Computational Complexity per Layer:__{: style="color: red"}    
    * Self-Attention layers are faster than recurrent layers when the sequence length $$n$$ is smaller than the representation dimensionality $$d$$.  
        > Which is most often the case with sentence representations used by state-of-the-art models in machine translations, such as word-piece and byte-pair representations.  

    * To improve computational performance for tasks involving very long sequences, self-attention could be restricted to considering only a neighborhood of size $$r$$ in the input sequence centered around the respective output position.  
        This would increase the maximum path length to $$\mathcal{O}(n/r)$$.  

    __Parallelizable Computations:__{: style="color: red"} (measured by the minimum number of sequential ops required)  
    Self-Attention layers connect all positions with a constant number of sequentially executed operations, whereas a recurrent layer requires $$\mathcal{O}(n)$$ sequential operations.  


    __Path Length between Positions:__{: style="color: red"} (Long-Range Dependencies)  
    {: #lst-p}
    * __Convolutional Layers:__ A single convolutional layer with kernel width $$k < n$$ does not connect all pairs of input and output positions.  
        Doing so requires:  
        * __Contiguous Kernels (valid)__: a stack of $$\mathcal{O}(n/k)$$ convolutional layers
        * __Dilated Kernels__: $$\mathcal{O}(\log_k(n))$$  
            increasing the length of the longest paths between any two positions in the network.  
        * __Separable Kernels__: decrease the complexity considerably, to $$\mathcal{O}\left(k \cdot n \cdot d+n \cdot d^{2}\right)$$  
        
        > Convolutional layers are generally more expensive than recurrent layers, by a factor of $$k$$.  

    * __Self-Attention__:  
        Even with $$k = n$$, the complexity of a separable convolution is equal to the combination of a self-attention layer and a point-wise feed-forward layer, the approach taken in this model.  

    __Interpretability:__{: style="color: red"}  
    As side benefit, self-attention could yield more interpretable models.  
    Not only do individual attention heads clearly learn to perform different tasks, many appear to exhibit behavior related to the syntactic and semantic structure of the sentences.  
    <br>

19. **Results:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents419}  
    * __Attention Types__:  
        For small values of $$d_k$$ the two mechanisms perform similarly, additive attention outperforms dot product attention without scaling for larger values of $$d_k$$.  
    * __Positional Encodings__:  
        We also experimented with using learned positional embeddings instead, and found that the two versions produced nearly identical results.  
            

<!-- 5. **Key Insights:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents45}  
    :    -->

***

<!-- ## FIFTH
{: #content5}

1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents51}  
    :   

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents52}  
    :   

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents53}  
    :   

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents54}  
    :   

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents55}  
    :   

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents56}  
    :   

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents57}  
    :   

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents58}  
    :   --> 

*** 

<!-- ## FastText
{: #content6}

1. **Introduction:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents61}  
    This paper proposes a new approach to form word-embeddings based on the skip-gram model, where each word is represented as a bag of character n-grams.

2. **Structure:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents62}    
    * __Input__: sequence of input vectors  
    * __Output__: sequence of output labels
                
3. **Strategy:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents63}  
    The idea is to use one LSTM to read the input sequence, one time step at a time, to obtain large fixed dimensional vector representation, and then to use another LSTM to extract the output sequence from that vector.  
    The second LSTM is essentially a recurrent neural network language model except that it is __conditioned__ on the __input sequence__.

4. **Solves:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents64}  
    * Despite their flexibility and power, DNNs can only be applied to problems whose inputs and targets can be sensibly encoded with vectors of fixed dimensionality. It is a significant limitation, since many important problems are best expressed with sequences whose lengths are not known a-priori.  
        The RNN can easily map sequences to sequences whenever the alignment between the inputs the outputs is known ahead of time. However, it is not clear how to apply an RNN to problems whose input and the output sequences have different lengths with complicated and non-monotonic relationship.  


5. **Key Insights:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents65}  
    * Uses LSTMs to capture the information present in a sequence of inputs into one vector of features that can then be used to decode a sequence of output features  
    * Uses two different LSTM, for the encoder and the decoder respectively  
    * Reverses the words in the source sentence to make use of short-term dependencies (in translation) that led to better training and convergence 

6. **Preparing Data (Pre-Processing):**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents66}  
    :   
                    

7. **Architecture:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents67}  
    :   * __Encoder__:  
            * *__LSTM:__* 
                * 4 Layers:    
                    * 1000 Dimensions per layer
                    * 1000-dimensional word embeddings
        * __Decoder__:  
            * *__LSTM:__* 
                * 4 Layers:    
                    * 1000 Dimensions per layer
                    * 1000-dimensional word embeddings
        * An __Output__ layer made of a standard __softmax function__  
            > over 80,000 words  
        * __Objective Function__:  
            <p>$$\dfrac{1}{\vert \mathbb{S} \vert} \sum_{(T,S) \in \mathbb{S}} \log p(T \vert S)
            $$</p>  
            where $$\mathbb{S}$$ is the training set.  
                
8. **Algorithm:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents68}  
:   * Train a large deep LSTM 
    * Train by maximizing the log probability of a correct translation $$T$$  given the source sentence $$S$$  
    * Produce translations by finding the most likely translation according to the LSTM:   
        <p>$$\hat{T} = \mathrm{arg } \max_{T} p(T \vert S)$$</p>
    * Search for the most likely translation using a simple left-to-right beam search decoder which maintains a small number B of partial hypotheses  
        > A __partial hypothesis__ is a prefix of some translation  
    * At each time-step we extend each partial hypothesis in the beam with every possible word in the vocabulary  
        > This greatly increases the number of the hypotheses so we discard all but the $$B$$  most likely hypotheses according to the model’s log probability  
    * As soon as the “<EOS>” symbol is appended to a hypothesis, it is removed from the beam and is added to the set of complete hypotheses  
    *

9. **Training:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents69}  
    :   * SGD
        * Momentum 
        * Half the learning rate every half epoch after the 5th epoch
        * Gradient Clipping  
            > enforce a hard constraint on the norm of the gradient
        * Sorting input

10. **Parameters:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents610}  
    :   * __Initialization__ of all the LSTM params with __uniform distribution__ $$\in [-0.08, 0.08]$$  
        * __Learning Rate__: $$0.7$$ 
        * __Batches__: $$28$$ sequences
        * __Clipping__: 
                  

11. **Issues/The Bottleneck:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents611}  
    :   * 

12. **Results:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents612}  
    :   

13. **Discussion:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents613}  
    :   *   -->

<!-- 
5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents65}  
    :   

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents66}  
    :   

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents67}  
    :   

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents68}  
    :    -->

<!-- ## Seven
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
    :    -->

<!-- ## Eight
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