---
layout: NotesPage
title: Statistical Learning Theory
permalink: /work_files/research/dl/theory/stat_lern_thry
prevLink: /work_files/research/dl/theory.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Statistical Learning Theory](#content1)
  {: .TOC1}
  * [The Vapnik-Chervonenkis (VC) Theory](#content2)
  {: .TOC2}
  * [The Bias-Variance Decomposition Theory](#content3)
  {: .TOC3}
  * [Generalization Theory](#content4)
  {: .TOC4}
<!--  * [FIFTH](#content5)
  {: .TOC5}
  * [SIXTH](#content6)
  {: .TOC6} -->
</div>

***
***

* [Principles of Risk Minimization for Learning Theory (original papers)](http://papers.nips.cc/paper/506-principles-of-risk-minimization-for-learning-theory.pdf)  
* [Statistical Learning Theory from scratch (paper)](http://www.tml.cs.uni-tuebingen.de/team/luxburg/publications/StatisticalLearningTheory.pdf)    
* [The learning dynamics behind generalization and overfitting in Deep Networks](https://www.youtube.com/watch?v=pFWiauHOFpY)  
* [Notes on SLT](http://maxim.ece.illinois.edu/teaching/SLT/SLT.pdf)  
* [Mathematics of Learning (w/ proofs & necessary+sufficient conditions for learning)](http://web.mit.edu/9.s915/www/classes/dealing_with_data.pdf)  
* [Generalization Bounds for Hypothesis Spaces](https://courses.cs.washington.edu/courses/cse522/11wi/scribes/lecture4.pdf)  
* [Generalization Bound Derivation](https://mostafa-samir.github.io/ml-theory-pt2/)  
* [Overfitting isn’t simple: Overfitting Re-explained with Priors, Biases, and No Free Lunch](http://mlexplained.com/2018/04/24/overfitting-isnt-simple-overfitting-re-explained-with-priors-biases-and-no-free-lunch/)  
* [9.520/6.860: Statistical Learning Theory and Applications, Fall 2017](http://www.mit.edu/~9.520/fall17/)  
* [What is a Hypothesis in Machine Learning? (blog)](https://machinelearningmastery.com/what-is-a-hypothesis-in-machine-learning/)  
* [No Free Lunch Theorem and PAC Learning (Lec Notes!)](http://www.cs.cornell.edu/courses/cs6783/2015fa/lec3.pdf)  
* [Regularization and Reproducing Kernel Hilbert Spaces (ESL)](https://web.stanford.edu/~hastie/Papers/ESLII.pdf#page=186)  
* [Feasibility of learning: VC-inequality from Hoeffding (Slides)](https://slideplayer.com/slide/4890272/)  



__Fundamental Theorem of Statistical Learning (binary classification):__{: style="color: red"}  
Let $$\mathcal{H}$$ be a hypothesis class of functions from a domain $$X$$ to $$\{0,1\}$$ and let the loss function be the $$0-1$$ loss.  
The following are equivalent:  
$$\begin{array}{l}{\text { 1. } \mathcal{H} \text { has uniform convergence. }} \\ {\text { 2. The ERM is a PAC learning algorithm for } \mathcal{H} \text { . }} \\ {\text { 3. } \mathcal{H} \text { is } PAC \text { learnable. }} \\ {\text { 4. } \mathcal{H} \text { has finite } VC \text { dimension. }}\end{array}$$  
This can be extended to __regression__ and __multiclass classification__.   

<button>Proof.</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
<div hidden="" markdown="1">
* 1 $$\Rightarrow 2$$ We have seen uniform convergence implies that $$\mathrm{ERM}$$ is $$\mathrm{PAC}$$ learnable
* 2 $$\Rightarrow 3$$ Obvious.
* 3 $$\Rightarrow 4$$ We just proved that PAC learnability implies finite $$\mathrm{VC}$$ dimension.
* 4 $$\Rightarrow 1$$ We proved that finite $$\mathrm{VC}$$ dimension implies uniform convergence.
</div>

__Notes:__{: style="color: red"}  
{: #lst-p}
* VC dimension fully determines <span>learnability</span>{: style="color: goldenrod"} for binary classification.  
* The VC dimension doesn’t just determine __learnability__, it also gives a <span>bound on the sample complexity</span>{: style="color: goldenrod"} (which can be shown to be __tight__{: style="color: goldenrod"}).  
* [Lecture Slides (ref)](https://www.cs.toronto.edu/~jlucas/teaching/csc411/lectures/lec23_24_handout.pdf)  
* <button>Extra Notes (what you should know)</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/9bYxbit2n1mvyrttH3CzgI-2CgdrrDNVkejd1fP5-AU.original.fullsize.png){: width="100%" hidden=""}  



__Theoretical Concepts:__{: style="color: red"}  
{: #lst-p}
* __Kolmogorov Complexity__:  
    In __Algorithmic Information Theory__, the __Kolmogorov Complexity__ of an object, such as a piece of text, is the <span>__length__ of the *__shortest__* __computer program__</span>{: style="color: purple"} (in a predetermined programming language) that <span>_produces_ the object as __output__</span>{: style="color: purple"}.  
    It is a measure of the __computational resources__ needed to *__specify__* the object.  
    It is also known as __algorithmic complexity__, __Solomonoff–Kolmogorov complexity__, __program-size complexity__, __descriptive complexity__, or __algorithmic entropy__.  
* __Rademacher Complexity__:  
* __Generalization Bounds__: 
* __Sample Complexity__: 
* __PAC-Bayes Bound__:  
* __Kolmogorov Randomness__:  
* __Minimum Description Length (MDL)__:   
    The [__minimum description length (MDL) principle__](https://en.wikipedia.org/wiki/Minimum_description_length) is a formalization of __Occam's razor__ in which the best hypothesis (a model and its parameters) for a given set of data is the one that leads to the <span>best compression of the data</span>{: style="color: purple"}.  
* __Minimum Message Length (MML)__:  
    [__MML__](https://en.wikipedia.org/wiki/Minimum_message_length) is a formal Information Theory restatement of __Occam's Razor__: even when models are equal in goodness of fit accuracy to the observed data, the one generating the <span>shortest overall message</span>{: style="color: purple"} is more likely to be correct (where the message consists of a statement of the model, followed by a statement of data encoded concisely using that model).  
* [Statistical Decision Theory (ESL!)](https://web.stanford.edu/~hastie/Papers/ESLII.pdf#page=37)  
* __PAC Learnability__:  
    A hypothesis class $$\mathcal{H}$$ is PAC learnable, if there exists a learning algorithm A, satisfying that for any $$\epsilon>0$$ and $$\delta \in(0,1)$$ there exist $$\mathfrak{M}(\epsilon, \delta)=$$ poly $$\left(\frac{1}{\epsilon}, \frac{1}{\delta}\right)$$ such that for i.i.d samples $$S^{m}=\left\{\left(x_{i}, y_{i}\right)\right\}_ {i=1}^{m}$$ drawn from any distribution $$\mathcal{D}$$ and $$m \geq \mathfrak{M}(\epsilon, \delta)$$ the algorithm returns a hypothesis $$A\left(S^{m}\right) \in \mathcal{H}$$ satisfying  
    <p>$$P_{S^{m} \sim \mathcal{D}^{m}}\left(L_{\mathcal{D}}(A(S))>\min _{h \in \mathcal{H}} L_{\mathcal{D}}(h)+\epsilon\right)<\delta$$</p>  
    To show that empirical risk minimization (ERM) is a PAC learning algorithm, we need to show that $$L_{S}(h) \approx L_{\mathcal{D}}(h)$$ for all $$h$$.  
* __Uniform Convergence__:  
    A hypothesis class $$\mathcal{H}$$ has the uniform convergence property, if for any $$\epsilon>0$$ and $$\delta \in(0,1)$$ there exist $$\mathfrak{M}(\epsilon, \delta)=$$ $$\text{poly}\left(\frac{1}{\epsilon}, \frac{1}{\delta}\right)$$ such that for any distribution $$\mathcal{D}$$ and $$m \geq \mathfrak{M}(\epsilon, \delta)$$ i.i.d samples $$S^{m}=\left\{\left(x_{i}, y_{i}\right)\right\}_ {i=1}^{m} \sim \mathcal{D}^{m}$$ with probability at least $$1-\delta$$, $$\left\vert L_{S}^{m}(h)-L_{\mathcal{D}}(h)\right\vert <\epsilon$$ for all $$h \in \mathcal{H}$$.  

    * For a single $$h,$$ law of large numbers says $$L_{S}^{m}(h) \stackrel{m \rightarrow \infty}{\rightarrow} L_{\mathcal{D}}(h)$$  
    * For loss bounded by 1 the Hoeffding inequality states:  
        <p>$$P\left(\left\vert L_{S}^{m}(h)-L_{\mathcal{D}}(h)\right\vert >\epsilon\right) \leq 2 e^{-2 \epsilon^{2} m}$$</p>  
    * The difficulty is to bound all the $$h \in \mathcal{H}$$ <span>uniformly</span>{: style="color: purple"}.  
* __Complexity in ML__:  
    * __Definitions of the complexity of an object ($$h$$)__:  
        * __Minimum Description Length (MDL)__: the number of bits for specifying an object.  
        * __Order of a Polynomial__  
    * __Definitions of the complexity of a class of objects ($$\mathcal{H}$$)__:  
        * __Entropy__  
        * __VC-dim__  



## Statistical Learning Theory
{: #content1}

1. **Statistical Learning Theory:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    __Statistical Learning Theory__ is a framework for machine learning drawing from the fields of statistics and functional analysis. Under certain assumptions, this framework allows us to study the question:  
    > __How can we affect performance on the test set when we can only observe the training set?__{: style="color: blue"}  

    It is a _statistical_ approach to __Computational Learning Theory__.  
    <br>

2. **Formal Definition:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    Let:  
    * $$X$$: $$\:$$ the vector space of all possible __inputs__  
    * $$Y$$: $$\:$$ the vector space of all possible __outputs__  
    * $$Z = X \times Y$$: $$\:$$ the __product space__ of (input,output) pairs  
    * $$n$$: $$\:$$ the number of __samples__ in the __training set__  
    * $$S=\left\{\left(\vec{x}_{1}, y_{1}\right), \ldots,\left(\vec{x}_{n}, y_{n}\right)\right\}=\left\{\vec{z}_{1}, \ldots, \vec{z}_{n}\right\}$$: $$\:$$ the __training set__  
    * $$\mathcal{H} = f : X \rightarrow Y$$: $$\:$$ the __hypothesis space__ of all functions  
    * $$V(f(\vec{x}), y)$$: $$\:$$ an __error/loss function__  

    __Assumptions:__  
    {: #lst-p}
    * The training and test data are generated by an *__unknown, joint__* __probability distribution over datasets__ (over the product space $$Z$$, denoted: $$p_{\text{data}}(z)=p(\vec{x}, y)$$) called the __data-generating process__.  
        * $$p_{\text{data}}$$ is a __joint distribution__ so that it allows us to model _uncertainty in predictions_ (e.g. from noise in data) because $$y$$ is not a deterministic function of $$\vec{x}$$, but rather a _random variable_ with __conditional distribution__ $$p(y \vert \vec{x})$$ for a fixed $$\vec{x}$$.  
    * The __i.i.d. assumptions:__  
        * The examples in each dataset are __independent__ from each other  
        * The _training set_ and _test set_ are __identically distributed__ (drawn from the same probability distribution as each other)  

        > A collection of random variables is __independent and identically distributed__ if each random variable has the same probability distribution as the others and all are mutually independent.  

        > _Informally,_ it says that all the variables provide the same kind of information independently of each other.  
        > * [Discussion on the importance if i.i.d assumptions](https://stats.stackexchange.com/questions/213464/on-the-importance-of-the-i-i-d-assumption-in-statistical-learning/214220)  

        <button>Summary for Motivating i.i.d Assumptions</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
        <div hidden="" markdown="1">
        When learning a model of $$y$$  given $$X$$, independence plays a role as:  
        {: #lst-p}
        * A useful working modelling assumption that allows us to derive learning methods
        * A sufficient but not necessary assumption for proving consistency and providing error bounds
        * A sufficient but not necessary assumption for using random data splitting techniques such as bagging for learning and cross-validation for assessment.  

        To understand precisely what alternatives to i.i.d. that are also sufficient is non-trivial and to some extent a research subject.  
        </div>


    __The Inference Problem__{: style="color: red"}    
    Finding a function $$f : X \rightarrow Y$$ such that $$f(\vec{x}) \sim y$$.  

    __The Expected Risk:__  
    <p>$$I[f]=\mathbf{E}[V(f(\vec{x}), y)]=\int_{X \times Y} V(f(\vec{x}), y) p(\vec{x}, y) d \vec{x} d y$$</p>  

    __The Target Function:__  
    is the best possible function $$f$$ that can be chosen, is given by:  
    <p>$$f=\inf_{h \in \mathcal{H}} I[h]$$</p>  

    __The Empirical Risk:__  
    Is a *__proxy measure__* for the __expected risk__, based on the training set.  
    It is necessary because the probability distribution $$p(\vec{x}, y)$$ is _unknown_.  
    <p>$$I_{S}[f]=\frac{1}{n} \sum_{i=1}^{n} V\left(f\left(\vec{x}_{i}\right), y_{i}\right)$$</p>  
    <br>

3. **Empirical risk minimization:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    __Empirical Risk Minimization (ERM)__ is a principle in _statistical learning theory_ that is based on approximating the __Generalization Error (True Risk)__ by measuring the __Training Error (Empirical Risk)__, i.e. the performance on training data.  

    A _learning algorithm_ that chooses the function $$f_{S}$$ that minimizes the _empirical risk_ is called __empirical risk minimization__:  
    <p>$$R_{\mathrm{emp}}(h) = I_{S}[f]=\frac{1}{n} \sum_{i=1}^{n} V\left(f\left(\vec{x}_{i}\right), y_{i}\right)$$</p>    
    <p>$$f_{S} = \hat{h} = \arg \min _{h \in \mathcal{H}} R_{\mathrm{emp}}(h)$$</p>  

    __Complexity:__{: style="color: red"}  
    <button>Show</button>{: .showText value="show"
     onclick="showText_withParent_PopHide(event);"}
    * Empirical risk minimization for a classification problem with a _0-1 loss function_ is known to be an __NP-hard__ problem even for such a relatively simple class of functions as linear classifiers.  
        * [Paper Proof](https://arxiv.org/abs/1012.0729)  
    * Though, it can be solved efficiently when the minimal empirical risk is zero, i.e. data is linearly separable.  
    * __Coping with Hardness:__  
        * Employing a __convex approximation__ to the 0-1 loss: _Hinge Loss_, _SVM_  
        * Imposing __Assumptions on the data-generating distribution__ and thus, stop being an __agnostic learning algorithm__.  
    {: hidden=""}  
    <br>

4. **Definitions:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    * __Generalization Error:__{: style="color: red"}  
        AKA: __Expected Risk/Error__, __Out-of-Sample Error__[^2], __$$E_{\text{out}}$$__   
        It is a measure of how accurately an algorithm is able to predict outcome values for previously unseen data.  
    * __Generalization Gap:__{: style="color: red"}  
        It is a measure of how accurately an algorithm is able to predict outcome values for previously unseen data.  

        __Formally:__  
        The generalization gap is the __difference between the expected and empirical error__:  
        <p>$$G =I\left[f_{n}\right]-I_{S}\left[f_{n}\right]$$</p>  

        An Algorithm is said to __Generalize__ (achieve __Generalization__) if:  
        <p>$$\lim _{n \rightarrow \infty} G_n = \lim _{n \rightarrow \infty} I\left[f_{n}\right]-I_{S}\left[f_{n}\right]=0$$</p>  
        Equivalently:  
        <p>$$E_{\text { out }}(g) \approx E_{\text { in }}(g)$$</p>  
        or 
        <p>$$I\left[f_{n}\right] \approx I_{S}\left[f_{n}\right]$$</p>  

        __Computing the Generalization Gap:__  
        Since $$I\left[f_{n}\right]$$ cannot be computed for an unknown distribution, the generalization gap __cannot be computed__ either.  
        Instead the goal of __statistical learning theory__ is to _bound_ or _characterize_ the generalization gap in probability:  
        <p>$$P_{G}=P\left(I\left[f_{n}\right]-I_{S}\left[f_{n}\right] \leq \epsilon\right) \geq 1-\delta_{n} \:\:\:\:\:\: (\alpha)$$</p>  
        That is, the goal is to characterize the probability $${\displaystyle 1-\delta _{n}}$$ that the generalization gap is less than some error bound $${\displaystyle \epsilon }$$ (known as the __learning rate__ and generally dependent on $${\displaystyle \delta }$$ and $${\displaystyle n}$$).  

        | Note: $$\alpha \implies \delta_n = 2e^{-2\epsilon^2n}$$
    * __The Empirical Distribution:__{: style="color: red"}  
        _AKA **Data-Generating Distribution**_  
        is the __discrete__ uniform distribution over the _sample points_.   
    * __The Approximation-Generalization Tradeoff:__{: style="color: red"}  
        * __Goal__:  
            Small $$E_{\text{out}}$$: Good approximation of $$f$$ *__out of sample__* (not in-sample).  
        * The tradeoff is characterized by the __complexity__ of the __hypothesis space $$\mathcal{H}$$__:  
            * __More Complex $$\mathcal{H}$$__: Better chance of approximating $$f$$  
            * __Less Complex $$\mathcal{H}$$__: Better chance of generalizing out-of-sample  
        * [**Abu-Mostafa**](https://www.youtube.com/embed/zrEyxfl2-a8?start=358){: value="show" onclick="iframePopA(event)"}
        <a href="https://www.youtube.com/embed/zrEyxfl2-a8?start=358"></a>
            <div markdown="1"> </div>    
        * [Lecture-Slides on Approximation-Generalization](https://mdav.ece.gatech.edu/ece-6254-spring2017/notes/13-bias-variance-marked.pdf)  
    * __Excess Risk (Generalization-Gap) Decomposition \| Estimation-Approximation Tradeoff:__{: style="color: red"}  
        __Excess Risk__ is defined as the difference between the expected-risk/generalization-error of any function $$\hat{f} = g^{\mathcal{D}}$$ that we learn from the data (exactly just bias-variance), and the expected-risk of the __target function__ $$f$$ (known as the __bayes optimal predictor__)
        * [**Excess Risk Decomposition Video**](https://www.youtube.com/embed/YA_CE9jat4I){: value="show" onclick="iframePopA(event)"}
        <a href="https://www.youtube.com/embed/YA_CE9jat4I"></a>
            <div markdown="1"> </div>    
        * [Excess Risk & Bias-Variance Lecture Slides](https://www.ics.uci.edu/~smyth/courses/cs274/readings/xing_singh_CMU_bias_variance.pdf)  
    <br>

8. **Notes:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18}  
    * __Choices of Loss Functions__:  
        * __Regression__:  
            * __MSE__: $$\: V(f(\vec{x}), y)=(y-f(\vec{x}))^{2}$$ 
            * __MAE__: $$\: V(f(\vec{x}), y)=\vert{y-f(\vec{x})}\vert$$  
        * __Classification__:  
            * __Binary__: $$\: V(f(\vec{x}), y)=\theta(-y f(\vec{x}))$$  
                where $$\theta$$ is the _Heaviside Step Function_.  
    * __Training Data, Errors, and Risk__:  
        * __Training-Error__ is the __Empirical Risk__  
            * It is a __proxy__ for the __Generalization Error/Expected Risk__  
            * This is what we minimize
        * __Test-Error__ is an *__approximation__* to the __Generalization Error/Expected Risk__ 
            * This is what we (can) compute to ensure that minimizing Training-Err/Empirical-Risk (ERM) also minimized the Generalization-Err/Expected-Risk (which we can't compute directly)  
    * __Why the goal is NOT to minimize $$E_{\text{in}}$$ completely (intuition)__:  
        Basically, if you have noise in the data; then fitting the (finite) training-data completely; i.e. minimizing the in-sample-err completely will underestimate the out-of-sample-err.  
        Since, if noise existed AND you fit training-data completely $$E_{\text{in}} = 0$$ THEN you inherently have fitted the noise AND your performance on out-sample will be lower.   


***

## The Vapnik-Chervonenkis (VC) Theory
{: #content2}
<!-- 
1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents26}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents27}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents28} -->

***

## The Bias-Variance Decomposition Theory
{: #content3}

* [Bias and Variance Latest Research: A Modern Take on the Bias-Variance Tradeoff in Neural Networks](https://arxiv.org/abs/1810.08591)  
* [Ditto: On the Bias-Variance Tradeoff: Textbooks Need an Update](https://arxiv.org/abs/1912.08286)  

11. **The Bias-Variance Decomposition Theory:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents311}    
    __The Bias-Variance Decomposition Theory__ is a way to quantify the __Approximation-Generalization Tradeoff__.  

    __Assumptions:__  
    {: #lst-p}
    * The analysis is done over the __entire data-distribution__  
    * The target function $$f$$ is already __known__; and you're trying to answer the question:  
        "How can $$\mathcal{H}$$ approximate $$f$$ over all? not just on your sample."  
    * Applies to __real-valued targets__ (can be extended)  
    * Use __Square Error__ (can be extended)  
    <br>

1. **The Bias-Variance Decomposition:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}    
    The __Bias-Variance Decomposition__ is a way of analyzing a learning algorithm's *__expected out-of-sample error__*[^1] as a _sum of three terms:_  
    * __Bias:__ is an error from erroneous assumptions in the learning algorithm.  
    * __Variance:__ is an error from sensitivity to small fluctuations in the training set.  
    * __Irreducible Error__ (resulting from noise in the problem itself)  

    Equivalently, __Bias__ and __Variance__ measure _two different sources of errors in an estimator:_   
    * __Bias:__ measures the expected deviation from the true value of the function or parameter.  
        > AKA: __Approximation Error__[^3]  (statistics)  How well can $$\mathcal{H}$$ approximate the target function '$$f$$'  
    * __Variance:__ measures the deviation from the expected estimator value that any particular sampling of the data is likely to cause.  
        > AKA: __Estimation (Generalization) Error__ (statistics) How well we can zoom in on a good $$h \in \mathcal{H}$$  


    __Bias-Variance Decomposition Formula:__  
    For any function $$\hat{f} = g^{\mathcal{D}}$$ we select, we can decompose its *__expected (out-of-sample) error__* on an _unseen sample $$x$$_ as:  
    <p>$$\mathbb{E}_{\mathbf{x}}\left[(y-\hat{f}(x))^{2}\right]=(\operatorname{Bias}[\hat{f}(x)])^{2}+\operatorname{Var}[\hat{f}(x)]+\sigma^{2}$$</p>  
    Where:  
    * __Bias__:  
        <p>$$\operatorname{Bias}[\hat{f}(x)]=\mathbb{E}_{\mathbf{x}}[\hat{f}(x)]-f(x)$$</p>  
    * __Variance__:  
        <p>$$\operatorname{Var}[\hat{f}(x)]=\mathbb{E}_{\mathbf{x}}\left[\hat{f}(x)^{2}\right]-\mathbb{E}_{\mathbf{x}}[\hat{f}(x)]^{2}$$</p>  
    and the expectation ranges over different realizations of the training set $$\mathcal{D}$$.  

2. **The Bias-Variance Tradeoff:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}  
    is the property of a set of predictive models whereby, models with a _lower bias_ (in parameter estimation) have a _higher variance_ (of the parameter estimates across samples) and vice-versa.  

    __Effects of Bias:__{: style="color: black"}  
    {: #lst-p}
    * __High Bias__: simple models, lead to *__underfitting__*{: style="color: red"}.  
    * __Low Bias__: complex models, lead to *__overfitting__*{: style="color: red"}.  
    
    __Effects of Variance:__{: style="color: black"}  
    {: #lst-p}
    * __High Variance__: complex models, lead to *__overfitting__*{: style="color: red"}.  
    * __Low Variance__: simple models, lead to *__underfitting__*{: style="color: red"}.  

    * <button>__The Tradeoff:__</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        ![The Tradeoff](https://cdn.mathpix.com/snip/images/Z32r3Oyv4h7fVJP0r73zfDIMSmMTIzJH3RDGgLqozWQ.original.fullsize.png){: width="80%"}  
    * [Bias-Variance Example End2End](https://youtu.be/zrEyxfl2-a8?t=1860)  
    <br>

3. **Derivation:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}  
    <p>$${\displaystyle {\begin{aligned}\mathbb{E}_{\mathcal{D}} {\big [}I[g^{(\mathcal{D})}]{\big ]}&=\mathbb{E}_{\mathcal{D}} {\big [}\mathbb{E}_{x}{\big [}(g^{(\mathcal{D})}-y)^{2}{\big ]}{\big ]}\\
    &=\mathbb{E}_{x} {\big [}\mathbb{E}_{\mathcal{D}}{\big [}(g^{(\mathcal{D})}-y)^{2}{\big ]}{\big ]}\\
    &=\mathbb{E}_{x}{\big [}\mathbb{E}_{\mathcal{D}}{\big [}(g^{(\mathcal{D})}- f -\varepsilon)^{2}{\big ]}{\big ]}
    \\&=\mathbb{E}_{x}{\big [}\mathbb{E}_{\mathcal{D}} {\big [}(f+\varepsilon -g^{(\mathcal{D})}+\bar{g}-\bar{g})^{2}{\big ]}{\big ]}\\
    &=\mathbb{E}_{x}{\big [}\mathbb{E}_{\mathcal{D}} {\big [}(\bar{g}-f)^{2}{\big ]}+\mathbb{E}_{\mathcal{D}} [\varepsilon ^{2}]+\mathbb{E}_{\mathcal{D}} {\big [}(g^{(\mathcal{D})} - \bar{g})^{2}{\big ]}+2\: \mathbb{E}_{\mathcal{D}} {\big [}(\bar{g}-f)\varepsilon {\big ]}+2\: \mathbb{E}_{\mathcal{D}} {\big [}\varepsilon (g^{(\mathcal{D})}-\bar{g}){\big ]}+2\: \mathbb{E}_{\mathcal{D}} {\big [}(g^{(\mathcal{D})} - \bar{g})(\bar{g}-f){\big ]}{\big ]}\\
    &=\mathbb{E}_{x}{\big [}(\bar{g}-f)^{2}+\mathbb{E}_{\mathcal{D}} [\varepsilon ^{2}]+\mathbb{E}_{\mathcal{D}} {\big [}(g^{(\mathcal{D})} - \bar{g})^{2}{\big ]}+2(\bar{g}-f)\mathbb{E}_{\mathcal{D}} [\varepsilon ]\: +2\: \mathbb{E}_{\mathcal{D}} [\varepsilon ]\: \mathbb{E}_{\mathcal{D}} {\big [}g^{(\mathcal{D})}-\bar{g}{\big ]}+2\: \mathbb{E}_{\mathcal{D}} {\big [}g^{(\mathcal{D})}-\bar{g}{\big ]}(\bar{g}-f){\big ]}\\
    &=\mathbb{E}_{x}{\big [}(\bar{g}-f)^{2}+\mathbb{E}_{\mathcal{D}} [\varepsilon ^{2}]+\mathbb{E}_{\mathcal{D}} {\big [}(g^{(\mathcal{D})} - \bar{g})^{2}{\big ]}{\big ]}\\
    &=\mathbb{E}_{x}{\big [}(\bar{g}-f)^{2}+\operatorname {Var} [y]+\operatorname {Var} {\big [}g^{(\mathcal{D})}{\big ]}{\big ]}\\
    &=\mathbb{E}_{x}{\big [}\operatorname {Bias} [g^{(\mathcal{D})}]^{2}+\operatorname {Var} [y]+\operatorname {Var} {\big [}g^{(\mathcal{D})}{\big ]}{\big ]}\\
    &=\mathbb{E}_{x}{\big [}\operatorname {Bias} [g^{(\mathcal{D})}]^{2}+\sigma ^{2}+\operatorname {Var} {\big [}g^{(\mathcal{D})}{\big ]}{\big ]}\\
\end{aligned}}}$$</p>  
    where:  
    $$\overline{g}(\mathbf{x})=\mathbb{E}_{\mathcal{D}}\left[g^{(\mathcal{D})}(\mathbf{x})\right]$$ is the __average hypothesis__ over all realization of $$N$$ data-points $$\mathcal{D}_ i$$, and $${\displaystyle \varepsilon }$$ and $${\displaystyle {\hat {f}}} = g^{(\mathcal{D})}$$ are __independent__.    

    <button>Derivation with Wikipedia Notation</button>{: .showText value="show"
     onclick="showText_withParent_PopHide(event);"}
    <p hidden="">$${\displaystyle {\begin{aligned}\operatorname {E}_ {\mathcal{D}} {\big [}(y-{\hat {f}})^{2}{\big ]}&=\operatorname {E} {\big [}(f+\varepsilon -{\hat {f}})^{2}{\big ]}\\&=\operatorname {E} {\big [}(f+\varepsilon -{\hat {f}}+\operatorname {E} [{\hat {f}}]-\operatorname {E} [{\hat {f}}])^{2}{\big ]}\\&=\operatorname {E} {\big [}(f-\operatorname {E} [{\hat {f}}])^{2}{\big ]}+\operatorname {E} [\varepsilon ^{2}]+\operatorname {E} {\big [}(\operatorname {E} [{\hat {f}}]-{\hat {f}})^{2}{\big ]}+2\operatorname {E} {\big [}(f-\operatorname {E} [{\hat {f}}])\varepsilon {\big ]}+2\operatorname {E} {\big [}\varepsilon (\operatorname {E} [{\hat {f}}]-{\hat {f}}){\big ]}+2\operatorname {E} {\big [}(\operatorname {E} [{\hat {f}}]-{\hat {f}})(f-\operatorname {E} [{\hat {f}}]){\big ]}\\&=(f-\operatorname {E} [{\hat {f}}])^{2}+\operatorname {E} [\varepsilon ^{2}]+\operatorname {E} {\big [}(\operatorname {E} [{\hat {f}}]-{\hat {f}})^{2}{\big ]}+2(f-\operatorname {E} [{\hat {f}}])\operatorname {E} [\varepsilon ]+2\operatorname {E} [\varepsilon ]\operatorname {E} {\big [}\operatorname {E} [{\hat {f}}]-{\hat {f}}{\big ]}+2\operatorname {E} {\big [}\operatorname {E} [{\hat {f}}]-{\hat {f}}{\big ]}(f-\operatorname {E} [{\hat {f}}])\\&=(f-\operatorname {E} [{\hat {f}}])^{2}+\operatorname {E} [\varepsilon ^{2}]+\operatorname {E} {\big [}(\operatorname {E} [{\hat {f}}]-{\hat {f}})^{2}{\big ]}\\&=(f-\operatorname {E} [{\hat {f}}])^{2}+\operatorname {Var} [y]+\operatorname {Var} {\big [}{\hat {f}}{\big ]}\\&=\operatorname {Bias} [{\hat {f}}]^{2}+\operatorname {Var} [y]+\operatorname {Var} {\big [}{\hat {f}}{\big ]}\\&=\operatorname {Bias} [{\hat {f}}]^{2}+\sigma ^{2}+\operatorname {Var} {\big [}{\hat {f}}{\big ]}\\\end{aligned}}}$$</p>


4. **Results and Takeaways of the Decomposition:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents34}  
    Match the __"Model Complexity"__ to the *__Data Resources__*, NOT to the _Target Complexity_.  
    ![img](/main_files/dl/theory/stat_lern_thry/1.png){: width="80%"}  
    ![img](https://cdn.mathpix.com/snip/images/6obGTZZntd7tBrbKS6Kdw6TElQHxeSsgKerCNm-G_OI.original.fullsize.png){: width="80%""}  
    ![img](https://cdn.mathpix.com/snip/images/bgXvOhxcfLQ2kWBkuIWRFoGT8gAFhjTKfbYqwiLmPLA.original.fullsize.png){: width="80%""}  
    ![img](https://cdn.mathpix.com/snip/images/lkARUPobs-Pf3UMgURmEFZnawKzhtHgpEaXTVafJFds.original.fullsize.png){: width="85%""}  

    <button>Analogy to the Approximation-Generalization Tradeoff</button>{: .showText value="show"
    onclick="showText_withParent_PopHide(event);"}
    <p hidden="">Pretty much like I'm sitting in my office, and I want a document of some kind, an old letter. Someone has asked me for a letter of recommendation, and I don't want to rewrite it from scratch. So I want to take the older letter, and just see what I wrote, and then add the update to that.  <br>
    Before everything was archived in the computers, it used to be a piece of paper. So I know the letter of recommendation is somewhere. Now I face the question, should I write the letter of recommendation from scratch? Or should I look for the letter of recommendation? The recommendation is there. It's much easier when I find it. However, finding it is a big deal. So the question is not that the target function is there. The question is, can I find it?<br>  
    (Therefore, when I give you 100 examples, you choose the hypothesis set to match the 100 examples. If the 100 examples are terribly noisy, that's even worse. Because their information to guide you is worse.)  <br>
    <strong style="color: red">The data resources you have is, "what do you have in order to navigate the hypothesis set?". Let's pick a hypothesis set that we can afford to navigate. That is the game in learning. Done with the bias and variance.</strong></p>

    * Learning and Approximating are __NOT__ the same thing (refer to the end2end example above)  
        * When Approximating, you can match the complexity of your model to the complexity of the *__"known"__* target function: a __linear__ model is better at approximating a sine wave  
        * When Learning, you should only use a model as complex as the amount of data you have to settle on a good approximation of the *__"Unknown"__* target function: a __constant__ model is better at learning an approximation of a sine wave from 2 sample data points  


5. **Measuring the Bias and Variance:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents35}  
    * __Training Error__: reflects Bias, NOT variance
    * __Test Error__: reflects Both


6. **Reducing the Bias and Variance, and Irreducible Err:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents36}  
    * __Adding Good Feature__:  
        * Decrease Bias  
    * __Adding Bad Feature__:  
        * Doesn't affect (increase) Bias much  
    * __Adding ANY Feature__:  
        * Increases Variance  
    * __Adding more Data__:  
        * Decreases Variance
        * (May) Decreases Bias: if $$h$$ can fit $$f$$ exactly.  
    * __Noise in Test Set__:  
        * Affects ONLY Irreducible Err
    * __Noise in Training Set__:  
        * Affects BOTH and ONLY Bias and Variance  
    * __Dimensionality Reduction__:  
        * Decrease Variance (by simplifying models)  
    * __Feature Selection__:  
        * Decrease Variance (by simplifying models)  
    * __Regularization__:  
        * Increase Bias
        * Decrease Variance
    * __Increasing # of Hidden Units in ANNs__:  
        * Decrease Bias
        * Increase Variance  
    * __Increasing # of Hidden Layers in ANNs__:  
        * Decrease Bias  
        * Increase Variance  
    * __Increasing $$k$$ in K-NN__:  
        * Increase Bias
        * Decrease Variance  
    * __Increasing Depth in Decision-Trees__:  
        * Increase Variance  
    * __Boosting__:  
        * Decreases Bias  
    * __Bagging__:  
        * Reduces Variance              

    * We __Cannot Reduce__ the __Irreducible Err__  
    <br>    
            
77. **Bias-Variance Decomposition Analysis vs. VC-Analysis:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents38}  
    ![VC vs. Bias-Variance](https://cdn.mathpix.com/snip/images/mBGCV2Vs9VP6gYfSpPSF2Pg594cyXl3xLOp4A7BpdWc.original.fullsize.png)   
    * [Caltech Comparison on Learning Curves](https://youtu.be/zrEyxfl2-a8?t=3020)  
    * [Example on Linear Regression (Caltech)](https://youtu.be/zrEyxfl2-a8?t=3271)  


7. **Application of the Decomposition to Classification:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents37}  
    A similar decomposition exists for:  
    * Classification w/ $$0-1$$ loss  
    * Probabilistic Classification w/ Squared Error  

8. **Bias-Variance Decomposition and Risk (Excess Risk Decomposition):**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents38}  
    The __Bias-Variance Decomposition__ analyzes the behavior of the *__Expected Risk/Generalization Error__* for any function $$\hat{f}$$:  
    <p>$$R(\hat{f}) = \mathbb{E}\left[(y-\hat{f}(x))^{2}\right]=(\operatorname{Bias}[\hat{f}(x)])^{2}+\operatorname{Var}[\hat{f}(x)]+\sigma^{2}$$</p>  
    Assuming that $$y = f(x) + \epsilon$$.  

    The __Bayes Optimal Predictor__ is $$f(x) = \mathbb{E}[Y\vert X=x]$$.  

    The __Excess Risk__ is:  
    <p>$$\text{ExcessRisk}(\hat{f}) = R(\hat{f}) - R(f)$$</p>  

    __Excess Risk Decomposition:__{: style="color: red"}  
    We add and subtract the __target function $$f_{\text{target}}=\inf_{h \in \mathcal{H}} I[h]$$__ that minimizes the __(true) expected risk__:  
    <p>$$\text{ExcessRisk}(\hat{f}) = \underbrace{\left(R(\hat{f}) - R(f_{\text{target}})\right)}_ {\text { estimation error }} + \underbrace{\left(R(f_{\text{target}}) - R(f)\right)}_ {\text { approximation error }}$$</p>  



    The __Bias-Variance Decomposition__ for *__Excess Risk:__*  
    * Re-Writing __Excess Risk__:  
        <p>$$\text{ExcessRisk}(\hat{f}) = R(\hat{f}) - R(f) = \mathbb{E}\left[(y-\hat{f}(x))^{2}\right] - \mathbb{E}\left[(y-f(x))^{2}\right]$$</p>  
        which is equal to:  
        <p>$$R(\hat{f}) - R(f) = \mathbb{E}\left[(f(x)-\hat{f}(x))^{2}\right]$$</p>  
    <p>$$\mathbb{E}\left[(f(x)-\hat{f}(x))^{2}\right] = (\operatorname{Bias}[\hat{f}(x)])^{2}+\operatorname{Var}[\hat{f}(x)]$$</p>  

    * if you dont want to mess with stat-jargon; lemme rephrase:  
        is the minimizer $${\displaystyle f=\inf_{h \in \mathcal{H}} I[h]}$$ where $$I[h]$$ is the expected-risk/generalization-error (assume MSE);  
        is it $$\overline{f}(\mathbf{x})=\mathbb{E}_ {\mathcal{D}}\left[f^{(\mathcal{D})}(\mathbf{x})\right]$$ the average hypothesis over all realizations of $$N$$ data-points $$\mathcal{D}_ i$$??  


***

## Generalization Theory
{: #content4}

* [Generalization Bounds: PAC-Bayes, Rademacher, ERM, etc. (Notes!)](https://www.cs.princeton.edu/courses/archive/fall17/cos597A/lecnotes/generalize.pdf)  
* [Deep Learning Generalization (blog!)](http://www.offconvex.org/2017/12/08/generalization1/)  

1. **Generalization Theory:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents41}  
    

    __Approaches to (Notions of) Quantitative Description of Generalization Theory:__{: style="color: red"}  
    {: #lst-p}
    * VC Dimension
    * Rademacher Complexity
    * PAC-Bayes Bound  



    __Prescriptive vs Descriptive Theory:__{: style="color: red"}  
    {: #lst-p}
    * __Prescriptive__: only attaches a label to the problem, without giving any insight into how to solve the problem.  
    * __Descriptive__: describes the problem in detail (e.g. by providing cause) and allows you to solve the problem.  

    Generalization Theory Notions consist of attaching a descriptive label to the basic phenomenon of lack of generalization. They are hard to compute for today’s complicated ML models, let alone to use as a guide in designing learning systems.  
    __Generalization Bounds as Descriptive Labels:__{: style="color: red"}  
    {: #lst-p}
    * __Rademacher Complexity__:  
        <button>Assumptions</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        * labels and loss are 0,1,  
        * the badly generalizing $$h$$ predicts perfectly on the training sample $$S$$ and  
            is completely wrong on the heldout set $$S_2$$, meaning:  
            <p>$$\Delta_{S}(h)-\Delta_{S_{2}}(h) \approx-1$$</p>  
        {: hidden=""}
    <br>
        
    <!-- 2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents42}
        3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents43} -->

4. **Overfitting:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents44}  
    One way to summarize __Overfitting__ is:  
    <span>discovering patterns in data that do not exist in the intended application</span>{: style="color: purple"}.  
    The typical case of overfitting "<span>decreasing loss only on the training set and increasing the loss on the validation set</span>{: style="color: purple"}" is only one example of this.  

    The question then is how we prevent overfitting from occurring.  
    The problem is that <span>we cannot know apriori what patterns will generalize from the dataset</span>{: style="color: purple"}.  


    __No-Free-Lunch (NFL) Theorem:__{: style="color: red"}  
    {: #lst-p}
    * __NFL Theorems for Supervised Machine Learning:__  
        * In his 1996 paper The Lack of A Priori Distinctions Between Learning Algorithms, David Wolpert examines if it is possible to get useful theoretical results with a training data set and a learning algorithm without making any assumptions about the target variable.  
        * _Wolpert_ proves that given a noise-free data set (i.e. no random variation, only trend) and a machine learning algorithm where the cost function is the error rate, all machine learning algorithms are equivalent when assessed with a generalization error rate (the model’s error rate on a validation data set).  
        * Extending this logic he demonstrates that for any two algorithms, A and B, there are as many scenarios where A will perform worse than B as there are where A will outperform B. This even holds true when one of the given algorithms is random guessing.  
        * This is because nearly all (non-rote) machine learning algorithms make some assumptions (known as inductive or learning bias) about the relationships between the predictor and target variables, introducing bias into the model.  
            The assumptions made by machine learning algorithms mean that some algorithms will fit certain data sets better than others. It also (by definition) means that there will be as many data sets that a given algorithm will not be able to model effectively.  
            How effective a model will be is directly dependent on how well the assumptions made by the model fit the true nature of the data.  
        * Implication: you can’t get good machine learning “for free”.  
            You must use knowledge about your data and the context of the world we live in (or the world your data lives in) to select an appropriate machine learning model.  
            There is no such thing as a single, universally-best machine learning algorithm, and there are no context or usage-independent (a priori) reasons to favor one algorithm over all others.  
    * __NFL Theorem for Search/Optimization:__  
        * All algorithms that search for an extremum of a cost function perform exactly the same when averaged over all possible cost functions. So, for any search/optimization algorithm, any elevated performance over one class of problems is exactly paid for in performance over another class.  
        * It state that any two optimization algorithms are equivalent when their performance is averaged across all possible problems.    
        * Wolpert and McReady essentially say that <span>you need some prior knowledge that is encoded in your algorithm in order to search well</span>{: style="color: purple"}.  
            They created the theorem to give an easy counter example to researchers that would create a (tweak on an) algorithm and claimed that it would work better on all possible problems. It can’t. There’s a proof. If you have a good algorithm, it must in some way fit on your problem space, and you will have to investigate how.  
    * <button>__Explanation through a thought experiment:__</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
        * Suppose you see someone toss a coin and get heads. What is the probability distribution over the next result of the coin toss?  
            Did you think heads 50% and tails 50%?  
            If so, you’re wrong: the answer is that we don’t know.  
            For all we know, the coin could have heads on both sides. Or, it might even obey some strange laws of physics and come out as tails every second toss.  
            The point is, <span>there is no way we can extract only patterns that will __generalize__</span>{: style="color: purple"}: there will always be some scenarios where those patterns will not exist.  
            This is the essence of what is called the __No Free Lunch Theorem__: <span>any model that you create will always “overfit” and be completely wrong in some scenarios</span>{: style="color: purple"}.  
        {: hidden=""}  
    * __Main Concept:__ Generalizing is extrapolating to new data. To do that you need to make assumptions and for problems where the assumptions don’t hold you will be suboptimal.  
    * __Practical Implications__:  
        * Bias-free learning is futile because a learner that makes no a priori assumptions will have no rational basis for creating estimates when provided new, unseen input data.  
            Models are simplifications of a specific component of reality (observed with data). To simplify reality, a machine learning algorithm or statistical model needs to make assumptions and introduce bias (known specifically as inductive or learning bias).  
            The assumptions of an algorithm will work for some data sets but fail for others.  
        * This shows that we need some restriction on $$\mathcal{H}$$ even for the realizable PAC setting. We cannot learn arbitrary set of hypothesis, there is no free lunch.  
        * There is no universal (one that works for all $$\mathcal{H}$$) learning algorithm.  
            I.e., if the algorithm $$A$$ has no idea about $$\mathcal{H},$$ even the singleton hypothesis class $$\mathcal{H}=\{h\}$$ (as in the statement of the theorem) is not PAC learnable.  
        * Why do we have to fix a hypothesis class when coming up with a learning algorithm? Can we _"just learn"_?  
            The NFL theorem formally shows that the answer is __NO__.  
        * Counter the following claim: "My machine learning algorithm/optimization strategy is the best, always and forever, for all the scenarios".  
        * Always check your assumptions before relying on a model or search algorithm.  
        * There is no “super algorithm” that will work perfectly for all datasets.  
        * Variable length and redundant encodings are not covered by the NFL theorems. Does Genetic Programming get a pass?  
        * NFL theorems are like a statistician sitting with his head in the fridge, and his feet in the oven. On average, his temperature is okay! NFL theorems prove that the arithmetic mean of performance is constant over all problems, it doesn’t prove that for other statistics this is the case. There has been an interesting ‘counter’ proof, where a researcher proved that for a particular problem space, a hill-climber would outperform a hill-descender on 90% of the problem instances, and did that by virtue of being exponentially worse on the remaining 10% of the problems. Its average performance abided by the NFL theorem and the two algorithms were equal when looking at mean performance, yet the hill-climber was better in 90% of the problems, i.e., it had a much better median performance. So is there maybe a free appetizer?  
        * While no one model/algorithm works best for every problem, it may be that one model/algorithm works best for all real-world problems, or all problems that we care about, practically speaking.  
    * [No Free Lunch Theorems Main Site](http://www.no-free-lunch.org/)  
    * [No Free Lunch Theorem (Lec Notes)](http://www.cs.utah.edu/~bhaskara/courses/theoryml/scribes/lecture3.pdf)  
    * [Machine Learning Theory - NFL Theorem (Lec Notes)](http://www.cs.cornell.edu/courses/cs6783/2015fa/lec3.pdf)  
    * [Overfitting isn’t simple: Overfitting Re-explained with Priors, Biases, and No Free Lunch (Blog)](http://mlexplained.com/2018/04/24/overfitting-isnt-simple-overfitting-re-explained-with-priors-biases-and-no-free-lunch/)  
    * [Learning as Refining the Hypothesis Space (Blog-Paper)](https://artint.info/html/ArtInt_191.html)  
    * [All Models Are Wrong (Blog)](https://community.alteryx.com/t5/Data-Science-Blog/All-Models-Are-Wrong/ba-p/348080)  
    * [Does the 'no free lunch' theorem also apply to deep learning? (Quora)](https://www.quora.com/Does-the-no-free-lunch-theorem-also-apply-to-deep-learning)  

    <br>



[^1]: with respect to a particular problem.  
[^2]: Note that Abu-Mostafa defines _out-sample error $$E_{\text{out}}$$_ as the _expected error/risk $$I[f]$$_; thus making $$G = E_{\text{out}} - E_{\text{in}}$$.  
[^3]: can be viewed as a measure of the __average network approximation error__ _over all possible training data sets $$\mathcal{D}$$_   