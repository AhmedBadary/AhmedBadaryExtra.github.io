---
layout: NotesPage
title: The Naive Bayes Classifier
permalink: /work_files/research/ml/naive_bayes
prevLink: /work_files/research/ml.html
---


<div markdown="1" class = "TOC">
# Table of Contents

  * [Introduction and the Naive Bayes Classifier](#content1)
  {: .TOC1}
  <!-- * [SECOND](#content2)
  {: .TOC2} -->
</div>

***
***

[Full Treatment of Naive Bayes Classification](http://www.cs.columbia.edu/~mcollins/em.pdf)  
[Bayes Classifier and Bayes Error (paper)](https://www.cs.helsinki.fi/u/jkivinen/opetus/iml/2013/Bayes.pdf)  
[Bayes Classifier and Bayes Error (question)](https://stats.stackexchange.com/questions/296014/why-is-the-naive-bayes-classifier-optimal-for-0-1-loss?noredirect=1&lq=1)  
[Naive Bayes CS188 (+Probabilistic Calibration)](https://www.youtube.com/watch?v=1nOb0vwWkAE)  

![img](/main_files/misc/naive_bayes_mindmap.png){: width="100%"}  

> A Naive Bayes classifier that figured out that you liked pickles and ice cream would probably naively recommend you a pickle ice cream.  


## Introduction and the Naive Bayes Classifier
{: #content1}

0. **Naive Bayes:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents10}  
    __Naive Bayes__ is a simple technique for *__constructing classifiers__*.  

1. **Naive Bayes Classifiers:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    __Naive Bayes Classifiers__ are a family of simple probabilistic classifiers based on applying [_Bayes' Theorem_](https://en.wikipedia.org/wiki/Bayes%27_theorem) with strong (naive) independence assumptions between the features.  

    __The Assumptions:__{: style="color: red"}  
    {: #lst-p}
    1. __Naive Independence__: the feature probabilities are indpendenet given a class $$c$$.   
    2. __Bag-of-Words__: we assume that the position of the words does _not_ matter.  
    <br>


    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * Not a __Bayesian Method__: the name only references the use of Bayes' theorem in the classifier's decision rule  
    * The __Naive Bayes Classifier__ is a *__Bayes Classifier__* (i.e. minimizes the prob of misclassification)  
    * __As a Parametric Model (analysis)__:  
        <button>Analysis</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        * A Bayes classifier basically picks the label $$y$$ that has the maximum probability, given that testing data-point $$x$$:  
            $$y^{* }=\operatorname{argmax}_ {y} P(y)=\operatorname{argmax}_ {y} \frac{P(x \mid y) P(y)}{P(x)}$$  
            If you assume the features of $$x$$ are conditionally independent given the label, you get the Naive Bayes classifier.  
            So, classification depends a lot on $$P(x \mid y)$$. The parametric way to classify would be to decide a model (Gaussian, Bernoulli, etc.) for the features of $$x$$, and typically the models are different for different classes $$y$$. The parameters here are the parameters of you model (mean and covariance for Gaussian, individual feature probabilities for Bernoulli, etc.) and the training problem becomes a parameter estimation problem.
        {: hidden=""}
    <br>

2. **The Probabilistic Model (Naive Bayes Probability/Statistical Model):**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    Abstractly, naive Bayes is a __conditional probability model__:  
    given a problem instance to be classified, represented by a vector $${\displaystyle \: \mathbf{x} =(x_{1},\dots ,x_{n})}$$ representing some $$n$$ features (independent variables), it assigns to this instance probabilities  
    <p>$${\displaystyle p(C_{k}\mid x_{1},\dots ,x_{n}) = p(C_{k}\mid \mathbf {x})}$$</p>  
    for each of the $$k$$ possible classes $$C_k$$.  

    Using __Bayes' Theorem__ we _decompose the conditional probability_ as:  
    <p>$${\displaystyle p(C_{k}\mid \mathbf {x} )={\frac {p(C_{k})\ p(\mathbf {x} \mid C_{k})}{p(\mathbf {x} )}}\,}$$</p>  

    Notice that the *__numerator__* is equivalent to the *__joint probability distribution__*:  
    <p>$$p\left(C_{k}\right) p\left(\mathbf{x} | C_{k}\right) = p\left(C_{k}, x_{1}, \ldots, x_{n}\right)$$</p>  

    Using the __Chain-Rule__ for repeated application of the conditional probability, the _joint probability_ model can be rewritten as:  
    <p>$$p(C_{k},x_{1},\dots ,x_{n})\, = p(x_{1}\mid x_{2},\dots ,x_{n},C_{k})p(x_{2}\mid x_{3},\dots ,x_{n},C_{k})\dots p(x_{n-1}\mid x_{n},C_{k})p(x_{n}\mid C_{k})p(C_{k})$$</p>  

    Using the __Naive Conditional Independence__ assumptions:  
    <p>$$p\left(x_{i} | x_{i+1}, \ldots, x_{n}, C_{k}\right)=p\left(x_{i} | C_{k}\right)$$</p>  
    Thus, we can write the __joint model__ as:  
    <p>$${\displaystyle {\begin{aligned}p(C_{k}\mid x_{1},\dots ,x_{n})&\varpropto p(C_{k},x_{1},\dots ,x_{n})\\&=p(C_{k})\ p(x_{1}\mid C_{k})\ p(x_{2}\mid C_{k})\ p(x_{3}\mid C_{k})\ \cdots \\&=p(C_{k})\prod _{i=1}^{n}p(x_{i}\mid C_{k})\,,\end{aligned}}}$$</p>  

    Finally, the *__conditional distribution over the class variable $$C$$__* is:  
    <p>$${\displaystyle p(C_{k}\mid x_{1},\dots ,x_{n})={\frac {1}{Z}}p(C_{k})\prod _{i=1}^{n}p(x_{i}\mid C_{k})}$$</p>   
    where, $${\displaystyle Z=p(\mathbf {x} )=\sum _{k}p(C_{k})\ p(\mathbf {x} \mid C_{k})}$$ is a __constant__ scaling factor, a __dependent only__ on the, _known_, feature variables $$x_i$$s.  
    <br>

3. **The Classifier:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    We can construct the __classifier__ from the __probabilistic model__ above.  
    The __Naive Bayes Classifier__ combines this model with a __decision rule__.  

    __The Decision Rule:__{: style="color: red"}  
    we commonly use the [__Maximum A Posteriori (MAP)__](https://en.wikipedia.org/wiki/Maximum_a_posteriori_estimation) hypothesis, as the decision rule; i.e. pick the hypothesis that is most probable.  

    The Classifier is the _function that assigns a class label $$\hat{y} = C_k$$_ for some $$k$$ as follows:  
    <p>$${\displaystyle {\hat {y}}={\underset {k\in \{1,\dots ,K\}}{\operatorname {argmax} }}\ p(C_{k})\displaystyle \prod _{i=1}^{n}p(x_{i}\mid C_{k}).}$$</p>  

    It, basically, maximizes the probability of the class given an input $$\boldsymbol{x}$$.  
    <br>

4. **Naive Bayes Estimate VS MAP Estimate:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    __MAP Estimate:__  
    <p>$${\displaystyle {\hat {y}_{\text{MAP}}}={\underset {k\in \{1,\dots ,K\}}{\operatorname {argmax} }}\ p(C_{k})\ p(\mathbf {x} \mid C_{k})}$$</p>  
    __Naive Bayes Estimate:__  
    <p>$${\displaystyle {\hat {y}_{\text{NB}}}={\underset {k\in \{1,\dots ,K\}}{\operatorname {argmax} }}\ p(C_{k})\displaystyle \prod _{i=1}^{n}p(x_{i}\mid C_{k})}$$</p>  

5. **Estimating the Parameters of the Classifier:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  
    __Parameters to be Estimated:__{: style="color: red"}  
    * The __prior probability of each class__: 
        <p>$$p(C_{k})$$</p>  
    * The __conditional probability of each feature (word) given a class__:  
        <p>$$p(x_{i}\mid C_{k}) \:\: \forall i \in {1, .., n}$$</p>  

    We, generally, use __Maximum Likelihood Estimates__ for the parameters.  

    __The MLE Estimates for the Parameters:__{: style="color: red"}  
    * $$\hat{P}(C_k) = \dfrac{\text{doc-count}(C=C_k)}{N_\text{doc}}$$,  
    <br>
    * $$\hat{P}(x_i | C_i) = \dfrac{\text{count}(x_i,C_j)}{\sum_{x \in V} \text{count}(x, C_j)}$$  
    <br>

6. **MLE Derivation of the Parameter Estimates:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}  
    * [Derivation](http://www.cs.cornell.edu/courses/cs5740/2017sp/res/nb-prior.pdf)  
    * [Partial derivative of a summation (stackexchange - helpful hint)](https://math.stackexchange.com/questions/2605546/partial-derivative-of-a-summation)  
    
    The __Likelihood__ of the observed data (TBC)  

7. **Motivation:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}  
    To estimate the parameters of the "true" MAP estimate, we need a prohibitive number of examples ~ $$\mathcal{O}(\vert x\vert^n \cdot \vert C\vert)$$.  

8. **Notes:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18}
    * In a naive Bayes classifier we are interested in computing the conditional $$p(y \mid x ; \theta) \propto p(y ; \theta) \prod_{i}^{d} p\left(x_{i} \mid y ; \theta\right)$$.  
        Is this a parametric or nonparametric model? The model is specified by $$\mathcal{H}=\{p(x, y ; \theta)\}$$ where $$\theta$$ contains the parameter for the class prior multinomial distribution $$p(y)$$ (finite number of parameters), and the class conditional distributions $$p\left(x_{i} \mid y\right)$$ for each dimension. The latter can be parametric (such as a multinomial over the vocabulary, or a Gaussian), or nonparametric (such as $$1D$$ kernel density estimation). Therefore, naive Bayes can be either parametric or nonparametric, although in practice the former is more common.  
        In machine learning we are often interested in a function of the distribution $$T(F)$$, for example, the mean. We call $$T$$ the statistical functional, viewing $$F$$ the distribution itself a function of $$x$$. However, we will also abuse the notation and say $$\theta=T(F)$$ is a "parameter" even for nonparametric models.

***

<!-- ## SECOND
{: #content2} -->

<!-- 1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents26}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents27}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents28} -->