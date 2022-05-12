---
layout: NotesPage
title: HW 2
permalink: /work_files/research/conv_opt/hw/hw2
prevLink: /work_files/research/conv_opt.html
---



## Q.1)
1. 
    $$\left( \begin{array}{cccccc} 0 & 0   & 0 & \frac{1}{3} & 0 & 0 \\ 
                                   1 & 0   & 0 &  0  & 0 & 0 \\ 
                                   0 & \frac{1}{2} & 0 &  0  & 0 & 0 \\ 
                                   0 & 0   & 1 &  0  & 0 & 1 \\ 
                                   0 & 0   & 0 & \frac{1}{3} & 0 & 0 \\ 
                                   0 & \frac{1}{2} & 0 & \frac{1}{3} & 1 & 0
     \end{array} \right)
     \\ \\$$

2. 
    $$x_2 = \left( \begin{array}{c} 0.23249528+0.j \\ 0.23249528+0.j \\ 0.11624764+0.j \\  0.69748583+0.j \\ 0.23249528+0.j \\  0.58123819+0.j \end{array} \right) \\ \\$$


3. 
    $$x_3 = \left( \begin{array}{c} 1/9 \\ 1/9 \\ 1/18 \\ 1/3 \\ 1/9 \\  5/18 \end{array} \right)$$

    We notice that sequence does indeed converge to the value $$x_3$$ above.  


    ```python
        from numpy import *

        def importance(A):
            return linalg.eig(A)[1][,:0]

        def iter(A, x0, eps=10**-5):
            x, old_x = A.dot(x0), x0
            print(x0)
            while not allclose(x, old_x, rtol=1e-010, atol=1e-18):
                old_x = x
                x = A.dot(x)
                print(x)
            return x

        def sanity_check(A, x_2, x_3):
            return allclose(A.dot(x_2), 1*x_2) and allclose(A.dot(x_3), 1*x_3)

        x0 = 1/6*ones(6)
        A = array([[0,0,0,1/3,0,0],[1,0,0,0,0,0],[0,1/2,0,0,0,0],[0,0,1,0,0,1],\
        [0,0,0,1/3,0,0],[0,1/2,0,1/3,1,0]])

        x_2 = importance(A)
        x_3 = iter(A, x0)

        print(x_2)
    >>> array([ 0.23249528+0.j,  0.23249528+0.j,  0.11624764+0.j,  0.69748583+0.j,
        0.23249528+0.j,  0.58123819+0.j])

        print(x_3)
    >>> array([ 0.11111111,  0.11111111,  0.05555556,  0.33333333,  0.11111111,
        0.27777778])

        sanity_check(A, x_2, x_3)
    >>> True
    ```  
    > Please run the code to print (dump) all the resulting $$x_k$$ vectors until convergence.  

    > Notice also that $$x_2$$ and $$x_3$$ refer to the eigenvector that we foind in the $$i-th$$ question.


## Q.2)

