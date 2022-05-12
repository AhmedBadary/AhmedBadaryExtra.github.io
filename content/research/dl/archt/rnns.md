---
layout: NotesPage
title: Recurrent Neural Networks <br /> Deep Learning Book Ch.10
permalink: /work_files/research/dl/archits/rnns
prevLink: /work_files/research/dl/archits.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Introduction](#content1)
  {: .TOC1}
<!--   * [SECOND](#content2)
  {: .TOC2}
  * [THIRD](#content3)
  {: .TOC3}
  * [FOURTH](#content4)
  {: .TOC4}
  * [FIFTH](#content5)
  {: .TOC5}
  * [SIXTH](#content6)
  {: .TOC6} -->
</div>

***
***


* [RNNs in NLP](/work_files/research/dl/nlp/rnns)  
* [RNNs in CV](/work_files/research/dl/rnns_cv)  
* [Illustrated Guide to Recurrent Neural Networks: Understanding the Intuition (Vid!)](https://www.youtube.com/watch?v=LHXXI4-IEns)  
* [All of RNNs (ch.10 summary)](https://medium.com/@jianqiangma/all-about-recurrent-neural-networks-9e5ae2936f6e)  
* [TRAINING RECURRENT NEURAL NETWORKS (Illya Stutskever PhD)](http://www.cs.utoronto.ca/~ilya/pubs/ilya_sutskever_phd_thesis.pdf)  
* [Guide to RNNs and LSTMs](https://skymind.ai/wiki/lstm#a-beginners-guide-to-recurrent-networks-and-lstms)  
* [Exploring LSTMs, their Internals and How they Work (Blog!)](https://blog.echen.me/2017/05/30/exploring-lstms/)  
* [A Critical Review of RNNs for Sequence Learning: Complete Overview and Motivation/Interpretations of RNNs (Paper!)](https://arxiv.org/pdf/1506.00019.pdf)  
* [On the difficulty of training Recurrent Neural Networks: Analytical, Geometric, & Dynamical-Systems Perspectives (Paper!)](https://arxiv.org/abs/1211.5063)  
* [The fall of RNN / LSTM for Transformers (Reddit!)](https://www.reddit.com/r/MachineLearning/comments/8ca36k/d_the_fall_of_rnn_lstm_eugenio_culurciello_medium/)  
* [The emergent algebraic structure of RNNs and embeddings in NLP (Paper!)](https://arxiv.org/pdf/1803.02839.pdf)  



## Introduction
{: #content1}

1. **Recurrent Neural Networks:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    __Recurrent Neural Networks (RNNs)__ are a family of neural networks for processing __sequential data__.  

    In an RNN, the connections between units form a _directed cycle_, allowing it to exhibit dynamic temporal behavior.  

    The standard RNN is a __nonlinear dynamical system__ that maps sequences to sequences.  


2. **Big Idea:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    RNNs __share parameters across different positions__/index of time/time-steps of the sequence, which allows it to _generalize well to examples of different sequence length_.  
    * Such sharing is particularly important when a specific piece of information can occur at multiple positions within the sequence.  

    > A related idea, is the use of convolution across a 1-D temporal sequence (_time-delay NNs_). This convolution operation allows the network to share parameters across time but is _shallow_.  
    The output of convolution is a sequence where each member of the output is a function of a small number of neighboring members of the input.  


3. **Dynamical Systems:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    A __Dynamical System__ is a system in which a <span>function</span>{: style="color: purple"} describes the <span>time dependence</span>{: style="color: purple"} of a <span>point</span>{: style="color: purple"} in a <span>geometrical space</span>{: style="color: purple"}.  

    __Classical Form of a Dynamical System:__{: style="color: red"}  
    <p>$$\boldsymbol{s}^{(t)}=f\left(\boldsymbol{s}^{(t-1)} ; \boldsymbol{\theta}\right) \tag{10.1}$$</p>  
    where $$\boldsymbol{s}^{(t)}$$  is called the state of the system.  

    ![img](/main_files/dl/archits/rnns/1.png){: width="100%"}  

    __A Dynamical System driven by an external signal $$\boldsymbol{x}^{(t)}$$__:  
    <p>$$\boldsymbol{s}^{(t)}=f\left(\boldsymbol{s}^{(t-1)}, \boldsymbol{x}^{(t)} ; \boldsymbol{\theta}\right) \tag{10.4}$$</p>  
    the state now contains information about the whole past sequence.   

    Basically, any function containing __recurrence__ can be considered an RNN.  

    __The RNN Equation (as a Dynamical System):__{: style="color: red"}  
    <p>$$\boldsymbol{h}^{(t)}=f\left(\boldsymbol{h}^{(t-1)}, \boldsymbol{x}^{(t)} ; \boldsymbol{\theta}\right) \tag{10.5}$$</p>  
    where the variable $$\mathbf{h}$$ represents the __state__.  

    ![img](/main_files/dl/archits/rnns/2.png){: width="100%"}  
    * [Dynamical Systems (wiki!)](https://en.wikipedia.org/wiki/Dynamical_system)  


4. **Unfolding the Computation Graph:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    __Unfolding__ maps the left to the right in the figure below (from _figure 10.2_) (both are computational graphs of a RNN without output $$\mathbf{o}$$):  
    ![img](/main_files/dl/archits/rnns/3.png){: width="100%"}  
    where the black square indicates that an interaction takes place with a delay of $$1$$ time step, from the state at time $$t$$  to the state at time $$t + 1$$.  

    We can represent the unfolded recurrence after $$t$$ steps with a function $$g^{(t)}$$:  
    <p>$$\begin{aligned} \boldsymbol{h}^{(t)} &=g^{(t)}\left(\boldsymbol{x}^{(t)}, \boldsymbol{x}^{(t-1)}, \boldsymbol{x}^{(t-2)}, \ldots, \boldsymbol{x}^{(2)}, \boldsymbol{x}^{(1)}\right) \\ &=f\left(\boldsymbol{h}^{(t-1)}, \boldsymbol{x}^{(t)} ; \boldsymbol{\theta}\right) \end{aligned}$$</p>  
    The function $$g^{(t)}$$ takes the whole past sequence $$\left(\boldsymbol{x}^{(t)}, \boldsymbol{x}^{(t-1)}, \boldsymbol{x}^{(t-2)}, \ldots, \boldsymbol{x}^{(2)}, \boldsymbol{x}^{(1)}\right)$$ as input and produces the current state, but the unfolded recurrent structure allows us to factorize $$g^{(t)}$$ into _repeated applications of a function $$f$$_.  
    
    The unfolding process, thus, introduces two major advantages:  
    {: #lst-p}
    1. Regardless of the sequence length, the learned model always has the same input size.  
        Because it is specified in terms of transition from one state to another state, rather than specified in terms of a variable-length history of states.  
    2. It is possible to use the _same_ transition function $$f$$ with the same parameters at every time step.  
    Thus, we can learn a single shared model $$f$$ that operates on all time steps and all sequence lengths, rather than needing to learn a separate model $$g^{(t)}$$ for all possible time steps  

    __Benefits:__   
    {: #lst-p}
    * Allows generalization to sequence lengths that did _not_ appear in the training set
    * Enables the model to be estimated to be estimated with far fewer training examples than would be required without parameter sharing.  
    <br>

5. **The State of the RNN $$\mathbf{h}^{(t)}$$:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  
    The network typically learns to use $$\mathbf{h}^{(t)}$$ as a kind of _lossy summary_ of the task-relevant aspects of the past sequence of inputs up to $$t$$.  
    This summary is, in general, _necessarily lossy_, since it maps an arbitrary length sequence $$\left(\boldsymbol{x}^{(t)}, \boldsymbol{x}^{(t-1)}, \boldsymbol{x}^{(t-2)}, \ldots, \boldsymbol{x}^{(2)}, \boldsymbol{x}^{(1)}\right)$$  to a fixed length vector $$h^{(t)}$$.  

    The most demanding situation (the extreme) is when we ask $$h^{(t)}$$ to be rich enough to allow one to approximately recover/reconstruct the input sequence, as in __AutoEncoders__.  

6. **RNN Architectures/Design Patterns:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}  
    We will be introducing three variations of the RNN, and will be analyzing _variation 1_, the basic form of the RNN.  
    1. __Variation 1; The Standard RNN (basic form):__{: #bodyContents161}  
        <button>Architecture</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        ![img](/main_files/dl/archits/rnns/4.png){: width="100%" hidden=""}  
        * __Architecture__:  
            * Produces an output at each time-step
            * Recurrent connections between hidden units  
        * __Equations__:  
            The standard RNN is __parametrized__ with three weight matrices and three bias vectors:  
            <p>$$\theta=\left[W_{h x} = U, W_{h h} = W, W_{o h} = V, b_{h}, b_{o}, h_{0}\right]$$</p>  
            Then given an input sequence $$\left(\boldsymbol{x}^{(t)}, \boldsymbol{x}^{(t-1)}, \boldsymbol{x}^{(t-2)}, \ldots, \boldsymbol{x}^{(2)}, \boldsymbol{x}^{(1)}\right)$$ the RNN performs the following computations for every time step:   
            <p>$$\begin{aligned} \boldsymbol{a}^{(t)} &=\boldsymbol{b}+\boldsymbol{W h}^{(t-1)}+\boldsymbol{U} \boldsymbol{x}^{(t)} \\ \boldsymbol{h}^{(t)} &=\tanh \left(\boldsymbol{a}^{(t)}\right) \\ \boldsymbol{o}^{(t)} &=\boldsymbol{c}+\boldsymbol{V} \boldsymbol{h}^{(t)} \\ \hat{\boldsymbol{y}}^{(t)} &=\operatorname{softmax}\left(\boldsymbol{o}^{(t)}\right) \end{aligned}$$</p>  
            where the parameters are the bias vectors $$\mathbf{b}$$ and $$\mathbf{c}$$ along with the weight matrices $$\boldsymbol{U}$$, $$\boldsymbol{V}$$ and $$\boldsymbol{W}$$, respectively, for input-to-hidden, hidden-to-output and hidden-to-hidden connections.  
            We, also, Assume the hyperbolic tangent activation function, and that the output is discrete[^1].  
        * __The (Total) Loss__:  
            The __Total Loss__ for a given sequence of $$\mathbf{x}$$ values paired with a sequence of $$\mathbf{y}$$ values is the _sum of the losses over all the time steps_. Assuming $$L^{(t)}$$ is the __negative log-likelihood__ of $$y^{(t)}$$ given $$\boldsymbol{x}^{(1)}, \ldots, \boldsymbol{x}^{(t)}$$, then:  
            <p>$$\begin{aligned} & L\left(\left\{\boldsymbol{x}^{(1)}, \ldots, \boldsymbol{x}^{(\tau)}\right\},\left\{\boldsymbol{y}^{(1)}, \ldots, \boldsymbol{y}^{(\tau)}\right\}\right) \\=& \sum_{t} L^{(t)} \\=& -\sum_{t} \log p_{\text { model }}\left(y^{(t)} |\left\{\boldsymbol{x}^{(1)}, \ldots, \boldsymbol{x}^{(t)}\right\}\right) \end{aligned}$$</p>  
            where $$p_{\text { model }}\left(y^{(t)} |\left\{\boldsymbol{x}^{(1)}, \ldots, \boldsymbol{x}^{(t)}\right\}\right)$$ is given by reading the entry for $$y^{(t)}$$ from the model's output vector $$\hat{\boldsymbol{y}}^{(t)}$$.  
        * __Complexity__:  
            * __Forward Pass__:  
                The runtime is $$\mathcal{O}(\tau)$$ and cannot be reduced by parallelization because the forward propagation graph is inherently sequential; each time step may only be computed after the previous one.  
            * __Backward Pass__:  
                The standard algorithm used is called __Back-Propagation Through Time (BPTT)__, with a runtime of $$\mathcal{O}(\tau)$$  
                                 
        * __Properties__:  
            * The Standard RNN is __Universal__, in the sense that any function computable by a __Turing Machine__ can be computed by such an RNN of a _finite size_.  
                > The functions computable by a Turing machine are discrete, so these results regard exact implementation of the function, not approximations.  
                The RNN, when used as a Turing machine, takes a binary sequence as input, and its outputs must be discretized to provide a binary output.  

            * The output can be read from the RNN after a number of time steps that is asymptotically linear in the number of time steps used by the Turing machine and asymptotically linear in the length of the input (_Siegelmann and Sontag, 1991; Siegelmann, 1995; Siegelmann and Sontag, 1995; Hyotyniemi, 1996_).  
            * The theoretical RNN used for the proof can simulate an __unbounded stack__ by representing its activations and weights with rational numbers of unbounded precision.  

    2. __Variation 2:__{: #bodyContents162}  
        <button>Architecture</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        ![img](/main_files/dl/archits/rnns/5.png){: width="100%" hidden=""}  
        * __Architecture__:  
            * Produces an output at each time-step  
            * Recurrent connections _only_ from the output at one time step to the hidden units at the next time step  
        * __Equations__:  
            <p>$$\begin{aligned} \boldsymbol{a}^{(t)} &=\boldsymbol{b}+\boldsymbol{W o}^{(t-1)}+\boldsymbol{U} \boldsymbol{x}^{(t)} \\
            \boldsymbol{h}^{(t)} &=\tanh \left(\boldsymbol{a}^{(t)}\right) \\
            \boldsymbol{o}^{(t)} &=\boldsymbol{c}+\boldsymbol{V} \boldsymbol{h}^{(t)} \\
            \hat{\boldsymbol{y}}^{(t)} &=\operatorname{softmax}\left(\boldsymbol{o}^{(t)}\right) \end{aligned}$$</p>  
        * __Properties__:  
            * Strictly __less powerful__ because it _lacks hidden-to-hidden recurrent connections_.  
                It __cannot__ simulate a _universal Turing Machine_.  
            * It requires that the output units capture all the information about the past that the network will use to predict the future; due to the lack of hidden-to-hidden recurrence.  
                But, since the outputs are trained to match the training set targets, they are unlikely to capture the necessary information about the past history.  
            * The __Advantage__ of eliminating hidden-to-hidden recurrence is that all the time steps are __de-coupled__[^2]. Training can thus be parallelized, with the gradient for each step $$t$$ computed in isolation.  
                Thus, the model can be trained with [__Teacher Forcing__](#bodyContents17).  
                

    3. __Variation 3:__{: #bodyContents163}  
        <button>Architecture</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        ![img](/main_files/dl/archits/rnns/6.png){: width="100%" hidden=""}  
        * __Architecture__:  
            * Produces a _single_ output, after reading entire sequence
            * Recurrent connections between hidden units
        * __Equations__:  
            <p>$$\begin{aligned} \boldsymbol{a}^{(t)} &=\boldsymbol{b}+\boldsymbol{W h}^{(t-1)}+\boldsymbol{U} \boldsymbol{x}^{(t)} \\
            \boldsymbol{h}^{(t)} &=\tanh \left(\boldsymbol{a}^{(t)}\right) \\
            \boldsymbol{o} = \boldsymbol{o}^{(T)} &=\boldsymbol{c}+\boldsymbol{V} \boldsymbol{h}^{(T)} \\
            \hat{\boldsymbol{y}} = \hat{\boldsymbol{y}}^{(T)} &=\operatorname{softmax}\left(\boldsymbol{o}^{(T)}\right) \end{aligned}$$</p>  


7. **Teacher Forcing:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}  
    Teacher forcing is a procedure that emerges from the maximum likelihood criterion, in which during training the model receives the ground truth output $$y^{(t)}$$ as input at time $$t + 1$$.  
    
    Models that have recurrent connections from their _outputs_ leading _back into the model_ may be trained with teacher forcing.  

    Teacher forcing may still be applied to models that have hidden-to-hidden connections as long as they have connections from the output at one time step to values computed in the next time step. As soon as the hidden units become a function of earlier time steps, however, the BPTT algorithm is necessary. Some models may thus be trained with both teacher forcing and BPTT.  

    The __disadvantage__ of strict teacher forcing arises if the network is going to be later used in an __closed-loop__ mode, with the network outputs (or samples from the output distribution) fed back as input. In this case, the fed-back inputs that the network sees during training could be quite different from the kind of inputs that it will see at test time.  
    
    __Methods for Mitigation:__  
    {: #lst-p}
    1. Train with both teacher-forced inputs and free-running inputs, for example by predicting the correct target a number of steps in the future through the unfolded recurrent output-to-input paths[^3].  
    2. Another approach (_Bengio et al., 2015b_) to mitigate the gap between the inputs seen at training time and the inputs seen at test time randomly chooses to use generated values or actual data values as input. This approach exploits a curriculum learning strategy to gradually use more of the generated values as input.

    > proof: p.377, 378  

9. **Computing the Gradient in an RNN:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents19}  
    > Note: The computation is, as noted before, w.r.t. the [__standard RNN (variation 1)__](#bodyContents161)  

    Computing the gradient through a recurrent neural network is straightforward. One simply applies the generalized back-propagation algorithm of _section 6.5.6_ to the unrolled computational graph. No specialized algorithms are necessary.  

    <button>Derivation</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](/main_files/dl/archits/rnns/7.png){: width="100%" hidden=""}  
    Once the gradients on the internal nodes of the computational graph are obtained, we can obtain the gradients on the parameter nodes, which have descendents at all the time steps:  
    <button>Derivation Cont'd</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](/main_files/dl/archits/rnns/8.png){: width="100%" hidden=""}  

    __Notes:__  
    {: #lst-p}
    * We do not need to compute the gradient with respect to $$\mathbf{x}^{(t)}$$ for training because it does not have any parameters as ancestors in the computational graph defining the loss.  
    <br>

    
    [^1]: A natural way to represent discrete variables is to regard the output $$\mathbf{o}$$ as giving the unnormalized log probabilities of each possible value of the discrete variable. We can then apply the softmax operation as a post-processing step to obtain a vector $$\hat{\boldsymbol{y}}$$ of normalized probabilities over the output.  
    [^2]: for any loss function based on comparing the prediction at time $$t$$ to the training target at time $$t$$.  
    [^3]: In this way, the network can learn to take into account input conditions (such as those it generates itself in the free-running mode) not seen during training and how to map the state back toward one that will make the network generate proper outputs after a few steps.  
    

10. **Recurrent Networks as Directed Graphical Models:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents110}  
    Since we wish to interpret the _output_ of an RNN as a _probability distribution_, we usually use the __cross-entropy__ associated with that distribution to define the _loss_.  
    > E.g. Mean squared error is the cross-entropy loss associated with an output distribution that is a unit Gaussian.  

    When we use a _predictive log-likelihood training objective_, such as equation 10.12, we train the RNN to _estimate the conditional distribution_ of the next sequence element $$\boldsymbol{y}^{(t)}$$ given the past inputs. This may mean that we maximize the log-likelihood:  
    <p>$$\log p\left(\boldsymbol{y}^{(t)} | \boldsymbol{x}^{(1)}, \ldots, \boldsymbol{x}^{(t)}\right) \tag{10.29}$$</p>  
    or, if the model includes connections from the output at one time step to the nexttime step,  
    <p>$$\log p\left(\boldsymbol{y}^{(t)} | \boldsymbol{x}^{(1)}, \ldots, \boldsymbol{x}^{(t)}, \boldsymbol{y}^{(1)}, \ldots, \boldsymbol{y}^{(t-1)}\right) \tag{10.30}$$</p>  
    Decomposing the joint probability over the sequence of $$\mathbf{y}$$ values as a series of one-step probabilistic predictions is one way to capture the _full joint distribution_ across the whole sequence. When we do not feed past $$\mathbf{y}$$ values as inputs that condition the next step prediction, the outputs $$\mathbf{y}$$ are __conditionally independent__ given the sequence of $$\mathbf{x}$$ values.  



    __Summary:__{: style="color: red"}  
    This section is useful for understanding RNN from a _probabilistic graphical model_ perspective. The main point is to show that __RNN provides a very efficient parametrization of the *joint distribution* over the observations $$y^{(t)}$$.__  
    The introduction of _hidden state_ and _hidden-to-hidden_ connections can be motivated as reducing [fig 10.7]() to [fig 10.8](); which have $$\mathcal{O}(k^{\tau})$$ and $$\mathcal{O}(1)\times \tau$$ parameters, respectively (where $$\tau$$ is the length of the sequence).  
    <br>


18. **Backpropagation Through Time:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents118}  
    * We can think of the recurrent net as a layered, feed-forward net with shared weights and then train the feed-forward net with (linear) weight constraints.
    * We can also think of this training algorithm in the time domain:
        * The forward pass builds up a stack of the activities of all the units at each time step
        * The backward pass peels activities off the stack to compute the error derivatives at each time step
        * After the backward pass we add together the derivatives at all the different times for each weight.  
    <br>


19. **Downsides of RNNs:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents119}  
    * RNNs are not __Inductive__: They memorize sequences extremely well, but they don’t necessarily always show convincing signs of generalizing in the correct way.  
    * They unnecessarily __couple their representation size to the amount of computation per step__: if you double the size of the hidden state vector you’d quadruple the amount of FLOPS at each step due to the matrix multiplication.  
        > Ideally, we’d like to maintain a huge representation/memory (e.g. containing all of Wikipedia or many intermediate state variables), while maintaining the ability to keep computation per time step fixed.  
    <br>


20. **RNNs as a model with Memory \| Comparison with other Memory models:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents120}  
    [Modeling Sequences](/concepts_#bodyContents23)  


__NOTES:__  
{: #lst-p}
* RNNs may also be applied in two dimensions across spatial data such as images  
* A __Deep RNN in vertical dim (stacking up hidden layers)__ increases the memory representational ability with _linear scaling in computation_ (as opposed to increasing the size of the hidden layer -> quadratic computation).  
* A __Deep RNN in time-dim (add extra pseudo-steps for each real step)__ increase ONLY the representational ability (efficiency) and NOT memory.  
* __Dropout in Recurrent Connections__: dropout is ineffective when applied to recurrent connections as repeated random masks zero all hidden units in the limit. The most common solution is to only apply dropout to non-recurrent connections.  
* **Different Connections in RNN Architectures:**  
    1. __PeepHole Connection:__  
        is an addition on the equations of the __LSTM__ as follows:  
        <p>$$ \Gamma_o = \sigma(W_o[a^{(t-1)}, x^{(t)}] + b_o) \\
        \implies 
        \sigma(W_o[a^{(t-1)}, x^{(t)}, c^{(t-1)}] + b_o)$$</p>  
        Thus, we add the term $$c^{(t-1)}$$ to the output gate.  
* __Learning Long-Range Dependencies in RNNs/sequence-models__:  
    One key factor affecting the ability to learn such dependencies is the length of the paths forward and backward signals have to traverse in the network. The shorter these paths between any combination of positions in the input and output sequences, the easier it is to learn long-range dependencies.  
* __LSTM (simple) Implementation__: [github](https://github.com/nicodjimenez/lstm), [blog](http://nicodjimenez.github.io/2014/08/08/lstm.html)
* [**Sampling from RNNs**](https://medium.com/machine-learning-at-petiteprogrammer/sampling-strategies-for-recurrent-neural-networks-9aea02a6616f){: value="show" onclick="iframePopA(event)"}
<a href="https://medium.com/machine-learning-at-petiteprogrammer/sampling-strategies-for-recurrent-neural-networks-9aea02a6616f"></a>
    <div markdown="1"> </div>    
* __Gradient Clipping Intuition__:  
    ![img](/main_files/concepts/1.png){: width="55%"}   
    * The image above is that of the __Error Surface__ of a _single hidden unit RNN_  
    * The observation here is that there exists __High Curvature Walls__.   
        This Curvature Wall will move the gradient to a very different/far, probably less useful area. 
        Thus, if we clip the gradients we will avoid the walls and will remain in the more useful area that we were exploring already.   
    Draw a line between the original point on the Error graph and the End (optimized) point then evaluate the Error on points on that line and look at the changes $$\rightarrow$$ this shows changes in the curvature.  

<!-- ***

## SECOND
{: #content2}

1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents26}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents27}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents28}

***

## THIRD
{: #content3}

1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents34}

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents35}

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents36}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents37}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents38}

 -->