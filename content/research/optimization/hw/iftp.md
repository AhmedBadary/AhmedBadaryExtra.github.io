---
layout: page
title: The Index Fund Tracking Problem
permalink: /work_files/research/conv_opt/hw/iftp
prevLink: /work_files/research/conv_opt.html
---

**Abstract:**  
<p class="message">The following analysis demonstrates how to <i>Formulate</i> the Index Fund Tracking Problem as an optimization problem. "Shorting" is treated as an optional constraint where these constraints affect the solution to the optimization problem as demonstrated here. We finally look at how to deal with the mechanics of handling the trade-off between the tracking error and the number of assets that are being traded.</p>

## The Set Up

***

#### The problems goal is to track a certain time-series containing the returns (the % gain if we invest one dollar at the beginning of period $$t$$, and collect it at the end of the period) of a certain financial index, (for example the SP 500 index).
{: style="color: SteelBlue  "}

#### The index by itself may not be tradable, or it may be very costly to trade it because it has too many assets in it. However we can try to invest in a few tradable assets, such as stocks, and hope to closely follow the index so that the return of our portfolio matches that of the index.
{: style="color: SteelBlue  "}

## Mathematical Set Up

***

#### Mathematically, we are given a real-valued time-series $$s(t)$$ with time $$t$$ from $${1, \cdots, T}$$. Here, $$s(t)$$ is the return of the index at time $$t$$.
{: style="color: SteelBlue  "} 
#### We also have a universe of $$n$$ possible tradable assets, with, $$s_i(t), \: t = 1, \cdots , T$$ the return time-series for asset $$i, \: i = 1, \cdots, n$$.
{: style="color: SteelBlue  "}
#### Investing an amount $$x_i$$ in the $$i$$-th asset at the beginning of period $$t$$ produces the return $$x_is_i(t)$$ at the end of period $$t$$.
{: style="color: SteelBlue  "}

## Approach

***

> Here our variable is the vector of amounts invested in each asset, $$x = (x_1, \cdots, x_n)$$,
which we refer to as the "_portfolio vector_". 

####  In order to minimize the transaction costs involved in trading each asset, we would like to limit the number of assets present in the portfolio.
{: style="color: SteelBlue  "}

#### We plan to find the vector $$x \in \mathbf{R}^n$$ based on the available data, and hold it for some time in the future.
{: style="color: SteelBlue  "}

## Proposed Formulation 

***

**We start by expressing the time series of returns of the portfolio vector $$x, s(x)$$, as a linear function of $$x$$.**

> Where the $$t$$-th coordinate of $$s(x)$$ is the return of the portfolio at time $$t$$.  

Precisely, we will express the time series as a $$T$$-dimensional vector $$s(x) = Ax$$, with $$x \in \mathbf{R}^n$$
and $$A$$ a $$(T \times n)$$ matrix expressed in terms of the data.

First, we Let $$s = (s(1), \cdots, s(T)) \in \mathbf{R}^T$$ and $$s_i = (s_i(1), \cdots, s_i(T)) \in \mathbf{R}^T , i = 1, \cdots, n$$.  
Now, we can express,  
<p>$$s(x) = \sum_{i=1}^n x_is_i = Ax,$$</p>
where $$A = [s_1, \cdots, s_n]$$ a $$(T \times n)$$ matrix.

**Now, we formulate the problem of _minimizing the tracknig error_ as a Least-Sqaures Problem**  

> Remember that the _tracking error_ is defined as the average squared error between the return of the index and that of the portfolio.  

> We, also, assume "Shorting" is allowed  
>   > i.e. selling assets.

Mathematically, the tracking error is  
<p>$$ \dfrac{1}{T} \sum_{t=1}^T \left(s(t) - \sum_{i=1}^n x_is_i(t) \right)^2$$</p>
We rewrite this as a norm
<p>$$\dfrac{1}{T} \|Ax - s\|_2^2$$</p>
Now, the Least-Squares problem comes naturally as minimizing the tracking error is just minimizing a sum of squares with no constraints
<p>$${\displaystyle \min_x \|Ax - s\|_2^2}$$</p>

**Assume that _Shorting_ is not allowed anymore. We try to reformulate the problem by adding the shorting constraint**

When shorting is not allowed, $$x$$ cannot be negative.
Thus, we add the constraints $$x \geq 0$$ to the least-squares problem,
<p>$$\min_x \|Ax - s\|_2^2 \:\: : \:\: x \geq 0 $$</p>
resulting in a QP (Quadratic Program) formulation of the problem,  
<p>$$\min_x x^TQx + c^Tx \:\: : \:\: Cx \leq d$$</p>
which is a QP in standard form, with 
<p> $$C = −I_n, d = 0, c = −2A^Ts,$$ and $$Q \:= A^TA$$ is a positive semi-definite matrix.</p>


**We add our concern for transaction costs; i.e. trading-off the tracking error against the number of assets that have to be traded.**

To control the transaction costs we need to minimize the number of non-zero components of $$x$$,  
since a zero value in $$x_i$$ means the $$i$$-th asset will not have to be traded.   

The $$l_1$$ norm allows us to minimize the number of non-zero components of a vector $$\vec{x}$$.  

Thus, we add a _regularized_ $$l_1$$ term to the original Least-Squares problem,  
<p>$$\min_x \|Ax - s\|_2^2 + \lambda \|x\|_1 \:\: : \:\: x \geq 0 $$</p>
where $$\lambda \geq 0$$ is the regularization parameter that controls the trade-off between the tracking error and the number of assets (i.e. the transaction costs).  

We notice that as $$\lambda$$ gets bigger the number of non-zero components in $$x$$ decreases and vice-versa.

**Finally, we formulate the above problem as a Quadratic Program (QP)**

We write,

<p>$$\min_x \|Ax - s\|_2^2 + \lambda \|x\|_1 \:\: : \:\: x \geq 0 $$</p>
<p>$$= \min_x \|Ax - s\|_2^2 + \lambda \vec{1}^T x \:\: : \:\: x \geq 0 $$</p>
where $$\vec{1}$$ is the vector of all ones.

This allows us to formulate the QP,  
<p>$$\min_x x^TQx + (c + \lambda \vec{1})^Tx \:\: : \:\: Cx \leq d$$</p>

Q.E.D