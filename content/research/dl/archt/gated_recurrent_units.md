---
layout: NotesPage
title: Gated Units <br /> RNN Architectures
permalink: /work_files/research/dl/nlp/gated_units
prevLink: /work_files/research/dl/nlp.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [GRUs](#content2)
  {: .TOC2}
  * [LSTMs](#content3)
  {: .TOC3}
</div>

***
***


* [Building an LSTM from Scratch in PyTorch](http://mlexplained.com/category/fromscratch/)  
* [Exploring LSTMs, their Internals and How they Work (Blog!)](https://blog.echen.me/2017/05/30/exploring-lstms/)  


## GRUs
{: #content2}

1. **Gated Recurrent Units:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    __Gated Recurrent Units (GRUs)__ are a class of modified (_**Gated**_) RNNs that allow them to combat the _vanishing gradient problem_ by allowing them to capture more information/long range connections about the past (_memory_) and decide how strong each signal is.  
    <br>

2. **Main Idea:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}  
    Unlike _standard RNNs_ which compute the hidden layer at the next time step directly first, __GRUs__ computes two additional layers (__gates__) (Each with different weights):  
    {: #lst-p}
    * *__Update Gate__*:  
        <p>$$z_t = \sigma(W^{(z)}x_t + U^{(z)}h_{t-1})$$</p>  
    * *__Reset Gate__*:  
        <p>$$r_t = \sigma(W^{(r)}x_t + U^{(r)}h_{t-1})$$</p>  

    The __Update Gate__ and __Reset Gate__ computed, allow us to more directly influence/manipulate what information do we care about (and want to store/keep) and what content we can ignore.  
    
    We can view the actions of these gates from their respecting equations as:  
    {: #lst-p}
    * *__New Memory Content__*:  
        at each hidden layer at a given time step, we compute some new memory content,  
        if the reset gate $$ = \approx 0$$, then this ignores previous memory, and only stores the new word information.  
        <p>$$ \tilde{h}_ t = \tanh(Wx_t + r_t \odot Uh_{t-1})$$</p>  
    * *__Final Memory__*:  
        the actual memory at a time step $$t$$, combines the _Current_ and _Previous time steps_,  
        if the _update gate_ $$ = \approx 0$$, then this, again, ignores the _newly computed memory content_, and keeps the old memory it possessed.  
        <p>$$h_ t = z_ t \odot h_ {t-1} + (1-z_t) \odot \tilde{h}_ t$$</p>  

***

## Long Short-Term Memory
{: #content3}

1. **LSTM:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}  
    The __Long Short-Term Memory__ (LSTM) Network is a special case of the Recurrent Neural Network (RNN) that uses special gated units (a.k.a LSTM units) as building blocks for the layers of the RNN.  
    
    __LSTM Equations:__  
    <p>
    $$\begin{align}
        f_{t}&=\sigma_{g}\left(W_{f} x_{t}+U_{f} h_{t-1}+b_{f}\right) \\
        i_{t}&=\sigma_{g}\left(W_{i} x_{t}+U_{i} h_{t-1}+b_{i}\right) \\
        o_{t}&=\sigma_{g}\left(W_{o} x_{t}+U_{o} h_{t-1}+b_{o}\right) \\
        c_{t}&=f_{t} \circ c_{t-1}+i_{t} \circ \sigma_{c}\left(W_{c} x_{t}+U_{c} h_{t-1}+b_{c}\right) \\
        h_{t}&=o_{t} \circ \sigma_{h}\left(c_{t}\right)
    \end{align}$$  
    </p>  
    where:  
    $$\sigma_{g}$$: sigmoid function.  
    $${\displaystyle \sigma_{c}}$$: hyperbolic tangent function.  
    $${\displaystyle \sigma_{h}}$$: hyperbolic tangent function or, as the peephole LSTM paper suggests, $${\displaystyle \sigma_{h}(x)=x}$$.  
    <br>

2. **Architecture:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}  
    The LSTM, usually, has four gates:  
    {: #lst-p}
    * __Input Gate__:  
        The input gate determines how much does the _current input vector (current cell)_ matters      
        It controls the extent to which a new value flows into the cell  
        <p>$$i_t = \sigma(W^{(i)}x_t + U^{(i)}h_{t-1})$$</p>   
    * __Forget Gate__:  
        Determines how much of the _past memory_, that we have kept, is still needed   
        It controls the extent to which a value remains in the cell  
        <p>$$f_t = \sigma(W^{(f)}x_t + U^{(f)}h_{t-1})$$</p>   
    * __Output Gate__: 
        Determines how much of the _current cell_ matters for our _current prediction (i.e. passed to the sigmoid)_  
        It controls the extent to which the value in the cell is used to compute the output activation of the LSTM unit  
        <p>$$o_t = \sigma(W^{(o)}x_t + U^{(o)}h_{t-1})$$</p>  
    * __Memory Cell__: 
        The memory cell is the cell that contains the _short-term memory_ collected from each input  
        <p>$$\begin{align}
        \tilde{c}_t & = \tanh(W^{(c)}x_t + U^{(c)}h_{t-1}) & \text{New Memory} \\
        c_t & = f_t \odot c_{t-1} + i_t \odot \tilde{c}_ t & \text{Final Memory}
        \end{align}$$</p>  
        The __Final Hidden State__ is calculated as follows:  
        <p>$$h_t = o_t \odot \sigma(c_t)$$</p>  


3. **Properties:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}  
    * __Syntactic Invariance__:  
        When one projects down the vectors from the _last time step hidden layer_ (with PCA), one can observe the spatial localization of _syntacticly-similar sentences_  
        ![img](/main_files/dl/nlp/9/5.png){: width="100%"}  


__LSTMS:__  
* The core of the history/memory is captured in the _cell-state $$c_{n}$$_ instead of the hidden state $$h_{n}$$.  
* (&) __Key Idea:__ The update to the cell-state $$c_{n}=c_{n-1}+\operatorname{tanh}\left(V\left[w_{n-1} ; h_{n-1}\right]+b_{c}\right)$$  here are __additive__. (differentiating a sum gives the identity) Making the gradient flow nicely through the sum. As opposed to the multiplicative updates to $$h_n$$ in vanilla RNNs.  
    > There is non-linear funcs applied to the history/context cell-state. It is composed of linear functions. Thus, avoids gradient shrinking.  

* In the recurrency of the LSTM the activation function is the identity function with a derivative of 1.0. So, the backpropagated gradient neither vanishes or explodes when passing through, but remains constant.
* By the selective read, write and forget mechanism (using the gating architecture) of LSTM, there exist at least one path, through which gradient can flow effectively from $$L$$  to $$\theta$$. Hence no vanishing gradient.   
* However, one must remember that, this is not the case for exploding gradient. It can be proved that, there __can exist__ at-least one path, thorough which gradient can explode.  
* LSTM decouples cell state (typically denoted by c) and hidden layer/output (typically denoted by h), and only do additive updates to c, which makes memories in c more stable. Thus the gradient flows through c is kept and hard to vanish (therefore the overall gradient is hard to vanish). However, other paths may cause gradient explosion.  
* The Vanishing gradient solution for LSTM is known as _Constant Error Carousel_.  
* [**Why can RNNs with LSTM units also suffer from “exploding gradients”?**](https://stats.stackexchange.com/questions/320919/why-can-rnns-with-lstm-units-also-suffer-from-exploding-gradients/339129#339129){: value="show" onclick="iframePopA(event)"}
<a href="https://stats.stackexchange.com/questions/320919/why-can-rnns-with-lstm-units-also-suffer-from-exploding-gradients/339129#339129"></a>
    <div markdown="1"> </div>    
* [Lecture on gradient flow paths through gates](https://www.cse.iitm.ac.in/~miteshk/CS7015/Slides/Teaching/pdf/Lecture15.pdf)  

* [**LSTMs (Lec Oxford)**](https://www.youtube.com/embed/eDUaRvMDs-s?start=775){: value="show" onclick="iframePopA(event)"}
<a href="https://www.youtube.com/embed/eDUaRvMDs-s?start=776"></a>
    <div markdown="1"> </div>    


__Important Links:__  
[The unreasonable effectiveness of Character-level Language Models](https://nbviewer.jupyter.org/gist/yoavg/d76121dfde2618422139)  
[character-level language model with a Vanilla Recurrent Neural Network, in Python/numpy](https://gist.github.com/karpathy/d4dee566867f8291f086)  
[Visualizing and Understanding Recurrent Networks - Karpathy Lec](https://skillsmatter.com/skillscasts/6611-visualizing-and-understanding-recurrent-networks)  
[Cool LSTM Diagrams - blog](https://medium.com/mlreview/understanding-lstm-and-its-diagrams-37e2f46f1714)  
[Illustrated Guide to Recurrent Neural Networks: Understanding the Intuition](https://www.youtube.com/watch?v=LHXXI4-IEns)  
[Code LSTM in Python](https://iamtrask.github.io/2015/11/15/anyone-can-code-lstm/)  
[Mikolov Thesis: STATISTICAL LANGUAGE MODELS BASED ON NEURAL NETWORKS](http://www.fit.vutbr.cz/~imikolov/rnnlm/thesis.pdf)  
