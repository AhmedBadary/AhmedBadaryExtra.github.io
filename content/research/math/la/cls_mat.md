---
layout: NotesPage
title: Classes of Matrices
permalink: /work_files/research/la/cls_mat
prevLink: /work_files/research/la.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Diagonal Matrices](#content1)
  {: .TOC1} 
  * [Symmetric Matrices](#content2)
  {: .TOC2}
  * [Skew-Symmetric Matrices](#content3)
  {: .TOC3}
  * [Covariance Matrices](#content4)
  {: .TOC4}
  * [Positive Semi-Definite Matrices](#content5)
  {: .TOC5}
  * [Positive Definite Matrices](#content6)
  {: .TOC6}
  * [Orthogonal Matrices](#content7)
  {: .TOC7}
  * [Dyads](#content8)
  {: .TOC8}
  * [Correlation Matrices](#content9)
  {: .TOC9}
</div>

***
***

[Special Matrices in ML](https://medium.com/@jonathan_hui/machine-learning-linear-algebra-special-matrices-c750cd742dfe)   
[Matrix Cookbook](https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf)  



## Diagonal Matrices
{: #content1}

1. **Definition.**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    **Diagonal matrices** are square matrices $$A$$ with $$A_{ij} = 0 \text{, when } i \ne j.$$  
    <br>

2. **Properties:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    1. Diagonal matrices correspond to quadratic functions that are simple sums of squares, of the form:  
        <p>$$q(x) = \sum_{i=1}^n \lambda_i x_i^2 = x^T \mathbf{diag}(\lambda) x.$$</p>  
    2. They are easy to invert $$A^{-1}_ {ii} = 1/A_ {ii} \: \forall i \in [1, n]$$  
    3. The __pseudo-inverse__ is easy to compute: keep zero diagonal elements as zero  
    4. Allow easier matrix multiplication and powers  
    <br>


***

## Symmetric Matrices
{: #content2}

1. **Definition:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}    
    **Symmetric matrices** are square matrices that satisfy $$A_{ij} = A_{ji}$$ for every pair $$(i,j).$$  

    **The set of symmetric** $$(n \times n)$$ matrices is denoted $$\mathbf{S}^n$$. This set is a subspace of $$\mathbf{R}^{n \times n}$$.  
    <br>

2. **Properties:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}    
    * Has __orthonormal__ eigenvectors (even with repeated eigenvalues) 
    * Its inverse is also symmetric
    * All eigenvalues of a symmetric matrix are __real__ 
    * $$A^TA$$ is __invertible__ iff columns of $$A$$ are linearly independent  
    * Every symmetric matrix $$S$$ can be diagonalized (factorized) with $$Q$$ formed by the orthonormal eigenvectors $$v_i$$ of $$S$$ and $$\Lambda$$ is a diagonal matrix holding all the eigenvalues:  
        <p>$$\begin{aligned} S&=Q \Lambda Q^{T} \\
            &= \lambda_{1} v_{1} v_{1}^{T}+\ldots+\lambda_{n} v_{n} v_{h}^{T} = \sum_{i=1}^n \lambda_i v_i v_i^T
            \end{aligned}$$</p>  
    * One can create a symmetric matrix from any matrix by:  
        <p>$$M = {\displaystyle {\tfrac {1}{2}}\left(A+A^{\textsf {T}}\right)}$$</p>  
    <br>

3. **Examples:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}   
    1. [**Representation of a weighted, undirected graph.**](http://livebooklabs.com/keeppies/c5a5868ce26b8125/3c5245ebb8a556da){: value="show" onclick="iframePopA(event)"}
        <a href="http://livebooklabs.com/keeppies/c5a5868ce26b8125/73a4ae787085d554">` Visit the Book`</a>
        <div markdown="1"> </div>

    2. [**Laplacian matrix of a graph.**](http://livebooklabs.com/keeppies/c5a5868ce26b8125/0e696ef8a78e090c){: value="show" onclick="iframePopA(event)"}
        <a href="http://livebooklabs.com/keeppies/c5a5868ce26b8125/73a4ae787085d554">` Visit the Book`</a>
        <div markdown="1"> </div>
    3. [**Hessian of a function.**](http://livebooklabs.com/keeppies/c5a5868ce26b8125/6c0afdfbf11892c6){: value="show" onclick="iframePopA(event)"}
        <a href="http://livebooklabs.com/keeppies/c5a5868ce26b8125/73a4ae787085d554">` Visit the Book`</a>
        <div markdown="1"> </div>
    4. [**Gram matrix of data points.**](http://livebooklabs.com/keeppies/c5a5868ce26b8125/e236418f4e2d6b3b){: value="show" onclick="iframePopA(event)"}
        <a href="http://livebooklabs.com/keeppies/c5a5868ce26b8125/73a4ae787085d554">` Visit the Book`</a>
        <div markdown="1"> </div>
    <br>

*** 

## Skew-Symmetric Matrices
{: #content3}

1. **Definition.**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}  

2. **Properties:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}   

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}   

***

## Covariance Matrices
{: #content4}

1. **Definition.**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents41}   
    **Standard Form:**  
    <p>$$\Sigma :=\mathrm {E} \left[\left(\mathbf {X} -\mathrm {E} [\mathbf {X} ]\right)\left(\mathbf {X} -\mathrm {E} [\mathbf {X} ]\right)^{\rm {T}}\right]$$</p>  
    <p>$$ \Sigma := \dfrac{1}{m} \sum_{k=1}^m (x_k - \hat{x})(x_k - \hat{x})^T. $$</p>  


    **Matrix Form:**  
    <p>$$ \Sigma := \dfrac{X^TX}{n} $$</p>  

    > valid only for (1) $$X$$ w/ samples in rows and variables in columns  (2) $$X$$ is centered (mean=0)  



2. **Properties:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents42}   
    1. The sample covariance matrix allows to find the variance along any direction in data space.

    2. The diagonal elements of $$\Sigma$$ give the variances of each vector in the data.

    3. The trace of $$\Sigma$$ gives the sum of all the variances.

    4. The matrix $$\Sigma$$ is positive semi-definite, since the associated quadratic form $$u \rightarrow u^T \Sigma u$$ is non-negative everywhere.

    4. It is Symmetric.

    4. Every symmetric positive semi-definite matrix is a covariance matrix.  
        [**Proof.**](http://ahmedbadary.ml/work_files/research/opt_probs#bodyContents12){: value="show" onclick="iframePopA(event)"}  
        <a href="http://ahmedbadary.ml/work_files/research/opt_probs#bodyContents12">` OR, Visit the website`</a>  
        <div markdown="1"> </div>

    5. The sample variance along direction $$u$$ can be expressed as a quadratic form in $$u$$:  
        $$ \sigma^2(u) = \dfrac{1}{n} \sum_{k=1}^n [u^T(x_k-\hat{x})]^2 = u^T \Sigma u,$$  
    6. The diminsion of the matrix is $$(n \times n)$$, where $$n$$ is the number of variables/features/columns.

    7. The inverse of this matrix, $${\displaystyle \Sigma ^{-1},}$$ if it exists, is the inverse covariance matrix, also known as the _concentration matrix_ or _precision matrix_.

    7. If a vector of $$n$$ possibly correlated random variables is jointly normally distributed, or more generally elliptically distributed, then its probability density function can be expressed in terms of the covariance matrix.

    8. $$\Sigma =\mathrm {E} (\mathbf {XX^{\rm {T}}} )-{\boldsymbol {\mu }}{\boldsymbol {\mu }}^{\rm {T}}$$.

    9. $${\displaystyle \operatorname {var} (\mathbf {AX} +\mathbf {a} )=\mathbf {A} \,\operatorname {var} (\mathbf {X} )\,\mathbf {A^{\rm {T}}} }$$.

    10. $$\operatorname {cov} (\mathbf {X} ,\mathbf {Y} )=\operatorname {cov} (\mathbf {Y} ,\mathbf {X} )^{\rm {T}}$$.

    11. $$\operatorname {cov} (\mathbf {X}_ {1}+\mathbf {X}_ {2},\mathbf {Y} )=\operatorname {cov} (\mathbf {X}_ {1},\mathbf {Y} )+\operatorname {cov} (\mathbf {X}_ {2},\mathbf {Y} )$$.  

    12. If $$(p = q)$$, then $$\operatorname {var} (\mathbf {X} +\mathbf {Y} )=\operatorname {var} (\mathbf {X} )+\operatorname {cov} (\mathbf {X} ,\mathbf {Y} )+\operatorname {cov} (\mathbf {Y} ,\mathbf {X} )+\operatorname {var} (\mathbf {Y} )$$.

    13. $$\operatorname {cov} (\mathbf {AX} +\mathbf {a} ,\mathbf {B} ^{\rm {T}}\mathbf {Y} +\mathbf {b} )=\mathbf {A} \,\operatorname {cov} (\mathbf {X} ,\mathbf {Y} )\,\mathbf {B}$$.

    14. If $${\displaystyle \mathbf {X} }$$  and $${\displaystyle \mathbf {Y} }$$  are independent (or somewhat less restrictedly, if every random variable in $${\displaystyle \mathbf {X} }$$ is uncorrelated with every random variable in $${\displaystyle \mathbf {Y} }$$), then $${\displaystyle \operatorname {cov} (\mathbf {X} ,\mathbf {Y} )=\mathbf {0} }$$.

    15. $$\operatorname {var} (\mathbf {b} ^{\rm {T}}\mathbf {X} )= \mathbf {b} ^{\rm {T}}\operatorname {cov} (\mathbf {X} )\mathbf {b} = \operatorname {cov} (\mathbf{b}^T\mathbf {X}, \mathbf{b}^T\mathbf {X} ) \geq 0,\,$$.
        > This quantity is NON-Negative because it's variance.  
        > Maybe $$= \mathbf {b} ^{\rm {T}}\operatorname {var} (\mathbf {X} )\mathbf {b}$$??  
    

    16. An identity covariance matrix, $$\Sigma = I$$ has variance $$= 1$$ for all variables.
 
    17. A covariance matrix of the form, $$\Sigma=\sigma^2I$$ has variance $$= \sigma^2$$ for all variables.

    18. A diagonal covariance matrix has variance $$\sigma_i^2$$ for the $$i-th$$  variable.

    19. When the mean $$\hat{x}$$ is not known the denominator of the "SAMPLE COVARIANCE MATRIX" should be $$(n-1)$$ and not $$n$$.

    > where,
     $${\displaystyle \mathbf {X} ,\mathbf {X} _{1}},$$ and $${\displaystyle \mathbf {X} _{2}}$$ are random $$(p\times 1)$$ vectors, $${\displaystyle \mathbf {Y} }$$  is a random $$(q\times 1)$$ vector, $${\displaystyle \mathbf {a} }$$  is a $$(q\times 1)$$ vector, $${\displaystyle \mathbf {b} }$$ is a $$(p\times 1)$$ vector, and $${\displaystyle \mathbf {A} }$$ and $${\displaystyle \mathbf {B} }$$  are $$(q\times p)$$ matrices of constants.

3. **$$\Sigma$$ as a Linear Operator:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents43}   
    * **Applied to one vector**, the covariance matrix _maps a linear combination_, $$c$$, of the random variables, $$X$$, onto a vector of covariances with those variables:   

    $${\displaystyle \mathbf {c} ^{\rm {T}}\Sigma =\operatorname {cov} (\mathbf {c} ^{\rm {T}}\mathbf {X} ,\mathbf {X} )}$$

    * **Treated as a bilinear form**, it yields the covariance between the two linear combinations:  

    $${\displaystyle \mathbf {d} ^{\rm {T}}\Sigma \mathbf {c} =\operatorname {cov} (\mathbf {d} ^{\rm {T}}\mathbf {X} ,\mathbf {c} ^{\rm {T}}\mathbf {X} )}$$

    * **The variance of a linear combination** is then (its covariance with itself)

    $${\displaystyle \mathbf {c} ^{\rm {T}}\Sigma \mathbf {c} }$$  

    * **The (pseudo-)inverse covariance matrix** provides an _inner product_,  $${\displaystyle \langle c-\mu \|\Sigma ^{+}\| c-\mu \rangle }$$  which induces the _Mahalanobis distance_, a measure of the "unlikelihood" of $$c$$.


4. **Applications [Examples]:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents44}   
    1. [**The Whitening Transformation:**](https://en.wikipedia.org/wiki/Whitening_transformation) allows one to completely decorrelate the data,  Equivalently,  
    allows one to find an optimal basis for representing the data in a compact way.

    2. [**Rayleigh Quotient:**](https://en.wikipedia.org/wiki/Rayleigh_quotient)

    2. [**Principle Component Analysis [PCA]**](https://en.wikipedia.org/wiki/Principal_components_analysis)

    2. [**The Karhunen-Loève transform (KL-transform)**](https://en.wikipedia.org/wiki/Karhunen-Lo%C3%A8ve_transform)

    2. [**Mutual fund separation theorem**](https://en.wikipedia.org/wiki/Mutual_fund_separation_theorem)

    5. [**Capital asset pricing model**](https://en.wikipedia.org/wiki/Capital_asset_pricing_model)

    7. [**Portfolio Theory:**](https://en.wikipedia.org/wiki/Modern_portfolio_theory) The matrix of covariances among various assets' returns is used to determine, under certain assumptions, the relative amounts of different assets that investors should (in a normative analysis) or are predicted to (in a positive analysis) choose to hold in a context of diversification.
    <br>

***

## Positive Semi-Definite Matrices
{: #content5}

1. **Definition:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents51}  
    A *__symmetric__* $${\displaystyle n\times n}$$ *__real__* matrix $${\displaystyle M}$$ is said to be __positive semi-definite__ if the scalar $${\displaystyle z^{\textsf {T}}Mz}$$ is *__non-negative__* for *__every non-zero__* column vector $${\displaystyle z}$$  of $$n$$ real numbers.  

    __Mathematically:__  
    <p>$$M \text { positive semi-definite } \Longleftrightarrow \quad x^{\top} M x \geq 0 \text { for all } x \in \mathbb{R}^{n}$$</p>  
    <br>

2. **Properties:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents52}   
    * $$AA^T$$ and $$A^TA$$ are PSD  
    * $$M$$ is positive definite if All pivots > 0      
    * $$M$$ is positive definite if and only if __all of its eigenvalues are non-negative__.  
    * __Covariance Matrices $$\Sigma$$__ are PSD  
    <br>

<!-- 3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents53}    -->

***

## Positive Definite Matrices
{: #content6}

1. **Definition:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents61}    
    A *__symmetric__* $${\displaystyle n\times n}$$ *__real__* matrix $${\displaystyle M}$$ is said to be __positive definite__ if the scalar $${\displaystyle z^{\textsf {T}}Mz}$$ is strictly *__positive__* for *__every non-zero__* column vector $${\displaystyle z}$$  of $$n$$ real numbers.  


    __Mathematically:__  
    <p>$$M \text { positive definite } \Longleftrightarrow x^{\top} M x>0 \text { for all } x \in \mathbb{R}^{n} \backslash \mathbf{0}$$</p>  


2. **Properties:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents62}  
    * $$M$$ is positive definite if and only if __all of its eigenvalues are positive__  
    * The matrix $${\displaystyle M}$$ is positive definite if and only if the bilinear form $${\displaystyle \langle z,w\rangle =z^{\textsf {T}}Mw}$$ is positive definite  
    * A symmetric matrix $${\displaystyle M}$$ is positive definite if and only if its __quadratic form is a strictly convex function__  
    * Every positive definite matrix is __invertible__ and its inverse is also positive definite.  
    * $$M$$ is positive definite if All pivots > 0  
    * __Covariance Matrices $$\Sigma$$__ are positive definite unless one variable is an exact linear function of the others. Conversely, every positive semi-definite matrix is the covariance matrix of some multivariate distribution  
    * Any quadratic function from $${\displaystyle \mathbb {R} ^{n}}$$ to $${\displaystyle \mathbb {R} }$$ can be written as $${\displaystyle x^{\textsf {T}}Mx+x^{\textsf {T}}b+c}$$ where $${\displaystyle M}$$ is a symmetric $${\displaystyle n\times n}$$ matrix, $$b$$ is a real $$n$$-vector, and $$c$$ a real constant. This quadratic function is strictly convex, and hence has a unique finite global minimum, if and only if $${\displaystyle M}$$ is positive definite.  
    <br>


<!-- 3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents63}  
 -->

***

## Orthogonal Matrices
{: #content7}

1. **Definition.**{: style="color: SteelBlue"}{: .bodyContents7 #bodyContents71}  
    Orthogonal (or, unitary (complex)) matrices are square matrices, such that the columns form an orthonormal basis.  
    <br>

2. **Properties:**{: style="color: SteelBlue"}{: .bodyContents7 #bodyContents72}  
    1. If $$U = [u_1, \ldots, u_n]$$ is an orthogonal matrix, then  
        <p>$$u_i^Tu_j = \left\{ \begin{array}{ll} 1 & \mbox{if } i=j, \\  0 & \mbox{otherwise.} \end{array} \right. $$</p>  

    2. $$U^TU = UU^T = I_n$$.  

    3. Easy inverse:  
        <p>$$U^{-1} = U^T$$</p>  

    4. Geometrically, orthogonal matrices correspond to rotations (around a point) or reflections (around a line passing through the origin).  
        > i.e. they preserve length and angles!  
        > Proof. Part 5 and 6.  

    5. For all vectors $$\vec{x}$$,  
        $$ \|Ux\|_2^2 = (Ux)^T(Ux) = x^TU^TUx = x^Tx = \|x\|_2^2 .$$  
        > Known as, _the rotational invariance_ of the Euclidean norm.  
        > Thus, If we multiply x with an orthogonal matrix, the errors present in x will not be magnified. This behavior is very desirable for maintaining numerical stability.  

    6. If $$x, y$$ are two vectors with unit norm, then the angle $$\theta$$ between them satisfies $$\cos \theta = x^Ty$$  
    while the angle $$\theta'$$ between the rotated vectors $$x' = Ux, y' = Uy$$ satisfies $$\cos \theta' = (x')^Ty'$$.  
    Since, $$(Ux)^T(Uy) = x^T U^TU y = x^Ty,$$ we obtain that the angles are the same.  
    <br>


3. **Examples:**{: style="color: SteelBlue"}{: .bodyContents7 #bodyContents73}  
    * [**Permutation Matrices**](http://livebooklabs.com/keeppies/c5a5868ce26b8125/72793237f1b79da9){: value="show" onclick="iframePopA(event)"}
        <a href="http://livebooklabs.com/keeppies/c5a5868ce26b8125/72793237f1b79da9">` Visit the Book`</a>
        <div markdown="1"> </div>
    <br>

***

## Dyads
{: #content8}

1. **Definition.**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents81}  
    A matrix $$A \in \mathbf{R}^{m \times n}$$ is a dyad if it is of the form $$A = uv^T$$ for some vectors $$u \in \mathbf{R}^m, v \in \mathbf{R}^n$$.  
    
    The dyad acts on an input vector $$x \in \mathbf{R}^n$$ as follows:  
    <p>$$ Ax = (uv^T) x = (v^Tx) u.$$</p>  
    <br>

2. **Properties:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents82}  
    1. The output always points in the same direction $$u$$ in output space ($$\mathbf{R}^m$$), no matter what the input $$x$$ is.

    2. The output is always a simple scaled version of $$u$$.

    3. The amount of scaling depends on the vector $$v$$, via the linear function $$x \rightarrow v^Tx$$.  
    <br>

3. **Examples:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents83}  
    * [**Single factor model of financial price data**](http://livebooklabs.com/keeppies/c5a5868ce26b8125/438c7a0d0fc50d09){: value="show" onclick="iframePopA(event)"}
        <a href="http://livebooklabs.com/keeppies/c5a5868ce26b8125/438c7a0d0fc50d09">` Visit the Book`</a>
        <div markdown="1"> </div>

    <br>

4. **Normalized dyads:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents84}  
    :   We can always normalize the dyad, by assuming that both u,v are of unit (Euclidean) norm, and using a factor to capture their scale.  
    :   That is, any dyad can be written in normalized form:  
    :   $$ A = uv^T = (\|u\|_2 \cdot |v|_2 ) \cdot (\dfrac{u}{\|u\|_2}) ( \dfrac{v}{\|v\|_2}) ^T = \sigma \tilde{u}\tilde{v}^T,$$  
    :   where $$\sigma > 0$$, and $$\|\tilde{u}\|_2 = \|\tilde{v}\|_2 = 1.$$

5. **Symmetric dyads:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents85}  
    :    Another important class of symmetric matrices is that of the form $$uu^T$$, where $$u \in \mathbf{R}^n$$.
    The matrix has elements $$u_iu_j$$, and is symmetric.
    > If $$\|u\|_2 = 1$$, then the dyad is said to be normalized.

    :   $$
        uu^T = \left(\begin{array}{ccc} u_1^2  & u_1u_2  & u_1u_3  \\
        u_1u_2 & u_2^2   & u_2u_3  \\
        u_1u_3 & u_2u_3  & u_3^2  \end{array} \right)
        $$  
    :   * **Properties:**
            1. Symmetric dyads corresponds to quadratic functions that are simply squared linear forms:  
            $$q(x) = (u^Tx)^2$$
            2. When the vector $$u$$ is normalized (unit), then:  
            $$\mathbf{Tr}(uu^T) = \|u\|_2^2 = 1^2 = 1$$  
            > This follows from the fact that the diagonal entries of a symmetric dyad are just $$u_i^2, \forall i \in [1, n]$$
            3. 

***

## Correlation matrix
{: #content9}

1. **Definition.**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents91}  
    :   $${\text{corr}}(\mathbf {X} )=\left({\text{diag}}(\Sigma )\right)^{-{\frac {1}{2}}}\,\Sigma \,\left({\text{diag}}(\Sigma )\right)^{-{\frac {1}{2}}}$$

2. **Properties:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents92}  
    0. It is the matrix of "Pearson product-moment correlation coefficients" between each of the random variables in the random vector $${\displaystyle \mathbf {X} }$$.

    1. The correlation matrix can be seen as the covariance matrix of the standardized random variables $${\displaystyle X_{i}/\sigma (X_{i})}$$ for $${\displaystyle i=1,\dots ,n}$$.

    2. Each element on the principal diagonal of a correlation matrix is the correlation of a random variable with itself, which always equals 1.

    3. Each off-diagonal element is between 1 and –1 inclusive.


<!-- 3. **Examples:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents93}  

***

## Ten
{: #content10}

1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents10 #bodyContents101}  

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents10 #bodyContents102}  

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents10 #bodyContents103}  

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents10 #bodyContents104}  

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents10 #bodyContents105}  

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents10 #bodyContents106}  

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents10 #bodyContents107}  

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents10 #bodyContents108}  
 -->