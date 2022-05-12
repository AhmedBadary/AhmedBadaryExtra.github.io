---
layout: NotesPage
title: Normalization Methods in Deep Learning
permalink: /work_files/research/dl/concepts/norm_methods
prevLink: /work_files/research/dl/concepts.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Normalization](#content1)
  {: .TOC1}
  * [Batch Normalization](#content2)
  {: .TOC2}
  * [Weight Normalization](#content3)
  {: .TOC3}
  * [Layer Normalization](#content4)
  {: .TOC4}
  * [Instance Normalization](#content5)
  {: .TOC5}
  * [Group Normalization](#content6)
  {: .TOC6}
  * [Batch ReNormalization](#content7)
  {: .TOC7}
  * [Batch-Instance Normalization](#content8)
  {: .TOC8}
  * [Switchable Normalization](#content9)
  {: .TOC9}
  * [Spectral Normalization](#content10)
  {: .TOC10}
  * [Further Exploration/Discussions](#content11)
  {: .TOC11}
</div>

***
***

[Deeper Understanding of Batch Normalization](https://medium.com/@SeoJaeDuk/deeper-understanding-of-batch-normalization-with-interactive-code-in-tensorflow-manual-back-1d50d6903d35)  
[Preprocessing for Deep Learning](https://hadrienj.github.io/posts/Preprocessing-for-deep-learning/)  
[Self Normalizing Neural Networks](https://arxiv.org/pdf/1706.02515.pdf)  
[An Overview of Normalization Methods in Deep Learning](http://mlexplained.com/2018/11/30/an-overview-of-normalization-methods-in-deep-learning/)    

![img](/main_files/dl/concepts/normalization/1.png){: width="100%"}  

## Normalization
{: #content1}

1. **Normalization:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    __Normalization__, aka __Feature Scaling__, is a method used to normalize the range of independent variables or features of data. It is generally performed during the data preprocessing step.  

    __Motivation:__{: style="color: red"}  
    Since the range of values of raw data varies widely, in some machine learning algorithms, objective functions will not work properly without normalization (e.g. dot-product-based functions are scale sensitive).  
    Moreover, normalizing the inputs leads to __spherical contours__ of the objective which makes the optimization easier (for vanilla sgd) and speeds up the convergence.  

    * [**Why&How to Normalize Inputs (Ng)**](https://www.youtube.com/embed/FDCfw-YqWTE){: value="show" onclick="iframePopA(event)"}
    <a href="https://www.youtube.com/embed/FDCfw-YqWTE"></a>
        <div markdown="1"> </div>    

    <br>

2. **Input Normalization:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    

    __Rescaling (min-max normalization):__{: style="color: red"}  
    is the simplest method and consists in rescaling the range of features to scale the range in $$[0, 1]$$ or $$[−1, 1]$$. Selecting the target range depends on the nature of the data. To rescale to $$[0, 1]$$ range:  
    <p>$$x'=\dfrac{x-{\text{min}}(x)}{ {\text{max}}(x)-{\text{min}}(x)}$$</p>  

    To rescale a range between an arbitrary set of values $$[a, b]$$, the formula becomes:  
    <p>$${\displaystyle x'=a+{\frac {(x-{\text{min}}(x))(b-a)}{ {\text{max}}(x)-{\text{min}}(x)}}}$$</p>  
    where $$a,\: b$$ are the min-max values.  


    __(Zero-) Centering - Mean Normalization:__{: style="color: red"}  
    * Define the mean $$\mu_j$$ of each feature of the datapoints $$x^{(i)}$$:  
        <p>$$\mu_{j}=\frac{1}{m} \sum_{i=1}^{m} x_{j}^{(i)}$$</p>  
    * Replace each $$x_j^{(i)}$$ with $$x_j - \mu_j$$  


    __Standardization (Z-score Normalization):__{: style="color: red"}  
    Feature standardization makes the values of each feature in the data have zero-mean (when subtracting the mean in the numerator) and unit-variance. Subtract the mean from each feature, then, divide the values of each feature by its standard deviation.  
    <p>$$x' = \frac{x - \bar{x}}{\sigma}$$</p>  


    __(Scaling to) Unit Length Normalization:__{: style="color: red"}  
    Another option that is widely used in machine-learning is to scale the components of a feature vector such that the complete vector has length one. This usually means dividing each component by the Euclidean length of the vector:  
    <p>$${\displaystyle x'={\frac {x}{\left\|{x}\right\|}}}$$</p>  
    We can use $$L_1$$ norm or other metrics based on problem.  

    <br>

3. **Activation Normalization:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    Extends the idea of __input normalization__ to deeper networks. Interprets activations in a layer as a featurized input (abstract representation of the input) and aims to normalize those layer outputs/activations.  

    <span id="affine_transform">The difference however, is in the target mean and variance we want to achieve. Unlike _inputs_, we might not want to force the activations to have mean$$=0$$ and variance$$=1$$. E.g. if we are using the sigmoid activation; mean$$=0$$ and variance$$=1$$ will utilize the *__linear__* part of sigmoid. So, changing the mean and variance will allow the network to take advantage of the non-linearity.</span>   
    ![img](/main_files/concepts/3.png){: width="40%" .center-image}  

    > In practice, it's much more common to normalize the outputs before applying the activation (e.g. in Batch-Norm)  

    <br>

4. **[Statistical Normalization](https://en.wikipedia.org/wiki/Normalization_(statistics)) - Transformations:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    Let $$X$$ be $$n \times d$$ design matrix of sample pts.  
    Each row $$i$$ of $$X$$ is a sample pt $$X_i^T$$.  

    __Centering Transform:__{: style="color: red"}  
    AKA __Mean Normalization__ is just removing the mean from each observation. It centers the data around $$0$$.  
    <p>$$X' = X - \mathbf{\mu}$$</p>   
    where $$\mathbf{\mu}$$ is the mean of all the rows of $$X$$.  

    __Decorrelation Transform:__{: style="color: red"}  
    removes only the correlations but leaves variances intact,  
    <p>$$Z = X'V$$</p>  
    where $$\text{Var}(X') = \Sigma = \dfrac{1}{n}X'^TX' = V\Lambda V^T$$, and $$\text{Var}(Z) = \Lambda$$ is the sample covariance matrix.  

    It transforms the sample points to the eigenvector coordinate system.  

    __Standardization Transform:__{: style="color: red"}  
    sets variances to $$1$$ but leaves correlations intact,  
    <p>$$X'_s = \dfrac{X - \mathbf{\mu}}{\mathbf{\sigma}_ X}$$</p>  
    where $$\mathbf{\sigma}_ X$$ is the standard deviation of all the rows of $$X$$.  

    __Sphering Transform:__{: style="color: red"}  
    Rescales the uncorrelated matrix $$Z$$ in order to obtain a covariance matrix corresponding to the identity matrix. To do that we scale our decorrelated data by dividing each dimension by the square-root of its corresponding eigenvalue.  
    <p>$$W = X'\Sigma^{-1/2} = X'(V \Lambda^{-1/2} V^T)$$</p>  
    this is __ZCA whitening__.  

    __Whitening Transform:__{: style="color: red"}  
    The [Whitening Transformation](https://en.wikipedia.org/wiki/Whitening_transformation) is a linear transformation that transforms a vector of random variables with a known covariance matrix into a set of new variables whose covariance is the identity matrix, meaning that they are uncorrelated and each have variance 1. The transformation is called "whitening" because it changes the input vector into a white noise vector.  
    = __Centering__ + __Sphering__  

    Then $$W$$ has covariance matrix $$I . \left[\text { If } X_{i} \sim \mathcal{N}(\mu, \Sigma), \text { then approximately, } W_{i} \sim \mathcal{N}(0, I)\right]$$.  



    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * __Decorrelation:__ intuitively, it means that we want to rotate the data until there is no correlation anymore.  
    * __Centering__ seems to make it easier for hidden units to get into a good operating region of the sigmoid or ReLU  
    * __Standardization (normalizing variance)__ makes the objective function better conditioned, so gradient descent converges faster  

    <br>

<!-- 5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  
6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}  -->  

***

## Batch Normalization
{: #content2}

1. **Batch Normalization:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    __Batch Normalization__ is a normalization method that normalizes activations in a network across the mini-batch. For each feature, batch normalization computes the mean and variance of that feature in the mini-batch. It then subtracts the mean and divides the feature by its mini-batch standard deviation.  
    <span>This restricts the activations to have __$$0$$__ mean and __unit__ variance.</span>{: style="color: goldenrod"}  
    This is followed by an __affine transformation__ of the normalized activations to __rescale the mean and variance__, in a learnable way, to whatever the network sees fit. [This is done because restricting the mean and variance of the activations might hinder the network from taking advantage of the freedom of setting the distribution of the activations to something that might help the later layers learn faster](#affine_transform). _This means that the expressiveness of the network does not change._  

    <button>Show Paper</button>{: .showText value="show"
     onclick="showText_withParent_PopHide(event);"}
    <p hidden=""><img style="float: left" width="45%" src="https://cdn.mathpix.com/snip/images/iQfN-SDV0z9nzlyRhX8oUuX8ZUgxd9kuAjmpKhROwBk.original.fullsize.png" />
    <iframe src="https://docs.google.com/viewerng/viewer?url=https://arxiv.org/pdf/1502.03167.pdf&amp;embedded=true" frameborder="0" height="535" width="415" title="Batch Normalization" scrolling="auto"></iframe></p>  

    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * __Scale Invariance:__ Batch Norm renders the loss function of neural networks scale invariant.  
        I.E. scaling the weights by a constant does not change the output, or the loss, of the batch normalized network.  
        * __Implications of Scale Invariance -__ [__Exponentially Growing Learning Rate__](https://www.inference.vc/exponentially-growing-learning-rate-implications-of-scale-invariance-induced-by-batchnorm/):  
            * It is possible to use <span>__exponentially growing__ learning rate schedule</span>{: style="color: purple"} when training neural networks with batch normalization.  
            * The paper establishes the following __Equivalence__:  
                * __Weight decay__ with __constant__ learning rate  
                * __No__ weight decay and an __exponentially growing__ learning rate  

                This equivalence holds for other normalization layers as well, __Group Normalization__, __Layer Normalization__, __Instance Norm__, etc.  
    * __Weight Decay and BN:__  
        * [This Paper](https://arxiv.org/pdf/1810.12281.pdf) shows that __weight decay__ on a BN-network is just <span>tweaking the __*effective* learning rate__</span>{: style="color: purple"}.  
        * Without weight decay, the gradient of a BN-network is always __orthogonal to the current value of the parameter vector__ and therefore __increases the scale of weights__ (__reduces effective learning rate__).  
            Intuitively, you can compensate the decrease of effective learning rate by using an exponential learning rate scheme or just simply weight decay.  
    <br>

2. **Effectiveness of Batch Normalization:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}  
    There are many different proposed reasons that try to explain the wide success and effectiveness of the method. We summarize here some of those reasons and give an intuition to why those reasons apply.  

    __Summarizing the intuition of why BN works:__  
    The overall intuition is that batch normalization makes the loss surface “easier to navigate”, making optimization easier, enabling the use of higher learning rates, and improving model performance across multiple tasks.  
    Further, there is a _regularization_ effect when using BN induced by added noise to the estimate of the mean and variance of the data due to using mini-batches instead.  

    * [Busting the myth about batch normalization](https://blog.paperspace.com/busting-the-myths-about-batch-normalization/)  

    <br>

22. **Internal Covariate Shift as an Intuitive but Wrong Motivation for the Success of BN:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents222}  
    The correlation between batch normalization and internal covariate shift is widely accepted but was not supported by experimental results. Scholars recently show with experiments that the hypothesized relationship is not an accurate one. Rather, the enhanced accuracy with the batch normalization layer seems to be independent of internal covariate shift.  

    __Two Problems with the ICS Explanation:__  
    1. Even if the mean and variance are constant, the distribution of activations can still change. Why are the mean and variance so important?  
    2. If we introduce $$\gamma$$  and $$\beta$$, the mean and variance will deviate from $$0$$ and $$1$$ anyway. What then, is the point of batch normalization?  
    <br>


3. **Suppressing Higher-Order Effects (Goodfellow):**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}  

    __Quick Intuition:__  
    {: #lst-p}
    * In a neural network, changing one weight affects subsequent layers, which then affect subsequent layers, and so on.
    * This means changing one weight can make the activations fly all over the place in complex ways.
    * This forces us to use lower learning rates to prevent the gradients from exploding, or – if we use sigmoid activations – to prevent the gradients from disappearing.
    * Batch normalization to the rescue! Batch normalization reparameterizes the network to make optimization easier.
    * With batch normalization, we can control the magnitude and mean of the activations __independent__ of all other layers.
    * This means weights don’t fly all over the place (as long as we have sensible initial means and magnitudes), and we can optimize much easier.  

    __Further Intuition:__  
    Deep Neural networks have higher-order interactions, which means changing weights of one layer might also effect the statistics of other layers in addition to the loss function. These cross layer interactions, when unaccounted lead to internal covariate shift. Every time we update the weights of a layer, there is a chance that it effects the statistics of a layer further in the neural network in an unfavorable way.  
    Convergence may require careful initializing, hyperparameter tuning and longer training durations in such cases. However, when we add the batch normalized layer between the layers, the statistics of a layer are only effected by the two hyperparameters  $$\gamma$$  and $$\beta$$. Now our optimization algorithm has to adjust only two hyperparameters to control the statistics of any layer, rather than the entire weights in the previous layer. This greatly speeds up convergence, and avoids the need for careful initialization and hyperparameter tuning. Therefore, Batch Norm acts more like a check pointing mechanism.  
    > Notice that the ability to arbitrarily set the mean and the standard deviation of a layer also means that we can recover the original distribution if that was sufficient for proper training.  


    * [**GoodFellow Lecture**](https://www.youtube.com/embed/Xogn6veSyxA?start=225){: value="show" onclick="iframePopA(event)"}
    <a href="https://www.youtube.com/embed/Xogn6veSyxA?start=225"></a>
        <div markdown="1"> </div>    
    * [Further Discussion of Higher-Order Effects](http://mlexplained.com/2018/01/10/an-intuitive-explanation-of-why-batch-normalization-really-works-normalization-in-deep-learning-part-1/)   

    <br>


4. **Induced Smoothness of the Optimization Landscape ([Santurkar et al.](https://arxiv.org/pdf/1805.11604.pdf)):**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}  
    In a new paper, the authors claim that BN works because it makes the loss surface __smoother__. Concretely, it improves the $$\beta$$-smoothness or the Lipschitzness of the function. This smoothness induces a more predictive and stable behavior of the gradients, allowing for faster training.  


    * [**How Does Batch Normalization Help Optimization? (Santurkar et al.)**](https://arxiv.org/pdf/1805.11604.pdf){: value="show" onclick="iframePopA(event)"}
    <a href="https://arxiv.org/pdf/1805.11604.pdf"></a>
        <div markdown="1"> </div>    

    <br>

5. **Batch Norm as a Regularizer:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}  
    BN also acts a regularizer. The mean and the variance estimated for each batch is a noisier version of the true mean, and this injects randomness in our optima search. This helps in regularization.  
    <br>

6. **Length-Direction Decoupling:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents26}  
    It is argued that the success of batch normalization could be at least partially credited to the __length-direction decoupling effect__ that the method provides.  

    By interpreting the batch normalization procedure as the reparametrization of weight space, it could be shown that the length and the direction of the weights are separated after the procedure, and they could thus be trained separately.  

    This property could then be used to __prove the faster convergence of problems with batch normalization__:  
    {: #lst-p}
    * [Linear Convergence of the __Least-Squares__ Problem with Batch Normalization](https://en.wikipedia.org/wiki/Batch_normalization#Linear_Convergence_of_the_Least-Square_Problem_with_Batch_Normalization)  
    * [Linear Convergence of the __Learning Halfspace__ Problem with Batch Normalization](https://en.wikipedia.org/wiki/Batch_normalization#Linear_Convergence_of_the_Learning_Halfspace_Problem_with_Batch_Normalization)  
    * [Linear Convergence of __Neural Networks__ with Batch Normalization](https://en.wikipedia.org/wiki/Batch_normalization#Linear_Convergence_of_Neural_Networks_with_Batch_Normalization)  
    <br>

7. **Limitations/Problems of BN:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents27}  
    
    When doing normalization, we ideally want to the use the __global__ mean and variance to standardize our data. Computing this for each layer is far too expensive though, so we need to approximate using some other measures. BN approximates the mean and variance with those of the __mini batch__, which is a noisy estimate. Although, we motivated some of the effectiveness of BN to its regularizing effects due to this, same, noisy estimate, this estimate can be problematic in the following scenarios:  
    1. __Small Batch Sizes:__  
        If the batch size is $$1$$, the variance is $$0$$ so batch normalization cannot be applied. Slightly larger mini-batch sizes won’t have this problem, but small mini-batches make our estimates very noisy and can negatively impact training, meaning batch normalization imposes a certain lower bound on our batch size.  
    2. __Recurrent Connections in an RNN:__  
        In an RNN, _the recurrent activations of each time-step will have different statistics_. This means that we have to _fit a separate batch normalization layer for each time-step_. This makes the model _more complicated_ and – more importantly – it _forces us to store the statistics for each time-step during training_.  
    3. __Dependence of the loss between samples in a mini-batch:__  
        BN makes the loss value for each sample in a mini-batch dependent on other samples in the mini-batch. For instance, if a sample causes a certain layer’s activations to become much larger, this will make the mean and variance larger as well. This will change the activation for all other samples in the mini-batch as well. Furthermore, the mini-batch statistics will depend on the mini-batch size as well (a smaller mini-batch size will increase the random variation in the mean and variance statistics).
        The problem arises not when training a model on a single machine, but when we start to conduct distributed training, things can get ugly. As mentioned in [this paper](https://arxiv.org/pdf/1706.02677.pdf), we need to take extra care in choosing the batch size and learning rate in the presence of batch normalization when doing distributed training. If two different machines use different batch sizes, they will indirectly be optimizing different loss functions: this means that the value of $$\gamma$$ that worked for one machine is unlikely to work for another machine. This is why the authors stressed that the batch size for each worker must be kept constant across all machines.  
    4. __BN parameters in Fine-Tuning Applications:__  
        When Fine-Tuning a larger network by freezing all the layers except the last layer; it is unclear if one should use the mean and variance computed on the *__original dataset__* or use the mean and variance of the mini-batches. Though most frameworks use the mini-batch statistics, if we are using a different mini-batch size there will be a mismatch between the optimal batch normalization parameters and the parameters in the network.  
        If there is a mis-match in the mini-batch sizes it seems to be better to use the statistics of the _original dataset_ instead.  
        [Further Discussion](https://forums.fast.ai/t/freezing-batch-norm/8377/5)  


    <br>


<!-- 7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents27}  
8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents28}   -->

***

## Weight Normalization
{: #content3}


<button>Paper</button>{: .showText value="show"
     onclick="showText_withParent_PopHide(event);"}
<iframe hidden="" src="https://arxiv.org/pdf/1602.07868.pdf" frameborder="0" height="780" width="600" title="Weight Normalization" scrolling="auto"></iframe>


1. **Weight Normalization:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}  
    __Weight Normalization__ is a normalization method that, instead of normalizing the _mini-batch_, <span>normalizes the weights of the layer</span>{: style="color: goldenrod"}.  

    WN reparameterizes the weights $$\boldsymbol{w}$$ of any layer in the network in the following way:  
    <p>$$\boldsymbol{w}=\frac{g}{\|\boldsymbol{v}\|} \boldsymbol{v} \:\:\:\:\:\:\: $$</p>  
    where $$\boldsymbol{v}$$ is a $$k$$-dimensional vector, $$g$$ is a scalar, and $$\|\boldsymbol{v}\|$$ denotes the Euclidean norm of $$\boldsymbol{v}$$.  
    This reparameterization has the effect of fixing the Euclidean norm of the weight vector $$\boldsymbol{w}$$: we now have $$\|\boldsymbol{w}\| = g$$, independent of the parameters $$\boldsymbol{v}$$.  

    Weight Normalization <span>separates the norm of the weight vector from its direction without reducing expressiveness</span>{: style="color: goldenrod"}:  
    {: #lst-p}
    * For variance, this has a similar effect to _dividing the inputs by the standard deviation in batch normalization_.  
    * As for the mean, the authors of the paper proposed using a method called [__“mean-only batch normalization”__](#bodyContents33) together with weight normalization.  
    <br>

2. **Advantages:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}  
    * Since WN separates the norm of the weight vector from its direction, and then optimizes both $$g$$ and $$\boldsymbol{v}$$ using gradient descent. This change in learning dynamics makes optimization easier.  
    * It makes the mean and variance __independent of the batch__; since now they are connected to the weights of the network.  
    * It is often __much faster__ than BN. In CNNs, the number of weights tends to be far smaller than the number of inputs, meaning weight normalization is computationally cheaper compared to batch normalization (CNNs share weights).   
    <br>

3. **Mean-Only Batch Normalization:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}  
    Although weight normalization on its own can assist training, the authors of the paper proposed using a method called “mean-only batch normalization” in conjunction with weight normalization.  

    __Mean-Only Batch Normalization__ is a method that subtracts out the mean of the mini-batch but does not divide the inputs by the standard deviation or rescales them.  

    Though this method counteracts some of the computational speed-up of weight normalization, it is cheaper than batch-normalization since it does not need to compute the standard deviations. The authors claim that this method provides the following benefits:  
    {: #lst-p}
    1. It makes the mean of the activations independent from $$\boldsymbol{v}$$:  
        Weight normalization independently cannot isolate the mean of the activations from the weights of the layer, causing high-level dependencies between the means of each layer. Mean-only batch normalization can resolve this problem.  
    2. It adds “gentler noise” to the activations:  
        One of the side-effects of batch normalization is that it adds some stochastic noise to the activations as a result of using noisy estimates computed on the mini-batches. This has a regularization effect in some applications but can be potentially harmful in some noise-sensitive domains like reinforcement learning. The noise caused by the mean estimations, however, are “gentler” since the law of large numbers ensures the mean of the activations is approximately normally distributed.  
        Thus, weight normalization <span>can still work in settings with a smaller mini-batch size</span>{: style="color: goldenrod"}.  
    <br>
 

<!-- 4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents34}   -->

***

## Layer Normalization
{: #content4}

<button>Paper</button>{: .showText value="show"
     onclick="showText_withParent_PopHide(event);"}
<iframe hidden="" src="https://arxiv.org/pdf/1607.06450.pdf" frameborder="0" height="840" width="646" title="Layer Normalization" scrolling="auto"></iframe>


1. **Layer Normalization:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents41}  
    __Layer Normalization__ is a normalization method developed by Hinton that, instead of normalizing the inputs across batches like BN, <span>normalizes the inputs across the __features__</span>{: style="color: goldenrod"}:  
    <p>$$\begin{aligned} \mu_{i} &=\frac{1}{m} \sum_{j=1}^{m} x_{i j} \\ \sigma_{i}^{2} &=\frac{1}{m} \sum_{j=1}^{m}\left(x_{i j}-\mu_{i}\right)^{2} \\ \hat{x}_{i j} &=\frac{x_{i j}-\mu_{i}}{\sqrt{\sigma_{i}^{2}+\epsilon}} \end{aligned}$$</p>  

    This is deceptively similar to the batch norm equations:  
    <p>$$\begin{aligned} \mu_{j} &=\frac{1}{m} \sum_{i=1}^{m} x_{i j} \\ \sigma_{j}^{2} &=\frac{1}{m} \sum_{i=1}^{m}\left(x_{i j}-\mu_{j}\right)^{2} \\ \hat{x}_{i j} &=\frac{x_{i j}-\mu_{j}}{\sqrt{\sigma_{j}^{2}+\epsilon}} \end{aligned}$$</p>  
    where $$x_{i j}$$  is the $$i,j$$-th element of the input, the first dimension represents the batch and the second represents the feature (I have modified the notation from the original papers to make the contrast clearer).  

    <button>BN vs LN Illustration</button>{: .showText value="show"
     onclick="showTextPopHide(event);"}
    ![LN vs BN](https://cdn.mathpix.com/snip/images/oLjDSgRfXNgvvaobfQKjDuNfUhcjce-K7TKcX8-DjWM.original.fullsize.png){: width="70%" hidden=""}  
    In batch normalization, the statistics are computed across the batch and are the same for each example in the batch. In contrast, in layer normalization, the statistics are computed across each feature and are __independent of other examples__.  

    This means that layer normalization is __not a simple reparameterization of the network__, unlike the case of weight normalization and batch normalization, which both have the same expressive power as an unnormalized neural network. The layer normalized model, thus, has __different invariance properties than the other methods__.   
    <br>

2. **Advantages:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents42}  
    * The independence between inputs means that each input has a different normalization operation, allowing arbitrary mini-batch sizes to be used.
    * The experimental results show that layer normalization performs well for recurrent neural networks.  
    <br>

3. **Analysis of the Invariance Properties of LN:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents43}  
    <br>

***

## Instance Normalization
{: #content5}

<button>Paper</button>{: .showText value="show"
     onclick="showText_withParent_PopHide(event);"}
<iframe hidden="" src="https://docs.google.com/viewer?url=https://arxiv.org/pdf/1607.08022.pdf&amp;embedded=true" frameborder="0" height="840" width="646" title="Layer Normalization" scrolling="auto"></iframe>


<!-- <iframe hidden="" src="https://arxiv.org/pdf/1607.08022.pdf" frameborder="0" height="840" width="646" title="Layer Normalization" scrolling="auto"></iframe> -->


1. **Instance Normalization:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents51}  
    __Instance Normalization__ is similar to layer normalization but with an extra restriction: it computes the mean/standard deviation and normalize across __each channel in each training example__.  

    __Motivation:__{: style="color: red"}  
    In __Style Transfer__ problems, the network should be *agnostic to the __contrast__ of the original image*.   
    Therefore, it is specific to images and not trivially extendable to RNNs.  


    Experimental results show that instance normalization performs well on style transfer when replacing batch normalization. Recently, instance normalization has also been used as a replacement for batch normalization in __GANs__.   
    <br>

<!-- 2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents52}  
3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents53}   -->



***

## Group Normalization
{: #content6}

<button>Paper</button>{: .showText value="show"
     onclick="showText_withParent_PopHide(event);"}
<iframe hidden="" src="https://docs.google.com/viewer?url=https://arxiv.org/pdf/1803.08494.pdf&amp;embedded=true" frameborder="0" height="840" width="646" title="Layer Normalization" scrolling="auto"></iframe>


1. **Group Normalization:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents61}  
    __Group Normalization__ computes the mean and standard deviation over __groups of channels__ for _each training example_.  
    You can think of GN as being half way between _layer normalization_ and _instance normalization_:  
    {: #lst-p}
    * When we put all the channels into a single group, it becomes __Layer Normalization__  
    * When we put each channel in a different group, it becomes __Instance Normalization__  
    <br>

2. **Motivation/Advantages:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents62}  
    _Layer Norm_ and _Instance Norm_ were significantly inferior to BN on image recognition tasks. Group Normalization was able to achieve much closer performance to BN with a batch-size of 32 on ImageNet and outperformed it on smaller batch sizes.  

    For tasks like _object detection_ and _segmentation_ that __use much higher resolution images__ (and therefore cannot increase their batch size due to memory constraints), Group Normalization was shown to be a very effective normalization method.  
    <br>

3. **Effectiveness of Group Normalization:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents63}  
    > __Why is group normalization so effective compared to layer normalization and instance normalization?__  

    __Layer Norm__ makes an implicit assumption that <span>all channels are “equally important” when computing the mean</span>{: style="color: goldenrod"}. This assumption is often not true in __convolution layers__.  
    For instance, neurons near the edge of an image and neurons near the center of an image will have very different activation statistics.  This means that computing different statistics for different channels can give models much-needed flexibility.  

    __Instance Norm__, on the other hand, assumes that the <span>channels are completely independent from each other</span>{: style="color: goldenrod"}. Channels in an image are not completely independent though, so being able to leverage the statistics of nearby channels is an advantage group normalization has over instance normalization.  
    <br>


***

## Batch ReNormalization
{: #content7}

<button>Paper</button>{: .showText value="show"
     onclick="showText_withParent_PopHide(event);"}
<iframe hidden="" src="https://docs.google.com/viewer?url=https://arxiv.org/pdf/1702.03275.pdf&amp;embedded=true" frameborder="0" height="840" width="646" title="Layer Normalization" scrolling="auto"></iframe>


1. **Batch ReNormalization:**{: style="color: SteelBlue"}{: .bodyContents7 #bodyContents71}  
    __Batch ReNormalization__ is an extension of BN for applying batch normalization to small batch sizes.  
    > In the Authors words: "an effective extension to ensure that the training and inference models generate the same outputs that depend on individual examples rather than the entire mini-batch"  

    The authors propose to use a moving average while also taking the effect of previous layers on the statistics into account. Their method is – at its core – a simple reparameterization of normalization with the moving average. If we denote the moving average mean and standard deviation as $$\mu$$ and $$\sigma$$ and the mini-batch mean and standard deviation as $$\mu_B$$ and $$\sigma_B$$, the batch renormalization equation is:  
    <p>$$\frac{x_{i}-\mu}{\sigma}=\frac{x_{i}-\mu_{\mathcal{B}}}{\sigma_{\mathcal{B}}} \cdot r+d, \quad \text { where } r=\frac{\sigma_{\mathcal{B}}}{\sigma}, \quad d=\frac{\mu_{\mathcal{B}}-\mu}{\sigma}$$</p>  

    In other words, we multiply the batch normalized activations by $$r$$ and add $$d$$, where both $$r$$ and $$d$$ are computed from the mini-batch statistics and moving average statistics. The trick here is to __not backpropagate__ through $$r$$ and $$d$$. Though this means we ignore some of the effects of previous layers on previous mini batches, since the mini batch statistics and moving average statistics should be the same on average, the overall effect of this should cancel out on average as well.  
    <br>


2. **Motivation (derivation):**{: style="color: SteelBlue"}{: .bodyContents7 #bodyContents72}  
    The basic idea behind batch renormalization comes from the fact that we do not use the individual mini-batch statistics for batch normalization during inference. Instead, we use a __moving average__ of the mini-batch statistics. This is because a moving average provides a better estimate of the true mean and variance compared to individual mini-batches.  

    __Why don’t we use the moving average during training?__  
    The answer has to do with the fact that during training, we need to perform backpropagation. In essence, when we use some statistics to normalize the data, we need to __backpropagate through those statistics as well__. If we use the statistics of activations from previous mini-batches to normalize the data, we need to account for how the previous layer affected those statistics during backpropagation. If we ignore these interactions, we could potentially cause previous layers to keep on increasing the magnitude of their activations even though it has no effect on the loss. This means that if we use a moving average, we would need to store the data from all previous mini-batches during training, which is far too expensive.  
    <br>

3. **Performance:**{: style="color: SteelBlue"}{: .bodyContents7 #bodyContents73}  
    Unfortunately, batch renormalization’s performance still degrades when the batch size decreases (though not as badly as batch normalization), meaning group normalization still has a slight advantage in the small batch size regime.
    <br>

***

## Batch-Instance Normalization
{: #content8}

<button>Paper</button>{: .showText value="show"
     onclick="showText_withParent_PopHide(event);"}
<iframe hidden="" src="https://docs.google.com/viewer?url=https://arxiv.org/pdf/1805.07925.pdf&amp;embedded=true" frameborder="0" height="840" width="646" title="Layer Normalization" scrolling="auto"></iframe>


1. **Batch-Instance Normalization:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents81}  
    __Batch-Instance Normalization__ is an extension of _instance normalization_ that attempts to <span>account for differences in contrast and style in images</span>{: style="color: goldenrod"}. It is basically, just, an _interpolation between batch normalization and instance normalization_.  

    Denoting the batch normalized outputs and the instance normalized outputs as $$\hat{x}^{(B)}$$ and $$\hat{x}^{(I)}$$ each, the batch-instance normalized output can be expressed as:  
    <p>$$\mathbf{y}=\left(\rho \cdot \hat{\mathbf{x}}^{(B)}+(1-\rho) \cdot \hat{\mathbf{x}}^{(I)}\right) \cdot \gamma+\beta$$</p>  
    The interesting aspect of batch-instance normalization is that the balancing parameter $$\rho$$ is __learned__ through gradient descent.  
    <br>

2. **Motivation:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents82}  
    The problem with instance normalization is that it __completely erases style information__. Though this is beneficial in certain settings like style transfer, it can be problematic in settings like weather classification where the style (e.g. the brightness of the image) can be a crucial feature. In other words, the degree of style information that should be removed is dependent on the task at hand. Batch-instance normalization attempts to deal with this by __learning__ how much style information should be used for each __task and feature map (channel)__.  
    Thus, B-IN extends instance normalization to account for differences in contrast and style in images.  
    <br>

3. **Performance:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents83}  
    Batch-instance normalization outperformed batch normalization on CIFAR-10/100, ImageNet, domain adaptation, and style transfer. In image classification tasks, the value of $$\rho$$  tended to be close to $$0$$ or $$1$$, meaning many layers used either instance or batch normalization almost exclusively. In addition, layers tended to use batch normalization more than instance normalization, which fits the intuition proposed by the authors that instance normalization serves more as a method to eliminate unnecessary style variation. On style transfer – on the other hand – the model tended to use instance normalization more, which makes sense given style is much less important in style transfer.  

    The authors also found that in practice, using a higher learning rate for $$\rho$$ improves performance.  

    One important contribution of batch-instance normalization is that it showed that __models could learn to adaptively use different normalization methods using gradient descent__. This raises the question: _could models learn to use an even wider variety of normalization methods?_  
    This nicely leads us to the next normalization method: __Switchable Normalization__.    

***

## Switchable Normalization
{: #content9}

<button>Paper</button>{: .showText value="show"
     onclick="showText_withParent_PopHide(event);"}
<iframe hidden="" src="https://docs.google.com/viewer?url=https://arxiv.org/pdf/1811.07727.pdf&amp;embedded=true" frameborder="0" height="840" width="646" title="Layer Normalization" scrolling="auto"></iframe>

<button>Arxiv</button>{: .showText value="show"
     onclick="showText_withParent_PopHide(event);"}
<iframe hidden="" src="https://arxiv.org/pdf/1811.07727.pdf" frameborder="0" height="840" width="646" title="Layer Normalization" scrolling="auto"></iframe>


1. **Switchable Normalization:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents91}  
    __Switchable Normalization__ is a method that uses a weighted average of different mean and variance statistics from batch normalization, instance normalization, and layer normalization. Similar to batch-instance normalization, the weights were learned through backpropagation.  
    <br>

2. **Motivation:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents92}  
    Given the different methods proposed for normalization, common questions arise, including:  
    Is batch normalization still the best normalization method out-of-the-box? What if we combine different normalization methods? What if the best normalization method actually differs depending on the depth of the layer?  
    Switchable Normalization aims to answer those questions.  
    <br>

3. **Performance:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents93}  
    The authors showed that switch normalization could potentially outperform batch normalization on tasks such as image classification and object detection.  

    Perhaps more interestingly, the paper showed that <span>the statistics of instance normalization were used more heavily in earlier layers</span>{: style="color: goldenrod"}, whereas <span>layer normalization was preferred in the later layers</span>{: style="color: goldenrod"}, and <span>batch normalization being used in the middle</span>{: style="color: goldenrod"}. Smaller batch sizes lead to a preference towards layer normalization and instance normalization, as is expected.  
    <br>

***

## Spectral Normalization
{: #content10}

<button>Paper</button>{: .showText value="show"
     onclick="showText_withParent_PopHide(event);"}
<iframe hidden="" src="https://docs.google.com/viewer?url=https://arxiv.org/pdf/1805.07925.pdf&amp;embedded=true" frameborder="0" height="840" width="646" title="Layer Normalization" scrolling="auto"></iframe>


1. **Spectral Normalization:**{: style="color: SteelBlue"}{: .bodyContents10 #bodyContents101}  
    __Spectral Normalization__ is a method proposed to improve the training of __GANs__ by limiting the Lipschitz constant of the discriminator.  
    The authors restrict the Lipschitz constant by normalizing the weight matrices by their largest eigenvalue (or their spectral norm – hence the name). The largest eigenvalue is computed using the _power method_ which makes the computational cost of this method very cheap. (Compared to weight normalization, spectral normalization does not reduce the rank of the weight matrix.)[^1]  
    <br>

    SN is not designed to be a replacement for batch normalization, but it gives us a very interesting look into normalization in deep learning in general.  
    <br>

2. **Performance:**{: style="color: SteelBlue"}{: .bodyContents10 #bodyContents102}  
    Experimental results show that spectral normalization improves the training of GANs with minimal additional tuning.  
    <br>

***

## Further Exploration/Discussions
{: #content11}

Though recent papers have explored different normalization methods at different depths of the network, there are still many dimensions that can be explored. In [this paper](https://arxiv.org/pdf/1805.11604.pdf), the authors show that $$L_1$$ normalization performs better than batch normalization, suggesting that as we understand batch normalization better, we might be able to come up with more principled methods of normalization. This means that we might see new normalization methods use different statistics instead of changing what they compute the statistics over.  

[^1]: Most likely a wrong statement