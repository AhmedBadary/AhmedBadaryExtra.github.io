---
layout: NotesPage
title: Estimation
permalink: /work_files/research/ml/estimation
prevLink: /work_files/research/ml.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Estimation](#content1)
  {: .TOC1}
  * [Maximum Likelihood Estimation (MLE)](#content2)
  {: .TOC2}
  * [Maximum A Posteriori (MAP) Estimation](#content3)
  {: .TOC3}
  * [](#content4)
  {: .TOC4}
</div>

***
***

[MLE vs MAP Estimation](https://himarora.github.io/machine%20learning/maximum-likelihood-estimation-vs-maximum-a-posteriori-estimation/)  


## Estimation
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

## Maximum Likelihood Estimation (MLE)
{: #content2}

1. **Maximum Likelihood Estimation:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    __Likelihood in Parametric Models:__{: style="color: red"}  
    {: #lst-p}
    Suppose we have a parametric model $$\{p(y ; \theta) \vert \theta \in \Theta\}$$ and a sample $$D=\left\{y_{1}, \ldots, y_{n}\right\}$$:  
    * The likelihood of parameter estimate $$\hat{\theta} \in \Theta$$ for sample $$\mathcal{D}$$ is:  
        <p>$$p(\mathcal{D} ; \hat{\theta})=\prod_{i=1}^{n} p\left(y_{i} ; \hat{\theta}\right)$$</p>  
    * In practice, we prefer to work with the __log-likelihood__.  Same maximum but  
        <p>$$\log p(\mathcal{D} ; \hat{\theta})=\sum_{i=1}^{n} \log p\left(y_{i} ; \theta\right)$$</p>  
        and sums are easier to work with than products.  

    > Likelihood is the probability of the data given the parameters of the model  

    __MLE for Parametric Models:__{: style="color: red"}  
    {: #lst-p}
    The __maximum likelihood estimator (MLE)__ for $$\theta$$ in the (parametric) model $$\{p(y, \theta) \vert \theta \in \Theta\}$$ is:  
    <p>$$\begin{aligned} \hat{\theta} &=\underset{\theta \in \Theta}{\arg \max } \log p(\mathcal{D}, \hat{\theta}) \\ &=\underset{\theta \in \Theta}{\arg \max } \sum_{i=1}^{n} \log p\left(y_{i} ; \theta\right) \end{aligned}$$</p>  

    > You are finding the value of the parameter $$\theta$$ that, if used (in the model) to generate the probability of the data, would make the data most _"likely"_ to occur.  

    * __MLE Intuition__:  
        If I choose a _hypothesis_ $$h$$ underwhich the _observed data_ is very *__plausible__* then the _hypothesis_ is very *__likely__*.  
    * [**Maximum Likelihood as Empirical Risk Minimization**](https://www.youtube.com/embed/JrFj0xpGd2Q?start=2609){: value="show" onclick="iframePopA(event)"}
    <a href="https://www.youtube.com/embed/JrFj0xpGd2Q?start=2609"></a>
        <div markdown="1"> </div>    
    * Finding the MLE is an optimization problem.
    * For some model families, calculus gives a closed form for the MLE
    * Can also use numerical methods we know (e.g. SGD)  


    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * __Why maximize the natural log of the likelihood?__  
        <button>Discussion</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        *   
            1. Numerical Stability: change products to sums  
            2. The logarithm of a member of the family of exponential probability distributions (which includes the ubiquitous normal) is polynomial in the parameters (i.e. max-likelihood reduces to least-squares for normal distributions)  
            $$\log\left(\exp\left(-\frac{1}{2}x^2\right)\right) = -\frac{1}{2}x^2$$   
            3. The latter form is both more numerically stable and symbolically easier to differentiate than the former. It increases the dynamic range of the optimization algorithm (allowing it to work with extremely large or small values in the same way).  
            4. The logarithm is a monotonic transformation that preserves the locations of the extrema (in particular, the estimated parameters in max-likelihood are identical for the original and the log-transformed formulation)  

            * Gradient methods generally work better optimizing $$log_p(x)$$ than $$p(x)$$ because the gradient of $$log_p(x)$$ is generally more __well-scaled__. [link](https://stats.stackexchange.com/questions/174481/why-to-optimize-max-log-probability-instead-of-probability)
                __Justification:__ the gradient of the original term will include a $$e^{\vec{x}}$$ multiplicative term that scales very quickly one way or another, requiring the step-size to equally scale/stretch in the opposite direction.  
        {: hidden=""}

<!--
2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22} -->

<!-- 3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24} -->

***

## Maximum A Posteriori (MAP) Estimation
{: #content3}

<!-- 1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents34}
 -->