---
layout: NotesPage
title: The Partition Function
permalink: /work_files/research/dl/concepts/partition_func
prevLink: /work_files/research/dl/concepts.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Introduction - The Partition Function](#content1)
  {: .TOC1}
  <!-- * [SECOND](#content2)
  {: .TOC2} -->
  * [Estimating the Partition Function](#content3)
  {: .TOC3}
</div>

***
***


[A Thorough Introduction to Boltzmann Machines](http://willwolf.io/2018/10/20/thorough-introduction-to-boltzmann-machines/)  
[Strategies for Confronting the Partition Function (Blog! + code)](http://willwolf.io/2018/10/29/additional-strategies-partition-function/)  
[Approximating the Softmax (Ruder)](http://ruder.io/word-embeddings-softmax/index.html)  
[Confronting the partition function (Slides)](http://www.tsc.uc3m.es/~jcid/MLG/mlg2018/DL_Cap18.pdf)  
[Graphical Models, Exponential Families, and Variational Inference (M Jordan)](https://people.eecs.berkeley.edu/~wainwrig/Papers/WaiJor08_FTML.pdf)  
* [Towards Biologically Plausible Deep Learning (paper!)](https://arxiv.org/pdf/1502.04156.pdf)  



## Introduction - The Partition Function
{: #content1}

1. **The Partition Function:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    __The Partition Function__ is the _normalization constant_ of an unnormalized probability distribution $$\tilde{p}(\mathbf{x} ; \boldsymbol{\theta})$$.   
    
    Formally, it is the (possibly infinite) sum over the unnormalized probability $$\tilde{p}(\mathbf{x} ; \boldsymbol{\theta})$$ of all the states/events $$\boldsymbol{x} \in X$$,  
    {: #lst-p}
    * __Discrete Variables__:  
        <p>$$Z(\boldsymbol{\theta}) = \sum_{\boldsymbol{x}} \tilde{p}(\boldsymbol{x})$$</p>  
    * __Continuous Variables__:  
        <p>$$Z(\boldsymbol{\theta}) = \int \tilde{p}(\boldsymbol{x}) d \boldsymbol{x}$$</p>  

    It is defined such that:  
    <p>$$\sum_\mathbf{x} p(\mathbf{x} ; \boldsymbol{\theta}) = \sum_\mathbf{x} \dfrac{\tilde{p}(\mathbf{x} ; \boldsymbol{\theta})}{Z(\boldsymbol{\theta})} = 1$$</p>  

    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * The Partition Function contains an __explicit Temperature__  
    * The Partition Function is a __generating function__  
    * [Statistical Mechanics of Learning from Examples](https://pdfs.semanticscholar.org/2498/a4e1755f047accc06a6e0fab0b0eb1b37ae0.pdf)  
        _Sompolinsky et al._ confront the partition function for a Perceptron using statistical mechanics methods developed for spin glasses and simple nets (Garder, Derrida) and applied it to Perceptrons and, later, to something like MLPs.  
    * [Unreasonable effectiveness of learning neural networks: From accessible states and robust ensembles to basic algorithmic schemes](https://www.pnas.org/content/pnas/113/48/E7655.full.pdf)  
        Uses old techniques from non-equilibrium statistical mechanics to address the modern problems of inference.  
    <br>

2. **Handling the Partition Function - Motivation:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    Many __*Undirected* Probabilistic Graphical Models (PGMs)__ are defined by an unnormalized probability distribution $$\tilde{p}(\mathbf{x} ; \boldsymbol{\theta})$$.  
    To obtain a valid probability distribution, we need to *__normalize__* $$\tilde{p}$$ by dividing by a partition function $$Z(\boldsymbol{\theta})$$:  
    <p>$$p(\mathbf{x} ; \boldsymbol{\theta})=\dfrac{1}{Z(\boldsymbol{\theta})} \tilde{p}(\mathbf{x} ; \boldsymbol{\theta})$$</p>  
    Calculating the partition function can be *__intractable__* for many interesting models.  

    __The Partition Function in Deep Probabilistic Models:__{: style="color: red"}  
    Deep Probabilistic Models are usually designed with the partition function in mind. There a few approaches taken in the designs:  
    {: #lst-p}
    * Some models are designed to have a __tractable normalizing constant__.  
    * Others are designed to be used in ways (training/inference) that _avoid_ computing the normalized probability altogether.  
    * Yet, other models directly confront the challenge of intractable partition functions.  
        They use techniques, described below, for training and evaluating models with intractable $$Z$$.  

    __Handling the Partition Function:__{: style="color: red"}  
    There are a few approaches to handle the (intractable) partition function:  
    {: #lst-p}
    1. Estimate the __partition function__ as a *__learned parameter__*; __Noise-Contrastive Estimation__.  
    2. Estimate the *__gradient__* of the partition function directly; __Stochastic MLE__, __Contrastive-Divergence__.  
    3. Avoid computing quantities related to the partition function altogether; __Score Matching__, __Pseudolikelihood__.  
    4. Estimate the __partition function__ (itself) explicitly: __Annealed IS__, __Bridge Sampling__, __Linked IS__.   
    <br>

3. **The Log-Likelihood Gradient:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    __Phase Decomposition of Learning:__{: style="color: red"}  
    Learning using __MLE__ requires computing the gradient of the __NLL__, $$\nabla_{\boldsymbol{\theta}} \log p(\mathbf{x} ; \boldsymbol{\theta})$$.  
    What makes learning undirected models by maximum likelihood particularly difficult is that the __partition function depends on the parameters__; thus, the gradient of the NLL wrt the parameters involves computing the gradient of $$Z(\mathbf{\theta})$$.  
    In __undirected models__, this gradient can be written as:    
    <p>$$\nabla_{\boldsymbol{\theta}} \log p(\mathbf{x} ; \boldsymbol{\theta})=\nabla_{\boldsymbol{\theta}} \log \tilde{p}(\mathbf{x} ; \boldsymbol{\theta})-\nabla_{\boldsymbol{\theta}} \log Z(\boldsymbol{\theta})$$</p>  
    which *__decomposes__* the gradient (learning) into a <span>__positive phase__</span>{: style="color: purple"} and a <span>__negative phase__</span>{: style="color: purple"}.  

    __Difficulties in Learning wrt the Decomposition:__  
    {: #lst-p}
    * __Difficulty in the *Negative* Phase:__  
        \- For most __undirected models__ of interest, the __negative phase__ is *__difficult__* to compute. This is usually due to having to compute the unnormalized probability for __all__ the states.  
        \- __Directed models__ define many "implicit" *__conditional independencies__* between the variables, making it easier to compute the normalization due to many terms canceling out.  
        * __Example - RBMs__:  
            The quintessential example of a model with a straightforward positive phase and a difficult negative phase is the RBM.  
            It has hidden units that are conditionally independent from each other given the visible units.  

        > *__Word2vec__* is another example.  
    * __Difficulty in the *Positive* Phase__:  
        \- Latent Variable Models, generally, have intractable positive phase.  
        \- Models with no latent variables or with few interactions between latent variables typically have a tractable positive phase.  
        * __Example - VAEs__:  
            VAEs define a __continuous__ distribution (over the data) with __latent variable $$z$$__:  
            <p>$$p_{\theta}(x)=\int p_{\theta}(z) p_{\theta}(x \vert z) d z$$</p>  
            which is __intractable__ to compute for every $$z$$.  
            Due to complicated interactions between latent variables, this integral requires exponential time to compute as it needs to be evaluated over all configurations of latent variable.  
            (all $$z_i$$ variables are dependent on each other.)   

    __Positive and Negative Phases:__  
    The terms positive and negative do not refer to the sign of each term in the equation, but rather reflect their effect on the probability density defined by the model.  
    \- The __positive phase__ <span>*__increases__* the probability of training data</span>{: style="color: goldenrod"}  (by reducing the corresponding free energy)  
    \- The __negative phase__ <span>*__decreases__*  the probability of samples generated by the model</span>{: style="color: goldenrod"}.  


    __Monte Carlo Methods for Approximate LL Maximization:__{: style="color: red"}  
    To use MC methods for approximate learning, we need to rewrite the gradient of the partition function $$\nabla_{\boldsymbol{\theta}} \log Z$$ as an expectation of the __unnormalized probability__ $$\tilde{p}$$:  
    <p>$$\nabla_{\boldsymbol{\theta}} \log Z=\mathbb{E}_{\mathbf{x} \sim p(\mathbf{x})} \nabla_{\boldsymbol{\theta}} \log \tilde{p}(\mathbf{x})$$</p>  
    This identity is the basis for a variety of Monte Carlo methods for __approximately maximizing the likelihood__ of models with intractable partition functions.  
    * <button>Derivation - Discrete Variables</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        * Decomposing the gradient of $$\log Z$$:  
            <p>$$\begin{aligned} \nabla_{\boldsymbol{\theta}} \log Z =& \frac{\nabla_{\boldsymbol{\theta}} Z}{Z} \\=& \frac{\nabla_{\boldsymbol{\theta}} \sum_{\mathbf{x}} \tilde{p}(\mathbf{x})}{Z} \\=& \frac{\sum_{\mathbf{x}} \nabla_{\boldsymbol{\theta} \tilde{p}(\mathbf{x})}}{Z} \end{aligned}$$</p>  
        * For models that guarantee $$p(\mathbf{x})>0$$ for all $$\mathbf{x},$$ we can substitute $$\exp (\log \tilde{p}(\mathbf{x}))$$ for $$\tilde{p}(\mathbf{x})$$:  
            <p>$$\begin{aligned} \frac{\sum_{\mathbf{x}} \nabla_{\boldsymbol{\theta}} \exp (\log \tilde{p}(\mathbf{x}))}{Z} &= \frac{\sum_{\mathbf{x}} \exp (\log \tilde{p}(\mathbf{x})) \nabla_{\boldsymbol{\theta}} \log \tilde{p}(\mathbf{x})}{Z} \\ &=\frac{\sum_{\mathbf{x}} \tilde{p}(\mathbf{x}) \nabla_{\boldsymbol{\theta}} \log \tilde{p}(\mathbf{x})}{Z} \\ &=\sum_{\mathbf{x}} p(\mathbf{x}) \nabla_{\boldsymbol{\theta}} \log \tilde{p}(\mathbf{x}) \\ &= \mathbb{E}_{\mathbf{x} \sim p(\mathbf{x})} \nabla_{\boldsymbol{\theta}} \log \tilde{p}(\mathbf{x}) \end{aligned}$$</p>  
        {: hidden=""}

    * <button>Derivation - Continuous Variables</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        * We use __Leibniz's rule for diﬀerentiation under the integral sign__ to obtain the identity:  
            <p>$$\nabla_{\boldsymbol{\theta}} \int \tilde{p}(\mathbf{x}) d \boldsymbol{x}=\int \nabla_{\boldsymbol{\theta}} \tilde{p}(\mathbf{x}) d \boldsymbol{x}$$</p>  
            * __Applicability - Measure Theory:__  
                This identity is applicable only under certain regularity conditions on $$\tilde{p}$$ and $$\nabla_{\boldsymbol{\theta}} \tilde{p}(\mathbf{x})$$.  
                In measure theoretic terms, the conditions are:  
                1. The unnormalized distribution $$\tilde{p}$$ must be a Lebesgue-integrable function of $$\boldsymbol{x}  for every value of $$\boldsymbol{\theta}$$.  
                2. The gradient $$\nabla_{\boldsymbol{\theta}} \tilde{p}(\mathbf{x})$$ must exist for all $$\boldsymbol{\theta}$$ and almost all $$\boldsymbol{x}$$.  
                3. There must exist an integrable function $$R(\boldsymbol{x})$$ that bounds $$\nabla_{\boldsymbol{\theta}} \tilde{p}(\mathbf{x})$$ in the sense that $$\max_{i}\left\vert\frac{\partial}{\partial \theta_{\theta}} \tilde{p}(\mathbf{x})\right\vert \leq R(\boldsymbol{x})$$ for all $$\boldsymbol{\theta}$$ and almost all $$\boldsymbol{x}$$.   

                Fortunately, <span>most machine learning models of interest have these properties.</span>{: style="color: purple"}.  
        {: hidden=""}

    __Intuition:__  
    The Monte Carlo approach to learning provides an intuitive framework in terms of the *__phases__* of the __learning decomposition__:  
    {: #lst-p}
    * __Positive Phase__:  
        In the positive phase, we increase $$\log \tilde{p}(\mathbf{x})$$ for $$\boldsymbol{x}$$ drawn from the data.  
        * __Parametrize $$\log \tilde{p}$$ in terms of an Energy Function__:  
            We interpret the positive phase as <span>__pushing down on the energy__ of training examples</span>{: style="color: purple"}.   
    * __Negative Phase__:  
        In the negative phase, we decrease the partition function by decreasing $$\log \tilde{p}(\mathbf{x})$$ drawn from the model distribution.  
        * __Parametrize $$\log \tilde{p}$$ in terms of an Energy Function__:  
            We interpret the negative phase as <span>__pushing up on the energy__ of samples drawn from the models</span>{: style="color: purple"}.  

    <button>Illustration - Phase Learning</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/HEn1uNFj_rtWwuNKaHdn8DyPvb-SM69ZsL4zwjdXXsU.original.fullsize.png){: width="100%" hidden=""}  
    <br>


4. **Stochastic Maximum Likelihood and Contrastive Divergence:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    To __approximately maximize the log likelihood__, using the identity derived above, we need to use __MCMC__ methods.  

    __Motivation - The Naive Approach:__{: style="color: red"}  
    The naive way to compute the identity above, is to approximate it by __burning in a set of Markov Chains__ from a **_random initialization_** everytime the gradient is needed.  
    When learning is performed using __stochastic gradient descent__, this means <span>the chains must be *__burned in once per gradient step__*</span>{: style="color: purple"}.  
    <button>Naive MCMC Algorithm</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/1pNcMVQ9WFqRWUxnrWlKyHq9GCOpAFUKtQJnxze1MeI.original.fullsize.png){: width="100%" hidden=""}  
    The __high cost of burning in the Markov chains__ in the _inner loop_ makes this procedure __computationally infeasible__.  

    __Learning Intuition (from naive algorithm):__  
    {: #lst-p}
    * We can view the MCMC approach to maximum likelihood as trying to __achieve balance between two forces__:  
        * One <span>__pushing up__ on the model distribution where the data occurs</span>{: style="color: purple"}   
            Corresponds to __maximizing $$\log \tilde{p}$$__.  
        * Another <span>__pushing down__ on the model distribution where the model samples occur</span>{: style="color: purple"}.  
            Corresponds to __minimizing $$\log Z$$__.  
    * There are several __approximations__ to the __negative phase.__  
        Each of these approximations can be understood as making the negative phase __computationally cheaper__ but also making it __push down in the *wrong locations*__.  
    * __Negative Phase Intuition__:  
        * Because the negative phase involves drawing samples from the model’s distribution, we can think of it as <span>finding points that the model believes in strongly</span>{: style="color: purple"}.  
        * Because the negative phase acts to reduce the probability of those points, they are generally considered to <span>represent the model’s incorrect beliefs about the world</span>{: style="color: purple"}.  
            Referred to, in literature, as __“hallucinations”__ or __“fantasy particles”__.  
            * <button>Biological Relation to Dreaming</button>{: .showText value="show" onclick="showTextPopHide(event);"}
                * In fact, the negative phase has been proposed as a possible explanation for dreaming in humans and other animals _(Crick and Mitchison, 1983)_, the idea being that the brain maintains a probabilistic model of the world and follows the gradient of $$\log \tilde{p}$$ when experiencing real events while awake and follows the negative gradient of $$\log \tilde{p}$$ to minimize $$\log Z$$ while sleeping and experiencing events sampled from the current model. This view explains much of the language used to describe algorithms with a positive and a negative phase, but it has not been proved to be correct with neuroscientific experiments.  
                    In machine learning models, it is usually necessary to use the positive and negative phase simultaneously, rather than in separate periods of wakefulness and REM sleep.  
                    As we will see in section 19.5, other machine learning algorithms draw samples from the model distribution for other purposes, and such algorithms could also provide an account for the function of dream sleep.  
                {: hidden=""}

    __Summary:__  
    <div class="borderexample" markdown="1" Style="padding: 0;">
    The main cost of the _naive_ MCMC algorithm is the __cost of burning in the Markov chains from a random initialization at each step__.
    </div>   


    __Contrastive Divergence:__{: style="color: red"}  
    One way to avoid the high cost in Naive MCMC, is to <span>initialize the Markov chains from a distribution that is very close to the model distribution</span>{: style="color: purple"}, so that the burn in operation does not take as many steps.  
    The __Contrastive Divergence (CD)__  (or CD-$$k$$ to indicate CD with $$k$$ Gibbs steps) algorithm initializes the Markov chain at each step with samples from the __data distribution__ _(Hinton, 2000, 2010)_.  
    \- Obtaining samples from the data distribution is _free_, because they are already available in the dataset.  
    \- Initially, the data distribution is not close to the model distribution, so the negative phase is not very accurate.  
    \- Fortunately, the positive phase can still accurately increase the model’s probability of the data.  
    \- After the positive phase has had some time to act, the model distribution is closer to the data distribution, and the negative phase starts to become accurate.  
    <button>Contrastive Divergence Algorithm</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/Tq22qSUmQjXraJOE0tlRAbIrIZdYn-zv8-3bZUrKCi8.original.fullsize.png){: width="100%" hidden=""}  

    __Drawbacks:__  
    {: #lst-p}
    * __Spurious Modes__:  
        Since CD is still an approximation to the correct negative phase, it results in __spurious modes__; i.e. <span>fails to suppress regions of high probability that are far from actual training examples</span>{: style="color: purple"}.  
        __Spurious Modes:__ are those regions that have _high probability under the model_ but _low probability under the data-generating distribution_.  
        <button>Spurious Modes - Illustration</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        ![img](https://cdn.mathpix.com/snip/images/Pcv0tGJ87LYdEOkXI-4Rx37TW7_-WoaeJUj9xjfSZyU.original.fullsize.png){: width="100%" hidden=""}  
        \- Modes in the distribution that are __far from the data distribution__ will *__not be visited__* by Markov chains initialized at _training points_, unless $$k$$ is very large.  
    * __CD as a Biased Estimator in RBMs and Boltzmann Machines:__  
        \- _Carreira-Perpiñan and Hinton (2005)_ showed experimentally that the CD estimator is *__biased__* for __RBMs__ and __fully visible Boltzmann machines__, in that it _converges to different points than the maximum likelihood estimator_.  
        \- They argue that because the bias is *__small__*, CD could be used as an <span>inexpensive way to initialize a model</span>{: style="color: purple"} that could later be fine-tuned via more expensive MCMC methods.  
        * __Interpretation:__ _Bengio and Delalleau (2009)_ show that CD can be interpreted as <span>discarding the smallest terms of the correct MCMC update gradient</span>{: style="color: purple"}, which _explains the bias_.  
    * __Random Gradients__:  
        _Sutskever and Tieleman (2010)_ showed that the CD <span>update direction is not the gradient of any function</span>{: style="color: purple"}.  
        This allows for situations where CD could cycle forever, but in practice this is not a serious problem.  
    * __Difficulty for Deep Models:__  
        * CD is useful for training __shallow models__ like __RBMs__.  
        * The __RBMs__ can be *__stacked__* to __*initialize* deeper models__ like __DBNs__ or __DBMs__.  
        * However, CD does NOT provide much help for training __deeper models__ _directly_.  
            * This is because it is <span>difficult to obtain samples of the hidden units given samples of the visible units</span>{: style="color: purple"}.  
                * Since the hidden units are __not included in the data__, initializing from training points cannot solve the problem.  
                * Even if we initialize the visible units from the data, we will still need to _burn in a Markov chain_ sampling from the distribution over the hidden units conditioned on those visible samples.  


    __Relation to Autoencoder Training:__  
    \- The CD algorithm can be thought of as <span>penalizing the model for having a Markov chain that *__changes the input rapidly__* when the *__input comes from the data__*</span>{: style="color: purple"}.  
    \- This means training with CD somewhat resembles __autoencoder training__.  
    \- Even though CD is more _biased_ than some of the other training methods, it can be useful for __pretraining shallow models__ that will later be __stacked__.  
    {: #lst-p}
    * This is because the <span>earliest models in the stack are encouraged to __copy more information__ up to their __latent variables__</span>{: style="color: purple"}, thereby <span>making it available to the later models</span>{: style="color: purple"}.  
        This should be thought of more as an often-exploitable *__side effect__* of CD training rather than a principled design advantage.  


    __Stochastic Maximum Likelihood (SML) - Persistent Contrastive Divergence (PCD, PCD-$$k$$):__{: style="color: red"}  
    __SML__ AKA __PCD__ is a method that initializes the Markov Chains, in CD, at each gradient step with their <span>states from the *__previous__* gradient step</span>{: style="color: purple"}.  
    This strategy resolves many of the problems with CD.  
    __Idea:__  
    {: #lst-p}
    * The basic idea of this approach is that, as long as the steps taken by the stochastic gradient algorithm are small, the model from the previous step will be similar to the model from the current step.  
    * It follows that the samples from the previous model’s distribution will be very close to being fair samples from the current model’s distribution, so a Markov chain initialized with these samples will not require much time to mix.  
    <button>SML/PCD Algorithm</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/wB9YjPq8Dl4HNJQT-H-G4TBa4h1Uji6nKFe8K6vPtgc.original.fullsize.png){: width="100%" hidden=""}  

    __Advantages:__  
    {: #lst-p}
    * SML is considerably <span>more resistant to forming models with __spurious modes__</span>{: style="color: purple"} than CD is:  
        Because each Markov chain is continually updated throughout the learning process, rather than restarted at each gradient step, the chains are free to wander far enough to find all the model’s modes.  
    * SML is able to <span>train deep models efficiently</span>{: style="color: purple"}:  
        * SML provides an initialization point for both the *__hidden__* and the __*visible* units__:  
            Because it is possible to store the state of all the sampled variables, whether visible or latent.  
        * CD is only able to provide an initialization for the visible units, and therefore requires burn-in for deep models.  
    * __Performance/Results - In-Practice__:  
        _Marlinet al. (2010)_ compared SML to many other criteria presented in this section. They found that:  
        * SML results in the <span>best test set log-likelihood for an __RBM__</span>{: style="color: purple"}, and that 
        * if the RBM’s *__hidden units__* are used as __features__ for an __SVM classifier__, SML results in the <span>best classification accuracy</span>{: style="color: purple"}.  


    __Mixing Evaluation:__  
    <button>Discussion</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/_cahz7TXWFoCdoaiMM2HIkj1xdkm-xzvhcWJXQ7woNs.original.fullsize.png){: width="100%" hidden=""}  

    __Sample Evaluation:__  
    <button>Discussion</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    <div hidden="">Care must be taken when evaluating the samples from a model trained with SML. It is necessary to draw the samples starting from a fresh Markov chain initialized from a random starting point after the model is done training. The samples present in the persistent negative chains used for training have been influenced by several recent versions of the model, and thus can make the model appear to have greater capacity than it actually does.</div>


    __Bias-Variance of CD and SML:__{: style="color: red"}  
    _Berglund and Raiko (2013)_ performed experiments to examine the bias and variance in the *__estimate of the gradient__* provided by CD and SML:  
    {: #lst-p}
    * __CD__ proves to have __*lower* variance__  than the estimator based on exact sampling.  
        The cause of CD's low variance is its use of the same training points in both the positive and negative phase.  
        If the negative phase is initialized from different training points, the variance rises above that of the estimator based on exact sampling.   
    * __SML__ has higher variance.  


    __Improving CD & SML:__{: style="color: red"}  
    {: #lst-p}
    * __MCMC Algorithms__:  
        All these methods based on using MCMC to draw samples from the model canin principle be used with almost any variant of MCMC. This means that techniques such as SML can be improved by using any of the enhanced MCMC techniques described in chapter 17, such as parallel tempering _(Desjardins et al., 2010; Choet al., 2010)_.  
    * __Fast PCD (FPCD)__:  
        Another approach to accelerating mixing during learning relies not on changing the Monte Carlo sampling technology but rather on changing the parametrization of the model and the cost function.  
        __FPCD__ is such a method that involves replacing the parameters $$\boldsymbol{\theta}$$ of a traditional model with an expression:  
        <p>$$\boldsymbol{\theta}=\boldsymbol{\theta}^{(\mathrm{slow})}+\boldsymbol{\theta}^{(\mathrm{fast})}$$</p>  
        <button>Discussion</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        ![img](https://cdn.mathpix.com/snip/images/LM2-pHOcdnMiHYxNHo5Uee7iwKEy__DYiik76SIhymw.original.fullsize.png){: width="100%" hidden=""}  


    __Training with Positive Phase Estimators (bound-based, variational methods):__{: style="color: red"}  
    One key benefit to the MCMC-based methods described in this section is that they provide an estimate of the gradient of $$\log Z,$$ and thus we can essentially decompose the problem into the $$\log \tilde{p}$$ contribution and the $$\log Z$$ contribution.  
    We can then use any other method to tackle $$\log \tilde{p}(\mathbf{x})$$ and just add our negative phase gradient onto the other method’s gradient.  
    In particular, this means that our <span>positive phase can make use of methods that provide only a __lower bound on $$\tilde{p}$$__</span>{: style="color: goldenrod"}.  
    Most of the other methods of dealing with $$\log Z$$ presented in this chapter are incompatible with bound-based positive phase methods.  
    <br>


5. **Pseudolikelihood:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  
    __Motivation:__{: style="color: red"}  
    We can sidestep the issue of approximating the intractable partition function by training the model without computing it at all.  

    __Idea:__{: style="color: red"}  
    Most of these approaches are based on the observation that it is <span>easy to compute *__ratios__* of probabilities in an __undirected model__</span>{: style="color: purple"}.  
    This is because the partition function appears in both the numerator and the denominator of the ratio and cancels out:  
    <p>$$\frac{p(\mathbf{x})}{p(\mathbf{y})}=\frac{\frac{1}{Z} \tilde{p}(\mathbf{x})}{\frac{1}{Z} \tilde{p}(\mathbf{y})}=\frac{\tilde{p}(\mathbf{x})}{\tilde{p}(\mathbf{y})}$$</p>  

    __Pseudolikelihood:__{: style="color: red"}  
    The __Pseudolikelihood__ is an objective function, based on predicting the value of feature $$x _ {i}$$ given all the other features $$\boldsymbol{x}_ {-i}$$:  
    <p>$$\sum_{i=1}^{n} \log p\left(x_{i} \vert \boldsymbol{x}_ {-i}\right)$$</p>  

    __Derivation:__  
    {: #lst-p}
    * The pseudolikelihood is based on the observation that conditional probabilities take this ratio-based form and thus can be computed without knowledge of the partition function.  
    * <button>Derivation</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/u8dif-AW7sUp2ySsRfu3DdAgIe1VSJjept2ielw2PLY.original.fullsize.png){: width="100%" hidden=""}  

    __Computational Cost:__  
    {: #lst-p}
    * If each random variable has $$k$$ different values, this requires only $$k \times n$$ evaluations of $$\tilde{p}$$ to compute,  
    * as opposed to the $$k^{n}$$ evaluations needed to compute the partition function.  

    __Justification:__  
    Estimation by maximizing the pseudolikelihood is __asymptotically consistent__ _(Mase, 1995)_.  
    When the datasets do not approach the large sample limit, pseudolikelihood may display different behavior from the maximum likelihood estimator.  

    __Generalized Pseudolikelihood Estimator:__{: style="color: red"}  
    The __Generalized Pseudolikelihood Estimator__ gives us a way to trade-off computational complexity for deviation from maximum likelihood behavior.  
    The GPE objective function:  
    <p>$$\sum_{i=1}^{m} \log p\left(\mathbf{x}_{\mathbb{S}^{(i)}} \vert \mathbf{x}_{-\mathbb{S}^{(i)}}\right)$$</p>    
    __Complexity-Consistency Tradeoff:__  
    It uses $$m$$ different sets $$\mathbb{S}^{(i)}, i=1, \ldots, m$$ of indices of variables that appear together on the left side of the conditioning bar:  
    {: #lst-p}
    * In the extreme case of $$m=1$$ and $$\mathbb{S}^{(1)}=1, \ldots, n,$$ the generalized pseudolikelihood <span>recovers the log-likelihood</span>{: style="color: purple"}.  
    * In the extreme case of $$m=n$$ and $$\mathbb{S}^{(i)}=\{i\},$$ the generalized pseudolikelihood <span>recovers the pseudolikelihood</span>{: style="color: purple"}.  


    __Performance:__{: style="color: red"}  
    The performance of pseudolikelihood-based approaches depends largely on how the model will be used:  
    {: #lst-p}
    * Pseudolikelihood tends to perform poorly on tasks that require a good model of the full joint $$p(\mathbf{x}),$$ such as density estimation and sampling. 
    * It can perform better than maximum likelihood for tasks that require only the conditional distributions used during training, such as filling in small amounts of missing values.  
    * Generalized pseudolikelihood techniques are especially powerful if the data has regular structure that allows the $$\mathbb{S}$$ index sets to be designed to capture the most important correlations while leaving out groups of variables that have only negligible correlation.  
        For example, in natural images, pixels that are widely separated in space also have weak correlation, so the generalized pseudolikelihood can be applied with each $$\mathbb{S}$$ set being a small, spatially localized window.  

    __Drawbacks - Training with Lower-Bound Maximization Methods:__{: style="color: red"}  
    {: #lst-p}
    * One weakness of the pseudolikelihood estimator is that it cannot be used with other approximations that provide only a lower bound on $$\tilde{p}(\mathbf{x}),$$ e.g. __variational inference__.  
        * This is because $$\tilde{p}$$ appears in the denominator.  
            A lower bound on the denominator provides only an upper bound on the expression as a whole, and there is no benefit to maximizing an upper bound.  
            This makes it difficult to apply pseudolikelihood approaches to deep models such as __deep Boltzmann machines__, since variational methods are one of the dominant approaches to approximately marginalizing out the many layers of hidden variables that interact with each other.  
    * Nonetheless, pseudolikelihood is still useful for deep learning, because it can be used to train single-layer models or deep models using approximate inference methods that are not based on lower bounds.  

    __Pseudolikelihood vs SML/PCD - Computational Cost:__  
    Pseudolikelihood has a much greater cost per gradient step than SML, due to its explicit computation of all the conditionals.  
    But generalized pseudolikelihood and similar criteria can still perform well if only one randomly selected conditional is computed per example _(Goodfellow et al., 2013b)_, thereby bringing the computational cost down to match that of SML.  


    __Relation to the Negative Phase:__{: style="color: red"}  
    Though the pseudolikelihood estimator does not explicitly minimize $$\log Z$$, it can still be thought of as having something resembling a negative phase.  
    The denominators of each conditional distribution result in the learning algorithm suppressing the probability of all states that have only one variable differing from a training example.  

    __Asymptotic Efficiency:__{: style="color: red"}  
    See _Marlin and de Freitas (2011)_ for a theoretical analysis of the asymptotic efficiency of pseudolikelihood.  
    <br>

6. **Score-Matching and Ratio-Matching:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}  
    <button>PDF</button>{: .showText value="show"
     onclick="showTextPopHide(event);"}
    <iframe hidden="" src="/main_files/pdf/score-ratio_matching.pdf" frameborder="0" height="840" width="646" title="Layer Normalization" scrolling="auto"></iframe>

    __Denoising Score Matching:__{: style="color: red"}  
    <button>Denoising Score Matching - Discussion</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/3yUoSuXqxsiW13WrbGbRNpvujyqSAhz5af0MLcXZrX8.original.fullsize.png){: width="100%" hidden=""}  
    <br>

7. **Noise-Contrastive Estimation (NCE):**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}  
    __Noise-Contrastive Estimation (NCE)__ is a method for computing the partition function as a learned parameter in the model; where the probability distribution estimated by the model is represented __explicitly__ as:  
    <p>$$\log p_{\text {model }}(\mathbf{x})=\log \tilde{p}_ {\text {model}}(\mathbf{x} ; \boldsymbol{\theta})+c$$</p>  
    where $$c$$ is explicitly introduced as an approximation of $$-\log Z(\boldsymbol{\theta})$$.  

    Rather than estimating only $$\boldsymbol{\theta}$$, the noise contrastive estimation procedure treats $$c$$ as just another parameter and estimates $$\boldsymbol{\theta}$$ and $$c$$ simultaneously, using the same algorithm for both.  
    The resulting $$\log p_{\text {model}}(\mathbf{x})$$ thus may not correspond exactly to a valid probability distribution, but it will become closer and closer to being valid as the estimate of $$c$$ improves.[^1]  

    __Derivation:__{: style="color: red"}  
    {: #lst-p}
    * __Problem with Maximum Likelihood Criterion:__{: style="color: red"}  
        Such an approach would not be possible using maximum likelihood as the criterion for the estimator.  
        The maximum likelihood criterion would choose to set $$c$$ arbitrarily high, rather than setting $$c$$ to create a valid probability distribution.  
    * __Solution - New Estimator of the original problem:__{: style="color: red"}  
        NCE works by reducing the unsupervised learning problem of estimating $$p(\mathrm{x})$$ to that of learning a probabilistic binary classifier in which one of the categories corresponds to the data generated by the model.  
        This supervised learning problem is constructed in such a way that maximum likelihood estimation defines an *__asymptotically consistent__* estimator of the original problem.  

        Specifically,  
        1. <span>Posit two distributions:</span>{: style="color: goldenrod"} the __model__, and a __noise distribution__.
            * The __Noise Distribution $$p_{\text{noise}}(\mathbf{x})$$:__{: style="color: red"}  
                We introduce a new distribution $$p_{\text{noise}}(\mathbf{x})$$ over the noise.  
                The noise distribution should be __tractable to evaluate and to sample from__.    
        2. <span>Construct a new *__joint model__* over both $$\boldsymbol{x}$$ and a __*binary* variable__ $$y$$</span>{: style="color: goldenrod"}:  
            * We can now construct a model over both $$\mathbf{x}$$ and a new, binary class variable $$y$$. In the new joint model, we specify that  
                (1) $$p_{\mathrm{joint}}(y=1)=\frac{1}{2}$$  
                (2) $$p_{\mathrm{joint}}(\mathbf{x} \vert y=1)=p_{\mathrm{model}}(\mathbf{x})$$  
                (3) $$p_{\mathrm{joint}}(\mathbf{x} \vert y=0)=p_{\mathrm{noise}}(\mathbf{x})$$  
                In other words, $$y$$ is a __switch variable__ that <span>determines whether we will __generate__ $$\mathbf{x}$$ from the *__model__* or from the *__noise distribution__*</span>{: style="color: purple"}.  
            * Equivalently, We can construct a similar __joint model of *training data*__.  
                Formally, 
                (1) $$p_{\text {train}}(y=1)=\frac{1}{2}$$  
                (2) $$p_{\text {train}}(\mathbf{x} \vert y=1)=p_{\text {data }}(\mathbf{x}),$$  
                (3) $$p_{\text {train}}(\mathbf{x} \vert y=0)=p_{\text {noise}}(\mathbf{x})$$  
                In this case, the __switch variable__ <span>determines whether we draw $$\mathbf{x}$$ from the *__data__* or from the *__noise distribution__*</span>{: style="color: purple"}.  
        3. <span>Construct the new supervised Binary Classification Task</span>{: style="color: goldenrod"} - __fitting $$p_{\text {joint}}$$ to $$p_{\text {train}}$$__:  
            We can now just use standard maximum likelihood learning on the supervised learning problem of fitting $$p_{\text {joint}}$$ to $$p_{\text {train}}$$, by swapping $$p_{\text {model}}$$ with $$p_{\text {joint}}$$:  
            <p>$$\boldsymbol{\theta}, c=\underset{\boldsymbol{\theta}, c}{\arg \max } \mathbb{E}_{\mathbf{x}, \mathbf{y} \sim p_{\text {train}}} \log p_{\text {joint}}(y \vert \mathbf{x})$$</p>  
            * __Expanding $$p_{\text{joint}}(y \vert x)$$:__  
                The distribution $$p_{\text{joint}}$$ is essentially a *__logistic regression__* model applied to the difference in log probabilities of the model and the noise distribution:  
                <p>$$\begin{aligned}  
                    p_{\text {joint}}(y=1 \vert \mathbf{x}) &= \frac{p_{\text {model }}(\mathbf{x})}{p_{\text {model }}(\mathbf{x})+p_{\text {noise}}(\mathbf{x})} \\
                    &= \frac{1}{1+\frac{p_{\text {noise}}(\mathbf{x})}{p_{\text {model}} (\mathbf{x})}}  \\
                    &= \frac{1}{1+\exp \left(\log \frac{p_{\text {noise}}(\mathbf{x})}{p_{\text {model }}(\mathbf{x})}\right)} \\
                    &= \sigma\left(-\log \frac{p_{\text {noise}}(\mathbf{x})}{p_{\text {model }}(\mathbf{x})}\right) \\
                    &= \sigma\left(\log p_{\text {model }}(\mathbf{x})-\log p_{\text {noise}}(\mathbf{x})\right) 
                    \end{aligned}$$</p>     
    * <button>Different Derivation</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        ![img](https://cdn.mathpix.com/snip/images/xhM0Q_ZbT3N-zobKCCyKe2mFA3OAyDatXGYFkok0H3Q.original.fullsize.png){: width="100%" hidden=""}  

    __Summary:__  
    {: #lst-p}
    1. <span>Posit two distributions:</span>{: style="color: goldenrod"} the __model__, and a __noise distribution__.
    2. Given a data point, <span>predict from which distribution this point was generated</span>{: style="color: goldenrod"}.  

    NCE is thus simple to apply as long as  $$ \log \tilde{p}_{\text {model}}$$ is easy to back-propagate through, and, as specified above, $$p_{\text {noise}}$$ is easy to evaluate (in order to evaluate $$p_{\text {joint}}$$ and sample from (to generate the training data).  

    __The Noise Distribution:__{: style="color: red"}  
    {: #lst-p}
    * __Practical Implications and Complexity__:  
    * __Better Distributions - Parametric $$p_{\text{noise}}$$__:  
        The noise distribution is generally __non-parametric__.  
        However, there is nothing stopping us from evolving this distribution and giving it trainable parameters, then updating these parameters such that it generates increasingly __"optimal"__ samples.  
        * __Optimality__:  
            Of course, we would have to design what __"optimal"__ means.  
            * __Adversarial Contrastive Estimation__:  
                One interesting approach is called [Adversarial Contrastive Estimation](https://arxiv.org/abs/1805.03642), wherein the authors adapt the noise distribution to generate increasingly "harder negative examples, which forces the main model to learn a better representation of the data.  


    __Weaknesses/Drawbacks:__{: style="color: red"}  
    {: #lst-p}
    * __Problems with Many RVs:__  
        When NCE is applied to problems with many random variables, it becomes __less efficient__.  
        * The logistic regression classifier can reject a noise sample by identifying any one variable whose value is unlikely.  
            This means that learning slows down greatly after $$p_{\text {model}}$$ has learned the basic marginal statistics.  
        * Imagine learning a model of images of faces, using unstructured Gaussian noise as $$p_{\text {noise}}$$.  
            If $$p_{\text {model }}$$ learns about eyes, it can reject almost all unstructured noise samples without having learned anything about other facial features, such as mouths.  
    * __Noise Distribution Complexity__:  
        The constraint that $$p_{\text {noise}}$$ must be easy to evaluate and easy to sample from can be overly restrictive:  
        * For our __training data__, we <span>require the ability to sample from our noise distribution.</span>{: style="color: purple"}.  
        * For our __target__, we <span>require the ability to compute the likelihood of some data under our noise distribution</span>{: style="color: purple"}.  

        When $$p_{\text {noise}}$$ is simple, most samples are likely to be too obviously distinct from the data to force $$p_{\text {model}}$$ to improve noticeably.  
    * __Training with Lower-Bound Maximizing Methods__:  
        NCE does not work if only a lower bound on $$\tilde{p}$$ is available.  
        Such a lower bound could be used to construct a lower bound on $$p_{\text {joint}}(y=1 \vert \mathbf{x}),$$ but it can only be used to construct an upper bound on $$p_{\text {joint}}(y=0 \vert \mathbf{x}),$$ which appears in half the terms of the NCE objective.  
        Likewise, a lower bound on $$p_{\text {noise}}$$ is not useful, because it provides only an upper bound on $$p_{\text {joint}}(y=1 \vert \mathbf{x})$$.  


    __Self-Contrastive Estimation:__{: style="color: red"}  
    When the model distribution is copied to define a new noise distribution before each gradient step, NCE defines a procedure called __self-contrastive estimation__, whose <span>expected gradient is equivalent to the expected gradient of maximum likelihood</span>{: style="color: purple"} _(Goodfellow, 2014)_.  
    __Interpretation:__  
    {: #lst-p}
    * __Self-Contrastive Estimation__:  
        The special case of NCE where the noise samples are those generated by the model suggests that maximum likelihood can be interpreted as a <span>procedure that forces a model to constantly learn to __distinguish__ *__reality__* from its __own evolving *beliefs*__</span>{: style="color: goldenrod"},   
    * __NCE__:  
        However, NCE achieves some __reduced computational cost__ by <span>only forcing the model to __distinguish__ *__reality__* from a *__fixed baseline (noise model)__*</span>{: style="color: goldenrod"}.  


    __Connection to Importance Sampling:__{: style="color: red"}  
    _Jozefowicz et al. (2016)_ show that NCE and IS are not only similar as both are sampling-based approaches, but are strongly connected.  
    While NCE uses a binary classification task, they show that IS can be described similarly using a __surrogate loss function__: Instead of performing binary classification with a logistic loss function like NCE, IS then optimises a multi-class classification problem with a softmax and cross-entropy loss function.  
    They observe that as IS performs *__multi-class classification__*, it may be a better choice for __language modeling__, as the loss leads to <span>tied updates between the data and noise samples</span>{: style="color: purple"} rather than <span>independent updates</span>{: style="color: purple"} as with NCE.  
    Indeed, Jozefowicz et al. (2016) use IS for language modeling and obtain state-of-the-art performance on the 1B Word benchmark.  


    __Relation to Generative Adversarial Networks (GANs):__{: style="color: red"}  
    Noise contrastive estimation is based on the idea that a <span>good generative model should be able to __distinguish data from noise__</span>{: style="color: purple"}.  
    A closely related idea is that a <span>good generative model should be able to __generate samples that no classifier can distinguish from data__</span>{: style="color: purple"}.  
    This idea yields generative adversarial networks.  

    __Self-Normalization:__{: style="color: red"}  
    _Mnih and Teh (2012)_ and _Vaswani et al. (2013)_ fix $$c = 1$$.  
    They report does not affect the model's performance.  
    This assumption has the nice side-effect of __reducing the model's parameters__, while ensuring that the model *__self-normalises__* by not depending on the explicit normalisation in $$c$$.  
    Indeed, _Zoph et al. (2016)_ find that even when learned, $$c$$ is close to $$1$$ and has low variance.  
    <br>

8. **Negative Sampling:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18}  
    __Negative Sampling (NEG)__ can be seen as an approximation to __NCE__.  
    As we have mentioned above, NCE can be shown to approximate the loss of $$\log p_{\text{model}}$$ as the number of samples $$k$$ increase.  
    NEG simplifies NCE and does away with this guarantee, as the objective of NEG is to learn high-quality word representations rather than achieving low perplexity on a test set, as is the goal in language modeling.  

    The key difference to NCE is that NEG only approximates this probability by making it as easy to compute as possible.  
    It simplifies NCE as follows:  
    {: #lst-p}
    1. Considers noise distributions whose likelihood we cannot evaluate  
    2. To accommodate, it simply set the most expensive term $$p_{\text {noise}}(x)=1$$  
        Equivalently, $$k\:p_{\text {noise}}(x)=1$$  
        * <button>Derivation - Discrete Variables</button>{: .showText value="show" onclick="showTextPopHide(event);"}  
            * Thus, __Expanding $$p_{\text{joint}}(y \vert x)$$:__  
                The distribution $$p_{\text{joint}}$$ is essentially a *__logistic regression__* model applied to the difference in log probabilities of the model and the noise distribution:  
                <p>$$\begin{aligned}  
                    p_{\text {joint}}(y=1 \vert \mathbf{x}) &= \frac{p_{\text {model }}(\mathbf{x})}{p_{\text {model }}(\mathbf{x})+p_{\text {noise}}(\mathbf{x})} \\
                    &= \frac{1}{1+\frac{p_{\text {noise}}(\mathbf{x})}{p_{\text {model}} (\mathbf{x})}}  \\
                    &= \frac{1}{1+\exp \left(\log \frac{p_{\text {noise}}(\mathbf{x})}{p_{\text {model }}(\mathbf{x})}\right)} \\
                    &= \sigma\left(-\log \frac{p_{\text {noise}}(\mathbf{x})}{p_{\text {model }}(\mathbf{x})}\right) \\
                    &= \sigma\left(-\log \frac{1}{p_{\text {model}}(\mathbf{x})}\right) \\
                    &= \sigma\left(\log p_{\text {model}}(\mathbf{x})\right) 
                    \end{aligned}$$</p>  
            {: hidden=""}  

    __Equivalence with NCE:__{: style="color: red"}  
    {: #lst-p}
    * $$k p_{\text {noise}}=1$$ is exactly then true, when (discrete):  
        1. $$k=\vert X\vert$$ and  
        2. $$p_{\text {noise}}$$ is a __*uniform* distribution__.  
        
        In this case, NEG is equivalent to NCE.  
    * The reason we set $$k p_{\text {noise}}=1$$ and not to some other constant can be seen by rewriting the equation, as $$P(y=1 \vert  \mathbf{x})$$ can simplify the sigmoid function.  
    * In all other cases, NEG only approximates NCE, which means that it will <span>not directly optimize the likelihood $$\log p_{\text {model}}(\mathbf{x})$$</span>{: style="color: purple"}.  
    * __Asymptotic Consistency:__  
        Since NEG only approximates NCE, it lacks any asymptotic consistency guarantees.  

    __Application - Language Modeling and Word Embeddings:__  
    NEG only approximates NCE, which means that it will not directly optimise the likelihood of correct words, which is key for language modelling. While NEG may thus be useful for learning word embeddings, its lack of asymptotic consistency guarantees makes it inappropriate for language modelling.  
    <br>

9. **Self-Normalization:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents19}  
    Remember from NCE that we decomposed the log likelihood of the model as:  
    <p>$$\log p_{\text {model }}(\mathbf{x})=\log \tilde{p}_ {\text {model}}(\mathbf{x} ; \boldsymbol{\theta})+c$$</p>  
    where $$c$$ is explicitly introduced as an approximation of $$-\log Z(\boldsymbol{\theta})$$.  

    If we are able to constrain our model so that it sets $$c=0$$ (i.e. $$e^c = 1$$), then we can avoid computing the normalization in $$c$$ altogether.  
    _Devlin et al. (2014)_ thus propose to add a __squared error penalty__ term to the loss function that encourages the model to <span>keep $$c$$ as close as possible to $$0$$</span>{: style="color: purple"}:  
    <p>$$\tilde{J} = J + \lambda (c-0)^{2}$$</p>  
    where $$\lambda$$ allows us to trade-off between model accuracy and mean self-normalisation.  

    At inference time, we set  
    <p>$$p_{\text {model }}(\mathbf{x})=\dfrac{\tilde{p}_ {\text {model}}(\mathbf{x} ; \boldsymbol{\theta})}{Z(\boldsymbol{\theta})} \approx \dfrac{\tilde{p}_ {\text {model}}(\mathbf{x} ; \boldsymbol{\theta})}{1} = \tilde{p}_ {\text {model}}(\mathbf{x} ; \boldsymbol{\theta})$$</p>  

    __Results - MT:__{: style="color: red"}  
    They report that self-normalisation achieves a speed-up factor of about 15, while only resulting in a small degradation of BLEU scores compared to a regular non-self-normalizing neural language model.  

    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * [Paper repro: “Self-Normalizing Neural Networks” (Blog - Code?)](https://becominghuman.ai/paper-repro-self-normalizing-neural-networks-84d7df676902)  
    <br>


***

<!-- ## SECOND
{: #content2}

1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}
2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}
3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}
4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}
5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25} -->

***

## Estimating the Partition Function
{: #content3}

1. **Estimating the Partition Function:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}  
    <button>PDF</button>{: .showText value="show"
     onclick="showTextPopHide(event);"}
    <iframe hidden="" src="/main_files/pdf/approx_part.pdf" frameborder="0" height="840" width="646" title="Layer Normalization" scrolling="auto"></iframe>

2. **Annealed Importance Sampling (AIS):**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}  
    <button>PDF</button>{: .showText value="show"
     onclick="showTextPopHide(event);"}
    <iframe hidden="" src="/main_files/pdf/ais.pdf" frameborder="0" height="840" width="646" title="Layer Normalization" scrolling="auto"></iframe>

3. **Bridge Sampling:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}  
    <button>PDF</button>{: .showText value="show"
     onclick="showTextPopHide(event);"}
    <iframe hidden="" src="/main_files/pdf/bs.pdf" frameborder="0" height="840" width="646" title="Layer Normalization" scrolling="auto"></iframe>

4. **Linked Importance Sampling (LIS):**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents34}  
    <button>PDF</button>{: .showText value="show"
     onclick="showTextPopHide(event);"}
    <iframe hidden="" src="/main_files/pdf/lis.pdf" frameborder="0" height="840" width="646" title="Layer Normalization" scrolling="auto"></iframe>

5. **Estimating the Partition Function while Training:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents35}  
    <button>PDF</button>{: .showText value="show"
     onclick="showTextPopHide(event);"}
    <iframe hidden="" src="/main_files/pdf/est_training.pdf" frameborder="0" height="840" width="646" title="Layer Normalization" scrolling="auto"></iframe>


[^1]: NCE is also applicable to problems with a tractable partition function, where there is no need to introduce the extra parameter $$c$$. However, it has generated the most interest as a means of estimating models with difficult partition functions.  