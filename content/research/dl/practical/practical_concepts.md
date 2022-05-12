---
layout: NotesPage
title: Practical Concepts in Machine Learning
permalink: /work_files/research/dl/practical/practical_concepts
prevLink: /work_files/research/dl/practical.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [FIRST](#content1)
  {: .TOC1}
<!--   * [SECOND](#content2)
  {: .TOC2}
  * [THIRD](#content3)
  {: .TOC3} -->
</div>

***
***


* [A Cookbook for Machine Learning: Vol 1 (Blog!)](https://www.inference.vc/design-patterns/)  
    * [Reddit Blog](https://www.reddit.com/r/MachineLearning/comments/7dd45h/d_a_cookbook_for_machine_learning_a_list_of_ml/)  
* [Deep Learning Cookbook (book)](http://noracook.io/Books/MachineLearning/deeplearningcookbook.pdf)  


<!-- ## FIRST
{: #content1} --> 

1. **Data Snooping:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  

    __The Principle:__  
    If a data set has __*affected*__ any step in the __learning process__, its __ability to *assess the outcome*__ has been compromised.  

    __Analysis:__  
    {: #lst-p}
    * Making decision by __examining the dataset__ makes *__you__* a part of the learning algorithm.  
        However, you didn't consider your contribution to the learning algorithm when making e.g. VC-Analysis for Generalization.  
    * Thus, you are __vulnerable__ to designing the model (or choices of learning) according to the *__idiosyncrasies__* of the __dataset__.  
    * The real problem is that you are not _"charging" for the decision you made by examining the dataset_.    

    __What's allowed?__  
    {: #lst-p}
    * You are allowed (even encouraged) to look at all other information related to the __target function__ and __input space__.  
        e.g. number/range/dimension/scale/etc. of the inputs, correlations, properties (monotonicity), etc.  
    * EXCEPT, for the __*specific* realization of the training dataset__.  


    __Manifestations of Data Snooping with Examples (one/manifestation):__{: style="color: red"}  
    {: #lst-p}
    * __Changing the Parameters of the model (Tricky)__:  
        * __Complexity__:  
            Decreasing the order of the fitting polynomial by observing geometric properties of the __training set__.  
    * __Using statistics of the Entire Dataset (Tricky)__:  
        * __Normalization__:  
            Normalizing the data with the mean and variance of the __entire dataset (training+testing)__.  
            * E.g. In Financial Forecasting; the average affects the outcome by exposing the trend.  
    * __Reuse of a Dataset__:  
        If you keep Trying one model after the other *on the* __same data set__, you will eventually 'succeed'.  
        _"If you torture the data long enough, it will confess"_.  
        This bad because the final model you selected, is the __*union* of all previous models__: since some of those models were *__rejected__* by __you__ (a *__learning algorithm__*).  
        * __Fixed (deterministic) training set for Model Selection__:  
            Selecting a model by trying many models on the __same *fixed (deterministic)* Training dataset__.  
    * __Bias via Snooping__:  
        By looking at the data in the future when you are not allowed to have the data (it wouldn't have been possible); you are creating __sampling bias__ caused by _"snooping"_.  
        * E.g. Testing a __Trading__ algorithm using the *__currently__* __traded companies__ (in S&P500).  
            You shouldn't have been able to know which companies are being *__currently__* traded (future).  



    __Remedies/Solutions to Data Snooping:__{: style="color: red"}  
    {: #lst-p}
    1. __Avoid__ Data Snooping:  
        A strict discipline (very hard).  
    2. __Account for__ Data Snooping:  
        By quantifying "How much __data contamination__".  

    <br>


2. **Mismatched Data:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  

3. **Mismatched Classes:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  

4. **Sampling Bias:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    __Sampling Bias__ occurs when: $$\exists$$ Region with zero-probability $$P=0$$ in training, but with positive-probability $$P>0$$ in testing.  

    __The Principle:__  
    If the data is sampled in a biased way, learning will produce a similarly biased outcome.  

    __Example: 1948 Presidential Elections__  
    {: #lst-p}
    * Newspaper conducted a *__Telephone__* poll between: __Jackson__ and __Truman__  
    * __Jackson__ won the poll __decisively__.  
    * The result was NOT __unlucky__:  
        No matter how many times the poll was re-conducted, and no matter how many times the sample sized is increased; the outcome will be fixed.  
    * The reason is the *__Telephone__*:  
        (1) Telephones were __expensive__ and only __rich people__ had Telephones.  
        (2) Rich people favored __Jackson__.  
        Thus, the result was __well reflective__ of the (mini) population being sampled.  

    __How to sample:__{: style="color: red"}  
    Sample in a way that <span>matches the __distributions__ of __train__ and __test__</span>{: style="color: purple"} samples.  

    The solution __Fails__ (doesn't work) if:  
    $$\exists$$ Region with zero-probability $$P=0$$ in training, but with positive-probability $$P>0$$ in testing.  
    > This is when sampling bias exists.  


    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * Medical sources sometimes refer to sampling bias as __ascertainment bias__.  
    * Sampling bias could be viewed as a subtype of __selection bias__.  
    <br>


5. **Model Uncertainty:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  

    __Interpreting Softmax Output Probabilities:__{: style="color: red"}  
    Softmax outputs only measure [__Aleatoric Uncertainty__](https://en.wikipedia.org/wiki/Uncertainty_quantification#Aleatoric_and_epistemic_uncertainty).  
    In the same way that in regression, a NN with two outputs, one representing mean and one variance, that parameterise a Gaussian, can capture aleatoric uncertainty, even though the model is deterministic.  
    Bayesian NNs (dropout included), aim to capture epistemic (aka model) uncertainty.  

    __Dropout for Measuring Model (epistemic) Uncertainty:__{: style="color: red"}  
    Dropout can give us principled uncertainty estimates.  
    Principled in the sense that the uncertainty estimates basically approximate those of our [Gaussian process](/work_files/research/dl/archits/nns#bodyContents13).  

    __Theoretical Motivation:__ dropout neural networks are identical to <span>variational inference in Gaussian processes</span>{: style="color: purple"}.  
    __Interpretations of Dropout:__  
    {: #lst-p}
    * Dropout is just a diagonal noise matrix with the diagonal elements set to either 0 or 1.  
    * [What My Deep Model Doesn't Know (Blog! - Yarin Gal)](http://mlg.eng.cam.ac.uk/yarin/blog_3d801aa532c1ce.html)  
    <br>

6. **Probability Calibration:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}  
    Modern NN are __miscalibrated__: not well-calibrated. They tend to be very confident. We cannot interpret the softmax probabilities as reflecting the true probability distribution or as a measure of confidence.  

    __Miscalibration:__ is the discrepancy between model confidence and model accuracy.  
    You assume that if a model gives $$80\%$$ confidence for 100 images, then $$80$$ of them will be accurate and the other $$20$$ will be inaccurate.  
    <button>Miscalibration in Modern Neural Networks</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/boMaW8Wx2tXfUYTJpd-rhcVGWnrtpC4_2AGbXPxtocc.original.fullsize.png){: width="100%" hidden=""}  

    __Model Confidence:__ probability of correctness.  
    __Calibrated Confidence (softmax scores) $$\hat{p}$$:__ $$\hat{p}$$ represents a true probability.  

    * [On Calibration of Modern Neural Networks](https://arxiv.org/pdf/1706.04599.pdf)    
        Paper that defines the problem and gives multiple effective solution for calibrating Neural Networks. 
    * [Calibration of Convolutional Neural Networks (Thesis!)](file:///Users/ahmadbadary/Downloads/Kängsepp_ComputerScience_2018.pdf)  
    * For calibrating output probabilities in Deep Nets; Temperature scaling outperforms Platt scaling. [paper](https://arxiv.org/pdf/1706.04599.pdf)  
    * [Plot and Explanation](https://scikit-learn.org/stable/modules/calibration.html)  
    * [Blog on How to do it](http://alondaks.com/2017/12/31/the-importance-of-calibrating-your-deep-model/)  
    <br>

7. **Debugging Strategies for Deep ML Models:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}  
    <button>Strategies</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    1. __Visualize the model in action:__  
        Directly observing qualitative results of a model (e.g. located objects, generated speech) can help avoid __evaluation bugs__ or __mis-leading evaluation results__. It can also help guide the expected quantitative performance of the model.  
    2. __Visualize the worst mistakes:__  
        By viewing the training set examples that are the hardest to model correctly by using a confidence measure (e.g. softmax probabilities), one can often discover problems with the way the data have been __preprocessed__ or __labeled__.  
    3. __Reason about Software using Training and Test *Error*:__  
        It is hard to determine whether the underlying software is correctly implemented.  
        We can use the training/test errors to help guide us:  
        * If training error is low but test error is high, then:  
            * it is likely that that the training procedure works correctly,and the model is overfitting for fundamental algorithmic reasons.  
            * or that the test error is measured incorrectly because of a problem with saving the model after training then reloading it for test set evaluation, or because the test data was prepared differently from the training data.  
        * If both training and test errors are high, then:  
            it is difficult to determine whether there is a software defect or whether the model is underfitting due to fundamental algorithmic reasons.  
            This scenario requires further tests, described next.  
    3. __Fit a *Tiny Dataset:*__  
        If you have high error on the training set, determine whether it is due to genuine underfitting or due to a software defect.  
        Usually even small models can be guaranteed to be able fit a suﬃciently small dataset. For example, a classification dataset with only one example can be fit just by setting the biase sof the output layer correctly.  
        This test can be extended to a small dataset with few examples.  
    4. __Monitor histograms of *Activations* and *Gradients:*__  
        It is often useful to visualize statistics of neural network activations and gradients, collected over a large amount of training iterations (maybe one epoch).  
        The __preactivation value__ of __hidden units__ can tell us if the units <span>__saturate__</span>{: style="color: purple"}, or how often they do.  
        For example, for rectifiers,how often are they off? Are there units that are always off?  
        For tanh units,the average of the absolute value of the preactivations tells us how saturated the unit is.  
        In a deep network where the propagated gradients quickly grow or quickly vanish, optimization may be hampered.  
        Finally, it is useful to compare the magnitude of parameter gradients to the magnitude of the parameters themselves. As suggested by Bottou (2015), we would like the magnitude of parameter updates over a minibatch to represent something like 1 percent of the magnitude of the parameter, not 50 percent or 0.001 percent (which would make the parametersmove too slowly). It may be that some groups of parameters are moving at a good pace while others are stalled. When the data is sparse (like in natural language) some parameters may be very rarely updated, and this should be kept in mind when monitoring their evolution.  
    5. Finally, many deep learning algorithms provide some sort of guarantee about the results produced at each step.  
        For example, in part III, we will see some approximate inference algorithms that work by using algebraic solutions to optimization problems.  
        Typically these can be debugged by testing each of their guarantees.Some guarantees that some optimization algorithms offer include that the objective function will never increase after one step of the algorithm, that the gradient with respect to some subset of variables will be zero after each step of the algorithm,and that the gradient with respect to all variables will be zero at convergence.Usually due to rounding error, these conditions will not hold exactly in a digital computer, so the debugging test should include some tolerance parameter. 
    {: hidden=""}
    <br>

8. **The Machine Learning Algorithm Recipe:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18}  
    Nearly all deep learning algorithms can be described as particular instances of a fairly simple recipe in both Supervised and Unsupervised settings:  
    * A combination of:  
        * A specification of a dataset
        * A cost function
        * An optimization procedure
        * A model
    * __Ex: Linear Regression__  
        <button>Example</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        * A specification of a dataset:  
            The Dataset consists of $$X$$ and $$y$$.  
        * A cost function:  
            $$J(\boldsymbol{w}, b)=-\mathbb{E}_{\mathbf{x}, \mathbf{y} \sim \hat{p}_{\text {data }}} \log p_{\text {model }}(y | \boldsymbol{x})$$  
        * An optimization procedure:  
            in most cases, the optimization algorithm is defined by solving for where the gradient of the cost is zero using the normal equation.  
        * A model:  
            The Model Specification is:  
            $$p_{\text {model}}(y \vert \boldsymbol{x})=\mathcal{N}\left(y ; \boldsymbol{x}^{\top} \boldsymbol{w}+b, 1\right)$$  
        {: hidden=""}
    * __Ex: PCA__  
        <button>Example</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        * A specification of a dataset:  
            $$X$$  
        * A cost function:  
            $$J(\boldsymbol{w})=\mathbb{E}_{\mathbf{x} \sim \hat{p}_{\text {data }}}\|\boldsymbol{x}-r(\boldsymbol{x} ; \boldsymbol{w})\|_ {2}^{2}$$  
        * An optimization procedure:  
            Constrained Convex optimization or Gradient Descent.  
        * A model:  
            Defined to have $$\boldsymbol{w}$$ with __norm__ $$1$$ and __reconstruction function__ $$r(\boldsymbol{x})=\boldsymbol{w}^{\top} \boldsymbol{x} \boldsymbol{w}$$.  
        {: hidden=""}


    * __Specification of a Dataset__:  
        Could be __labeled (supervised)__ or __unlabeled (unsupervised)__.  
    * __Cost Function__:  
        The cost function typically includes at least one term that causes the learning process to perform __statistical estimation__. The most common cost function is the negative log-likelihood, so that minimizing the cost function causes maximum likelihood estimation.  
    * __Optimization Procedure__:  
        Could be __closed-form__ or __iterative__ or __special-case__.  
        If the cost function does not allow for __closed-form__ solution (e.g. if the model is specified as __non-linear__), then we usually need __iterative__ optimization algorithms e.g. __gradient descent__.  
        If the cost can't be computed for __computational problems__ then we can approximate it with an iterative numerical optimization as long as we have some way to <span>approximating its __gradients__</span>{: style="color: purple"}.   
    * __Model__:  
        Could be __linear__ or __non-linear__.  

    If a machine learning algorithm seems especially unique or hand designed, it can usually be understood as using a __special-case optimizer__.  
    Some models, such as __decision trees__ and __k-means__, require *__special-case optimizers__* because their __cost functions__ have *__flat regions__* that make them inappropriate for minimization by gradient-based optimizers.  

    Recognizing that most machine learning algorithms can be described using this recipe helps to see the different algorithms as part of a taxonomy of methods for doing related tasks that work for similar reasons, rather than as a long list of algorithms that each have separate justifications.  

    <br>


***

## SECOND
{: #content2}

<!-- 
1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}
2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}
3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}
4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}
 -->
