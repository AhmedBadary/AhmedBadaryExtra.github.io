---
layout: NotesPage
title: HW 1
permalink: /work_files/research/conv_opt/hw/hw1
prevLink: /work_files/research/conv_opt.html
---



## Q.1)
1. Notice that the matrix is very sparse and it has symmetric rows.  

    > _I am not saying that the matrix itself is a symmetric matrix, the rows are just similar to each other so they cancel out_.  

    Lets subtract row 100 from row 200 and then subtract row 1 from all the the rows except row 200.  
    This will leave a one in the 100th row from the first column through the 49th column and then another one in the first row and the 50th column. Then we can do the same with row 230 and subtract it from row 200 and then row 256 subtract from rows 201 through 255.  
    Now, we are left with:  
    $$
    a_1 = -[\sum_{i=2}^{49} a_i],\  a_{50} = 0,\  a_{51}= - [\sum_{i=52}^{229} a_i],
    \ a_{230} = 0,\  a_{231} = -[\sum_{i=232}^{256} a_i].
    $$  
    Now, the Null Space consists of the span of these vectors.

2. The Rank is the number of vectors in the pivot positions $$ = 5$$.  
    Or,  
    The rank $$ = Dimension - Nullity = 256 - 255 = 5$$.  

    > From the _Rank-Nullity Theorem_.





## Q.2)
1. We prove the following inequalities:
    1. **$$\| x \|_2 \leq \| x \|_1$$:**  
        $$
        \begin{align}
        & \ (1)\ \  \|x\|_1^2 - \| x \|_2^2 = (\sum_{i=1}^n |x_i|)^2 - \sum_{i=1}^n x_i^2 \\
        & \ (2)\ \  (\sum_{i=1}^n |x_i|)^2 - \sum_{i=1}^n x_i^2 = 2 * \sum_{i=1}^n \sum_{j=i+1} |x_i x_j| \\
        & \ (3)\ \  2 * \sum_{i=1}^n \sum_{j=i+1} |x_i x_j| \geq 0 \\
        & \ \implies  \\
        & \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \| x \|_2 \leq \| x \|_1
        \end{align}
        $$
        > The last implications comes from the monotonicity of the squared function.

    2. **$$\| x \|_\infty \leq \| x \|_2$$:**  
        $$
        \begin{align}
        & \ \|x\|_2^2 = \sum_{i=1}^n x_i^2 \\
        & \ \| x \|_\infty^2 = \displaystyle {\mathrm{\ max}_{i} |x_i|} \\
        & \ \displaystyle {\mathrm{\ max}_{i} |x_i|} \leq \sum_{i=1}^n x_i^2 \\
        & \ \implies  \\
        & \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \| x \|_\infty \leq \| x \|_2
        \end{align}
        $$
        > The last implications comes from the monotonicity of the squared function.


    3. **$$\| x \|_2 \leq n*\| x \|_\infty$$:**  
        $$
        \begin{align}
        & \ (1)\ \ \|x\|_2^2 = \sum_{i=1}^n x_i^2 \\
        & \ (2)\ \ n*\| x \|_\infty^2 = n * \displaystyle {\mathrm{arg\ max}_{i} |x_i|} \\
        & \ (3)\ \  \sum_{i=1}^n x_i^2 \leq n * \displaystyle {\mathrm{arg\ max}_{i} |x_i|} \\
        & \ \implies  \\
        & \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \| x \|_2 \leq \sqrt{n} \| x \|_\infty
        \end{align}
        $$
        > The last implications comes from the monotonicity of the squared function.

    4. **$$\| x \|_1 \leq \sqrt{n} \| x \|_2$$:**  
        $$
        \begin{align}
        & \ (1)\ \ \|x\|_1 = \sum_{i=1}^n |x_i| \\
        & \ (2)\ \ n*\| x \|_\infty^2 = n * \displaystyle {\mathrm{arg\ max}_{i} |x_i|} \\
        & \ (3)\ \  \sum_{i=1}^n x_i^2 \leq n * \displaystyle {\mathrm{arg\ max}_{i} |x_i|} \\
        & \ \implies  \\
        & \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \| x \|_2 \leq \sqrt{n} \| x \|_\infty
        \end{align}
        $$
        > The last implications comes from the monotonicity of the squared function.

    5. **$$\sqrt{n}\|x\|_2 \leq n \|x\|_\infty$$:**  
        $$
        \begin{align}
        & \ (1)\ \ \|x\|_2 = (\sum_{i=1}^n x_i^2)^{1/2} \\
        & \ (2)\ \ (\sum_{i=1}^n x_i^2)^{1/2} \leq (\sum_{i=1}^n x_{max}^2)^{1/2} \\
        & \ (3)\ \ (\sum_{i=1}^n x_{max}^2)^{1/2} = \sqrt{n} \|x\|_\infty \\
        & \ (4)\ \ \text{ Multiply (3) by } \sqrt{n}
        & \ \implies  \\
        & \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \sqrt{n}\|x\|_2 \leq n \|x\|_\infty
        \end{align}
        $$

    6. **$$1/\sqrt{n}\|x\|_2 \leq \|x\|_\infty$$:**  
        $$
        \begin{align}
        & \ (1)\ \ \|x\|_2 = (\sum_{i=1}^n x_i^2)^{1/2} \\
        & \ (2)\ \ (\sum_{i=1}^n x_i^2)^{1/2} \leq (\sum_{i=1}^n x_{max}^2)^{1/2} \\
        & \ (3)\ \ (\sum_{i=1}^n x_{max}^2)^{1/2} = \sqrt{n} \|x\|_\infty \\
        & \ (4)\ \ \text{ Divide (3) by } \sqrt{n}
        & \ \implies  \\
        & \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \sqrt{n}\|x\|_2 \leq n \|x\|_\infty
        \end{align}
        $$

    7. **$$\|x\|_\infty \leq \|x\|_1$$:**  
        Follows trivially from (1) and (2).


    All of this implies that the big inequality indeed holds.


