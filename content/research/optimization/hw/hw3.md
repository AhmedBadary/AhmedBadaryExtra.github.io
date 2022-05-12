---
layout: NotesPage
title: HW 3
permalink: /work_files/research/conv_opt/hw/hw3
prevLink: /work_files/research/conv_opt.html
---



## Q.1)
1. 
    We quote the well-known Least-Squares expression that minimizes $$\|Ax-y\|_2^2$$ over $$x$$:  
    <p>$$x^{(k)} = (A_k^TA_k)^{-1}A_k^Ty^{(k)}$$</p>  
    Where $$(A_k^TA_k)^{-1}A_k^T$$ is the projection operator.

2. 
    First, we define  
    <p>$$H_k = A_k^TA_k$$</p>  
    Then, notice  
    <p>$$
    \begin{align}
    \left(A_{k+1}^TA_{k+1}\right) &= \left(A_k^TA_k + a_{k+1}a_{k+1}^T\right) = \left(H_k + a_{k+1}a_{k+1}^T\right) & (1) \\
    \left(A_{k+1}^T y^{k+1}\right) &= \left(A_{k}^Ty^k + a_{k+1}y^{k+1}\right) & (2) \\
    \left(H_k + a_{k+1}a_{k+1}^T\right)^{-1} &= H_k^{-1} - \dfrac{1}{1+a_{k+1}^TH_k^{-1}a_{k+1}} H_k^{-1}a_{k+1}a_{k+1}^TH_k^{-1} & (3) \\
    \end{align}$$</p>  
    > We will use these three equations as we derive the solution.  
    <p> So, the objective function we are minimizing is:</p>
    <p>$$\|A_{k+1}x-y^{k+1}\|_2^2$$</p>
    We notice, from the Least Squares solution in part 1 (and derived in Lecture) that the answer should have this form:
    <p> $$x^{(k+1)} = (A_{k+1}^TA_{k+1})^{-1}A_{k+1}^Ty^{(k+1)}$$</p>
    Now, we use the equations $$((1), (2), (3))$$ we wrote out to find a solution given the parameters stated in the question,
    <p> 
    $$
    \begin{align}
    x^{(k+1)} &= (A_{k+1}^TA_{k+1})^{-1}A_{k+1}^Ty^{(k+1)} \\
    &= \left(A_k^TA_k + a_{k+1}a_{k+1}^T\right)^{-1}A_{k+1}^Ty^{(k+1)} & \text{from part } (1) \\
    &= \left(H_k + a_{k+1}a_{k+1}^T\right)^{-1}A_{k+1}^Ty^{(k+1)} & \text{from part } (1) \\
    &= \left(H_k + a_{k+1}a_{k+1}^T\right)^{-1}\left(A_{k}^Ty^k + a_{k+1}y^{k+1}\right) & \text{from part } (2) \\
    &= \left(H_k^{-1} - \dfrac{1}{1+a_{k+1}^TH_k^{-1}a_{k+1}} H_k^{-1}a_{k+1}a_{k+1}^TH_k^{-1}\right) \left(A_{k}^Ty^k + a_{k+1}y^{k+1}\right) & \text{from part } (3)
    \end{align}
    $$
    </p>
    > Notice that the inverse of $$A_k^TA_k$$ always exists because $$A$$ had Full-Column-Rank.
    <p> Now, lets see whatx advantages does RLS possess.</p>  
    We notice that the inverse can be iteratively updated without recalculating the new inverse each time which implies that we do not have to re-compute the very expensive and very unstable "inverse".  
    This, obviously, requires some sort of hashing the old inverted matrix.  
    > Another way to rephrase this based on different application assuming you start mid-way,  
    > is saying that we only need to compute the inverse of a matrix that has a lower rank.  

