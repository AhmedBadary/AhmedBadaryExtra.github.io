---
layout: NotesPage
title: PCA <br /> Principal Component Analysis
permalink: /work_files/research/conv_opt/pca
prevLink: /work_files/research/conv_opt
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [PCA](#content1)
  {: .TOC1}
  * [Derivation 1. Fitting Gaussians to Data with MLE](#content2)
  {: .TOC2}
  * [Derivation 2. Minimizing Variance](#content3)
  {: .TOC3}
  * [Derivation 3. Minimize Projection Error](#content4)
  {: .TOC4}
</div>

***
***

[Visual of PCA, SVD](https://www.youtube.com/watch?v=5HNr_j6LmPc)  
[Derivation - Direction of Maximum Variance](https://www.youtube.com/watch?v=Axs-fuFJVvE)  
[Low-Rank Approximation w/ SVD (code, my github)](https://github.com/AhmedBadary/Statistical-Analysis/blob/master/Image%20Compression%20using%20Low-Rank%20Approximation%20(SVD).ipynb)  
[PPCA - Probabilistic PCA Slides](https://people.cs.pitt.edu/~milos/courses/cs3750-Fall2007/lectures/class17.pdf)  



## PCA
{: #content1}

1. **What?**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}    
    It is a statistical procedure that uses an orthogonal transformation to convert a set of observations of possibly correlated variables into a set of values of linearly uncorrelated variables called principal components.  
    <br>

2. **Goal?**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}    
    Given points $$\mathbf{x}_ i \in \mathbf{R}^d$$, find k-directions that capture most of the variation.  
    <br>

3. **Why?**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}    
    1. Find a small basis for representing variations in complex things.
        > e.g. faces, genes.  

    2. Reducing the number of dimensions makes some computations cheaper.  
    3. Remove irrelevant dimensions to reduce over-fitting in learning algorithms.
        > Like "_subset selection_" but the features are __not__ _axis aligned_.  
        > They are linear combinations of input features.  

    4. Represent the data with fewer parameters (dimensions)  
    <br>

4. **Finding Principal Components:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}   
    * Let '$$X$$' be an $$(n \times d)$$ design matrix, centered, with mean $$\hat{x} = 0$$.
    * Let '$$w$$' be a unit vector.
    * The _Orthogonal Projection_ of the point '$$x$$' onto '$$w$$' is $$\tilde{x} = (x.w)w$$.
        > Or $$\tilde{x} = \dfrac{x.w}{\|w\|_2^2}w$$, if $$w$$ is not a unit vector.
    * Let '$$X^TX$$' be the _sample covariance matrix_,  
        $$0 \leq \lambda_1 \leq \lambda_2 \leq \cdots \leq \lambda_d$$ be its eigenvalues  and let $$v_1, v_2, \cdots, v_d$$ be the corresponding _Orthogonal Unit Eigen-vectors_.
    * Given _Orthonormal directions (vectors)_ $$v_1, v_2, \ldots, v_k$$, we can write:   

        $$\tilde{x} = \sum_{i=1}^k (x.v_i)v_i.$$  

    > **The Principal Components:** are precisely the eigenvectors of the data's covariance matrix. [Read More](#pcvspd)  

    <br>

5. **Total Variance and Error Measurement:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}   
    * **The Total Variance** of the data can be expressed as the sum of all the eigenvalues:
    <p>$$
        \mathbf{Tr} \Sigma = \mathbf{Tr} (U \Lambda U^T) = \mathbf{Tr} (U^T U \Lambda) = \mathbf{Tr} \Lambda = \lambda_1 + \ldots + \lambda_n. 
        $$</p>
    * **The Total Variance** of the **_Projected_** data is:
    <p>$$
         \mathbf{Tr} (P \Sigma P^T ) = \lambda_1 + \lambda_2 + \cdots + \lambda_k. 
        $$</p>
    * **The Error in the Projection** could be measured with respect to variance.
        * We define the **ratio of variance** "explained" by the projected data (equivalently, the ratio of information _"retained"_) as:  
    <p>$$
        \dfrac{\lambda_1 + \ldots + \lambda_k}{\lambda_1 + \ldots + \lambda_n}. 
        $$</p>  
    > If the ratio is _high_, we can say that much of the variation in the data can be observed on the projected plane.  

    <br>

8. **Mathematical Formulation:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18}  
    PCA is mathematically defined as an orthogonal linear transformation that transforms the data to a new coordinate system such that the greatest variance by some projection of the data comes to lie on the first coordinate (called the first principal component), the second greatest variance on the second coordinate, and so on.  

    Consider a data matrix, $$X$$, with column-wise zero empirical mean (the sample mean of each column has been shifted to zero), where each of the $$n$$ rows represents a different repetition of the experiment, and each of the $$p$$ columns gives a particular kind of feature (say, the results from a particular sensor).  

    Mathematically, the transformation is defined by a set of $$p$$-dimensional vectors of weights or coefficients $${\displaystyle \mathbf {v}_ {(k)}=(v_{1},\dots ,v_{p})_ {(k)}}$$ that map each row vector $${\displaystyle \mathbf {x}_ {(i)}}$$ of $$X$$ to a new vector of principal component scores $${\displaystyle \mathbf {t} _{(i)}=(t_{1},\dots ,t_{l})_ {(i)}}$$, given by:  
    <p>$${\displaystyle {t_{k}}_{(i)}=\mathbf {x}_ {(i)}\cdot \mathbf {v}_ {(k)}\qquad \mathrm {for} \qquad i=1,\dots ,n\qquad k=1,\dots ,l}$$</p>  
    in such a way that the individual variables $${\displaystyle t_{1},\dots ,t_{l}}$$  of $$t$$ considered over the data set successively inherit the maximum possible variance from $$X$$, with each coefficient vector $$v$$ constrained to be a unit vector (where $$l$$ is usually selected to be less than $${\displaystyle p}$$ to reduce dimensionality).  
    
    __The Procedure and what it does:__{: style="color: red"}  
    {: #lst-p}
    * Finds a lower dimensional subspace (PCs) that Minimizes the RSS of projection errors  
    * Produces a vector (1st PC) with the highest possible variance, each succeeding component in turn has the highest variance possible under the constraint that it is orthogonal to the preceding components.  
    * Results in an __uncorrelated orthogonal basis set__.  
    * PCA constructs new axes that point to the directions of maximal variance (in the original variable space)  
    <br>


9. **Intuition:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents19}   
    PCA can be thought of as fitting a p-dimensional ellipsoid to the data, where each axis of the ellipsoid represents a principal component. If some axis of the ellipsoid is small, then the variance along that axis is also small, and by omitting that axis and its corresponding principal component from our representation of the dataset, we lose only a commensurately small amount of information.  

    * Its operation can be thought of as revealing the internal structure of the data in a way that best explains the variance in the data.  
    <br>

11. **PCA Algorithm:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents111}   
    * __Data Preprocessing__:  
        * Training set: $$x^{(1)}, x^{(2)}, \ldots, x^{(m)}$$ 
        * Preprocessing (__feature scaling__ + __mean normalization__):  
            * __mean normalization__:  
                $$\mu_{j}=\frac{1}{m} \sum_{i=1}^{m} x_{j}^{(i)}$$  
                Replace each $$x_{j}^{(i)}$$ with $$x_j^{(i)} - \mu_j$$  
            * __feature scaling__:  
                If different features on different, scale features to have comparable range  
                $$s_j = S.D(X_j)$$ (the standard deviation of feature $$j$$)  
                Replace each $$x_{j}^{(i)}$$ with $$\dfrac{x_j^{(i)} - \mu_j}{s_j}$$    
    * __Computing the Principal Components__:  
        * Compute the __SVD__ of the matrix $$X = U S V^T$$  
        * Compute the Principal Components:  
            <p>$$T = US = XV$$</p>  
            > Note: The $$j$$-th principal component is: $$Xv_j$$  
        * Choose the top $$k$$ components singular values in $$S = S_k$$  
        * Compute the Truncated Principal Components:  
            <p>$$T_k = US_k$$</p>  
    * __Computing the Low-rank Approximation Matrix $$X_k$$__:  
        * Compute the reconstruction matrix:  
            <p>$$X_k = T_kV^T = US_kV^T$$</p>  
    <br>        
    
    __Results and Definitions:__{: style="color: red"}  
    {: #lst-p}
    * Columns of $$V$$ are principal directions/axes  
    * Columns of $$US$$ are principal components ("scores")
    * [Principal Components ("scores") VS Principal Directions/Axes](https://stats.stackexchange.com/questions/174601/difference-between-principal-directions-and-principal-component-scores-in-the-co){: #pcvspd}  

    > __NOTE:__ the analysis above is valid only for (1) $$X$$ w/ samples in rows and variables in columns  (2) $$X$$ is centered (mean=0)  
    <br>

10. **Properties and Limitations:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents110}   
    __Limitations:__{: style="color: red"}  
    * PCA is highly sensitive to the (relative) scaling of the data; no consensus on best scaling.  
    <br>
            

12. **Optimality:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents112}       
    Optimal for Finding a lower dimensional subspace (PCs) that Minimizes the RSS of projection errors  
    <br>

6. **How does PCA relate to CCA:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}   
    __CCA__ defines coordinate systems that optimally describe the cross-covariance between two datasets while __PCA__ defines a new orthogonal coordinate system that optimally describes variance in a single dataset.  
    <br>

7. **How does PCA relate to ICA:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}   
    __Independent component analysis (ICA)__ is directed to similar problems as principal component analysis, but finds additively separable components rather than successive approximations.  
    <br>


