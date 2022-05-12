---
layout: NotesPage
title: Inference and Approximate Inference
permalink: /work_files/research/dl/concepts/inference
prevLink: /work_files/research/dl/concepts.html
---

<div markdown="1" class = "TOC">
# Table of Contents
  * [Inference and Approximate Inference](#content1)
  {: .TOC1}
  * [Variational Inference and Learning](#content2)
  {: .TOC2}
  * [Learned Approximate Inference](#content3)
  {: .TOC3}
  * [Mathematics of Approximate Inference Methods](#content4)
  {: .TOC4}
</div>

***
***

__Resources:__{: style="color: red"}  
{: #lst-p}
* [Variational Bayes and The Mean-Field Approximation (blog)](http://bjlkeng.github.io/posts/variational-bayes-and-the-mean-field-approximation/)  
* [Variational Inference: Mean Field Approximation (Lecture Notes)](https://www.cs.cmu.edu/~epxing/Class/10708-17/notes-17/10708-scribe-lecture13.pdf)  
* [Graphical Models, Exponential Families, and Variational Inference (M Jordan)](https://people.eecs.berkeley.edu/~wainwrig/Papers/WaiJor08_FTML.pdf)  
* [Why is the Variational Bound Tight: the variational bound compared to the original error surface (reddit!)](https://www.reddit.com/r/MachineLearning/comments/7dd45h/d_a_cookbook_for_machine_learning_a_list_of_ml/dpyc13e/?context=8&depth=9)  


## Inference and Approximate Inference
{: #content1}

1. **Inference:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    __Inference__ usually refers to <span>computing the probability distribution over one set of variables given another</span>{: style="color: purple"}.  


    __Goals:__{: style="color: red"}  
    {: #lst-p}
    - Computing the likelihood of observed data (in models with latent variables).
    - Computing the marginal distribution over a given subset of nodes in the model.
    - Computing the conditional distribution over a subsets of nodes given a disjoint subset of nodes.
    - Computing a mode of the density (for the above distributions).

    __Approaches:__{: style="color: red"}  
    {: #lst-p}
    - __Exact inference algorithms:__  
        * Brute force
        * The elimination algorithm
        * Message passing (sum-product algorithm, belief propagation)
        * Junction tree algorithm  
    - __Approximate inference algorithms__:  
        * Loopy belief propagation
        * Variational (Bayesian) inference $$+$$ mean field approximations
        * Stochastic simulation / sampling /  MCMC

    __Inference in Deep Learning - Formulation:__{: style="color: red"}  
    In the context of __Deep Learning__, we usually have two __sets of variables__:  
    (1) Set of *__visible__* (*__observed__*) __variables__: $$\: \boldsymbol{v}$$  
    (2) Set of *__latent__* __variables__: $$\: \boldsymbol{h}$$  

    __Inference__ in DL corresponds to <span>computing the *__likelihood__* of __observed data__ $$p(\boldsymbol{v})$$</span>{: style="color: goldenrod"}.  

    When training __probabilistic models with *latent variables*__, we are usually interested in computing  
    <p>$$p(\boldsymbol{h} \vert \boldsymbol{v})$$</p>   
    where $$\boldsymbol{h}$$ are the latent variables, and $$\boldsymbol{v}$$ are the observed (visible) variables (data).  
    <br>


2. **The Challenge of Inference:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    __Motivation - The Challenge of Inference:__{: style="color: red"}  
    The __challenge of inference__ usually refers to the difficult problem of computing $$p(\boldsymbol{h} \vert \boldsymbol{v})$$ or taking expectations wrt it.  
    Such operations are often necessary for tasks like __Maximum Likelihood Learning__.  

    __Intractable Inference:__  
    In DL, intractable inference problems, usually, arise from <span>interactions between *__latent__* __variables__ in a structured graphical model</span>{: style="color: purple"}.  
    These interactions are usually due to:  
    {: #lst-p}
    * __Directed Models__: _"explaining away"_ interactions between *__mutual ancestors__* of the __same visible unit__.  
    * __Undirected Models__: direct interactions between the latent variables.  

    __In Models:__  
    {: #lst-p}
    * __Tractable Inference:__  
        * Many *__simple__* graphical models with only <span>__one hidden layer__</span>{: style="color: purple"} have tractable inference.  
            E.g. __RBMs__, __PPCA__.  
    * __Intractable Inference__:  
        * Most graphical models with <span>__multiple hidden layers__</span>{: style="color: purple"} with __hidden variables__ have intractable *__posterior distributions__*.  
            __Exact inference__ requires an __exponential time__.  
            E.g. __DBMs__, __DBNs__.  
        * Even some models with only a <span>__single__ layer</span>{: style="color: goldenrod"} can be intractable.  
            E.g. __Sparse Coding__  

    <button>Interactions in Graphical Models</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/1GkbyQub5WitledsQpfv77ARrYUn67NzFhCFy_TMeUc.original.fullsize.png){: width="100%" hidden=""}  

    __Computing the Likelihood of Observed Data:__  
    We usually want to compute the likelihood of the observed data $$p(\boldsymbol{v})$$, equivalently the log-likelihood $$\log p(\boldsymbol{v})$$.  
    This usually requires marginalizing out $$\boldsymbol{h}$$.  
    This problem is __intractable__ (difficult) if it is _costly_ to __marginalize__ $$\boldsymbol{h}$$.  
    {: #lst-p}
    * __Data Likelihood__:  (<span>intractable</span>{: style="color: purple"})  
        $$p_{\theta}(\boldsymbol{v})=\int_\boldsymbol{h} p_{\theta}(h) p_{\theta}(v \vert h) dh$$  
    * __Marginal Likelihood (evidence)__: is the data likelihood $$p_{\theta}(\boldsymbol{v})$$ (<span>intractable</span>{: style="color: purple"})    
        $$\int_\boldsymbol{h} p_{\theta}(h) p_{\theta}(v \vert h) dh$$  
    * __Prior__:  
        $$p(\boldsymbol{h})$$ 
    * (Conditional) __Likelihood__:  
        $$p_{\theta}(\boldsymbol{v} \vert h)$$  
    * __Joint__:  
        $$p_{\theta}(\boldsymbol{v}, \boldsymbol{h})$$  
    * __Posterior__: (<span>intractable</span>{: style="color: purple"})    
        $$p_{\theta}(\boldsymbol{h} \vert \boldsymbol{v})=\frac{p_{\theta}(\boldsymbol{v}, \boldsymbol{h})}{p_{\theta}(\boldsymbol{v})}=\frac{p_{\theta}(\boldsymbol{v} \vert h) p_{\theta}(h)}{\int_{\boldsymbol{h}} p_{\theta}(h) p_{\theta}(x \vert h) d h}$$  

    <br>


22. **Approximate Inference:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents122}  
    __Approximate Inference__ is an important and practical approach to confronting the __challenge of (intractable) inference__.  
    It poses __exact inference__ as an __optimization problem__, and aims to *__approximate__* the underlying optimization problem.  
    <br>  
    

3. **Inference as Optimization:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    __Exact inference__ can be described as an __optimization problem__.  

    * __Inference Problem:__  
        * Compute the __log-likelihood__ of the __observed data__, $$\log p(\boldsymbol{v} ; \boldsymbol{\theta})$$.  
            Can be intractable to marginalize $$\boldsymbol{h}$$.  
    * __Inference Problem as Optimization - Core Idea__:  
        * Choose a family of distributions over the *__latent__* __variables__ $$\boldsymbol{h}$$ with its own set of variational parameters $$\boldsymbol{v}$$: $$q(\boldsymbol{h} \vert \boldsymbol{v})$$.  
        * Find the setting of the parameters that makes our approximation closest to the posterior distribution over the latent variables $$p(\boldsymbol{h} \vert \boldsymbol{v})$$.  
            I.E. __Optimization__  
        * Use learned $$q$$ in place of the posterior (as an approximation).  
    * __Optimization - Fitting $$q$$ to the posterior $$p$$__:  
        * Optimize $$q$$ to approximate $$p(\boldsymbol{h} \vert \boldsymbol{v})$$  
        * __Similarity Measure:__ use the *__KL-Divergence__* as a similarity measure between the two distributions  
            <p>$$D_{\mathrm{KL}}(q \| p) = \mathrm{E}_ {h \sim q}\left[\log \frac{q(h)}{p(h\vert {v})}\right] =\int_{h} q(h) \log \left(\frac{q(h)}{p(h\vert {v})}\right) dh$$</p>  
        * __Intractability:__ minimizing the KL Divergence (above) is an intractable problem.  
            Because the expression contains the intractable term $$p(\boldsymbol{h}\vert \boldsymbol{v})$$ which we were trying to avoid.  
    * __Evidence Lower Bound__:  
        * We rewrite the KL Divergence expression in terms of log-likelihood of the data:  
            <p>$$\begin{aligned} D_{\mathrm{KL}}(q \| p) &=\int_{\boldsymbol{h}} q(h) \log \frac{q(h)}{p(h \vert v)} dh \\ &=\int_{\boldsymbol{h}} q(h) \log \frac{q(h)}{p(h, v)} dh+\int_{\boldsymbol{h}} q(h) \log p(v) dh \\ &=\int_{\boldsymbol{h}} q(h) \log \frac{q(h)}{p(h, v)} dh+\log p(\boldsymbol{v}) \end{aligned}$$</p>  
            where we're using Bayes theorem on the second line and the RHS integral simplifies because it's simply integrating over the support of $$q$$ and $$p$$ is not a function of $$h$$.  
            Thus,  
            <p>$$\log p(\boldsymbol{v}) = D_{\mathrm{KL}}(q \| p) - \int_{\boldsymbol{h}} q(h) \log \frac{q(h)}{p(h, v)} dh$$</p>  
        * Notice that since the KL-Divergence is <span>_Non-Negative_</span>{: style="color: purple"}:  
            <p>$$\begin{align}
                D_{\mathrm{KL}}(q \| p) &\geq 0 \\
                D_{\mathrm{KL}}(q \| p) - \int_{\boldsymbol{h}} q(h) \log \frac{q(h)}{p(h, v)} dh &\geq - \int_{\boldsymbol{h}} q(h) \log \frac{q(h)}{p(h, v)} dh \\
                \log p(\boldsymbol{v}) &\geq - \int_{\boldsymbol{h}} q(h) \log \frac{q(h)}{p(h, v)} dh 
                \end{align}
                $$</p>   
            Thus, the term $$- \int_{\boldsymbol{h}} q(h) \log \frac{q(h)}{p(h, v)} dh$$ provides a __lower-bound__{: style="color: goldenrod"} on the __log likelihood of the data__.   
        * We rewrite the term as:  
            <p>$$\mathcal{L}(\boldsymbol{v}, \boldsymbol{\theta}, q) = - \int_{\boldsymbol{h}} q(h) \log \frac{q(h)}{p(h, v)} dh$$</p>  
            the __Evidence Lower Bound (ELBO)__{: style="color: goldenrod"} AKA <span>Variational Free Energy</span>{: style="color: goldenrod"}.  
            Thus,  
            <p>$$\log p(\boldsymbol{v}) \geq \mathcal{L}(\boldsymbol{v}, \boldsymbol{\theta}, q)$$</p>  
        * __The Evidence Lower Bound__ can also be defined as:  
            <p>$$\begin{align}
                \mathcal{L}(\boldsymbol{v}, \boldsymbol{\theta}, q) &= - \int_{\boldsymbol{h}} q(h) \log \frac{q(h)}{p(h, v)} dh \\
                &= \log p(\boldsymbol{v} ; \boldsymbol{\theta})-D_{\mathrm{KL}}(q(\boldsymbol{h} \vert \boldsymbol{v}) \| p(\boldsymbol{h} \vert \boldsymbol{v} ; \boldsymbol{\theta})) \\
                &= \mathbb{E}_ {\mathbf{h} \sim q}[\log p(\boldsymbol{h}, \boldsymbol{v})]+H(q)  
                \end{align}
                $$ </p>  
            The latter being the __canonical definition__ of the ELBO.  
    * __Inference with the Evidence Lower Bound__:  
        * For an appropriate choice of $$q, \mathcal{L}$$ is <span>__tractable__</span>{: style="color: purple"} to compute.  
        * For any choice of $$q, \mathcal{L}$$ provides a lower bound on the likelihood
        * For $$q(\boldsymbol{h} \vert \boldsymbol{v})$$ that are better approximations of $$p(\boldsymbol{h} \vert \boldsymbol{v}),$$ the lower bound $$\mathcal{L}$$ will be tighter  
            I.E. closer to $$\log p(\boldsymbol{v})$$.  
        * When $$q(\boldsymbol{h} \vert \boldsymbol{v})=p(\boldsymbol{h} \vert \boldsymbol{v}),$$ the approximation is perfect, and $$\mathcal{L}(\boldsymbol{v}, \boldsymbol{\theta}, q)=\log p(\boldsymbol{v} ; \boldsymbol{\theta})$$.  
        * <span>Maximizing the ELBO minimizes the KL-Divergence $$D_{\mathrm{KL}}(q \| p)$$</span>{: style="color: goldenrod"}.  
    * __Inference__:  
        We can thus think of inference as the procedure for finding the $$q$$ that maximizes $$\mathcal{L}$$:  
        * __Exact Inference__: maximizes $$\mathcal{L}$$ perfectly by searching over a family of functions $$q$$ that includes $$p(\boldsymbol{h} \vert \boldsymbol{v})$$.  
        * __Approximate Inference__: approximate inference uses approximate optimization to find $$q$$.  
            We can make the optimization procedure less expensive but approximate by:  
            * Restricting the family of distributions $$q$$ that the optimization is allowed to search over  
            * Using an imperfect optimization procedure that may not completely maximize $$\mathcal{L}$$ but may merely increase it by a significant amount.  
    * __Core Idea of Variational Inference__:  
        We don't need to explicitly compute the posterior (or the marginal likelihood), we can solve an optimization problem by finding the right distribution $$$$  that best fits the Evidence Lower Bound.  


    __Learning and Inference wrt the ELBO - Summary:__{: style="color: red"}  
    The <span>__ELBO__ $$\mathcal{L}(\boldsymbol{v}, \boldsymbol{\theta}, q)$$ is a lower bound on $$\log p(\boldsymbol{v} ; \boldsymbol{\theta})$$</span>{: style="color: goldenrod"}:  
    {: #lst-p}
    * __Inference__: can be viewed as <span>maximizing $$\mathcal{L}$$ with respect to $$q$$</span>{: style="color: goldenrod"}.  
    * __Learning__: can be viewed as <span>maximizing $$\mathcal{L}$$ with respect to $$\theta$$</span>{: style="color: goldenrod"}.  


    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * The difference between the ELBO and the KL divergence is the log normalizer (i.e. the evidence), which is the quantity that the ELBO bounds.  
    * Maximizing the ELBO is equivalent to Minimizing the KL-Divergence.  
    <br>

4. **Expectation Maximization:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    The __Expectation-Maximization__ Algorithm is an iterative method to find _maximum likelihood_ or _maximum a posteriori (MAP)_ estimates of parameters in statistical models with _unobserved latent variables_.  

    It is based on maximizing a lower bound $$\mathcal{L}$$.  
    It is not an approach to __approximate inference__.  
    It is an approach to learning with an *__approximate__* __posterior__.  

    __The EM Algorithm:__{: style="color: red"}  
    The EM Algorithm consists of alternating between two steps until convergence:  
    {: #lst-p}
    * The __E(xpectation)-step:__  
        * Let $$\theta^{(0)}$$ denote the value of the parameters at the beginning of the step.  
        * Set $$q\left(\boldsymbol{h}^{(i)} \vert \boldsymbol{v}\right)=p\left(\boldsymbol{h}^{(i)} ; \boldsymbol{\theta}^{(0)}\right)$$ for all indices $$i$$ of the training examples $$\boldsymbol{v}^{(i)}$$ we want to train on (both batch and minibatch variants are valid).  
            By this we mean $$q$$ is defined in terms of the current parameter value of $$\boldsymbol{\theta}^{(0)}$$;  
            if we vary $$\boldsymbol{\theta},$$ then $$p(\boldsymbol{h} \vert \boldsymbol{v} ; \boldsymbol{\theta})$$ will change, but $$q(\boldsymbol{h} \vert \boldsymbol{v})$$ will remain equal to $$p\left(\boldsymbol{h} \vert \boldsymbol{v} ; \boldsymbol{\theta}^{(0)}\right)$$.  
    * The __M(aximization)-step:__  
        * Completely or partially maximize  
            <p>$$\sum_i \mathcal{L}\left(\boldsymbol{v}^{(i)}, \boldsymbol{\theta}, q\right)$$</p>  
            with respect to $$\boldsymbol{\theta}$$ using your optimization algorithm of choice.  

    __Relation to Coordinate Ascent:__{: style="color: red"}  
    The algorithm can be viewed as a __Coordinate Ascent__ algorithm to maximize $$\mathcal{L}$$.  
    On one step, we maximize $$\mathcal{L}$$ with respect to $$q,$$ and on the other, we maximize $$\mathcal{L}$$ with respect to $$\boldsymbol{\theta}$$.  
    __Stochastic Gradient Ascent__ on _latent variable models_ can be seen as a special case of the EM algorithm where the M-step consists of taking a single gradient step.  
    > Other variants of the EM algorithm can make much larger steps. For some model families, the M-step can even be performed analytically, jumping all the way to the optimal solution for $$\theta$$ given the current $$q$$.  

    __As Approximate Inference - Interpretation:__{: style="color: red"}  
    Even though the E-step involves _exact inference_, the EM algorithm can be viewed as using _approximate inference_.  
    The M-step assumes that the same value of $$q$$ can be used for all values of $$\theta$$.  
    This will introduce a gap between $$\mathcal{L}$$ and the true $$\log p(\boldsymbol{v})$$ as the M-step moves further and further away from the value $$\boldsymbol{\theta}^{(0)}$$ used in the E-step.  
    Fortunately, the E-step reduces the gap to zero again as we enter the loop for the next time.  

    
    __Insights/Takeaways:__{: style="color: red"}  
    {: #lst-p}
    1. The __Basic Structure of the Learning Process:__  
        We update the model parameters to improve the likelihood of a completed dataset, where all missing variables have their values provided by an estimate of the posterior distribution.  
        > This particular insight is not unique to the EM algorithm. For example, using gradient descent to maximize the log-likelihood also has this same property; the log-likelihood gradient computations require taking expectations with respect to the posterior distribution over the hidden units.   
    2. __Reusing $$q$$:__  
        We can continue to use one value of $$q$$ even after we have moved to a different value of $$\theta$$.  
        This particular insight is used throughout _classical machine learning_ to derive large M-step updates.  
        In the context of deep learning, most models are too complex to admit a tractable solution for an optimal large M-step update, so this second insight, which is more unique to the EM algorithm, is rarely used.  



    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * [The Expectation-Maximization Algorithm and Derivation (Blog!)](http://bjlkeng.github.io/posts/the-expectation-maximization-algorithm/)  
    * The EM algorithm enables us to make large learning steps with a fixed $$q$$  
    <br>


5. **MAP Inference:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  
    __MAP Inference__ is an alternative form of inference where we are interested in computing the single most likely value of the missing variables, rather than to infer the entire distribution over their possible values $$p(\boldsymbol{h} \vert \boldsymbol{v})$$.  
    In the context of __latent variable models__, we compute:  
    <p>$$\boldsymbol{h}^{* }=\underset{\boldsymbol{h}}{\arg \max } p(\boldsymbol{h} \vert \boldsymbol{v})$$</p>  

    __As Approximate Inference:__{: style="color: red"}  
    It is __not__ usually thought of as __approximate inference__, since it computes the <span>exact most likely value of $$\boldsymbol{h}^{* }$$</span>{: style="color: purple"}.  
    However, to develop a [__learning process__](#bodyContents15lp) wrt maximizing the lower bound $$\mathcal{L}(\boldsymbol{v}, \boldsymbol{h}, q),$$ then it is helpful to think of MAP inference as a procedure that provides a value of $$q$$.  
    In this sense, we can think of MAP inference as __approximate inference__, because it <span>does not provide the optimal $$q$$</span>{: style="color: purple"}.  
    We can __derive__ MAP Inference as a form of approximate inference by <span>restricting the family of distributions $$q$$ may be drawn from</span>{: style="color: goldenrod"}.  
    __Derivation:__  
    {: #lst-p}
    * We require $$q$$ to take on a __Dirac distribution__:  
        <p>$$q(\boldsymbol{h} \vert \boldsymbol{v})=\delta(\boldsymbol{h}-\boldsymbol{\mu})$$</p>  
    * This means that we can now control $$q$$ entirely via $$\boldsymbol{\mu}$$.  
    * Dropping terms of $$\mathcal{L}$$ that do not vary with $$\boldsymbol{\mu},$$ we are left with the optimization problem:  
        <p>$$\boldsymbol{\mu}^{* }=\underset{\mu}{\arg \max } \log p(\boldsymbol{h}=\boldsymbol{\mu}, \boldsymbol{v})$$</p>  
    * which is *__equivalent__* to the __MAP inference problem__:  
        <p>$$\boldsymbol{h}^{* }=\underset{\boldsymbol{h}}{\arg \max } p(\boldsymbol{h} \vert \boldsymbol{v})$$</p>  

    __The Learning Procedure with MAP Inference:__{: style="color: red"}{: #bodyContents15lp}  
    We can, thus, justify a learning procedure similar to __EM__, where we alternate between:  
    {: #lst-p}
    * Performing MAP inference to infer $$\boldsymbol{h}^{* }$$, and  
    * Updating update $$\boldsymbol{\theta}$$ to increase $$\log p\left(\boldsymbol{h}^{* }, \boldsymbol{v}\right)$$.  

    __As Coordinate Ascent:__  
    As with EM, this is a form of __coordinate ascent__ on $$\mathcal{L},$$ where we alternate between using inference to optimize $$\mathcal{L}$$ with respect to $$q$$ and using parameter updates to optimize $$\mathcal{L}$$ with respect to $$\boldsymbol{\theta}$$.  

    __Lower Bound (ELBO) Justification:__  
    The procedure as a whole can be justified by the fact that $$\mathcal{L}$$ is a lower bound on $$\log p(\boldsymbol{v})$$.  
    In the case of MAP inference, this justification is rather *__vacuous__*, because the bound is __infinitely loose__, due to the __Dirac distribution's differential entropy of negative infinity__.  
    <span>Adding noise to $$\mu$$ would make the bound meaningful again</span>{: style="color: goldenrod"}.   

    __MAP Inference in Deep Learning - Applications:__{: style="color: red"}  
    MAP Inference is commonly used in deep learning as both a <span>__feature extractor__</span>{: style="color: purple"} and a <span>__learning mechanism__</span>{: style="color: purple"}.  
    It is primarily used for __sparse coding models__.  

    __MAP Inference in Sparse Coding Models:__{: style="color: red"}{: #bodyContents15map_sc}  
    <button>Sparse Coding Discussion</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/xhMTHTt2HOc7OibASJ5OYwn0Dw0ck6ZFGalynC643GQ.original.fullsize.png){: width="100%" hidden=""}  

    __Summary:__{: style="color: red"}  
    Learning algorithms based on MAP inference enable us to <span>__learn using a *point estimate*__ of $$p(\boldsymbol{h} \vert \boldsymbol{v})$$ rather than inferring the entire distribution</span>{: style="color: goldenrod"}.  
    <br>


6. **Variational Inference and Learning:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}  
    

    __Main Idea - Restricting family of distributions $$q$$:__{: style="color: red"}  
    The core idea behind variational learning is that we can maximize $$\mathcal{L}$$ over a restricted family of distributions $$q$$.  
    This family should be chosen so that it is easy to compute $$\mathbb{E}_ {q} \log p(\boldsymbol{h}, \boldsymbol{v})$$.  
    A typical way to do this is to introduce assumptions about how $$q$$ factorizes.  
    Mainly, we make a __Mean-Field Approximation__ to $$q$$.  


    __Mean-Field Approximation:__{: style="color: red"}  
    __Mean-Field Approximation__ is a type of _Variational Bayesian Inference_ where we assume that the unknown variables can be partitioned so that each partition is <span>__independent__</span>{: style="color: purple"} of the others.  
    The Mean-Field Approximation assumes the variational distribution over the latent variables factorizes as:  
    <p>$$q(\boldsymbol{h} \vert \boldsymbol{v})=\prod_{i} q\left(h_{i} \vert \boldsymbol{v}\right)$$</p>  
    I.E. it imposes the restriction that $$q$$ is a __factorial distribution__.  

    More generally, we can impose any graphical model structure we choose on $$q,$$ to flexibly determine how many interactions we want our approximation to capture.  
    This fully general graphical model approach is called __structured variational inference__ _(Saul and Jordan, 1996)_.  

    __The Optimal Probability Distribution $$q$$:__{: style="color: red"}  
    The beauty of the variational approach is that we do not need to specify a specific parametric form for $$q$$.  
    We specify how it should factorize, but then <span>the optimization problem determines the __*optimal* probability distribution__ within those factorization constraints</span>{: style="color: purple"}.  
    __The Inference Optimization Problem:__{: style="color: red"}  
    {: #lst-p}
    * For __*discrete* latent variables__: we use traditional optimization techniques to optimize a finite number of variables describing the $$q$$ distribution.  
    * For __*continuous* latent variables__: we use <span>__calculus of variations__</span>{: style="color: purple"} to perform optimization over a space of functions and actually determine which function should be used to represent $$q$$.  
        * __Calculus of Variations__ removes much of the responsibility from the human designer of the model, who now must specify only how $$q$$ factorizes, rather than needing to guess how to design a specific $$q$$ that can accurately approximate the posterior.  

        > Calculus of variations is the origin of the names "variational learning" and "variational inference", but the names apply in both discrete and continuous cases.    

    __KL-Divergence Optimization:__  
    {: #lst-p}
    * The Inference Optimization Problem boils down to <span>maximizing $$\mathcal{L}$$ with respect to $$q$$</span>{: style="color: purple"}.  
    * This is equivalent to <span>minimizing $$D_{\mathrm{KL}}(q(\boldsymbol{h} \vert \boldsymbol{v}) \| p(\boldsymbol{h} \vert \boldsymbol{v}))$$</span>{: style="color: purple"}.  
    * Thus, we are <span>fitting $$q$$ to $$p$$</span>{: style="color: goldenrod"}.  
    * However, we are doing so with the opposite direction of the KL-Divergence. We are, _unnaturally_, assuming that $$q$$ is constant and $$p$$ is varying.  
    * In the inference optimization problem, we choose to use $$D_{\mathrm{KL}}\left(q(\boldsymbol{h} \vert \boldsymbol{v}) \| p(\boldsymbol{h} \vert \boldsymbol{v})\right)$$ for *__computational reasons__*.  
        * Specifically, computing $$D_{\mathrm{KL}}\left(q(\boldsymbol{h} \vert \boldsymbol{v}) \| p(\boldsymbol{h} \vert \boldsymbol{v})\right)$$ involves evaluating expectations with respect to $$q,$$ so by designing $$q$$ to be simple, we can simplify the required expectations.  
        * The opposite direction of the KL divergence would require computing expectations with respect to the true posterior.  
            Because the form of the true posterior is determined by the choice of model, we cannot design a reduced-cost approach to computing $$D_{\mathrm{KL}}(p(\boldsymbol{h} \vert \boldsymbol{v}) \| q(\boldsymbol{h} \vert \boldsymbol{v}))$$ exactly.  
    * __Three Cases for Optimization__:  
        * If $$q$$ is high and $$p$$ is high, then we are happy (i.e. low KL divergence).
        * If $$q$$ is high and $$p$$ is low then we pay a price (i.e. high KL divergence).
        * If $$q$$ is low then we dont care (i.e. also low KL divergence, regardless of $$p$$).
    * __Optimization-based Inference vs Maximum Likelihood (ML) Learning__:  
        * __ML-Learning:__ fits a model to data by minimizing $$D_{\mathrm{KL}}\left(p_{\text {data }} \| p_{\text {model }}\right)$$.  
            It encourages the <span>__model__ to have __*high* probability__ everywhere that the __data__ has __*high* probability__</span>{: style="color: purple"}, 
        * __Optimization-based Inference__:   
            It encourages <span>__$$q$$__ to have __*low* probability__ everywhere the __true posterior__ has __*low* probability__</span>{: style="color: purple"}.  
    
    __Variational (Bayesian) Inference:__{: style="color: red"}  
    __Variational Bayesian Inference__ AKA __Variational Bayes__ is most often used to infer the <span>_conditional_ distribution over the latent variables given the observations</span>{: style="color: purple"}  (and parameters).  
    This is also known as the __posterior distribution over the *latent* variables__:  
    <p>$$p(z \vert x, \alpha)=\frac{p(z, x \vert \alpha)}{\int_{z} p(z, x \vert \alpha)}$$</p>  
    which is usually *__intractable__*.  

    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * __KL Divergence Optimization:__  
        Optimizing the KL-Divergence given by:  
        <p>$$D_{\mathrm{KL}}(q \| p) = \mathrm{E}_ {z \sim q}\left[\log \frac{q(z)}{p(z\vert x)}\right] =\int_{z} q(z) \log \left(\frac{q(z)}{p(z\vert x)}\right) dz$$</p>  
        * __Three Cases for Optimization__:  
            * If $$q$$ is high and $$p$$ is high, then we are happy (i.e. low KL divergence).
            * If $$q$$ is high and $$p$$ is low then we pay a price (i.e. high KL divergence).
            * If $$q$$ is low then we dont care (i.e. also low KL divergence, regardless of $$p$$).
    <br>

***

## Variational Inference and Learning
{: #content2}

<!-- 1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21} -->

2. **Variational Inference - Discrete Latent Variables:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}  
    Variational Inference with Discrete Latent Variables is relatively straightforward.  
    __Representing $$q$$:__  
    We define a distribution $$q$$ where each factor of $$q$$ is just defined by a lookup table over discrete states.  
    In the simplest case, $$h$$ is binary and we make the mean field assumption that $$q$$ factorizes over each individual $$h_{i}$$.  
    In this case we can parametrize $$q$$ with a vector $$\hat{h}$$ whose entries are probabilities.  
    Then $$q\left(h_{i}=1 \vert \boldsymbol{v}\right)=\hat{h}_ {i}$$.  
    __Optimizing $$q$$:__  
    After determining how to represent $$q$$ we simply __optimize its parameters__.  
    For __discrete__ latent variables this is just a standard optimization problem e.g. *__gradient descent__*.  
    However, because this optimization must occur in the inner loop of a learning algorithm, it must be __very fast__[^1].  
    A popular choice is to <span>__iterate fixed-point equations__</span>{: style="color: purple"}; to solve:  
    <p>$$\frac{\partial}{\partial \hat{h}_ {i}} \mathcal{L}=0$$</p>  
    for $$\hat{h}_ {i}$$.  
    We repeatedly update different elements of $$\hat{\boldsymbol{h}}$$ until we satisfy a convergence criterion.  


    __Application - Binary Sparse Coding:__{: style="color: red"}  
    <br>



3. **Variational Inference - Continuous Latent Variables:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}  
    Variational Inference and Learning with Continuous Latent Variables requires the use of the [__calculus of variations__](#bodyContents41) for maximizing $$\mathcal{L}$$ with respect to $$q(\boldsymbol{h} \vert \boldsymbol{v})$$.  

    In most cases, practitioners need not solve any calculus of variations problems themselves. Instead, there is a __general equation for the mean field fixed-point updates__.  

    __The General Equation for Mean-Field Fixed-Point Updates:__{: style="color: red"}  
    If we make the mean field approximation  
    <p>$$q(\boldsymbol{h} \vert \boldsymbol{v})=\prod_{i} q\left(h_{i} \vert \boldsymbol{v}\right)$$</p>  
    and fix $$q\left(h_{j} \vert \boldsymbol{v}\right)$$ for all $$j \neq i,$$ then the <span>optimal $$q\left(h_{i} \vert \boldsymbol{v}\right)$$ may be obtained by __normalizing the unnormalized distribution__</span>{: style="color: goldenrod"}:  
    <p>$$\tilde{q}\left(h_{i} \vert \boldsymbol{v}\right) = \exp \left(\mathbb{E}_{\mathbf{h}_{-i} \sim q\left(\mathbf{h}_ {-i} \vert \boldsymbol{v}\right)} \log \tilde{p}(\boldsymbol{v}, \boldsymbol{h})\right) = e^{\mathbb{E}_{\mathbf{h}_ {-i} \sim q\left(\mathbf{h}_ {-i} \vert \boldsymbol{v}\right)} \log \tilde{p}(\boldsymbol{v}, \boldsymbol{h})}$$</p>  
    as long as $$p$$ does not assign $$0$$ probability to any joint configuration of variables.  
    \- Carrying out the expectation inside the equation will yield the correct functional form of $$q\left(h_{i} \vert \boldsymbol{v}\right)$$.   
    \- The General Equation yields the mean field approximation for any probabilistic model.  
    \- Deriving functional forms of $$q$$ directly using calculus of variations is only necessary if one wishes to develop a new form of variational learning.  
    \- The General Equation is a __fixed-point equation__, designed to be iteratively applied for each value of $$i$$ repeatedly until convergence.  

    __Functional Form of the Optimal Distribution/Solution:__{: style="color: red"}  
    The General Equation tells us the <span>__functional form__ that the _optimal solution_ will take</span>{: style="color: purple"}, whether we arrive there by fixed-point equations or not.  
    <span>This means we can take the functional form from that equation but regard some of the values that appear in it as *__parameters__*, which we can optimize with any optimization algorithm we like.</span>{: style="color: goldenrod"}  
    <button>Example - Application:</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/YFBRwnXeoFZ7iB-yu4PE3Pszt1U5A8BGnc5ZhATfijg.original.fullsize.png){: width="100%" hidden=""}  

    For examples of real applications of variational learning with continuous variables in the context of deep learning, see _Goodfellow et al. (2013d)_.  
    <br>


4. **Interactions between Learning and Inference:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}  
    <span>Using __approximate inference__ as part of a __learning algorithm__ affects the **learning process**</span>{: style="color: purple"}, and this in turn <span>affects the **_accuracy_ of the inference algorithm**</span>{: style="color: purple"}.  
    __Analysis:__  
    {: #lst-p}
    * The training algorithm tends to adapt the model in a way that makes the approximating assumptions underlying the approximate inference algorithm become more true.  
    * When training the parameters, variational learning increases  
        <p>$$\mathbb{E}_ {\mathbf{h} \sim q} \log p(\boldsymbol{v}, \boldsymbol{h})$$</p>  
    * For a specific $$v$$ this:  
        * increases $$p(\boldsymbol{h} \vert \boldsymbol{v})$$ for values of $$\boldsymbol{h}$$ that have high probability under $$q(\boldsymbol{h} \vert \boldsymbol{v})$$ and  
        * decreases $$p(\boldsymbol{h} \vert \boldsymbol{v})$$ for values of $$\boldsymbol{h}$$ that have low probability under $$q(\boldsymbol{h} \vert \boldsymbol{v})$$.  
    * This behavior <span>causes our approximating assumptions to become *__self-fulfilling prophecies__*</span>{: style="color: purple"}.  
        If we train the model with a unimodal approximate posterior, we will obtain a model with a true posterior that is far closer to unimodal than we would have obtained by training the model with exact inference.  

    __Computing the Effect (Harm) of using Variational Inference:__{: style="color: red"}  
    Computing the true amount of harm imposed on a model by a variational approximation is thus very difficult.  
    {: #lst-p}
    * There exist several methods for estimating $$\log p(\boldsymbol{v})$$:  
        We often estimate $$\log p(\boldsymbol{v} ; \boldsymbol{\theta})$$ after training the model and find that the gap with $$\mathcal{L}(\boldsymbol{v}, \boldsymbol{\theta}, q)$$ is small.  
        * From this, we can __conclude__ that <span>our variational approximation is __accurate for the specific value of $$\boldsymbol{\theta}$$__</span>{: style="color: purple"} that we obtained from the learning process.  
        * We should *__not__* __conclude__ that <span>our variational approximation is __accurate in general__</span>{: style="color: purple"} or that <span>the variational approximation __did *little harm* to the learning process__</span>{: style="color: purple"}.  
    * To measure the *__true amount of harm__ induced by the variational approximation*:  
        * We would need to know $$\boldsymbol{\theta}^{* }=\max_{\boldsymbol{\theta}} \log p(\boldsymbol{v} ; \boldsymbol{\theta})$$.  
        * It is possible for $$\mathcal{L}(\boldsymbol{v}, \boldsymbol{\theta}, q) \approx \log p(\boldsymbol{v} ; \boldsymbol{\theta})$$ and $$\log p(\boldsymbol{v} ; \boldsymbol{\theta}) \ll \log p\left(\boldsymbol{v} ; \boldsymbol{\theta}^{* }\right)$$ to hold simultaneously.  
        * If $$\max_{q} \mathcal{L}\left(\boldsymbol{v}, \boldsymbol{\theta}^{* }, q\right) \ll \log p\left(\boldsymbol{v} ; \boldsymbol{\theta}^{* }\right),$$ because $$\boldsymbol{\theta}^{* }$$ induces too complicated of a posterior distribution for our $$q$$ family to capture, then the learning process will never approach $$\boldsymbol{\theta}^{* }$$.  
        * Such a problem is very difficult to detect, because we can only know for sure that it happened if we have a superior learning algorithm that can find $$\boldsymbol{\theta}^{* }$$ for comparison.  
    <br>


5. **Learned Approximate Inference:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}  
    __Motivation:__{: style="color: red"}  
    Explicitly performing optimization via iterative procedures such as _fixed-point equations_ or _gradient-based optimization_ is often __very expensive__ and __time consuming__.  
    Many approaches to inference avoid this expense by <span>learning to perform approximate inference</span>{: style="color: purple"}.  

    __Learned Approximate Inference:__  
    Learns to perform approximate inference by viewing the (multistep iterative) optimization process as a function $$f$$ that maps an input $$v$$ to an approximate distribution $$q^{* }=\arg \max_{q} \mathcal{L}(\boldsymbol{v}, q)$$, and then <span>approximates this function with a __neural network__</span>{: style="color: goldenrod"} that implements an approximation $$f(\boldsymbol{v} ; \boldsymbol{\theta})$$.  


    __Wake-Sleep:__{: style="color: red"}  
    __Motivation__:  
    {: #lst-p}
    * One of the main difficulties with training a model to infer $$h$$ from $$v$$ is that we do not have a supervised training set with which to train the model.  
    * Given a $$v$$ we do not know the appropriate $$h$$.  
    * The mapping from $$v$$ to $$h$$ depends on the choice of model family, and evolves throughout the learning process as $$\theta$$ changes.  

    __Wake-Sleep Algorithm__:  
    The __wake-sleep algorithm__ _(Hinton et al., 1995b; Frey et al., 1996)_ resolves this problem by <span>drawing samples of both $$h$$ and $$v$$ __from the *model distribution*__</span>{: style="color: purple"}.  
    * For example, in a __directed model__, this can be done cheaply by performing *__ancestral sampling__* beginning at $$h$$ and ending at $$v$$.  
        The inference network can then be trained to perform the reverse mapping: predicting which $$h$$ caused the present $\boldsymbol{v}$.  
    
    __DrawBacks__:  
    The main drawback to this approach is that we will only be able to train the inference network on values of $$\boldsymbol{v}$$ that have high probability under the model.  
    Early in learning, the <span>model distribution will not resemble the data distribution</span>{: style="color: purple"}, so <span>the inference network will not have an opportunity to _learn on samples that resemble data_</span>{: style="color: purple"}.  

    __Relation to Biological Dreaming:__  
    <button>Discussion</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/gAcJcN1TtW7H23J0TssVMLYjOufszOjoEigvRExEVeo.original.fullsize.png){: width="100%" hidden=""}  


    __Generative Modeling - Application:__{: style="color: red"}  
    Learned approximate inference has recently become one of the dominant approaches to generative modeling, in the form of the __Variational AutoEncoder__ _(Kingma, 2013; Rezende et al., 2014)_.  
    In this elegant approach, there is <span>no need to _construct explicit targets_ for the inference network</span>{: style="color: purple"}.  
    Instead, the <span>inference network is simply used to define $$\mathcal{L},$$</span>{: style="color: purple"} and then <span>the parameters of the inference network are adapted to increase $$\mathcal{L}$$</span>{: style="color: purple"}.  


<!-- 6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents26}
7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents27} -->


***
***

## Mathematics of Approximate Inference
{: #content4}

[Directional Derivative](http://tutorial.math.lamar.edu/Classes/CalcIII/DirectionalDeriv.aspx)  
[The Calculus of Variations (Blog!)](http://bjlkeng.github.io/posts/the-calculus-of-variations/#id1)  

1. **Calculus of Variations:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents41}  
    
    Method for finding the *__stationary__* __functions__ of a functional $$I[f]$$ (function of functions) by solving a differential equation.  

    __Formally,__ calculus of variations seeks to find the function $$y=f(x)$$ such that the integral (functional):  
    <p>$$I[y]=\int_{x_{1}}^{x_{2}} L\left(x, y(x), y^{\prime}(x)\right) d x$$</p>   
    <p>$$\begin{array}{l}{\text {where}}\\{x_{1}, x_{2} \text { are constants, }} \\ {y(x) \text { is twice continuously differentiable, }} \\ {y^{\prime}(x)=d y / d x} \\ {L\left(x, y(x), y^{\prime}(x)\right) \text { is twice continuously differentiable with respect to its arguments } x, y, y^{\prime}}\end{array}$$</p>  
    is __stationary__.  


    __Euler Lagrange Equation - Finding Extrema:__{: style="color: red"}  
    Finding the extrema of functionals is similar to finding the maxima and minima of functions. The maxima and minima of a function may be located by finding the points where its derivative vanishes (i.e., is equal to zero). The extrema of functionals may be obtained by finding functions where the functional derivative is equal to zero. This leads to solving the associated Euler–Lagrange equation.  

    The __Euler Lagrange Equation__ is a second-order partial differential equation whose solutions are the functions for which a given functional is stationary:  
    <p>$$\frac{\partial L}{\partial f}-\frac{d}{d x} \frac{\partial L}{\partial f^{\prime}} = 0$$</p>  
    It is defined in terms of the __functional derivative__:  
    <p>$$\frac{\delta J}{\delta f(x)} = \frac{\partial L}{\partial f}-\frac{d}{d x} \frac{\partial L}{\partial f^{\prime}} = 0$$</p>  




    __Shortest Path between Two Points:__{: style="color: red"}  
    Find path such that the distance $$AB$$ between two points is minimized.  
    Using the *__arc length__*, we define the following __functional__:  
    <p>$$\begin{align}
        I &= \int_{A}^{B} dS \\
             &= \int_{A}^{B} \sqrt{dx^2 + dy^2} \\
             &= \int_{A}^{B} \sqrt{1 + \left(\dfrac{dy}{dx}\right)^2} dx \\ 
             &= \int_{x_1}^{x_2} \sqrt{1 + \left(\dfrac{dy}{dx}\right)^2} dx
        \end{align}
        $$</p>  
    * Now, we formulate the __variational problem__:  
        Find the extremal function $$y=f(x)$$ between two points $$A=(x_1, y_1)$$ and $$B=(x_2, y_2)$$ such that the following integral is __minimized__:  
        <p>$$I[y] = \int_{x_{1}}^{x_{2}} \sqrt{1+\left[y^{\prime}(x)\right]^{2}} d x$$</p>   
        where $$y^{\prime}(x)=\frac{d y}{d x}, y_{1}=f\left(x_{1}\right), y_{2}=f\left(x_{2}\right)$$.  
    * __Solution:__  
        We use the __Euler-Lagrange Equation__ to find the extremal function $$f(x)$$ that minimizes the functional $$I[y]$$:  
        <p>$$\frac{\partial L}{\partial f}-\frac{d}{d x} \frac{\partial L}{\partial f^{\prime}}=0$$</p>  
        where $$L=\sqrt{1+\left[f^{\prime}(x)\right]^{2}}$$.  
        * Since $$f$$ does not appear explicity in $$L,$$ the first term in the Euler-Lagrange equation vanishes for all $$f(x)$$  
            <p>$$\frac{\partial L}{\partial f} = 0$$</p>  
        * Thus,  
            <p>$$\frac{d}{d x} \frac{\partial L}{\partial f^{\prime}}=0$$</p>  
        * Substituting for $$L$$ and taking the derivative:  
            <p>$$\frac{d}{d x} \frac{f^{\prime}(x)}{\sqrt{1+\left[f^{\prime}(x)\right]^{2}}}=0$$</p>  
            for some constant $$c$$.  
        * If the derivative $$\frac{d}{dx}$$, above, is zero, then  
            <p>$$\frac{f^{\prime}(x)}{\sqrt{1+\left[f^{\prime}(x)\right]^{2}}}=c$$</p>  
            for some constant $$c$$.  
        * Square both sides:  
            <p>$$\frac{\left[f^{\prime}(x)\right]^{2}}{1+\left[f^{\prime}(x)\right]^{2}}=c^{2}$$</p>  
            where $$0 \leq c^{2}<1$$.  
        * Solving:  
            <p>$$\left[f^{\prime}(x)\right]^{2}=\frac{c^{2}}{1-c^{2}}$$</p>  
            $$\implies$$  
            <p>$$f^{\prime}(x)=m$$</p>  
            is a constant $$m$$.  
        * Integrating:  
            <p>$$f(x)=m x+b$$</p>  
            is an __equation of a (straight) line__, where $$m=\frac{y_{2}-y_{1}}{x_{2}-x_{1}} \quad$$ and $$\quad b=\frac{x_{2} y_{1}-x_{1} y_{2}}{x_{2}-x_{1}}$$.  

        In other words, the shortest distance between two points is a straight line.  
        <div class="borderexample" markdown="1">
        <span>We have found the extremal function $$f(x)$$ that minimizes the functional $$A[y]$$ so that $$A[f]$$ is a minimum.</span>{: style="color: purple"}
        </div>  

    <br>

2. **Mean Field Methods:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents42}

3. **Mean Field Approximations:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents43}

<!-- 4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents44}
5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents45}
6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents46}
7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents47}
8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents48} -->


[^1]: To achieve this speed, we typically use special optimization algorithms that are designed to solve comparatively small and simple problems in few iterations.  