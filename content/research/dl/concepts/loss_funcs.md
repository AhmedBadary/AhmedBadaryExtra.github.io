---
layout: NotesPage
title: Loss Functions
permalink: /work_files/research/dl/concepts/loss_funcs
prevLink: /work_files/research/dl/concepts.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Loss Functions](#content1)
  {: .TOC1}
  * [Loss Functions for Regression](#content2)
  {: .TOC2}
  * [Loss Functions for Classification](#content3)
  {: .TOC3}
<!--       * [FOURTH](#content4)
  {: .TOC4}
  * [FIFTH](#content5)
  {: .TOC5}
  * [SIXTH](#content6)
  {: .TOC6} -->
</div>

***
***

[Loss Functions (blog)](https://isaacchanghau.github.io/post/loss_functions/)  
[Information Theory (Cross-Entropy and MLE, MSE, Nash, etc.)](https://jhui.github.io/2017/01/05/Deep-learning-Information-theory/)  


# Loss Functions
{: #content1}


### **Loss Functions**{: style="color: SteelBlue; font-size: 1.27em"}{: .bodyContents1 #bodyContents11}    
Abstractly, a __loss function__ or __cost function__ is a function that maps an event or values of one or more variables onto a real number, intuitively, representing some "cost" associated with the event.  

Formally, a __loss function__ is a function $$L :(\hat{y}, y) \in \mathbb{R} \times Y \longmapsto L(\hat{y}, y) \in \mathbb{R}$$  that takes as inputs the predicted value $$\hat{y}$$ corresponding to the real data value $$y$$ and outputs how different they are.  

***

# Loss Functions for Regression
{: #content2}

![img](/main_files/dl/concepts/loss_funcs/6.png){: width="61%"}  
<br>

### **Introduction**{: style="color: SteelBlue; font-size: 1.27em"}{: .bodyContents2 #bodyContents211}    
Regression Losses usually only depend on the __residual__ $$r = y - \hat{y}$$ (i.e. what you have to add to your prediction to match the target)  

__Distance-Based Loss Functions:__{: style="color: red"}  
A Loss function $$L(\hat{y}, y)$$ is called __distance-based__ if it:  
* Only depends on the __residual__:  
    <p>$$L(\hat{y}, y) = \psi(y-\hat{y})  \:\: \text{for some } \psi : \mathbb{R} \longmapsto \mathbb{R}$$</p>  
* Loss is $$0$$ when residual is $$0$$:  
    <p>$$\psi(0) = 0$$</p>  

__Translation Invariance:__{: style="color: red"}  
Distance-based losses are translation-invariant:  
<p>$$L(\hat{y}+a, y+a) = L(\hat{y}, y)$$</p>  

> Sometimes __Relative-Error__ $$\dfrac{\hat{y}-y}{y}$$ is a more _natural_ loss but it is NOT translation-invariant  


<br>

### **MSE**{: style="color: SteelBlue; font-size: 1.27em"}{: .bodyContents2 #bodyContents21}    
The __MSE__ minimizes the sum of *__squared differences__* between the predicted values and the target values.  
<p>$$L(\hat{y}, y) = \dfrac{1}{n} \sum_{i=1}^{n}\left(y_{i}-\hat{y}_ {i}\right)^{2}$$</p>  
![img](/main_files/dl/concepts/loss_funcs/1.png){: width="30%" .center-image}  

<button>Derivation</button>{: .showText value="show"
onclick="showTextPopHide(event);"}
![img](/main_files/dl/concepts/loss_funcs/5.png){: width="100%" hidden=""}  
<br>

### **MAE**{: style="color: SteelBlue; font-size: 1.27em"}{: .bodyContents2 #bodyContents22}    
The __MAE__ minimizes the sum of *__absolute differences__* between the predicted values and the target values.  
<p>$$L(\hat{y}, y) = \dfrac{1}{n} \sum_{i=1}^{n}\vert y_{i}-\hat{y}_ {i}\vert$$</p>  

__Properties:__{: style="color: red"}  
* Solution may be __Non-unique__  
* __Robustness__ to outliers  
* __Unstable Solutions:__{: #bodyContents22stability}    
    <button>Explanation</button>{: .showText value="show"
    onclick="showTextPopHide(event);"}
    _The instability property of the method of least absolute deviations means that, for a small horizontal adjustment of a datum, the regression line may jump a large amount. The method has continuous solutions for some data configurations; however, by moving a datum a small amount, one could “jump past” a configuration which has multiple solutions that span a region. After passing this region of solutions, the least absolute deviations line has a slope that may differ greatly from that of the previous line. In contrast, the least squares solutions is stable in that, for any small adjustment of a data point, the regression line will always move only slightly; that is, the regression parameters are continuous functions of the data._{: hidden=""}  
* __Data-points "Latching"[^3]:__  
    * __Unique Solution__:  
        If there are $$k$$ *__features__* (including the constant), then at least one optimal regression surface will pass through $$k$$ of the *__data points__*; unless there are multiple solutions.  
    * __Multiple Solutions__:  
        The region of valid least absolute deviations solutions will be __bounded by at least $$k$$ lines__, each of which __passes through at least $$k$$ data points__.  
    > [Wikipedia](https://en.wikipedia.org/wiki/Least_absolute_deviations#Other_properties)  
* 
<br>

### **Huber Loss**{: style="color: SteelBlue; font-size: 1.27em"}{: .bodyContents2 #bodyContents23}    

AKA: __Smooth Mean Absolute Error__  
<p>$$L(\hat{y}, y) = \left\{\begin{array}{cc}{\frac{1}{2}(y-\hat{y})^{2}} & {\text { if }|(y-\hat{y})|<\delta} \\ {\delta(y-\hat{y})-\frac{1}{2} \delta} & {\text { otherwise }}\end{array}\right.$$</p>  

__Properties:__{: style="color: red"}  
* It’s __less sensitive__{: style="color: green"} to outliers than the *MSE* as it treats error as square only inside an interval.  

__Code:__{: style="color: red"}  
```python
def Huber(yHat, y, delta=1.):
    return np.where(np.abs(y-yHat) < delta,.5*(y-yHat)**2 , delta*(np.abs(y-yHat)-0.5*delta))
```
<br>

### **KL-Divergence**{: style="color: SteelBlue; font-size: 1.27em"}{: .bodyContents2 #bodyContents25}  


<p>$$L(\hat{y}, y) = $$</p>  

<br>

### **Analysis and Discussion**{: style="color: SteelBlue; font-size: 1.27em"}{: .bodyContents2 #bodyContents26}  
__MSE vs MAE:__{: style="color: red"}  

| __MSE__ | __MAE__ |
| Sensitive to _outliers_ | Robust to _outliers_ |
| Differentiable Everywhere | Non-Differentiable at $$0$$ |
| Stable[^1] Solutions | Unstable Solutions |
| Unique Solution | Possibly multiple[^2] solutions |

* __Statistical Efficiency__:  
    * "For normal observations MSE is about $$12\%$$ more efficient than MAE" - Fisher  
    * $$1\%$$ Error is enough to make MAE more efficient  
    * 2/1000 bad observations, make the median more efficient than the mean  
* Subgradient methods are slower than gradient descent  
    * you get a lot better convergence rate guarantees for MSE  




<br>

### **Notes**{: style="color: SteelBlue; font-size: 1.27em"}{: .bodyContents2 #bodyContents27}  




***

# Loss Functions for Classification
{: #content3}

![img](/main_files/dl/concepts/loss_funcs/0.png){: width="65%" #losses}  
<br>

### **$$0-1$$ Loss**{: style="color: SteelBlue; font-size: 1.27em"}{: .bodyContents3 #bodyContents311}    

<p>$$L(\hat{y}, y) = I(\hat{y} \neq y) = \left\{\begin{array}{ll}{0} & {\hat{y}=y} \\ {1} & {\hat{y} \neq y}\end{array}\right.$$</p>  
<br>

### **MSE**{: style="color: SteelBlue; font-size: 1.27em"}{: .bodyContents3 #bodyContents31}    

We can write the loss in terms of the margin $$m = y\hat{y}$$:  
$$L(\hat{y}, y)=(y - \hat{y})^{2}=(1-y\hat{y})^{2}=(1-m)^{2}$$   
> Since $$y \in {-1,1} \implies y^2 = 1$$  


<p>$$L(\hat{y}, y) = (1-y \hat{y})^{2}$$</p>  


![img](/main_files/dl/concepts/loss_funcs/1.png){: width="30%" .center-image}  

<button>Derivation</button>{: .showText value="show"
onclick="showTextPopHide(event);"}
![img](/main_files/dl/concepts/loss_funcs/5.png){: width="100%" hidden=""}  

<br>

### **Hinge Loss**{: style="color: SteelBlue; font-size: 1.27em"}{: .bodyContents3 #bodyContents32}    

<p>$$L(\hat{y}, y) = \max (0,1-y \hat{y})=|1-y \hat{y}|_ {+}$$</p>  

__Properties:__{: style="color: red"}  
* Continuous, Convex, Non-Differentiable  

![img](/main_files/dl/concepts/loss_funcs/3.png){: width="30%" .center-image}  
<br>

### **Logistic Loss**{: style="color: SteelBlue; font-size: 1.27em"}{: .bodyContents3 #bodyContents33}  

AKA: __Log-Loss__, __Logarithmic Loss__  

<p>$$L(\hat{y}, y) = \log{\left(1+e^{-y \hat{y}}\right)}$$</p>  

![img](/main_files/dl/concepts/loss_funcs/2.png){: width="30%" .center-image}  

__Properties:__{: style="color: red"}  
{: #lst-p}
* The logistic loss function does not assign zero penalty to any points. Instead, functions that correctly classify points with high confidence (i.e., with high values of $${\displaystyle \vert f({\vec {x}})\vert}$$) are penalized less. This structure leads the logistic loss function to be sensitive to outliers in the data.  
<br>


### **Cross-Entropy (Log Loss)**{: style="color: SteelBlue; font-size: 1.27em"}{: .bodyContents3 #bodyContents34}  

<p>$$L(\hat{y}, y) = -\sum_{i} y_i \log \left(\hat{y}_ {i}\right)$$</p>  

__Binary Cross-Entropy:__{: style="color: red"}  
<p>$$L(\hat{y}, y) = -\left[y \log \hat{y}+\left(1-y\right) \log \left(1-\hat{y}_ {n}\right)\right]$$</p>  

![img](/main_files/dl/concepts/loss_funcs/4.png){: width="30%" .center-image}  


__Cross-Entropy and Negative-Log-Probability:__{: style="color: red"}  
The __Cross-Entropy__ is equal to the __Negative-Log-Probability__ (of predicting the true class) in the case that the true distribution that we are trying to match is *__peaked at a single point__* and is *__identically zero everywhere else__*; this is usually the case in ML when we are using a _one-hot encoded vector_ with one class $$y = [0 \: 0 \: \ldots \: 0 \: 1 \: 0 \: \ldots \: 0]$$ peaked at the $$j$$-th position   
$$\implies$$  
<p>$$L(\hat{y}, y) = -\sum_{i} y_i \log \left(\hat{y}_ {i}\right) = - \log (\hat{y}_ {j})$$</p>  

__Cross-Entropy and Log-Loss:__{: style="color: red"}    
The __Cross-Entropy__ is equal to the __Log-Loss__ in the case of $$0, 1$$ classification.  

__Equivalence of *Binary Cross-Entropy* and *Logistic-Loss*:__  
Given $$p \in\{y, 1-y\}$$ and $$q \in\{\hat{y}, 1-\hat{y}\}$$:  
<p>$$H(p,q)=-\sum_{x }p(x)\,\log q(x) = -y \log \hat{y}-(1-y) \log (1-\hat{y}) = L(\hat{y}, y)$$</p>  

* Notice the following property of the __logistic function__ $$\sigma$$ (used in derivation below):   
    $$\sigma(-x) = 1-\sigma(x)$$  

<button>Derivation</button>{: .showText value="show"
 onclick="showText_withParent_PopHide(event);"}
_Given:_{: hidden=""}  
* $$\hat{y} = \sigma(yf(x))$$,[^5]  
* $$y \in \{-1, 1\}$$,   
* $$\hat{y}' = \sigma(f(x))$$,  
* $$y' = (1+y)/2 = \left\{\begin{array}{ll}{1} & {\text { for }} y' = 1 \\ {0} & {\text { for }} y = -1\end{array}\right. \in \{0, 1\}$$[^4]   
* We start with the modified binary cross-entropy  
    $$\begin{aligned} -y' \log \hat{y}'-(1-y') \log (1-\hat{y}') &= \left\{\begin{array}{ll}{-\log\hat{y}'} & {\text { for }} y' = 1 \\ {-\log(1-\hat{y}')} & {\text { for }} y' = 0\end{array}\right. \\ \\
    &= \left\{\begin{array}{ll}{-\log\sigma(f(x))} & {\text { for }} y' = 1 \\ {-\log(1-\sigma(f(x)))} & {\text { for }} y' = 0\end{array}\right. \\ \\
    &= \left\{\begin{array}{ll}{-\log\sigma(1\times f(x))} & {\text { for }} y' = 1 \\ {-\log(\sigma((-1)\times f(x)))} & {\text { for }} y' = 0\end{array}\right. \\ \\
    &= \left\{\begin{array}{ll}{-\log\sigma(yf(x))} & {\text { for }} y' = 1 \\ {-\log(\sigma(yf(x)))} & {\text { for }} y' = 0\end{array}\right. \\ \\
    &= \left\{\begin{array}{ll}{-\log\hat{y}} & {\text { for }} y' = 1 \\ {-\log\hat{y}} & {\text { for }} y' = 0\end{array}\right. \\ \\
    &= -\log\hat{y} \\ \\
    &= \log\left[\dfrac{1}{\hat{y}}\right] \\ \\
    &= \log\left[\hat{y}^{-1}\right] \\ \\
    &= \log\left[\sigma(yf(x))^{-1}\right] \\ \\
    &= \log\left[ \left(\dfrac{1}{1+e^{-yf(x)}}\right)^{-1}\right] \\ \\
    &= \log \left(1+e^{-yf(x)}\right)\end{aligned}$$  
{: hidden=""}

> [Reference (Understanding binary-cross-entropy-log-loss)](https://towardsdatascience.com/understanding-binary-cross-entropy-log-loss-a-visual-explanation-a3ac6025181a)  


__Cross-Entropy as Negative-Log-Likelihood (w/ equal probability outcomes):__{: style="color: red"}  


__Cross-Entropy and KL-Div:__{: style="color: red"}  
When comparing a distribution $${\displaystyle q}$$ against a fixed reference distribution $${\displaystyle p}$$, cross entropy and KL divergence are identical up to an additive constant (since $${\displaystyle p}$$ is fixed): both take on their minimal values when $${\displaystyle p=q}$$, which is $${\displaystyle 0}$$ for KL divergence, and $${\displaystyle \mathrm {H} (p)}$$ for cross entropy.  
> Basically, minimizing either will result in the same solution.  


__Cross-Entropy VS MSE (& Classification Loss):__{: style="color: red"}  
Basically, CE > MSE because the gradient of MSE $$z(1-z)$$ leads to saturation when then output $$z$$ of a neuron is near $$0$$ or $$1$$ making the gradient very small and, thus, slowing down training.  
CE > Class-Loss because Class-Loss is binary and doesn't take into account _"how well"_ are we actually approximating the probabilities as opposed to just having the target class be slightly higher than the rest (e.g. $$[c_1=0.3, c_2=0.3, c_3=0.4]$$).  
* [Why You Should Use Cross-Entropy Error Instead Of Classification Error Or Mean Squared Error For Neural Network Classifier Training](https://jamesmccaffrey.wordpress.com/2013/11/05/why-you-should-use-cross-entropy-error-instead-of-classification-error-or-mean-squared-error-for-neural-network-classifier-training/)  


<br>


### **Exponential Loss**{: style="color: SteelBlue; font-size: 1.27em"}{: .bodyContents3 #bodyContents35}  

<p>$$L(\hat{y}, y) = e^{-\beta y \hat{y}}$$</p>  
<br>

### **Perceptron Loss**{: style="color: SteelBlue; font-size: 1.27em"}{: .bodyContents3 #bodyContents36}  

<p>$${\displaystyle L(\hat{y}_i, y_i) = {\begin{cases}0&{\text{if }}\ y_i\cdot \hat{y}_i \geq 0\\-y_i \hat{y}_i&{\text{otherwise}}\end{cases}}}$$</p>  
<br>


### **Notes**{: style="color: SteelBlue; font-size: 1.27em"}{: .bodyContents3 #bodyContents37}  
* __Logistic loss__ diverges faster than __hinge loss__ [(image)](#losses). So, in general, it will be more sensitive to outliers. [Reference. Bad info?](https://towardsdatascience.com/support-vector-machine-vs-logistic-regression-94cc2975433f)   


<br><br>

[^1]: [Stability](#bodyContents22stability)  
[^2]: Reason is that the errors are equally weighted; so, tilting the regression line (within a region) will decrease the distance to a particular point and will increase the distance to other points by the same amount.  
[^3]: [Reference](http://articles.adsabs.harvard.edu//full/1982AJ.....87..928B/0000936.000.html)  
[^4]: We have to redefine the indicator/target variable to establish the equality.  
[^5]: $$f(x) = w^Tx$$ in logistic regression  