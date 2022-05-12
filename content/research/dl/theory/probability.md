---
layout: NotesPage
title: Probability Theory <br /> Mathematics of Deep Learning
permalink: /work_files/research/dl/theory/probability
prevLink: /work_files/research/dl/theory.html
---


<div markdown="1" class = "TOC">
# Table of Contents

  * [Motivation](#content1)
  {: .TOC1}
  * [Basics](#content2)
  {: .TOC2}
<!--   * [THIRD](#content3)
  {: .TOC3} -->
  * [Discrete Distributions](#content9)
  {: .TOC9}
  * [Notes, Tips, and Tricks](#content10)
  {: .TOC10}
</div>

***
***

[COUNT BAYESIE: PROBABLY A PROBABILITY BLOG](https://www.countbayesie.com)  
[Review of Probability Theory (Stanford)](http://cs229.stanford.edu/section/cs229-prob.pdf)  
[A First Course in Probability (Book: _Sheldon Ross_)](http://julio.staff.ipb.ac.id/files/2015/02/Ross_8th_ed_English.pdf)  
[Statistics 110: Harvard](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo)  
[Lecture Series on Probability (following DL-book)](https://www.youtube.com/playlist?list=PLR6O_WZHBlOELxOrXlzB1LCXd2cUIXkkm)  
[Probability Quora FAQs](https://www.quora.com/What-is-the-probability-statistics-topic-FAQ)  
[Math review for Stat 110](https://projects.iq.harvard.edu/files/stat110/files/math_review_handout.pdf)  
[Deep Learning Probability](https://jhui.github.io/2017/01/05/Deep-learning-probability-and-distribution/)  
[Probability as Extended Logic](http://bjlkeng.github.io/posts/probability-the-logic-of-science/)  
[CS188 Probability Lecture (very intuitive)](https://www.youtube.com/watch?v=sMNbLXsvRig&list=PL7k0r4t5c108AZRwfW-FhnkZ0sCKBChLH&index=13&t=0s)  
[Combinatorics (Notes)](https://www.dartmouth.edu/~chance/teaching_aids/books_articles/probability_book/Chapter3.pdf)  
[Digital textbook on probability and statistics (!)](https://www.statlect.com/)  


## Motivation
{: #content1}

1. **Uncertainty in General Systems and the need for a Probabilistic Framework:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    1. __Inherent stochasticity in the system being modeled:__  
        Take Quantum Mechanics, most interpretations of quantum mechanics describe the dynamics of sub-atomic particles as being probabilistic.  
    2. __Incomplete observability__:  
        Deterministic systems can appear stochastic when we cannot observe all the variables that drive the behavior of the system.  
        > i.e. Point-of-View determinism (Monty-Hall)  
    3. __Incomplete modeling__:  
        Building a system that makes strong assumptions about the problem and discards (observed) information result in uncertainty in the predictions.    
    <br />

2. **Bayesian Probabilities and Frequentist Probabilities:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    __Frequentist Probabilities__ describe the predicted number of times that a __repeatable__ process will result in a given output in an absolute scale.  

    __Bayesian Probabilities__ describe the _degree of belief_ that a certain __non-repeatable__ event is going to result in a given output, in an absolute scale.      
    
    We assume that __Bayesian Probabilities__ behaves in exactly the same way as __Frequentist Probabilities__.  
    This assumption is derived from a set of _"common sense"_ arguments that end in the logical conclusion that both approaches to probabilities must behave the same way - [Truth and probability (Ramsey 1926)](https://socialsciences.mcmaster.ca/econ/ugcm/3ll3/ramseyfp/ramsess.pdf).

3. **Probability as an extension of Logic:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    "Probability can be seen as the extension of logic to deal with uncertainty. Logic provides a set of formal rules for determining what propositions are implied to be true or false given the assumption that some other set of propositions is true or false. Probability theory provides a set of formal rules for determining the likelihood of a proposition being true given the likelihood of other propositions." - deeplearningbook p.54


***

## Basics
{: #content2}

0. **Elements of Probability:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents20}  
    * __Sample Space $$\Omega$$__: The set of all the outcomes of a stochastic experiment; where each _outcome_ is a complete description of the state of the real world at the end of the experiment.  
    * __Event Space $${\mathcal {F}}$$__: A set of _events_; where each event $$A \in \mathcal{F}$$ is a subset of the sample space $$\Omega$$ - it is a collection of possible outcomes of an experiment.  
    * __Probability Measure $$\operatorname {P}$$__: A function $$\operatorname {P}: \mathcal{F} \rightarrow \mathbb{R}$$ that satisfies the following properties:  
        * $$\operatorname {P}(A) \geq 0, \: \forall A \in \mathcal{f}$$, 
        * $$\operatorname {P}(\Omega) = 1$$, $$\operatorname {P}(\emptyset) = 0$$[^1]  
        * $${\displaystyle \operatorname {P}(\bigcup_i A_i) = \sum_i \operatorname {P}(A_i) }$$, where $$A_1, A_2, ...$$ are [_disjoint_ events](#bodyContents102)  

    __Properties:__{: style="color: red"}  
    * $${\text { If } A \subseteq B \Longrightarrow P(A) \leq P(B)}$$,   
    * $${P(A \cap B) \leq \min (P(A), P(B))} $$,  
    * __Union Bound:__ $${P(A \cup B) \leq P(A)+P(B)}$$  
    * $${P(\Omega \backslash A)=1-P(A)}$$.  
    * __Law of Total Probability (LOTB):__ $$\text { If } A_{1}, \ldots, A_{k} \text { are a set of disjoint events such that } \cup_{i=1}^{k} A_{i}=\Omega, \text { then } \sum_{i=1}^{k} P\left(A_{k}\right)=1$$  
    * __Inclusion-Exclusion Principle__:  
        <p>$$\mathbb{P}\left(\bigcup_{i=1}^{n} A_{i}\right)=\sum_{i=1}^{n} \mathbb{P}\left(A_{i}\right)-\sum_{i< j} \mathbb{P}\left(A_{i} \cap A_{j}\right)+\sum_{i< j < k} \mathbb{P}\left(A_{i} \cap A_{j} \cap A_{k}\right)-\cdots+(-1)^{n-1} \sum_{i< \ldots< n} \mathbb{P}\left(\bigcap_{i=1}^{n} A_{i}\right)$$</p>  
        * [**Example 110**](https://www.youtube.com/embed/LZ5Wergp_PA?start=2057){: value="show" onclick="iframePopA(event)"}
        <a href="https://www.youtube.com/embed/LZ5Wergp_PA?start=2057"></a>
            <div markdown="1"> </div>    
              

    * [**Properties and Proofs 110**](https://www.youtube.com/embed/LZ5Wergp_PA?start=1359){: value="show" onclick="iframePopA(event)"}
    <a href="https://www.youtube.com/embed/LZ5Wergp_PA?start=1359"></a>
        <div markdown="1"> </div>    

[^1]: Corresponds to "wanting" the probability of events that are __certain__ to have p=1 and events that are __impossible__ to have p=0  
                

1. **Random Variables:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    A __Random Variable__ is a variable that can take on different values randomly.  
    Formally, a random variable $$X$$ is a _function_ that maps outcomes to numerical quantities (labels), typically real numbers:
    <p>$${\displaystyle X\colon \Omega \to \mathbb{R}}$$</p>  

    Think of a R.V.: as a numerical "summary" of an aspect of the experiment.  

    __Types__:
    * *__Discrete__*: is a variable that has a finite or countably infinite number of states  
    * *__Continuous__*: is a variable that is a real value  

    __Examples:__  
    * __Bernoulli:__ A r.v. $$X$$ is said to have a __Bernoulli__ distribution if $$X$$ has only $$2$$ possible values, $$0$$ and $$1$$, and $$P(X=1) = p, P(X=0) = 1-p$$; denoted $$\text{Bern}(p)$$.    
    * __Binomial__: The distr. of #successes in $$n$$ independent __$$\text{Bern}(p)$$__ trials and its distribution is $$P(X=k) = \left(\begin{array}{l}{n} \\ {k}\end{array}\right) p^k (1-p)^{n-k}$$; denoted $$\text{Bin}(n, p)$$.          
    <br>

2. **Probability Distributions:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}  
    A __Probability Distribution__ is a function that describes the likelihood that a random variable (or a set of r.v.) will take on each of its possible states.  
    Probability Distributions are defined in terms of the __Sample Space__.  
    * __Classes__:  
        * *__Discrete Probability Distribution:__* is encoded by a discrete list of the probabilities of the outcomes, known as a __Probability Mass Function (PMF)__.  
        * *__Continuous Probability Distribution:__* is described by a __Probability Density Function (PDF)__.  
    * __Types__:  
        * *__Univariate Distributions:__* are those whose sample space is $$\mathbb{R}$$.  
        They give the probabilities of a single random variable taking on various alternative values 
        * *__Multivariate Distributions__* (also known as *__Joint Probability distributions__*):  are those whose sample space is a vector space.   
        They give the probabilities of a random vector taking on various combinations of values.  


    A __Cumulative Distribution Function (CDF)__: is a general functional form to describe a probability distribution:  
    <p>$${\displaystyle F(x)=\operatorname {P} [X\leq x]\qquad {\text{ for all }}x\in \mathbb {R} .}$$</p>  
    > Because a probability distribution P on the real line is determined by the probability of a scalar random variable X being in a half-open interval $$(−\infty, x]$$, the probability distribution is completely characterized by its cumulative distribution function (i.e. one can calculate the probability of any event in the event space)  
    
 

3. **Probability Mass Function:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}  
    A __Probability Mass Function (PMF)__ is a function (probability distribution) that gives the probability that a discrete random variable is exactly equal to some value.  
    __Mathematical Definition__:  
    Suppose that $$X: S \rightarrow A, \:\:\: (A {\displaystyle \subseteq }  \mathbb{R})$$ is a discrete random variable defined on a sample space $$S$$. Then the probability mass function $$f_X: A \rightarrow [0, 1]$$ for $$X$$ is defined as:   
    <p>$$p_{X}(x)=P(X=x)=P(\{s\in S:X(s)=x\})$$</p>  
    The __total probability for all hypothetical outcomes $$x$$ is always conserved__:  
    <p>$$\sum _{x\in A}p_{X}(x)=1$$</p>
    __Joint Probability Distribution__ is a PMF over many variables, denoted $$P(\mathrm{x} = x, \mathrm{y} = y)$$ or $$P(x, y)$$.  

    A __PMF__ must satisfy these properties:  
    * The domain of $$P$$ must be the set of all possible states of $$\mathrm{x}$$.  
    * $$\forall x \in \mathrm{x}, \: 0 \leq P(x) \leq 1$$. Impossible events has probability $$0$$. Guaranteed events have probability $$1$$.  
    * $${\displaystyle \sum_{x \in \mathrm{x}} P(x) = 1}$$, i.e. the PMF must be normalized.  
    <br>
            
4. **Probability Density Function:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}  
    A __Probability Density Function (PDF)__ is a function (probability distribution) whose value at any given sample (or point) in the sample space can be interpreted as providing a relative likelihood that the value of the random variable would equal that sample.  
    The __PDF__ is defined as the _derivative_ of the __CDF__:  
    <p>$$f_{X}(x) = \dfrac{dF_{X}(x)}{dx}$$</p>  
    A Probability Density Function $$p(x)$$ does not give the probability of a specific state directly; instead the probability of landing inside an infinitesimal region with volume $$\delta x$$ is given by $$p(x)\delta x$$.  
    We can integrate the density function to find the actual probability mass of a set of points. Specifically, the probability that $$x$$ lies in some set $$S$$ is given by the integral of $$p(x)$$ over that set.  
    > In the __Univariate__ example, the probability that $$x$$ lies in the interval $$[a, b]$$ is given by $$\int_{[a, b]} p(x)dx$$  


    A __PDF__ must satisfy these properties:  
    * The domain of $$P$$ must be the set of all possible states of $$x$$.  
    * $$\forall x \in \mathrm{x}, \: 0 \leq P(x) \leq 1$$. Impossible events has probability $$0$$. Guaranteed events have probability $$1$$.  
    * $$\int p(x)dx = 1$$, i.e. the integral of the PDF must be normalized.  
    <br>


44. **Cumulative Distribution Function:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents244}  
    A __Cumulative Distribution Function (CDF)__ is a function (probability distribution) of a real-valued random variable $$X$$, or just distribution function of $$X$$, evaluated at $$x$$, is the probability that $$X$$ will take a value less than or equal to $$x$$.    
    <p>$$F_{X}(x)=\operatorname {P} (X\leq x)$$ </p>  
    The probability that $$X$$ lies in the semi-closed interval $$(a, b]$$, where $$a  <  b$$, is therefore  
    <p>$${\displaystyle \operatorname {P} (a<X\leq b)=F_{X}(b)-F_{X}(a).}$$</p>  
    
    __Properties__:    
    * $$0 \leq F(x) \leq 1$$, 
    * $$\lim_{x \rightarrow -\infty} F(x) = 0$$, 
    * $$\lim_{x \rightarrow \infty} F(x) = 1$$, 
    * $$x \leq y \implies F(x) \leq F(y)$$.  
    <br>

5. **Marginal Probability:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}  
    The __Marginal Distribution__ of a subset of a collection of random variables is the probability distribution of the variables contained in the subset.  
    __Two-variable Case__:  
    Given two random variables $$X$$ and $$Y$$ whose joint distribution is known, the marginal distribution of $$X$$ is simply the probability distribution of $$X$$ averaging over information about $$Y$$.
    * __Discrete__:    
        <p>$${\displaystyle \Pr(X=x)=\sum_ {y}\Pr(X=x,Y=y)=\sum_ {y}\Pr(X=x\mid Y=y)\Pr(Y=y)}$$</p>    
    * __Continuous__:    
        <p>$${\displaystyle p_{X}(x)=\int _{y}p_{X,Y}(x,y)\,\mathrm {d} y=\int _{y}p_{X\mid Y}(x\mid y)\,p_{Y}(y)\,\mathrm {d} y}$$</p>  
    * *__Marginal Probability as Expectation__*:    
    <p>$${\displaystyle p_{X}(x)=\int _{y}p_{X\mid Y}(x\mid y)\,p_{Y}(y)\,\mathrm {d} y=\mathbb {E} _{Y}[p_{X\mid Y}(x\mid y)]}$$</p>  
    <button>Intuitive Explanation</button>{: .showText value="show"  
     onclick="showTextPopHide(event);"}
    ![img](/main_files/math/prob/1.png){: width="100%" hidden=""}  

    __Marginalization:__{: style="color: red"} the process of forming the marginal distribution with respect to one variable by summing out the other variable  

    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * __Marginal Distribution of a variable__: is just the prior distr of the variable  
    * __Marginal Likelihood__: also known as the evidence, or model evidence, is the denominator of the Bayes equation. Its only role is to guarantee that the posterior is a valid probability by making its area sum to 1.  
        ![Example](https://cdn.mathpix.com/snip/images/UPUhBUhhUivvvIHO3nt5S52UcqPkSMS_eZEg3mhDXhk.original.fullsize.png)  
    * __both terms above are the same__  
    * __Marginal Distr VS Prior__:  
        * [Discussion](https://stats.stackexchange.com/questions/249275/whats-the-difference-between-prior-and-marginal-probabilities?rq=1)  
        * __Summary__:  
            Basically, it's a conceptual difference.  
            The prior, denoted $$p(\theta)$$, denotes the probability of some event 𝜔 even before any data has been taken.  
            A marginal distribution is rather different. You hold a variable value and integrate over the unknown values.  
            But, in some contexts they are the same.  

            


            


6. **Conditional Probability:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents26}  
    __Conditional Probability__ is a measure of the probability of an event given that another event has occurred.  
    Conditional Probability is only defined when $$P(x) > 0$$ - We cannot compute the conditional probability conditioned on an event that never happens.   
    __Definition__:  
    <p>$$P(A|B)={\frac {P(A\cap B)}{P(B)}} = {\frac {P(A, B)}{P(B)}}$$</p>  

    > Intuitively, it is a way of updating your beliefs/probabilities given new evidence. It's inherently a sequential process.  



7. **The Chain Rule of Conditional Probability:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents27}  
    Any joint probability distribution over many random variables may be decomposed into conditional distributions over only one variable.  
    The chain rule permits the calculation of any member of the joint distribution of a set of random variables using only conditional probabilities:    
    <p>$$\mathrm {P} \left(\bigcap _{k=1}^{n}A_{k}\right)=\prod _{k=1}^{n}\mathrm {P} \left(A_{k}\,{\Bigg |}\,\bigcap _{j=1}^{k-1}A_{j}\right)$$</p>  

8. **Independence and Conditional Independence:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents28}  
    Two random variables $$x$$ and $$y$$ (or events ) are __independent__ if their probability distribution can be expressed as a product of two factors, one involving only $$x$$ and one involving only $$y$$:  
    <p>$$\mathrm{P}(A \cap B) = \mathrm{P}(A)\mathrm{P}(B)$$</p>  

    Two random variables $$A$$ and $$B$$ are __conditionally independent__ _given a random variable $$Y$$_ if the conditional probability distribution over $$A$$ and $$B$$ factorizes in this way for every value of $$Y$$:  
    <p>$$\Pr(A\cap B\mid Y)=\Pr(A\mid Y)\Pr(B\mid Y)$$</p>  
    or equivalently,  
    <p>$$\Pr(A\mid B\cap Y)=\Pr(A\mid Y)$$</p>  
    > In other words, $$A$$ and $$B$$ are conditionally independent given $$Y$$ if and only if, given knowledge that $$Y$$ occurs, knowledge of whether $$A$$ occurs provides no information on the likelihood of $$B$$ occurring, and knowledge of whether $$B$$ occurs provides no information on the likelihood of $$A$$ occurring.  


    __Pairwise VS Mutual Independence:__{: style="color: red"}  
    * __Pairwise__:  
        <p>$$\mathrm{P}\left(A_{m} \cap A_{k}\right)=\mathrm{P}\left(A_{m}\right) \mathrm{P}\left(A_{k}\right)$$</p>  
    * __Mutual Independence:__
        <p>$$\mathrm{P}\left(\bigcap_{i=1}^{k} B_{i}\right)=\prod_{i=1}^{k} \mathrm{P}\left(B_{i}\right)$$</p>  
        for *__all subsets__* of size $$k \leq n$$  

    __Pairwise__ independence does __not__ imply __mutual__ independence, but the other way around is TRUE (by definition).  



    __Notation:__  
    * *__$$A$$ is Independent from $$B$$__*:  $$A{\perp}B$$
    * *__$$A$$ and $$B$$ are conditionally Independent given $$Y$$__*:  $$A{\perp}B \:\vert Y$$  

    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * Unconditional Independence is very rare (there is usually some hidden factor influencing the interaction between the two events/variables)  
    * _Conditional Independence_ is the most basic and robust form of knowledge about uncertain environments  
            
    <br>
                
9. **Expectation:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents29}  
    The __expectation__, or __expected value__, of some function $$f(x)$$ with respect to a probability distribution $$P(x)$$ is the _"theoretical"_ average, or mean value, that $$f$$ takes on when $$x$$ is drawn from $$P$$.  
    > The Expectation of a R.V. is a weighted average of the values $$x$$ that the R.V. can take -- $$\operatorname {E}[X] = \sum_{x \in X} x \cdot p(x)$$  
    * __Discrete case__:  
        <p>$${\displaystyle \operatorname {E}_{x \sim P} [f(X)]=f(x_{1})p(x_{1})+f(x_{2})p(x_{2})+\cdots +f(x_{k})p(x_{k})} = \sum_x P(x)f(x)$$</p>             
    * __Continuous case__:  
    <p>$${\displaystyle \operatorname {E}_ {x \sim P} [f(X)] = \int p(x)f(x)dx}$$</p>   
    __Linearity of Expectation:__  
    <p>$${\displaystyle {\begin{aligned}\operatorname {E} [X+Y]&=\operatorname {E} [X]+\operatorname {E} [Y],\\[6pt]\operatorname {E} [aX]&=a\operatorname {E} [X],\end{aligned}}}$$</p>   
    __Independence:__   
    If $$X$$ and $$Y$$ are independent $$\implies \operatorname {E} [XY] = \operatorname {E} [X] \operatorname {E} [Y]$$  
    <br>

10. **Variance:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents210}  
    __Variance__ is the expectation of the squared deviation of a random variable from its mean.  
    It gives a measure of how much the values of a function of a random variable $$x$$ vary as we sample different values of $$x$$ from its probability distribution:  
    <p>$$\operatorname {Var} (f(x))=\operatorname {E} \left[(f(x)-\mu )^{2}\right] = \sum_{x \in X} (x - \mu)^2 \cdot p(x)$$</p>  
    __Variance expanded__:  
    <p>$${\displaystyle {\begin{aligned}\operatorname {Var} (X)&=\operatorname {E} \left[(X-\operatorname {E} [X])^{2}\right]\\
        &=\operatorname {E} \left[X^{2}-2X\operatorname {E} [X]+\operatorname {E} [X]^{2}\right]\\
        &=\operatorname {E} \left[X^{2}\right]-2\operatorname {E} [X]\operatorname {E} [X]+\operatorname {E} [X]^{2}\\
        &=\operatorname {E} \left[X^{2}\right]-\operatorname {E} [X]^{2}\end{aligned}}}$$  </p>   
    __Variance as Covariance__: 
    Variance can be expressed as the covariance of a random variable with itself: 
    <p>$$\operatorname {Var} (X)=\operatorname {Cov} (X,X)$$</p>   
    
    __Properties:__  
    {: #lst-p}
    * $$\operatorname {Var} [a] = 0, \forall a \in \mathbb{R}$$ (constant $$a$$)  
    * $$\operatorname {Var} [af(X)] = a^2 \operatorname {Var} [f(X)]$$ (constant $$a$$)
    * $$\operatorname {Var} [X + Y] = a^2 \operatorname {Var} [X] + \operatorname {Var} [Y] + 2 \operatorname {Cov} [X, Y]$$.  

    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * When comparing Variances, *__ALWAYS NORMALIZE FIRST__*: Variance depends on Scale  
    <br>

11. **Standard Deviation:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents211}  
    The __Standard Deviation__ is a measure that is used to quantify the amount of variation or dispersion of a set of data values.  
    It is defined as the square root of the variance:  
    <p>$${\displaystyle {\begin{aligned}\sigma &={\sqrt {\operatorname {E} [(X-\mu )^{2}]}}\\&={\sqrt {\operatorname {E} [X^{2}]+\operatorname {E} [-2\mu X]+\operatorname {E} [\mu ^{2}]}}\\&={\sqrt {\operatorname {E} [X^{2}]-2\mu \operatorname {E} [X]+\mu ^{2}}}\\&={\sqrt {\operatorname {E} [X^{2}]-2\mu ^{2}+\mu ^{2}}}\\&={\sqrt {\operatorname {E} [X^{2}]-\mu ^{2}}}\\&={\sqrt {\operatorname {E} [X^{2}]-(\operatorname {E} [X])^{2}}}\end{aligned}}}$$</p>  
    
    __Properties:__  
    * 68% of the data-points lie within $$1 \cdot \sigma$$s from the mean
    * 95% of the data-points lie within $$2 \cdot \sigma$$s from the mean
    * 99% of the data-points lie within $$3 \cdot \sigma$$s from the mean
    <br>

12. **Covariance:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents212}  
    __Covariance__ is a measure of the joint variability of two random variables.  
    It gives some sense of how much two values are linearly related to each other, as well as the scale of these variables:  
    <p>$$\operatorname {cov} (X,Y)=\operatorname {E} { {\big[ }(X-\operatorname {E} [X])(Y-\operatorname {E} [Y]){ \big] } }$$ </p>  
    __Covariance expanded:__  
    <p>$${\displaystyle {\begin{aligned}\operatorname {cov} (X,Y)&=\operatorname {E} \left[\left(X-\operatorname {E} \left[X\right]\right)\left(Y-\operatorname {E} \left[Y\right]\right)\right]\\&=\operatorname {E} \left[XY-X\operatorname {E} \left[Y\right]-\operatorname {E} \left[X\right]Y+\operatorname {E} \left[X\right]\operatorname {E} \left[Y\right]\right]\\&=\operatorname {E} \left[XY\right]-\operatorname {E} \left[X\right]\operatorname {E} \left[Y\right]-\operatorname {E} \left[X\right]\operatorname {E} \left[Y\right]+\operatorname {E} \left[X\right]\operatorname {E} \left[Y\right]\\&=\operatorname {E} \left[XY\right]-\operatorname {E} \left[X\right]\operatorname {E} \left[Y\right].\end{aligned}}}$$ </p>  
    > when $${\displaystyle \operatorname {E} [XY]\approx \operatorname {E} [X]\operatorname {E} [Y]} $$, this last equation is prone to catastrophic cancellation when computed with floating point arithmetic and thus should be avoided in computer programs when the data has not been centered before.  

    __Covariance of Random Vectors__:  
    <p>$${\begin{aligned}\operatorname {cov} (\mathbf {X} ,\mathbf {Y} )&=\operatorname {E} \left[(\mathbf {X} -\operatorname {E} [\mathbf {X} ])(\mathbf {Y} -\operatorname {E} [\mathbf {Y} ])^{\mathrm {T} }\right]\\&=\operatorname {E} \left[\mathbf {X} \mathbf {Y} ^{\mathrm {T} }\right]-\operatorname {E} [\mathbf {X} ]\operatorname {E} [\mathbf {Y} ]^{\mathrm {T} },\end{aligned}}$$ </p>  

    __The Covariance Matrix__ of a random vector $$x \in \mathbb{R}^n$$ is an $$n \times n$$ matrix, such that:    
    <p>$$ \operatorname {cov} (X)_ {i,j} = \operatorname {cov}(x_i, x_j) \\
        \operatorname {cov}(x_i, x_j) = \operatorname {Var} (x_i)$$</p>   
    __Interpretations__:  
    * High absolute values of the covariance mean that the values change very much and are both far from their respective means at the same time.
    * __The sign of the covariance__:   
        The sign of the covariance shows the tendency in the linear relationship between the variables:  
        * *__Positive__*:  
            the variables tend to show similar behavior
        * *__Negative__*:  
            the variables tend to show opposite behavior  
        * __Reason__:  
        If the greater values of one variable mainly correspond with the greater values of the other variable, and the same holds for the lesser values, (i.e., the variables tend to show similar behavior), the covariance is positive. In the opposite case, when the greater values of one variable mainly correspond to the lesser values of the other, (i.e., the variables tend to show opposite behavior), the covariance is negative.  

    __Covariance and Variance:__  
    <p>$$\operatorname{Var}[X+Y]=\operatorname{Var}[X]+\operatorname{Var}[Y]+2 \operatorname{Cov}[X, Y]$$</p>  

    __Covariance and Independence:__  
    If $$X$$ and $$Y$$ are independent $$\implies \operatorname{cov}[X, Y]=\mathrm{E}[X Y]-\mathrm{E}[X] \mathrm{E}[Y] = 0$$.  
    * Independence $$\Rightarrow$$ Zero Covariance  
    * Zero Covariance $$\nRightarrow$$ Independence

    __Covariance and Correlation:__  
    If $$\operatorname{Cov}[X, Y]=0 \implies $$ $$X$$ and $$Y$$ are __Uncorrelated__.  

    * [**Covariance/Correlation Intuition**](https://www.youtube.com/embed/KDw3hC2YNFc){: value="show" onclick="iframePopA(event)"}
    <a href="https://www.youtube.com/embed/KDw3hC2YNFc"></a>
        <div markdown="1"> </div>    
    * [**Covariance and Correlation (Harvard Lecture)**](https://www.youtube.com/embed/IujCYxtpszU){: value="show" onclick="iframePopA(event)"}
    <a href="https://www.youtube.com/embed/IujCYxtpszU"></a>
        <div markdown="1"> </div>    
    * [**Covariance as slope of the Regression Line**](https://www.youtube.com/embed/ualmyZiPs9w){: value="show" onclick="iframePopA(event)"}
    <a href="https://www.youtube.com/embed/ualmyZiPs9w"></a>
        <div markdown="1"> </div>    

    <br>  

13. **Mixtures of Distributions:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents213}  
    It is also common to define probability distributions by combining other simpler probability distributions. One common way of combining distributions is to construct a __mixture distribution__.    
    A __Mixture Distribution__ is the probability distribution of a random variable that is derived from a collection of other random variables as follows: first, a random variable is selected by chance from the collection according to given probabilities of selection, and then the value of the selected random variable is realized.    
    On each trial, the choice of which component distribution should generate the sample is determined by sampling a component identity from a multinoulli distribution:  
    <p>$$P(x) = \sum_i P(x=i)P(x \vert c=i)$$</p>    
    where $$P(c)$$ is the multinoulli distribution over component identities.    

14. **Bayes' Rule:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents214}  
    __Bayes' Rule__ describes the probability of an event, based on prior knowledge of conditions that might be related to the event.    
    <p>$${\displaystyle P(A\mid B)={\frac {P(B\mid A)\,P(A)}{P(B)}}}$$</p>  
    where,   
    <p>$$P(B) =\sum_A P(B \vert A) P(A)$$</p>  


15. **Common Random Variables:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents215}  
    __Discrete RVs:__{: style="color: red"}    
    {: #lst-p}
    * __Bernoulli__:  
    ![img](/main_files/math/prob/2.png){: width="90%"}  
    * __Binomial__:  
    ![img](/main_files/math/prob/3.png){: width="90%"}  
    * __Geometric__:  
    ![img](/main_files/math/prob/4.png){: width="90%"}  
    * __Poisson__:  
    ![img](/main_files/math/prob/5.png){: width="90%"}  

    __Continuous RVs:__{: style="color: red"}  
    {: #lst-p}
    * __Uniform__:  
    ![img](/main_files/math/prob/6.png){: width="90%"}  
    * __Exponential__:  
    ![img](/main_files/math/prob/7.png){: width="90%"}  
    * __Normal/Gaussian__:  
    ![img](/main_files/math/prob/8.png){: width="90%"}  
            
            
16. **Summary of Distributions:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents216}  
    ![img](/main_files/math/prob/9.png){: width="80%"}  


17. **Formulas:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents217}  
    * $$\overline{X} = \hat{\mu}$$,  
    * $$\operatorname {E}[\overline{X}]=\operatorname {E}\left[\frac{X_{1}+\cdots+X_{n}}{n}\right] = \mu$$,  
    * $$\operatorname{Var}[\overline{X}]=\operatorname{Var}\left[\frac{X_{1}+\cdots+X_{n}}{n}\right] = \dfrac{\sigma^2}{n}$$,    
    * $$\operatorname {E}\left[X_{i}^{2}\right]=\operatorname {Var} [X]+\operatorname {E} [X]^{2} = \sigma^{2}+\mu^{2}$$,  
    * $$\operatorname {E}\left[\overline{X}^{2}\right]=\operatorname {E}\left[\hat{\mu}^{2}\right]=\frac{\sigma^{2}}{n}+\mu^{2}\:$$, [^2]  
    <br>


18. **Correlation:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents218}  
    In the broadest sense __correlation__ is any statistical association, though it commonly refers to the degree to which a pair of variables are linearly related.  

    There are several correlation coefficients, often denoted $${\displaystyle \rho }$$ or $$r$$, measuring the degree of correlation:  

    __Pearson Correlation Coefficient [\[wiki\]](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient):__{: style="color: red"}  
    It is a measure of the __linear correlation__ between two variables $$X$$ and $$Y$$.  
    <p>$$\rho_{X, Y}=\frac{\operatorname{cov}(X, Y)}{\sigma_{X} \sigma_{Y}}$$</p>  
    where, $${\displaystyle \sigma_{X}}$$ is the standard deviation of $${\displaystyle X}$$ and $${\displaystyle \sigma_{Y}}$$  is the standard deviation of $${\displaystyle Y}$$, and $$\rho \in [-1, 1]$$.   



    __Correlation and Independence:__{: style="color: red"}  
    1. Uncorrelated $$\nRightarrow$$ Independent  
    2. Independent $$\implies$$ Uncorrelated  

    Zero correlation will indicate no linear dependency, however won't capture non-linearity. Typical example is uniform random variable $$x$$, and $$x^2$$ over $$[-1,1]$$ with zero mean. Correlation is zero but clearly not independent.  
    <br> 

19. **Probabilistic Inference:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents219}  
    __Probabilistic Inference:__ compute a desired probability from other known probabilities (e.g. conditional from joint).  

    __We generally compute Conditional Probabilities:__  
    {: #lst-p}
    * $$p(\text{sun} \vert T=\text{12 pm}) = 0.99$$  
    * These represent the agents beliefs given the evidence  

    __Probabilities change with new evidence:__  
    {: #lst-p} 
    * $$p(\text{sun} \vert T=\text{12 pm}, C=\text{Stockholm}) = 0.85$$  
    $$\longrightarrow$$  
    * $$p(\text{sun} \vert T=\text{12 pm}, C=\text{Stockholm}, M=\text{Jan}) = 0.40$$  
    * Observing new evidence causes beliefs to be updated

    __Inference by Enumeration:__{: style="color: red"}  
    {: #lst-p}
    * [**CS188 Lec. 10-2**](https://www.youtube.com/embed/sMNbLXsvRig?start=3508){: value="show" onclick="iframePopA(event)"}
    <a href="https://www.youtube.com/embed/sMNbLXsvRig?start=3508"></a>
        <div markdown="1"> </div>    

    __Problems:__  
    * Worst-case time complexity $$\mathrm{O}\left(\mathrm{d}^{n}\right)$$
    * Space complexity $$\mathrm{O}\left(\mathrm{d}^{n}\right)$$ to store the joint distribution  

    __Inference with Bayes Theorem:__{: style="color: red"}  
    * __Diagnostic Probability from Causal Probability:__  
        <p>$$P(\text { cause } | \text { effect })=\frac{P(\text { effect } | \text { cause }) P(\text { cause })}{P(\text { effect })}$$</p>  




[^2]: Comes from $$\operatorname{Var}[\overline{X}]=\operatorname {E}\left[\overline{X}^{2}\right]-\{\operatorname {E}[\overline{X}]\}^{2}$$  


***

## Discrete Distributions
{: #content9}

<!-- 1. **Uniform Distribution:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents91}   -->

2. **Bernoulli Distribution:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents92}  
    :   A distribution over a single binary random variable.  
        It is controlled by a single parameter $$\phi \in [0, 1]$$, which fives the probability of the r.v. being equal to $$1$$.  
        > It models the probability of a single experiment with a boolean outcome (e.g. coin flip $$\rightarrow$$ {heads: 1, tails: 0})  
    :   __PMF:__  
    :   $${\displaystyle P(x)={\begin{cases}p&{\text{if }}p=1,\\q=1-p&{\text{if }}p=0.\end{cases}}}$$  
    :   __Properties:__  
        <p>$$P(X=1) = \phi$$</p>
        <p>$$P(X=0) = 1 - \phi$$</p>
        <p>$$P(X=x) = \phi^x (1 - \phi)^{1-x}$$</p>
        <p>$$\operatorname {E}[X] = \phi$$</p>
        <p>$$\operatorname {Var}(X) = \phi (1 - \phi)$$</p>

3. **Binomial Distribution:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents93}     
    > $${\binom {n}{k}}={\frac {n!}{k!(n-k)!}}$$ is the number of possible ways of getting $$x$$ successes and $$n-x$$ failures

<!-- 4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents94}  
5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents95}  
6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents96}  
7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents97}  
8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents98}   -->

***

## 110
{: #content99}

1. **Problems:**{: style="color: SteelBlue"}{: .bodyContents99 #bodyContents991}  
    * [**deMortmonts/Matching problem**](https://www.youtube.com/embed/LZ5Wergp_PA?start=2305){: value="show" onclick="iframePopA(event)"}
    <a href="https://www.youtube.com/embed/LZ5Wergp_PA?start=2305"></a>
        <div markdown="1"> </div>    
        Sol: Inclusion-Exclusion  
    * [**Newton-Pepys: most likely event of rolling 6's in dice**](https://www.youtube.com/embed/P7NE4WF8j-Q?start=1057){: value="show" onclick="iframePopA(event)"}
    <a href="https://www.youtube.com/embed/P7NE4WF8j-Q?start=1057"></a>
        <div markdown="1"> </div>    
    
***

## Notes, Tips and Tricks
{: #content10}

* It is more practical to use a simple but uncertain rule rather than a complex but certain one, even if the true rule is deterministic and our modeling system has the fidelity to accommodate a complex rule.  
    For example, the simple rule “Most birds fly” is cheap to develop and is broadly useful, while a rule of the form, “Birds fly, except for very young birds that have not yet learned to fly, sick or injured birds that have lost the ability to fly, flightless species of birds including the cassowary, ostrich and kiwi. . .” is expensive to develop, maintain and communicate and, after all this effort, is still brittle and prone to failure.

* __Disjoint Events (Mutually Exclusive):__{: .bodyContents10 #bodyContents102} are events that cannot occur together at the same time
    Mathematically:  
    * $$A_i \cap A_j = \varnothing$$ whenever $$i \neq j$$  
    * $$p(A_i, A_j) = 0$$,  

* __Complexity of Describing a Probability Distribution__:  
    A description of a probability distribution is _exponential_ in the number of variables it models.  
    The number of possibilities is __exponential__ in the number of variables.  

* __Probability VS Likelihood__:  
    __Probabilities__ are the areas under a fixed distribution  
    $$pr($$data$$|$$distribution$$)$$  
    i.e. probability of some _data_ (left hand side) given a distribution (described by the right hand side)  
    __Likelihoods__ are the y-axis values for fixed data points with distributions that can be moved..  
    $$L($$distribution$$|$$observation/data$$)$$  

    > Likelihood is, basically, a specific probability that can only be calculated after the fact (of observing some outcomes). It is not normalized to $$1$$ (it is __not__ a probability). It is just a way to quantify how likely a set of observation is to occur given some distribution with some parameters; then you can manipulate the parameters to make the realization of the data more _"likely"_ (it is precisely meant for that purpose of estimating the parameters); it is a _function_ of the __parameters__.  
    Probability, on the other hand, is absolute for all possible outcomes. It is a function of the __Data__.  

* __Maximum Likelihood Estimation__:  
    A method that tries to find the _optimal value_ for the _mean_ and/or _stdev_ for a distribution *__given__* some observed measurements/data-points.

* __Variance__:  
    When $$\text{Var}(X) = 0 \implies X = E[X] = \mu$$. (not interesting)  

* __Reason we sometimes prefer Biased Estimators__:  
        