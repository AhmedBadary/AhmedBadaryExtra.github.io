---
layout: NotesPage
title: Gradient-Based Optimization
permalink: /work_files/research/dl/concepts/grad_opt
prevLink: /work_files/research/dl/concepts.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Gradient-Based Optimization](#content1)
  {: .TOC1}
  * [Gradient Descent](#content2)
  {: .TOC2}
  * [Gradient Descent Variants](#content3)
  {: .TOC3}
  * [Gradient Descent "Optimization"](#content4)
  {: .TOC4}
 * [Parallelizing and distributing SGD](#content5)
  {: .TOC5}
  * [Additional strategies for optimizing SGD](#content6)
  {: .TOC6}
  * [Further Advances in DL Optimization](#content7)
  {: .TOC7}
</div>

***
***

[Optimizing Gradient Descent](http://ruder.io/optimizing-gradient-descent/index.html#gradientdescentoptimizationalgorithms)  
[Blog: SGD, Momentum and Adaptive Learning Rate](https://deepnotes.io/sgd-momentum-adaptive)  
[EE227C Notes: Convex Optimization and Approximation](https://ee227c.github.io/notes/ee227c-notes.pdf)  
[Convex Functions](http://www.princeton.edu/~amirali/Public/Teaching/ORF523/S16/ORF523_S16_Lec7_gh.pdf)  
[Strong Convexity](http://xingyuzhou.org/blog/notes/strong-convexity)  
[Lipschitz continuous gradient (condition)](http://xingyuzhou.org/blog/notes/Lipschitz-gradient)  
[Conjugate Gradient](http://www.seas.ucla.edu/~vandenbe/236C/lectures/cg.pdf)  
[NOTES ON FIRST-ORDER METHODS FOR MINIMIZING SMOOTH FUNCTIONS](http://web.stanford.edu/class/msande318/notes/notes-first-order-smooth.pdf)  
[Gradient Descent (paperspace)](https://blog.paperspace.com/intro-to-optimization-in-deep-learning-gradient-descent/)  
[An Intuitive Introduction to the Hessian for Deep Learning](http://mlexplained.com/2018/02/02/an-introduction-to-second-order-optimization-for-deep-learning-practitioners-basic-math-for-deep-learning-part-1/)  
[NIPS Optimization Lecture!!](https://channel9.msdn.com/Events/Neural-Information-Processing-Systems-Conference/Neural-Information-Processing-Systems-Conference-NIPS-2016/Large-Scale-Optimization-Beyond-Stochastic-Gradient-Descent-and-Convexity)  
[10 Gradient Descent Optimisation Algorithms + Cheat Sheet (Blog!)](https://www.kdnuggets.com/2019/06/gradient-descent-algorithms-cheat-sheet.html)  



## Gradient-Based Optimization
{: #content1}

1. **Gradient-Based Optimization:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    __Gradient Methods__ are algorithms to solve problems of the form:  
    <p>$$\min_{x \in \mathbb{R}^{n}} f(x)$$</p>  
    with the search directions defined by the __gradient__ of the function at the current point.  
    <br>

2. **Gradient-Based Algorithms:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    Examples, include:  
    * __Gradient Descent__: minimizes arbitrary differentiable functions. 
    * __Conjugate Gradient__: minimizes sparse linear systems w/ symmetric & positive-definite matrices.  
    * __Coordinate Descent__: minimizes functions of two variables.  
    <br>

<!-- 3. **Derivation:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  

4. **Choosing the learning rate:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18} -->

***

## Gradient Descent
{: #content2}

1. **Gradient Descent:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    __Gradient Descent__ is a _first-order, iterative_ algorithm to minimize an objective function $$J(\theta)$$ parameterized by a model's parameters $$\theta \in \mathbb{R}^{d}$$ by updating the parameters in the opposite direction of the gradient of the objective function $$\nabla_{\theta} J(\theta)$$  w.r.t. to the parameters.  
    <br>

    
    __Intuition (for derivation):__{: style="color: red"}  
    1. __Local Search from a starting location on a hill__{: style="color: DarkMagenta"}
    1. __Feel around how a small movement/step around your location would change the height of the surrounding hill (is the ground higher or lower)__{: style="color: DarkGray"}
    1. __Make the movement/step consistent as a small fixed step along some direction__{: style="color: Olive"}
    1. __Measure the steepness of the hill at the new location in the chosen direction__{: style="color: MediumBlue"}
    1. __Do so by Approximating the steepness with some local information__{: style="color: Crimson"}
    1. __Find the direction that decreases the steepness the most__{: style="color: SpringGreen"}    

    $$\iff$$ _._{: hidden=""}  

    1. __Local Search from an initial point $$x_0$$ on a function__{: style="color: DarkMagenta"}
    1. __Explore the value of the function at different small nudges around $$x_0$$__{: style="color: DarkGray"}
    1. __Make the nudges consistent as a small fixed step $$\delta$$ along a normalized direction $$\hat{\boldsymbol{u}}$$__{: style="color: Olive"}
    1. __Evaluate the function at the new location $$x_0 + \delta \hat{\boldsymbol{u}}$$__{: style="color: MediumBlue"}
    1. __Do so by Approximating the function w/ first-order information (Taylor expansion)__{: style="color: Crimson"}
    1. __Find the direction $$\hat{\boldsymbol{u}}$$ that minimizes the function the most__{: style="color: SpringGreen"}  
    <br>

2. **Derivation:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}  
    __A small change in $$\boldsymbol{x}$$:__{: style="color: red"}  
    We would like to know how would a small change in $$\boldsymbol{x}$$, namely $$\Delta \boldsymbol{x}$$ would affect the value of the function $$f(x)$$. This will allow us to evaluate the function:  
    <p>$$f(\mathbf{x}+\Delta \mathbf{x})$$</p>  
    to find the direction that makes $$f$$ decrease the fastest.  

    Let's set up $$\Delta \boldsymbol{x}$$, the change in $$\boldsymbol{x}$$, as a fixed step $$\delta$$ along some normalized direction $$\hat{\boldsymbol{u}}$$:  
    <p>$$\Delta \boldsymbol{x} = \delta \hat{\boldsymbol{u}}$$</p>  

    __The Gradient:__{: style="color: red"}  
    The gradient tells us how that _small change in $$f(\mathbf{x}+\Delta \mathbf{x})$$ affects $$f$$_ through the __first-order approximation__:  
    <p>$$f(\mathbf{x}+\Delta \mathbf{x}) \approx f(\mathbf{x})+\Delta \mathbf{x}^{T} \nabla_{\mathbf{x}} f(\mathbf{x})$$</p>  

    In the single variable case, $$f(x+\delta) \approx f(x)+\delta f'(x)$$, we know that $$f\left(x-\delta \operatorname{sign}\left(f^{\prime}(x)\right)\right)$$ is less than $$f(x)$$ for small enough $$\delta$$.  
    <span>We can thus reduce $$f(x)$$ by moving $$x$$ in small steps with the opposite sign of the derivative.</span>{: style="color: goldenrod"}   


    __The Change in $$f$$:__{: style="color: red"}  
    The change in the objective function is:  
    <p>$$\begin{aligned} \Delta f &= f(\boldsymbol{x}_ 0 + \Delta \boldsymbol{x}) - f(\boldsymbol{x}_ 0) \\
        &= f(\boldsymbol{x}_ 0 + \delta \hat{\boldsymbol{u}}) - f(\boldsymbol{x}_ 0)\\
        &= \delta \nabla_x f(\boldsymbol{x}_ 0)^T\hat{\boldsymbol{u}} + \mathcal{O}(\delta^2) \\
        &= \delta \nabla_x f(\boldsymbol{x}_ 0)^T\hat{\boldsymbol{u}} \\
        &\geq -\delta\|\nabla f(\boldsymbol{x}_ 0)\|_ 2
        \end{aligned}
    $$</p>   
    using the first order approximation above.  
    Notice:  
    <p>$$\nabla_x f(\boldsymbol{x}_ 0)^T\hat{\boldsymbol{u}} \in \left[-\|\nabla f(\boldsymbol{x}_ 0)\|_ 2, \|\nabla f(\boldsymbol{x}_ 0)\|_ 2\right]$$</p>  
    since $$\hat{\boldsymbol{u}}$$ is a unit vector; either aligned with $$\nabla_x f(\boldsymbol{x}_ 0)$$ or in the opposite direction; it contributes nothing to the magnitude of the dot product.  

    So, the $$\hat{\boldsymbol{u}}$$ that <span>changes the above inequality to equality, achieves the largest negative value</span>{: style="color: goldenrod"} (moves the most downhill). That vector $$\hat{\boldsymbol{u}}$$ is, then, the one in the negative direction of $$\nabla_x f(\boldsymbol{x}_ 0)$$; the opposite direction of the gradient.  


    __The Directional Derivative:__{: style="color: red"}  
    The directional derivative in direction $$\boldsymbol{u}$$ (a unit vector) is the slope of the function $$f$$ in direction $$\boldsymbol{u}$$. In other words, the directional derivative is the derivative of the function $$f(\boldsymbol{x}+\alpha \boldsymbol{u})$$ with respect to $$\delta$$, evaluated at $$\delta= 0$$.  
    Using the _chain rule_, we can see that $$\frac{\partial}{\partial \delta} f(\boldsymbol{x}+\delta \boldsymbol{u})$$ evaluates to $$\boldsymbol{u}^{\top} \nabla_{\boldsymbol{x}} f(\boldsymbol{x})$$ when $$\delta=0$$.  


    __Minimizing $$f$$:__{: style="color: red"}  
    To minimize $$f$$, we would like to find _the direction in which $$f$$ decreases the fastest_. We do so by using the __directional derivative__:  
    <p>$$\begin{aligned} & \min _{\boldsymbol{u}, \boldsymbol{u}^{\top} \boldsymbol{u}=1} \boldsymbol{u}^{\top} \nabla_{\boldsymbol{x}} f(\boldsymbol{x}) \\
    =& \min_{\boldsymbol{u}, \boldsymbol{u}^{\top} \boldsymbol{u}=1}\|\boldsymbol{u}\|_{2}\left\|\nabla_{\boldsymbol{x}} f(\boldsymbol{x})\right\|_{2} \cos \theta \\
    =& \min_{\boldsymbol{u}} \cos \theta \\ \implies& \boldsymbol{u} = -\nabla_x f(x)\end{aligned}$$</p>    
    by substituting $$\|\boldsymbol{u}\|_2 = 1$$ and ignoring factors that do not depend on $$\boldsymbol{u}$$, we get $$\min_{\boldsymbol{u}} \cos \theta$$; this is minimized when $$\boldsymbol{u}$$ points in the opposite direction as the gradient.  
    Or rather, because $$\hat{\boldsymbol{u}}$$ is a unit vector, we need:  
    <p>$$\hat{\boldsymbol{u}} = - \dfrac{\nabla_x f(x)}{\|\nabla_x f(x)\|_ 2}$$</p>  

    > In other words, the gradient points directly uphill, and the negative gradient points directly downhill.  We can decrease $$f$$ by moving in the direction of the negative gradient.  

    __The method of steepest/gradient descent:__{: style="color: red"}  
    Proposes a new point to decrease the value of $$f$$:  
    <p>$$\boldsymbol{x}^{\prime}=\boldsymbol{x}-\epsilon \nabla_{\boldsymbol{x}} f(\boldsymbol{x})$$</p>  
    where $$\epsilon$$ is the __learning rate__, defined as:  
    <p>$$\epsilon = \dfrac{\delta}{\left\|\nabla_{x} f(x)\right\|_ {2}}$$</p>    

    * [**Derivation Video**](https://www.youtube.com/embed/fpYC7KK5t7A){: value="show" onclick="iframePopA(event)"}
    <a href="https://www.youtube.com/embed/fpYC7KK5t7A"></a>
        <div markdown="1"> </div>    

    <br>

3. **The Learning Rate:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}  
    The __learning rate__ is a hyper-parameter that controls how much we are adjusting the weights of our network with respect the loss gradient.  

    The learning rate comes from a modification of the step-size in the GD derivation.  
    We get the learning rate by employing a simple idea:  
    We have a __fixed step-size__ $$\delta$$ that dictated how much we should be moving in the direction of steepest descent. However, we would like to keep the step-size from being too small or overshooting. The idea is to *__make the step-size proportional to the magnitude of the gradient__* (i.e. some constant multiplied by the magnitude of the gradient):  
    <p>$$\delta = \epsilon \left\|\nabla_{x} f(x)\right\|_ {2}$$</p>   
    If we do so, we get a nice cancellation as follows:  
    <p>$$\begin{aligned}\Delta \boldsymbol{x} &= \delta \hat{\boldsymbol{u}}  \\
        &= -\delta \dfrac{\nabla_x f(x)}{\|\nabla_x f(x)\|_ 2} \\
        &= - \epsilon \left\|\nabla_{x} f(x)\right\|_ {2} \dfrac{\nabla_x f(x)}{\|\nabla_x f(x)\|_ 2} \\
        &= - \dfrac{\epsilon \left\|\nabla_{x} f(x)\right\|_ {2}}{\|\nabla_x f(x)\|_ 2} \nabla_x f(x) \\
        &= - \epsilon \nabla_x f(x)
    \end{aligned}$$</p>  
    where now we have a *__fixed learning rate__* instead of a _fixed step-size_.  

    __Choosing the Learning Rate:__{: style="color: red"}  
    {: #lst-p}
    * __Set it to a small constant__  
    * __Line Search__: evaluate $$f\left(\boldsymbol{x}-\epsilon \nabla_{\boldsymbol{x}} f(\boldsymbol{x})\right)$$ for several values of $$\epsilon$$ and choose the one that results in the smallest objective value.  
        Finds a local minimum along a search direction by solving an optimization problem in 1-D.  
        > e.g. for *__smooth $$f$$__*: __Secant Method__, __Newton-Raphson Method__ (may need Hessian, hard for large dims)  
            for *__non-smooth $$f$$__*: use __direct line search__ e.g. __golden section search__  
        > Note: usually NOT used in DL  
    * __Trust Region Method__  
    * __Grid Search__: is simply an exhaustive searching through a manually specified subset of the hyperparameter space of a learning algorithm. It is guided by some performance metric, typically measured by cross-validation on the training set or evaluation on a held-out validation set.  
    * [__Population-Based Training (PBT)__](https://deepmind.com/blog/article/population-based-training-neural-networks): is an elegant implementation of using a genetic algorithm for hyper-parameter choice.  
        In PBT, a population of models are created. They are all continuously trained in parallel. When any member of the population has had sufficiently long to train to show improvement, its validation accuracy is compared to the rest of the population. If its performance is in the lowest $$20\%$$, then it copies and mutates the hyper-parameters and variables of one of the top $$20\%$$ performers.  
        In this way, the most successful hyper-parameters spawn many slightly mutated variants of themselves and the best hyper-parameters are likely discovered.  
    * __Bayesian Optimization__: is a global optimization method for noisy black-box functions. Applied to hp optimization, it builds a probabilistic model of the function mapping from hp values to the objective evaluated on a validation set. By iteratively evaluating a promising hp configuration based on the current model, and then updating it, it, aims to gather observations revealing as much information as possible about this function and, in particular, the location of the optimum. It tries to balance exploration (hps for which the outcome is most uncertain) and exploitation (hps expected close to the optimum).  
        In practice, it has been shown to obtain better results in fewer evaluations compared to grid search and random search, due to the ability to reason about the quality of experiments before they are run.  
            

    __Line Search VS Trust Region:__  
    Trust-region methods are in some sense dual to line-search methods: trust-region methods first choose a step size (the size of the trust region) and then a step direction, while line-search methods first choose a step direction and then a step size.  


    __Learning Rate Schedule:__{: style="color: red"}  
    A learning rate schedule changes the learning rate during learning and is most often changed between epochs/iterations. This is mainly done with two parameters: __decay__ and __momentum__.  
    * __Decay__: serves to settle the learning in a nice place and avoid oscillations, a situation that may arise when a too high constant learning rate makes the learning jump back and forth over a minima, and is controlled by a hyperparameter.  
    * __Momentum__: is analogous to a ball rolling down a hill; we want the ball to settle at the lowest point of the hill (corresponding to the lowest error). Momentum both speeds up the learning (increasing the learning rate) when the error cost gradient is heading in the same direction for a long time and also avoids local minima by 'rolling over' small bumps.  
            

    __Types of learning rate schedules for Decay:__  
    {: #lst-p}
    * __Time-based__ learning schedules alter the learning rate depending on the learning rate of the previous time iteration. Factoring in the decay the mathematical formula for the learning rate is:  
        <p>$${\displaystyle \eta_{n+1}={\frac {\eta_{n}}{1+dn}}}$$</p>  
        where $$\eta$$ is the learning rate, $$d$$ is a decay parameter and $$n$$ is the iteration step.  
    * __Step-based__ learning schedules changes the learning rate according to some pre defined steps:  
        <p>$${\displaystyle \eta_{n}=\eta_{0}d^{floor({\frac {1+n}{r}})}}$$</p>   
        where $${\displaystyle \eta_{n}}$$ is the learning rate at iteration $$n$$, $$\eta_{0}$$ is the initial learning rate, $$d$$ is how much the learning rate should change at each drop (0.5 corresponds to a halving) and $$r$$ corresponds to the droprate, or how often the rate should be dropped ($$10$$ corresponds to a drop every $$10$$ iterations). The floor function here drops the value of its input to $$0$$ for all values smaller than $$1$$.  
    * __Exponential__ learning schedules are similar to step-based but instead of steps a decreasing exponential function is used. The mathematical formula for factoring in the decay is:  
        <p>$$ {\displaystyle \eta_{n}=\eta_{0}e^{-dn}}$$</p>  
        where $$d$$ is a decay parameter.  
    <br>

4. **Convergence:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}  
    Gradient Descent converges when every element of the gradient is zero, or very close to zero within some threshold.  

    With certain assumptions on $$f$$ (convex, $$\nabla f$$ lipschitz) and particular choices of $$\epsilon$$ (chosen via line-search etc.), convergence to a local minimum can be guaranteed.  
    Moreover, if $$f$$ is convex, all local minima are global minimia, so convergence is to the global minimum.  
    <br>

5. **Choosing (tuning) the hyperparameters:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}  
    We can set/tune most hyperparameters by reasoning about their effect on __model capacity__.  
    <button>Effect of HPs on model capacity</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/uEjsgHkxOZlxf4mXE6XnJYqegpjvoQfKG28_A4nG0Fk.original.fullsize.png){: width="100%" hidden=""}  

    __Important HPs:__  
    {: #lst-p}
    1. Learning Rate  
    1. \# Hidden Units  
    1. Mini-batch Size  
    1. Momentum Coefficient  

    
    __Hyperparameter search:__{: style="color: red"}  
    Sample at random in a grid (hypercube) of different parameters, then zoom in to a tighter range of "good" values.  
    Search (sample) on a logarithmic scale to get uniform sizes between values:  
    * Select value $$r \in [a, b]$$ (e.g. $$\in [-4, 0]$$, and set your hp as $$10^r$$ (e.g. $$\epsilon = 10^{r}$$). You'll be effectively sampling $$\in [10^{-4}, 10^0] \iff [0.0001, 1]$$.  
    <br>

8. **Notes:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents28}  
    * Gradient descent can be viewed as __applying Euler's method for solving ordinary differential equations $${\displaystyle x'(t)=-\nabla f(x(t))}$$ to a [gradient flow](https://en.wikipedia.org/wiki/Vector_field#Gradient_field_in_euclidean_spaces)__.  
    * Neural nets are unconstrained optimization problems with many, many local minima. They sometimes benefit from line search or second-order optimization algorithms, but when the input data set is very large, researchers often favor the dumb, blind, stochastic versions of gradient descent.  
    * Grid search suffers from the curse of dimensionality, but is often embarrassingly parallel because typically the hyperparameter settings it evaluates are independent of each other.  
    <br>

***

## Gradient Descent Variants
{: #content3}

There are three variants of gradient descent, which differ in the amount of data used to compute the gradient. The amount of data imposes a trade-off between the accuracy of the parameter updates and the time it takes to perform the update.  


1. **Batch Gradient Descent:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}  
    __Batch Gradient Descent__ AKA __Vanilla Gradient Descent__, computes the gradient of the objective wrt. the parameters $$\theta$$ for the entire dataset:  
    <p>$$\theta=\theta-\epsilon \cdot \nabla_{\theta} J(\theta)$$</p>  

    Since we need to compute the gradient for the entire dataset for each update, this approach can be very slow and is intractable for datasets that can't fit in memory.  
    Moreover, batch-GD doesn't allow for an _online_ learning approach.  
    <br>

2. **Stochastic Gradient Descent:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}  
    __SGD__ performs a parameter update for each data-point:  
    <p>$$\theta=\theta-\epsilon \cdot \nabla_{\theta} J\left(\theta ; x^{(i)} ; y^{(i)}\right)$$</p>  

    SGD exhibits a lot of fluctuation and has a lot of variance in the parameter updates. However, although, SGD can potentially move in the wrong direction due to limited information; in-practice, if we slowly decrease the learning-rate, it shows the same convergence behavior as batch gradient descent, almost certainly converging to a local or the global minimum for non-convex and convex optimization respectively.  
    Moreover, the fluctuations it exhibits enables it to jump to new and potentially better local minima.  

    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * __Why reduce the learning rate after every epoch?__  
        This is due to the fact that the random sampling of batches acts as a source of noise which might make SGD keep oscillating around the minima without actually reaching it.  
        It is necessary to guarantee convergence.  
    * __The following conditions guarantee convergence under convexity conditions for SGD__:  
        <p>$$\begin{array}{l}{\sum_{k=1}^{\infty} \epsilon_{k}=\infty, \quad \text { and }} \\ {\sum_{k=1}^{\infty} \epsilon_{k}^{2}<\infty}\end{array}$$</p>  
    * [Stochastic Gradient Descent Escapes Saddle Points Efficiently (M.J.)](https://arxiv.org/pdf/1902.04811.pdf)  
            
    <br>

3. **Mini-batch Gradient Descent:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}   
    A hybrid approach that perform updates for a, pre-specified, mini-batch of $$n$$ training examples:  
    <p>$$\theta=\theta-\epsilon \cdot \nabla_{\theta} J\left(\theta ; x^{(i : i+n)} ; y^{(i : i+n)}\right)$$</p>

    This allows it to:  
    1. Reduce the variance of the parameter updates $$\rightarrow$$ more stable convergence
    2. Makes use of matrix-vector highly optimized libraries  

<!-- 4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents34}  

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents35}  

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents36}  

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents37}  

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents38}   -->


***

## Gradient Descent "Optimization"
{: #content4}

![img](https://cdn.mathpix.com/snip/images/CPfGpiDoF2QyJoFL6LpF-cNWlH9CKUf7yA2trb3mxVE.original.fullsize.png){: width="30%"}  
$$\:$$ _Evolutionary Map Of Optimizers_

1. **Challenges in vanilla approaches to gradient descent:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents41}  
    All the variants described above, however, do not guarantee _"good" convergence_ due to some challenges:  
    * Choosing a proper learning rate is usually difficult:  
        A learning rate that is too small leads to painfully slow convergence, while a learning rate that is too large can hinder convergence and cause the loss function to fluctuate around the minimum or even to diverge.  
    *  Learning rate schedules[^1] try to adjust the learning rate during training by e.g. annealing, i.e. reducing the learning rate according to a pre-defined schedule or when the change in objective between epochs falls below a threshold. These schedules and thresholds, however, have to be defined in advance and are thus unable to adapt to a dataset's characteristics[^2].  
    * The learning rate is _fixed_ for all parameter updates:  
        If our data is sparse and our features have very different frequencies, we might not want to update all of them to the same extent, but perform a larger update for rarely occurring features.  
    * Another key challenge of minimizing highly non-convex error functions common for neural networks is avoiding getting trapped in their numerous suboptimal local minima. Dauphin et al.[^3] argue that the difficulty arises in fact not from local minima but from saddle points, i.e. points where one dimension slopes up and another slopes down. These saddle points are usually surrounded by a plateau of the same error, which makes it notoriously hard for SGD to escape, as the gradient is close to zero in all dimensions.  
    <br>

22. **Preliminaries - Important Concepts:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents422}  
    __Exponentially Weighted Averages:__{: style="color: red"}  
    [EWAs (NG)](https://www.youtube.com/watch?v=lAq96T8FkTw&list=PLkDaE6sCZn6Hn0vK8co82zjQtt3T2Nkqc&index=17)  
    <p>$$v_{t}=\beta v_{t-1}+ (1-\beta) \theta_{t}$$</p>  
    You can think of $$v_t$$ as approximately averaging over $$\approx \dfrac{1}{1-\beta}$$ previous values $$\theta_i$$.  

    The _larger_ the $$\beta$$ the _slower_ $$v_t$$ adapts to changes in (new) $$\theta$$ and the _less_ __noisy__ the value of $$v_t$$.  

    __Intuition:__{: style="color: brown"}  
    It is a recursive equation. Thus, 
    <p>$$v_{100} = (1-\beta) \theta_{100} + (1-\beta)\beta \theta_{99} + (1-\beta)\beta^{2} \theta_{98} + (1-\beta)\beta^{3} \theta_{97} + (1-\beta)\beta^{4} \theta_{96} + \ldots + (1-\beta)\beta^{100} \theta_{1}$$</p>  
    * It is an element-wise product between the values of $$\theta_i$$ and an __exponentially decaying__ function $$v(i)$$.  
        For _$$ T=100, \beta=0.9$$_:  
        ![img](https://cdn.mathpix.com/snip/images/e4SvtXH_4R88TdhgIJmfbhSMgTqc4lt5QJOnpi-hBuw.original.fullsize.png){: width="34%"}  
    * The sum of the coefficients of $$\theta_i$$ is equal to $$\approx 1$$   
        > But not exactly $$1$$ which is why __bias correction__ is needed.  
    * It takes about $$(1-\beta)^{\dfrac{1}{\beta}}$$ time-steps for $$v$$ to decay to about a third of its peak value. So, after $$(1-\beta)^{\dfrac{1}{\beta}}$$ steps, the weight decays to about a third of the weight of the current time-step $$\theta$$ value.  
        In general:   
        <p>$$(1-\epsilon)^{\dfrac{1}{\epsilon}} \approx \dfrac{1}{e} \approx 0.35 \approx \dfrac{1}{3}$$</p>    
    [EWAs Intuition (NG)](https://www.youtube.com/watch?v=NxTFlzBjS-4&list=PLkDaE6sCZn6Hn0vK8co82zjQtt3T2Nkqc&index=18)  
    <br>
    <br>

    __Exponentially Weighted Averages Bias Correction:__{: style="color: red"}  

    __The Problem:__{: style="color: brown"}  
    The estimate of the first value $$\theta_1$$ will not be a good estimate of because it will be multiplied by $$(1-\beta) << 1$$. This will be a much lower estimate especially during the initial phase of the estimate. It will produce the _purple_ curve instead of the _green_ curve:  
    ![img](https://cdn.mathpix.com/snip/images/_IAbXpX9_bnr1pvchJG3UxN-354OAsrmDoFpFYocI8g.original.fullsize.png){: width="50%"}  

    __Bias Correction:__{: style="color: brown"}    
    Replace $$v_t$$ with:  
    $$\:\:\:\:\:\: \dfrac{v_{t}}{1-\beta^{t}}$$   
    * __Small $$t$$:__ $$\implies \beta^t$$ is large $$\implies \dfrac{1}{1-\beta^t}$$ is large  
    * __Large $$t$$__: $$\implies \beta^t$$ is small $$\implies \dfrac{1}{1-\beta^t} \approx 1$$  
    <br> 


2. **Momentum:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents42}  
    __Motivation:__{: style="color: red"}  
    SGD has trouble navigating _ravines_ (i.e. areas where the surface curves much more steeply in one dimension than in another[^4]) which are common around local optima.  
    In these scenarios, SGD oscillates across the slopes of the ravine while only making hesitant progress along the bottom towards the local optimum.  

    __Momentum:__{: style="color: red"}  
    __Momentum__[^5] is a method that helps accelerate SGD in the relevant direction and dampens oscillations (image^). It does this by adding a fraction $$\gamma$$ of the update vector of the past time step to the current update vector:  
    <p>$$\begin{aligned} v_{t} &=\gamma v_{t-1}+\eta \nabla_{\theta} J(\theta) \\ \theta &=\theta-v_{t} \end{aligned}$$</p>  
    > Note: Some implementations exchange the signs in the equations. The momentum term $$\gamma$$ is usually set to $$0.9$$ or a similar value, and $$v_0 = 0$$.  

    ![img](https://cdn.mathpix.com/snip/images/jnTKkZmZsRZXw_8BNtgUxb7tZEg68sgRCspxVOmTw0I.original.fullsize.png){: width="70%"}  

    Essentially, when using momentum, we push a ball down a hill. The ball accumulates momentum as it rolls downhill, becoming faster and faster on the way (until it reaches its terminal velocity if there is air resistance, i.e.  $$\gamma < 1$$). The same thing happens to our parameter updates: The momentum term increases for dimensions whose gradients point in the same directions and reduces updates for dimensions whose gradients change directions. As a result, we gain faster convergence and reduced oscillation.  
    In this case we think of the equation as:  
    <p>$$v_{t} =\underbrace{\gamma}_{\text{friction }} \: \underbrace{v_{t-1}}_{\text{velocity}}+\eta \underbrace{\nabla_{\theta} J(\theta)}_ {\text{acceleration}}$$</p>  
    > Instead of using the gradient to change the position of the weight "particle," use it to change the velocity. - Hinton  


    * [**Momentum NG**](https://www.youtube.com/embed/k8fTYJPd3_I){: value="show" onclick="iframePopA(event)"}
    <a href="https://www.youtube.com/embed/k8fTYJPd3_I"></a>
        <div markdown="1"> </div>    
        __Momentum Calculation (EWAs):__  
        <p>$$\begin{align} 
            v_{dw} &= \beta\:v_{dw}+(1-\beta) dw \\ 
            v_{db} &=\beta\:v_{db}+(1-\beta) db \end{align}$$</p>  
        __Parameter Updates:__  
        <p>$$\begin{align} 
            w &= w - \epsilon\:v_{dw} \\ 
            b &= b - \epsilon\:v_{d_b} \end{align}$$</p>  
    * [**Why Momentum Really Works (distill)**](https://distill.pub/2017/momentum/){: value="show" onclick="iframePopA(event)"}
    <a href="https://distill.pub/2017/momentum/"></a>
        <div markdown="1"> </div>    

    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * Bias Correction is NOT used in practice; only 10 iterations needed to catch up.  
    * The $$(1-\beta)$$ coefficient usually gets dropped in the literature. The effect is that that lr needs to be rescaled which is not a problem.  
    * [Learning representations by back-propagating errors (Rumelhart, Hinton)](https://www.iro.umontreal.ca/~vincentp/ift3395/lectures/backprop_old.pdf)  
    * [visualizing Momentum (video)](https://www.youtube.com/watch?v=7HZk7kGk5bU)  
    <br>


3. **Nesterov Accelerated Gradient:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents43}  
    __Motivation:__{: style="color: red"}  
    Momentum is good, however, a ball that rolls down a hill, blindly following the slope, is highly unsatisfactory. We'd like to have a smarter ball, a ball that has a notion of where it is going so that it knows to slow down before the hill slopes up again.  

    __Nesterov Accelerated Gradient (NAG):__{: style="color: red"}  
    __NAG__[^6] is a way to five our momentum term this kind of prescience. Since we know that we will use the momentum term $$\gamma\:v_{t-1}$$ to move the parameters $$\theta$$, we can compute a rough approximation of the next position of the parameters with $$\theta - \gamma v_{t-1}$$ (w/o the gradient). This allows us to, effectively, look ahead by calculating the gradient not wrt. our current parameters $$\theta$$ but wrt. the approximate future position of our parameters:  
    <p>$$\begin{aligned} v_{t} &=\gamma v_{t-1}+\eta \nabla_{\theta} J\left(\theta-\gamma v_{t-1}\right) \\ \theta &=\theta-v_{t} \end{aligned}$$</p>  
    > $$\gamma = 0.9$$,  

    While Momentum first computes the current gradient (small blue vector) and then takes a big jump in the direction of the updated accumulated gradient (big blue vector), NAG first makes a big jump in the direction of the previous accumulated gradient (brown vector), measures the gradient and then makes a correction (red vector), which results in the complete NAG update (green vector). This anticipatory update prevents us from going too fast and results in increased responsiveness, which has significantly increased the performance of RNNs on a number of tasks[^7].  
    ![img](https://cdn.mathpix.com/snip/images/Gf7UUuUreRzopC-75FXkehiXbEkrtVJjiwIDSMBtJzw.original.fullsize.png){: width="40%"}  

    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * This really helps the optimization of __recurrent neural networks__[^8]  
    * Momentum allows us to __adapt our updates to the slope of our error function__ and speed up SGD  
    * [A Dynamical Systems Perspective on Nesterov Acceleration (M.Jordan)](https://arxiv.org/pdf/1905.07436.pdf)  
    <br> 

4. **Adagrad:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents44}  
    __Motivation:__{: style="color: red"}  
    Now that we are able to __adapt our updates to the slope of our error function__{: style="color: goldenrod"} and speed up SGD in turn, we would also like to __adapt our updates to each individual parameter__{: style="color: goldenrod"} to perform larger or smaller updates depending on their importance.  
    > The magnitude of the gradient can be very different for different weights and can change during learning: This makes it <span>hard to choose single global learning rate</span>{: style="color: goldenrod"}.  - Hinton


    __Adagrad:__{: style="color: red"}  
    __Adagrad__[^9] is an algorithm for gradient-based optimization that does just this: It adapts the learning rate to the parameters, performing smaller updates (i.e. low learning rates) for parameters associated with frequently occurring features, and larger updates (i.e. high learning rates) for parameters associated with infrequent features.  

    __Adagrad per-parameter update:__  
    Adagrad uses a different learning rate for every parameter $$\theta_i$$ at every time step $$t$$, so, we first show Adagrad's per-parameter update.  
    
    The SGD update for every parameter $$\theta_i$$ at each time step $$t$$ is:  
    <p>$$\theta_{t+1, i}=\theta_{t, i}-\eta \cdot g_{t, i}$$</p>  
    where $$g_{t, i}=\nabla_{\theta} J\left(\theta_{t, i}\right)$$, is the partial derivative of the objective function w.r.t. to the parameter $$\theta_i$$ at time step $$t$$, and $$g_{t}$$ is the gradient at time-step $$t$$.  

    In its update rule, Adagrad modifies the general learning rate $$\eta$$ at each time step $$t$$ for every parameter $$\theta_i$$ based on the past gradients that have been computed for $$\theta_i$$:  
    <p>$$\theta_{t+1, i}=\theta_{t, i}-\frac{\eta}{\sqrt{G_{t, i i}+\epsilon}} \cdot g_{t, i}$$</p>  

    $$G_t \in \mathbb{R}^{d \times d}$$ here is a diagonal matrix where each diagonal element $$i, i$$ is the sum of the squares of the gradients wrt $$\theta_i$$ up to time step $$t$$[^12], while $$\epsilon$$ is a smoothing term that avoids division by zero ($$\approx 1e - 8$$).  
    > Without the sqrt, the algorithm performs __much worse__  

    As $$G_t$$ contains the sum of the squares of the past gradients w.r.t. to all parameters $$\theta$$ along its diagonal, we can now vectorize our implementation by performing a matrix-vector product $$\odot$$ between $$G_t$$ and  $$g_t$$:  
    <p>$$\theta_{t+1}=\theta_{t}-\frac{\eta}{\sqrt{G_{t}+\epsilon}} \odot g_{t}$$</p>  


    __Properties:__{: style="color: red"}  
    {: #lst-p}
    * Well-suited for dealing with __sparse data__ (because it adapts the lr of each parameter wrt __feature frequency__)  
        * Pennington et al.[^11] used Adagrad to train GloVe word embeddings, as infrequent words require much larger updates than frequent ones.  
    * __Eliminates need for manual tuning of lr__:  
        One of Adagrad's main benefits is that it eliminates the need to manually tune the learning rate. Most implementations use a default value of $$0.01$$ and leave it at that.  
    * __Weakness -> Accumulation of the squared gradients in the denominator__:  
        Since every added term is positive, the accumulated sum keeps growing during training. This in turn causes the learning rate to shrink and eventually become infinitesimally small, at which point the algorithm is no longer able to acquire additional knowledge.  
    * [Visualization - How adaptive gradient methods speedup convergence](https://www.youtube.com/watch?v=Cy2g9_hR-5Y)  
    <br>

5. **Adadelta:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents45}  
    __Motivation:__{: style="color: red"}  
    __Adagrad__ has a weakness where it suffers from __aggressive, monotonically decreasing lr__{: style="color: goldenrod"} by _accumulation of the squared gradients in the denominator_. The following algorithm aims to resolve this flow.    

    __Adadelta:__{: style="color: red"}  
    Adadelta[^13] is an extension of Adagrad that seeks to reduce its aggressive, monotonically decreasing learning rate. Instead of accumulating all past squared gradients, Adadelta restricts the window of accumulated past gradients to some fixed size $$w$$.  

    Instead of inefficiently storing $$w$$ previous squared gradients, the sum of gradients is recursively defined as a decaying average of all past squared gradients. The running average $$E\left[g^{2}\right]_ {t}$$ at time step $$t$$ then depends (as a fraction $$\gamma$$ similarly to the Momentum term) only on the previous average and the current gradient:  
    <p>$$E\left[g^{2}\right]_{t}=\gamma E\left[g^{2}\right]_{t-1}+(1-\gamma) g_{t}^{2}$$</p>  

    We set $$\gamma$$ to a similar value as the momentum term, around $$0.9$$.  
    For clarity, we now rewrite our vanilla SGD update in terms of the parameter update vector $$\Delta \theta_{t}$$:
    <p>$$\begin{aligned} \Delta \theta_{t} &=-\eta \cdot g_{t, i} \\ \theta_{t+1} &=\theta_{t}+\Delta \theta_{t} \end{aligned}$$</p>  

    In the __parameter update vector__ of Adagrad, we replace the diagonal matrix $$G_t$$ with the _decaying average over past squared gradients_ $$E[g^2]_ t$$:  
    <p>$$-\frac{\eta}{\sqrt{E[g^2]_ t+\epsilon}} \odot g_{t}$$</p>  
    Since the denominator is just the __root mean squared (RMS) error criterion__ _of the gradient_, we can replace it with the criterion short-hand:  
    <p>$$-\frac{\eta}{RMS[g]_{t}} \odot g_{t}$$</p>  

    This __*modified* parameter update vector__ does NOT have the same __hypothetical units__ as the parameter.  
    We accomplish this by first defining another __exponentially decaying average__, this time not of squared gradients but __of squared parameter updates__:  
    <p>$$E[\Delta \theta^2]_t = \gamma E[\Delta \theta^2]_{t-1} + (1 - \gamma) \Delta \theta^2_t$$</p>  
    The __RMS Error of parameter updates__ is thus:  
    <p>$$RMS[\Delta \theta]_ {t} = \sqrt{E[\Delta \theta^2]_ t + \epsilon}$$</p>  

    Since $$RMS[\Delta \theta]_ {t}$$ is __unknown__, we approximate it with the $$RMS$$ of parameter updates up to (until) the previous time step. Replacing the learning rate $$\eta$$ in the previous update rule with $$RMS[\Delta \theta]_ {t-1}$$ finally yields the Adadelta update rule:  
    <p>$$\begin{align}  \begin{split}  \Delta \theta_t &= - \dfrac{RMS[\Delta \theta]_{t-1}}{RMS[g]_{t}} g_{t} \\  \theta_{t+1} &= \theta_t + \Delta \theta_t  \end{split}  \end{align}$$</p>  
    <br>

    __Properties:__{: style="color: red"}  
    {: #lst-p}
    * __Eliminates need for lr completely__:  
        With Adadelta, we do not even need to set a default learning rate, as it has been eliminated from the update rule.  
    <br>


6. **RMSprop:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents46}  
    __Motivation:__   
    RMSprop and Adadelta have both been developed independently around the same time stemming from the need to __resolve Adagrad's radically diminishing learning rates__.  

    __RMSprop:__{: style="color: red"}  
    __RMSprop__ is an unpublished, adaptive learning rate method proposed by Geoff Hinton in [Lecture 6e of his Coursera Class](http://www.cs.toronto.edu/~tijmen/csc321/slides/lecture_slides_lec6.pdf).  

    RMSprop in fact is identical to the first update vector of Adadelta that we derived above:  
    <p>$$\begin{align}  \begin{split}  E[g^2]_t &= 0.9 E[g^2]_{t-1} + 0.1 g^2_t \\  \theta_{t+1} &= \theta_{t} - \dfrac{\eta}{\sqrt{E[g^2]_t + \epsilon}} g_{t}  \end{split}  \end{align}$$</p>  

    RMSprop as well __divides the learning rate by an exponentially decaying average of squared gradients__{: style="color: goldenrod"}.  
    Hinton suggests $$\gamma$$ to be set to $$0.9$$, while a good default value for the learning rate $$\eta$$ is $$0.001$$.  


    __RMSprop as an extension of Rprop:__{: style="color: red"}  
    Hinton, actually, thought of RMSprop as a way of extending _Rprop_ to work with __mini-batches__.  
    <button>Why Rprop does not work with mini-batches?</button>{: .showText value="show"
     onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/KxK61epXdFZw6Rqb7mwqXSIDUouk-TWeNdLu3M_wBFU.original.fullsize.png){: width="60%" hidden=""}  

    __Rprop:__ is equivalent to using the gradient but also dividing by the magnitude of the gradient.  
    The problem with mini-batch rprop is that we divide by a different number for each mini-batch.  
    So why not __force the number we divide by to be very similar for adjacent mini-batches__?  
    That is the idea behind RMSprop.  
    <br>

    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * It is of note that Hinton has tried to add _momentum_ to RMSprop and found that "it does not help as much as it normally does - needs more investigation".  
    * [Visualizing Rprop - How adaptive gradient methods speedup convergence](https://www.youtube.com/watch?v=Cy2g9_hR-5Y)  
    <br>

7. **Adam:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents47}  
    __Motivation:__  
    Adding __momentum__ to Adadelta/RMSprop.  

    __Adam:__{: style="color: red"}  
    __Adaptive Moment Estimation (Adam)__[^14] is another method that computes adaptive learning rates for each parameter. In addition to storing an exponentially decaying average of past squared gradients $$v_t$$ like Adadelta and RMSprop, Adam also keeps an exponentially decaying average of past gradients $$m_t$$, similar to momentum.  

    __Adam VS Momentum:__  
    Whereas momentum can be seen as a ball running down a slope, Adam behaves like a heavy ball with friction, which thus prefers flat minima in the error surface[^15].  

    We compute the decaying averages of past and past squared gradients $$m_t$$ and $$v_t$$ respectively as follows:  
    <p>$$\begin{align}  \begin{split}  m_t &= \beta_1 m_{t-1} + (1 - \beta_1) g_t \\  v_t &= \beta_2 v_{t-1} + (1 - \beta_2) g_t^2  \end{split}  \end{align}$$</p>  

    $$m_t$$ and $$v_t$$ are estimates of the first moment (the mean) and the second moment (the uncentered variance) of the gradients respectively, hence the name of the method.  
    As $$m_t$$ and $$v_t$$ are initialized as vectors of $$0$$'s, the authors of Adam observe that they are biased towards zero, especially during the initial time steps, and especially when the decay rates are small (i.e. $$\beta_1$$ and $$\beta_2$$ are close to $$1$$).  

    They counteract these biases by computing bias-corrected first and second moment estimates:  
    <p>$$\begin{align}  \begin{split}  \hat{m}_ t &= \dfrac{m_t}{1 - \beta^t_1} \\  \hat{v}_ t &= \dfrac{v_t}{1 - \beta^t_2} \end{split}  \end{align}$$</p>  

    They then use these to update the parameters just as we have seen in Adadelta and RMSprop, which yields the Adam update rule:
    <p>$$\theta_{t+1} = \theta_{t} - \dfrac{\eta}{\sqrt{\hat{v}_ t} + \epsilon} \hat{m}_ t$$</p>  

    The authors propose default values of $$0.9$$ for $$\beta_1$$, $$0.999$$ for $$\beta_2$$, and $$10^{ −8}$$ for $$\epsilon$$. They show empirically that Adam works well in practice and compares favorably to other adaptive learning-method algorithms.  
    <br>

8. **[AdaMax](http://ruder.io/optimizing-gradient-descent/index.html#adamax)**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents48}  

9. **[Nadam](http://ruder.io/optimizing-gradient-descent/index.html#nadam)**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents49}  

10. **[AMSGrad](http://ruder.io/optimizing-gradient-descent/index.html#amsgrad):**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents410}  
    __Motivation:__{: style="color: red"}  
    Adaptive LR methods fail to converge to an optimal solution in some cases, e.g. for object recognition [[17]](https://ruder.io/optimizing-gradient-descent/index.html#fn17) or machine translation [[18]](https://ruder.io/optimizing-gradient-descent/index.html#fn18).  
    Reddi et al. (2018) [[19]](https://ruder.io/optimizing-gradient-descent/index.html#fn19) formalize this issue and pinpoint the exponential moving average of past squared gradients as a reason for the poor generalization behaviour of adaptive learning rate methods.

    In settings where Adam converges to a suboptimal solution, it has been observed that some minibatches provide large and informative gradients, but as these minibatches only occur rarely, exponential averaging diminishes their influence, which leads to poor convergence.  
    To fix this behaviour, the authors propose a new algorithm, AMSGrad that uses the maximum of past squared gradients $$v_t$$ rather than the exponential average to update the parameters.  

    Instead of using $$v_{t}$$ (or its bias-corrected version $$\hat{v}_{t}$$) directly, we now employ the previous $$v_{t-1}$$ if it is larger than the current one:  
    $$\hat{v}_{t}=\max \left(\hat{v}_{t-1}, v_{t}\right)$$  

    This way, AMSGrad results in a *__non-increasing step size__*, which avoids the problems suffered by Adam. For simplicity, the authors also remove the debiasing step that we have seen in Adam.


    __Parameter Updates:__{: style="color: red"}  
    <p>$$
    \begin{aligned}
    m_{t} &=\beta_{1} m_{t-1}+\left(1-\beta_{1}\right) g_{t} \\
    v_{t} &=\beta_{2} v_{t-1}+\left(1-\beta_{2}\right) g_{t}^{2} \\
    \hat{v}_{t} &=\max \left(\hat{v}_{t-1}, v_{t}\right) \\
    \theta_{t+1} &=\theta_{t}-\frac{\eta}{\sqrt{\hat{v}_{t}}+\epsilon} m_{t}
    \end{aligned}
    $$</p>

    TLDR: AMSGrad = Adam but always divide by max $$\hat{v}_ i$$ for $$i \in [1, t]$$.   
    <br>


11. **Visualization of the Algorithms**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents411}  
    __SGD optimization on loss surface contours:__{: style="color: red"}  
    ![img](/main_files/dl/concepts/grad_opt/1.gif){: width="100%"}  

    We see their behavior on the contours of a loss surface (the Beale function) over time. Note that Adagrad, Adadelta, and RMSprop almost immediately head off in the right direction and converge similarly fast, while Momentum and NAG are led off-track, evoking the image of a ball rolling down the hill. NAG, however, is quickly able to correct its course due to its increased responsiveness by looking ahead and heads to the minimum.  

    <br>

    __SGD optimization on saddle point:__{: style="color: red"}  
    ![img](/main_files/dl/concepts/grad_opt/2.gif){: width="100%"}  

    Image shows the behavior of the algorithms at a saddle point, i.e. a point where one dimension has a positive slope, while the other dimension has a negative slope, which pose a difficulty for SGD as we mentioned before. Notice here that SGD, Momentum, and NAG find it difficulty to break symmetry, although the two latter eventually manage to escape the saddle point, while Adagrad, RMSprop, and Adadelta quickly head down the negative slope.  


    __Analysis:__{: style="color: red"}  
    As we can see, the adaptive learning-rate methods, i.e. Adagrad, Adadelta, RMSprop, and Adam are most suitable and provide the best convergence for these scenarios.  


    [__Tutorial for Visualization__](http://louistiao.me/notes/visualizing-and-animating-optimization-algorithms-with-matplotlib/)  


12. **Analysis - Choosing an Optimizer:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents412}  
    * __Sparse Input Data__:  
        If your input data is sparse, then you likely achieve the best results using one of the adaptive learning-rate methods. An additional benefit is that you won't need to tune the learning rate but likely achieve the best results with the default value.  

    In summary, RMSprop is an extension of Adagrad that deals with its radically diminishing learning rates. It is identical to Adadelta, except that Adadelta uses the RMS of parameter updates in the numerator update rule. Adam, finally, adds bias-correction and momentum to RMSprop. Insofar, RMSprop, Adadelta, and Adam are very similar algorithms that do well in similar circumstances. Kingma et al.[^14] show that its bias-correction helps Adam slightly outperform RMSprop towards the end of optimization as gradients become sparser. Insofar, Adam might be the best overall choice.  

    Interestingly, many recent papers use vanilla SGD without momentum and a simple learning rate annealing schedule. As has been shown, SGD usually achieves to find a minimum, but it might take significantly longer than with some of the optimizers, is much more reliant on a robust initialization and annealing schedule, and may get stuck in saddle points rather than local minima. Consequently, if you care about fast convergence and train a deep or complex neural network, you should choose one of the adaptive learning rate methods.

***

## [Parallelizing and distributing SGD](http://ruder.io/optimizing-gradient-descent/index.html#parallelizinganddistributingsgd)  
{: #content5}


***

## [Additional strategies for optimizing SGD](http://ruder.io/optimizing-gradient-descent/index.html#additionalstrategiesforoptimizingsgd)  
{: #content6}

<p class="message" markdown="1">For a great overview of some other common tricks, refer to[^24]</p>  



1. **[Shuffling and Curriculum Learning](http://ruder.io/optimizing-gradient-descent/index.html#shufflingandcurriculumlearning):**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents61}  
    Generally, we want to avoid providing the training examples in a meaningful order to our model as this may bias the optimization algorithm. Consequently, it is often a good idea to shuffle the training data after every epoch.  

    On the other hand, for some cases where we aim to solve progressively harder problems, supplying the training examples in a meaningful order may actually lead to improved performance and better convergence. The method for establishing this meaningful order is called Curriculum Learning[^25].  

    Zaremba and Sutskever[^26] were only able to train LSTMs to evaluate simple programs using Curriculum Learning and show that a combined or mixed strategy is better than the naive one, which sorts examples by increasing difficulty.  

    > Note: _"Generally, we want to avoid providing the training examples in a meaningful order to our model as this may bias the optimization algorithm."_  
        Yes, ok, but this is just the kind of bias that we want to introduce to the network.  

    <br>

2. **[Batch Normalization](http://ruder.io/optimizing-gradient-descent/index.html#batchnormalization):**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents62}  
    To facilitate learning, we typically normalize the initial values of our parameters by initializing them with zero mean and unit variance. As training progresses and we update parameters to different extents, we lose this normalization, which slows down training and amplifies changes as the network becomes deeper.  

    Batch normalization[^27] reestablishes these normalizations for every mini-batch and changes are back-propagated through the operation as well. By making normalization part of the model architecture, we are able to use higher learning rates and pay less attention to the initialization parameters. Batch normalization additionally acts as a regularizer, reducing (and sometimes even eliminating) the need for Dropout.  

    [Goodfellow on BN](https://www.youtube.com/watch?v=Xogn6veSyxA&feature=youtu.be&t=326s)  
    [Excellent Blog on BN](https://rohanvarma.me/Batch-Norm/)  
    <br>

3. **[Early Stopping](http://ruder.io/optimizing-gradient-descent/index.html#earlystopping):**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents63}  
    According to Geoff Hinton: "Early stopping (is) beautiful free lunch" ([NIPS 2015 Tutorial slides](https://media.nips.cc/Conferences/2015/tutorialslides/DL-Tutorial-NIPS2015.pdf), slide 63). You should thus always monitor error on a validation set during training and stop (with some patience) if your validation error does not improve enough.  
    <br>

4. **[Gradient Noise](http://ruder.io/optimizing-gradient-descent/index.html#gradientnoise):**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents64}  
    Neelakantan et al.[^28] add noise that follows a Gaussian distribution $$\mathcal{N}(0, \sigma^2_t)$$ to each gradient update:  
    <p>$$g_{t, i} = g_{t, i} + \mathcal{N}(0, \sigma^2_t)$$</p>  

    They anneal the variance according to the following schedule:  
    <p>$$\sigma^2_t = \dfrac{\eta}{(1 + t)^\gamma}$$</p>  

    They show that adding this noise makes networks more robust to poor initialization and helps training particularly deep and complex networks. They suspect that the added noise gives the model more chances to escape and find new local minima, which are more frequent for deeper models.  


***

## [Further Advances in DL Optimization](http://ruder.io/deep-learning-optimization-2017/index.html)  
{: #content7}


[^1]: H. Robinds and S. Monro, “A stochastic approximation method,” Annals of Mathematical Statistics, vol. 22, pp. 400–407, 1951.
[^2]: Darken, C., Chang, J., &amp; Moody, J. (1992). Learning rate schedules for faster stochastic gradient search. Neural Networks for Signal Processing II Proceedings of the 1992 IEEE Workshop, (September), 1–11. <a href="http://doi.org/10.1109/NNSP.1992.253713">http://doi.org/10.1109/NNSP.1992.253713</a>
[^3]: Dauphin, Y., Pascanu, R., Gulcehre, C., Cho, K., Ganguli, S., &amp; Bengio, Y. (2014). Identifying and attacking the saddle point problem in high-dimensional non-convex optimization. arXiv, 1–14. Retrieved from <a href="http://arxiv.org/abs/1406.2572">http://arxiv.org/abs/1406.2572</a>
[^4]: Sutton, R. S. (1986). Two problems with backpropagation and other steepest-descent learning procedures for networks. Proc. 8th Annual Conf. Cognitive Science Society.
[^5]: Qian, N. (1999). On the momentum term in gradient descent learning algorithms. Neural Networks : The Official Journal of the International Neural Network Society, 12(1), 145–151. <a href="http://doi.org/10.1016/S0893-6080(98)00116-6">http://doi.org/10.1016/S0893-6080(98)00116-6</a>
[^6]: Nesterov, Y. (1983). A method for unconstrained convex minimization problem with the rate of convergence o(1/k2). Doklady ANSSSR (translated as Soviet.Math.Docl.), vol. 269, pp. 543– 547.
[^7]: Bengio, Y., Boulanger-Lewandowski, N., &amp; Pascanu, R. (2012). Advances in Optimizing Recurrent Networks. Retrieved from <a href="http://arxiv.org/abs/1212.0901">http://arxiv.org/abs/1212.0901</a>
[^8]: Sutskever, I. (2013). Training Recurrent neural Networks. PhD Thesis.
[^9]: Duchi, J., Hazan, E., &amp; Singer, Y. (2011). Adaptive Subgradient Methods for Online Learning and Stochastic Optimization. Journal of Machine Learning Research, 12, 2121–2159. Retrieved from <a href="http://jmlr.org/papers/v12/duchi11a.html">http://jmlr.org/papers/v12/duchi11a.html</a>
[^10]: Dean, J., Corrado, G. S., Monga, R., Chen, K., Devin, M., Le, Q. V, … Ng, A. Y. (2012). Large Scale Distributed Deep Networks. NIPS 2012: Neural Information Processing Systems, 1–11. <a href="http://papers.nips.cc/paper/4687-large-scale-distributed-deep-networks.pdf">http://papers.nips.cc/paper/4687-large-scale-distributed-deep-networks.pdf</a>
[^11]: Pennington, J., Socher, R., &amp; Manning, C. D. (2014). Glove: Global Vectors for Word Representation. Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing, 1532–1543. <a href="http://doi.org/10.3115/v1/D14-1162">http://doi.org/10.3115/v1/D14-1162</a>
[^12]: Duchi et al. [3] give this matrix as an alternative to the <em>full</em> matrix containing the outer products of all previous gradients, as the computation of the matrix square root is infeasible even for a moderate number of parameters $$d$$.  
[^13]: Zeiler, M. D. (2012). ADADELTA: An Adaptive Learning Rate Method. Retrieved from <a href="http://arxiv.org/abs/1212.5701">http://arxiv.org/abs/1212.5701</a>
[^14]: Kingma, D. P., &amp; Ba, J. L. (2015). Adam: a Method for Stochastic Optimization. International Conference on Learning Representations, 1–13.
[^24]: LeCun, Y., Bottou, L., Orr, G. B., &amp; Muller, K. R. (1998). Efficient BackProp. Neural Networks: Tricks of the Trade, 1524, 9–50. <a href="http://doi.org/10.1007/3-540-49430-8_2">http://doi.org/10.1007/3-540-49430-8_2</a>
[^25]: Bengio, Y., Louradour, J., Collobert, R., &amp; Weston, J. (2009). Curriculum learning. Proceedings of the 26th Annual International Conference on Machine Learning, 41–48. <a href="http://doi.org/10.1145/1553374.1553380">http://doi.org/10.1145/1553374.1553380</a>
[^26]: Zaremba, W., &amp; Sutskever, I. (2014). Learning to Execute, 1–25. Retrieved from <a href="http://arxiv.org/abs/1410.4615">http://arxiv.org/abs/1410.4615</a>
[^27]: Ioffe, S., &amp; Szegedy, C. (2015). Batch Normalization : Accelerating Deep Network Training by Reducing Internal Covariate Shift. arXiv Preprint arXiv:1502.03167v3.
[^28]: Neelakantan, A., Vilnis, L., Le, Q. V., Sutskever, I., Kaiser, L., Kurach, K., &amp; Martens, J. (2015). Adding Gradient Noise Improves Learning for Very Deep Networks, 1–11. Retrieved from <a href="http://arxiv.org/abs/1511.06807">http://arxiv.org/abs/1511.06807</a>