2. Let $$n'$$ be the number of non-zero entries:  
    $$\sum x_i^2 \geq |x^\ast|^2,\ $$ where $$x^\ast = \max_{1\leq i\leq n} |x_i|  \\$$ 
    $$\implies n' * \sum x_i^2 \geq n'|x^\ast|^2 \implies n' \geq n' * |x^\ast|^2 / \sum x_i^2 \geq \|x\|_2^2 / \|x\|_2^2.$$



## Q.3)

1. $$\sum_{i=1}^n (1+r_i)x_i = (\vec{1} + \vec{r})^T\vec{x}$$

2. $$\vec{1}^T \vec{r} = \sum_{i=1}^n (r_i)$$


## Q.4)

1. We rewrite $$x_1 = -2x_2 -3x_3 + 1$$ to make it a vector space.
    $$\implies H = \begin{bmatrix} -2 & -3 \\ 1 & 0 \\ 0 & 1 \end{bmatrix} + \begin{bmatrix} 1 \\  0 \\ 0  \end{bmatrix} \left[(n-1)\right]$$.  
    Thus, this shows that it is indeed an affine set.


2. $$\text{proj}_{\vec{w}}(x_0 - v) = \dfrac{|-1|}{\sqrt{1^2+2^2+3^2}} = d$$  
    Point: $$\dfrac{-1}{(1^2+2^2+3^2)} <1,2,3>$$

## Q.5)

### 1. We solve the optimization problem.

