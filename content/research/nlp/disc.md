---
layout: NotesPage
title: Discriminative Models in NLP <br \> Maxent Models and Discriminative Estimation
permalink: /work_files/research/nlp/disc
prevLink: /work_files/research/dl.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Generative vs Discriminative Models](#content1)
  {: .TOC1}
  * [Feature Extraction for Discriminative Models in NLP](#content2)
  {: .TOC2}
  * [Feature-Based Linear Classifiers](#content3)
  {: .TOC3}
  <!-- * [FOURTH](#content4)
  {: .TOC4} -->
</div>

***
***

## Generative vs Discriminative Models
{: #content1}

Given some data $$\{(d,c)\}$$ of paired observations $$d$$ and hidden classes $$c$$:  

1. **Generative (Joint) Models:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    :   __Generative Models__ are __Joint Models__.  
    :   __Joint Models__ place probabilities $$\left(P(c,d)\right)$$ over both the observed data and the "target" (hidden) variables that can only be computed from those observed.  
    :   Generative models are typically probabilistic, specifying a joint probability distribution ($$P(d,c)$$) over observation and target (label) values,  
    and tries to __Maximize__ this __joint Likelihood__.  
        > Choosing weights turn out to be trivial: chosen as the __relative frequencies__.  
    :   __Examples:__  
        * n-gram Models
        * Naive Bayes Classifiers  
        * Hidden Markov Models (HMMs)
        * Probabilistic Context-Free Grammars (PCFGs)
        * IBM Machine Translation Alignment Models

2. **Discriminative (Conditional) Models:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    :   __Discriminative Models__ are __Conditional Models__.  
    :   __Conditional Models__ provide a model only for the "target" (hidden) variabless.  
        They take the data as given, and put a probability $$\left(P(c \| d)\right)$$ over the "target" (hidden) structures given the data.  
    :   Conditional Models seek to __Maximize__ the __Conditional Likelihood__.  
        > This (maximization) task is usually harder to do.  
    :   __Examples:__  
        * Logistic Regression
        * Conditional LogLinear/Maximum Entropy Models  
        * Condtional Random Fields  
        * SVMs  
        * Perceptrons  

3. **Generative VS Discriminative Models:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    :   Basically, _Discriminative Models_ infer outputs based on inputs,  
        while _Generative Models_ generate, both, inputs and outputs (typically given some hidden parameters).  
    :   However, notice that the two models are usually viewed as complementary procedures.  
        One does __not__ necessarily outperform the other, in either classification or regression tasks.   

***

## Feature Extraction for Discriminative Models in NLP
{: #content2}

1. **Features (Intuitively):**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    :   __Features__ ($$f$$) are elementary pieces of evidence that link aspects of what we observe ($$d$$) with a category ($$c$$) that we want to predict.  

2. **Features (Mathematically):**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}  
    :   A __Feature__ $$f$$ is a function with a bounded real value.  
    :   $$f : \: C \times D \rightarrow \mathbf{R}$$


3. **Models and Features:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}  
    :   Models will assign a __weight__ to each Feature:  
        * A __Positive Weight__ votes that this configuration is likely _Correct_.  
        * A __Negative Weight__ votes that this configuration is likely _Incorrect_. 

4. **Feature Expectations:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}  
    :   * __Empirical  Expectation (count)__:  
    :   $$E_{\text{emp}}(f_i) = \sum_{(c,d)\in\text{observed}(C,D)} f_i(c,d)$$    
    :   * __Model Expectation__:  
    :   $$E(f_i) = \sum_{(c,d)\in(C,D)} P(c,d)f_i(c,d)$$
    :   > The two Expectations represent the __Actual__ and the __Predicted__ __Counts__ of a feature __firing__, respectively.  

5. **Features in NLP:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}  
    In NLP, features have a particular form.  
    They consist of:  
    {: #lst-p}
    * __Indicator Function__: a boolean matching function of properties of the input  
    * __A Particular Class__: specifies some class $$c_j$$  
        <p>$$f_i(c,d) \cong [\Phi(d) \wedge c=c_j] = \{0 \vee 1\}$$</p>  
        where $$\Phi(d)$$ is a given predicate on the data $$d$$, and $$c_j$$ is a particular class.  
    
    > Basically, each feature picks out a data subset and suggests a label for it.  

***

## Feature-Based Linear Classifiers
{: #content3}

1. **Linear Classifiers (Classification):**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}  
    :   * We have a __Linear Function__ from the feature sets $$\{f_i\}$$ to the classes $$\{c\}$$  
        * __Assign Weights__ $$\lambda_i$$ to each feature $$f_i$$  
        * __Consider each class__ for an observed datum $$d$$  
        * __Features Vote__ with their _weights_    :
        :   $$\text{vote}(c) = \sum \lambda_i f_i(c,d)$$  
        * __Classification__:  
            choose the class $$c$$ which __Maximizes__ the __vote__ $$\sum \lambda_i f_i(c,d)$$  


2. **Exponential Models:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}  
    :   __Exponential Models__ make a probabilistic model from the linear combination $$\sum\lambda_if_i(c,d)$$
    :   * __Making the Value Positive__:    
    :   $$\sum\lambda_if_i(c,d) \rightarrow e^{\sum\lambda_if_i(c,d)}$$   
    :   * __Normalizing the Value (Making a Probability)__:  
    :  $$e^{\sum\lambda_if_i(c,d)} \rightarrow \dfrac{e^{\sum\lambda_if_i(c,d)}}{\sum_{c \in C} e^{\sum\lambda_if_i(c,d)}}$$ 
    :   $$\implies$$
    :   $$P(c \| d, \vec{\lambda}) = \dfrac{e^{\sum\lambda_if_i(c,d)}}{\sum_{c \in C} e^{\sum\lambda_if_i(c,d)}}$$
    :   The function $$P(c \| d,\vec{\lambda})$$ is referred to as the __Soft-Max__ function.  
    :   Here, the __Weights__ are the __Paramters__ of the probability model, combined via a __Soft-Max__ function.
    :   __Learning:__  
        * Given this model form, we want to choose paramters $$\{\lambda_i\}$$ that __Maximize the Conditional Likelihood__ of the data according to this model (i.e. the soft-max func.).    
    :   Exponential Models, construct _not onlt_ __classifications__ but, also, __Probability Distributions__ over the classifications.
    :   __Examples:__  
        * Log-Linear Model
        * Max Entropy (MaxEnt) Model
        * Logistic Regression  
        * Gibbs Model 

3. **Exponential Models (Training) | Maximizing the Likelihood:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}  
    __The Likelihood Value__:   
    {: #lst-p} 
    * The __(log) conditional likelihood__ of a MaxEnt model is a function of the i.i.d. data $$(C,D)$$ and the parameters ($$\lambda$$):  
        <p>$$\log P(C \| D,\lambda) = \log \prod_{(c,d) \in (C,D)} P(c \| d,\lambda) = \sum_{(c,d) \in (C,D)} \log P(c \| d,\lambda)$$</p>  
    * If there aren't many values of $$c$$, it's easy to calculate:    
        <p>$$\log P(c \| d,\lambda) = \sum_{(c,d) \in (C,D)} \log \dfrac{e^{\sum_i \lambda_if_i(c,d)}}{\sum_c e^{\sum_i \lambda_if_i(c,d)}}$$</p>    
    * We can separate this into two components:    
        <p>$$\log P(c \| d,\lambda) = \sum_{(c,d) \in (C,D)} \log e^{\sum_i \lambda_if_i(c,d)} - \sum_{(c,d) \in (C,D)} \log \sum_c' e^{\sum_i \lambda_if_i(c',d)}$$</p>    
        <p>$$\implies$$</p>    
        <p>$$\log P(C \| D, \lambda) = N(\lambda) - M(\lambda)$$</p>    
    * The Derivative of the Numerator is easy to calculate:    
        <p>$$\dfrac{\partial N(\lambda)}{\partial \lambda_i} = \dfrac{\partial \sum_{(c,d) \in (C,D)} \log e^{\sum_i \lambda_if_i(c,d)}}{\partial \lambda_i}  
    \\= \dfrac{\partial \sum_{(c,d) \in (C,D)} \sum_i \lambda_if_i(c,d)}{\partial \lambda_i} 
    \\\\= \sum_{(c,d) \in (C,D)} \dfrac{\partial \sum_i \lambda_if_i(c,d)}{\partial \lambda_i} 
    \\\\= \sum_{(c,d) \in (C,D)} f_i(c,d)$$</p>    

    * The derivative of the Numerator is __the Empirical Expectation__, $$E_{\text{emp}}(f_i)$$  
    * The Derivative of the Denominator:    
        <p>$$\dfrac{\partial M(\lambda)}{\partial \lambda_i}  = \dfrac{\partial \sum_{(c,d) \in (C,D)} \log \sum_c' e^{\sum_i \lambda_if_i(c',d)}}{\partial \lambda_i} \\\\= \sum_{(c,d) \in (C,D)} \sum_c' P(c' \| d, \lambda)f_i(c', d)$$</p>  

    * The derivative of the Denominator is equal to __the Predicted Expectation (count)__, $$E(f_i, \lambda)$$  
    * Thus, the derivative of the log likelihood is:  
        <p>$$\dfrac{\partial \log P(C \| D, \vec{\lambda})}{\partial \lambda_i} = \text{Actual Count}(f_i, C) - \text{Predicted Count}(f_i, \vec{\lambda})$$</p>    
    * Thus, the optimum parameters are those for which each feature's _predicted expectation_ equals its _empirical expectation_.    
    

    The __Optimum Distribution__ is always:  
    {: #lst-p}
    * Unique (parameters need not be unique)  
    * Exists (if feature counts are from actual data)  


    These models are called __Maximum Entropy (Maxent)__ Models because we find the model having the maximum entropy, and satisfying the constraints:    
    <p>$$E_p(f_j) = E_\hat{p}(f_j), \:\:\: \forall j$$</p>   
    
    
    Finally, to find the optimal parameters $$\lambda_1, \dots, \lambda_d$$ one needs to optimize (maximize) the log likelihood, or equivalently, minimize the -ve likelihood.    
    One can do that in variety of ways using optimization methods.  
    
    Common __Optimization Methods__:    
    {: #lst-p}
    * (Stochastic) Gradient Descent
    * Iterative Proportional Fitting Methods:  
        * Generalized Iterative Scaling (GIS)
        * Improved Iterative Scaling (IIS)
    * Conjugate Gradient (CG) (+ Preconditioning)
    * Quasi-Newton Methods -  Limited-Memory Variable Metric (LMVM):  
        * L-BFGS
            This one is the most commonly used.  