---
layout: NotesPage
title: Optimization Problems
permalink: /work_files/research/opt_probs
prevLink: /work_files/research
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Geometry and Lin-Alg [Hyper-Planes]](#content1)
  {: .TOC1}
  * [Statistics](#content2)
  {: .TOC2}
  * [Inner Products Over Balls](#content3)
  {: .TOC3}
  * [Gradients and Derivatives](#content4)
  {: .TOC4}
  * [FIFTH](#content5)
  {: .TOC5}
  * [SIXTH](#content6)
  {: .TOC6}
</div>

***
***

## Geometry and Lin-Alg [Hyper-Planes]
{: #content1}

1. **Minimum Distance from a point to a hyperplane/Affine-set?**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents11}
    :   $$d = \dfrac{\| w \cdot x_0 + b \|}{\|w\|},$$  
    :   where we have an n-dimensional hyperplane: $$w \cdot x + b = 0$$ and a point $$x_0$$.
    > Also known as, **The Signed Distance**.  
    * **Proof.**  
        * Suppose we have an affine hyperplane defined by $$w \cdot x + b$$ and a point $$x_0$$.
        * Suppose that $$\vec{v} \in \mathbf{R}^n$$ is a point satisfying $$w \cdot \vec{v} + b = 0$$, i.e. it is a point on the plane.
        * We construct the vector $$x_0−\vec{v}$$ which points from $$\vec{v}$$ to $$x_0$$, and then, project it onto the unique vector perpendicular to the plane, i.e. $$w$$,  

            $$d=\| \text{proj}_{w} (x_0-\vec{v})\| = \left\| \frac{(x_0-\vec{v})\cdot w}{w \cdot w} w \right\| = \|x_0 \cdot w - \vec{v} \cdot w\|\frac{\|w\|}{\|w\|^2} = \frac{\|x_0 \cdot w - \vec{v} \cdot w\|}{\|w\|}.$$

        * We chose $$\vec{v}$$ such that $$w\cdot \vec{v}=-b$$ so we get  

            $$d=\| \text{proj}_{w} (x_0-\vec{v})\| = \frac{\|x_0 \cdot w +b\|}{\|w\|}$$

2. **Every symmetric positive semi-definite matrix is a covariance matrix:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents12}
    * **Proof.**  
        * Suppose $$M$$ is a $$(p\times p)$$ positive-semidefinite matrix.  

        * From the finite-dimensional case of the spectral theorem, it follows that $$M$$ has a nonnegative symmetric square root, that can be denoted by $$M^{1/2}$$.  

        * Let $${\displaystyle \mathbf {X} }$$ be any $$(p\times 1)$$ column vector-valued random variable whose covariance matrix is the $$(p\times p)$$ identity matrix.   

        * Then,   

            $${\displaystyle \operatorname {var} (\mathbf {M} ^{1/2}\mathbf {X} )=\mathbf {M} ^{1/2}(\operatorname {var} (\mathbf {X} ))\mathbf {M} ^{1/2}=\mathbf {M} \,}$$


***

## Statistics
{: #content2}

1. **Asynchronous:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents21} \\

2. **Every symmetric positive semi-definite matrix is a covariance matrix:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents22}
    * **Proof.**  
        * Suppose $$M$$ is a $$(p\times p)$$ positive-semidefinite matrix.  

        * From the finite-dimensional case of the spectral theorem, it follows that $$M$$ has a nonnegative symmetric square root, that can be denoted by $$M^{1/2}$$.  

        * Let $${\displaystyle \mathbf {X} }$$ be any $$(p\times 1)$$ column vector-valued random variable whose covariance matrix is the $$(p\times p)$$ identity matrix.   

        * Then,   

            $${\displaystyle \operatorname {var} (\mathbf {M} ^{1/2}\mathbf {X} )=\mathbf {M} ^{1/2}(\operatorname {var} (\mathbf {X} ))\mathbf {M} ^{1/2}=\mathbf {M} \,}$$

***

## Inner Products Over Balls
{: #content3}

1. **Extrema of inner product over a ball:**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents31}
    :   Let $$y \in \mathbf{R}^n$$ be  a  given non-null vector, and let $$\chi = \left\{x \in \mathbf{R}^n :\  \|x\|_2 \leq r\right\}$$,  
    where $$r$$ is some given positive number.
    1. **Determine the optimal value $$p_1^\ast$$ and the optimal set of the problem $$\min_{x \in \chi} \; |y^Tx|$$:**    
        The minimum value of $$\min_{x \in \chi} \; |y^Tx|$$ is $$p_1^\ast = 0$$.  
        This value is attained either by $$x = 0$$, or by any vector $$x\in\chi_r$$ orthogonal to $$y$$.  
        The optimal set: $$\chi_{opt} = \left\{x : \ x = Vz, \|z\|_2 \leq r\right\}$$        
    2. **Determine the optimal value $$p_2^\ast$$ and the optimal set of the problem $$\max_{x\in \chi} \; |y^Tx|:$$**
        The optimal value of $$\max_{x\in \chi} \; |y^Tx|$$ is attained for any $$x = \alpha y$$ with $$\|x\|_2 = r$$.  
        Thus for $$|\alpha| = \dfrac{r}{\|y\|_2}$$, for which we have $$p_2^\ast∗ = r\|y\|_2.$$  
        The optimal set contains two points: $$\chi_{opt} = \left\{x : \  x = \alpha y, \alpha = ± \dfrac{r}{\|y\|_2} \right\}$$.
    3. **Determine the optimal value $$p_3^\ast$$ and the optimal set of the problem $$\min_{x\in \chi} \; y^Tx$$:**  
        We have $$p_3^\ast = −r\|y\|_2,$$ which is attained at the unique optimal poin   
        $$x^\ast = −\dfrac{r}{\|y\|_2} y.$$ 

    4. **Determine the optimal value $$p_4^\ast$$ and the optimal set of the problem $$\max_{x\in\chi} \; y^Tx$$:**  
        We have $$p_4^\ast = r \|y\|_2,$$ which is attained at the unique optimal point  
         $$x^\ast = \dfrac{r}{\|y\|_2} y.$$

***

## Gradients and Derivatives
{: #content4}

1. **Gradient of log-sum-exp function:**{: style="color: SteelBlue  "}{: .bodyContents4 #bodyContents41}
    :   Find the gradient at $$x$$ of the function $$lse : \  \mathbf{R}^n \rightarrow \mathbf{R}$$ defined as,  
    :   $$
        lse(x) = \log{(\sum_{i=1}^n e^{x_i})}.
        $$

    :   **Solution.**  
        $$\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \nabla_x \  lse(x)$$
    :   $$
        \begin{align}
        & \ = \nabla_x \log(\sum_{i=1}^n e^{x_i}) \\
        & \ = \dfrac{\dfrac{d}{dx_i} (\sum_{i=1}^n e^{x_i})}{\log(\sum_{i=1}^n e^{x_i})} \\
        & \ = \dfrac{e^{x_i}}{lse(x)} \\
        & \ = \dfrac{[e^{x_1} \  e^{x_2} \  \ldots \  e^{x_n}]^T}{lse(x)}
        \end{align}
        $$
