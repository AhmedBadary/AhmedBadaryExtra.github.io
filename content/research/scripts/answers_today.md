---
layout: NotesPage
title: Answers to Prep Questions (Learning)
permalink: /work_files/research/answers_today
prevLink: /work_files/research.html
---


1. __List limitations of PCA:__{: style="color: red"}  
    1. PCA is highly sensitive to the (relative) scaling of the data; no consensus on best scaling. 
1. __Feature Importance__{: style="color: red"}  
    1. Use linear regression and select variables based on $$p$$ values
    1. Use Random Forest, Xgboost and plot variable importance chart
    1. Lasso
    1. Measure information gain for the available set of features and select top $$n$$ features accordingly.
    1. Use Forward Selection, Backward Selection, Stepwise Selection
    1. Remove the correlated variables prior to selecting important variables
    1. In linear models, feature importance can be calculated by the scale of the coefficients  
    1. In tree-based methods (such as random forest), important features are likely to appear closer to the root of the tree. We can get a feature's importance for random forest by computing the averaging depth at which it appears across all trees in the forest   
1. __Define *Relative Entropy* - Give it's formula:__{: style="color: red"}  
    The __Kullback–Leibler divergence__ (__Relative Entropy__) is a measure of how one probability distribution diverges from a second, expected probability distribution.    

    __Mathematically:__    
    <p>$${\displaystyle D_{\text{KL}}(P\parallel Q)=\operatorname{E}_{x \sim P} \left[\log \dfrac{P(x)}{Q(x)}\right]=\operatorname{E}_{x \sim P} \left[\log P(x) - \log Q(x)\right]}$$</p>  
    1. __Discrete__:    
    <p>$${\displaystyle D_{\text{KL}}(P\parallel Q)=\sum_{i}P(i)\log \left({\frac {P(i)}{Q(i)}}\right)}$$  </p>  
    1. __Continuous__:    
    <p>$${\displaystyle D_{\text{KL}}(P\parallel Q)=\int_{-\infty }^{\infty }p(x)\log \left({\frac {p(x)}{q(x)}}\right)\,dx,}$$ </p>  

    1. __Give an interpretation:__{: style="color: blue"}  
        1. __Discrete variables__:  
            It is the extra amount of information needed to send a message containing symbols drawn from probability distribution $$P$$, when we use a code that was designed to minimize the length of messages drawn from probability distribution $$Q$$.  
    1. __List the properties:__{: style="color: blue"}  
        1. Non-Negativity:  
                $${\displaystyle D_{\mathrm {KL} }(P\|Q) \geq 0}$$  
        1. $${\displaystyle D_{\mathrm {KL} }(P\|Q) = 0 \iff}$$ $$P$$ and $$Q$$ are:
            1. *__Discrete Variables__*:  
                    the same distribution 
            1. *__Continuous Variables__*:  
                    equal "almost everywhere"  
        1. Additivity of _Independent Distributions_:  
                $${\displaystyle D_{\text{KL}}(P\parallel Q)=D_{\text{KL}}(P_{1}\parallel Q_{1})+D_{\text{KL}}(P_{2}\parallel Q_{2}).}$$  
        1. $${\displaystyle D_{\mathrm {KL} }(P\|Q) \neq D_{\mathrm {KL} }(Q\|P)}$$  
            > This asymmetry means that there are important consequences to the choice of the ordering   
        1. Convexity in the pair of PMFs $$(p, q)$$ (i.e. $${\displaystyle (p_{1},q_{1})}$$ and  $${\displaystyle (p_{2},q_{2})}$$ are two pairs of PMFs):  
                $${\displaystyle D_{\text{KL}}(\lambda p_{1}+(1-\lambda )p_{2}\parallel \lambda q_{1}+(1-\lambda )q_{2})\leq \lambda D_{\text{KL}}(p_{1}\parallel q_{1})+(1-\lambda )D_{\text{KL}}(p_{2}\parallel q_{2}){\text{ for }}0\leq \lambda \leq 1.}$$  
    1. __Describe it as a distance:__{: style="color: blue"}  
        Because the KL divergence is non-negative and measures the difference between two distributions, it is often conceptualized as measuring some sort of distance between these distributions.  
        However, it is __not__ a true distance measure because it is __*not symmetric*__.  
        > KL-div is, however, a *__Quasi-Metric__*, since it satisfies all the properties of a distance-metric except symmetry  
    1. __List the applications of relative entropy:__{: style="color: blue"}  
        Characterizing:  
        {: #lst-p}
        1. Relative (Shannon) entropy in information systems
        1. Randomness in continuous time-series 
        1. Information gain when comparing statistical models of inference  
    1. __How does the direction of minimization affect the optimization:__{: style="color: blue"}  
        Suppose we have a distribution $$p(x)$$ and we wish to _approximate_ it with another distribution $$q(x)$$.  
        We have a choice of _minimizing_ either:  
        1. $${\displaystyle D_{\text{KL}}(p\|q)} \implies q^\ast = \operatorname {arg\,min}_q {\displaystyle D_{\text{KL}}(p\|q)}$$  
            Produces an approximation that usually places high probability anywhere that the true distribution places high probability.  
        2. $${\displaystyle D_{\text{KL}}(q\|p)} \implies q^\ast \operatorname {arg\,min}_q {\displaystyle D_{\text{KL}}(q\|p)}$$  
            Produces an approximation that rarely places high probability anywhere that the true distribution places low probability.  
            > which are different due to the _asymmetry_ of the KL-divergence  

        <button>Choice of KL-div Direction</button>{: .showText value="show"  
         onclick="showTextPopHide(event);"}
        ![img](/main_files/math/infothry/1.png){: width="100%" hidden=""}  