## Q.2)
```python
import numpy as np, matplotlib.pyplot as plt, matplotlib.patches as mpatches
from numpy import *
from numpy.linalg import *
from scipy.interpolate import spline #ar = array ; %matplotlib inline # Please Uncomment + put each line on a separate line.

# Variables
x = ar([0,1,2,3,4,5,6,7,8,9])
y = ar([5.31, 5.61, 5.28, 5.54, 3.85, 4.49, 5.99, 5.32, 4.39, 4.73])
mse_errs, max_errs, polys, degs = [], [], [], [i for i in range(5, 9)]
mse_errs_ext, max_errs_ext, polys_ext, degs_ext = [], [], [], [i for i in range(3, 12)]

# Helper Functions
def mse(p, x, y):
    sm = [abs(p(x[i])-y[i])**2 for i in range(len(x))]
    return sum(sm)/len(x), sm[argmax(sm)]

def plot_err(x, y, xlabel, ylabel, title, xlim=None, ylim=None):
    _ = plt.plot(x, y, '.', x, y, 'r')
    plt.xlabel(xlabel, fontweight='bold')
    plt.ylabel(ylabel, fontweight='bold')
    plt.title(title,  fontsize=15,y=1.04)
    plt.gca().title.set_color('red')
    plt.gca().yaxis.label.set_color('red')
    plt.gca().xaxis.label.set_color('red')
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    if xlim != None:
        plt.gca().set_xlim(xlim)
    if ylim != None:
        plt.gca().set_ylim(ylim)
    plt.show()

# Answers to the sub-questions
def q2_1():
    for n in range(5,9):
        p = poly1d(polyfit(x, y, n))
        polys.append(p)
        print("n =", n, ":  p_" + str(n)," =",p, "\n")

def q2_2():   
    for n in range(5,9):
        p = poly1d(polyfit(x, y, n))
        mse_errs.append(round(mse(p, x, y)[0], 11))
        max_errs.append(round(mse(p, x, y)[1], 10))
        print("n =", n, ":  Mean_Sq_Err =", round(mse(p, x, y)[0], 11), "| Max_Err =", round(mse(p, x, y)[1], 10))

def plot_errs():
    plot_err(degs, mse_errs, "degree", "MSE-Err", 'MSE-Err vs Degree', xlim=[2.9,11.1], ylim=[-0.01,.35])
    plot_err(degs, max_errs, "degree", "MAX-Err", 'MAX-Err vs Degree', xlim=[4.9,8.1])

""" Void
This function creates more polynomials with different degrees in [3, 12) (hence, "extended").
Then it plots them.
"""
def plot_extended_errs():
    for n in range(3,12):
        p = poly1d(polyfit(x, y, n))
        polys_ext.append(p)
        mse_errs_ext.append(mse(p, x, y)[0])
        max_errs_ext.append(mse(p, x, y)[1])
    plot_err(degs_ext, mse_errs_ext, "degree-extended", "MSE-Err", 'MSE-Err vs Degree-Extended ', xlim=[2.9,11.1], ylim=[-0.01,.35])
    plot_err(degs_ext, max_errs_ext, "degree-extended", "MAX-Err", 'MAX-Err vs Degree-Extended ', xlim=[2.9,11.1], ylim=[-0.01,1.35])
```  
> Notice, all the code blocks below (Q.2) refer to this piece of code above.  

1. We proceed by using the "polyfit" module in "numpy".  
    ```python
    >>> q2_1()
                                 5           4          3         2         1
    >>> n = 5 :  P_5 = 0.002876 x - 0.06977 x + 0.5933 x - 2.043 x + 2.259 x + 5.2
                                 6           5          4         3         2         1  
    >>> n = 6 :  P_6 = 0.001985 x - 0.05071 x + 0.4724 x - 1.932 x + 3.237 x - 1.593 x + 5.33
                                  7            6           5          4         3         2
    >>> n = 7 :  P_7 = 4.785e-06 x + 0.001834 x - 0.04884 x + 0.4609 x - 1.895 x + 3.181 x - 1.562 x + 5.33
                                8          7         6         5         4         3         2
    >>> n = 8 :  P_8 = -.00067 x + .02413 x - .3528 x + 2.687 x - 11.37 x + 26.32 x  - 30.5 x + 13.46 x + 5.31
    ```  
    This gives us the solutions:  
    <p>$$
        P_5(x) = 0.002876 x^{5} - 0.06977 x^{4} + 0.5933 x^{3} - 2.043 x^{2} + 2.259 x^{1} + 5.2 \\
        P_6(x) = 0.001985 x^{6} - 0.05071 x^{5} + 0.4724 x^{4} - 1.932 x^{3} + 3.237 x^{2} - 1.593 x^{1} + 5.33 \\
        P_7(x) = 4.785 \cdot 10^6 x^{7} + 0.001834 x^{6} - 0.04884 x^{5} + 0.4609 x^{4} - 1.895 x^{3} + 3.181 x^{2} - 1.562 x^{1} + 5.33 \\
        P_8(x) = -6.701 \cdot 10^{-4} x^{8} + 0.02413 x^{7} - 0.3528 x^{6} + 2.687 x^{5} - 11.37 x^{4} + 26.32 x^{3} - 30.49 x^{2} + 13.46 x^{1} + 5.311
        $$
    </p>  
    Let's plot the polynomials against each other.  
    When we do so, we will notice how much each polynomial oscillates and we will see which polynomial actually goes through the data points (in blue).  
    <img src="/main_files/conv_opt/3/3.1/espp.png" width="70%" style="position: relative;">  
    > Please refer to the legend to differentiate the polynomials.

2. We proceed by using the found polynomials and the defined "mean-squared-loss" function.    
    ```python
    >>> q2_2()
    >>> n = 5 :  Mean_Sq_Err = 0.23202104429 | Max_Err = 0.7823959188
    >>> n = 6 :  Mean_Sq_Err = 0.10826098368 | Max_Err = 0.3902666906
    >>> n = 7 :  Mean_Sq_Err = 0.10825867873 | Max_Err = 0.3887930312
    >>> n = 8 :  Mean_Sq_Err = 0.00614953188 | Max_Err = 0.0200802073
    ```  
    Now, we plot them and compare them with each other.  
    <img src="/main_files/conv_opt/3/3.1/esp1.png" width="48%" style="position: relative;">
    <img src="/main_files/conv_opt/3/3.1/esp2.png" width="48%" style="position: relative;">  
    We notice that as the degree of the polynomial increases (upto $$n=8$$) the accuracy increases and the error decreases.  
    This can be contributed to the degree of oscillation of the data itself which can be readily seen in the plot of the data and it's "Spline-Interpolation":  
    <img src="/main_files/conv_opt/3/3.1/esp3.png" width="70%" style="position: relative;left:50px">  
    As you can see, the data points are quite non-monotonic, in-fact, they oscillate wildly. Thus, it will be very hard to model this data with a line for example, or with any polynomial of insufficient degree of oscillation.  
    However, we should remember Runge's phenomenon (i.e. the "wildly-oscillating polynomials" problem). This tells us that as the degree of the interpolating (or regression) polynomial increases, the approximation becomes very very unstable outside of the domain of regression.  
    In-fact, as we will see further below, the optimal degree (not necessarily in the domain) is actually $$n = 10$$.

