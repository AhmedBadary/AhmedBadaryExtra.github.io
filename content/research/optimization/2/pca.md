---
layout: NotesPage
title: PCA <br /> Principle Compnent Analysis
permalink: /work_files/research/conv_opt/pca_opt
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

## PCA
{: #content1}

1. **What?**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents11}
    :   It is a statistical procedure that uses an orthogonal transformation to convert a set of observations of possibly correlated variables into a set of values of linearly uncorrelated variables called principal components.

2. **Goal?**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents12}
    :   Given points $$ \in \mathbf{R}^d$$, find k-directions that capture most of the variation.

3. **Why?**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents13}
    :   1. Find a small basis for representing variations in complex things.
            > e.g. faces, genes.
        2. Reducing the number of dimensions makes some computations cheaper.
        3. Remove irrelevant dimensions to reduce overfitting in learnging algorithms.
            > Like "_subset selection_" but the features are __not__ _axis aligned_.  
            > They are linear combinations of input features.

4. **Finding Principle Components:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents14} \\
    * Let '$$X$$' be an $$(n \times d)$$ design matrix, centered, with mean $$\hat{x} = 0$$.
    * Let '$$w$$' be a unit vector.
    * The _Orthogonal Projection_ of the point '$$x$$' onto '$$w$$' is $$\tilde{x} = (x.w)w$$.
        > Or $$\tilde{x} = \dfrac{x.w}{\|w\|_2^2}w$$, if $$w$$ is not a unit vector.
    * Let '$$X^TX$$' be the _sample covariance matrix_,  
        $$0 \leq \lambda_1 \leq \lambda_2 \leq \cdots \leq \lambda_d$$ be its eigenvalues  and let $$v_1, v_2, \cdots, v_d$$ be the corresponding _Orthogonal Unit Eigen-vectors_.
    * Given _Orthonormal directions (vectors)_ $$v_1, v_2, \ldots, v_k$$, we can write:   

        $$\tilde{x} = \sum_{i=1}^k (x.v_i)v_i.$$  

    > **The Principle Components:** are precisely the eigenvectors of the data's covariance matrix. 

5. **Total Variance and Error Measurement:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents15} 
    :    * **The Total Variance** of the data can be expressed as the sum of all the eigenvalues:
    :   $$
        \mathbf{Tr} \Sigma = \mathbf{Tr} (U \Lambda U^T) = \mathbf{Tr} (U^T U \Lambda) = \mathbf{Tr} \Lambda = \lambda_1 + \ldots + \lambda_n. 
        $$
    :    * **The Total Variance** of the **_Projected_** data is:
    :   $$
         \mathbf{Tr} (P \Sigma P^T ) = \lambda_1 + \lambda_2 + \cdots + \lambda_k. 
        $$
    :    * **The Error in the Projection** could be measured with respect to variance.
            * We define the **ratio of variance** "explained" by the projected data as:
    :   $$
        \dfrac{\lambda_1 + \ldots + \lambda_k}{\lambda_1 + \ldots + \lambda_n}. 
        $$
    :   > If the ratio is _high_, we can say that much of the variation in the data can be observed on the projected plane.

***

## Derivation 1. Fitting Gaussians to Data with MLE
{: #content2}

1. **What?**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents21}
    1. Fit a Gaussian to data with MLE
    2. Choose k Gaussian axes of greatest variance.
    > Notice: MLE estimates a _covariance matrix_; $$\hat{\Sigma} = \dfrac{1}{n}X^TX$$.

2. **Algorithm:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents22} \\
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

1. **What?**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents31} \\
    1. Find a direction '$$w$$' that maximizes the variance of the projected data.
    2. Maximize the variance

