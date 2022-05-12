---
layout: NotesPage
title: Deep Generative Models
permalink: /work_files/research/dl/archits/dgms
prevLink: /work_files/research/dl.html
---


<div markdown="1" class = "TOC">
# Table of Contents

  * [Introduction and Preliminaries](#content9)
  {: .TOC9}
  * [Deep Generative Models](#content1)
  {: .TOC1}
  * [Likelihood-based Models](#content2)
  {: .TOC2}
<!--   
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


* [Probabilistic Models and Generative Neural Networks (paper)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4943066/)  
* [Latent Variable Model Intuition (slides!)](http://mlvis2016.hiit.fi/latentVariableGenerativeModels.pdf)  
* [Generative Models (OpenAI Blog!)](https://openai.com/blog/generative-models/)  




__In situations respecting the following assumptions, Semi-Supervised Learning should *improve performance*:__{: style="color: red"}  :  
{: #lst-p}
* Semi-supervised learning works <span>when $$p(\mathbf{y} \vert \mathbf{x})$$ and $$p(\mathbf{x})$$ are __tied__ together</span>{: style="color: goldenrod"}.  
    * This happens when $$\mathbf{y}$$ is closely associated with one of the causal factors of $$\mathbf{x}$$.  
* The <span>__best possible model__ of $$\mathbf{x}$$ (wrt. __generalization__)</span>{: style="color: goldenrod"} is the one that <span>*__uncovers__* the above __"true" structure__</span>{: style="color: goldenrod"}, with <span>$$\boldsymbol{h}$$ as a __latent variable__ that *__explains__* the __observed variations__ in $$\boldsymbol{x}$$</span>{: style="color: goldenrod"}.  
    * Since we can write the __Marginal Probability of Data__ as:  
        <p>$$p(\boldsymbol{x})=\mathbb{E}_ {\mathbf{h}} p(\boldsymbol{x} \vert \boldsymbol{h})$$</p>  
        * Because the __"true" generative process__ can be conceived as <span>*__structured__* according to this __directed graphical model__</span>{: style="color: purple"}, with $$\mathbf{h}$$ as the __parent__ of $$\mathbf{x}$$:  
            <p>$$p(\mathbf{h}, \mathbf{x})=p(\mathbf{x} \vert \mathbf{h}) p(\mathbf{h})$$</p>  
    * Thus, __The "ideal" representation learning discussed above should recover these latent factors__.  
* The <span>__marginal__ $$p(\mathbf{x})$$ is *__intimately tied__* to the __conditional__ $$p(\mathbf{y} \vert \mathbf{x})$$, and knowledge of the structure of the former should be helpful to learn the latter</span>{: style="color: purple"}.  
    * Since the __conditional distribution__ of $$\mathbf{y}$$ given $$\mathbf{x}$$ is <span>tied by *Bayes' rule* to the __components in the above equation__</span>{: style="color: purple"}:  
        <p>$$p(\mathbf{y} \vert \mathbf{x})=\frac{p(\mathbf{x} \vert \mathbf{y}) p(\mathbf{y})}{p(\mathbf{x})}$$</p>  





## Introduction and Preliminaries
{: #content9}

1. **Unsupervised Learning:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents91}  
    __Unsupervised Learning__ is the task of making inferences, by learning a better representation from some datapoints that do not have any labels associated with them.  
    It intends to learn/infer an __*a priori* probability distribution__ $$p_{X}(x)$$; I.E. it solves a __density estimation problem__.  
    It is a type of *__self-organized__* __Hebbian learning__ that helps find previously unknown patterns in data set without pre-existing labels.   
    ![img](/main_files/dl/archits/dgms/1.png){: width="100%"}  


2. **Density Estimation:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents92}  
    __Density Estimation__ is a problem in Machine Learning that requires learning a function $$p_{\text {model}} : \mathbb{R}^{n} \rightarrow \mathbb{R}$$, where $$p_{\text {model}}(x)$$ can be interpreted as a __probability  density function__ (if $$x$$ is continuous) or a __probability mass function__ (if $$x$$ is discrete) on the space that the examples were drawn from.  

    To perform such a task well, an algorithm needs to <span>learn the __structure of the data__</span>{: style="color: purple"} it has seen. It must know where examples cluster tightly and where they are unlikely to occur.  

    * __Types__ of Density Estimation:  
        * *__Explicit__*: Explicitly define and solve for $$p_\text{model}(x)$$  
        * *__Implicit__*: Learn model that can sample from $$p_\text{model}(x)$$ without explicitly defining it     

    <br>


3. **Generative Models (GMs):**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents93}  
    A __Generative Model__ is a _statistical model_ of the <span>__joint__ probability distribution</span>{: style="color: purple"} on $$X \times Y$$:  
    <p>$${\displaystyle P(X,Y)}$$</p>   
    where $$X$$ is an _observable_ variable and $$Y$$ is a _target_ variable.  

    In __supervised settings__, a __Generative Model__ is a model of the <span>__conditional__ probability</span>{: style="color: purple"} of the observable $$X,$$ given a target $$y,$$:  
    <p>$$P(X | Y=y)$$</p>   


    __Application - Density Estimation:__{: style="color: red"}  
    Generative Models address the __Density Estimation__ problem, a core problem in unsupervised learning, since they model   
    Given training data, GMs will generate new samples from the same distribution.   
    * __Types__ of Density Estimation:  
        * *__Explicit__*: Explicitly define and solve for $$p_\text{model}(x)$$  
        * *__Implicit__*: Learn model that can sample from $$p_\text{model}(x)$$ without explicitly defining it     


    __Examples of Generative Models:__{: style="color: red"}  
    {: #lst-p}
    * Gaussian Mixture Model (and other types of mixture model)
    * Hidden Markov Model
    * Probabilistic context-free grammar
    * Bayesian network (e.g. Naive Bayes, Autoregressive Model)
    * Averaged one-dependence estimators
    * Latent Dirichlet allocation (LDA)
    * Boltzmann machine (e.g. Restricted Boltzmann machine, Deep belief network)
    * Variational autoencoder
    * Generative Adversarial Networks
    * Flow-based Generative Model

    <button>A generative model for generative (graphical) models - Diagram</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/ZIHj9KE3aa7i-o5jSaxLD8fP-tDPzFtBf7ymVT8g2JQ.original.fullsize.png){: width="100%" hidden=""}  

    

    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * Generative Models are __Joint Models__.  
    * Latent Variables are __Random Variables__{: style="color: goldenrod"}.  
    <br>

<!-- 3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents93}
4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents94} -->

***

## Deep Generative Models
{: #content1}

1. **Generative Models (GMs):**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    

2. **Deep Generative Models (DGMs):**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    
    * DGMs __represent *probability distributions* over multiple variables__ in some way:  
        * Some allow the probability distribution function to be evaluated explicitly. 
        * Others do not allow the evaluation of the probability distribution function but support operations that implicitly require knowledge of it, such as drawing samples from the distribution.  
    * __Structure/Representation:__  
        * Some of these models are structured probabilistic models described in terms of graphs and factors, using the language of (probabilistic) graphical models.  
        * Others cannot be easily described in terms of factors but represent probability distributions nonetheless.  

<!-- 3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13} -->
<!-- 4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14} -->

<!-- 5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}
6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}
7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}
8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18}
 -->

