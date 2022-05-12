---
layout: NotesPage
title: Neural Machine Translation <br /> 
permalink: /work_files/research/dl/nlp/nmt
prevLink: /work_files/research/dl/nlp.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Machine Translation](#content1)
  {: .TOC1}
  * [GRUs](#content2)
  {: .TOC2}
  * [LSTMs](#content3)
  {: .TOC3}
  * [Neural Machine Translation](#content4)
  {: .TOC4}
</div>

***
***

## Machine Translation
{: #content1}

1. **Methods:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    :   * Methods are _statistical_  
        * Uses _parallel corpora_

3. **Traditional MT:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13} 
    :   Traditional MT was very complex and included multiple disciplines coming in together.  
        The systems included many independent parts and required a lot of human engineering and experts.  
        The systems also scaled very poorly as the search problem was essentially exponential.

2. **Statistical Machine Translation Systems:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12} 
    :   * __Input__:  
            * __Source Language__: $$f$$  
            * __Target Language__: $$e$$  
        * __The Probabilistic Formulation__:  
    :   $$ \hat{e} = \mathrm{arg\,min}_e \: p(e \vert f) = \mathrm{arg\,min}_e \: p(f \vert e) p(e)$$
    :   * __The Translation Model $$p(f \vert e)$$__: trained on parallel corpus
        * __The Language Model $$p(e)$$__: trained on English only corpus  
        > Abundant and free!
    :   ![img](/main_files/dl/nlp/9/1.png){: width="100%"}     


4. **Deep Learning Naive Approach:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    :   One way we can learn to translate is to learn to _translate directly with an RNN_. 
    :   ![img](/main_files/dl/nlp/9/2.png){: width="80%"}  
    :   * __The Model__:  
            * *__Encoder__* :  
                $$h_t = \phi(h_{t-1}, x_t) = f(W^{(hh)}h_{t-1} + W^{(hx)}x_t)$$
            * *__Decoder__* :  
                $$\begin{align}
                    h_t & = \phi(h_{t-1}) = f(W^{(hh)}h_{t-1}) \\
                    y_t & = \text{softmax}(W^{(S)}h_t)
                    \end{align}$$  
            * *__Error__* :  
                $$\displaystyle{\max_\theta \frac{1}{N} \sum_{n=1}^N \log p_\theta(y^{(n)}\vert x^{(n)})}$$  
                > Cross Entropy Error.  
            * *__Goal__* :  
                Minimize the __Cross Entropy Error__ for all target words conditioned on source words
    :   * __Drawbacks__:  
            The problem of this approach lies in the fact that the last hidden layer needs to capture the entire sentence to be translated.  
            However, since we know that the _RNN Gradient_ basically __vanishes__ as the length of the sequence increases, the last hidden layer is usually only capable of capturing upto ~5 words.
    :   ![img](/main_files/dl/nlp/9/3.png){: width="100%"}     

5. **Naive RNN Translation Model Extension:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15} 
    :   1. Train Different RNN weights for encoding and decoding
            ![img](/main_files/dl/nlp/9/4.png){: width="100%"}   
        2. Compute every hidden state in the decoder from the following concatenated vectors :  
            * Previous hidden state (standard)
            * Last hidden vector of encoder $$c=h_T$$  
            * Previous predicted output word $$y_{t-1}$$.  
            $$\implies h_{D, t} = \phi_D(h_{t-1}, c, y_{t-1})$$  
            > NOTE: Each input of $$\phi$$ has its own linear transformation matrix.  
        3. Train stacked/deep RNNs with multiple layers. 
        4. Potentially train Bidirectional Encoder
        5. Train input sequence in reverser order for simpler optimization problem:  
            Instead of $$A\:B\:C \rightarrow X\:Y$$ train with $$ C\:B\:A \rightarrow X\:Y$$  
        6. Better Units (Main Improvement):  
            * Use more complex hidden unit computation in recurrence
            * Use GRUs _(Cho et al. 2014)_  
            * _Main Ideas_:
                * Keep around memories to capture long distance dependencies
                * Allow error messages to flow at different strengths depending on the inputs

***

## GRUs
{: #content2}

1. **Gated Recurrent Units:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21} 
    :   __Gated Recurrent Units (GRUs)__ are a class of modified (_**Gated**_) RNNs that allow them to combat the _vanishing gradient problem_ by allowing them to capture more information/long range connections about the past (_memory_) and decide how strong each signal is.  

2. **Main Idea:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22} 
    :   Unlike _standard RNNs_ which compute the hidden layer at the next time step directly first, __GRUs__ computes two additional layers (__gates__):  
        > Each with different weights
    :   * *__Update Gate__*:  
    :   $$z_t = \sigma(W^{(z)}x_t + U^{(z)}h_{t-1})$$  
    :   * *__Reset Gate__*:  
    :   $$r_t = \sigma(W^{(r)}x_t + U^{(r)}h_{t-1})$$  
    :   The __Update Gate__ and __Reset Gate__ computed, allow us to more directly influence/manipulate what information do we care about (and want to store/keep) and what content we can ignore.  
        We can view the actions of these gates from their respecting equations as:  
    :   * *__New Memory Content__*:  
            at each hidden layer at a given time step, we compute some new memory content,  
            if the reset gate $$ = ~0$$, then this ignores previous memory, and only stores the new word information.  
    :   $$ \tilde{h}_t = \tanh(Wx_t + r_t \odot Uh_{t-1})$$
    :   * *__Final Memory__*:  
            the actual memory at a time step $$t$$, combines the _Current_ and _Previous time steps_,  
            if the _update gate_ $$ = ~0$$, then this, again, ignores the _newly computed memory content_, and keeps the old memory it possessed.  
    :   $$h_t = z_t \odot h_{t-1} + (1-z_t) \odot \tilde{h}_t$$  

***

## Long Short-Term Memory
{: #content3}

1. **LSTM:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31} 
    :   The __Long Short-Term Memory__ (LSTM) Network is a special case of the Recurrent Neural Network (RNN) that uses special gated units (a.k.a LSTM units) as building blocks for the layers of the RNN.  

2. **Architecture:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32} 
    :   The LSTM, usually, has four gates:  
    :   * __Input Gate__: 
            The input gate determines how much does the _current input vector (current cell)_ matters      
    :   $$i_t = \sigma(W^{(i)}x_t + U^{(i)}h_{t-1})$$ 
    :   * __Forget Gate__: 
            Determines how much of the _past memory_, that we have kept, is still needed   
    :   $$i_t = \sigma(W^{(i)}x_t + U^{(i)}h_{t-1})$$ 
    :   * __Output Gate__: 
            Determines how much of the _current cell_ matters for our _current prediction (i.e. passed to the sigmoid)_
    :   $$i_t = \sigma(W^{(i)}x_t + U^{(i)}h_{t-1})$$  
    :   * __Memory Cell__: 
            The memory cell is the cell that contains the _short-term memory_ collected from each input
    :   $$\begin{align}
            \tilde{c}_t & = \tanh(W^{(c)}x_t + U^{(c)}h_{t-1}) & \text{New Memory} \\
            c_t & = f_t \odot c_{t-1} + i_t \odot \tilde{c}_t & \text{Final Memory}
        \end{align}$$
    :   The __Final Hidden State__ is calculated as follows:  
    :   $$h_t = o_t \odot \sigma(c_t)$$
     