2. **Derivation:**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents32}
    :   $$\max_{w : \|w\|_2=1} \: Var(\left\{\tilde{x_1}, \tilde{x_2}, \cdots, \tilde{x_n} \right\})$$
    :   $$
        \begin{align}
        & \ = \max_{w : \|w\|_2=1}  \dfrac{1}{n} \sum_{i=1}{n}(x_i.\dfrac{w}{\|w\|})^2 \\
        & \ = \max_{w : \|w\|_2=1}  \dfrac{1}{n} \dfrac{\|xw\|^2}{\|w\|^2} \\
        & \ = \max_{w : \|w\|_2=1}  \dfrac{1}{n} \dfrac{w^TX^TXw}{w^Tw}
        \end{align}
        $$
    :   Where $$\dfrac{1}{n}\dfrac{w^TX^TXw}{w^Tw}$$ is the **_Rayleigh Quotient_**.
    :   For any Eigen-vector $$v_i$$, the _Rayleigh Quotient_ is $$ = \lambda_i$$.
    :   $$\implies$$ the vector $$v_d$$ with the largest $$\lambda_d$$, achieves the maximum variance: $$\dfrac{\lambda_d}{n}.$$
    :   Thus, the maximum of the _Rayleigh Quotient_ is achieved at the Eigen-vector that has the highest correpsonding Eigen-value.
    :   We find subsequent vectors by finding the next biggest $$\lambda_i$$ and choosing its corresponding Eigen-vector.

3. **Another Derivation from Statistics:**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents33}
    :   The data matrix has points $$x_i$$; its component along a proposed axis $$u$$ is $$(x · u)$$.
    :   The variance of this is $$E(x · u − E(x · u))^2$$
    :   and the optimization problem is
    :   $$
        \begin{align}
        \max_{x : \|x\|_2=1} \: E(x · u − E(x · u))^2 & \\
        & \ = \max_{u : \|u\|_2=1} \:  E[(u \cdot (x − Ex))^2] \\
        & \ = \max_{u : \|u\|_2=1} \:  uE[(x − Ex) \cdot (x − Ex)^T]u \\
        & \ = \max_{u : \|u\|_2=1} \:  u^T \Sigma u
        \end{align}
        $$
    :   where the matrix $${\displaystyle \Sigma \:= \dfrac{1}{n} \sum_{j=1}^n (x_j-\hat{x})(x_j-\hat{x})^T}.$$
    :   Since $$\Sigma$$ is symmetric, the $$u$$ that gives the maximum value to $$u^T\Sigma u$$ is the eigenvector of $$\Sigma$$ with the largest eigenvalue.
    :   The second and subsequent principal component axes are the other eigenvectors sorted by eigenvalue.

***

## Derivation 3. Minimize Projection Error
{: #content4}

1. **What?**{: style="color: SteelBlue  "}{: .bodyContents4 #bodyContents41} \\
    1. Find direction '$$w$$' that minimizes the _Projection Error_.

2. **Derivation:**{: style="color: SteelBlue  "}{: .bodyContents4 #bodyContents42}
    :   $$
        \begin{align}
        \min_{\tilde{x} : \|\tilde{x}\|_2 = 1} \; \sum_{i=1}^n \|x_i - \tilde{x_i}\|^2 & \\
        & \ = \min_{w : \|w\|_2 = 1} \; \sum_{i=1}^n \|x_i -\dfrac{x_i \cdot w}{\|w\|_2^2}w\|^2 \\
        & \ = \min_{w : \|w\|_2 = 1} \; \sum_{i=1}^n \left[\|x_i\|^2 - (x_i \cdot \dfrac{w}{\|w\|_2})^2\right] \\
        & \ = \min_{w : \|w\|_2 = 1} \; c - n*\sum_{i=1}^n(x_i \cdot \dfrac{w}{\|w\|_2})^2 \\
        & \ = \min_{w : \|w\|_2 = 1} \; c - n*Var(\left\{\tilde{x_1}, \tilde{x_2}, \cdots, \tilde{x_n} \right\}) \\
        & \ = \max_{w : \|w\|_2 = 1} \; Var(\left\{\tilde{x_1}, \tilde{x_2}, \cdots, \tilde{x_n} \right\})
        \end{align}
        $$
    :   Thus, minimizing projection error is equivalent to maximizing variance.
