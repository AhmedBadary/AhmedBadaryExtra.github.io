---
layout: NotesPage
title: Sampling and Monte Carlo Methods
permalink: /work_files/research/dl/concepts/sampling
prevLink: /work_files/research/dl/concepts.html
---


<div markdown="1" class = "TOC">
# Table of Contents

  * [Sampling](#content1)
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

__Resources:__{: style="color: red"}  
{: #lst-p}
* [Importance Sampling (Tut - Ben Lambert)](https://www.youtube.com/watch?v=V8f8ueBc9sY)  
* [Random Walk Metropolis Sampling Algorithm (Tut. B-Lambert)](https://www.youtube.com/watch?v=U561HGMWjcw)  
* [Gibbs Sampling (Tut. B-Lambert)](https://www.youtube.com/watch?v=ER3DDBFzH2g)  
* [Hamiltonian Monte Carlo Intuition (Tut. B-Lambert)](https://www.youtube.com/watch?v=a-wydhEuAm0)  
* [Markov Chains (Stat 110)](https://www.youtube.com/watch?v=8AJPs3gvNlY)  
* [Markov Chain Monte Carlo Methods, Rejection Sampling and the Metropolis-Hastings Algorithm!](http://bjlkeng.github.io/posts/markov-chain-monte-carlo-mcmc-and-the-metropolis-hastings-algorithm/)  
* [MCMC Course Tutorial (Mathematical Monk Vids!)](https://www.youtube.com/watch?v=12eZWG0Z5gY)  
* [An Introduction to MCMC for Machine Learning (M Jordan!)](https://www.cs.ubc.ca/~arnaud/andrieu_defreitas_doucet_jordan_intromontecarlomachinelearning.pdf)  
* [MCMC Intuition for Everyone (blog)](https://towardsdatascience.com/mcmc-intuition-for-everyone-5ae79fff22b1)  



## Sampling
{: #content1}

1. **Monte Carlo Sampling:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    When a sum or an integral cannot be computed exactly we can approximate it using Monte Carlo sampling. 
    The idea is to __view the sum or integral as if it were an *expectation under some distribution*__ and to <span>approximate the expectation by a corresponding average</span>{: style="color: goldenrod"}:   
    \- __Sum:__  
    <p>$$s=\sum_{\boldsymbol{x}} p(\boldsymbol{x}) f(\boldsymbol{x})=E_{p}[f(\mathbf{x})]$$</p>  
    \- __Integral:__  
    <p>$$s=\int p(\boldsymbol{x}) f(\boldsymbol{x}) d \boldsymbol{x}=E_{p}[f(\mathbf{x})]$$</p>  
    We can approximate $$s$$ by drawing $$n$$ samples $$\boldsymbol{x}^{(1)}, \ldots, \boldsymbol{x}^{(n)}$$ from $$p$$ and then forming the __empirical average__:  
    <p>$$\hat{s}_{n}=\frac{1}{n} \sum_{i=1}^{n} f\left(\boldsymbol{x}^{(i)}\right)$$</p><br>

2. **Importance Sampling:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    There is __no unique decomposition__ of the MC approximation because $$p(\boldsymbol{x}) f(\boldsymbol{x})$$ can always be rewritten as:  
    <p>$$p(\boldsymbol{x}) f(\boldsymbol{x})=q(\boldsymbol{x}) \frac{p(\boldsymbol{x}) f(\boldsymbol{x})}{q(\boldsymbol{x})} $$</p>  
    where we now sample from $$q$$ and average $$\frac{p f}{q}$$.  

    Formally, the expectation becomes:  
    <p>$$E_{p}[f(\mathbf{x})] = \sum_{\boldsymbol{x}} p(\boldsymbol{x}) f(\boldsymbol{x}) = \sum_{\boldsymbol{x}} q(\boldsymbol{x}) \dfrac{p(\boldsymbol{x})}{q(\boldsymbol{x})} f(\boldsymbol{x}) = E_q\left[\dfrac{p(\boldsymbol{x})}{q(\boldsymbol{x})} f(\boldsymbol{x})\right]$$</p>  


    __Biased Importance Sampling:__{: style="color: red"}  
    Another approach is to use biased importance sampling, which has the advantage of not requiring normalized $$p$$ or $$q$$. In the case of discrete variables, the biased importance sampling estimator is given by  
    <p>$$\begin{aligned} \hat{s}_{B I S} &=\frac{\sum_{i=1}^{n} \frac{p\left(\boldsymbol{x}^{(i)}\right)}{q\left(\boldsymbol{x}^{(i)}\right)} f\left(\boldsymbol{x}^{(i)}\right)}{\sum_{i=1}^{n} \frac{p\left(\boldsymbol{x}^{(i)}\right)}{q\left(\boldsymbol{x}^{(i)}\right)}} \\ &=\frac{\sum_{i=1}^{n} \frac{p\left(\boldsymbol{x}^{(i)}\right)}{\tilde{q}\left(\boldsymbol{x}^{(i)}\right)} f\left(\boldsymbol{x}^{(i)}\right)}{\sum_{i=1}^{n} \frac{p(i)}{\tilde{q}(i)}} \\ &=\frac{\sum_{i=1}^{n} \frac{\tilde{p}\left(\boldsymbol{x}^{(i)}\right)}{\tilde{q}\left(\boldsymbol{x}^{(i)}\right)} f\left(\boldsymbol{x}^{(i)}\right)}{\sum_{i=1}^{n} \frac{\tilde{p}\left(\boldsymbol{x}^{(i)}\right)}{\tilde{q}\left(\boldsymbol{x}^{(i)}\right)}} \end{aligned}$$</p>  
    where $$\tilde{p}$$ and $$\tilde{q}$$ are the unnormalized forms of $$p$$ and $$q$$, and the $$\boldsymbol{x}^{(i)}$$ are the samples from $$q$$.  
    __Bias:__  
    This estimator is biased because $$\mathbb{E}[\hat{s}_ {BIS}] \neq s$$, except __asymptotically when $$n \rightarrow \infty$$__ and the __denominator of the first equation__ (above) __converges to $$1$$__. Hence this estimator is called *__asymptotically unbiased__*.  


    __Statistical Efficiency:__{: style="color: red"}  
    Although a good choice of $$q$$ can greatly improve the efficiency of Monte Carlo estimation, a poor choice of $$q$$ can make the efficiency much worse.  
    \- If there are <span>samples of $$q$$ for which $$\frac{p(\boldsymbol{x})|f(\boldsymbol{x})|}{q(\boldsymbol{x})}$$ is large, then the variance of the estimator can get very large</span>{: style="color: goldenrod"}.  
    This may happen when $$q(\boldsymbol{x})$$ is tiny while neither $$p(\boldsymbol{x})$$ nor $$f(\boldsymbol{x})$$ are small enough to cancel it.  
    The $$q$$ distribution is usually chosen to be a simple distribution so that it is easy to sample from. When $$\boldsymbol{x}$$ is high dimensional, this simplicity in $$q$$ causes it to match $$p$$ or $$p\vert f\vert $$ poorly.  
    (1) When $$q\left(\boldsymbol{x}^{(i)}\right) \gg p\left(\boldsymbol{x}^{(i)}\right)\left|f\left(\boldsymbol{x}^{(i)}\right)\right|$$, importance sampling collects useless samples (summing tiny numbers or zeros).  
    (2) On the other hand, when $$q\left(\boldsymbol{x}^{(i)}\right) \ll p\left(\boldsymbol{x}^{(i)}\right)\left|f\left(\boldsymbol{x}^{(i)}\right)\right|$$, which will happen more rarely, the ratio can be huge.  
    Because these latter events are rare, they may not show up in a typical sample, yielding typical underestimation of $$s$$, compensated rarely by gross overestimation.  
    Such very large or very small numbers are typical when $$\boldsymbol{x}$$ is high dimensional, because in high dimension the dynamic range of joint probabilities can be very large.  

    <span> A good IS sampling distribution $$q$$ is a *low variance* distribution.</span>{: style="color: goldenrod"}{: .borderexample}  


    __Applications:__{: style="color: red"}  
    In spite of this danger, importance sampling and its variants have been found very useful in many machine learning algorithms, including deep learning algorithms. They have been used to:  
    {: #lst-p}
    * Accelerate training in neural language models with a large vocabulary  
    * Accelerate other neural nets with a large number of outputs  
    * Estimate a partition function (the normalization constant of a probability distribution)
    * Estimate the log-likelihood in deep directed models, e.g. __Variational Autoencoders__  
    * Improve the estimate of the gradient of the cost function used to train model parameters with stochastic gradient descent  
        Particularly for models, such as __classifiers__, in which most of the total value of the cost function comes from a small number of misclassified examples.  
        Sampling more _difficult examples_ more frequently can __reduce the variance of the gradient__ in such cases _(Hinton, 2006)_.  


    __Approximating Distributions:__{: style="color: red"}  
    To approximate the expectation (mean) of a distribution $$p$$:  
    <p>$${\mathbb{E}}_ {p}[x]=\sum_{x} x p(x)$$</p>  
    by sampling from a distribution $$q$$.  
    Notice that:  
    (1) $${\displaystyle {\mathbb{E}}_ {p}[x]=\sum_{x} x p(x) = \sum_{x} x\frac{p(x)}{q(x)} q(x)}$$  
    (2) $${\displaystyle \sum_{x} x\frac{p(x)}{q(x)} q(x)=\mathbb{E}_ {q}\left[x \frac{p(x)}{q(x)}\right]}$$  
    We approximate the expectation over $$q$$ in (2) with the empirical distribution:  
    <p>$$\mathbb{E}_ {q}\left[x \frac{p(x)}{q(x)}\right] \approx \dfrac{1}{n} \sum_{i=1}^n x_i \dfrac{p(x_i)}{q(x_i)}$$</p>  

    __Approximating UnNormalized Distributions - *Biased* Importance Sampling:__{: style="color: red"}  
    Let $$p(x)=\frac{h(x)}{Z}$$, then  
    <p>$$\begin{aligned}\mathbb{E}_{p}[x] &= \sum_{x} x \frac{h(x)}{Z} \\ &= \sum_{x} x \frac{h(x)}{Z q(x)} q(x) \\ &\approx \frac{1}{Z} \frac{1}{n} \sum_{i=1}^{n} x_{i} \frac{h\left(x_{i}\right)}{q\left(x_{i}\right)} \end{aligned}$$</p>  
    where the samples $$x_i$$ are drawn from $$q$$.  
    To get rid of the $$\dfrac{1}{Z}$$ factor,  
    \- First, we define the importance sample __*weight:*__  
    <p>$$w_i = \frac{h\left(x_{i}\right)}{q\left(x_{i}\right)}$$</p>  
    \- then the __sample *mean weight:*__  
    <p>$$\bar{w} = \dfrac{1}{n} \sum_{i=1}^n w_i = $$</p>  
    \- Now, we decompose $$Z$$ by noticing that:  
    <p>$$\mathbb{E}_ {p}[1]=1=\sum_{x} \frac{h(x)}{Z}$$</p>  
    $$\implies$$  
    <p>$$Z = \sum_{x} h(x)$$</p>  
    \- we approximate the expectation again with IS:  
    <p>$$\begin{aligned} Z 
    &= \sum_{x} h(x) \\ &= \sum_{x} \frac{h(x)}{q(x)} q(x) \\ &\approx \dfrac{1}{n} \sum_{i=1}^{n} \frac{h\left(x_{i}\right)}{q\left(x_{i}\right)} \\ &= \bar{w} \end{aligned}$$</p>  
    Thus, the sample normalizing constant $$\hat{Z}$$ is equal to the sample _mean weight_:  
    <p>$$Z = \bar{w}$$</p>  

    Finally, 
    <p>$$\mathbb{E}_ {p}[x] \approx \frac{1}{\bar{w}} \frac{1}{n} \sum_{i=1}^{n} x_{i} w_i  = \dfrac{\overline{xw}}{\bar{w}}$$</p>  


    __Curse of Dimensionality in IS - Variance of the Estimator:__{: style="color: red"}  
    A big problem with Importance Sampling is that the __variance__ of the IS estimator can be greatly _sensitive_ to the choice of $$q$$.  
    The __Variance__ is:  
    <p>$$\operatorname{Var}\left[\hat{s}_ {q}\right]=\operatorname{Var}\left[\frac{p(\mathbf{x}) f(\mathbf{x})}{q(\mathbf{x})}\right] / n$$</p>  
    The __Minimum Variance__ occurs when $$q$$ is:  
    <p>$$q^{* }(\boldsymbol{x})=\frac{p(\boldsymbol{x})|f(\boldsymbol{x})|}{Z}$$</p>  
    where $$Z$$ is the normalization constant, chosen so that $$q^{* }(\boldsymbol{x})$$ sums or integrates to $$1$$ as appropriate.  
    \- Any choice of sampling distribution $$q$$ is __valid__ (in the sense of yielding the correct expected value), and 
    \- $$q^{ * }$$ is the __optimal one__ (in the sense of yielding minimum variance).  
    \- Sampling from $$q^{ * }$$ is usually infeasible, but other choices of $$q$$ can be feasible while still reducing the variance somewhat.<br>  


3. **Markov Chain Monte Carlo (MCMC) Methods:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    __Motivation:__{: style="color: red"}  
    In many cases, we wish to use a Monte Carlo technique but there is no tractable method for drawing exact samples from the distribution $$p_{\text {model}}(\mathbf{x})$$ or from a good (low variance) importance sampling distribution $$q(\mathbf{x})$$.  
    In the context of deep learning, this most often happens when $$p_{\text {model}}(\mathbf{x})$$ is represented by an *__undirected model__*.  
    In these cases, we introduce a mathematical tool called a __Markov chain__ to *__approximately sample__* from $$p_{\text {model}}(\mathbf{x})$$. The family of algorithms that use Markov chains to perform Monte Carlo estimates is called __Markov Chain Monte Carlo (MCMC) methods__.  

    __Idea of MCs:__  
    \- The core idea of a Markov chain is to have a state $$\boldsymbol{x}$$ that begins as an arbitrary value.  
    \- Over time, we randomly update $$\boldsymbol{x}$$ repeatedly.  
    \- Eventually $$\boldsymbol{x}$$ becomes (very nearly) a fair sample from $$p(\boldsymbol{x})$$.  

    __Definition:__  
    Formally, a __Markov chain__ is defined by:  
    * A __random state__ $$x$$ and  
    * A __transition distribution__ $$T\left(x^{\prime} \vert x\right)$$  
        specifying the probability that a random update will go to state $$x^{\prime}$$ if it starts in state $$x$$.<br>  
    Running the Markov chain means repeatedly updating the state $$x$$ to a value $$x^{\prime}$$ sampled from $$T\left(\mathbf{x}^{\prime} \vert x\right)$$.  


    __Finite, Countable States:__  
    We take the case where the random variable $$\mathbf{x}$$ has __countably many states__.  
    __Representation:__  
    We represent the state as just a positive integer $$x$$.  
    Different integer values of $$x$$ map back to different states $$\boldsymbol{x}$$ in the original problem.  

    Consider what happens when we __run *infinitely* many Markov chains in *parallel*__.  
    \- All the states of the different Markov chains are drawn from some distribution $$q^{(t)}(x)$$, where $$t$$ indicates the number of time steps that have elapsed.  
    \- At the beginning, $$q^{(0)}$$ is some distribution that we used to arbitrarily initialize $$x$$ for each Markov chain.  
    \- Later, $$q^{(t)}$$ is influenced by all the Markov chain steps that have run so far.  
    \- Our __goal__ is for <span>$$q^{(t)}(x)$$ to converge to $$p(x)$$</span>{: style="color: purple"}.  

    * __Probability of transitioning to a new state__:  
        Let's update a single Markov chain's state $$x$$ to a new state $$x^{\prime}$$.  
        The __probability of a single state landing in state $$x^{\prime}$$__ is given by:  
        <p>$$q^{(t+1)}\left(x^{\prime}\right)=\sum_{x} q^{(t)}(x) T\left(x^{\prime} \vert x\right)$$</p>  
        * __Describing $$q$$__:  
            Because we have reparametrized the problem in terms of a positive integer $$x$$, we can describe the probability distribution $$q$$ using a vector $$\boldsymbol{v}$$ with:  
            <p>$$q(\mathrm{x}=i)=v_{i}$$</p>  
        * __The Transition Operator $$T$$ as a Matrix__:  
            Using our integer parametrization, we can represent the effect of the transition operator $$T$$ using a matrix $$A$$.  
            We define $$A$$ so that:  
            <p>$$A_{i, j}=T\left(\mathbf{x}^{\prime}=i \vert \mathbf{x}=j\right)$$</p>  

        Rather than writing it in terms of $$q$$ and $$T$$ to understand how a single state is updated, we may now use $$v$$ and $$A$$ to describe how the entire distribution over all the different Markov chains (running in parallel) shifts as we apply an update.  
        Rewriting the __probability of a single state landing in state $$x^{\prime} = i$$__:  
        <p>$$\boldsymbol{v}^{(t)}=\boldsymbol{A} \boldsymbol{v}^{(t-1)}$$</p>  
        * __Matrix Exponentiation:__  
            Applying the Markov chain update repeatedly corresponds to multiplying by the matrix $$A$$ repeatedly.  
            In other words, we can think of the process as exponentiating the matrix $$\boldsymbol{A}$$.  

        Thus, $$\boldsymbol{v}^{(t)}$$ can, finally, be rewritten as  
        <p>$$\boldsymbol{v}^{(t)}=\boldsymbol{A}^{t} \boldsymbol{v}^{(0)}$$</p>  
    * __Convergence - The Stationary Distribution__:  
        Let's first examine the matrix $$A$$.  
        * __Stochastic Matrices__:  
            __Stochastic Matrices__ are ones where each of their columns represents a _probability distribution_.  
            The Matrix $$A$$ is a stochastic matrix.  
            * __Perron-Frobenius Theorem - Largest Eigenvalue__:  
                If there is a nonzero probability of transitioning from any state $$x$$ to any other state $$x$$ for some power $$t$$, then the __Perron-Frobenius theorem__ guarantees that the <span>largest eigenvalue is real and equal to $$1$$</span>{: style="color: goldenrod"}.  
            * __Unique Largest Eigenvalue__:  
                Under some additional mild conditions, $$A$$ is guaranteed to have only one eigenvector with eigenvalue $$1$$.  
        * __Exponentiated Eigenvalues__:  
            Over time, we can see that __all the eigenvalues are exponentiated__:  
            <p>$$\boldsymbol{v}^{(t)}=\left(\boldsymbol{V} \operatorname{diag}(\boldsymbol{\lambda}) \boldsymbol{V}^{-1}\right)^{t} \boldsymbol{v}^{(0)}=\boldsymbol{V} \operatorname{diag}(\boldsymbol{\lambda})^{t} \boldsymbol{V}^{-1} \boldsymbol{v}^{(0)}$$</p>  

            This process causes <span>all the eigenvalues that are not equal to $$1$$ to decay to zero</span>{: style="color: purple"}.  

        The process thus <span>converges to a __stationary distribution__ (__equilibrium distribution__)</span>{: style="color: goldenrod"}.  
        * __Convergence Condition - Eigenvector Equation:__  
            At __convergence__, the following __eigenvector equation__ holds:  
            <p>$$\boldsymbol{v}^{\prime}=\boldsymbol{A} \boldsymbol{v}=\boldsymbol{v}$$</p>  
            and this same condition *__holds for every additional step__*.  
            * __Stationary Point Condition__:  
                Thus, To be a __stationary point__, $$\boldsymbol{v}$$ must be an __eigenvector with corresponding eigenvalue $$1$$__.  
                This condition guarantees that <span>once we have reached the stationary distribution, repeated applications of the transition sampling procedure do not change the _distribution_ over the states of all the various Markov chains</span>{: style="color: purple"} (although the transition operator does change each individual state, of course).  
        * __Convergence to $$p$$__:  
            If we have chosen $$T$$ correctly, then the stationary distribution $$q$$ will be equal to the distribution $$p$$ we wish to sample from.  
            __Gibbs Sampling__ is one way to choose $$T$$.  

    __Continuous Variables:__  

    __Convergence:__  
    In general, a Markov chain with transition operator $T$ will converge, under mild conditions, to a fixed point described by the equation  
    <p>$$q^{\prime}\left(\mathbf{x}^{\prime}\right)=\mathbb{E}_ {\mathbf{x} \sim q} T\left(\mathbf{x}^{\prime} \vert \mathbf{x}\right)$$</p>  
    which is exactly what we had in the __discrete case__ defined as a *__sum__*:  
    <p>$$q^{\prime}\left(x^{\prime}\right)=\sum_{x} q^{(t)}(x) T\left(x^{\prime} \vert x\right)$$</p>  
    and in the __continuous case__ as an *__integral__*:  
    <p>$$q^{\prime}\left(x^{\prime}\right)=\int_{x} q^{\prime}(x) T\left(x^{\prime} \vert x\right)$$</p>  


    __Using the Markov Chain:__{: style="color: red"}  
    <div class="borderexample">Regardless of whether the state is continuous or discrete, all Markov chain methods consist of <span style="color: goldenrod">repeatedly applying stochastic updates until eventually the state begins to yield samples from the equilibrium distribution</span>.</div>  
    \- __Training the Markov Chain:__{: style="color: red"}  
    Running the Markov chain until it reaches its equilibrium distribution is called *__burning in__* the Markov chain.  

    \- __Sampling from the Markov Chain:__{: style="color: red"}  
    After the chain has reached equilibrium, a sequence of infinitely many samples may be drawn from the equilibrium distribution.  
    There are <span>__difficulties/drawbacks__</span>{: style="color: darkred"} with using Markov Chains for sampling:  
    {: #lst-p}
    * __Representative Samples - Independence__:  
        The samples are __identically distributed__, but _any two successive samples_ will be __highly correlated__ with each other.  
        * __Issue__:  
            A _finite sequence_ of samples may thus not be very _representative of the equilibrium distribution_.   
        * __Solutions__:  
            1. One way to mitigate this problem is to __return only every $$n$$ successive samples__, so that our estimate of the statistics of the equilibrium distribution is not as _biased by the correlation_ between an MCMC sample and the next several samples.  
                <span>Markov chains are thus expensive to use because of the time required to _burn in_ to the equilibrium distribution and the time required to transition from one sample to another reasonably decorrelated sample after reaching equilibrium</span>{: style="color: darkred"}.   
            2. To get *__truly independent samples__*, one can __run multiple Markov chains in parallel__.  
            This approach uses extra parallel computation to _eliminate latency_.  

        \- The strategy of using only a single Markov chain to generate all samples and the strategy of using one Markov chain for each desired sample are two extremes.  
        \- In __deeplearning__ we usually <span>_use a number of chains that is similar to the number of examples in a minibatch_ and then draw as many samples as are needed from this fixed set of Markov chains</span>{: style="color: goldenrod"}.  
        > A commonly used number of Markov chains is $$100$$.  
    * __Convergence to Equilibrium - Halting__:  
        The theory of Markov Chains allows us to __*guarantee* convergence to equilibrium__. However, it does not specify anything about the __convergence *criterion*__:  
        {: #lst-p}
        * <span>The theory does not allow us to know the Mixing Time in advance.</span>{: style="color: darkred"}.   
            The __Mixing Time__ is the number of steps the Markov chain must run before reaching its _equilibrium distribution_.  
        * <span>The theory, also, does not guide us on how to test/determine whether an MC has reached equilibrium.</span>{: style="color: darkred"}.   

        __Convergence Criterion Theoretical Analysis:__  
        If we analyze the Markov chain from the point of view of a matrix $$A$$ acting on a vector of probabilities $$v$$ , then we know that the chain mixes when $$A^{t}$$ has effectively lost all the eigenvalues from $$A$$ besides the unique eigenvalue of 1.  
        This means that the <span>_magnitude of the second-largest eigenvalue_ will determine the __mixing time__</span>{: style="color: purple"}.  

        __Convergence Criterion In Practice:__  
        In practice, though, we _cannot actually represent our Markov chain in terms of a matrix_.  
        \- The _number of states_ that our probabilistic model can visit is _exponentially large in the number of variables_, so it is infeasible to represent $$\boldsymbol{v}$$, $$A$$, or the eigenvalues of $$\boldsymbol{A}$$.  
        Because of these and other obstacles, we usually __do not know whether a Markov chain has mixed__.  
        Instead, we simply <span>run the Markov chain for an amount of time that we roughly estimate to be sufficient, and use heuristic methods to determine whether the chain has mixed</span>{: style="color: goldenrod"}.  
        These heuristic methods include *__manually inspecting samples__* or __*measuring correlations* between successive samples__.  
    
    <div class="borderexample" markdown="1">
    <span>This section described how to _draw samples_ from a distribution $$q(x)$$ by _repeatedly updating_ $$\boldsymbol{x} \leftarrow \boldsymbol{x}^{\prime} \sim T\left(\boldsymbol{x}^{\prime} \vert \boldsymbol{x}\right)$$.</span>{: style="color: goldenrod"} 
    </div>  


    __Finding a useful $$q(x)$$:__{: style="color: red"}  
    There are two basic approaches to ensure that $$q(x)$$ is a useful distribution:  
    {: #lst-p}
    (1) Derive $$T$$ from a given learned $$p_{\text {model}}$$. E.g. [__Gibbs Sampling__](#bodyContents14), Metropolis-Hastings, etc.     
    (2) Directly _parameterize_ $$T$$ and learn it, so that its stationary distribution implicitly defines the $$p_{\text {model}}$$ of interest. E.g. Generative Stochastic Networks, Diffusion Inversion, Approximate Bayesian Computation.  
    <br>

4. **Gibbs Sampling:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    __Gibbs Sampling__ is an MCMC algorithm for obtaining a sequence of observations which are approximated from a specified multivariate probability distribution, when direct sampling is difficult.  

    It is a method for finding a useful distribution $$q(x)$$ by deriving $$T$$ from a given learned $$p_{\text {model}}$$; in the case of sampling from __EBMs__.  

    It is a conceptually simple and effective approach to building a Markov Chain that samples from $$p_{\text {model}}(\boldsymbol{x})$$, in which sampling from $$T\left(\mathbf{x}^{\prime} \vert \mathbf{x}\right)$$ is accomplished by selecting one variable $$\mathbf{x}_ {i}$$ and sampling it from $$p_{\text {model}}$$ conditioned on its neighbors in the undirected graph $$\mathcal{G}$$ defining the structure of the energy-based model.  

    __Block Gibbs Sampling:__{: style="color: red"}  
    We can, also, sample several variables at the same time as long as they are conditionally independent given all their neighbors.  
    __Block Gibbs Sampling__ is a Gibbs sampling approach that updates many variables simultaneously.  

    __Application - RBMs:__  
    All the hidden units of an RBM may be sampled simultaneously because they are conditionally independent from each other given all the visible units.  
    Likewise, all the visible units may be sampled simultaneously because they are conditionally independent from each other given all the hidden units.  


    __In Deep Learning:__{: style="color: red"}  
    In the context of the deep learning approach to undirected modeling, it is rare to use any approach other than Gibbs sampling. Improved sampling techniques are one possible research frontier.  



    __Summary:__{: style="color: red"}  
    {: #lst-p}
    * A method for sampling from probability distributions of $$\geq 2$$-dimensions.  
    * It is an __MCMC__ method; A __*dependent* sampling__ algorithm.  
    * It is a special case of the __Metropolis-Hastings__ Algorithm.  
        * But, accept all proposals (i.e. no rejections).  
        * It is slightly more __efficient__ than MH because of no rejections.  
        * It requires us to know the __conditional probabilities__ $$p(X_i \vert X_{0}^t, \ldots, X_{i-1}^{t}, X_{i+1}^{t-1}, \ldots, X_{n}^{t-1})$$ and be able to sample from them.  
        * It is __slow__ for *__correlated parameters__*; like MH.  
            Can be alleviated by doing *__block__* sampling (blocks of correlated variables).  
            I.E. sample $$X_j, X_k \sim p(X_j, X_k \vert X_{0}^t, \ldots, X_{n}^{t-1})$$ at the same time.  
            It is _more efficient_ than sampling from uni-dimensional conditional distributions, but generally harder.  
            <button>Sampling Paths</button>{: .showText value="show" onclick="showTextPopHide(event);"}
            ![img](https://cdn.mathpix.com/snip/images/L1FMvW_bNnZNbzbulNgszJhCWqAVxFrX0TG1f5aO6yo.original.fullsize.png){: width="100%" hidden=""}  
            * Gibbs walks in a zig-zag pattern.  
            * MH walks in the diagonal direction but frequently goes off in the orthogonal direction (which have to be rejected).  
            * Hamiltonian MC, best of both worlds: walks in diagonal direction and accept a high proportion of steps).  
    * Often used in __Bayesian Inference__.  
    * Guaranteed to __Asymptotically Converge__ to the true joint distribution.  
    * It is an alternative to deterministic algorithms for inference like EM.  
    * [Gibbs Sampling (Tut. B-Lambert)](https://www.youtube.com/watch?v=ER3DDBFzH2g)  
    <br>


5. **The Challenge of Mixing between Separated Modes in MCMC Algorithms:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  
    The primary difficulty involved with MCMC methods is that they have a tendency to __mix poorly__.  

    __Slow Mixing/Failure to Mix:__{: style="color: red"}  
    Ideally, __successive samples__ from a Markov chain designed to sample from $$p(\boldsymbol{x})$$ would be <span>completely _independent_</span>{: style="color: purple"} from each other and would __visit many different regions__ in $$\boldsymbol{x}$$ space __proportional to their probability__.  
    Instead, especially in *__high-dimensional__* cases, <span>MCMC samples become very *__correlated__*</span>{: style="color: purple"}. We refer to such behavior as __slow mixing__ or even __failure to mix__.  

    __Intuition - Noisy Gradient Descent:__  
    MCMC methods with slow mixing can be seen as inadvertently performing something resembling __noisy gradient descent__ _on the energy function_, or equivalently __noisy hill climbing__ _on the probability_, with respect to the state of the chain (the random variables being sampled).  
    \- The chain tends to take small steps (in the space of the state of the Markov chain), from a configuration $$\boldsymbol{x}^{(t-1)}$$ to a configuration $$\boldsymbol{x}^{(t)}$$, with the energy $$E\left(\boldsymbol{x}^{(t)}\right)$$ generally lower or approximately equal to the energy $$E\left(\boldsymbol{x}^{(t-1)}\right)$$, with a preference for moves that yield lower energy configurations.  
    \- When starting from a rather _improbable configuration_ (higher energy than the typical ones from $$p(\mathbf{x})$$), the chain tends to __gradually reduce the energy of the state__ and only occasionally move to another mode.  
    \- Once the chain has found a region of low energy (for example, if the variables are pixels in an image, a region of low energy might be a connected manifold of images of the same object), which we call a __mode__, the chain will tend to walk around that mode (following a kind of *__random walk__*).  
    \- Once in a while it will step out of that mode and generally return to it or (if it finds an escape route) move toward another mode.  
    \- The problem is that <span>successful escape routes are rare for many interesting distributions</span>{: style="color: goldenrod"}, so the Markov chain will continue to sample the same mode longer than it should.   

    __In Gibbs Sampling:__{: style="color: red"}  
    The problem is very clear when we consider the Gibbs Sampling algorithm.  
    The probability of going from one mode to a nearby mode within a given number of steps is _determined_ by the <span>_shape_ of the __“energy barrier”__</span>{: style="color: purple"} between these modes.  
    \- Transitions between two modes that are __separated by a high energy barrier__ (a region of low probability) are _exponentially less likely_ (in terms of the height of the energy barrier).  
    <button>Gibbs Algorithm Paths</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/2qEiOUCm6i-VjZCNSi3TqQgOyQXCZIEcMoKdIZmJAOM.original.fullsize.png){: width="100%" hidden=""}  
    The problem arises when there are <span>multiple modes with high probability that are separated by regions of low probability</span>{: style="color: purple"}, especially when each Gibbs sampling step must update only a small subset of variables whose values are largely determined by the other variables.  

    __Example and Analysis:__  
    <button>Example and Analysis</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/pIdAEPT0Unuz4oVxenQhB8_WBFtvwU60iA_LD7c4Rn8.original.fullsize.png){: width="100%" hidden=""}  

    __Possible Solution - Block Gibbs Sampling:__  
    Sometimes this problem can be resolved by finding groups of highly dependent units and updating all of them simultaneously in a block. Unfortunately, when the dependencies are complicated, it can be computationally intractable to draw a sample from the group. After all, the problem that the Markov chain was originally introduced to solve is this problem of sampling from a large group of variables.  


    __In (Generative) Latent Variable Models:__{: style="color: red"}  
    In the context of models with __latent variables__, which define a __joint distribution__ $$p_{\text {model}}(\boldsymbol{x}, \boldsymbol{h}),$$ we often __draw samples__ of $$\boldsymbol{x}$$ by *__alternating__* between sampling from $$p_{\text {model}}(\boldsymbol{x} \vert \boldsymbol{h})$$ and sampling from $$p_{\text {model}}(\boldsymbol{h} \vert \boldsymbol{x})$$.  

    __Learning-Mixing Tradeoff:__  
    \- From the pov of __mixing rapidly__, we would like $$p_{\text {model}}(\boldsymbol{h} \vert \boldsymbol{x})$$ to have high entropy.  
    \- From the pov of learning a useful representation of $$\boldsymbol{h},$$ we would like $$\boldsymbol{h}$$ to <span>encode enough information</span>{: style="color: purple"} about $$\boldsymbol{x}$$ <span>to reconstruct it well</span>{: style="color: purple"}, which implies that <span>$$\boldsymbol{h}$$ and $$\boldsymbol{x}$$ and $$\boldsymbol{x}$$ should have _high_ __mutual information__</span>{: style="color: purple"}.  
    These two goals are at odds with each other. We often <span>learn generative models that very precisely _encode_ $$\boldsymbol{x}$$ into $$\boldsymbol{h}$$ but are not able to _mix_ very well</span>{: style="color: goldenrod"}.  

    __In Boltzmann Machines:__  
    This situation arises frequently with Boltzmann machines-the sharper the distribution a Boltzmann machine learns, the harder it is for a Markov chain sampling from the model distribution to mix well.  
    <button>Slow Mixing in Deep Probabilistic Models - Illustration</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/JHPt1iCCZnS-q351i2PFJL8aeJd-2iUSU5nXxEbYYaA.original.fullsize.png){: width="100%" hidden=""}  


    __Summary - Takeaways:__{: style="color: red"}  
    All this could make MCMC methods __less useful__ when the <span>distribution of interest has a __manifold structure__ with a **_separate_ manifold for each class**</span>{: style="color: purple"}: the distribution is __concentrated around many modes__, and these __modes are separated by vast regions of high energy__.  
    This type of distribution is what we expect in many __classification problems__, and it would make MCMC methods __converge very slowly__ because of *__poor mixing between modes__*.  
    <br>


6. **Solutions for the Slow Mixing Problem:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}  
    Since, it is difficult to mix between the different modes of a distribution when the distribution has <span>sharp peaks of high probability surrounded by regions of low probability</span>{: style="color: purple"},  
    Several techniques for faster mixing are based on <span>constructing alternative versions of the target distribution in which the __peaks are not as *high*__ and the __surrounding valleys are not as *low*__</span>{: style="color: purple"}.  
    \- A particularly simple way to do so, is to use __Energy-based Models__:  
    <p>$$p(\boldsymbol{x}) \propto \exp (-E(\boldsymbol{x}))$$</p>  
    \- Energy-based models may be augmented with an extra parameter $$\beta$$ controlling __how sharply peaked__ the distribution is:  
    <p>$$p_{\beta}(\boldsymbol{x}) \propto \exp (-\beta E(\boldsymbol{x}))$$</p>  
    \- The $$\beta$$ parameter is often described as being the __reciprocal of the *temperature*__, reflecting the origin of energy-based models in statistical physics.  
    \- \- When the _temperature falls to **zero**_, and _$$\beta$$ rises to **infinity**_, the EBM becomes __deterministic__.  
    \- \- When the *temperature rises to __infinity__*, and *$$\beta$$ falls to __zero__*, the distribution (for discrete $$\boldsymbol{x}$$) becomes __uniform__.  

    Typically, a model is trained to be evaluated at $$\beta=1$$. However, we can make use of other temperatures, particularly those where $$\beta<1$$.  

    __Tempering:__{: style="color: red"}  
    __Tempering__ is a general strategy of mixing between modes of $$p_{1}$$ rapidly by drawing samples with $$\beta<1$$.  
    Markov chains based on __tempered transitions__ _(Neal, 1994)_ temporarily sample from higher-temperature distributions to mix to different modes, then resume sampling from the unit temperature distribution.  
    These techniques have been applied to models such as __RBMs__ _(Salakhutdinov, 2010)_.  

    __Parallel Tempering:__  
    Another approach is to use __parallel tempering__ _(Iba, 2001)_, in which the Markov chain simulates many different states in parallel, at different temperatures.  
    \- The highest temperature states mix slowly, while the lowest temperature states, at temperature $$1$$, provide accurate samples from the model.  
    \- The transition operator includes stochastically swapping states between two different temperature levels, so that a sufficiently high-probability sample from a high-temperature slot can jump into a lower temperature slot. This approach has also been applied to RBMs _(Desjardins et al., 2010 ; Cho et al., 2010)_.  


    __Results - In Practice:__  
    Although tempering is a promising approach, at this point it has not allowed researchers to make a strong advance in solving the challenge of sampling from complex EBMs.  
    One possible reason is that there are __critical temperatures__ around which the temperature transition must be very slow (as the temperature is gradually reduced) for tempering to be effective.  


    __Depth for Mixing (in Latent-Variable Models):__{: style="color: red"}  
    {: #lst-p}
    * __Problem - Mixing in Latent Variable Models__:  
        When drawing samples from a latent variable model $$p(\boldsymbol{h}, \boldsymbol{x}),$$ we have seen that if $$p(\boldsymbol{h} \vert \boldsymbol{x})$$ encodes $$\boldsymbol{x}$$ too well, then sampling from $$p(\boldsymbol{x} \vert \boldsymbol{h})$$ will not change $$\boldsymbol{x}$$ very much, and mixing will be poor.  
        * __Example of the problem $$(\alpha)$$__:  
            Many representation learning algorithms, such as __Autoencoders__ and __RBMs__, tend to <span>yield a marginal distribution over $$\boldsymbol{h}$$ that is more *__uniform__* and more *__unimodal__* than the original data distribution over $$\boldsymbol{x}$$</span>{: style="color: purple"}.  
        * __Reason for $$(\alpha)$$__:  
            It can be argued that this arises from <span>trying to minimize reconstruction error while using all the available representation space</span>{: style="color: purple"}, because minimizing reconstruction error over the training examples will be better achieved when different training examples are __easily distinguishable__ from each other in $$\boldsymbol{h}$$-space, and thus __well separated__.  
    * __Solution - Deep Representations__:  
        One way to resolve this problem is to make $$\boldsymbol{h}$$ a __deep representation__, encoding $$\boldsymbol{x}$$ into $$\boldsymbol{h}$$ in such a way that a Markov chain in the space of $$\boldsymbol{h}$$ can mix more easily.  
        * __Solution to the problem $$(\alpha)$$__:  
            \- _Bengio et al. (2013 a)_ observed that deeper stacks of regularized autoencoders or RBMs yield marginal distributions in the top-level $$\boldsymbol{h}$$-space that appeared more spread out and more uniform, with less of a gap between the regions corresponding to different modes (categories, in the experiments).  
            \- Training an RBM in that higher-level space allowed __Gibbs sampling__ to *__mix faster between modes__*.  
        
            > It remains unclear, however, how to exploit this observation to help better train and sample from deep generative models.  

    
    __Summary/Takeaway of MCMC methods In-Practice (DL):__{: style="color: red"}  
    Despite the difficulty of mixing, Monte Carlo techniques are useful and are often the best tool available.  
    Indeed, they are the primary tool used to confront the *__intractable partition function__* of __undirected models__.  



<!-- 7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18} -->

***

<!-- ## SECOND
{: #content2}

1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23} -->