---
layout: NotesPage
title: Latent Variable Models
permalink: /work_files/research/dl/archits/latent_variable_models
prevLink: /work_files/research/dl/archits.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Latent Variable Models](#content1)
  {: .TOC1}
  * [Linear Factor Models](#content2)
  {: .TOC2}
  <!-- * [THIRD](#content3)
  {: .TOC3} -->
</div>

***
***


* [OneTab](https://www.one-tab.com/page/ZBsF69s-QzOY6Eb5uDha_Q)  
* [ICA (Stanford Notes)](http://cs229.stanford.edu/notes/cs229-notes11.pdf)  
* [Deep ICA (+code)](https://towardsdatascience.com/deep-independent-component-analysis-in-tensorflow-manual-back-prop-in-tf-94602a08b13f)  



## Latent Variable Models
{: #content1}

1. **Latent Variable Models:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    __Latent Variable Models__ are statistical models that relate a set of observable variables (so-called manifest variables) to a set of latent variables.  

    __Core Assumption - Local Independence:__{: style="color: red"}  
    __Local Independence:__  
    The observed items are conditionally independent of each other given an individual score on the latent variable(s). This means that the latent variable *__explains__* why the observed items are related to another.  

    In other words, the targets/labels on the observations are the result of an individual's position on the latent variable(s), and that the observations have nothing in common after controlling for the latent variable.  

    <p>$$p(A,B\vert z) = p(A\vert z) \times (B\vert z)$$</p>  


    <button>Example of Local Independence</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/wnxPRKkVBA88V1k3i4HdWBTtn0NQFBi5gdNkTLcCeFk.original.fullsize.png){: width="100%" hidden=""}  


    __Methods for inferring Latent Variables:__{: style="color: red"}  
    <button>Show List</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
    * Hidden Markov models (HMMs)
    * Factor analysis
    * Principal component analysis (PCA)
    * Partial least squares regression
    * Latent semantic analysis and probabilistic latent semantic analysis
    * EM algorithms
    * Pseudo-Marginal Metropolis-Hastings algorithm
    * Bayesian Methods: LDA  
    {: hidden=""}



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
    <br>


<!-- 2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}
3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}
4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}
5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}
6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}
7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}
8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18} -->

***

