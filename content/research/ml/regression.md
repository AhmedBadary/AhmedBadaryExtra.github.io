---
layout: NotesPage
title: Regression
permalink: /work_files/research/ml/regrs
prevLink: /work_files/research/ml.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Regression](#content1)
  {: .TOC1}
  * [Linear Regression](#content2)
  {: .TOC2}
  * [Logistic Regression](#content3)
  {: .TOC3}
  <!-- * [](#content4)
  {: .TOC4} -->
</div>

***
***

[Generalized Linear Models and Exponential Family Distributions (Blog!)](http://willwolf.io/2017/05/18/minimizing_the_negative_log_likelihood_in_english/)  
[Logistic regression as a neural network (Blog!)](https://www.datasciencecentral.com/profiles/blogs/logistic-regression-as-a-neural-network)  

[A very simple demo of interactive controls on Jupyter notebook - Interactive Linear Regression (Article+Code)](https://towardsdatascience.com/a-very-simple-demo-of-interactive-controls-on-jupyter-notebook-4429cf46aabd)  


* __Least-Squares Linear Regression__:  
    MLE + Noise Normally Distributed + Conditional Probability Normally Distributed  
* __Logistic Regression__:  
    MLE + Noise $$\sim$$ Logistic Distribution (latent) + Conditional Probability $$\sim$$ Bernoulli Distributed  
* __Ridge Regression__: 
    MAP + Noise Normally Distributed + Conditional Probability Normally Distributed + Weight Prior Normally Distributed  



## Regression
{: #content1}
<!-- 
1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}
2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}
3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}
4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}
5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}
6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}
7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}
8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18}
 -->
***

## Linear Regression
{: #content2}

* [Linear Regression as a Statistical Model](/work_files/research/theory/models#bodyContents111)  



Assume that the target distribution is a sum of a deterministic function $$f(x; \theta)$$ and a normally distributed error $$\epsilon \sim \mathcal{N}\left(0, \sigma^{2}\right)$$:  
<p>$$y = f(x; \theta) + \epsilon$$</p>  
Thus, $$y \sim \mathcal{N}\left(f(x; \theta), \sigma^{2}\right)$$, and (we assume) there is a distribution $$p(y\vert x)$$ where $$y \sim \mathcal{N}\left(f(x; \theta), \sigma^{2}\right)$$.  
\- Notice that, $$\epsilon = y - \hat{y} \implies $$  
<p>$$\begin{align} 
    \epsilon &\sim \mathcal{N}\left(0, \sigma^{2}\right) \\
            &\sim \frac{1}{\sigma \sqrt{2 \pi}} e^{-\frac{\left(\epsilon\right)^{2}}{2 \sigma^{2}}} \\
            &\sim \frac{1}{\sigma \sqrt{2 \pi}} e^{-\frac{\left(y-\hat{y}\right)^{2}}{2 \sigma^{2}}}
    \end{align}$$</p>  

In LR, the equivalent is:  
We assume that we are given data $$x_{1}, \ldots, x_{n}$$ and outputs $$y_{1}, \ldots, y_{n}$$ where $$x_{i} \in \mathbb{R}^{d}$$ and $$y_{i} \in \mathbb{R}$$ and that there is a distribution $$p(y \vert x)$$ where $$y \sim \mathcal{N}\left(w^{\top} x, \sigma^{2}\right)$$.  
- In other words, we assume that the conditional distribution of $$Y_i \vert \theta$$ is a Gaussian (Each individual term $$p\left(y_{i} \vert \mathbf{x}_ {i}, \boldsymbol{\theta}\right)$$ comes from a Gaussian):  
<p>$$Y_{i} \vert \boldsymbol{\theta} \sim \mathcal{N}\left(h_{\boldsymbol{\theta}}\left(\mathbf{x}_ {i}\right), \sigma^{2}\right)$$</p>  
In other words, we assume that there is a true linear model weighted by some true $$w$$ and the values generated are scattered around it with some error $$\epsilon \sim \mathcal{N}\left(0, \sigma^{2}\right)$$.  
Then we just want to obtain the max likelihood estimation:  
<p>$$\begin{aligned} p(Y \vert X, w) &=\prod_{i=1}^{n} p\left(y_{i} \vert x_{i}, w\right) \\ \log p(\cdot) &=\sum_{i}-\log \left(2 \pi \sigma^{2}\right)-\frac{1}{2 \sigma^{2}}\left(y_{i}-w^{\top} x_{i}\right)^{2} \end{aligned}$$</p>  


<!-- 1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22} -->

<!-- 3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24} -->

***

## Logistic Regression
{: #content3}

The errors are not directly observable, since we never observe the actual probabilities directly.  


__Latent Variable Interpretation:__{: style="color: red"}  
The logistic regression can be understood simply as finding the $$\beta$$ parameters that best fit:  
<p>$$y=\left\{\begin{array}{ll}{1} & {\beta_{0}+\beta_{1} x+\varepsilon>0} \\ {0} & {\text { else }}\end{array}\right.$$</p>  
where $\varepsilon$ is an error distributed by the standard logistic distribution.  
The associated latent variable is $${\displaystyle y'=\beta _{0}+\beta _{1}x+\varepsilon }$$. The error term $$ \varepsilon $$ is __not observed__, and so the $$y'$$ is also an unobservable, hence termed "latent" (the observed data are values of $$y$$ and $$ x$$). Unlike ordinary regression, however, the $$ \beta  $$ parameters cannot be expressed by any direct formula of the $$y$$ and $$ x$$ values in the observed data. Instead they are to be found by an iterative search process.  



__Notes:__{: style="color: red"}  
{: #lst-p}
* Can be used with a polynomial kernel.
* Convex Cost Function
* No closed form solution

<!-- 1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents34}
 -->