***

2. [FurtherAnalysis]


## Q.3)
1. We begin our analysis by manipulating the equations algebraically.  
    <p>$$ \begin{align}
        \|x-a_1\|^2 &= d_1^2 \\
        \|x-a_2\|^2 &= d_2^2 \\
        \|x-a_3\|^2 &= d_3^2 \\
        \end{align}\\
        $$
        $$
        \implies \\
        $$
        $$
        \begin{align}
        x^Tx−2a_1^Tx+\|a_1\|^2 &= d_1^2 &(1)\\ 
        x^Tx−2a_2^Tx+\|a_2\|^2 &= d_2^2 &(2)\\ 
        x^Tx−2a_3^Tx+\|a_3\|^2 &= d_3^2 &(3)
        \end{align}
        $$  </p>  
    We subtract Eq. $$(1)$$ from Eq. $$(2)$$ and again from Eq. $$(3)$$.  
    <p>$$\iff \\$$
    $$ \begin{align}
        2(a_1 − a_2)^Tx &= \|a_1\|^2 − \|a_2\|^2 − d_1^2 + d_2^2 \\
        2(a_1 − a_3)^Tx &= \|a_1\|^2 − \|a_3\|^2 − d_1^2 + d_3^2 
        \end{align}\\
        \implies
        $$
    $$
    \begin{align}
    \left[ \begin{array}{c}   2(a_1 − a_2)^T \\ 
                                2(a_1 − a_3)^T  
     \end{array} \right]\vec{x} &= \left[ \begin{array}{c}   \|a_1\|^2 − \|a_2\|^2 − d_1^2 + d_2^2 \\ 
                                \|a_1\|^2 − \|a_3\|^2 − d_1^2 + d_3^2  
     \end{array} \right]
     \\ \\
     &\iff \\
     A\vec{x} &= \vec{y}
     \end{align}
    $$</p>

2. What we are looking for is what/how the petrubations in the measurement correspond to in the column space.  
    We notice that really all we need is to look at what the inverse of $$A$$ does to the unit ball (unit circle in  $$\mathbf{R}^2$$).  
    We proceed by computing $$A^{-1}$$ and then finding the SVD of the inverse matrix. We, then, use the properties of the SVD and the singular values to compute the volumes (areas) of the ellipsoids resulting from transforming the unit ball.  
    The example (ellipsoid) with the smaller volume will have less petrubations in the column space (range) of the output $$x$$.  
    ```python
    >>> q_3_2()
    >>> ArgMin =  2  : Min =  0.0523598775598
    ```  
    We see that the ellipsoid induced by the second scenario is actually smaller and thus has a better chance of getting the correct solution $$x^\ast$$ with the same bound on the petrubation in the measurement vector.  
    Now, the region of uncertainty is just the ellipsoid itself which is characterized by the SVD of $$A^{-1}$$:  
    Region of uncertainty case 1: $$\frac{\left(x\right)^2}{0.64339784}+\frac{\left(y\right)^2}{0.07771242}=1^2$$  
    Region of uncertainty case 2: $$\frac{\left(x\right)^2}{0.16666667}+\frac{\left(y\right)^2}{0.1}=1^2$$  
    Both can be seen here:  
    <img src="/main_files/conv_opt/3/3.1/esp4.png" width="50%" height="30%" style="position: relative;">  
    > case 1: Highlighted ; case 2: not-Highlighted

    ```python
    import numpy as np
    from numpy import *
    from numpy.linalg import *
    ar = array

    # Helper Function
    def ellipse_area(a, b):
        return pi*a*b

    def get_area(a1, a2, a3):
        a1, a2, a3 = a1, a2, a3
        A = ar([2*(a1-a2).T, 2*(a1-a3).T])
        U, s, V = np.linalg.svd(inv(A), full_matrices=False)
        return ellipse_area(s[0], s[1])

    # Solutions to sub-problems
    def q_3_2():
        area1, area2 = get_area(ar([0,0]), ar([4,-1]), ar([5,0])), get_area(ar([0,0]), ar([0,3]), ar([5,0]))
        print("ArgMin = ", argmin([area1,area2])+1, " : Min = ", min(area1, area2))
    ```  
    > Please notice that this is the code that Q.3 is referring to.


<img src="/main_files/conv_opt/3/3.1/esp5.png">