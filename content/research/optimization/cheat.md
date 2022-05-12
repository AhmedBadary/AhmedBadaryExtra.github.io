---
layout: NotesPage
title: Optimization <br > Cheat Sheet
permalink: /cheat
prevLink: /work_files/research/conv_opt.html
---
<div markdown="1" class = "TOC">
# Table of Contents

  * [Mathematical Background](#content1)
  {: .TOC1}
  * [Mathematical Formulation [Standard Forms]](#content2)
  {: .TOC2}
</div>

***
***

## FIRST
{: #content1}

1. **Functions:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}
    * __*Graph* of a function $$f : \mathbf{R}^n \rightarrow \mathbf{R}$$__: is the set of input-output pairs that $$f$$ can attain, that is:  
    $$\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ G(f) := \left \{ (x,f(x)) \in \mathbf{R}^{n+1} : x \in \mathbf{R}^n \right \}.$$ \\
    > It is a subset of $$\mathbf{R}^{n+1}$$.
    * __*Epigraph* of a function $$f$$__: describes the set of input-output pairs that $$f$$ can achieve, as well as "anything above":  
    $$\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \mathop{\bf epi} f := \left \{ (x,t) \in \mathbf{R}^{n+1} ~:~ x \in \mathbf{R}^n, \ \  t \ge f(x) \right \}.$$
    * __Level sets__:  is the set of points that achieve exactly some value for the function $$f$$.  
    For $$t \in \mathbf{R}$$, the $$t-$$level set of the function $$f$$ is defined as:  
    $$\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \mathbf{L}_t(f) := \left\{ x \in \mathbf{R}^{n} ~:~ x \in \mathbf{R}^n, \ \  t = f(x) \right \}.$$
    * __Sub-level sets__: is the set of points that achieve at most a certain value for  $$f$$, or below:  
    $$\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \mathbf{S}_t(f) := \left\{ x \in \mathbf{R}^{n} ~:~ x \in \mathbf{R}^n, \ \  t \ge f(x) \right\}.$$  



2. **Optimization Problems:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}
    * __Functional Form__:  An optimization problem is a problem of the form
    $$\:\:\:\:\:\:\:$$ $$p^\ast := \displaystyle\min_x f_0(x) :  f_i(x) \le 0, \ \  i=1,\ldots, m$$  
    where: $$x \in \mathbf{R}^n$$ is the decision variable;  $$f_0 : \mathbf{R}^n \rightarrow \mathbf{R}$$ is the objective function, or cost;  $$f_i : \mathbf{R}^n \rightarrow \mathbf{R}, \ \  i=1, \ldots, m$$ represent the constraints;  $$p^\ast$$ is the optimal value.
    * __Feasibility Problems__:  Sometimes an objective function is not provided. This means that we are just _interested_ in _finding_ a _feasible point_, or determine that the problem is _infeasible_. 
    > By convention, we set $$f_0$$ to be a constant in that case, to reflect the fact that we are indifferent to the choice of a point x as long as it is feasible.
                

3. **Optimality:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}
    * __Feasible Set__:  
    $$\:\:\:\:\:\:\:$$ $$ \mathbf{X} :=  \left\{ x \in \mathbf{R}^n ~:~  f_i(x) \le 0, \ \  i=1, \ldots, m \right\}.$$  
    * __Optimal Value__:  
    $$\:\:\:\:\:\:\:$$$$\:\:\:\:\:\:\:$$  $$p^\ast := \min_x : f_0(x) ~:~ f_i(x) \le 0, \ \  i=1, \ldots, m.$$   
    * __Optimal Set__:  The set of feasible points for which the objective function achieves the optimal value:  
    $$\:\:\:\:\:\:\:$$$$\:\:\:\:\:\:\:$$  $$ \mathbf{X}^{\rm opt} :=  \left\{ x \in \mathbf{R}^n ~:~  f_0(x) = p^\ast, \ \ f_i(x) \le 0, \ \  i=1,\ldots, m \right\} = \mathrm{arg min}_{x \in \mathbf{X}}  f_0(x)$$  
    > By convention, the optimal set is empty if the problem is not feasible.  
    > A _point_ $$x$$ is said to be **optimal** if it belongs to the optimal set.  
    > If the optimal value is **ONLY** attained in the **limit**, then it is **NOT** in the optimal set.    
    * __Suboptimality__:  the $$\epsilon$$-suboptimal set is defined as:  
    $$\:\:\:\:\:\:\:$$$$\:\:\:\:\:\:\:$$  $$ \mathbf{X}_\epsilon := \left\{ x \in \mathbf{R}^n ~:~ f_i(x) \le 0, \ \  i=1, \ldots, m, \ \  f_0(x) \le p^\ast + \epsilon \right\}.$$  
    > $$\implies \  \mathbf{X}_0 = \mathbf{X}_{\rm opt}$$.  
    * __Local Optimality__:  
        A point $$z$$ is **Locally Optimal**: if there is a value $$R>0$$ such that $$z$$ is optimal for the following problem:  
    $$\:\:\:\:\:\:\:$$ $$\:\:\:\:\:\:\:$$ $$min_x : f_0(x) ~:~ f_i(x) \le 0, \ \ i=1, \ldots, m,  \ \ \|z-x\|_2 \le R$$.  
    > i.e. a _local minimizer_ $$x$$ _minimizes_ $$f_0$$, but **only** for _nearby points_ on the feasible set.  
    * __Global Optimality__:  
        A point $$z$$ is **Globally Optimal**: if it is the _optimal value_ of the original problem on all of the feasible region.   
            