1. We notice first that the output vector $$y(t)$$ depends only on the state $$x(t)$$ and that, in-turn, $$x(t)$$ depends only on the input vector $$u(t-1)$$. Since $$x(t)$$ has a recursive definition, we are voin going to try to find a closed form formula for computing the sequence of $$x(t)$$ if possible:  
    $$
     \\ 
    x(1) = Ax(0) + Bu(0) = Bu(0), \:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\: \text{(from the initial conditions)} \\
    x(2) = Ax(1) + Bu(1) = ABu(0) + Bu(1) \\
    x(3) = Ax(2) + Bu(2) = A^2Bu(0) + ABu(1) + Bu(2) \\
    x(4) = Ax(3) + Bu(3) = A^3Bu(0) + A^2Bu(1) + ABu(2) + Bu(3)
    \\
    $$
    From, this, we can extrapolate a formula:
    $$x(T) = \sum_{i=0}^{T-1} A^iBu((T-1)-i)$$,  
    Now, from the definition of $$U(T)$$, we re-write:
    $$x(T) = H'U(T)$$,  
    where $$H' = \left( \begin{array}{ccccc} A^{T-1}B & A^{T-2}B & \cdots & AB & B \end{array} \right)$$.

    <p class="message">
    proof. <br />
        Induct on $$x(k) = Ax(k-1) + Bu(k-1)$$,  
        $$ 
        \begin{align}
        &= A\left(\sum_{i=0}^{k-2} A^iBu((k-2)-i)\right) + Bu(k-1) \\
        &= \left(\sum_{i=0}^{k-2} A^{(i+1)}Bu((k-2)-i)\right) + Bu(k-1) \\
        &= \left(\sum_{i=1}^{k-1} A^{i}Bu((k-1)-i)\right) + Bu(k-1), \:\: (\text{shifting the index}) \\
        &= \sum_{i=0}^{k-1} A^iBu((k-1)-i), \:\:\:\:\:\:\:\:\: (Bu(k-1)\text{ is the first element}) \\
        \end{align}
        \\
        \:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\: \mathbf{Q.E.D}
        $$ 
    </p>
    Now, that we have a formula for $$x(T)$$, we write:  
    <p>
    $$
    y(T) = Cx(T) = CH'U(T) = HU(T)
    $$  
    </p>
    where,  
    <p>
    $$
    H = CH' = C \left( \begin{array}{ccccc} A^{T-1}B & A^{T-2}B & \cdots & AB & B \end{array} \right) \in \mathbf{R}^{m \times TP}
    $$
    </p>

2. The range of $$H$$, represents all the possible outputs $$(y(t))$$ for any possible input vector $$u(t)$$. If a vector $$\vec{v}$$ is not in $$\mathbf{Range}(H)$$, then it doesn't matter what the input $$u(t)$$ is, we can never get that vector $$\vec{v}$$ as an output.  
    Notice that this also implies that the range characterizes the output of the LDA given only the input vector $$u(t)$$ and abstracts away the solution of the state of the system, $$x(t)$$.


## Q.3)

1.  \\
    $$\operatorname{tr} (A)$$  
    <p>  
    $${\displaystyle
    \begin{align}
    &= \operatorname{tr}(UDU^T) \:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\: &(A \text{is symmetric}) \\
    &= \operatorname{tr}(U^TUD) \:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\: &(\text{Cyclic property of Trace}) \\
    &= \operatorname{tr}(I_nD) \:\:\:\:\:\:\:\:\:\:\:\:\:\: &(\text{Orthogonality of} U) \\
    &= \operatorname{tr}(D) \\
    &= \sum_{i=1}^{d} \lambda_i \:\:\:\:\:\:\:\:\:\:\:\:\:\: &(\text{def. of Trace}) \\
    &= \vec{\lambda}^T\cdot\vec{1} \:\:\:\:\:\:\:\:\:\:\:\:\:\: &(\text{where$$ \lambda $$is vec of eigenvalues}) \\
    \end{align}
    }
    $$  
    </p>
    $${\displaystyle \|A\|_{\rm {F}}}$$  
    <p>  
    $$
    {\displaystyle
    \begin{align}
    &= {\sqrt {\sum _{i=1}^{m}\sum _{j=1}^{n}|a_{ij}|^{2}}} \:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\: &(\text{def.}) \\
    &= {\sqrt{\langle A, B \rangle}} \:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\: &(\text{Scalar product}) \\
    &= {\sqrt{\operatorname{tr}(A^TA)}} \:\:\:\:\:\:\:\:\:\:\:\:\:\: &(\text{Sum of the diagonal entries}) \\
    &= {\sqrt{\operatorname{tr}((U\Lambda U^T)^T(U\Lambda U^T))}} \:\:\:\:\:\:\:\:\:\:\:\:\:\: &(A\text{ is symmetric}) \\
    &= {\sqrt{\operatorname{tr}(U\Lambda U^TU\Lambda U^T)}} \\
    &= {\sqrt{\operatorname{tr}(U\Lambda^2U^T)}} \\
    &= {\sqrt{\operatorname{tr}(UU^T\Lambda^2)}} \:\:\:\:\:\:\:\:\:\:\:\:\:\: &(\text{Cyclic property of trace}) \\
    &= {\sqrt{\operatorname{tr}(\Lambda^2)}} \:\:\:\:\:\:\:\:\:\:\:\:\:\: &(\text{from the first part}) \\
    &= {\sqrt {\sum _{i=1}^{n} \lambda_{i}^{2}(A)}} \\
    &= {\sqrt {\vec{\lambda}*\vec{\lambda}\cdot\vec{1}}} \:\:\:\:\:\:\:\:\:\:\:\:\:\: &(\text{element-wise product}) \\
    \end{align}
    }
    $$  
    </p>

