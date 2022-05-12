---
layout: NotesPage
title: Activation Functions
permalink: /work_files/research/dl/concepts/activation_funcs
prevLink: /work_files/research/dl/concepts.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Introduction](#content1)
  {: .TOC1}
  * [Activation Functions](#content2)
  {: .TOC2}
</div>

***
***


* [Comprehensive list of activation functions in neural networks with pros/cons](https://stats.stackexchange.com/questions/115258/comprehensive-list-of-activation-functions-in-neural-networks-with-pros-cons)  
* [State Of The Art Activation Function: GELU, SELU, ELU, ReLU and more. With visualization of the activation functions and their derivatives (reddit!)](https://www.reddit.com/r/MachineLearning/comments/dekblo/d_state_of_the_art_activation_function_gelu_selu/)  




## Introduction
{: #content1}

1. **Activation Functions:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    In NNs, the __activation function__ of a node defines the output of that node given an input or set of inputs.  
    The activation function is an abstraction representing the rate of action potential firing in the cell.  
    <br>

    <!-- 2. **Motivation:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}   -->

3. **Desirable Properties:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    * __Non-Linearity__:  
    When the activation function is non-linear, then a two-layer neural network can be proven to be a universal function approximator. The identity activation function does not satisfy this property. When multiple layers use the identity activation function, the entire network is equivalent to a single-layer model. 
    * __Range__:  
    When the range of the activation function is finite, gradient-based training methods tend to be more stable, because pattern presentations significantly affect only limited weights. When the range is infinite, training is generally more efficient because pattern presentations significantly affect most of the weights. In the latter case, smaller learning rates are typically necessary.  
    * __Continuously Differentiable__:  
    This property is desirable for enabling gradient-based optimization methods. The binary step activation function is not differentiable at 0, and it differentiates to 0 for all other values, so gradient-based methods can make no progress with it.
    * __Monotonicity__:  
        * When the activation function is monotonic, the error surface associated with a single-layer model is guaranteed to be convex.  
        * During the training phase, backpropagation informs each neuron how much it should influence each neuron in the next layer. If the activation function isn't monotonic then increasing the neuron's weight might cause it to have less influence, the opposite of what was intended.  
            > However, Monotonicity isn't required. Several papers use non monotonic trained activation functions.  
            > Gradient descent finds a local minimum even with non-monotonic activation functions. It might only take longer.  
        * From a biological perspective, an "activation" depends on the sum of inputs, and once the sum surpasses a threshold, "firing" occurs. This firing should happen even if the sum surpasses the threshold by a small or a large amount; making monotonicity a desirable property to not limit the range of the "sum".  
    * __Smoothness with Monotonic Derivatives__:  
    These have been shown to generalize better in some cases.  
    * __Approximating Identity near Origin__:  
    Equivalent to $${\displaystyle f(0)=0}$$ and $${\displaystyle f'(0)=1}$$, and $${\displaystyle f'}$$ is continuous at $$0$$.  
    When activation functions have this property, the neural network will learn efficiently when its weights are initialized with small random values. When the activation function does not approximate identity near the origin, special care must be used when initializing the weights.  
    * __Zero-Centered Range__:  
    Has effects of centering the data (zero mean) by centering the activations. Makes learning easier.   
    > [WHY NORMALIZING THE DATA/SIGNAL IS IMPORTANT](https://www.youtube.com/watch?v=FDCfw-YqWTE&list=PLkDaE6sCZn6Hn0vK8co82zjQtt3T2Nkqc&index=10&t=0s)  

    <br>

4. **Undesirable Properties:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    * __Saturation__:  
    An activation functions output, with finite range, may saturate near its tail or head (e.g. $$\{0, 1\}$$ for sigmoid). This leads to a problem called __vanishing gradient__.  
    * __Vanishing Gradients__:  
    Happens when the gradient of an activation function is very small/zero. This usually happens when the activation function __saturates__ at either of its tails.  
    The chain-rule will *__multiply__* the local gradient (of activation function) with the whole objective. Thus, when gradient is small/zero, it will "kill" the gradient $$\rightarrow$$ no signal will flow through the neuron to its weights or to its data.  
    __Slows/Stops learning completely__.  
    * __Range Not Zero-Centered__:  
    This is undesirable since neurons in later layers of processing in a Neural Network would be receiving data that is not zero-centered. This has implications on the dynamics during gradient descent, because if the data coming into a neuron is always positive (e.g. $$x>0$$ elementwise in $$f=w^Tx+b$$), then the gradient on the weights $$w$$ will during backpropagation become either all be positive, or all negative (depending on the gradient of the whole expression $$f$$). This could introduce undesirable zig-zagging dynamics in the gradient updates for the weights. However, notice that once these gradients are added up across a batch of data the final update for the weights can have variable signs, somewhat mitigating this issue. Therefore, this is an inconvenience but it has less severe consequences compared to the saturated activation problem above.  
    __Makes optimization harder.__   
    <br>

<!-- 5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}  
 -->

***

## Activation Functions
{: #content2}

![img](/main_files/concepts/16.png){: max-width="180%" width="180%"}  

1. **Sigmoid:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    <p>$$S(z)=\frac{1}{1+e^{-z}} \\ S^{\prime}(z)=S(z) \cdot(1-S(z))$$</p>  
    ![img](/main_files/concepts/3.png){: width="68%" .center-image}  
    __Properties:__{: style="color: red"}  
    Never use as activation, use as an output unit for binary classification.  
    * __Pros__:  
        * Has a nice interpretation as the firing rate of a neuron  
    * __Cons__:  
        * They Saturate and kill gradients $$\rightarrow$$ Gives rise to __vanishing gradients__[^1] $$\rightarrow$$ Stop Learning  
        * Happens when initialization weights are too large  
        * or sloppy with data preprocessing  
        * Neurons Activation saturates at either tail of $$0$$ or $$1$$  
        * Output NOT __Zero-Centered__ $$\rightarrow$$ Gradient updates go too far in different directions $$\rightarrow$$ makes optimization harder   
        * The local gradient $$(z * (1-z))$$ achieves maximum at $$0.25$$, when $$z = 0.5$$. $$\rightarrow$$ very time the gradient signal flows through a sigmoid gate, its magnitude always diminishes by one quarter (or more) $$\rightarrow$$ with basic SGD, the lower layers of a network train much slower than the higher one  

2. **Tanh:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}  
    <p>$$\tanh (z)=\frac{e^{z}-e^{-z}}{e^{z}+e^{-z}} \\ \tanh ^{\prime}(z)=1-\tanh (z)^{2}$$</p>  
    ![img](/main_files/concepts/4.png){: width="68%" .center-image}  

    __Properties:__{: style="color: red"}  
    Strictly superior to Sigmoid (scaled version of sigmoid \| stronger gradient). Good for activation.  
    * __Pros__:  
        * Zero Mean/Centered  
    * __Cons__:  
        * They Saturate and kill gradients $$\rightarrow$$ Gives rise to __vanishing gradients__[^1] $$\rightarrow$$ Stop Learning  
    <br>

3. **ReLU:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}  
    <p>$$R(z)=\left\{\begin{array}{cc}{z} & {z>0} \\ {0} & {z<=0}\end{array}\right\} \\  R^{\prime}(z)=\left\{\begin{array}{ll}{1} & {z>0} \\ {0} & {z<0}\end{array}\right\}$$</p>  
    ![img](/main_files/concepts/5.png){: width="68%" .center-image}  

    __Properties:__{: style="color: red"}  
    The best for activation (Better gradients).  
    * __Pros__:  
        * Non-saturation of gradients which _accelerates convergence_ of SGD  
        * Sparsity effects and induced regularization. [discussion](https://stats.stackexchange.com/questions/176794/how-does-rectilinear-activation-function-solve-the-vanishing-gradient-problem-in/176905#176905)  
            ReLU (as usually used in neural networks) introduces sparsity in <span>__activations__</span>{: style="color: purple"} not in _weights_ or _biases_.  
        * Not computationally expensive  
    * __Cons__:  
        * __ReLU not zero-centered problem__:  
        The problem that ReLU is not zero-centered can be solved/mitigated by using __batch normalization__, which normalizes the signal before activation:  
        > From paper: We add the BN transform immediately before the nonlinearity, by normalizing $$x =  Wu + b$$; normalizing it is likely to produce activations with a stable distribution.  
        > * [WHY NORMALIZING THE SIGNAL IS IMPORTANT](https://www.youtube.com/watch?v=FDCfw-YqWTE&list=PLkDaE6sCZn6Hn0vK8co82zjQtt3T2Nkqc&index=10&t=0s)
        * __Dying ReLUs (Dead Neurons):__  
        If a neuron gets clamped to zero in the forward pass (it doesn’t "fire" / $$x<0$$), then its weights will get zero gradient. Thus, if a ReLU neuron is unfortunately initialized such that it never fires, or if a neuron’s weights ever get knocked off with a large update during training into this regime (usually as a symptom of aggressive learning rates), then this neuron will remain permanently dead.  
        * [**cs231n Explanation**](https://www.youtube.com/embed/gYpoJMlgyXA?start=1249){: value="show" onclick="iframePopA(event)"}
        <a href="https://www.youtube.com/embed/gYpoJMlgyXA?start=1249"></a>
            <div markdown="1"> </div>    
        * __Infinite Range__:  
        Can blow up the activation.  
    <br>

4. **Leaky-ReLU:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}  
    <p>$$R(z)=\left\{\begin{array}{cc}{z} & {z>0} \\ {\alpha z} & {z<=0}\end{array}\right\} \\ 
        R^{\prime}(z)=\left\{\begin{array}{ll}{1} & {z>0} \\ {\alpha} & {z<0}\end{array}\right\}$$</p>  
    ![img](/main_files/concepts/6.png){: width="68%" .center-image}  

    __Properties:__{: style="color: red"}  
    Sometimes useful. Worth trying.  
    * __Pros__:  
        * Leaky ReLUs are one attempt to fix the “dying ReLU” problem by having a small negative slope (of 0.01, or so).  
    * __Cons__:  
        The consistency of the benefit across tasks is presently unclear.  
    <br>

5. **ELU:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}  

    <!-- 
    6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents26}  

    7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents27}  
     -->
 
8. **Notes:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents28}  
    * It is very rare to mix and match different types of neurons in the same network, even though there is no fundamental problem with doing so.  
    * __Identity Mappings__:  
    When an activation function cannot achieve an identity mapping (e.g. ReLU map all negative inputs to zero); then adding extra depth actually decreases the best performance, in the case a shallower one would suffice (Deep Residual Net paper).  
    <br>

1. **Softmax:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    
    __Motivation:__{: style="color: red"}  
    {: #lst-p}
    * __Information Theory__ - from the perspective of information theory the softmax function can be seen as trying to minimize the cross-entropy between the predictions and the truth.  
    * __Probability Theory__ - from this perspective since $$\hat{y}_ i$$ represent log-probabilities we are in fact looking at the log-probabilities, thus when we perform exponentiation we end up with the raw probabilities. In this case the softmax equation find the MLE (Maximum Likelihood Estimate).  
        If a neuron's output is a log probability, then the summation of many neurons' outputs is a multiplication of their probabilities. That's more commonly useful than a sum of probabilities.  
    * It is a softened version of the __argmax__ function (limit as $$T \rightarrow 0$$)  

    __Properties__{: style="color: red"}  
    {: #lst-p}
    * There is one nice attribute of Softmax as compared with standard normalisation:  
        It react to low stimulation (think blurry image) of your neural net with rather uniform distribution and to high stimulation (ie. large numbers, think crisp image) with probabilities close to 0 and 1.   
        While standard normalisation does not care as long as the proportion are the same.  
        Have a look what happens when soft max has 10 times larger input, ie your neural net got a crisp image and a lot of neurones got activated.  
        <button>Example SM</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        > >>> softmax([1,2])              # blurry image of a ferret  
            [0.26894142,      0.73105858])  #     it is a cat perhaps !?  
            >>> softmax([10,20])            # crisp image of a cat  
            [0.0000453978687, 0.999954602]) #     it is definitely a CAT !   
        {: hidden=""}  
        And then compare it with standard normalisation:  
        <button>Example Normalization</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
        > >>> std_norm([1,2])                      # blurry image of a ferret  
            [0.3333333333333333, 0.6666666666666666] #     it is a cat perhaps !?  
            >>> std_norm([10,20])                    # crisp image of a cat  
            [0.3333333333333333, 0.6666666666666666] #     it is a cat perhaps !?  
        {: hidden=""}

    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * Alternatives to Softmax:  
        * [AN EXPLORATION OF SOFTMAX ALTERNATIVES BELONGING TO THE SPHERICAL LOSS FAMILY (paper)](https://arxiv.org/pdf/1511.05042.pdf)  
        * [From Softmax to Sparsemax: A Sparse Model of Attention and Multi-Label Classification (paper)](http://proceedings.mlr.press/v48/martins16.pdf)  
    <br>
    



<!-- 
    __Desirable Properties:__{: style="color: red"}  
    {: #lst-p}
    * __Non-Linearity__:  
    When the activation function is non-linear, then a two-layer neural network can be proven to be a universal function approximator. The identity activation function does not satisfy this property. When multiple layers use the identity activation function, the entire network is equivalent to a single-layer model. 
    * __Range__:  
    When the range of the activation function is finite, gradient-based training methods tend to be more stable, because pattern presentations significantly affect only limited weights. When the range is infinite, training is generally more efficient because pattern presentations significantly affect most of the weights. In the latter case, smaller learning rates are typically necessary.  
    * __Continuously Differentiable__:  
    This property is desirable for enabling gradient-based optimization methods. The binary step activation function is not differentiable at 0, and it differentiates to 0 for all other values, so gradient-based methods can make no progress with it.
    * __Monotonicity__:  
    When the activation function is monotonic, the error surface associated with a single-layer model is guaranteed to be convex.  
    * __Smoothness with Monotonic Derivatives__:  
    These have been shown to generalize better in some cases.  
    * __Approximating Identity near Origin__:  
    Equivalent to $${\displaystyle f(0)=0}$$ and $${\displaystyle f'(0)=1}$$, and $${\displaystyle f'}$$ is continuous at $$0$$.  
    When activation functions have this property, the neural network will learn efficiently when its weights are initialized with small random values. When the activation function does not approximate identity near the origin, special care must be used when initializing the weights.  
    * __Zero-Centered Range__:  
    Has effects of centering the data (zero mean) by centering the activations. Makes learning easier.   
    > [WHY NORMALIZING THE DATA/SIGNAL IS IMPORTANT](https://www.youtube.com/watch?v=FDCfw-YqWTE&list=PLkDaE6sCZn6Hn0vK8co82zjQtt3T2Nkqc&index=10&t=0s)
            
    __Undesirable Properties:__{: style="color: red"}  
    {: #lst-p}
    {: #lst-p}
    * __Saturation__:  
        An activation functions output, with finite range, may saturate near its tail or head (e.g. $$\{0, 1\}$$ for sigmoid). This leads to a problem called __vanishing gradient__.  
    * __Vanishing Gradients__:  
        Happens when the gradient of an activation function is very small/zero. This usually happens when the activation function __saturates__ at either of its tails.  
        The chain-rule will *__multiply__* the local gradient (of activation function) with the whole objective. Thus, when gradient is small/zero, it will "kill" the gradient $$\rightarrow$$ no signal will flow through the neuron to its weights or to its data.  
        __Slows/Stops learning completely__.  
    * __Range Not Zero-Centered__:  
        This is undesirable since neurons in later layers of processing in a Neural Network would be receiving data that is not zero-centered. This has implications on the dynamics during gradient descent, because if the data coming into a neuron is always positive (e.g. $$x>0$$ elementwise in $$f=w^Tx+b$$), then the gradient on the weights $$w$$ will during backpropagation become either all be positive, or all negative (depending on the gradient of the whole expression $$f$$). This could introduce undesirable zig-zagging dynamics in the gradient updates for the weights. However, notice that once these gradients are added up across a batch of data the final update for the weights can have variable signs, somewhat mitigating this issue. Therefore, this is an inconvenience but it has less severe consequences compared to the saturated activation problem above.  
        __Makes optimization harder.__   

    __Activation Functions:__{: style="color: red"}  
    {: #lst-p}
    ![img](/main_files/concepts/16.png){: max-width="180%" width="180%"}  
    * __Properties__:                  
        * __Sigmoid__:  
            Never use as activation, use as an output unit for binary classification.  
            * __Pros__:  
                * Has a nice interpretation as the firing rate of a neuron  
            * __Cons__:  
                * They Saturate and kill gradients $$\rightarrow$$ Gives rise to __vanishing gradients__[^1] $$\rightarrow$$ Stop Learning  
                    * Happens when initialization weights are too large  
                    * or sloppy with data preprocessing  
                    * Neurons Activation saturates at either tail of $$0$$ or $$1$$  
                * Output NOT __Zero-Centered__ $$\rightarrow$$ Gradient updates go too far in different directions $$\rightarrow$$ makes optimization harder   
                * The local gradient $$(z * (1-z))$$ achieves maximum at $$0.25$$, when $$z = 0.5$$. $$\rightarrow$$ very time the gradient signal flows through a sigmoid gate, its magnitude always diminishes by one quarter (or more) $$\rightarrow$$ with basic SGD, the lower layers of a network train much slower than the higher one  
        * __Tanh__:  
            Strictly superior to Sigmoid (scaled version of sigmoid \| stronger gradient). Good for activation.  
            * __Pros__:  
                * Zero Mean/Centered  
            * __Cons__:  
                * They Saturate and kill gradients $$\rightarrow$$ Gives rise to __vanishing gradients__[^1] $$\rightarrow$$ Stop Learning  
        * __ReLU__:  
            The best for activation (Better gradients).  
            * __Pros__:  
                * Non-saturation of gradients which _accelerates convergence_ of SGD  
                * Sparsity effects and induced regularization. [discussion](https://stats.stackexchange.com/questions/176794/how-does-rectilinear-activation-function-solve-the-vanishing-gradient-problem-in/176905#176905)  
                * Not computationally expensive  
            * __Cons__:  
                * __ReLU not zero-centered problem__:  
                    The problem that ReLU is not zero-centered can be solved/mitigated by using __batch normalization__, which normalizes the signal before activation:  
                    > From paper: We add the BN transform immediately before the nonlinearity, by normalizing $$x =  Wu + b$$; normalizing it is likely to produce activations with a stable distribution.  
                    > * [WHY NORMALIZING THE SIGNAL IS IMPORTANT](https://www.youtube.com/watch?v=FDCfw-YqWTE&list=PLkDaE6sCZn6Hn0vK8co82zjQtt3T2Nkqc&index=10&t=0s)
                * __Dying ReLUs (Dead Neurons):__  
                    If a neuron gets clamped to zero in the forward pass (it doesn’t "fire" / $$x<0$$), then its weights will get zero gradient. Thus, if a ReLU neuron is unfortunately initialized such that it never fires, or if a neuron’s weights ever get knocked off with a large update during training into this regime (usually as a symptom of aggressive learning rates), then this neuron will remain permanently dead.  
                    * [**cs231n Explanation**](https://www.youtube.com/embed/gYpoJMlgyXA?start=1249){: value="show" onclick="iframePopA(event)"}
                    <a href="https://www.youtube.com/embed/gYpoJMlgyXA?start=1249"></a>
                        <div markdown="1"> </div>    
                * __Infinite Range__:  
                    Can blow up the activation.  
        * __Leaky Relu__:  
            Sometimes useful. Worth trying.  
            * __Pros__:  
                * Leaky ReLUs are one attempt to fix the “dying ReLU” problem by having a small negative slope (of 0.01, or so).  
            * __Cons__:  
                The consistency of the benefit across tasks is presently unclear.  
        * __ELU__:  
            
    * __Derivatives of Activation Functions__:  
        * __Sigmoid__:  
            <p>$$S(z)=\frac{1}{1+e^{-z}} \\ S^{\prime}(z)=S(z) \cdot(1-S(z))$$</p>  
            ![img](/main_files/concepts/3.png){: width="68%" .center-image}  
        * __Tanh__:  
            <p>$$\tanh (z)=\frac{e^{z}-e^{-z}}{e^{z}+e^{-z}} \\ \tanh ^{\prime}(z)=1-\tanh (z)^{2}$$</p>  
            ![img](/main_files/concepts/4.png){: width="68%" .center-image}  
        * __Relu__:  
            <p>$$R(z)=\left\{\begin{array}{cc}{z} & {z>0} \\ {0} & {z<=0}\end{array}\right\} \\  R^{\prime}(z)=\left\{\begin{array}{ll}{1} & {z>0} \\ {0} & {z<0}\end{array}\right\}$$</p>  
            ![img](/main_files/concepts/5.png){: width="68%" .center-image}  
        * __Leaky Relu__:  
            <p>$$R(z)=\left\{\begin{array}{cc}{z} & {z>0} \\ {\alpha z} & {z<=0}\end{array}\right\} \\ 
            R^{\prime}(z)=\left\{\begin{array}{ll}{1} & {z>0} \\ {\alpha} & {z<0}\end{array}\right\}$$</p>  
            ![img](/main_files/concepts/6.png){: width="68%" .center-image}  
        * [Further Reading](https://ml-cheatsheet.readthedocs.io/en/latest/activation_functions.html)  

    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * It is very rare to mix and match different types of neurons in the same network, even though there is no fundamental problem with doing so.  
    * __Identity Mappings__:  
        When an activation function cannot achieve an identity mapping (e.g. ReLU map all negative inputs to zero); then adding extra depth actually decreases the best performance, in the case a shallower one would suffice (Deep Residual Net paper).   -->