4. **Problem Classes:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}
* **Least-squares:**{: style="color: SteelBlue  "}{: .bodyContents4 #bodyContents41}
        :   $$\min_x \;\;\;\; \sum_{i=1}^m \left( \sum_{j=1}^n A_{ij} . x_j - b_i \right)^2$$
        :   where $$A_{ij}, \  b_i, \  1 \le i \le m,  \ 1 \le j \le n$$, are given numbers, and $$x \in \mathbf{R}^n$$ is the variable.

    * **Linear Programming:**{: style="color: SteelBlue  "}{: .bodyContents4 #bodyContents42} 
        :   $$ \min \sum_{j=1}^n c_jx_j ~:~ \sum_{j=1}^n A_{ij} . x_j  \le b_i , \;\; i=1, \ldots, m, $$ 
        :   where $$ c_j, b_i$$ and $$A_{ij}, \  1 \le i \le m, \  1 \le j \le n$$, are given real numbers.  

    * **Quadratic Programming:**{: style="color: SteelBlue  "}{: .bodyContents4 #bodyContents43}
        :   $$\min_x \;\;\;\; \displaystyle\sum_{i=1}^m \left(\sum_{j=1}^n C_{ij} . x_j+d_i\right)^2 + \sum_{i=1}^n c_ix_i \;:\;\;\;\; \sum_{j=1}^m A_{ij} . x_j \le b_i, \;\;\;\; i=1,\ldots,m.$$  
        > Includes a **sum of squared linear functions**, in addition to a **linear term**, in the _objective_.  

    * **Nonlinear optimization:**{: style="color: SteelBlue  "}{: .bodyContents4 #bodyContents44}
        :   A broad class that includes _Combinatorial Optimization_.

        > One of the reasons for which non-linear problems are hard to solve is the issue of _local minima_.

    * **Convex optimization:**{: style="color: SteelBlue  "}{: .bodyContents4 #bodyContents45}
        :    A generalization of QP, where the objective and constraints involve "bowl-shaped", or convex, functions.

        > They are _easy_ to solve because they _do not suffer_ from the "curse" of _local minima_.

    * **Combinatorial optimization:**{: style="color: SteelBlue  "}{: .bodyContents4 #bodyContents46}
        :   In combinatorial optimization, some (or all) the variables are boolean (or integers), reflecting discrete choices to be made.

        > Combinatorial optimization problems are in general extremely hard to solve. Often, they can be approximately solved with linear or convex programming.

    * **NON-Convex Optimization Problems [Examples]:**{: style="color: SteelBlue  "}{: .bodyContents4 #bodyContents47} \\
        * **Boolean/integer optimization:** some variables are constrained to be Boolean or integers.  
        > Convex optimization can be used for getting (sometimes) good approximations.
        * **Cardinality-constrained problems:** we seek to bound the number of non-zero elements in a vector variable.  
        > Convex optimization can be used for getting good approximations.
        * **Non-linear programming:** usually non-convex problems with differentiable objective and functions.  
        > Algorithms provide only local minima.  


***

## Linear Algebra
{: #content2}

1. **Basics:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}
    * **Linear Independence:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents11}
        :   A set of vectors $$\{x_1, ... , x_m\} \in {\mathbf{R}}^n, i=1, \ldots, m$$ is said to be independent if and only if the following condition on a vector $$\lambda \in {\mathbf{R}}^m$$:  
        :   $$\sum_{i=1}^m \lambda_i x_i = 0 \ \ \ \implies  \lambda = 0.$$

            > i.e. no vector in the set can be expressed as a linear combination of the others.

    * **Subspace:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents12}
        :   A subspace of $${\mathbf{R}}^n$$ is a subset that is closed under addition and scalar multiplication. Geometrically, subspaces are "flat" (like a line or plane in 3D) and pass through the origin.  

        * A **Subspace** $$\mathbf{S}$$ can always be represented as the span of a set of vectors $$x_i \in {\mathbf{R}}^n, i=1, \ldots, m$$, that is, as a set of the form:  
        $$\mathbf{S} = \mbox{ span}(x_1, \ldots, x_m) := \left\{ \sum_{i=1}^m \lambda_i x_i ~:~ \lambda \in {\mathbf{R}}^m \right\}.$$
        $$\\$$ 

    * **Affine Sets (Cosets | Abstract Algebra):**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents13}
        :   An affine set is a translation of a subspace — it is "flat" but does not necessarily pass through 0, as a subspace would. 
        :   An affine set $$\mathbf{A}$$ can always be represented as the translation of the subspace spanned by some vectors:
        :   $$\:\:\:\:\:\:\:$$ $$ \mathbf{A} = \left\{ x_0 + \sum_{i=1}^m \lambda_i x_i ~:~ \lambda \in {\mathbf{R}}^m \right\}\ \ \ $$  
        for some vectors $$x_0, x_1, \ldots, x_m.$$  
        $$\implies \mathbf{A} = x_0 + \mathbf{S}.$$

        * **(Special case)** **lines**: When $$\mathbf{S}$$ is the span of a single non-zero vector, the set $$\mathbf{A}$$ is called a line passing through the point $$x_0$$. Thus, lines have the form
        $$\left\{ x_0 + tu ~:~ t \in \mathbf{R} \right\}$$,  \\
        where $$u$$ determines the direction of the line, and $$x_0$$ is a point through which it passes.

    * **Basis:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents14}
        :    A **basis** of $${\mathbf{R}}^n$$ is a set of $$n$$ independent vectors. If the vectors $$u_1, \ldots, u_n$$ form a basis, we can express any vector as a linear combination of the $$u_i$$'s:
        :   $$\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ x = \sum_{i=1}^n \lambda_i u_i, \ \ \ \text{for appropriate numbers } \lambda_1, \ldots, \lambda_n$$.


    * **Dimension:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents15} 
        :   The number of vectors in the span of the (sub-)space.

2. **Norms and Scalar Products:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}
    * **Scalar Product:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents21}
    :   The scalar product (or, inner product, or dot product) between two vectors $$x,y \in \mathbf{R}^n$$ is the scalar denoted $$x^Ty$$, and defined as: 
    :   $$x^Ty = \sum_{i=1}^n x_i y_i.$$ 

    * **Norms:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents22} 
    :   A measure of the "length" of a vector in a given space.
    :   **Theorem.** A function from $$\chi$$ to $$\mathbf{R}$$ is a norm, if:  
        1. $$\|x\| \geq 0, \: \forall x \in \chi$$, and $$\|x\| = 0 \iff x = 0$$.
        2. $$\|x+y\| \leq \|x\| + \|y\|,$$ for any $$x, y \in \chi$$ (triangle inequality).
        3. $$\|\alpha x\| = \|\alpha\| \|x\|$$, for any scalar $$\alpha$$ and any $$x\in \chi$$.

    * **$$l_p$$ Norms:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents200} 
    :   $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$  $$\ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$  $$\|x\|_p = \left( \sum_{k=1}^n \|x_k\|_p \right)^{1/p}, \ 1 \leq p < \infty$$.


    * **The $$l_1-norm$$:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents24}
    :   $$ \|x\|_1 := \sum_{i=1}^n \| x_i \| $$   
    :   Corresponds to the distance travelled on a rectangular grid to go from one point to another.  \\
        > Induces a diamond shape

    * **The $$l_2-norm$$ (Euclidean Norm):**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents23} 
    :   $$  \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \| x \|_2 := \sqrt{ \sum_{i=1}^n x_i^2 } = \sqrt{x^Tx} $$.  
    :   Corresponds to the usual notion of distance in two or three dimensions.
    :   > The $$l_2-norm$$ is invariant under orthogonal transformations,     
        > i.e., $$\|x\|_2 = \|Vz\|_2 = \|z\|_2,$$ where $$V$$ is an orthogonal matrix. 
    :   > The set of points with equal l_2-norm is a circle (in 2D), a sphere (in 3D), or a hyper-sphere in higher dimensions. 

    * **The $$l_\infty-norm$$:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents25}
    :   $$ \| x \|_\infty := \displaystyle\max_{1 \le i \le n} \| x_i \|$$  
    :   > useful in measuring peak values.  
        > Induces a square

    * **The Cardinality:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents20}
    :   The **Cardinality** of a vector $$\vec{x}$$ is often called the $$l_0$$ (pseudo) norm and denoted with,  
    :   $$\|\vec{x}\|_0$$.
    :   > Defined as the number of non-zero entries in the vector.


    * **Cauchy-Schwartz inequality:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents26}
    :   For any two vectors $$x, y \in \mathbf{R}^n$$, we have  
    :   $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$ $$ \ \ \ \ \ \ \ \ \ \ \ \ \ $$  $$x^Ty \le \|x\|_2 \cdot \|y\|_2$$.
    :   > The above inequality is an equality if and only if $$x, y$$ are collinear:  
        > : $$ {\displaystyle \max_{x : \: \|x\|_2 \le 1} \: x^Ty = \|y\|_2,}$$ 
        > with optimal $$x$$ given by  
        > $$x^\ast = \dfrac{y}{\|y\|_2}, \ $$ if $$y$$ is non-zero.

    * **Angles between vectors:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents27} 
    :   When none of the vectors x,y is zero, we can define the corresponding angle as theta such that,
    :    $$\cos\  \theta = \dfrac{x^Ty}{\|x\|_2 \|y\|_2} .$$ 


3. **Notes:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}
    * __Norms and Metrics__:  
    Norms induce metrics on topological spaces but not the other way around.  
    Technically, a norm is a metric with two additional properties: (1) Translation Invariance (2) Absolute homogeneouity/scalability  
    We can always define a metric from a norm: $$d(x,y) = \|x - y \|$$  
    A metric is a function of two variables and a norm is a function of one variable.
    * __Collinearity__:  In geometry, collinearity of a set of points is the property of their lying on a single line  
            


<!-- 4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24} -->

<!-- 5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents26}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents27}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents28}
 -->