2.  
    $$
    |\langle A,A\rangle| |\langle I,I\rangle| \ge |\langle A,I\rangle|^2$$ (Cauchy Shwartz) or,  
    $$\operatorname{trace}(A^2)\ge\frac{1}{n}\operatorname{trace}(A)^2$$ but n here is just the rank,  
    $$\implies\|A\|_F^2\ge\frac{\operatorname{trace}(A)^2}{rank(A)}$$

3. It appears that the only critireon needed here is the fact that the matrix is square. Otherwise the Trace is not defined. 
    However, since we did our analysis with respect to the eigenvalues, we should note that the singular values and the eigen values of a matrix may very much not agree if the matrix was not PSD.
    Notice that if the same analysis could be made with the singularvalues instead.  

    Also, notice that even for non-square matrices, we could have a similar tight bound if we replace the $$trace(A)^2$$ with the trace norm (nuclear norm).


## Q.4)

1. 
    * **Proof.**  
        * Suppose we have an affine hyperplane defined by $$c^T \cdot x = b$$ and a point $$d$$.
        * Suppose that $$\vec{x_0} \in \mathbf{R}^n$$ is a point satisfying $$c^T \cdot \vec{x_0} - b = 0$$, i.e. it is a point on the plane.
        * We construct the vector $$d−\vec{x_0}$$ which points from $$\vec{x_0}$$ to $$d$$, and then, project it onto the unique vector perpendicular to the plane, i.e. $$c^T$$,  

            $$dist=\| \text{proj}_{c} (d-\vec{x_0})\| = \left\| \frac{c^T\cdot(d-\vec{x_0}) }{c^T \cdot c} c \right\| = \|c^T \cdot d - c^T\vec{x_0}\|\frac{\|c\|}{\|c\|^2} = \frac{\|c^T \cdot d - c^T\vec{x_0}\|}{\|c\|}.$$

        * We chose $$\vec{x_0}$$ such that $$c^T\cdot \vec{x_0} = b$$ and $$\|c\|_2=1$$ so we get  

            $$dist=\| \text{proj}_{c} (d-\vec{x_0})\| = \|c^T \cdot d - b\|$$

2. 
    $$\min_{c,b} dist^2 = \min_{c,b} |c^T \cdot d - b|^2 = \min_{c,b} \|c^T \cdot d - b\|_2^2$$
    $$\implies \min_{c,b} (c^Td-b)^T(c^Td-b) = (d^Tc-b^T)(c^Td-b)=d^Tcc^Td-d^Tcb-b^Tc^Td+b^Tb \\= c^Tdd^Tc-2b^Tc^Td+b^Tb$$

3. To minimize this, we find both partial derivatives and set them both equal to zero and solve.
    Since, partial of b is 0 we proceed:  
    $$frac{d}{db} f_0(b,c) = -2 (dd^T-b^Td) \sum bi = 0$$  
    > This is equal to zero when $$b = 1/n \sum x_i$$ is the average of the sample points.  
    Now we only need to minimize over $$c$$:  
    $$\min_c (c^T(dd^T-b^Td)c) = \min_c (c^T((d^d)I-dd^T)c) = \min_c (c^T(DD^T)c)$$  

4. We can use expressions for projectors from the SVD to obtain for the general solution.
    We compute the SVD.
    The sol with minimum norm is V1 Σ−1r UT1 b