---
layout: NotesPage
title: The Theory of Learning
permalink: /work_files/research/dl/theory/lern_prob
prevLink: /work_files/research/dl/nlp.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [The Learning Problem](#content1)
  {: .TOC1}
  * [The Feasibility of Learning](#content2)
  {: .TOC2}
  * [Error and Noise](#content3)
  {: .TOC3}
  * [The Learning Model I](#content4)
  {: .TOC4}
  * [The Learning Model II](#content5)
  {: .TOC5}
  * [The Bias Variance Decomposition](#content6)
  {: .TOC6}
</div>

***
***

[Lecture on Statistical Learning Theory from Risk perspective & Bayes Decision Rule](https://www.youtube.com/watch?v=rqJ8SrnmWu0&list=PLnZuxOufsXnvftwTB1HL6mel1V32w0ThI&index=4)  
[Learning Theory Andrew NG (CS229 Stanford)](https://www.youtube.com/watch?v=tojaGtMPo5U&list=PLA89DCFA6ADACE599&index=9)  
[Empirical Risk Minimization (Cornell)](https://www.youtube.com/watch?v=AkmPv2WEsHw)  


__Fundamental Problem of Machine Learning: It is *Ill-Posed*:__{: style="color: red"}  
Learning appears __impossible__: Learning a truly "unknown" function is __impossible__.  
<button>Show Discussion</button>{: .showText value="show" onclick="showTextPopHide(event);"}
![img](https://cdn.mathpix.com/snip/images/lgiqZ1ILbIe7TEciHCRsTgXrIfSDdrrpzvT078EloAI.original.fullsize.png){: width="100%" hidden=""}  
* __Solution: Work with a Restricted Hypothesis Space:__{: style="color: red"}  
    Either by <span>applying prior knowledge</span>{: style="color: purple"} or by <span>guessing</span>{: style="color: purple"}, we choose a space of hypotheses $$H$$ that is smaller than the space of all possible functions:  
    * simple conjunctive rules, linear functions, multivariate Gaussian joint probability distributions, etc.  

    * Lets say you have an unknown target function $$f: X \rightarrow Y$$ that you are trying to capture by learning. In order to capture the target function you have to come up with (__guess__) some hypotheses $$h_{1}, \ldots, h_{n}$$ where $$h \in H$$, and then __search__ through these hypotheses to select the best one that approximates the target function.   


__Two Views of Learning and their corresponding Strategies:__{: style="color: red"}  
{: #lst-p}
1. Learning is the _removal_ of our remaining __uncertainty__  
    – Suppose we knew that the unknown function was an m-of-n boolean function. Then we could use the training examples to deduce which function it is.  
    – Our prior "knowledge" might be wrong  
    * __Strategy__: Develop Languages for Expressing Prior Knowledge  
        Rule grammars, stochastic models, Bayesian networks  
2. Learning requires __guessing__ a good, small _hypothesis class_.  
    – We can start with a very small class and enlarge it until it contains an hypothesis that fits the data.  
    – Our guess of the hypothesis class could be wrong: The smaller the class, the more likely we are wrong.  
    * __Strategy__: Develop Flexible Hypothesis Spaces  
        Nested collections of hypotheses: decision trees, neural networks, cases, SVMs  


__Key Issues in Machine Learning:__{: style="color: red"}  
<button>List</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
* What are good hypothesis spaces?
    - which spaces have been useful in practical applications?  
* What algorithms can work with these spaces?
    - Are there general design principles for learning algorithms?  
* How can we optimize accuracy on future data points?
    - This is related to the problem of "overfitting"
* How can we have confidence in the results? (the __statistical__ question)
    - How much training data is required to find an accurate hypotheses?
* Are some learning problems computational intractable? (the __computational__ question)
* How can we formulate application problems as machine learning problems? (the __engineering__ question)    
{: hidden=""}


__A Framework for Hypothesis Spaces:__{: style="color: red"}  
{: #lst-p}
* __Size__: Does the hypothesis space have a __fixed size__ or a __variable size__?  
    * __Fixed-sized__ spaces are easier to understand, but variable-sized spaces are generally more useful.  
    * __Variable-sized__ spaces introduce the problem of __overfiting__.  
* __Stochasticity:__ Is the hypothesis a __classifier__, a __conditional distribution__, or a __joint distribution__?  
    This affects how we evaluate hypotheses.  
    * For a __deterministic__ hypothesis, a training example is either consistent (correctly predicted) or inconsistent (incorrectly predicted).  
    * For a __stochastic__ hypothesis, a training example is more likely or less likely.  
* __Parameterization:__ Is each hypothesis described by a set of __symbolic (discrete)__ choices or is it described by a set of __continuous__ parameters?  
    If both are required, we say the space has a __mixed__ parameterization.  
    * __Discrete parameters__ must be found by combinatorial search methods  
    * __Continuous parameters__ can be found by numerical search methods  
* <button>Hypothesis Spaces Diagram</button>{: .showText value="show" onclick="showTextPopHide(event);"}
![img](https://cdn.mathpix.com/snip/images/VFFJtf0S4AltKowR4d_7VR0v-ztBmt108ogBYAPDa5o.original.fullsize.png){: width="100%" hidden=""}  
    Note: __LTU__ == Linear Threshold Unit.  


__A Framework for Learning Algorithms:__{: style="color: red"}  
{: #lst-p}
* <button>Show Discussion</button>{: .showText value="show" onclick="showTextPopHide(event);"}
![img](https://cdn.mathpix.com/snip/images/jww-nPeIv3F0oytJ4PqraBXL49bL30kGCg4JwL1bi70.original.fullsize.png){: width="100%" hidden=""}  
* <button>Show Diagram</button>{: .showText value="show" onclick="showTextPopHide(event);"}
![img](https://cdn.mathpix.com/snip/images/y1wmxHjLNnaAzMg3rojdoNoid06vpgoVp1NMIlt6-sk.original.fullsize.png){: width="100%" hidden=""}  
* <button>Three Components of Learning Algorithms</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/qsm50cMRH8q1Sr5QTJWNWDf4kFrhGIZTZjvjWRlN0aw.original.fullsize.png){: width="100%" hidden=""}  



## The Learning Problem
{: #content1}

1. **When to use ML:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    When:  
    1. A pattern Exists
    2. We cannot pin the pattern down mathematically 
    3. We have Data  

    We usually can do without the first two. But the third condition we __CANNOT__ do without.  
    The Theory of Learning only depends on the data.  

    > "We have to have data. We are learning from data. So if someone knocks on my door with an interesting machine learning application, and they tell me how exciting it is, and how great the application would be, and how much money they would make, the first question I ask, __'what data do you have?'__. If you have data, we are in business. If you don't, you are _out of luck_." - Prof. Ng


2. **The ML Approach to Problem Solving:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    Consider the Netflix problem: _Predicting how a viewer will rate a movie_.   
    * __Direct Approach__:  
        ![img](/main_files/dl/theory/caltech/1.png){: width="40%"}  
        * Ask each user to give a rank/rate for the different "factors/features" (E.g. Action, Comedy, etc.)  
        * Watch each movie and assign a rank/rate for the same factors  
        * Match the factors and produce a __rating__  
    * __ML Approach__:  
        ![img](/main_files/dl/theory/caltech/2.png){: width="40%"}  
        Essentially it is a __Reversed__ approach  
        * Start with the __Ratings__ (dataset) that the users assigned to each movie  
        * Then _deduce_ the "factors/features" that are consistent with those Ratings  
            Note: we usually start with random initial numbers for the factors  
    <br>

3. **Components of Learning:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    * __Input__: $$\vec{x}$$  
    * __Output__: $$y$$ 
    * __Data__:  $${(\vec{x}_ 1, y_ 1), (\vec{x}_ 2, y_ 2), ..., (\vec{x}_ N, y_ N)}$$ 
    * __Target Function__: $$f : \mathcal{X} \rightarrow \mathcal{Y}$$  (Unknown/Unobserved)  
    * __Hypothesis__: $$g : \mathcal{X} \rightarrow \mathcal{Y}$$  
    <br>

5. **Components of the Solution:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  
    * __The Learning Model__:  
        * __The Hypothesis Set__:  $$\mathcal{H}=\{h\},  g \in \mathcal{H}$$  
            > E.g. Perceptron, SVM, FNNs, etc.  
        * __The Learning Algorithm__: picks $$g \approx f$$ from a hypothesis set $$\mathcal{H}$$  
            > E.g. Backprop, Quadratic Programming, etc.  

    Motivating the inclusion of a _Hypothesis Set_:  
    * __No Downsides__: There is __no loss of generality__ by including a hypothesis set, since any restrictions on the elements of the set have no effect on what the learning algorithms  
        Basically, there is no downside because from a practical POV thats what you do; by choosing an initial approach, e.g. SVM, Linear Regression, Neural Network, etc., we are already dictating a hypothesis set. If we don't choose one, then the hypothesis set has no restrictions and is the set of all possible hypothesis without loss of generalization.  
    * __Upside__: The hypothesis set plays a pivotal role in the _theory of learning_, by dictating whether we can learn or not.  
    <br>

6. **The Basic Premise/Goal of Learning:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}  
    "Using a set of observations to uncover an underlying process"  
    Rephrased mathematically, the __Goal of Learning__ is:   
    Use the Data to find a hypothesis $$g \in \mathcal{H}$$, from the hypothesis set $$\mathcal{H}=\{h\}$$, that _approximates_ $$f$$ well.  
    <br>

7. **Types of Learning:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}  
    * __Supervised Learning__: the task of learning a function that maps an input to an output based on example input-output pairs.  
        ![img](/main_files/dl/theory/caltech/4.png){: width="70%"}  
    * __Unsupervised Learning__: the task of making inferences, by learning a better representation, from some datapoints that do not have any labels associated with them.  
        ![img](/main_files/dl/theory/caltech/5.png){: width="70%"}  
        > Unsupervised Learning is another name for [Hebbian Learning](https://en.wikipedia.org/wiki/Hebbian_theory)
    * __Reinforcement Leaning__: the task of learning how software agents ought to take actions in an environment so as to maximize some notion of cumulative reward.  
        ![img](/main_files/dl/theory/caltech/6.png){: width="70%"}  
    <br>

8. **The Learning Diagram:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18}  
    ![img](/main_files/dl/theory/caltech/3.png){: width="70%"}  

***

## The Feasibility of Learning
{: #content2}

The Goal of this Section is to answer the question: Can we make any statements/inferences outside of the sample data that we have?  

1. **The Problem of Learning:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    Learning a truly __Unknown__ function is __Impossible__, since outside of the observed values, the function could assume _any value_ it wants.  

2. **The Bin Analogy - A Related Experiment::**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}  
    <button>Show Discussion</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    * ![img](/main_files/dl/theory/caltech/7.png){: width="70%"}  

        $$\mu$$ is a constant that describes the actual/real probability of picking the red marble.  
        $$\nu$$, however, is random and depends on the frequency of red marbles in the particular sample that you have collected.    

        Does $$\nu$$ approximate $$\mu$$?  
        * The short answer is __NO__:  
            The Sample an be mostly green while bin is mostly red.  
        * The Long answer is __YES__:  
            The Sample frequency $$\nu$$ is likely/probably close to bin frequency $$\mu$$.  
            > Think of a presidential poll of 3000 people that can predict how the larger $$10^8$$ mil. people will vote  

        The Main distinction between the two answers is in the difference between *__Possible__* VS *__Probable__*. 

        What does $$\nu$$ say about $$\mu$$?  
        In a big sample (Large $$N$$), $$\nu$$ is _probably_ close to $$\mu$$ (within $$\epsilon$$).   
        Formally, we the __Hoeffding's Inequality__:  
        <p>$$\mathbb{P}[|\nu-\mu|>\epsilon] \leq 2 e^{-2 \epsilon^{2} N}$$</p>  
        In other words, the probability that $$\nu$$ does not approximate $$\mu$$ well (they are not within an $$\epsilon$$ of each other), is bounded by a negative exponential that dampens fast but depends directly on the tolerance $$\epsilon$$.  
        > This reduces to the statement that "$$\mu = \nu$$" is PAC (PAC: Probably, Approximately Correct).    

        Properties:  
        * It is valid for $$N$$ and $$\epsilon$$. 
        * The bound does not depend on the value of $$\mu$$.  
        * There is a __Trade-off__ between the number of samples $$N$$ and the tolerance $$\epsilon$$.  
        * Saying that $$\nu \approx \mu \implies \mu \approx \nu$$, i.e. saying $$\nu$$ is approximately the same as $$\mu$$, implies that $$\mu$$ is approximately the same as $$\nu$$ (yes, tautology).   
            The logic here is subtle:  
            * Logically, the inequality is making a statement on $$\nu$$ (the random variable), it is saying that $$\nu$$ tends to be close to $$\mu$$ (the constant, real probability).  
            * However, since the inequality is symmetric, we are using the inequality to infer $$\mu$$ from $$\nu$$.  
                But that is not the cause and effect that actually takes place. $$\mu$$, actually, affects $$\nu$$.  

        Translating to the Learning Problem:  
        ![img](/main_files/dl/theory/caltech/8.png){: width="70%"}  
        > Notice how the meaning of the accordance between $$\mu$$ and $$\nu$$  is not accuracy of the model, but rather accuracy of the TEST.  

        Back to the Learning Diagram:  
        ![img](/main_files/dl/theory/caltech/9.png){: width="70%"}  
        The marbles in the bin correspond to the input space (datapoints). This adds a NEW COMPONENT to the Learning problem - the probability of generating the input datapoints (up to this point we treated learning in an absolute sense based on some fixed datapoints).   
        To adjust the statement of the learning problem to accommodate the new component:  
        we add a probability distribution $$P$$  over the input space $$\mathcal{X}$$. This, however, doesn't restrict the argument at all; we can invoke any probability on the space, and the machinery still holds. We, also, do not, even, need to know what $$P$$ is (even though $$P$$ affects $$\mu$$), since Hoeffding's Inequality allows us to bound the LHS with no dependence on $$\mu$$.  
        Thus, now we assume that the input datapoints $$\vec{x}_1, ..., \vec{x}_N$$ are assumed to be generated by $$P$$, __independently__.  
        So this is a very benign addition, that would give us high dividends - The Feasibility of Learning.    

        However, this is not learning; it is __Verification__. Learning involves using an algorithm to search a space $$\mathcal{H}$$  and try different functions $$h \in \mathcal{H}$$. Here, we have already picked some specific function and are testing its performance on a sample, using maths to guarantee the accuracy of the test within some threshold we are willing to tolerate.  


        Extending Hoeffding's Inequality to Multiple hypotheses $$h_i$$:  
        ![img](/main_files/dl/theory/caltech/10.png){: width="70%"}  
        ![img](/main_files/dl/theory/caltech/11.png){: width="70%"}  

        Putting the right notation:  
        ![img](/main_files/dl/theory/caltech/12.png){: width="70%"}  
        ![img](/main_files/dl/theory/caltech/13.png){: width="70%"}  

        <button>Why Hoeffding Inequality doesn't apply for multiple bins</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        ![img](/main_files/dl/theory/caltech/14.png){: hidden=""}  
        > i.e. the 10 heads are not a good indication of the real probability  
        
        <button>From coins to learning</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        ![img](/main_files/dl/theory/caltech/15.png){: hidden=""}  
        Equivalently, in learning, if the hypothesis set size is 1000, and there are 10 points we test against, the probability that one of those hypothesis performing well on the 10 points, but actually being a bad hypothesis is high, and increases with the hypothesis set size.  
        > Hoeffding's inequality has a guarantee for one experiment, that gets terribly diluted as you increase the number of experiments.  

        Solution:  
        We follow the very same reasoning: we want to know the probability of at least one failing. This can be bounded by the union bound, which intuitively says that the maximum probability of at least an event occurring in N is when all the events are independent, in which case you just sum up the probabilities:  
        <p>$$\begin{aligned} \mathbb{P}\left[ | E_{\text {in }}(g)-E_{\text {out }}(g) |>\epsilon\right] \leq \mathbb{P}[ & | E_{\text {in }}\left(h_{1}\right)-E_{\text {out }}\left(h_{1}\right) |>\epsilon \\ & \text {or } | E_{\text {in }}\left(h_{2}\right)-E_{\text {out }}\left(h_{2}\right) |>\epsilon \\ & \cdots \\ & \text {or } | E_{\text {in }}\left(h_{M}\right)-E_{\text {out }}\left(h_{M}\right) |>\epsilon ] \\ \leq & \sum_{m=1}^{M} \mathbb{P}\left[ | E_{\text {in }}\left(h_{m}\right)-E_{\text {out }}\left(h_{m}\right) |>\epsilon\right] \end{aligned}$$</p>  
        Which implies:  
        <p>$$\begin{aligned} \mathbb{P}\left[ | E_{\text {in }}(g)-E_{\text {out }}(g) |>\epsilon\right] & \leq \sum_{m=1}^{M} \mathbb{P}\left[ | E_{\text {in }}\left(h_{m}\right)-E_{\text {out }}\left(h_{m}\right) |>\epsilon\right] \\ & \leq \sum_{m=1}^{M} 2 e^{-2 \epsilon^{2} N} \end{aligned}$$</p>   
        Or,  
        <p>$$\mathbb{P}\left[ | E_{\ln }(g)-E_{\text {out }}(g) |>\epsilon\right] \leq 2 M e^{-2 \epsilon^{2} N}$$</p>  
        The more sophisticated the model you use, the looser that in-sample will track the out-of-sample. Because the probability of them deviating becomes bigger and bigger and bigger.  
        The conclusion may seem both awkward and obvious, but the bigger the hypothesis set, the higher the probability of at least one function being very bad. In the event that we have an infinite hypothesis set, of course this bound goes to infinity and tells us nothing new.  

        [References](http://testuggine.ninja/notes/feasibility-of-learning#fnref:limited)
    {: hidden=""}


3. **The Learning Analogy:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}  
    For an exam, the practice problems are the training set. You're going to look at the question. You're going to answer. You're going to compare it with the real answer. And then you are going to adjust your hypothesis, your understanding of the material, in order to do it better, and go through them and perhaps go through them again, until you get them right or mostly right or figure out the material (this makes you better at taking the exam).
    We don't give out the actual exams questions because __acing the final is NOT the goal__, the goal is to __learn the material (have a small $$E_{\text{out}}$$)__. The final exam is only a way of gauging how well you actually learned. And in order for it to gauge how well you actually learned, I have to give you the final at the point you have already fixed your hypothesis. You prepared. You studied. You discussed with people. You now sit down to take the final exam. So you have one hypothesis. And you go through the exam. hopefully, will reflect what your understanding will be outside.  
    > The exam measures $$E_{\text{in}}$$, and we know that it tracks $$E_{\text{out}}$$ (by Hoeffding), so it tracks well how you understand the material proper.  


<!-- 4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents26}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents27}
-->

8. **Notes:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents28}  
    * __Learning Feasibility__:  
        When learning we only deal with In-Sample Errors $$[E_{\text{in}}(\mathbf{w})]$$; we never handle the out-sample error explicitly; we take the theoretical guarantee that when you do well in-sample $$\implies$$ you do well out-sample (Generalization).  

***

## Error and Noise
{: #content3}

The Current Learning Diagram:  
![img](/main_files/dl/theory/caltech/16.png){: width="50%"}  

1. **Error Measures:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}  
    __Error Measures__ aim to answer the question:  
    "What does it mean for $$h$$ to approximate $$f$$ ($$h \approx f$$)?"  
    The __Error Measure__: $$E(h, f)$$  
    It is almost always defined point-wise: $$\mathrm{e}(h(\mathbf{X}), f(\mathbf{X}))$$.  
    Examples:  
    * __Square Error__:  $$\:\:\:\mathrm{e}(h(\mathbf{x}), f(\mathbf{x}))=(h(\mathbf{x})-f(\mathbf{x}))^{2}$$  
    * __Binary Error__:  $$\:\:\:\mathrm{e}(h(\mathbf{x}), f(\mathbf{x}))=[h(\mathbf{x}) \neq f(\mathbf{x})]$$  (1 if true else 0)  

    The __overall error__ $$E(h,f) = $$ _average_ of pointwise errors $$\mathrm{e}(h(\mathbf{x}), f(\mathbf{x}))$$:  
    * __In-Sample Error__:  
        <p>$$E_{\mathrm{in}}(h)=\frac{1}{N} \sum_{n=1}^{N} \mathrm{e}\left(h\left(\mathbf{x}_{n}\right), f\left(\mathbf{x}_{n}\right)\right)$$</p>    
    * __Out-Sample Error__:  
        <p>$$E_{\text {out }}(h)=\mathbb{E}_ {\mathbf{x}}[\mathrm{e}(h(\mathbf{x}), f(\mathbf{x}))]$$</p>  

2. **The Learning Diagram - with pointwise error:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}  
    ![img](/main_files/dl/theory/caltech/17.png){: width="50%"}  
    There are two additions to the diagram:  
    * The first is to realize that we are defining the error measure __on a point__. 
    * Another is that in deciding whether $$g$$  is close to $$f$$ , which is the goal of learning, we test this with a point $$x$$. And the criterion for deciding whether $$g(x)$$ is approximately the same as $$f(x)$$ is our pointwise error measure.  

3. **Defining the Error Measure:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}  

    __Types:__  
    * False Positive
    * False Negative  

    There is no inherent merit to choosing one error function over another. It's not an analytic question. It's an application-domain question.  
    <button>Examples - Supermarket</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](/main_files/dl/theory/caltech/18.png){: hidden=""}  
    <button>Examples - CIA</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](/main_files/dl/theory/caltech/19.png){: hidden=""}  

    The error measure should be _specified by the user_. Since, that's not always possible, the alternatives:  
    * __Plausible Measures__: measures that have an _analytic argument_ for their merit, based on certain _assumptions_.  
        E.g. _Squared Error_ comes from the _Gaussian Noise_ Assumption.  
    * __Friendly Measures__: An _easy-to-use_ error measure, without much justification.  
        E.g. Linear Regression error leads to the easy closed-form solution, Convex Error measures are easy to optimize, etc.  
                  

4. **The Learning Diagram - with the Error Measure:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents34}  
    ![img](/main_files/dl/theory/caltech/20.png){: width="50%"}  
    The __Error Measure__ provides a quantitative assessment of the statement $$g(\mathbf{x}) \approx f(\mathbf{x})$$.  


5. **Noisy Targets:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents35}  
    The _'Target Function'_ is not always a _function_ because two _'identical'_ input points can be mapped to two different outputs (i.e. they have different labels).  

    The solution: Replacing the target function with a __Target Distribution__.  
    Instead of $$y = f(x)$$ we use the  _conditional target distribution_: $$P(y | \mathbf{x})$$. What changes now  is that, instead of $$y$$  being deterministic of $$\mathbf{x}$$, once you generate $$\mathbf{x}$$, $$y$$  is also probabilistic-- generated by $$P(y | \mathbf{x})$$.  
    $$(\mathbf{x}, y)$$ is now generated by the __joint distribution__:  
    <p>$$P(\mathbf{x}) P(y | \mathbf{x})$$</p>  

    Equivalently, we can define a __Noisy Target__ as a _deterministic (target) function_ $$\:f(\mathbf{x})=\mathbb{E}(y | \mathbf{x})\:$$  PLUS _Noise_ $$\: y-f(x)$$.     
    This can be done WLOG since a _deterministic target_ is a special kind of a _noisy target_:  
    Define $$P(y \vert \mathbf{x})$$ to be identically Zero, except for $$y = f(x)$$.   


6. **The Learning Diagram - with the Noisy Target:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents36}  
    ![img](/main_files/dl/theory/caltech/21.png){: width="50%"}  

    Now, $$E_{\text {out}}(h) = \mathbb{E}_ {x, y}[e(h(x), y)]$$ instead of $$\mathbb{E}_ {\mathbf{x}}[\mathrm{e}(h(\mathbf{x}), f(\mathbf{x}))]$$, and  
    $$\left(\mathbf{x}_{1}, y_{1}\right), \cdots,\left(\mathbf{x}_{N}, y_{N}\right)$$ are generated independently of each (each tuple).  


7. **Distinction between $$P(y | \mathbf{x})$$ and $$P(\mathbf{x})$$:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents37}  
    The __Target Distribution__ $$P(y \vert \mathbf{x})$$ is what we are *__trying to learn__*.  
    The __Input Distribution__ $$P(\mathbf{x})$$, only, *__quantifies relative importance__*  of $$\mathbf{x}$$; we are __NOT__ trying to learn this distribution.  
    > Rephrasing: Supervised learning only learns $$P(y \vert \mathbf{x})$$ and not $$P(\mathbf{x})$$; $$P(\mathbf{x}, y)$$ is __NOT__ a target distribution for Supervised Learning.  

    Merging $$P(\mathbf{x})P(y \vert \mathbf{x})$$ as $$P(\mathbf{x}, y)$$, although allows us to generate examples $$(\mathbf{x}, y)$$, mixes the two concepts that are inherently different.  


8. **Preamble to Learning Theory:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents38}  
    __Generalization VS Learning:__  
    We know that _Learning is Feasible_.
    * __Generalization__:  
        It is likely that the following condition holds:  
        <p>$$\: E_{\text {out }}(g) \approx E_{\text {in }}(g)  \tag{3.1}$$</p>  
        This is equivalent to "good" __Generalization__.  
    * __Learning__:  
        Learning corresponds to the condition that $$g \approx f$$, which in-turn corresponds to the condition:  
        <p>$$E_{\text {out }}(g) \approx 0  \tag{3.2}$$</p>      


    __How to achieve Learning:__{: style="color: red"}    
    We achieve $$E_{\text {out }}(g) \approx 0$$ through:  
    {: #lst-p}
    1. $$E_{\mathrm{out}}(g) \approx E_{\mathrm{in}}(g)$$  
        A __theoretical__ result achieved through Hoeffding __PROBABILITY THEORY__{: style="color: red"}  .   
    2. $$E_{\mathrm{in}}(g) \approx 0$$  
        A __Practical__ result of minimizing the In-Sample Error Function (ERM) __Optimization__{: style="color: red"}  .  

    Learning is, thus, reduced to the 2 following questions:  
    {: #lst-p}
    1. Can we make sure that $$E_{\text {out }}(g)$$ is close enough to $$E_{\text {in }}(g)$$? (theoretical)  
    2. Can we make $$E_{\text {in}}(g)$$ small enough? (practical)  


    What the Learning Theory will achieve:  
    {: #lst-p}
    * Characterizing the _feasibility of learning_ for __infinite $$M$$__ (hypothesis).  
        We are going to measure the model not by the number of hypotheses, but by a single parameter which tells us the sophistication of the model. And that sophistication will reflect the out-of-sample performance as it relates to the in-sample performance (through the Hoeffding (then VC) inequalities).   
    * Characterizing the tradeoff:  
        ![img](/main_files/dl/theory/caltech/22.png){: width="50%"}   
        In words:  
        We realized that we would like our model, the hypothesis set, to be elaborate, in order to be able to fit the data. The more parameters you have, the more likely you are going to fit the data and get here. So the $$E_{\text{in}}$$ goes down if you use more complex models. However, if you make the model more complex, the discrepancy between $$E_{\text{out}}$$ and $$E_{\text{in}}$$ gets worse and worse. $$E_{\text{in}}$$ tracks $$E_{\text{out}}$$ much more loosely than it used to.  




## Linear Models I
{: #content4}

![img](/main_files/dl/theory/caltech/3.jpg){: width="100%"}    

![img](/main_files/dl/theory/caltech/4.jpg){: width="100%"}    

* __[Interpreting Linear Classifiers (cs231n)](https://cs231n.github.io/linear-classify/#interpret)__  


    * [**Linear Classifiers Demo (cs231n)**](http://vision.stanford.edu/teaching/cs231n-demos/linear-classify/){: value="show" onclick="iframePopA(event)"}
    <a href="http://vision.stanford.edu/teaching/cs231n-demos/linear-classify/"></a>
        <div markdown="1"> </div>  
    * [Linear Regression from Conditional Distribution (gd example)](https://stats.stackexchange.com/questions/407812/derive-linear-regression-model-from-the-conditional-distribution-of-yx)  
    * [__Linear Regression Probabilistic Development__](http://bjlkeng.github.io/posts/a-probabilistic-view-of-regression/)  
    * In a linear model, if the errors belong to a normal distribution the least squares estimators are also the maximum likelihood estimators.[^1]  
            

[^1]: [Reference: Equivalence of Generalized-LS and MLE in Exponential Family](https://www.researchgate.net/publication/254284684_The_Equivalence_of_Generalized_Least_Squares_and_Maximum_Likelihood_Estimates_in_the_Exponential_Family)  
    



<!-- ***

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents42}

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents43}

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents44}

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents45}

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents46}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents47}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents48}

*** -->

## The Linear Model II
{: #content5}

* [Logistic Regression vs LDA? (ESL)](https://web.stanford.edu/~hastie/Papers/ESLII.pdf#page=146)  
* [Derivation of Logistic Regression](http://www.haija.org/derivation_logistic_regression.pdf)  
* [The Simpler Derivation of Logistic Regression](http://www.win-vector.com/blog/2011/09/the-simpler-derivation-of-logistic-regression/)  
* [Logistic Regression, Generalized Linear and Additive Models (CMU)](http://www.stat.cmu.edu/~cshalizi/uADA/12/lectures/ch12.pdf)  
* [Why do we use the Bernoulli distribution in the logistic regression model? (Quora)](https://www.quora.com/Why-do-we-use-the-Bernoulli-distribution-in-the-logistic-regression-model)  
* [Logistic Regression - ML Cheatsheet](https://ml-cheatsheet.readthedocs.io/en/latest/logistic_regression.html)  
* [Logistic Regression - CS Cheatsheet](https://cs-cheatsheet.readthedocs.io/en/latest/subjects/machine_learning/logistic_regression.html)  
* [Logistic Regression (Lec Ng)](https://www.youtube.com/watch?v=hjrYrynGWGA&list=PLkDaE6sCZn6Ec-XTbcX1uRg2_u4xOEky0&index=9)  



1. **Linear Models - Logistic Regression:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents51}  
    ![img](/main_files/dl/theory/caltech/25.png){: width="80%"}   
    The __Logistic Regression__ applies a _non-linear transform_  on the _signal_; it's a softer approximation to the hard-threshold non-linearity applied by _Linear Classification_.  


2. **The Logistic Function $$\theta$$:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents52}  
    <p>$$\theta(s)=\frac{e^{s}}{1+e^{s}}=\frac{1}{1+e^{-s}}$$</p>  

    ![img](/main_files/dl/theory/caltech/26.png){: width="80%"}   
    * __Soft Threshold__: corresponds to uncertainty; interpreted as probabilities.  
    * __Sigmoid__: looks like a flattened out 'S'.  
        

3. **The Probability Interpretation:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents53}  
    $$h(\mathbf{x})=\theta(s)$$ is interpreted as a probability.  
    It is in-fact a __Genuine Probability__. The output of logistic regression is treated genuinely as a probability even during learning.  
    Justification:  
    Data $$(\mathbf{x}, y)$$ with binary $$y$$, (we don't have direct access to probability, but the binary $$y$$ is affected by the probability), generated by a noisy target:  
    <p>$$P(y | \mathbf{x})=\left\{\begin{array}{ll}{f(\mathbf{x})} & {\text {for } y=+1} \\ {1-f(\mathbf{x})} & {\text {for } y=-1}\end{array}\right.$$</p>  
    The target $$f : \mathbb{R}^{d} \rightarrow[0,1]$$ is the probability.  
    We learn $$\:\:\:\: g(\mathbf{x})=\theta\left(\mathbf{w}^{\top} \mathbf{x}\right) \approx f(\mathbf{x})$$.   
    > In words: So I'm going to call the probability the target function itself. The probability that someone gets heart attack is $$f(\mathbf{x})$$. And I'm trying to learn $$f$$, notwithstanding the fact that the examples that I am getting are giving me just sample values of $$y$$, that happen to be generated by $$f$$.  

    <button>Further Analysis</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
    * Logistic Regression uses the __sigmoid__ function to "squash" the output feature/signal into the $$[0, 1]$$ space.  
        Although, one could interpret the _sigmoid classifier_ as just a function with $$[0,1]$$ range, it is actually, a __Genuine Probability__.  
    * To see this:  
        * A labeled, classification Data-Set, does __NOT__ (explicitly) give you the _probability_ that something is going to happen, rather, just the fact that an event either happened $$(y=1)$$ or that it did not $$(y=0)$$, without the actual probability of that event happening.  
        * One can think of this data as being generated by a (the following) noisy target:  
            $${\displaystyle P(y \vert x) ={\begin{cases}f(x)&{\text{for }}y = +1,\\1-f(x)&{\text{for }}y=-1.\\\end{cases}}}$$   
        * They have the form that a certain probability that the event occurred and a certain probability that the event did NOT occur, given their input-data.  
        * This is generated by the target we want to learn; thus, the function $$f(x)$$ is the target function to approximate.  
    * In Logistic Regression, we are trying to learn $$f(x)$$ not withstanding the fact that the data-points we are learning from are giving us just sample values of $$y$$ that happen to be generated by $$f$$.  
    * Thus, the __Target__ $$f : \mathbb{R}^d \longrightarrow [0,1]$$ is the probability.  
        <span>The output of Logistic Regression is treated genuinely as a __probability__ even _during **Learning**_.</span>{: style="color: purple"}   
    {: hidden=""}
    <br>

4. **Deriving the Error Measure (Cross-Entropy) from Likelihood:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents54}  
    The error measure for logistic regression is based on __likelihood__ - it is both, plausible and friendly/well-behaved? (for optimization).  
    For each $$(\mathbf{x}, y)$$, $$y$$ is generated wit probability $$f(\mathbf{x})$$.  

    __Likelihood__: We are maximizing the *__likelihood of this hypothesis__*, under the *__data set__* that we were given, with respect to the *__weights__*. I.E. Given the data set, how likely is this hypothesis? Which means, what is the probability of that data set under the assumption that this hypothesis is indeed the target?  

    * __Deriving the Likelihood:__   
        1. We start with:  
            <p>$$P(y | \mathbf{x})=\left\{\begin{array}{ll}{h(\mathbf{x})} & {\text {for } y=+1} \\ {1-h(\mathbf{x})} & {\text {for } y=-1}\end{array}\right.$$</p>  
        2. Substitute $$h(\mathbf{x})=\theta \left(\mathbf{w}^{\top} \mathbf{x}\right)$$:  
            <p>$$P(y | \mathbf{x})=\left\{\begin{array}{ll}{\theta(\mathbf{w}^T\mathbf{x})} & {\text {for } y=+1} \\ {1-\theta(\mathbf{w}^T\mathbf{x})} & {\text {for } y=-1}\end{array}\right.$$</p>  
        3. Since we know that $$\theta(-s)=1-\theta(s)$$, we can simplify the piece-wise function:  
            <p>$$P(y | \mathbf{x})=\theta\left(y \mathbf{w}^{\top} \mathbf{x}\right)$$</p>  
        4. To get the __likelihood__ of the dataset $$\mathcal{D}=\left(\mathbf{x}_{1}, y_{1}\right), \ldots,\left(\mathbf{x}_{N}, y_{N}\right)$$:  
            <p>$$\prod_{n=1}^{N} P\left(y_{n} | \mathbf{x}_{n}\right) =\prod_{n=1}^{N} \theta\left(y_{n} \mathbf{w}^{\mathrm{T}} \mathbf{x}_ {n}\right)$$</p>  

    * __Maximizing the Likelihood (Deriving the Cross-Entropy Error):__  
        1. Maximize:  
            <p>$$\prod_{n=1}^{N} \theta\left(y_{n} \mathbf{w}^{\top} \mathbf{x}_ {n}\right)$$</p>  
        2. Take the natural log to avoid products:  
            <p>$$\ln \left(\prod_{n=1}^{N} \theta\left(y_{n} \mathbf{w}^{\top} \mathbf{x}_ {n}\right)\right)$$</p>  
            Motivation:  
            * The inner quantity is __non-negative__ and non-zero.  
            * The natural log is __monotonically increasing__ (its max, is the max of its argument)  
        3. Take the average (still monotonic):  
            <p>$$\frac{1}{N} \ln \left(\prod_{n=1}^{N} \theta\left(y_{n} \mathbf{w}^{\top} \mathbf{x}_ {n}\right)\right)$$</p>  
        4. Take the negative and __Minimize__:  
            <p>$$-\frac{1}{N} \ln \left(\prod_{n=1}^{N} \theta\left(y_{n} \mathbf{w}^{\top} \mathbf{x}_ {n}\right)\right)$$</p>  
        5. Simplify:  
            <p>$$=\frac{1}{N} \sum_{n=1}^{N} \ln \left(\frac{1}{\theta\left(y_{n} \mathbf{w}^{\tau} \mathbf{x}_ {n}\right)}\right)$$</p>  
        6. Substitute $$\left[\theta(s)=\frac{1}{1+e^{-s}}\right]$$:  
            <p>$$\frac{1}{N} \sum_{n=1}^{N} \underbrace{\ln \left(1+e^{-y_{n} \mathbf{w}^{\top} \mathbf{x}_{n}}\right)}_{e\left(h\left(\mathbf{x}_{n}\right), y_{n}\right)}$$</p>  
        7. Use this as the *__Cross-Entropy__*  __Error Measure__:  
            <p>$$E_{\mathrm{in}}(\mathrm{w})=\frac{1}{N} \sum_{n=1}^{N} \underbrace{\ln \left(1+e^{-y_{n} \mathrm{w}^{\top} \mathbf{x}_{n}}\right)}_{\mathrm{e}\left(h\left(\mathrm{x}_{n}\right), y_{n}\right)}$$</p>  


6. **The Decision Boundary of Logistic Regression:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents56}  
    __Decision Boundary:__ It is the set of $$x$$ such that:  
    <p>$$\frac{1}{1+e^{-\theta \cdot x}}=0.5 \implies 0=-\theta \cdot x=-\sum_{i=0}^{n} \theta_{i} x_{i}$$</p>  


7. **The Logistic Regression Algorithm:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents57}  
    ![img](/main_files/dl/theory/caltech/27.png){: width="80%"}    

8. **Summary of Linear Models:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents58}  
    ![img](/main_files/dl/theory/caltech/26.png){: width="80%"}    

9. **Nonlinear Transforms:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents59}  
    <p>$$\mathbf{x}=\left(x_{0}, x_{1}, \cdots, x_{d}\right) \stackrel{\Phi}{\longrightarrow} \mathbf{z}=\left(z_{0}, z_{1}, \cdots \cdots \cdots \cdots \cdots, z_{\tilde{d}}\right)$$</p>  
    <p>$$\text {Each } z_{i}=\phi_{i}(\mathbf{x}) \:\:\:\:\: \mathbf{z}=\Phi(\mathbf{x})$$</p>  
    Example: $$\mathbf{z}=\left(1, x_{1}, x_{2}, x_{1} x_{2}, x_{1}^{2}, x_{2}^{2}\right)$$  
    The Final Hypothesis $$g(\mathbf{x})$$ in $$\mathcal{X}$$ space:  
    * __Classification:__ $$\operatorname{sign}\left(\tilde{\mathbf{w}}^{\top} \Phi(\mathbf{x})\right)$$ 
    * __Regression:__ $$\tilde{\mathbf{w}}^{\top} \Phi(\mathbf{x})$$  

    __Two Non-Separable Cases:__{: style="color: red"}  
    * Almost separable with some outliers:  
        ![img](/main_files/dl/theory/caltech/23.png){: width="38%"}   
        1. Accept that $$E_{\mathrm{in}}>0$$; use a linear model in $$\mathcal{X}$$.    
        2. Insist on $$E_{\mathrm{in}}=0$$; go to a high-dimensional $$\mathcal{Z}$$.  
            This has a __worse__ chance for generalizing. 
    * Completely Non-Linear:  
        ![img](/main_files/dl/theory/caltech/24.png){: width="38%"}   
        Data-snooping example: it is hard to choose the right transformations; biggest flop is to look at the data to choose the right transformations; it invalidates the VC inequality guarantee.  
        > Think of the VC inequality as providing you with a warranty.   

<!-- 5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents55} -->

## The Bias Variance Decomposition
{: #content6}

![img](/main_files/dl/theory/caltech/1.jpg){: width="100%"}    

![img](/main_files/dl/theory/caltech/2.jpg){: width="100%"}    