***

## Likelihood-based Models
{: #content2}

1. **Likelihood-based Models:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    __Likelihood-based Model__: is a statistical model of a <span>joint distribution over data</span>{: style="color: purple"}.  
    It estimates $$\mathbf{p}_ {\text {data}}$$ from samples $$\mathbf{x}^{(1)}, \ldots, \mathbf{x}^{(n)} \sim \mathbf{p}_ {\text {data}}(\mathbf{x})$$.  
    It Learns a distribution $$p$$ that allows:  
    {: #lst-p}
    - <span>Computing probability of a sample</span>{: style="color: purple"} $$p(x)$$ for arbitrary $$x$$  
    - <span>Sampling</span>{: style="color: purple"} $$x \sim p(x)$$  
        Sampling is a computable efficient process that generates an RV $$x$$ that has the same distribution as a $$p_{\text{data}}$$.  
    The distribution $$\mathbf{p}_ {\text {data}}$$ is just a <span>__function__</span>{: style="color: purple"} that takes as an <span>input a sample $$x$$</span>{: style="color: purple"} and <span>outputs the probability of $$x$$</span>{: style="color: purple"} under the learned distribution.  

    __The Goal for Learning Likelihood-based Models:__{: style="color: red"}  
    <button>Show Goal</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
    * __Original Goal__: estimate $$\mathbf{p}_{\text {data}}$$ from samples $$\mathbf{x}^{(1)}, \ldots, \mathbf{x}^{(n)} \sim \mathbf{p}_{\text {data}}(\mathbf{x})$$.  
    * __Revised Goal - Function Approximation__: Find $$\theta$$ (the parameter vector indexing into the distribution space) so that you approximately get the data distribution.  
        I.E. Learn $$\theta$$ so that $$p_{\theta}(x) \approx p_{\text {data}}(x)$$.  
    {: hidden=""}


    __Motivation:__{: style="color: red"}  
    {: #lst-p}
    * __Solving Hard Problems__:  
        * __Generating Data__: synthesizing images, videos, speech, text  
        * __Compressing Data__: constructing efficient codes  
        * __Anomaly Detection__  
    <br>

2. **The Histogram Model:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}  
    The __Histogram__ Model is a very simple __likelihood-based__ model.  
    It is a model of __discrete data__ where the samples can take on values in a finite set $$\{1, \ldots, \mathrm{k}\}$$.  
    
    The __Goal:__ estimate $$\mathbf{p}_{\text {data}}$$ from samples $$\mathbf{x}^{(1)}, \ldots, \mathbf{x}^{(n)} \sim \mathbf{p}_{\text {data}}(\mathbf{x})$$.  

    The __Model__: a <span>__Histogram__</span>{: style="color: purple"}  
    {: #lst-p}
    * __Described__ by $$k$$ nonnegative numbers: $$\mathrm{p}_{1}, \ldots, \mathrm{p}_{\mathrm{k}}$$  
    * __Trained__ by <span>counting frequencies</span>{: style="color: purple"}  
        <p>$$\mathrm{p}_ {\mathrm{i}}=(\# \text { times } i \text { appears in the dataset) } /(\#\text { points in the dataset) }$$</p>  
    * __At Runtime__:  
        * __Inference__ (querying $$p_i$$ for arbitrary $$i$$): simply a lookup into the array $$\mathrm{p}_{1}, \ldots, \mathrm{p}_{\mathrm{k}}$$  
        * __Sampling__ (lookup into the inverse cumulative distribution function):  
            1. From the model probabilities $$p_{1}, \ldots, p_{k},$$ compute the cumulative distribution:  
                <p>$$\mathrm{F}_{\mathrm{i}}=\mathrm{p}_ {1}+\cdots+\mathrm{p}_ {\mathrm{i}} \quad$ for all $\mathrm{i} \in\{1, \ldots, \mathrm{k}\}$$</p>  
            2. Draw a uniform random number  $$u \sim[0,1]$$  
            3. Return the smallest $$i$$ such that $$u \leq F_{i}$$  

    __Generalization Problem:__{: style="color: red"}  
    {: #lst-p}
    * __The Curse of Dimensionality__: Counting fails when there are too many bins and __generalization__ is not achieved.  
        <button>Analysis</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        * (Binary) MNIST: $$28 \times 28$$ images, each pixel in $$\{0,1\}$$  
        * There are $$2^{784} \approx 10^{236} \approx 10^{236}$$ probabilities to estimate  
        * Any reasonable training set covers only a tiny fraction of this  
        * Each image influences only one parameter and there is only $$60,000$$ MNIST images:  
            <span>__No generalization__ whatsoever!</span>{: style="color: purple"}  
        {: hidden=""}
    * __Solution__: <span>__Function Approximation__</span>{: style="color: goldenrod"}  
        Instead of storing each probability store a <span>__*parameterized* function__</span>{: style="color: purple"} $$p_{\theta}(x)$$.  
    <br>

3. **Achieving Generalization via Function Approximation:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}  
    __Function Approximation__: Defines a *__mapping $$p_{\theta}$$__* from a __parameter space__ to a __space__ of __probability distributions__.  
    E.g. $$\theta$$ are the weights of a NN, $$p_{\theta}$$ some NN architecture with those weights set.    

    Instead of storing each probability store a <span>__*parameterized* function__</span>{: style="color: purple"} $$p_{\theta}(x)$$.  
    i.e. Instead of treating the probabilities $$p_1, ..., p_k$$ themselves as __parameters__, we define them to be <span>__functions__ of other parameters $$\theta$$</span>{: style="color: purple"}.  
    The probability of every data point $$p_i = p_{\theta}(x_i)$$ will be a function of $$\theta$$.  
    The mapping is defined such that whenever we update $$\theta$$ for any one particular data point, its likely to influence $$p_i$$ for other data points that are similar to it.  
    We __constraint__ the <span>__dimension__ $$d$$ of $$\theta \in \mathbb{R}^d$$ to be *__much less__* than the __number of possible images__</span>{: style="color: purple"}.  
    Such that the __parameter space $$\Theta$$__ is <span>*__indexing__* into the low-dimensional space inside the __set of all probability distributions__</span>{: style="color: purple"}.  
    This is how we achieve __Generalization__{: style="color: goldenrod"} through <span>function approximation</span>{: style="color: goldenrod"}.  

    __The Revised Goal for Learning Likelihood-based Models - Function Approximation:__{: style="color: red"}  
    {: #lst-p}
    * __Original Goal__: estimate $$\mathbf{p}_{\text {data}}$$ from samples $$\mathbf{x}^{(1)}, \ldots, \mathbf{x}^{(n)} \sim \mathbf{p}_{\text {data}}(\mathbf{x})$$.  
    * __Revised Goal - Function Approximation__: Find $$\theta$$ (the parameter vector indexing into the distribution space) so that you approximately get the data distribution.  
        I.E. Learn $$\theta$$ so that $$p_{\theta}(x) \approx p_{\text {data}}(x)$$.  

    __New Challenges:__{: style="color: red"}  
    {: #lst-p}
    * How do we design function approximators to effectively represent complex joint distributions over $$x$$, yet remain easy to train?  
    * There will be many choices for model design, each with different tradeoffs and different compatibility criteria.  
        * Define "what does it mean for one probability distribution to be _approximately_ equal to another"?  
            A <span>measure of distance between distributions: __distance function__</span>{: style="color: purple"}.  
            It needs to be __differentiable__ wrt $$\theta$$, works on __finite-datasets__, etc.  
        * How to "define $$p_{\theta}$$"?  
        * How to "learn/optimize $$\theta$$"?  
        * How to ensure software-hardware compatibility?  

    <span>Designing the __model__ and the __training procedure (optimization)__ go hand-in-hand</span>{: style="color: purple"}.
    <br>

4. **Architecture and Learning in Likelihood-based Models:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}  
    __Fitting Distributions:__{: style="color: red"}  
    {: #lst-p}
    * Given data $$\mathbf{x}^{(1)}, \ldots, \mathbf{x}^{(n)}$$ sampled from a "true" distribution $$\mathbf{p}_ {\text {data}}$$  
    * Set up a __model class__: a set of parameterized distributions $$\mathrm{p}_ {\theta}$$  
    * Pose a __search problem over parameters__:  
        <p>$$\arg \min_ {\theta} \operatorname{loss}\left(\theta, \mathbf{x}^{(1)}, \ldots, \mathbf{x}^{(n)}\right)$$</p>  
    * __Desiderata__ - Want the loss function + search procedure to:  
        * Work with large datasets ($$n$$ is large, say millions of training examples)  
        * Yield $\theta$ such that $$p_ {\theta}$$ matches $$p_{\text {data}}$$ — i.e. the training algorithm _"works"_.  
            Think of the __loss__ as a <span>__*distance* between distributions__</span>{: style="color: purple"}.  
        * Note that the training procedure can only see the empirical data distribution, not the true data distribution: we want the model to __generalize__.  


    __Objective - Maximum Likelihood:__{: style="color: red"}  
    {: #lst-p}
    * __Maximum Likelihood__: given a dataset $$\mathbf{x}^{(1)}, \ldots, \mathbf{x}^{(n)},$$ find $$\theta$$ by solving the optimization problem  
        <p>$$\arg \min _{\theta} \operatorname{loss}\left(\theta, \mathbf{x}^{(1)}, \ldots, \mathbf{x}^{(n)}\right)=\frac{1}{n} \sum_{i=1}^{n}-\log p_{\theta}\left(\mathbf{x}^{(i)}\right)$$</p>  
    * Statistics tells us that if the <span>model family is expressive enough</span>{: style="color: purple"} and if <span>enough data is given</span>{: style="color: purple"}, then <span>solving the maximum likelihood problem will yield parameters that generate the data</span>{: style="color: goldenrod"}.  
        This is __IMPORTANT__ since one of the main reasons for introducing and using these methods (e.g. __MLE__) is that <span>__they *work* in practice__</span>{: style="color: purple"} i.e. leads to an algorithm we can run in practice that actually produces good models.  
    * Equivalent to minimizing KL divergence between the empirical data distribution and the model:  
        <p>$$\hat{p}_{\text {data }}(\mathbf{x})=\frac{1}{n} \sum_{i=1}^{n} \mathbf{1}\left[\mathbf{x}=\mathbf{x}^{(i)}\right]$$</p>  
        <p>$$\mathrm{KL}\left(\hat{p}_{\mathrm{data}} \| p_{\theta}\right)=\mathbb{E}_{\mathbf{x} \sim \hat{p}_{\mathrm{data}}}\left[-\log p_{\theta}(\mathbf{x})\right]-H\left(\hat{p}_ {\mathrm{data}}\right)$$</p>  
        I.E. the __maximum likelihood objective__ exactly <span>*__measures__* how good of a __compressor__ the model is</span>{: style="color: purple"}.  


    __Optimization - Stochastic Gradient Descent:__{: style="color: red"}  
    __Maximum likelihood__ is an __optimization problem__. We use __SGD__ to solve it.  
    {: #lst-p}
    * SGD minimizes expectations: for $${f}$$ a differentiable function of $$\theta,$$ it solves  
        <p>$$\arg \min_ {\theta} \mathbb{E}[f(\theta)]$$</p>  
    * With maximum likelihood (which is an expectation in-of-itself), the optimization problem is  
        <p>$$\arg \min _{\theta} \mathbb{E}_{\mathbf{x} \sim \hat{p}_{\text {data }}}\left[-\log p_{\theta}(\mathbf{x})\right]$$</p>  
    * __Why maximum likelihood + SGD?__  
        __Same Theme__: It <span>*__works__*</span>{: style="color: purple"} with large datasets and is compatible with neural networks.  


    __Designing the Model:__{: style="color: red"}  
    Our goal is to design __Neural Network models__ that <span>*__fit__* into the __maximum likelihood + sgd framework__</span>{: style="color: purple"}.  
    {: #lst-p}
    * __Key requirement for maximum likelihood + SGD__: <span>efficiently compute $$\log p(x)$$ and its</span>{: style="color: purple"} __gradient__{: style="color: goldenrod"}.  
    * __The Model $$p_{\theta}$$:__ is chosen to be __Deep Neural Networks__{: style="color: goldenrod"}  
        They work in the regime of high expressiveness and efficient computation (assuming specialized hardware).  
    * __Designing the Networks__:  
        * Any setting of $$\theta$$ must define a __valid probability distribution__ over $$x$$:  
            <p>$$\forall \theta, \quad \sum_{\mathbf{x}} p_{\theta}(\mathbf{x})=1 \quad \text{ and } \quad p_{\theta}(\mathbf{x}) \geq 0 \quad \forall \mathbf{x}$$</p>  
            * __Difficulty:__ The number of terms in the sum is the number of __possible data points__, thus, it is __exponential in the dimension__.  
                Thus, a naive implementation would have a forward pass w/ exponential time.  
            * __Energy-based Models__ do not have this constraint in the model definition, but then have to deal with that constraint in the training algorithm making it very hard to deal with/optimize.  
        * $$\log p_{\theta}(x)$$ should be __easy to evaluate and differentiate__ with respect to $$\theta$$   
        * This can be __tricky__ to set up!  


    __Bayes Nets and Neural Nets:__{: style="color: red"}  
    One way to __satisfy the condition__ of <span>defining a valid probability distribution over $$x$$</span>{: style="color: purple"} is to __model the variables with a Bayes Net__.  

    __Main Idea:__  
    <span>place a __Bayes Net__ structure (a directed acyclic graph) over the variables in the data, and model the __conditional distributions__ with Neural Networks</span>{: style="color: goldenrod"}.  

    This <span>Reduces the problem to __designing conditional likelihood-based models for single variables__</span>{: style="color: purple"}.  
    
    We know how to do this: the neural net takes variables being conditioned on as input, and outputs the distribution for the variable being predicted; NNs usually condition on a lot of stuff (features) and predict a single small variable (target $$y$$) this is done in practice all the time in supervised settings (e.g. classification).  

    This (the BN representation) yields __massive savings in the number of parameters to represent a joint distribution__.  
    <button>A Bayes Net over five variables</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/bkKsJ-vXI0OZXqG7-e5wqAW28DsUGsNKhz9VllwBvaE.original.fullsize.png){: width="100%" hidden=""}  

    __Does this work in practice?__{: style="color: red"}  
    {: #lst-p}
    * Given a Bayes net structure, <span>setting the __conditional distributions__ to __neural networks__</span>{: style="color: purple"} will yield a <span>*__tractable__* __log likelihood__ and __gradient__</span>{: style="color: purple"}.  
        Great for __maximum likelihood training__:  
        <p>$$\log p_{\theta}(\mathbf{x})=\sum_{i=1}^{d} \log p_{\theta}\left(x_{i} | \text { parents }\left(x_{i}\right)\right)$$</p>  
    * __Expressiveness:__ it is completely expressive.  
        Assuming a __fully expressive Bayes Net structure__: <span>any __joint distribution__ can be written as a __product of conditionals__</span>{: style="color: purple"}  
        <p>$$\log p(\mathbf{x})=\sum_{i=1}^{d} \log p\left(x_{i} | \mathbf{x}_ {1: i-1}\right)$$</p>  
    * This is known as an __Autoregressive Model__.  

    <div class="borderexample" markdown="1">
    <span>
    __Conclusion:__  
    <span>An *__expressive__* __Bayes Net structure__ with __Neural Network conditional distributions__ yields an *__expressive__* model for $$p(x)$$ with *__tractable__* __maximum likelihood training__</span>{: style="color: goldenrod"}.   
    </span>  
    </div>  
    <br>


5. **Autoregressive Models:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}  


    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * Very useful if the problem we are modeling requires a fixed size output (e.g. auto-regressive models).
    * Autoregressive models such as PixelRNN instead train a network that models the conditional distribution of every individual pixel given previous pixels (to the left and to the top). This is similar to plugging the pixels of the image into a char-rnn, but the RNNs run both horizontally and vertically over the image instead of just a 1D sequence of characters.  
    <br>

<!-- 6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents26}

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