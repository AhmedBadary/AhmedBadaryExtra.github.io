---
layout: NotesPage
title: Computational Learning Theory
permalink: /work_files/research/dl/theory/comp_learning_theory
prevLink: /work_files/research/dl/theory.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [FIRST](#content1)
  {: .TOC1}
  * [SECOND](#content2)
  {: .TOC2}
<!--     * [THIRD](#content3)
  {: .TOC3}
  * [FOURTH](#content4)
  {: .TOC4}
  * [FIFTH](#content5)
  {: .TOC5}
  * [SIXTH](#content6)
  {: .TOC6} -->
</div>

***
***

* [Learning Theory (Formal, Computational or Statistical) (Blog + references!)](http://bactra.org/notebooks/learning-theory.html)  


## FIRST
{: #content1}

<!-- 1. **Linear Models:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}
3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}
4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}
5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}
6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}
7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}
8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18} -->

***

## SECOND
{: #content2}

1. **Bayesian Learning:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    __Main Idea:__{: style="color: red"}  
    Instead of __looking__ for the <span>__most likely setting__ of the parameters</span>{: style="color: purple"} of a model we should __consider__ <span>__all possible settings__ of the parameters</span>{: style="color: purple"} and try and __estimate__ <span>for each of those possible settings __how probable it__ is _given the data_</span>{: style="color: purple"} _we observed_.  

    __The Bayesian Framework:__{: style="color: red"}  
    {: #lst-p}
    * __Prior-Belief Assumption:__{: style="color: DarkRed"}  
        The Bayesian framework assumes that we always have a prior distribution for everything.  
        * The prior may be very vague
        * When we see some data, we combine our prior distribution with a likelihood term to get a posterior distribution.  
        * The likelihood term takes into account how probable the observed data is given the parameters of the model:  
            * It favors parameter settings that make the data likely  
            * It fights the prior  
            * With enough data the likelihood terms always wins
        * [Continue NoteTaking (has great example) (Hinton Lec)](https://www.youtube.com/watch?v=NY1zXgIma3c&list=PLiPvV5TNogxKKwvKb1RKwkq2hm7ZvpHz0&index=58&t=47)  

    * __Bayes Theorem__:  
        <p>$$p(\mathcal{D}) p(\mathbf{\theta} \vert \mathcal{D})=\underbrace{p(\mathcal{D}, \mathbf{\theta})}_ {\text{joint probability}}=p(\mathbf{\theta}) p(\mathcal{D} \vert \mathbf{\theta})$$</p>  
        <p>$$\implies \\ p(\mathbf{\theta} \vert \mathcal{D}) = \dfrac{p(\mathbf{\theta}) p(\mathcal{D} \vert \mathbf{\theta})}{p(\mathcal{D})} = \dfrac{p(\mathbf{\theta}) p(\mathcal{D} \vert \mathbf{\theta})}{\int_{\mathbf{\theta}} p(\mathbf{\theta}) p(\mathcal{D} \vert \mathbf{\theta})}$$</p>  



    __Bayesian Probability:__{: style="color: red"}  
    {: #lst-p}
    * __Interpreting the Prior:__{: style="color: red"}  
        The prior probability of any event $$q$$, $$p(q)$$, <span>_quantifies_ the current __state of knowledge__ (*__Uncertainty__*)</span>{: style="color: purple"} of $$q$$.  
        Regardless whether $$q$$ is __deterministic__ or __random__.   
    * __Modeling Randomness:__{: style="color: red"}  
        If randomness is being modeled it would be modeled as a __stochastic process__ with *__fixed__* __parameters__.  
        For example random noise is often modeled as being generated from a normal distribution with some fixed (but possibly unknown) mean and covariance.  
    * __Interpreting Parameters:__{: style="color: red"}  
        Bayesians do *__not__* view parameters as being __stochastic__.  
        So, for instance, if we find that according to the posterior p(0.1 < p_1 < 0.2) = 0.10 that would be interpreted as "There is a 10% chance p_1 is between 0.1 and 0.2" not "p_1 is between 0.1 and 0.2 10% of the time".  



    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * A Bayesian is one who, vaguely expecting a horse, and catching a glimpse of a donkey, strongly believes he has seen a mule.  
    <br>


    <!-- 2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22} -->  

3. **Bayesian vs Frequentist Learning:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}  
    
    __Differences:__{: style="color: red"}  
    {: #lst-p}
    * __Translating Events into the Theory - Assigning a Probability Distribution:__{: style="color: red"}  
        * __Bayesian__: no need for __Random Variables__.  
            A probability distribution is assigned to a quantity because it is unknown - which means that it cannot be deduced logically from the information we have.  
        * __Frequentist__: needs a __Random Variable__.  
            A quantity/event that is __stochastic/random__ can be modeled as a __random variable__.  
    * __Unknown vs Random__{: style="color: red"}  
        * __Bayesian__: assumes quantities can be <span>unknown</span>{: style="color: purple"}.  
            __Subjective View:__ "being unknown" depends on which person you are asking about that quantity - hence it is a property of the statistician doing the analysis.  
        * __Frequentist__: assumes quantities can be <span>random/stochastic</span>{: style="color: purple"}.  
            __Objective View:__ "randomness"/"stochasticity" is described as a property of the actual quantity.  
            This generally does not hold: "randomness" cannot be a property of some standard examples, by simply asking two frequentists who are given different information about the same quantity to decide if its "random" (e.g. Bernoulli Urn).  
    <br>
    <br>


    |    | __Bayesian__ | __Frequentist__ |  
    | <span>_Uncertainty_</span>{: style="color: purple"}  | credible interval | confidence interval |  
    | <span>_Probability Interp._</span>{: style="color: purple"}  | Subjective: Degree of Belief (Logic) | Objective: Relative Frequency of Events |  
    | <span>_Uncertainty_</span>{: style="color: purple"}  | credible interval | confidence interval |  
    | <span>_estimation/inference_</span>{: style="color: purple"} | use data to best estimate unknown parameters | - pinpoint a value of parameter space as well as possible by using data to update belief<br>- all inference follow posterior<br>- use simulation method: generate samples from the posterior and use them to estimate the quantities of interest |  
    | <span>_parameter of the model_</span>{: style="color: purple"} | - Fixed, unknown Constants<br>- can NOT make probabilistic statements about the parameters | - Random Variables (parameters can’t be determined exactly, uncertainty is expressed in probability statements or distributions)<br>- can make probability statements about the parameters |  
    | <span>interval estimate</span>{: style="color: purple"} | Confidence Interval: a claim that the region covers the true parameter, reflecting uncertainty in sampling procedure. | Credible Interval: a claim that the true parameter is inside the region with measurable probability. |  
    | <span>Main Problem</span>{: style="color: purple"} | Variability of Data | Uncertainty of Knowledge |  




    __Probability Interpretation:__{: style="color: red"}  
    {: #lst-p}
    * __Bayesian__:  
        A Bayesian defines a "probability" in exactly the same way that most non-statisticians do - namely an indication of the plausibility of a proposition or a situation. If you ask him a question, he will give you a direct answer assigning probabilities describing the plausibilities of the possible outcomes for the particular situation (and state his prior assumptions).  
        <button>Interpretation Analysis</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        * Probability is Logic  
            my "non-plain english" reason for this is that the calculus of propositions is a special case of the calculus of probabilities, if we represent truth by 1 and falsehood by 0. Additionally, the calculus of probabilities can be derived from the calculus of propositions. This conforms with the "bayesian" reasoning most closely - although it also extends the bayesian reasoning in applications by providing principles to assign probabilities, in addition to principles to manipulate them. Of course, this leads to the follow up question "what is logic?" for me, the closest thing I could give as an answer to this question is "logic is the common sense judgements of a rational person, with a given set of assumptions" (what is a rational person? etc. etc.). Logic has all the same features that Bayesian reasoning has. For example, logic does not tell you what to assume or what is "absolutely true". It only tells you how the truth of one proposition is related to the truth of another one. You always have to supply a logical system with "axioms" for it to get started on the conclusions. They also has the same limitations in that you can get arbitrary results from contradictory axioms. But "axioms" are nothing but prior probabilities which have been set to 1. For me, to reject Bayesian reasoning is to reject logic. For if you accept logic, then because Bayesian reasoning "logically flows from logic" (how's that for plain english :P ), you must also accept Bayesian reasoning.  
        {: hidden=""}
    * __Frequentist__:  
        A Frequentist is someone that believes probabilities represent long run frequencies with which events occur; if needs be, he will invent a fictitious population from which your particular situation could be considered a random sample so that he can meaningfully talk about long run frequencies. If you ask him a question about a particular situation, he will not give a direct answer, but instead make a statement about this (possibly imaginary) population.  
        <button>Interpretation Analysis</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        * Probability is Frequency  
            although I'm not sure "frequency" is a plain english term in the way it is used here - perhaps "proportion" is a better word. I wanted to add into the frequentist answer that the probability of an event is thought to be a real, measurable (observable?) quantity, which exists independently of the person/object who is calculating it. But I couldn't do this in a "plain english" way.  
            So perhaps a "plain english" version of one the difference could be that frequentist reasoning is an attempt at reasoning from "absolute" probabilities, whereas bayesian reasoning is an attempt at reasoning from "relative" probabilities.  
        {: hidden=""}

    __Statistical Methods:__{: style="color: red"}  
    {: #lst-p}
    * __Bayesian__:  
        * Probability refers to degree of belief  
        * Inference about a parameter $$\theta$$ is by producing a probability distributions on it. 
            Typically, one starts with a prior distribution $$p(\theta)$$. One also chooses a likelihood function $$p(x \mid \theta)-$$ note this is a function of $$\theta$$, not $$x$$. After observing data $$x$$, one applies the Bayes Theorem to obtain the posterior distribution $$p(\theta \mid x)$$.  
            <p>$$p(\theta \mid x)=\frac{p(\theta) p(x \mid \theta)}{\int p\left(\theta^{\prime}\right) p\left(x \mid \theta^{\prime}\right) d \theta^{\prime}} \propto p(\theta) p(x \mid \theta)$$</p>  
            where $$Z \equiv \int p\left(\theta^{\prime}\right) p\left(x \mid \theta^{\prime}\right) d \theta^{\prime}$$ is known as the normalizing constant. The posterior distribution is a complete characterization of the parameter.  
            Sometimes, one uses the mode of the posterior as a simple point estimate, known as the __*maximum aposteriori* (MAP)__ estimate of the parameter:  
            $$\theta^{\text {MAP }}=\operatorname{argmax}_ {\theta} p(\theta \mid x)$$  
            > Note MAP is not a proper Bayesian approach.  
        * Prediction under an unknown parameter is done by integrating it out:  
            $$p(x \mid \text {Data})=\int p(x \mid \theta) p(\theta \mid \text{Data}) d \theta $$  
    * __Frequentist__: 
        * Probability refers to limiting relative frequency  
        * Data are random  
        * Estimators are random because they are functions of data  
        * Parameters are fixed, unknown constants not subject to probabilistic statements  
        * Procedures are subject to probabilistic statements, for example 95% confidence intervals traps the trueparameter value 95  




<!-- 4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}
5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}
6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents26}
7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents27}
8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents28} -->

***

<!-- ## THIRD
{: #content3}

1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}
2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}
3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}
4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents34}
5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents35}
6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents36}
7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents37}
8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents38}
 -->