* **Proof.**  
    > The Objective Function  

    $$t_i(\vec{w}) = \displaystyle {\mathrm{arg\ min}_{t} \|t\vec{w} − \vec{x}^{(i)} \|_2, \  i = 1, \ldots, m}.$$

    > We minimize using calculus

    $$
    \begin{align}
    & \ = \displaystyle {\mathrm{\ min}_{t} \|t\vec{w} − \vec{x}^{(i)} \|_2, \  i = 1, \ldots, m} \\
    & \ = \nabla_{t}  \displaystyle {\mathrm{arg\ min}_{t} \|t\vec{w} − \vec{x}^{(i)} \|_2, \  i = 1, \ldots, m} \\
    & \ = \nabla_{t} \left[\left(t\vec{w} - \vec{x}^{(i)}\right)^T \left(t\vec{w} - \vec{x}^{(i)}\right)\right]^{1/2} \\
    & \ = \nabla_{t} \left[\left(t\vec{w}^T - {\vec{x}^{(i)}}^T\right) \left(t\vec{w} - \vec{x}^{(i)}\right)\right]^{1/2} \\
    & \ = \nabla_{t} \left(t^2\vec{w}^T\vec{w} - 2t\vec{w}^T\vec{x}^{(i)} + {\vec{x}^{(i)}}^T\vec{x}^{(i)}\right) \\
    & \ = \dfrac{1}{2} \left[t^2\vec{w}^T\vec{w} - 2t\vec{w}^T\vec{x}^{(i)} + {\vec{x}^{(i)}}^T\vec{x}^{(i)} \right]^{-1/2} \left(2t\vec{w}^T\vec{w} - 2\vec{w}^T\vec{x}^{(i)} \right) \\
    & \ = \dfrac{1}{2} \left[t^2\vec{w}^T\vec{w} - 2t\vec{w}^T\vec{x}^{(i)} + {\vec{x}^{(i)}}^T\vec{x}^{(i)} \right]^{-1/2} \left(2t\vec{w}^T\vec{w} - 2\vec{w}^T\vec{x}^{(i)} \right) = 0 \\
    & \iff t\vec{w}^T\vec{w} - \vec{w}^T\vec{x}^{(i)} = 0 \\
    & \iff t_i(\vec{w}) =  \dfrac{\vec{w}^T\vec{x}^{(i)}}{\vec{w}^T\vec{w}} \\    
    & \iff t_i(\vec{w}) =  \dfrac{\vec{w}^T\vec{x}^{(i)}}{\|\vec{w}\|_2} \\    
    & \iff t_i(\vec{w}) =  \dfrac{\vec{w}^T\vec{x}^{(i)}}{1} \\    
    & \iff t_i(\vec{w}) =  \vec{w}^T\vec{x}^{(i)}
    \end{align}
    $$

### 2. First, lets define a few things:  
$$\hat{t}(\vec{w}) = \dfrac{1}{m} \sum_{i=1}{m} t_i = \dfrac{1}{m} \sum_{i=1}{m} \vec{w}^T\vec{x}^{(i)}$$.  
Notice that the inner product $$\vec{w}^T\vec{x}$$ is constant for all vectors $$\vec{w}$$.  
This implies that the vector x must be zero.

* **Proof.**
    For any two vectors $$w$$ and $$x$$:  
    $$
    \begin{align}
    & \ \vec{w}^T\vec{x} = <w,x> = C,\  \text{where } C\ \text{is a constant},\ \ \forall \vec{w} \\ 
    & \ \implies <2x,x> = C = <x,x> \\
    & \ \implies <2x,x> = <x,x> \\
    & \ \implies <x,x> = 0 \\
    & \ \iff x = 0 \\
    \end{align}
    $$

### 3. We rewrite the sample variance as a quadratic form:  
$$\sigma^2(w) = \dfrac{1}{m} \sum t_i(w)^2  = \dfrac{1}{m} \sum (\vec{w}^T\vec{x}^{(i)})^2 = w^T\Sigma w$$  

> Since $$\hat{x} = 0$$.  

$$\implies \Sigma = \dfrac{1}{m} \sum \vec{x}^{(i)} {\vec{x}^{(i)}}^T = C$$.  
Since it is a constant, the eigenvalues are all the same.  
This implies that $$\Sigma$$ is proportional to the identity matrix with constant of proportionality equals to the constant earlier, where $$C = \sigma^2(w)$$.



1.
array([ 0.23249528+0.j,  0.23249528+0.j,  0.11624764+0.j,  0.69748583+0.j,
        0.23249528+0.j,  0.58123819+0.j])

        [ 0.11111111,0.11111111,0.05555556,0.33333333,0.11111111,0.27777778]


tr(A) = tr(UDU T
) = tr(U
TUD) = tr(D) = X
d
i=1
λi
,