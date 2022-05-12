---
layout: NotesPage
title: Introduction and Basics of Deep Learning
permalink: /work_files/research/dl/theory/dl_book_pt2
prevLink: /work_files/research/dl/theory.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Introduction: Deep FeedForward Neural Networks](#content1)
  {: .TOC1}
  * [Gradient-Based Learning](#content2)
  {: .TOC2}
  * [Output Units](#content3)
  {: .TOC3}
<!--     * [FOURTH](#content4)
  {: .TOC4}
  * [FIFTH](#content5)
  {: .TOC5}
  * [SIXTH](#content6)
  {: .TOC6} -->
</div>

***
***

![img](https://cdn.mathpix.com/snip/images/xdjhM_cvHBtsMV1_70E_u-aDqFodvye8v9dcrB_QWDA.original.fullsize.png){: width="80%"}  

## Introduction: Deep Feedforward Neural Networks
{: #content1}

1. **(Deep) FeedForward Neural Networks:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    For a classifier; given $$y=f^{\ast}(\boldsymbol{x})$$, maps an input $$\boldsymbol{x}$$ to a category $$y$$.  
    An __FNN__ defines a mapping $$\boldsymbol{y}=f(\boldsymbol{x} ; \boldsymbol{\theta})$$  and learns the value of the parameters $$\boldsymbol{\theta}$$  that result in the best function approximation.  

    * FNNs are called __networks__ because they are typically represented by composing together many different functions
    * The model is associated with a __DAG__ describing how the functions are composed together. 
    * Functions connected in a __chain structure__ are the most commonly used structure of neural networks.  
        > E.g. we might have three functions $$f^{(1)}, f^{(2)},$$ and $$f^{(3)}$$ connected in a chain, to form $$f(\boldsymbol{x})=f^{(3)}\left(f^{(2)}\left(f^{(1)}(\boldsymbol{x})\right)\right)$$; being called the $$n$$-th __Layer__ respectively.   
    * The overall length of the chain is the __depth__ of the model.  
    * During training, we drive $$f(\boldsymbol{x})$$ to match $$f^{\ast}(\boldsymbol{x})$$.   
        The training data provides us with noisy, approximate examples of $$f^{\ast}(\boldsymbol{x})$$ evaluated at different training points.  
    <br>

2. **FNNs from Linear Models:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    Consider linear models biggest limitation: model capacity is limited to linear functions.  
    To __extend__ linear models to represent non-linear functions of $$\boldsymbol{x}$$ we can:  
    {: #lst-p}
    * Apply the linear model not to $$\boldsymbol{x}$$ itself but <span>_to a transformed input_ $$\phi(\boldsymbol{x})$$</span>{: style="color: purple"}, where $$\phi$$ is a <span>__nonlinear transformation__</span>{: style="color: purple"}.  
    * Equivalently, apply the __kernel trick__ to obtain nonlinear learning algorithm based on implicitly applying the $$\phi$$ mapping.  

    <span>We can think of $$\phi$$ as providing a __set of features *describing*__ $$\boldsymbol{x}$$, or as providing a __new representation__ for $$\boldsymbol{x}$$.</span>{: style="color: goldenrod"}  
    __Choosing the mapping $$\phi$$:__  
    {: #lst-p}
    1. Use a very generic $$\phi$$, s.a. infinite-dimensional (RBF) kernel.  
        If $$\phi(\boldsymbol{x})$$ is of _high enough dimension_, we can _always have enough capacity_ to fit the training set, but _generalization_ to the test set often _remains poor_.  
        Very generic feature mappings are usually _based only_ on the _principle of local smoothness_ and do not encode enough prior information to solve advanced problems.  
    2. Manually Engineer $$\phi$$.  
        Requires decades of human effort and the results are usually poor and non-scalable.  
    3. The _strategy_ of __deep learning__ is to <span>__learn $$\phi$$__</span>{: style="color: purple"}.  
        * We have a __model__:  
            <p>$$y=f(\boldsymbol{x} ; \boldsymbol{\theta}, \boldsymbol{w})=\phi(\boldsymbol{x} ; \boldsymbol{\theta})^{\top} \boldsymbol{w}$$</p>  
            We now have __parameters $$\theta$$__ that we <span>use to __learn $$\phi$$__ from a <span>*__broad class of functions__*</span>{: style="color: purple"}</span>{: style="color: purple"}, and __parameters $$\boldsymbol{w}$$__ that <span>__map__ from _$$\phi(\boldsymbol{x})$$_ to the _desired output_</span>{: style="color: purple"}.  
            This is an example of a __deep FNN__, with $$\phi$$ defining a __hidden layer__.   
        * This approach is the _only one_ of the three that _gives up_ on the _convexity_ of the training problem, but the _benefits outweigh the harms_.  
        * In this approach, we parametrize the representation as $$\phi(\boldsymbol{x}; \theta)$$ and use the optimization algorithm to find the $$\theta$$ that corresponds to a good representation.  
        * __Advantages:__  
            * __Capturing the benefit of the *first* approach__:  
                by being highly generic — we do so by using a very broad family $$\phi(\boldsymbol{x};\theta)$$.  
            * __Capturing the benefit of the *second* approach__:  
                Human practitioners can encode their knowledge to help generalization by designing families $$\phi(\boldsymbol{x}; \theta)$$ that they expect will perform well.  
                The __advantage__ is that the human designer only needs to find the right general function family rather than finding precisely the right function.  

    Thus, we can _motivate_ __Deep NNs__ as a way to do <span>__automatic, *non-linear* feature extraction__</span>{: style="color: goldenrod"} from the __inputs__.  

    This general principle of <span>improving models by learning features</span>{: style="color: purple"} extends beyond the feedforward networks to all models in deep learning.  
    FFNs are the application of this principle to learning __deterministic mappings__ from $$\boldsymbol{x}$$ to $$\boldsymbol{y}$$ that __lack__ *__feedback connections__*.  
    Other models, apply these principles to learning __stochastic mappings__, __functions with feedback__, and __probability distributions__ _over a single vector_.  


    __Advantage and Comparison of Deep NNs:__{: style="color: red"}  
    {: #lst-p}
    * __Linear classifier:__  
        * __Negative:__ Limited representational power
        * __Positive:__ Simple
    * __Shallow Neural network (Exactly one hidden layer):__  
        * __Positive:__ Unlimited representational power
        * __Negative:__ Sometimes prohibitively wide 
    * __Deep Neural network:__  
        * __Positive:__ Unlimited representational power
        * __Positive:__ Relatively small number of hidden units needed
    <br>

3. **Interpretation of Neural Networks:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    It is best to think of feedforward networks as __function approximation machines__ that are designed to achieve <span>_statistical generalization_</span>{: style="color: purple"}, occasionally drawing some insights from what we know about the brain, rather than as models of brain function.  

<!-- 4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14} -->

<!-- 5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18}
 -->

***

## Gradient-Based Learning
{: #content2}

1. **Stochastic Gradient Descent and FNNs:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    __Stochastic Gradient Descent__ applied to _nonconvex_ loss functions has _no convergence guarantees_ and is _sensitive_ to the _values_ of the _initial parameters_.  

    Thus, for FNNs (since they have _nonconvex loss functions_):  
    {: #lst-p}
    * *__Initialize all weights to small random values__*.  
    * The *__biases__* may be *__initialized to zero or to small positive values__*.  
    <br>

2. **Learning Conditional Distributions with Maximum Likelihood:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}  
    When __Training__ using __Maximum Likelihood__:  
    The *__cost function__* is, simply, the *__negative log-likelihood__*.  
    Equivalently, the *__cross-entropy__* _between_ the _training data_ and the _model distribution_.  

    $$J(\boldsymbol{\theta})=-\mathbb{E}_{\mathbf{x}, \mathbf{y} \sim \hat{p}_{\text {data }}} \log p_{\text {model }}(\boldsymbol{y} | \boldsymbol{x})  \tag{6.12}$$  

    * The specific form of the cost function changes from model to model, depending on the specific form of $$\log p_{\text {model}}$$.  
    * The expansion of the above equation typically yields some terms that do not depend on the model parameters and may be discarded.  

    __Maximum Likelihood and MSE:__  
    The equivalence between _maximum likelihood estimation with an output distribution_ and _minimization of mean squared error_ holds not just for a linear model, but in fact, the equivalence holds regardless of the $$f(\boldsymbol{x} ; \boldsymbol{\theta})$$ used to predict the mean of the Gaussian.  
    <button>Example: MSE from MLE with gaussian distr.</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        ![img](/main_files/dl_book/22.png){: hidden=""}  

    <p hidden>If $$p_{\text {model }}(\boldsymbol{y} | \boldsymbol{x})=\mathcal{N}(\boldsymbol{y} ; f(\boldsymbol{x} ; \boldsymbol{\theta}), \boldsymbol{I})$$ , then we recover the mean squared error cost, </p> 
    <p hidden>$$J(\theta)=\frac{1}{2} \mathbb{E}_{\mathbf{x}, \mathbf{y} \sim \hat{p}_{\text {data }}}\|\boldsymbol{y}-f(\boldsymbol{x} ; \boldsymbol{\theta})\|^{2}+\mathrm{const} \tag{6.13}$$ </p>  
    <p hidden>up to a scaling factor of $$1/2$$ and a term that does not depend on $$\theta$$.  
    The discarded constant is based on the variance of the Gaussian distribution, which in this case we chose not to parametrize.</p>

    __Why derive the cost function from Maximum Likelihood?__  
    It removes the burden of designing cost functions for each model.  
    Specifying a model $$p(\boldsymbol{y} | \boldsymbol{x})$$ automatically determines a cost function $$\log p(\boldsymbol{y} | \boldsymbol{x})$$.  

    __Cost Function Design - Desirable Properties:__  
    * The *__gradient__* of the cost function must be *__large__* and *__predictable__* enough to serve as a good guide.  
        Functions that *__saturate__* (become very flat) undermine this objective because they make the gradient become very small. In many cases this happens because the activation functions used to produce the output of the hidden units or the output units saturate.  
        The negative log-likelihood helps to avoid this problem for many models. Several output units involve an exp function that can saturate when its argument is very negative. The log function in the negative log-likelihood cost function undoes the exp of some output units.  

    <button>Making cross-entropy-cost-based training coherent</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        ![img](/main_files/dl_book/11.png){: hidden=""}  


3. **Learning Conditional Statistics:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}  
    Instead of learning a full probability distribution $$p(\boldsymbol{y} | \boldsymbol{x} ; \boldsymbol{\theta})$$, we often want to learn just one conditional statistic of $$\boldsymbol{y}$$ given $$\boldsymbol{x}$$.  
    > For example, we may have a predictor $$f(\boldsymbol{x} ; \boldsymbol{\theta})$$  that we wish to employ to predict the mean of $$\boldsymbol{y}$$.  

    __The Cost Function as a *Functional:*__  
    If we use a sufficiently powerful neural network, we can think of the neural network as being able to represent any function $$f$$ from a wide class of functions, with this class being limited only by features such as continuity and boundedness rather than by having a specific parametric form. From this point of view, we can view the cost function as being a __functional__ rather than just a function.  
    A __Functional__ is a mapping from functions to real numbers.  
    We can thus think of _learning as choosing a function_ rather than merely choosing a set of parameters.  
    We can design our cost functional to have its minimum occur at some specific function we desire.  
    > For example, we can design the cost functional to have its minimum lie on the function that maps $$\boldsymbol{x}$$  to the expected value of $$\boldsymbol{y}$$ given $$\boldsymbol{x}$$.  

    Solving an optimization problem with respect to a function requires a mathematical tool called __calculus of variations__, described in _section 19.4.2._  

4. **Important Results in Optimization:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}  
    The __calculus of variations__ can be used to derive the following two important results in Optimization:  
    1. Solving the optimization problem  
        <p>$${\displaystyle f^{\ast}=\underset{f}{\arg \min } \: \mathbb{E}_{\mathbf{x}, \mathbf{y} \sim p_{\text {data }}}\|\boldsymbol{y}-f(\boldsymbol{x})\|^{2}} \tag{6.14}$$</p>   
        yields  
        <p>$${\displaystyle f^{\ast}(\boldsymbol{x})=\mathbb{E}_{\mathbf{y} \sim p_{\text {data }}(\boldsymbol{y} | \boldsymbol{x})}[\boldsymbol{y}] \tag{6.15}}$$</p>  
        so long as this function lies within the class we optimize over.  
        In words: if we could train on infinitely many samples from the true data distribution, *__minimizing the MSE cost function__* would give a __*function* that *predicts* the *mean of $$\boldsymbol{y}$$* for *each* value of *$$\boldsymbol{x}$$*__.  
        > Different cost functions give different statistics.  
    2. Solving the optimization problem (commonly known as __Mean Absolute Error__)  
        <p>$$f^{\ast}=\underset{f}{\arg \min } \: \underset{\mathbf{x}, \mathbf{y} \sim p_{\mathrm{data}}}{\mathbb{E}}\|\boldsymbol{y}-f(\boldsymbol{x})\|_ {1} \tag{6.16}$$</p>  
        yields a __*function* that predicts the *median* value of *$$\boldsymbol{y}$$* for each $$\boldsymbol{x}$$__, as long as such a function may be described by the family of functions we optimize over.   

    * [Derivations (linear? prob not)](http://www.stat.cmu.edu/~larry/=stat401/lecture-01.pdf)  


    __Drawbacks of MSE and MAE (mean absolute error):__  
    They often lead to poor results when used with *__gradient-based__* optimization.  
    Some output units that saturate produce very small gradients when combined with these cost functions.  
    This is one reason that the __cross-entropy__ cost function is _more popular_ than __MSE__ or __MAE__, even when it is not necessary to estimate an entire distribution $$p(\boldsymbol{y} | \boldsymbol{x})$$.  


<!-- 5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents26}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents27}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents28}
 -->

***

## Output Units
{: #content3}

1. **Introduction:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}  
    The choice of cost function is tightly coupled with the choice of output unit. Most of the time, we simply use the cross-entropy between the data distribution and the model distribution.  
    Thus, the choice of _how to represent the output_ then determines the form of the cross-entropy function.  

    Throughout this analysis, we suppose that:  
    _The FNN provides a set of hidden features defined by_ $$\boldsymbol{h}=f(\boldsymbol{x} ; \boldsymbol{\theta})$$.  
    The _role of the output layer_, thus, is to _provide some additional transformation from the features to complete the task_ the FNN is tasked with.  


2. **Linear Units:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}  
    __Linear Units__ are a simple kind of output units, based on an _affine transformation_ with no non-linearity.  
    __Mathematically,__ given features $$\boldsymbol{h}$$, a layer of linear output units produces a vector $$\hat{\boldsymbol{y}}=\boldsymbol{W}^{\top} \boldsymbol{h}+\boldsymbol{b}$$.   
    
    __Application:__ used for *__Gaussian Output Distributions__*.  
    Linear output layers are often used to __produce the mean of a conditional Gaussian Distributions__:  
    <p>$$p(\boldsymbol{y} | \boldsymbol{x})=\mathcal{N}(\boldsymbol{y} ; \hat{\boldsymbol{y}}, \boldsymbol{I}) \tag{6.17}$$</p>   
    In this case, _maximizing the log-likelihood_ is equivalent to _minimizing the MSE_.  

    __Learning the Covariance of the Gaussian:__  

    The MLE framework makes it straightforward to:  
    {: #lst-p}
    * Learn the covariance of the Gaussian too
    * Make the covariance of the Gaussian be a function of the input  
    However, the covariance must be constrained to be a _positive definite matrix_ for all inputs.  
    > It is difficult to satisfy such constraints with a linear output layer, so typically other output units are used to parametrize the covariance.  
    > > Approaches to modeling the covariance are described shortly, in _section 6.2.2.4._  


    __Saturation:__  
    Because linear units do not saturate, they pose little difficulty for gradient- based optimization algorithms and may be used with a wide variety of optimization algorithms.  



3. **Sigmoid Units:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}  
    __Sigmoid Units__ 

    __Binary Classification:__ is a classification problem over two classes. It requires predicting the value of a _binary variable $$y$$_. It is one of many tasks requiring that.  
    __The MLE approach__ is to define a *__Bernoulli distribution__* over $$y$$ conditioned on $$\boldsymbol{x}$$.  
    A __Bernoulli distribution__ is defined by just _a single_ number.  
    The Neural Network needs to predict only $$P(y=1 \vert \boldsymbol{x})$$.  



<!-- 4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents34}  

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents35}  

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents36}  

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents37}  

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents38}  

 -->