13. **What's the difference between PCA estimate and OLS estimate:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents113}   
    

__Notes:__{: style="color: red"}  
{: #lst-p}
* __Variance__ is the _measure of spread_ along only *__one axis__*   
* __SVD(X) vs Spectral-Decomposition($$\Sigma = X^TX$$)__:  
    SVD is better $$\iff$$ more numerically stable $$iff$$ faster  
* __When are the PCs *independent*?__  
    Assuming that the dataset is Gaussian distributed would guarantee that the PCs are independent. [Discussion](https://datascience.stackexchange.com/questions/25789/why-does-pca-assume-gaussian-distribution)   


***

## Derivation 1. Fitting Gaussians to Data with MLE
{: #content2}

[Three Derivations of Principal Components (concise)](http://scribblethink.org/Work/PCAderivations/PCAderivations.pdf)  
[Better Derivations (longer)](https://www.stat.cmu.edu/~cshalizi/uADA/12/lectures/ch18.pdf)  


1. **What?**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    1. Fit a Gaussian to data with MLE
    2. Choose k Gaussian axes of greatest variance.
    > Notice: MLE estimates a _covariance matrix_; $$\hat{\Sigma} = \dfrac{1}{n}X^TX$$.

2. **Algorithm:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}   
    1. Center $$X$$
    2. Normalize $$X$$.
        > Optional. Should only be done if the units of measurement of the features differ.
    3. Compute the unit Eigen-values and Eigen-vectors of $$X^TX$$
    4. Choose '$$k$$' based on the Eigenvalue sizes
        > Optional. Top to bottom.
    5. For the best k-dim subspace, pick Eigenvectors $$v_{d-k+1}, \cdots, v_d$$.
    6. Compute the coordinates '$$x.v_i$$' of the trainning/test data in PC-Space.

***

## Derivation 2. Maximizing Variance
{: #content3}

1. **What?**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}   
    1. Find a direction '$$w$$' that maximizes the variance of the projected data.
    2. Maximize the variance

2. **Derivation:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}  
    :   $$\max_{w : \|w\|_2=1} \: Var(\left\{\tilde{x_1}, \tilde{x_2}, \cdots, \tilde{x_n} \right\})$$
    :   $$
        \begin{align}
        & \ = \max_{w : \|w\|_2=1}  \dfrac{1}{n} \sum_{i=1}^{n}(x_i.\dfrac{w}{\|w\|})^2 \\
        & \ = \max_{w : \|w\|_2=1}  \dfrac{1}{n} \dfrac{\|xw\|^2}{\|w\|^2}  \\
        & \ = \max_{w : \|w\|_2=1}  \dfrac{1}{n} \dfrac{w^TX^TXw}{w^Tw} \\
        \end{align}
        $$
    :   where $$\dfrac{1}{n}\dfrac{w^TX^TXw}{w^Tw}$$ is the **_Rayleigh Quotient_**.
    :   For any Eigen-vector $$v_i$$, the _Rayleigh Quotient_ is $$ = \lambda_i$$.
    :   $$\implies$$ the vector $$v_d$$ with the largest $$\lambda_d$$, achieves the maximum variance: $$\dfrac{\lambda_d}{n}.$$
    :   Thus, the maximum of the _Rayleigh Quotient_ is achieved at the Eigenvector that has the highest corresponding Eigenvalue.
    :   We find subsequent vectors by finding the next biggest $$\lambda_i$$ and choosing its corresponding Eigenvector.

    * [**Full Derivation**](https://www.youtube.com/embed/Axs-fuFJVvE){: value="show" onclick="iframePopA(event)"}
    <a href="https://www.youtube.com/embed/Axs-fuFJVvE"></a>
        <div markdown="1"> </div>    
    <br>

3. **Another Derivation from Statistics:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}  
    First, we note that, The sample variance along direction $$u$$ can be expressed as a quadratic form in $$u$$:  
    <p>$$ \sigma^2(u) = \dfrac{1}{n} \sum_{k=1}^n [u^T(x_k-\hat{x})]^2 = u^T \Sigma u,$$</p>  

    The data matrix has points $$x_i$$; its component along a proposed axis $$u$$ is $$(x · u)$$.  
    The variance of this is $$E(x · u − E(x · u))^2$$  
    and the optimization problem is
    <p>$$
        \begin{align}
        \max_{x : \|x\|_2=1} \: E(x · u − E(x · u))^2 & \\
        & \ = \max_{u : \|u\|_2=1} \:  E[(u \cdot (x − Ex))^2] \\
        & \ = \max_{u : \|u\|_2=1} \:  uE[(x − Ex) \cdot (x − Ex)^T]u \\
        & \ = \max_{u : \|u\|_2=1} \:  u^T \Sigma u
        \end{align}
        $$</p>
    where the matrix $${\displaystyle \Sigma \:= \dfrac{1}{n} \sum_{j=1}^n (x_j-\hat{x})(x_j-\hat{x})^T}.$$  
    Since $$\Sigma$$ is symmetric, the $$u$$ that gives the maximum value to $$u^T\Sigma u$$ is the eigenvector of $$\Sigma$$ with the largest eigenvalue.  
    The second and subsequent principal component axes are the other eigenvectors sorted by eigenvalue.  

    __Proof of variance along a direction:__{: style="color: red"}  
    <p>$$\boldsymbol{u}^{\top} \operatorname{cov}(\boldsymbol{X}) \boldsymbol{u}=\boldsymbol{u}^{\top} \mathbb{E}\left[(\boldsymbol{X}-\mathbb{E}(\boldsymbol{X}))(\boldsymbol{X}-\mathbb{E}(\boldsymbol{X}))^{\top}\right] \boldsymbol{u}=\mathbb{E}\left[\langle\boldsymbol{u}, \boldsymbol{X}-\mathbb{E}(\boldsymbol{X})\rangle^{2}\right] \geq 0 \\ \implies \\ 
    \operatorname{var}(\langle\boldsymbol{u}, \boldsymbol{X}\rangle)=\mathbb{E}\left[\langle\boldsymbol{u}, \boldsymbol{X}-\mathbb{E} \boldsymbol{X}\rangle^{2}\right]=\boldsymbol{u}^{\top} \operatorname{cov}(\boldsymbol{X}) \boldsymbol{u}$$</p>  

    * [PCA and Covariance Matrices (paper)](http://www.cs.columbia.edu/~djhsu/AML/lectures/notes-pca.pdf)  

***

## Derivation 3. Minimize Projection Error
{: #content4}

1. **What?**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents41}   
    1. Find direction '$$w$$' that minimizes the _Projection Error_.

2. **Derivation:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents42}  
    <p>$$
        \begin{align}
        \min_{\tilde{x} : \|\tilde{x}\|_2 = 1} \; \sum_{i=1}^n \|x_i - \tilde{x_i}\|^2 & \\
        & \ = \min_{w : \|w\|_2 = 1} \; \sum_{i=1}^n \|x_i -\dfrac{x_i \cdot w}{\|w\|_2^2}w\|^2 \\
        & \ = \min_{w : \|w\|_2 = 1} \; \sum_{i=1}^n \left[\|x_i\|^2 - (x_i \cdot \dfrac{w}{\|w\|_2})^2\right] \\
        & \ = \min_{w : \|w\|_2 = 1} \; c - n*\sum_{i=1}^n(x_i \cdot \dfrac{w}{\|w\|_2})^2 \\
        & \ = \min_{w : \|w\|_2 = 1} \; c - n*Var(\left\{\tilde{x_1}, \tilde{x_2}, \cdots, \tilde{x_n} \right\}) \\
        & \ = \max_{w : \|w\|_2 = 1} \; Var(\left\{\tilde{x_1}, \tilde{x_2}, \cdots, \tilde{x_n} \right\})
        \end{align}
        $$</p>  
    Thus, minimizing projection error is equivalent to maximizing variance.  