## Linear Factor Models
{: #content2}

1. **Linear Factor Models:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    __Linear Factor Models__ are *__generative models__* that are the simplest class of *__latent variable models__*[^1].  
    A linear factor model is defined by the use of a *__stochastic__*, *__linear__* __decoder__ function that <span>*generates* $$\boldsymbol{x}$$ by adding __noise__ to a __linear transformation__ of $$\boldsymbol{h}$$</span>{: style="color: goldenrod"}.  


    __Applications/Motivation:__{: style="color: red"}  
    {: #lst-p}
    * Building blocks of __mixture models__ _(Hinton et al., 1995a; Ghahramani and Hinton, 1996; Roweis et al., 2002)_   
    * Building blocks of larger, __deep probabilistic models__ _(Tang et al., 2012)_  
    * They also show many of the basic approaches necessary to build __generative models__ that the more advanced deep models will extend further.  
    * These models are interesting because they allow us to discover explanatory factors that have a simple joint distribution.  
    * The simplicity of using a __linear decoder__ made these models some of the first latent variable models to be extensively studied.  

    __LFTs as Generative Models:__{: style="color: red"}  
    Linear factor models are some of the simplest __generative models__ and some of the simplest models that <span>learn a __representation__ of data</span>{: style="color: purple"}.  

    __Data Generation Process:__{: style="color: DarkRed"}    
    A linear factor model describes the data generation process as follows:  
    {: #lst-p}
    1. __Sample__ the *__explanatory factors__* $$\boldsymbol{h}$$ from a __distribution__:  
        <p>$$\mathbf{h} \sim p(\boldsymbol{h}) \tag{1}$$</p>  
        where $$p(\boldsymbol{h})$$ is a factorial distribution, with $$p(\boldsymbol{h})=\prod_{i} p\left(h_{i}\right),$$ so that it is easy to sample from.  
    2. __Sample__ the *real-valued* *__observable variables__* *given* the __factors__:  
        <p>$$\boldsymbol{x}=\boldsymbol{W} \boldsymbol{h}+\boldsymbol{b}+ \text{ noise} \tag{2}$$</p>  
        where the noise is typically __Gaussian__ and __diagonal__ (independent across dimensions).  

    <button>Illustration</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/rrWlVKLy8vrKZTdgB-eLoAFHVMFAc39GG7nXAO80a3Q.original.fullsize.png){: width="100%" hidden=""}<br>

2. **Factor Analysis:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}  
    __Probabilistic PCA (principal components analysis)__, __Factor Analysis__ and other __linear factor models__ are special cases of the above equations (1 and 2) and only differ in the choices made for the *__noise distribution__* and the model’s *__prior over latent variables__* $$\boldsymbol{h}$$ before observing $$\boldsymbol{x}$$.  

    __Factor Analysis:__{: style="color: red"}  
    In __factor analysis__ *(Bartholomew, 1987; Basilevsky, 1994)*, the *__latent variable prior__* is just the <span>__unit variance Gaussian__</span>{: style="color: purple"}:  
    <p>$$\mathbf{h} \sim \mathcal{N}(\boldsymbol{h} ; \mathbf{0}, \boldsymbol{I})$$</p>  
    while the __observed variables__ $$x_i$$ are assumed to be *__conditionally independent__*, given $$\boldsymbol{h}$$.  
    Specifically, the *__noise__* is assumed to be drawn from a <span>__diagonal covariance Gaussian distribution__</span>{: style="color: purple"}, with covariance matrix $$\boldsymbol{\psi}=\operatorname{diag}\left(\boldsymbol{\sigma}^{2}\right),$$ with $$\boldsymbol{\sigma}^{2}=\left[\sigma_{1}^{2}, \sigma_{2}^{2}, \ldots, \sigma_{n}^{2}\right]^{\top}$$ a vector of <span>*__per-variable__* __variances__</span>{: style="color: purple"}.  

    The _**role**_ of the __latent variables__ is thus to <span>capture the *__dependencies__* between the different observed variables $$x_i$$</span>{: style="color: purple"}.  
    Indeed, it can easily be shown that $$\boldsymbol{x}$$ is just a <span>__multivariate normal random variable__</span>{: style="color: purple"}, with:   
    <p>$$\mathbf{x} \sim \mathcal{N}\left(\boldsymbol{x} ; \boldsymbol{b}, \boldsymbol{W} \boldsymbol{W}^{\top}+\boldsymbol{\psi}\right)$$</p>  


3. **Probabilistic PCA:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}  
    __Probabilistic PCA (principal components analysis)__, __Factor Analysis__ and other __linear factor models__ are special cases of the above equations (1 and 2) and only differ in the choices made for the *__noise distribution__* and the model’s *__prior over latent variables__* $$\boldsymbol{h}$$ before observing $$\boldsymbol{x}$$.  

    * <button>__Motivation__</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        * Addresses limitations of regular PCA
        * PCA can be used as a general Gaussian density model in addition to reducing dimensions
        * Maximum-likelihood estimates can be computed for elements associated with principal components
        * Captures dominant correlations with few parameters     
        * Multiple PCA models can be combined as a probabilistic mixture
        * Can be used as a base for Bayesian PCA  
        {: hidden=""}

    __Probabilistic PCA:__{: style="color: red"}  
    In order to _cast_ __PCA__ in a *__probabilistic framework__*, we can make a slight _modification_ to the __factor analysis model__, making the __conditional variances__ $$\sigma_i^2$$ <span>equal to each other</span>{: style="color: purple"}.  
    In that case the covariance of $$\boldsymbol{x}$$ is just $$\boldsymbol{W} \boldsymbol{W}^{\top}+\sigma^{2} \boldsymbol{I}$$, where $$\sigma^2$$ is now a __scalar__.  
    This yields the __conditional distribution__:  
    <p>$$\mathbf{x} \sim \mathcal{N}\left(\boldsymbol{x} ; \boldsymbol{b}, \boldsymbol{W} \boldsymbol{W}^{\top}+\sigma^{2} \boldsymbol{I}\right)$$</p>  
    or, equivalently,  
    <p>$$\mathbf{x}=\boldsymbol{W} \mathbf{h}+\boldsymbol{b}+\sigma \mathbf{z}$$</p>  
    where $$\mathbf{z} \sim \mathcal{N}(\boldsymbol{z} ; \mathbf{0}, \boldsymbol{I})$$ is __Gaussian noise__.  

    Notice that $$\boldsymbol{b}$$ is the <span>__mean__ value (over all data) on the directions that are not captured/represented</span>{: style="color: purple"}.  

    This probabilistic PCA model takes advantage of the observation that <span>most variations in the data can be captured by the latent variables $$\boldsymbol{h},$$ up to some small residual</span>{: style="color: goldenrod"} <span>__reconstruction error__</span>{: style="color: goldenrod"} $$\sigma^2$$.   
    
    __Learning (parameter estimation):__{: style="color: DarkRed"}  
    _Tipping and Bishop (1999)_ then show an *__iterative__* __EM__ algorithm for estimating the parameters $$\boldsymbol{W}$$ and $$\sigma^{2}$$.  

    __Relation to PCA - Limit Analysis:__{: style="color: DarkRed"}  
    _Tipping and Bishop (1999)_ show that probabilistic PCA becomes $$\mathrm{PCA}$$ as $$\sigma \rightarrow 0$$.  
    In that case, the conditional expected value of $$\boldsymbol{h}$$ given $$\boldsymbol{x}$$ becomes an orthogonal projection of $$\boldsymbol{x} - \boldsymbol{b}$$  onto the space spanned by the $$d$$ columns of $$\boldsymbol{W}$$, like in PCA.  

    As $$\sigma \rightarrow 0,$$ the density model defined by probabilistic PCA becomes very sharp around these $$d$$ dimensions spanned by the columns of $$\boldsymbol{W}$$.  
    This can make the model assign very low likelihood to the data if the data does not actually cluster near a hyperplane.  


    __PPCA vs Factor Analysis:__{: style="color: red"}  
    {: #lst-p}
    * Covariance
        * __PPCA__ (& PCA) is covariant under rotation of the original data axes
        * __Factor analysis__ is covariant under component-wise rescaling
    * Principal components (or factors)
        * __PPCA__: different principal components (axes) can be found incrementally
        * __Factor analysis__: factors from a two-factor model may not correspond to those from a one-factor model


    __Manifold Interpretation of PCA:__{: style="color: red"}  
    Linear factor models including PCA and factor analysis can be interpreted as <span>learning a __manifold__</span>{: style="color: goldenrod"} _(Hinton et al., 1997)_.  
    We can view __PPCA__ as <span>defining a __thin pancake-shaped region of high probability__</span>{: style="color: purple"}—a __Gaussian distribution__ that is very narrow along some axes, just as a pancake is very flat along its vertical axis, but is elongated along other axes, just as a pancake is wide along its horizontal axes.  
    <button>Illustration</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/ayo7yf-CBpBA38gdTlc0sCPWk9gG0PhFSpXzfSOp1HU.original.fullsize.png){: width="100%" hidden=""}  
    __PCA__ can be interpreted as <span>aligning this pancake with a linear manifold in a higher-dimensional space</span>{: style="color: goldenrod"}.  
    This interpretation applies not just to traditional PCA but also to any __linear autoencoder__ that learns matrices $$\boldsymbol{W}$$ and $$\boldsymbol{V}$$ with the goal of making the reconstruction of $$x$$ lie as close to $$x$$ as possible:  
    {: #lst-p}
    * Let the __Encoder__ be:  
        <p>$$\boldsymbol{h}=f(\boldsymbol{x})=\boldsymbol{W}^{\top}(\boldsymbol{x}-\boldsymbol{\mu})$$</p>  
        The encoder computes a __low-dimensional representation__ of $$h$$.  
    * With the __autoencoder view__, we have a __decoder__ computing the *__reconstruction__*:  
        <p>$$\hat{\boldsymbol{x}}=g(\boldsymbol{h})=\boldsymbol{b}+\boldsymbol{V} \boldsymbol{h}$$</p>  
    * The choices of linear encoder and decoder that minimize __reconstruction error__:  
        <p>$$\mathbb{E}\left[\|\boldsymbol{x}-\hat{\boldsymbol{x}}\|^{2}\right]$$</p>  
        correspond to $$\boldsymbol{V}=\boldsymbol{W}, \boldsymbol{\mu}=\boldsymbol{b}=\mathbb{E}[\boldsymbol{x}]$$ and the columns of $$\boldsymbol{W}$$ form an orthonormal basis which spans the same subspace as the principal eigenvectors of the covariance matrix:  
        <p>$$\boldsymbol{C}=\mathbb{E}\left[(\boldsymbol{x}-\boldsymbol{\mu})(\boldsymbol{x}-\boldsymbol{\mu})^{\top}\right]$$</p>  
    * In the case of PCA, the columns of $$\boldsymbol{W}$$ are these eigenvectors, ordered by the magnitude of the corresponding eigenvalues (which are all real and non-negative).  
    * __Variances:__  
        One can also show that eigenvalue $$\lambda_{i}$$ of $$\boldsymbol{C}$$ corresponds to the variance of $$x$$ in the direction of eigenvector $$\boldsymbol{v}^{(i)}$$.  
    * __Optimal Reconstruction:__  
        * If $$\boldsymbol{x} \in \mathbb{R}^{D}$$ and $$\boldsymbol{h} \in \mathbb{R}^{d}$$ with $$d<D$$, then the <span>__*optimal*__ __reconstruction error__</span>{: style="color: goldenrod"}  (choosing $$\mu, b, V$$ and $$W$ as above) is:  
            <p>$$\min \mathbb{E}\left[\|\boldsymbol{x}-\hat{\boldsymbol{x}}\|^{2}\right]=\sum_{i=d+1}^{D} \lambda_{i}$$</p>  
        * Hence, if the __covariance__ has *__rank__* $$d,$$ the __eigenvalues__ $$\lambda_{d+1}$$ to $$\lambda_{D}$$ are $$0$$ and __reconstruction error__ is $$0$.  
        * Furthermore, one can also show that the above solution can be obtained by <span>__*maximizing* the variances of the elements__ of $$\boldsymbol{h},$$ under *orthogonal* $$\boldsymbol{W}$$</span>{: style="color: purple"}, instead of *__minimizing reconstruction error__*.  



    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * [PPCA - Probabilistic PCA Slides](https://people.cs.pitt.edu/~milos/courses/cs3750-Fall2007/lectures/class17.pdf)  /  [PPCA Better Slides](https://www.cs.ubc.ca/~schmidtm/Courses/540-W16/L12.pdf)  
    * [Probabilistic PCA (Original Paper!)](http://www.robots.ox.ac.uk/~cvrg/hilary2006/ppca.pdf)  
    * EM Algorithm for PCA is more advantageous than MLE (closed form).  
    * __Mixtures of probabilistic PCAs__: can be defined and are a combination of local probabilistic PCA models.  
    * PCA can be generalized to the __nonlinear Autoencoders__.  
    * ICA can be generalized to a __nonlinear generative model__, in which we use a nonlinear function $$f$$ to generate the observed data.  
    <br>

4. **Independent Component Analysis (ICA):**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}  

5. **Slow Feature Analysis:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}

6. **Sparse Coding:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents26}  
    __Sparse Coding__ _(Olshausen and Field, 1996)_ is a *__linear factor model__* that has been heavily studied as an <span>unsupervised feature learning</span>{: style="color: purple"} and <span>feature extraction</span>{: style="color: purple"} mechanism.  
    In Sparse Coding the *__noise distribution__* is <span>__Gaussian noise__</span>{: style="color: purple"} with <span>isotropic precision</span>{: style="color: purple"} $$\beta$$:  
    <p>$$p(\boldsymbol{x} \vert \boldsymbol{h})=\mathcal{N}\left(\boldsymbol{x} ; \boldsymbol{W} \boldsymbol{h}+\boldsymbol{b}, \frac{1}{\beta} \boldsymbol{I}\right)$$</p>  

    The *__latent variable prior__* $$p(\boldsymbol{h})$$ is chosen to be one with sharp peaks near $$0$$.  
    Common choices include:  
    {: #lst-p}
    * __factorized Laplace__:  
        <p>$$p\left(h_{i}\right)=$ Laplace $\left(h_{i} ; 0, \frac{2}{\lambda}\right)=\frac{\lambda}{4} e^{-\frac{1}{2} \lambda\left|h_{i}\right|}$$</p>  
    * __factorized Student-t distributions__:  
        <p>$$p\left(h_{i}\right) \propto \frac{1}{\left(1+\frac{h_{i}^{2}}{\nu}\right)^{\frac{\nu+1}{2}}}$$</p>  
    * __Cauchy__  

    __Learning/Training:__{: style="color: red"}  
    {: #lst-p}
    * Training sparse coding with __maximum likelihood__ is __*intractable*__{: style="color: purple"}.  
    * Instead, the training _alternates_ between <span>__encoding__ the data</span>{: style="color: purple"} and <span>training the decoder to __better reconstruct the data__ given the encoding</span>{: style="color: purple"}.  
        This is a [principled approximation to Maximum-Likelihood](/work_files/research/dl/concepts/inference#bodyContents15map_sc).  
        * Minimization wrt. $$\boldsymbol{h}$$ 
        * Minimization wrt. $$\boldsymbol{W}$$ 

    __Architecture:__{: style="color: red"}  
    {: #lst-p}
    * __Encoder__:  
        * <span>Non-parametric</span>{: style="color: purple"}.  
        * It is an <span>optimization algorithm</span>{: style="color: goldenrod"} that solves an __optimization problem__ in which we seek the <span>*__single most likely code value__*</span>{: style="color: purple"}:  
            <p>$$\boldsymbol{h}^{* }=f(\boldsymbol{x})=\underset{\boldsymbol{h}}{\arg \max } p(\boldsymbol{h} vert \boldsymbol{x})$$</p>   
            * Assuming a __Laplace Prior__ on $$p(\boldsymbol{h})$$:  
                <p>$$\boldsymbol{h}^{* }=\underset{h}{\arg \min } \lambda\|\boldsymbol{h}\|_{1}+\beta\|\boldsymbol{x}-\boldsymbol{W h}\|_{2}^{2}$$</p>  
                where we have taken a log, dropped terms not depending on $$\boldsymbol{h}$$, and divided by positive scaling factors to simplify the equation.  
            * __Hyperparameters:__  
                Both $$\beta$$ and $$\lambda$$ are hyperparameters.  
                However, $$\beta$$ is usually set to $$1$$ because its role is shared with $$\lambda$$.  
                It could also be treated as a parameter of the model and _"learned"_[^2].  


    __Variations:__{: style="color: red"}  
    Not all approaches to sparse coding explicitly build a $$p(\boldsymbol{h})$$ and a $$p(\boldsymbol{x} \vert \boldsymbol{h})$$.  
    Often we are just interested in learning a dictionary of features with activation values that will often be zero when extracted using this inference procedure.  


    __Sparsity:__{: style="color: red"}  
    {: #lst-p}
    * Due to the imposition of an $$L^{1}$$ norm on $$\boldsymbol{h},$$ this procedure will yield a sparse $$\boldsymbol{h}^{* }$$.  
    * If we sample $$\boldsymbol{h}$$ from a Laplace prior, it is in fact a <span>zero probability event</span>{: style="color: purple"} for an element of $$\boldsymbol{h}$$ to actually be zero.  
        <span>The __generative model__ itself is *__not__* especially __sparse__, *__only__* the __feature extractor__ is</span>{: style="color: purple"}.  
        * _Goodfellow et al. (2013d)_ describe approximate inference in a different model family, the spike and slab sparse coding model, for which samples from the prior usually contain true zeros.  


    __Properties:__{: style="color: red"}  
    {: #lst-p}
    * <span>__Advantages:__</span>{: style="color: purple"}  
        * The sparse coding approach combined with the use of the *__non-parametric__* __encoder__  can in principle minimize the combination of reconstruction error and log-prior better than any specific parametric encoder.  
        * Another advantage is that there is no generalization error to the encoder.  
            Thus, resulting in better generalization when sparse coding is used as a feature extractor for a classifier than when a parametric function is used to predict the code.  
            * A parametric encoder must learn how to map $$\boldsymbol{x}$$ to $$\boldsymbol{h}$$ in a way that generalizes. For unusual $$\boldsymbol{x}$$ that do not resemble the training data, a learned, parametric encoder may fail to find an $$\boldsymbol{h}$$ that results in accurate reconstruction or a sparse code.  
            * For the vast majority of formulations of sparse coding models, where the inference problem is convex, the optimization procedure will always find the optimal code (unless degenerate cases such as replicated weight vectors occur).  
            * Obviously, the sparsity and reconstruction costs can still rise on unfamiliar points, but this is due to generalization error in the decoder weights, rather than generalization error in the encoder.  
            * Thus, the lack of generalization error in sparse coding’s optimization-based encoding process may result in better generalization when sparse coding is used as a feature extractor for a classifier than when a parametric function is used to predict the code.  
                <button>Results</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
                * _Coates and Ng (2011)_ demonstrated that sparse coding features generalize better for object recognition tasks than the features of a related model based on a parametric encoder, the linear-sigmoid autoencoder.  
                * _Goodfellow et al. (2013d)_ showed that a variant of sparse coding generalizes better than other feature extractors in the regime where extremely few labels are available (twenty or fewer labels per class).  
                {: hidden=""}
    * <span>__Disadvantages:__</span>{: style="color: purple"}  
        * The primary disadvantage of the __*non-parametric* encoder__ is that it requires greater time to compute $$\boldsymbol{h}$$ given $$\boldsymbol{x}$$ because the non-parametric approach requires running an iterative algorithm.  
            * The parametric autoencoder approach uses only a fixed number of layers, often only one.  
        * It is not straight-forward to back-propagate through the non-parametric encoder: which makes it difficult to pretrain a sparse coding model with an unsupervised criterion and then fine-tune it using a supervised criterion.  
            * Modified versions of sparse coding that permit approximate derivatives do exist but are not widely used _(Bagnell and Bradley, 2009)_.  

    __Generation (Sampling):__{: style="color: red"}  
    {: #lst-p}
    * Sparse coding, like other linear factor models, often produces poor samples.  
        <button>Examples</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        ![img](https://cdn.mathpix.com/snip/images/dnnZUyAMmMg__pGi1O1os8yQXGUu0lY3LcpuWtWKTok.original.fullsize.png){: width="100%" hidden=""}  
    * This happens even when the model is able to reconstruct the data well and provide useful features for a classifier.  
        * The __reason__ is that <span>each individual feature may be learned well</span>{: style="color: purple"}, but the <span>__factorial prior__ on the __hidden code__ results in the model including __*random* subsets__ of __*all*__ of the __features__ in each generated sample</span>{: style="color: goldenrod"}.  
    * __Motivating Deep Models:__{: style="color: red"}  
        This motivates the development of deeper models that can <span>impose a __non-factorial distribution__ on the *__deepest code layer__*</span>{: style="color: goldenrod"}, as well as the development of more sophisticated shallow models.  

    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * [Sparse Coding (Hugo Larochelle!)](https://www.youtube.com/watch?v=7a0_iEruGoM&list=PL6Xpj9I5qXYEcOhn7TqghAJ6NAPrNmUBH&index=60)  
    <br>


<!-- 7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents27}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents28} -->

<!-- 

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
*** 
-->
[^1]: __Probabilistic Models__, with __latent variables__.  
[^2]: some terms depending on $$\beta$$ omitted from above equation\* which are needed to learn $$\beta$$.  