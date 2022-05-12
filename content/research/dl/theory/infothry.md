---
layout: NotesPage
title: Information Theory
permalink: /work_files/research/dl/theory/infothry
prevLink: /work_files/research/dl/theory.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Information Theory](#content1)
  {: .TOC1}
</div>

***
***

[A Short Introduction to Entropy, Cross-Entropy and KL-Divergence](https://www.youtube.com/watch?v=ErfnhcEV1O8)  
[Deep Learning Information Theory (Cross-Entropy and MLE)](https://jhui.github.io/2017/01/05/Deep-learning-Information-theory/)  
[Further Info (Lecture)](https://www.youtube.com/watch?v=XL07WEc2TRI)  
[Visual Information Theory (Chris Olahs' Blog)](https://colah.github.io/posts/2015-09-Visual-Information/) 
[Deep Learning and Information Theory  (Blog)](https://deep-and-shallow.com/2020/01/09/deep-learning-and-information-theory/)  
[Information Theory | Statistics for Deep Learning (Blog)](https://medium.com/machine-learning-bootcamp/demystifying-information-theory-e21f3af09455)  


![img](https://cdn.mathpix.com/snip/images/TNzZfbJuHJsESt3Ds0LpsEBVdRsi56VBP8RK7r54Vc0.original.fullsize.png){: width="80%"}  


## Information Theory
{: #content1}

1. **Information Theory:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    __Information theory__ is a branch of applied mathematics that revolves around quantifying how much information is present in a signal.  
    In the context of machine learning, we can also apply information theory to continuous variables where some of these message length interpretations do not apply, instead, we mostly use a few key ideas from information theory to characterize probability distributions or to quantify similarity between probability distributions.  
    <br>

2. **Motivation and Intuition:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    The basic intuition behind information theory is that learning that an unlikely event has occurred is more informative than learning that a likely event has occurred. A message saying “the sun rose this morning” is so uninformative as to be unnecessary to send, but a message saying “there was a solar eclipse this morning” is very informative.  
    Thus, information theory quantifies information in a way that formalizes this intuition:  
    {: #lst-p}
    * Likely events should have low information content - in the extreme case, guaranteed events have no information at all  
    * Less likely events should have higher information content
    * Independent events should have additive information. For example, finding out that a tossed coin has come up as heads twice should convey twice as much information as finding out that a tossed coin has come up as heads once.  
    <br>

33. **Measuring Information:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents133}  
    In Shannons Theory, to __transmit $$1$$ bit of information__ means to __divide the recipients *Uncertainty* by a factor of $$2$$__.  

    Thus, the __amount of information__ transmitted is the __logarithm__ (base $$2$$) of the __uncertainty reduction factor__.  

    The __uncertainty reduction factor__ is just the __inverse of the probability__ of the event being communicated.  

    Thus, the __amount of information__ in an event $$\mathbf{x} = x$$, called the *__Self-Information__*  is:  
    <p>$$I(x) = \log (1/p(x)) = -\log(p(x))$$</p>  

    __Shannons Entropy:__  
    It is the __expected amount of information__ of an uncertain/stochastic source. It acts as a measure of the amount of *__uncertainty__* of the events.  
    Equivalently, the amount of information that you get from one sample drawn from a given probability distribution $$p$$.  
    <br>

3. **Self-Information:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    The __Self-Information__ or __surprisal__ is a synonym for the surprise when a random variable is sampled.  
    The __Self-Information__ of an event $$\mathrm{x} = x$$:  
    <p>$$I(x) = - \log P(x)$$</p>  
    Self-information deals only with a single outcome.  

    <button>Graph $$\log_2{1/x}$$</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/NQ7sPTwgM1cNWpDRoclXezOYWAE8lttajOy5ofO3UQ4.original.fullsize.png){: width="28%" hidden=""}  
    <br>

4. **Shannon Entropy:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    To quantify the amount of uncertainty in an entire probability distribution, we use __Shannon Entropy__.  
    __Shannon Entropy__ is defined as the average amount of information produced by a stochastic source of data.  
    <p>$$H(x) = {\displaystyle \operatorname {E}_{x \sim P} [I(x)]} = - {\displaystyle \operatorname {E}_{x \sim P} [\log P(X)] = -\sum_{i=1}^{n} p\left(x_{i}\right) \log p\left(x_{i}\right)}$$</p>  
    __Differential Entropy__ is Shannons entropy of a __continuous__ random variable $$x$$.  
    ![img](/main_files/math/prob/11.png){: width="60%"}  
    <br>

5. **Distributions and Entropy:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  
    Distributions that are nearly deterministic (where the outcome is nearly certain) have low entropy; distributions that are closer to uniform have high entropy.
    <br>

6. **Relative Entropy \| KL-Divergence:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}  
    The __Kullback–Leibler divergence__ (__Relative Entropy__) is a measure of how one probability distribution diverges from a second, expected probability distribution.  
    __Mathematically:__  
    <p>$${\displaystyle D_{\text{KL}}(P\parallel Q)=\operatorname{E}_{x \sim P} \left[\log \dfrac{P(x)}{Q(x)}\right]=\operatorname{E}_{x \sim P} \left[\log P(x) - \log Q(x)\right]}$$</p>  
    * __Discrete__:  
    <p>$${\displaystyle D_{\text{KL}}(P\parallel Q)=\sum_{i}P(i)\log \left({\frac {P(i)}{Q(i)}}\right)}$$  </p>  
    * __Continuous__:  
    <p>$${\displaystyle D_{\text{KL}}(P\parallel Q)=\int_{-\infty }^{\infty }p(x)\log \left({\frac {p(x)}{q(x)}}\right)\,dx,}$$ </p>  

    __Interpretation:__  
    {: #lst-p}
    * __Discrete variables__:  
        it is the extra amount of information needed to send a message containing symbols drawn from probability distribution $$P$$, when we use a code that was designed to minimize the length of messages drawn from probability distribution $$Q$$.  
    * __Continuous variables__:  

    __Properties:__  
    {: #lst-p}
    * Non-Negativity:  
            $${\displaystyle D_{\mathrm {KL} }(P\|Q) \geq 0}$$  
    * $${\displaystyle D_{\mathrm {KL} }(P\|Q) = 0 \iff}$$ $$P$$ and $$Q$$ are:
        * *__Discrete Variables__*:  
                the same distribution 
        * *__Continuous Variables__*:  
                equal "almost everywhere"  
    * Additivity of _Independent Distributions_:  
            $${\displaystyle D_{\text{KL}}(P\parallel Q)=D_{\text{KL}}(P_{1}\parallel Q_{1})+D_{\text{KL}}(P_{2}\parallel Q_{2}).}$$  
    * $${\displaystyle D_{\mathrm {KL} }(P\|Q) \neq D_{\mathrm {KL} }(Q\|P)}$$  
        > This asymmetry means that there are important consequences to the choice of the ordering  
    * Convexity in the pair of PMFs $$(p, q)$$ (i.e. $${\displaystyle (p_{1},q_{1})}$$ and  $${\displaystyle (p_{2},q_{2})}$$ are two pairs of PMFs):  
            $${\displaystyle D_{\text{KL}}(\lambda p_{1}+(1-\lambda )p_{2}\parallel \lambda q_{1}+(1-\lambda )q_{2})\leq \lambda D_{\text{KL}}(p_{1}\parallel q_{1})+(1-\lambda )D_{\text{KL}}(p_{2}\parallel q_{2}){\text{ for }}0\leq \lambda \leq 1.}$$  

    __KL-Div as a Distance:__  
    Because the KL divergence is non-negative and measures the difference between two distributions, it is often conceptualized as measuring some sort of distance between these distributions.  
    However, it is __not__ a true distance measure because it is __*not symmetric*__.  
    > KL-div is, however, a *__Quasi-Metric__*, since it satisfies all the properties of a distance-metric except symmetry  

    __Applications__  
    Characterizing:  
    {: #lst-p}
    * Relative (Shannon) entropy in information systems
    * Randomness in continuous time-series 
    * It is a measure of __Information Gain__; used when comparing statistical models of inference  

    __Example Application and Direction of Minimization__  
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
    <br>

7. **Cross Entropy:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}  
    The __Cross Entropy__ between two probability distributions $${\displaystyle p}$$ and $${\displaystyle q}$$ over the same underlying set of events measures the average number of bits needed to identify an event drawn from the set, if a coding scheme is used that is optimized for an "unnatural" probability distribution $${\displaystyle q}$$, rather than the "true" distribution $${\displaystyle p}$$.  
    <p>$$H(p,q) = \operatorname{E}_{p}[-\log q]= H(p) + D_{\mathrm{KL}}(p\|q) =-\sum_{x }p(x)\,\log q(x)$$</p>  
  
    It is similar to __KL-Div__ but with an additional quantity - the entropy of $$p$$.  
  
    Minimizing the cross-entropy with respect to $$Q$$ is equivalent to minimizing the KL divergence, because $$Q$$ does not participate in the omitted term.  
  
    We treat $$0 \log (0)$$ as $$\lim_{x \to 0} x \log (x) = 0$$.  
    <br>

8. **Mutual Information:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18}  
    The __Mutual Information (MI)__ of two random variables is a measure of the mutual dependence between the two variables.  
    More specifically, it quantifies the "amount of information" (in bits) obtained about one random variable through observing the other random variable.  
  
    It can be seen as a way of measuring the reduction in uncertainty (information content) of measuring a part of the system after observing the outcome of another parts of the system; given two R.Vs, knowing the value of one of the R.Vs in the system gives a corresponding reduction in (the uncertainty (information content) of) measuring the other one.  

    __As KL-Divergence:__  
    Let $$(X, Y)$$ be a pair of random variables with values over the space $$\mathcal{X} \times \mathcal{Y}$$ . If their joint distribution is $$P_{(X, Y)}$$ and the marginal distributions are $$P_{X}$$ and $$P_{Y},$$ the mutual information is defined as:  
    <p>$$I(X ; Y)=D_{\mathrm{KL}}\left(P_{(X, Y)} \| P_{X} \otimes P_{Y}\right)$$</p>  

    __In terms of PMFs for discrete distributions:__  
    The mutual information of two jointly discrete random variables $$X$$ and $$Y$$ is calculated as a double sum:  
    <p>$$\mathrm{I}(X ; Y)=\sum_{y \in \mathcal{Y}} \sum_{x \in \mathcal{X}} p_{(X, Y)}(x, y) \log \left(\frac{p_{(X, Y)}(x, y)}{p_{X}(x) p_{Y}(y)}\right)$$</p>  
    where $${\displaystyle p_{(X,Y)}}$$ is the joint probability mass function of $${\displaystyle X}$$ X and $${\displaystyle Y}$$, and $${\displaystyle p_{X}}$$ and $${\displaystyle p_{Y}}$$ are the marginal probability mass functions of $${\displaystyle X}$$ and $${\displaystyle Y}$$ respectively.  

    __In terms of PDFs for continuous distributions:__  
    In the case of jointly continuous random variables, the double sum is replaced by a double integral:  
    <p>$$\mathrm{I}(X ; Y)=\int_{\mathcal{Y}} \int_{\mathcal{X}} p_{(X, Y)}(x, y) \log \left(\frac{p_{(X, Y)}(x, y)}{p_{X}(x) p_{Y}(y)}\right) d x d y$$</p>  
    where $$p_{(X, Y)}$$ is now the joint probability density function of $$X$$ and $$Y$$ and $$p_{X}$$ and $$p_{Y}$$ are the marginal probability density functions of $$X$$ and $$Y$$ respectively.  


    __Intuitive Definitions:__{: style="color: red"}  
    {: #lst-p}
    * Measures the information that $$X$$ and $$Y$$ share:  
        It measures how much knowing one of these variables reduces uncertainty about the other.  
        * __$$X, Y$$ Independent__  $$\implies I(X; Y) = 0$$: their MI is zero  
        * __$$X$$ deterministic function of $$Y$$ and vice versa__ $$\implies I(X; Y) = H(X) = H(Y)$$ their MI is equal to entropy of each variable  
    * It's a Measure of the inherent dependence expressed in the joint distribution of  $$X$$ and  $$Y$$ relative to the joint distribution of $$X$$ and $$Y$$ under the assumption of independence.  
        i.e. The price for encoding $${\displaystyle (X,Y)}$$ as a pair of independent random variables, when in reality they are not.  

    __Properties:__{: style="color: red"}  
    {: #lst-p}
    * The KL-divergence shows that $$I(X; Y)$$ is equal to zero precisely when <span>the joint distribution conicides with the product of the marginals i.e. when </span>{: style="color: goldenrod"} __$$X$$ and $$Y$$ are *independent*__{: style="color: goldenrod"}.  
    * The MI is __non-negative__: $$I(X; Y) \geq 0$$  
        * It is a measure of the price for encoding $${\displaystyle (X,Y)}$$ as a pair of independent random variables, when in reality they are not.  
    * It is __symmetric__: $$I(X; Y) = I(Y; X)$$  
    * __Related to conditional and joint entropies:__  
        <p>$${\displaystyle {\begin{aligned}\operatorname {I} (X;Y)&{}\equiv \mathrm {H} (X)-\mathrm {H} (X|Y)\\&{}\equiv \mathrm {H} (Y)-\mathrm {H} (Y|X)\\&{}\equiv \mathrm {H} (X)+\mathrm {H} (Y)-\mathrm {H} (X,Y)\\&{}\equiv \mathrm {H} (X,Y)-\mathrm {H} (X|Y)-\mathrm {H} (Y|X)\end{aligned}}}$$</p>  
        where $$\mathrm{H}(X)$$ and $$\mathrm{H}(Y)$$ are the marginal entropies, $$\mathrm{H}(X | Y)$$ and $$\mathrm{H}(Y | X)$$ are the conditional entopries, and $$\mathrm{H}(X, Y)$$ is the joint entropy of $$X$$ and $$Y$$.  
        * Note the _analogy to the **union, difference, and intersection of two sets**_:  
            ![img](https://cdn.mathpix.com/snip/images/aT2_JfK4TlRP9b5JawVqQigLD7dzxOrFjDIapoSF-F4.original.fullsize.png){: width="35%" .center-image}  
    * __Related to KL-div of conditional distribution:__  
        <p>$$\mathrm{I}(X ; Y)=\mathbb{E}_{Y}\left[D_{\mathrm{KL}}\left(p_{X | Y} \| p_{X}\right)\right]$$</p>  
    * [MI (tutorial #1)](https://www.youtube.com/watch?v=U9h1xkNELvY)  
    * [MI (tutorial #2)](https://www.youtube.com/watch?v=d7AUaut6hso)  


    __Applications:__{: style="color: red"}  
    <button>Show Lists</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    * In search engine technology, mutual information between phrases and contexts is used as a feature for k-means clustering to discover semantic clusters (concepts)  
    * Discriminative training procedures for hidden Markov models have been proposed based on the maximum mutual information (MMI) criterion.
    * Mutual information has been used as a criterion for feature selection and feature transformations in machine learning. It can be used to characterize both the relevance and redundancy of variables, such as the minimum redundancy feature selection.
    * Mutual information is used in determining the similarity of two different clusterings of a dataset. As such, it provides some advantages over the traditional Rand index.
    * Mutual information of words is often used as a significance function for the computation of collocations in corpus linguistics.  
    * Detection of phase synchronization in time series analysis
    * The mutual information is used to learn the structure of Bayesian networks/dynamic Bayesian networks, which is thought to explain the causal relationship between random variables  
    * Popular cost function in decision tree learning.
    * In the infomax method for neural-net and other machine learning, including the infomax-based Independent component analysis algorithm
    {: hidden=""}



    __Independence assumptions and low-rank matrix approximation (alternative definition):__{: style="color: red"}  
    <button>show analysis</button>{: .showText value="show"  
     onclick="showTextPopHide(event);"}
     ![img](https://cdn.mathpix.com/snip/images/jzmGBSoIKS4x2IrykIaQR3P21Y2z8RS_VmZNKkOfjZQ.original.fullsize.png){: width="100%" hidden=""}  


    __As a Metric (relation to Jaccard distance):__{: style="color: red"}  
    <button>show analysis</button>{: .showText value="show"  
     onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/dOB7qr575sMswJ1MPEbHmFvlqvJp8ncf9ulYlR4aKDY.original.fullsize.png){: width="100%" hidden=""}
    <br>


9. **Pointwise Mutual Information (PMI):**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents19}  
    The PMI of a pair of outcomes $$x$$ and $$y$$ belonging to discrete random variables $$X$$ and $$Y$$ quantifies the discrepancy between the probability of their coincidence given their joint distribution and their individual distributions, assuming independence. Mathematically:  
    <p>$$\operatorname{pmi}(x ; y) \equiv \log \frac{p(x, y)}{p(x) p(y)}=\log \frac{p(x | y)}{p(x)}=\log \frac{p(y | x)}{p(y)}$$</p>  
    In contrast to mutual information (MI) which builds upon PMI, it refers to single events, whereas MI refers to the average of all possible events.  
    The mutual information (MI) of the random variables $$X$$ and $$Y$$ is the expected value of the PMI (over all possible outcomes).  

### More
* __Conditional Entropy__: $$H(X \mid Y)=H(X)-I(X, Y)$$  
* __Independence__: $$I(X, Y)=0$$
* __Independence Relations__:  $$H(X \mid Y)=H(X)$$