3. **Properties:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33} 
    :   * __Syntactic Invariance__:  
            When one projects down the vectors from the _last time step hidden layer_ (with PCA), one can observe the spatial localization of _syntacticly-similar sentences_  
            ![img](/main_files/dl/nlp/9/5.png){: width="100%"}  

***

## Neural Machine Translation (NMT)
{: #content4}

1. **NMT:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents41} 
    :   __NMT__ is an approach to machine translation that uses a large artificial neural network to predict the likelihood of a sequence of words, typically modeling entire sentences in a single integrated model.

2. **Architecture:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents42} 
    :   The approach uses an __Encoder-Decoder__ architecture.
    :   ![img](/main_files/dl/nlp/9/6.png){: width="70%"}   
    :   NMT models can be seen as a special case of _language models_.   
        In other words, they can be seen as __Conditional Recurrent Language Model__; a language model that has been conditioned on the calculated _encoded_ vector representation of the sentence.

3. **Modern Sequence Models for NMT:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents43} 
    :   

4. **Issues of NMT:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents44} 
    :   * __Predicting Unseen Words__:  
            The NMT model is very vulnerable when presented with a word that it has never seen during training (e.g. a new name).  
            In-fact, the model might not even be able to place the (translated) unseen word correctly in the (translated) sentence.
        * __Solution__:  
            * A possible solution is to apply _character-based_ translation, instead of word-based, however, this approach makes for very long sequences and the computation becomes infeasible.  
            * The (current) proposed approach is to use a __Mixture Model of Softmax and Pointers__  
                > _Pointer-sentinel Model_

5. **The Big Wins of NMT:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents45} 
    :   1. __End-to-End Training__: All parameters are simultaneously optimized to minimize a loss function on the networks output 
        2. __Distributed Representations Share Strength__: Better exploitation of word and phrase similarities 
        3. __Better Exploitation of Context__: NMT can use a much bigger context - both source and partial target text - to translate more accurately
        4. __More Fluent Text Generation__: Deep Learning text generation is much higher quality

    <button>Progress in Google Translate based on a one sentence test set from C. Manning</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/98YBK9uTfTjaWBXPimGFvYaiNz-USCPkLQbn9xNQXc8.original.fullsize.png){: width="100%" hidden=""}  

    <button>Google Translate BLEU Score Progression</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://1.bp.blogspot.com/-dvf6wpOpJC0/XtgVORHbA4I/AAAAAAAAGDc/I3a6N8uHzsQicDth9XfROnwb3dye8Pw3gCLcBGAsYHQ/s1600/image1.gif){: width="100%" hidden=""}  


8. **(GNMT) Google's Multilingual Neural Machine Translation System - Zero shot Translation:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents48} 
    :   * __Multilingual NMT Approaches__:  
    :   ![img](/main_files/dl/nlp/9/7.png){: width="100%"}   
    :   * __Google's Approach__:  
            Add an __*Artificial Token*__ at the beginning of the input sentence to indicate the target language.  



__Notes:__{: style="color: red"}  
{: #lst-p}
* __Evaluation Metrics:__  __BLEU Score:__{: style="color: red"} or Bilingual Evaluation Understudy Score  
    The second most popular score is __METEOR__{: style="color: red"}: which has an emphasis on recall and precision.  
:  
<br>