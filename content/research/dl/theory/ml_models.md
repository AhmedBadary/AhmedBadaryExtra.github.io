---
layout: NotesPage
title: ML Models 
permalink: /work_files/research/theory/models
prevLink: /work_files/research/theory.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Statistical Models](#content1)
  {: .TOC1}
  * [SECOND](#content2)
  {: .TOC2}
<!--     * [THIRD](#content3)
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

* [Latent Variable Model Intuition (slides!)](http://mlvis2016.hiit.fi/latentVariableGenerativeModels.pdf)  
* [Radford Neal's Research: Latent Variable Models (publications)](http://www.cs.toronto.edu/~radford/res-latent.html)  
* [Basics of Statistical Machine Learning: models, estimation, MLE, inference (paper/note!)](http://pages.cs.wisc.edu/~jerryzhu/cs731/stat.pdf)  


## Statistical Models
{: #content1}

22. **Statistical Models:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents122}  
    A __Statistical Model__ is a, non-deterministic, mathematical model that embodies a set of _statistical assumptions_ concerning the generation of sample data.  
    It is specified as a mathematical relationship between one or more _random variables_ and other non-random variables.  

    __Formal Definition:__{: style="color: red"}  
    A __Statistical Model__ consists of a pair $$(S, \mathcal{P})$$ where $$S$$ is the _set of possible observations_ (the _sample space_) and $$\mathcal{P}$$ is a <span>_**set**_ of __probability distributions__</span>{: style="color: purple"} on $$S$$.  

    The set $$\mathcal{P}$$ can be (and is usually) __parametrized__:  
    <p>$$\mathcal{P}=\left\{P_{\theta} : \theta \in \Theta\right\}$$</p>  
    The set $$\Theta$$ defines the __parameters__ of the model.  

    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * It is important that a statistical model consists of a __set__ of probability distributions,  
        while a _probability model_ is just one *__known__* distribution.  
    <br>

1. **Parametric Model:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    A __parametric model__ is a set of probability distributions indexed by a parameter $$\theta \in \Theta$$. We denote this as:  
    <p>$$\{p(y ; \theta) | \theta \in \Theta\},$$</p>  
    where $$\theta$$ is the __parameter__ and $$\Theta$$ is the __Parameter-Space__.  

    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * The parametric way to classify would be to decide a model (Gaussian, Bernoulli, etc.) for the features of $$\boldsymbol{x}$$, and typically the models are different for different classes $$y$$.  
    <br>

    | In machine learning we are often interested in a function of the distribution $$T(F)$$, for example, the mean. We call $$T$$ the statistical functional, viewing $$F$$ the distribution itself a function of $$x$$. However, we will also abuse the notation and say $$\theta=T(F)$$ is a "parameter" even for nonparametric models.  
    <br>

2. **Non-Parametric Model:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    A __non-parametric model__ is one which cannot be parametrized by a fixed number of parameters.  
    __Non-parametric models__ differ from parametric models in that the model structure is not specified a priori but is instead _determined from data_. The term _non-parametric_ is not meant to imply that such models completely lack parameters but that the number and nature of the parameters are flexible and not fixed in advance.  

    __Examples:__  
    {: #lst-p}
    * A __histogram__ is a simple nonparametric estimate of a probability distribution.
    * __Kernel density estimation__ provides better estimates of the density than histograms.
    * __Nonparametric regression and semiparametric regression__ methods have been developed based on kernels, splines, and wavelets.  
    * __Data envelopment analysis__ provides efficiency coefficients similar to those obtained by multivariate analysis without any distributional assumption.
    * __KNNs__ classify the unseen instance based on the K points in the training set which are nearest to it.
    * A __support vector machine (SVM)__ (with a Gaussian kernel) is a nonparametric large-margin classifier.  
    * __Method of moments__ (statistics) with polynomial probability distributions.  
    <br>


3. **Other classes of Statistical Models:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    Given $$\mathcal{P}=\left\{P_{\theta} : \theta \in \Theta\right\}$$, the _set of probability distributions on $$S$$_.  
    * A model is __"parametric"__ if all the parameters are in finite-dimensional parameter spaces; i.e. $$\Theta$$ has __*finite dimension*__  
    * A model is __"non-parametric"__ if all the parameters are in infinite-dimensional parameter spaces  
    * A __"semi-parametric"__ model contains finite-dimensional parameters of interest and infinite-dimensional nuisance parameters  
    * A __"semi-nonparametric"__ model has both finite-dimensional and infinite-dimensional unknown parameters of interest  
    <br>

4. **Types of Statistical Models:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    * Linear Model
    * GLM - General Linear Model
    * GiLM - Generalized Linear Model
    * Latent Variable Model  
    <br>


11. **The Statistical Model for Linear Regression:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents111}  
    Given a (random) sample $$\left(Y_{i}, X_{i 1}, \ldots, X_{i p}\right), i=1, \ldots, n$$ the relation between the _observations_ $$Y_i$$ and the _independent variables_ $$X_{ij}$$ is formulated as:  
    <p>$$Y_{i}=\beta_{0}+\beta_{1} \phi_{1}\left(X_{i 1}\right)+\cdots+\beta_{p} \phi_{p}\left(X_{i p}\right)+\varepsilon_{i} \qquad i=1, \ldots, n$$</p>  
    where $${\displaystyle \phi_{1},\ldots ,\phi_{p}}$$ may be nonlinear functions. In the above, the quantities $$\varepsilon_i$$ are random variables representing errors in the relationship.   

    __The Linearity of the Model:__{: style="color: red"}  
    The _"linear"_ part of the designation relates to the appearance of the regression coefficients, $$\beta_j$$ in a linear way in the above relationship.  
    Alternatively, one may say that the predicted values corresponding to the above model, namely:  
    <p>$$\hat{Y}_{i}=\beta_{0}+\beta_{1} \phi_{1}\left(X_{i 1}\right)+\cdots+\beta_{p} \phi_{p}\left(X_{i p}\right) \qquad(i=1, \ldots, n)$$</p>  
    are __linear functions__ of the __coefficients__ $$\beta_j$$.  

    __Estimating the Parameters $$\beta_j$$:__  
    Assuming an estimation on the basis of a __least-squares__ analysis, estimates of the unknown parameters $$\beta_j$$ are determined by _minimizing a sum of squares function:_  
    <p>$$S=\sum_{i=1}^{n}\left(Y_{i}-\beta_{0}-\beta_{1} \phi_{1}\left(X_{i 1}\right)-\cdots-\beta_{p} \phi_{p}\left(X_{i p}\right)\right)^{2}$$</p>  

    __Effects of Linearity:__  
    {: #lst-p}
    * The function to be minimized is a quadratic function of the $$\beta_j$$ for which minimization is a relatively simple problem  
    * The derivatives of the function are linear functions of the $$\beta_j$$ making it easy to find the minimizing values  
    * The minimizing values $$\beta_j$$ are linear functions of the observations $$Y_i$$  
    * The minimizing values $$\beta_j$$ are linear functions of the random errors $$\varepsilon_i$$  which makes it relatively easy to determine the statistical properties of the estimated values of $$\beta_j$$.  
    <br>


5. **Latent Variable Models:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  
    __Latent Variable Models__ are statistical models that relate a set of observable variables (so-called manifest variables) to a set of latent variables.  

    __Core Assumption - Local Independence:__{: style="color: red"}  
    __Local Independence:__  
    The observed items are conditionally independent of each other given an individual score on the latent variable(s). This means that the latent variable *__explains__* why the observed items are related to another.  

    In other words, the targets/labels on the observations are the result of an individual's position on the latent variable(s), and that the observations have nothing in common after controlling for the latent variable.  

    <p>$$p(A,B\vert z) = p(A\vert z) \times (B\vert z)$$</p>  


    <button>Example of Local Independence</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/wnxPRKkVBA88V1k3i4HdWBTtn0NQFBi5gdNkTLcCeFk.original.fullsize.png){: width="100%" hidden=""}  


    __Methods for inferring Latent Variables:__{: style="color: red"}  
    {: #lst-p}
    * Hidden Markov models (HMMs)
    * Factor analysis
    * Principal component analysis (PCA)
    * Partial least squares regression
    * Latent semantic analysis and probabilistic latent semantic analysis
    * EM algorithms
    * Pseudo-Marginal Metropolis-Hastings algorithm
    * Bayesian Methods: LDA




    __Notes:__{: style="color: red"}    
    {: #lst-p}
    * Latent Variables *__encode__*  information about the data  
        e.g. in compression, a 1-bit latent variable can encode if a face is Male/Female.  
    * __Data Projection:__  
        You *__"hypothesis"__* how the data might have been generated (by LVs).  
        Then, the LVs __generate__ the data/observations.  
        <button>Visualisation with Density (Generative) Models</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        ![img](https://cdn.mathpix.com/snip/images/ctljXHCOfIzpttSIOCsFbQxjFmjrEcf4a5Dr9KbWnTI.original.fullsize.png){: width="100%" hidden=""}  
    * [**Latent Variable Models/Gaussian Mixture Models**](https://www.youtube.com/embed/I9dfOMAhsug){: value="show" onclick="iframePopA(event)"}
    <a href="https://www.youtube.com/embed/I9dfOMAhsug"></a>
        <div markdown="1"> </div>    
    * [**Expectation-Maximization/EM-Algorithm for Latent Variable Models**](https://www.youtube.com/embed/lMShR1vjbUo){: value="show" onclick="iframePopA(event)"}
    <a href="https://www.youtube.com/embed/lMShR1vjbUo"></a>
        <div markdown="1"> </div>    

<!-- 6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}
 -->

8. **Three ways to build classifiers:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18}  
    1. Generative models (e.g. LDA) [We’ll learn about LDA next lecture.]
        * Assume sample points come from probability distributions, different for each class.  
        * Guess form of distributions  
        * For each class $$C$$, fit distribution parameters to class $$C$$ points, giving $$P(X\vert Y = C)$$  
        * For each $$C$$, estimate $$P(Y = C)$$   
        * Bayes’ Theorem gives $$P(Y\vert X)$$  
        * If $$0-1$$ loss, pick class $$C$$ that maximizes $$P(Y = C\vert X = x)$$ [posterior probability] equivalently, maximizes $$P(X = x\vert Y = C) P(Y = C)$$  
    2. Discriminative models (e.g. logistic regression) [We’ll learn about logistic regression in a few weeks.]  
        * Model $$P(Y\vert X)$$ directly  
    3. Find decision boundary (e.g. SVM)  
        * Model $$r(x)$$ directly (no posterior)  

    Advantage of (1 & 2): $$P(Y\vert X)$$ tells you probability your guess is wrong  
        [This is something SVMs don’t do.]  
    Advantage of (1): you can diagnose outliers: $$P(X)$$ is very small  
    Disadvantages of (1): often hard to estimate distributions accurately;  
        real distributions rarely match standard ones.  


***

## Regression Models
{: #content2}

1. **Linear Models:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    A __Linear Model__ takes an input $$x$$ and computes a signal $$s = \sum_{i=0}^d w_ix_i$$ that is a _linear combination_ of the input with weights, then apply a scoring function on the signal $$s$$.  
    * __Linear Classifier as a Parametric Model__:  
        Linear classifiers $$f(x, W)=W x+b$$  are an example of a parametric model that sums up the knowledge of the training data in the parameter: weight-matrix $$W$$.  
    * __Scoring Function__:  
        * *__Linear Classification__*:  
            $$h(x) = sign(s)$$  
        * *__Linear Regression__*:  
            $$h(x) = s$$  
        * *__Logistic Regression__*:  
            $$h(x) = \sigma(s)$$  

<!-- 2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}

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