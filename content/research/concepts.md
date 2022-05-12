---
layout: NotesPage
title: Concepts
permalink: /concepts_
prevLink: /
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [CNNs](#content1)
  {: .TOC1}
  * [RNNs](#content2)
  {: .TOC2}
  * [Math](#content3)
  {: .TOC3}
  * [Statistics and Probability Theory](#content4)
  {: .TOC4}
  * [Optimization](#content5)
  {: .TOC5}
  * [Machine Learning](#content6)
  {: .TOC6}
  * [Computer Vision](#content7)
  {: .TOC7}
  * [NLP](#content8)
  {: .TOC8}
  * [Physics](#content9)
  {: .TOC9}
  * [Algorithms](#content10)
  {: .TOC10}
  * [Misc.](#content11)
  {: .TOC11}
  * [Game Theory](#content12)
  {: .TOC12}
</div>

***
***

* [Interactive ML Demos (Blog)](https://arogozhnikov.github.io/2016/04/28/demonstrations-for-ml-courses.html)  


<button>The Scientific Method as an Ongoing Process</button>{: .showText value="show" onclick="showTextPopHide(event);"}
![img](https://cdn.mathpix.com/snip/images/XCvcfM_6eAB3B5pXgL2IZTyO1FkhciXiaVCcQBjsiAc.original.fullsize.png){: width="100%" hidden=""}  



__PyTorch:__{: style="color: red"}  
<button>Packages</button>{: .showText value="show" onclick="showTextPopHide(event);"}
![img](https://cdn.mathpix.com/snip/images/dq-w7AFpBfdXveRL3uGmnerIGtfIPyeJFRfj2o97XSU.original.fullsize.png){: width="100%" hidden=""}  
CNN Tensor Shape: $$[B, C, H, W]$$  


## CNNs
{: #content1}

<!-- 1. **:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}   -->

<!-- 2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
-->

<!-- __Notes:__   -->
<!-- * __Structured Convolutions__:  
    __Why?__  
    Language has structure, would like it to localize features.  
    > e.g. noun-verb pairs very informative, but not captured by normal CNNs  
 -->        

***
***

## RNNs
{: #content2}


<!-- 1. **RNN Architectures:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}   -->
<!-- 2. **Different Connections in RNN Architectures:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}   -->


3. **Modeling Sequences - Memory as a model property:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}  
    <button>Show Content</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    * Everything:  
        __Memoryless Models for Sequences:__{: style="color: red"}  
        {: #lst-p}
        * __Autoregressive Models:__  
            Predict the next term in a sequence from a fixed number of previous terms using _"delay taps"_.  
            > It tries to predict the next term, _basically as a weighted average_ (if model is linear) of the previous terms.  

            ![img](/main_files/concepts/11.png){: width="50%"}  
        * __Feed-Forward Neural Nets__:  
            Generalize Auto-regressive models by using one or more layers of non-linear hidden units e.g. Bengio's first LM.  
            ![img](/main_files/concepts/12.png){: width="50%"}  

        __Beyond Memoryless Models:__{: style="color: red"}  
        {: #lst-p}
        If we give our generative models some _hidden state_, and if we give this hidden state its own internal dynamics, we get a much more interesting kind of model.  
        > The hidden state produces _observations_ that we get to _"observe/see"_  

        * It can __store information__ in its _hidden state_ for a long time.  
        * If the dynamics is noisy and the way it generates outputs from its hidden state is noisy, (by observing the outputs of the model) we can never know its exact hidden state.  
            * The best we can do is to infer a probability distribution over the space of hidden state vectors.  
        * This __inference__ (of the hidden states by observing the outputs of the model) is only __tractable__ for _TWO_ types of hidden-state models:  
            1. __Linear Dynamical Systems (LDS) (loved by Engineers):__  
                * These are generative models. They have a real-valued hidden state that cannot be observed directly.
                    * The hidden state has linear dynamics with Gaussian noise and produces the observations using a linear model with Gaussian noise.
                    * There may also be driving inputs.
                * To predict the next output (so that we can shoot down the missile) we need to infer the hidden state.
                    * A linearly transformed Gaussian is a Gaussian. So the distribution over the hidden state given the data/observations so far is Gaussian (because all the noise in a LDS is Gaussian). It can be computed using _"Kalman filtering"_.
                ![img](/main_files/concepts/13.png){: width="35%"}  
            2. __Hidden Markov Models (HMMs) (loved by computer scientists):__  
                * Hidden Markov Models have a __discrete one-of-N__ hidden state distributions (rather than _Gaussian_ distributions). Transitions between states are stochastic and controlled by a transition matrix. The outputs produced by a state are stochastic. 
                    * We cannot be sure which state produced a given output (because the outputs produced by a state are stochastic). So the state is "hidden" (behind this _"probabilistic veil"_).  
                    * It is easy to represent a probability distribution across N states with N numbers.  
                        So, even tho we cant know what state it is in for sure, we can easily represent the probability distribution
                * To predict the next output we need to infer the probability distribution over hidden states. 
                    * HMMs have efficient algorithms for inference and learning (dynamic programming).  
                ![img](/main_files/concepts/14.png){: width="35%"}  
                * __A Fundamental Limitation of HMMs__:  
                    * Consider what happens when a hidden Markov model generates data
                        * At each time step it must select one of its hidden states. So with $$N$$ hidden states it can only remember $$\log(N)$$ bits about what it generated so far.
                    * Consider the information that the first half of an utterance contains about the second half:  
                        > This is the amount of info that the HMM needs to convey to the second half of an utterance it produces from the first half (having produced the first half)  

                        * The syntax needs to fit (e.g. number and tense agreement)
                        * The semantics needs to fit. The intonation needs to fit.
                        * The accent, rate, volume, and vocal tract characteristics must all fit.
                    * All these aspects combined could be $$100$$ bits of information that the first half of an utterance needs to convey to the second half. Thus, needing about $$2^100$$ hidden states to _"remember/store"_ that information.   $$2^100$$ is big!

        __Recurrent Neural Networks (RNNs):__{: style="color: red"}  
        {: #lst-p}
        * RNNs are very powerful, because they combine two properties:
            * Distributed hidden state that allows them to store a lot of information about the past efficiently.  
                > i.e. several different units can be active at once (unlike HMMs), so they can remember several different things at once.  

            * Non-linear dynamics that allows them to update their hidden state in complicated ways (unlike LDSs).  
        * With enough neurons and time, RNNs can compute anything that can be computed by your computer.  
        ![img](/main_files/concepts/15.png){: width="15%"}  

        * [Visualizing memorization in RNNs](https://distill.pub/2019/memorization-in-rnns/)  

        __Do generative models need to be stochastic?__  
        * Linear dynamical systems and HMMs are stochastic models.  
            The dynamics and the production of observations from the underlying state both involve __intrinsic noise__.  
            
            * But the __posterior probability distribution__ over their hidden states given the observed  data so far is a _**deterministic** function of the data_.    
        <br>    
        * Recurrent neural networks are deterministic.
            * So think of the hidden state of an RNN as the equivalent of the __deterministic probability distribution over hidden states__ in a linear dynamical system or hidden Markov model.  

        __What kinds of behavior can RNNs exhibit?__
        * They can oscillate. Good for motor control? (e.g. walking needs varying _stride_)  
        * They can settle to point attractors. Good for retrieving memories?  
            > By having the target point-attractors (to settle in) be the memories you want to retrieve.  

        * They can behave chaotically. Bad for information processing?
        * RNNs could potentially learn to implement lots of small programs (using different subsets of their hidden state) that each capture a nugget of knowledge and run in parallel, interacting to produce very complicated effects.
        * But the computational power of RNNs makes them very hard to train
            * For many years we could not exploit the computational power of RNNs despite some heroic efforts (e.g. Tony Robinson’s speech recognizer)  


        __Notes:__{: style="color: red"}  
        {: #lst-p}
        * __A Content-Addressable Memory__: an item can be accessed by just knowing part of its content.
    {: hidden=""}        

    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * [Associative LSTMs (Paper)](https://arxiv.org/pdf/1602.03032.pdf)  
    <br>            


4. **Stability - Vanishing and Exploding Gradients:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}  
    <!-- 
        5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}
        6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents26}
        7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents27}
        8. **Notes:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents28}           
    -->
            

***
***

## Maths
{: #content3}

1. **Metrics and Quasi-Metrics:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}  
    <button>Show Content</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    * content:  
        A __Metric (distance function)__ $$d$$  is a function that defines a distance between each pair of elements of a set $$X$$.  
        A Metric induces a _topology_ on a set; BUT, not all topologies can be generated by a metric.  
        Mathematically, it is a function:  
        $${\displaystyle d:X\times X\to [0,\infty )},$$  
        that must satisfy the following properties:  
        1.  $${\displaystyle d(x,y)\geq 0}$$ $$\:\:\:\:\:\:\:$$   non-negativity or separation axiom  
        2.  $${\displaystyle d(x,y)=0\Leftrightarrow x=y}$$ $$\:\:\:\:\:\:\:$$  identity of indiscernibles  
        3.  $${\displaystyle d(x,y)=d(y,x)}$$ $$\:\:\:\:\:\:\:$$  symmetry  
        4.  $${\displaystyle d(x,z)\leq d(x,y)+d(y,z)}$$ $$\:\:\:\:\:\:\:$$  subadditivity or triangle inequality  
        > The first condition is implied by the others.  

        <button>Examples</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}  
        ![img](/main_files/concepts/10.png){: width="100%" hidden=""}  
        A __Quasi-Metric__ is a metric that lacks the _symmetry_ property.  
        One can form a Metric function $$d'$$  from a Quasi-metric function $$d$$ by taking:  
        $$d'(x, y) = ​1⁄2(d(x, y) + d(y, x))$$  
    {: hidden=""}

2. **Binary Relations (abstract algebra):**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}  
    <button>Show Content</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    * content:  
        A __binary relation__ on a set $$A$$ is a set of ordered pairs of elements of $$A$$. In other words, it is a subset of the Cartesian product $$A^2 = A ×A$$.    
        The number of binary relations on a set of $$N$$ elements is $$= 2^{N^2}$$  

        __Examples:__    
        {: #lst-p}
        * "is greater than"  
        * "is equal to"  
        * A function $$f(x)$$  

        __Properties:__  (for a relation $$R$$ and set $$X$$)    
        {: #lst-p}
        * _Reflexive:_ for all $$x$$ in $$X$$ it holds that $$xRx$$  
        * _Symmetric:_ for all $$x$$ and $$y$$ in $$X$$ it holds that if $$xRy$$ then $$yRx$$  
        * _Transitive:_ for all $$x$$, $$y$$ and $$z$$ in $$X$$ it holds that if $$xRy$$ and $$yRz$$ then $$xRz$$  
        An __Equivalence Relation__ has all of the above properties.    
    {: hidden=""}


3. **Set Theory:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}  
    {: #lst-p}
    * __Number of subsets of a set of $$N$$ elements__ $$= 2^N$$  
    * __Number of pairs (e.g. $$(a,b)$$) of a set of $$N$$ elements__ $$= N^2$$  
        e.g. $$\mathbb{R} \times \mathbb{R} = \mathbb{R}^2$$  


4. **Proof Methods:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents34}  
    <button>Show List</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    * Direct Proof
    * Mathematical Induction
        * Strong Induction
        * Infinite Descent
    * Contradiction
    * Contraposition ($$(p \implies q) \iff (!q \implies !p)$$)  
    * Construction
    * Combinatorial
    * Exhaustion
    * Non-Constructive proof (existence proofs)
    {: hidden=""}

5. **Mathematical Concepts - The Map of Mathematics:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents35}  
    <button>Show Text</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    * __Real Analysis__:  
        The Real line begets Real Analysis. It's the study of real numbers and continuous functions on the reals. You have a concrete object (real numbers) and a concrete distance measure (the absolute value function) which is needed for the notions of convergence and continuity.  
    * __Metric Spaces__:  
        Less concrete than Real Analysis. You have a numerical way of explaining proximity by a distance measure, and you have a similar way of explaining convergence and continuity. Functional Analysis lies in the middle of those two.   
    * __Topology__:  
        Studies topological spaces, WHERE, everything is up for grabs. The proximity measure is no longer numerical. The proximity "measure" around a point is a poset-like at best. This makes the notions of convergence and continuity more tricky.  
    * __Functional Analysis__:  
        Can be thought of as a generalization of Linear Algebra to infinite dimensional vector spaces (e.g. spaces of functions with a given property - e.g. continuity).  
    * __Differential Topology__:  
        is the study of smooth manifolds and smooth maps. It is fundamentally using tools from calculus (hence the "differential" part in the name) but the focus is on spaces and maps up to diffeomorphism, which means that you don't care at all about notions like angles, lengths, curvature, flatness etc. Just like in ordinary (non-differential) topology, a gently curved line, a straight line, and a totally squiggly line are all the same up to diffeomorphism (the squiggly line should have no sharp cusps and corners though, which is how this is different from ordinary topology).  
        * __Pre-Reqs:__ include a very good foundation in real analysis, including multivariate differential analysis; linear algebra; and topology.  
    * __Differential Geometry__:  
        Its the study of precisely those things that differential topology doesn't care about (i.e. angles, curvature, etc.). Here the principal objects of study are manifolds endowed with the much more rigid structure of a (Riemannian) metric, which lets you discuss geometric properties like lengths, angles and curvature. 
        * __Applications__:  
            It ties well with: Lie Groups, General Relativity, Symplectic Geometry (Mechanics), Algebraic Topology.  
        * __Pre-Reqs__: similar to those for Differential Topology: solid multivariate analysis, some topology, and of course linear algebra.  
    * __Algebraic Topology__:  
        the study of algebraic invariants as a tool for classifying topological objects.  
        >  Some of those invariants can actually be developed via differential topology (de Rham cohomology), but most are defined in completely different terms that do not need the space to have any differential structure whatsoever.  
        * __Pre-Reqs__: Hard + Touches a lot of math; topology, a good grounding in algebra (abelian groups, rings etc.), know something about categories and functors.  
    * __Algebraic Geometry__:  
        very different topic. At the most basic level, its the study of _algebraic varieties_ (i.e. sets of solutions to polynomial equations).  
        Modern algebraic geometry, however, is much wider than this innocent statement seems to imply. It is notoriously complex and requires a very deep understanding of a wide variety of disciplines and domains.  
        * __Pre-Reqs__: commutative algebra, Galois theory, some number theory (especially algebraic number theory), complex function theory, category theory, and a serving of algebraic topology wouldn't hurt.  
        General topology is sort-of required: algebraic geometry uses the notion of "Zariski topology" but, honestly, this topology is so different from the things most analysts and topologists talk about that basic topology won't help.
    {: hidden=''}

    [Further Reading](https://www.quora.com/What-are-the-differences-between-differential-topology-differential-geometry-algebraic-topology-and-algebraic-geometry-In-what-order-does-one-usually-go-about-learning-them)   
            

6. **From Topology to Algebraic Topology:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents36}  
    <button>Analysis</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    * Suppose we have a closed loop of rope, i.e., a rope with its ends connected together. Such a closed loop could be a simple ring or it could be knotted up in various different ways:  
        ![img](/main_files/concepts/2.png){: width="100%"}  
    * Now, whether or not it is knotted does not depend on how thick the rope is, how long the rope is, or how it is positioned in space. As long as we don't cut the rope, any kind of continuous deformation of the rope, such as moving it around, stretching it, bending it, and so on, does not change an unknotted closed loop into a knotted one. So, if we want to study the possible different ways a closed loop can be knotted, we want to ignore any differences related to all these various kinds of continuous deformations. When we ignore all those properties, what is left are called topological properties. So, while two closed loops of different sizes or shapes are geometrically distinct, they could be topologically identical. They are topologically distinct only if they can not be transformed into each other with any continuous deformation. So, in the context of knot theory, topology is the study of the properties of knottedness, which do not depend on the details of position, shape, size, and so on.  
    * Now, algebraic topology is a way of studying topological properties by translating them into algebraic properties. In the case of knot theory, this might involve, for example, a map that assigns a unique integer to any given closed loop. Such a map can be very useful if we can show that it will always assign the same integer to two closed loops that can be continuously deformed into each other, i.e., topologically equivalent closed loops are always assigned the same number. (Such a map is called a knot invariant.) For example, if we are given two closed loops and they are mapped to different integers, then this instantly tells us that they are topologically distinct from each other. The converse is not necessarily true, since a map with poor "resolving power" might take many topologically distinct closed loops to the same integer. Algebraic topology in the context of knot theory is the study of these kinds of maps from topological objects such as closed loops to algebraic objects such as integers. These maps give, as it were, algebraic perspectives on the topological objects, and that is what algebraic topology in general is about.
    {: hidden=''}  

7. **Notes:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents37}  
    * __Dot Product Scale/Magnitude__: the scale of the dot product increases as dimensions get larger.  
        Assume that the components of $$q$$ and $$k$$ are independent random variables with mean $$0$$ and variance $$1$$. Then their dot product, $$q^Tk = \sum_{i=1}^{d_k} q_ik_i$$, (where $$d_k = \vert k \vert$$ is the dimension of $$k \in \mathbb{R}^{d_k} \iff q \in \mathbb{R}^{d_q}$$) has mean $$0$$ and variance $$d_k$$.  
            

8. **Formulas:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents38}  
    <button>Show Formulas</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    * __Binomial Theorem__:  
        <p>$$(x+y)^{n}=\sum_{k=0}^{n}{n \choose k}x^{n-k}y^{k}=\sum_{k=0}^{n}{n \choose k}x^{k}y^{n-k} \\={n \choose 0}x^{n}y^{0}+{n \choose 1}x^{n-1}y^{1}+{n \choose 2}x^{n-2}y^{2}+\cdots +{n \choose n-1}x^{1}y^{n-1}+{n \choose n}x^{0}y^{n},$$</p>  
    * __Binomial Coefficient__:  
        <p>$${\binom {n}{k}}={\frac {n!}{k!(n-k)!}} = {n \text{ choose } k} = {n \choose (n-k)}$$</p>
    * __Expansion $$x^n - y^n$$__:  
        <p>$$x^n - y^n = (x-y)(x^{n-1} + x^{n-2} y + ... + x y^{n-2} + y^{n-1})$$</p>  
    * __Number of subsets of a set of $$N$$ elements__ $$= 2^N$$  
        * __Number of pairs (e.g. $$(a,b)$$) of a set of $$N$$ elements__ $$= N^2$$  
        * __Number of subsets of size $$k$$__ $$= {\binom {n}{k}}$$  
            * There are at most $$k^N$$ ways to partition $$N$$ data points into $$k$$ clusters - there are $$N$$ choose $$k$$ clusters, precisely  
    * __Permutations and Combinations__:  
        * __Permutations of a set of size $$N$$__  $$= N!$$  
        * [Set Inclusion/Exclusion (stackex)](https://math.stackexchange.com/questions/2852683/how-many-subsets-of-size-k-from-1-2-n-such-that-if-subset-contains-2-it-doe)  
            e.g. $$\left|S_{1} \cup S_{2}\right|=\left|S_{1}\right|+\left|S_{2}\right|-\left|S_{1} \cap S_{2}\right|=2\left|S_{1}\right|-\left|S_{1} \cap S_{2}\right|$$  
        * __Number of Subsets of size $$k$$ where 1 element $$i$$ always appears__: $$\left(\begin{array}{l}n-1 \\ k-1 \end{array}\right)$$  
            (e.g. the number of sets that include the element $$1$$)  
            * __Intuition__: you have already chosen two elements ($$1$$ and $$2$$), now there are $$k-2$$ slots left in each subset and $$n-2$$ elements left to choose from.  
        * __Number of Subsets of size $$k$$ where 2 element $$i$$ and $$j$$ appear together__: $$\left(\begin{array}{l}n-2 \\ k-2 \end{array}\right)$$  
            (e.g. the number of sets that include both $$1$$ and $$2$$)  
        <button>Diagram</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        ![img](https://cdn.mathpix.com/snip/images/726OtLVApY6cM75FeWVsxKTNWwN7I3C3OGioTOea9xU.original.fullsize.png){: width="70%" hidden=""}  
    * __Logarithms__:  
        <p>$$\log_x(y) = \dfrac{\ln(y)}{\ln(x)}$$</p>  
    * __The length of a vector $$\mathbf{x}$$  along a direction (projection)__:  
        1. Along a unit-length vector $$\hat{\mathbf{w}}$$: $$\text{comp}_ {\hat{\mathbf{w}}}(\mathbf{x}) = \hat{\mathbf{w}}^T\mathbf{x}$$  
        2. Along an unnormalized vector $$\mathbf{w}$$: $$\text{comp}_ {\mathbf{w}}(\mathbf{x}) = \dfrac{1}{\|\mathbf{w}\|} \mathbf{w}^T\mathbf{x}$$    
    * __Summations__:  
        * $$\sum_{i=1}^{n} 2^{i}=2^{n+1}-2$$  
    {: hidden=""}
            
9. **Linear Algebra:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents39}       
    __Matrices:__{: style="color: red"}  
    {: #lst-p}
    * __Symmetric Matrices:__{: style="color: blue"}  
        * can choose its eigenvectors to be __orthonormal__  
    * __PSD:__{: style="color: blue"}  
    * __PD:__{: style="color: blue"}  


***
***

## Statistics and Probability Theory
{: #content4}

1. **ROC Curve:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents41}  
    * A way to quantify how good a **binary classifier** separates two classes
    * True-Positive-Rate / False-Positive-Rate
    * Good classifier has a ROC curve that is near the top-left diagonal (hugging it)
    * A Bad Classifier has a ROC curve that is close to the diagonal line
    * It allows you to set the **classification threshold**  
        * You can minimize False-positive rate or maximize the True-Positive Rate  

    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * ROC curves (& AUC) are useful even if the __predicted probabilities__ are not *__"properly calibrated"__*  
    <br>

2. **AUC - AUROC:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents42}  
    * Range $$ = 0.5 - 1.0$$, from poor to perfect  
    <br>

3. **Statistical Efficiency:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents43}  
    Essentially, a more efficient estimator, experiment, or test needs fewer observations than a less efficient one to achieve a given performance.  
    Efficiencies are often defined using the _variance_ or _mean square error_ as the measure of desirability.  
    An efficient estimator is also the minimum variance unbiased estimator (MVUE).  

    * An Efficient Estimator has lower variance than an inefficient one  
    * The use of an inefficient estimator gives results equivalent to those obtainable from a subset of data; and is therefor, wasteful of data  

4. **Errors VS Residuals:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents44}  
    The __Error__ of an observed value is the deviation of the observed value from the (unobservable) **_true_** value of a quantity of interest.  

    The __Residual__ of an observed value is the difference between the observed value and the *__estimated__* value of the quantity of interest.  

    * [**Example in Univariate Distributions**](https://en.wikipedia.org/wiki/Errors_and_residuals#In_univariate_distributions){: value="show" onclick="iframePopA(event)"}
    <a href="https://en.wikipedia.org/wiki/Errors_and_residuals#In_univariate_distributions"></a>
        <div markdown="1"> </div>    

    <!-- 5. **Maximum Likelihood Estimation:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents45}   -->

<!-- 6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents46}  
7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents47}  
    :     -->

**Notes:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents48}  
{: #lst-p}
* __Why maximize the natural log of the likelihood?__:  
    1. Numerical Stability: change products to sums  
    2. The logarithm of a member of the family of exponential probability distributions (which includes the ubiquitous normal) is polynomial in the parameters (i.e. max-likelihood reduces to least-squares for normal distributions)  
    $$\log\left(\exp\left(-\frac{1}{2}x^2\right)\right) = -\frac{1}{2}x^2$$   
    3. The latter form is both more numerically stable and symbolically easier to differentiate than the former. It increases the dynamic range of the optimization algorithm (allowing it to work with extremely large or small values in the same way).  
    4. The logarithm is a monotonic transformation that preserves the locations of the extrema (in particular, the estimated parameters in max-likelihood are identical for the original and the log-transformed formulation)  
* [__(GANs) Sampling from Discrete Distributions \| The Gumbel-Softmax Trick__](http://anotherdatum.com/gumbel-gan.html)  
* __Covariance Matrix__ is the inverse of the __Metric Tensor__  
    * In __Gaussians__: $$\Sigma^{1/2}$$ maps spheres to ellipsoids; eigenvalues are radii; they are also the standard deviations along the eigenvectors  
* __Reason we sometimes prefer Biased Estimators__:  
    Mainly, due to the *__Bias-Variance Decomposition__*. The __MSE__ takes into account both the _bias_ and the _variance_ and sometimes the biased estimator might have a lower variance than the unbiased one, which results in a total _decrease_ in the MSE.  
* __Cross-Field Terms__:  
    * Independent Variable $$\iff$$  Covariate $$\iff$$  Feature   
    * (Collection of) Independent Variables $$\iff$$  Covariates $$\iff$$  Features $$\iff$$  Input   
    * Dependent Variable $$\iff$$  Response $$\iff$$  Label $$\iff$$  Target $$\iff$$  Output  
    * [Statistics VS Machine Learning](https://towardsdatascience.com/the-actual-difference-between-statistics-and-machine-learning-64b49f07ea3)  
* __Uncorrelated Features in a Design Matrix__:  
    <p>$$\implies X^TX=nI$$</p>   
* __Expectation Maximization (EM) Algorithm__:  
    [EM-Algo Math](http://bjlkeng.github.io/posts/the-expectation-maximization-algorithm/)  
        

***
***

## Optimization
{: #content5}

1. **Sigmoid:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents51}  
    $$\sigma(-x) = 1 - \sigma(x)$$  

2. **Gradient-Based Optimization:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents52}  
    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * Gradients can't propagate through __argmax__  
    * __Derivative for a max function__:  
        The derivative is defined (even though its not continuous at the threshold) by setting the value at the threshold/zero to be either the right or the left derivative.  
        This is known as the __Sub-Gradient__ and that's why _gradient descent_ still works.  
    * [__Subgradient Descent__](https://www.youtube.com/watch?v=jYtCiV1aP44&list=PLnZuxOufsXnvftwTB1HL6mel1V32w0ThI&index=12&t=0s)  
    * [**Hessian-Free Optimization \| Conjugate Gradient Method (Hinton)**](https://www.youtube.com/embed/K2X0eBd-0lc?list=PLoRl3Ht4JOcdU872GhiYWf6jwrk_SNhz9){: value="show" onclick="iframePopA(event)"}
    <a href="https://www.youtube.com/embed/K2X0eBd-0lc?list=PLoRl3Ht4JOcdU872GhiYWf6jwrk_SNhz9"></a>
        <div markdown="1"> </div>    


3. **Backpropagation:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents53}  

    __NOTES:__  
    * [Neural Network Simulator for learning Backprop](https://www.mladdict.com/neural-network-simulator)  

    <button>Show</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
    * __Backprop (BPTT specifically here) and concept of Locality__:  
        In this context, local in space means that a unit's weight vector can be updated using only information stored in the connected units and the unit itself such that update complexity of a single unit is linear in the dimensionality of the weight vector. Local in time means that the updates take place continually (on-line) and depend only on the most recent time step rather than on multiple time steps within a given time horizon as in BPTT. Biological neural networks appear to be local with respect to both time and space. [wikipedia](https://en.wikipedia.org/wiki/Recurrent_neural_network#Gradient_descent)
    * __Backpropagation with weight constraints__:  
        * It is easy to modify the backprop algorithm to incorporate linear constraints between the weights.  
            <p>$$\begin{array}{l}{\text { To constrain: } w_{1}=w_{2}} \\ {\text { we need : } \Delta w_{1}=\Delta w_{2}}\end{array}$$</p>  
            So, we compute the gradients as usual for each $$w_i$$ then average them and update both weights (so they'll continue to satisfy the constraints).    
    * Backprop is a __Leaky Abstraction__  
    * __Properties of Loss Functions for Backpropagation__:  
        The mathematical expression of the loss function must fulfill two conditions in order for it to be possibly used in back propagation.[3] The first is that it can be written as an average $${\textstyle E={\frac {1}{n}}\sum _{x}E_{x}}$$ over error functions $${\textstyle E_{x}}$$ {\textstyle E_{x}}, for $${\textstyle n}$$ individual training examples, $${\textstyle x}$$. The reason for this assumption is that the backpropagation algorithm calculates the gradient of the error function for a single training example, which needs to be generalized to the overall error function. The second assumption is that it can be written as a function of the outputs from the neural network.  
    {: hidden=""}
            


4. **Error Measures - Loss Functions:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents54}  
    * __Cross Entropy__:  
        * __Deriving Binary Cross Entropy__:  
            It is the log-likelihood of a Bernoulli probability model.  
            <p>$$\begin{array}{c}{L(p)=p^{y}(1-p)^{1-y}} \\ {\log (L(p))=y \log p+(1-y) \log (1-p)}\end{array}$$</p>  
        * __[Cross Entropy > MSE for Classification](https://jamesmccaffrey.wordpress.com/2013/11/05/why-you-should-use-cross-entropy-error-instead-of-classification-error-or-mean-squared-error-for-neural-network-classifier-training/)__  
    <br>

    __Notes:__{: style="color: red"}   
    {: #lst-p}
    * __Loss VS Cost Function__:  
        * Loss is just the Error function from Caltech
        * Cost is more general than Loss: usually the sum of all the losses  
        * __Objective function__ is even more general, but a Cost might be a type of __Objective Function__  
            * The __Risk Function__ is an objective function is the expected loss  
    * [__Loss Functions for Regression__](https://www.youtube.com/watch?v=1oi_Mwozj5w&list=PLnZuxOufsXnvftwTB1HL6mel1V32w0ThI&index=8)  
    * __MSE__:  
        The principle of mean square error can be derived from the principle of maximum likelihood (after we set a linear model where errors are normally distributed).  
    * __Hinge Loss and 0-1 Loss__:  
        * Hinge loss upper bounds 0-1 loss
        * It is the tightest _convex_ upper bound on the 0/1 loss  
        * Minimizing 0-1 loss is NP-hard in the worst-case  
        img  
    * __Loss functions of common ML models__:  
        * maximize the posterior probabilities (e.g., naive Bayes)
        * maximize a fitness function (genetic programming)
        * maximize the total reward/value function (reinforcement learning)
        * maximize information gain/minimize child node impurities (CART decision tree classification)
        * minimize a mean squared error cost (or loss) function (CART, decision tree regression, linear regression, adaptive linear neurons, ...
        * maximize log-likelihood or minimize cross-entropy loss (or cost) function
        * minimize hinge loss (support vector machine)  
    <br>

5. **Mathematical Properties, Aspects, Considerations:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents55}  
    * __The Composition of Invariant Functions__:  
        A function that is _invariant_ to some transformation (e.g. rotation, permutation, etc.) can be composed by averaging over all transformations (rotations $$\rightarrow$$ e.g. rotation invariant filters).  
        Equivalently, for _BoW_, we average over all permutations (by averaging the words).  
        This causes *__smearing__*.   
    * __Smearing in Invariant Functions__:  
        In the linear case, a rotational invariant function commutes with all rotations of the elements in $$\mathbb{R}$$; Any commutative transformation should yield this; or a combo of commutative transformations; thus smearing.  
        > Implies that one should not use linear functions to aggregate over the set where we want some transformation invariance   
    * __Permutation Invariance__:  
        * [DeepSets: Modeling Permutation Invariance](https://www.inference.vc/deepsets-modeling-permutation-invariance/)  
    * __The Weight vector of a linear signal is orthogonal to the decision boundary__:  
        The weight vector $$\mathbf{w}$$ is orthogonal to the separating-plane/decision-boundary, defined by $$\mathbf{w}^T\mathbf{x} + b = 0$$, in the $$\mathcal{X}$$ space; Reason:  
        Since if you take any two points $$\mathbf{x}^\prime$$ and $$\mathbf{x}^{\prime \prime}$$ on the plane, and create the vector $$\left(\mathbf{x}^{\prime}-\mathbf{x}^{\prime \prime}\right)$$  parallel to the plane by subtracting the two points, then the following equations must hold:  
        <p>$$\mathbf{w}^{\top} \mathbf{x}^{\prime}+b=0 \wedge \mathbf{w}^{\top} \mathbf{x}^{\prime \prime}+b=0 \implies \mathbf{w}^{\top}\left(\mathbf{x}^{\prime}-\mathbf{x}^{\prime \prime}\right)=0$$</p>  

    __Identities:__{: style="color: red"}  
    {: #lst-p}
    * __Math Identities__:  
        <p>$$\frac{1}{N} \sum_{n=1}^{N}\left(\mathbf{w}^{\mathrm{T}} \mathbf{x}_{n}-y_{n}\right)^{2} = \frac{1}{N}\|\mathrm{Xw}-\mathrm{y}\|^{2}$$</p>  
        * $$\dfrac{\partial}{\partial y} \vert{x-y}\vert  = - \text{sign}(x-y)$$  
    <br>

    __Notes:__{: style="color: red"}  
    {: #lst-p}
    {: #lst-p}
    * The __well-behaved__ property from an optimization standpoint, implies that $$f''(x)$$ doesn't change too much or too rapidly, leading to a nearly quadratic function that is easy to optimize by gradient methods.  


6. **The Method of Lagrange Multipliers:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents56}  
    The __constrained__ optimization problem:  
    <p>$$\min_{\mathbf{x}} f(\mathbf{x}) \text { subject to } g(\mathbf{x}) \leq 0$$</p>  
    is equivalent to the __unconstrained__ optimization problem:  
    <p>$$\min_{\mathbf{x}}(f(\mathbf{x})+\lambda g(\mathbf{x}))$$</p>    
    where $$\lambda$$ is a scalar called the __Lagrange multiplier__.  
<br>

<!-- 7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents57}  

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents58}  -->

__NOTES:__  
* [Ch.8 Dl-book summary](https://medium.com/inveterate-learner/deep-learning-book-chapter-8-optimization-for-training-deep-models-part-i-20ae75984cb2)  
* [Why You Should Use Cross-Entropy Error Instead Of Classification Error Or Mean Squared Error For Neural Network Classifier Training](https://jamesmccaffrey.wordpress.com/2013/11/05/why-you-should-use-cross-entropy-error-instead-of-classification-error-or-mean-squared-error-for-neural-network-classifier-training/)  
* Points that satisfy all constraints (i.e. the feasible region) always convex and polytope.  
* __[Optimization Blog on opt techniques](http://ruder.io/optimizing-gradient-descent/index.html#gradientdescentoptimizationalgorithms)__  
* [WHY NORMALIZE THE INPUTS/DATA/SIGNAL](https://www.youtube.com/watch?v=FDCfw-YqWTE&list=PLkDaE6sCZn6Hn0vK8co82zjQtt3T2Nkqc&index=10&t=0s)
* [Optimization by Vector Space Methods (book)](http://math.oregonstate.edu/~show/old/142_Luenberger.pdf)
* [__OLS Derivation and Theory__](https://web.stanford.edu/~mrosenfe/soc_meth_proj3/matrix_OLS_NYU_notes.pdf)   


<br>

***
***

## Machine Learning
{: #content6}

1. **Theory:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents61}  
    * __ML from a Probabilistic Approach__:  
        When employing a _probabilistic approach_ to doing _"learning"_ (i.e. choosing the hypothesis), you are trying to find: __What is the most probable hypothesis, given the Data__.  

    __Why NNs are not enough?__  
    The gist of it is this: neural nets do *pattern recognition*, which achieves *local generalization* (which works great for supervised perception). But many simple problems require some (small) amount of abstract modeling, which modern neural nets can't learn.  

    __Is there enough info in the labels to learn good, general features in Classification problems?__  
    <button>Show Text</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
    <p hidden="">(((If the task is to learn to classify a particular image into one class/category; and the categories lie on the same manifold (i.e. just cats and dogs; or just vehicles etc.) then, the model can learn the patterns that relate to the particular class the image belongs to, BUT MOREOVER, it learns to ignore the rest of the patterns (i.e. background). So, in a way, yes, there is no information in the labels that tells the network to learn what a tree is (so any objects in the background are somewhat blurred to the network, they have no higher-order meaning) so the overall higher-level vision capabilities of the network doesn't necessarily "develop".   <br />
    As for the task of pre-training, we both know that even if you learn the patterns of very specific objects/classes (e.g. cats and dogs) you still need to develop certain visual features (e.g. edge/corner detection) and those featurizers will develop well, regardless of the amount of information. i.e. the lower-level visual capabilities will be developed. (we have evidence that pretraining works really well in Vision).  <br />
    I think the issue here is with Deterministic Noise (i.e. the Bias of the model). The CNN hypothesis just doesn't do things like inverse graphics and whatnot; regardless of the amount of information.  <br />
    Finally, a big problem is when the information is just conflicting, like two objects that should be recognized but we only label it as one of them. That's the Stochastic Noise. Which relates directly to how well we would generalize. This can be attributed to many things as well: E.g. (1) One-hot vectors need to be smoothed to allow the network to get a sense of the actual different objects in the image, AND to not over-fit the particulars of the data (e.g. consider a cat that looks like a tiger and a cat that looks like a dog; labeling it with 0.8 cat is much better to learn the "cattiness" of the image than the noise) (2) Target labels are just limited. There aren't enough categories in the target, which puts a huge limitation for one-shot learning generalization)))</p>  

    __Neural Tangent Kernel:__  
    {: #lst-p}
    * [Video](https://www.youtube.com/watch?v=raT2ECrvbag)  
    * [Neural Tangent Kernel: Convergence and Generalization in Neural Networks (paper)](https://arxiv.org/pdf/1806.07572.pdf)  

    __NTK Theorem:__ A properly randomly initialized <span>sufficiently wide</span>{: style="color: purple"} deep neural network <span>trained by gradient descent</span>{: style="color: purple"} with infinitesimal step size (a.k.a. gradient flow) is <span>equivalent to a kernel regression predictor</span>{: style="color: purple"} with a <span>deterministic</span>{: style="color: purple"} kernel called neural tangent kernel (NTK).  

    Thus, As width (of NN) $$\rightarrow \infty$$, trajectory approaches the trajectory of GD for a kernel regression problem, where the (fixed) kernel in question is the so-called Neural Tangent Kernel (NTK). (For convolutional nets the kernel is Convolutional NTK or CNTK.)  
    The paper proves that the evolution of an ANN during training can also be described by a kernel.  

    __Analysis and Discussion:__{: style="color: red"}  
    {: #lst-p}
    * Start with: Fully-Connected Network, Any Depth, Lipschitz Non-Linearity  
    * Gather all __parameters__ in the network into one vector $$\theta$$: initialized randomly, trained w/ GD
    * Since cost is non-convex, the analysis is difficult
    * Instead, study the network function $$f_{\theta} : \mathbb{R}^{n_0} \rightarrow \mathbb{R}^{n_L}$$ which maps inputs to outputs  
        We fully characterize the behavior of $$f_{\theta}$$ in the __infinite-width limit__ (\# of neurons in hidden layer $$\rightarrow \infty$$)  
    * __Behavior in the limit of the width:__  
        * In the limit, the network function has a __Gaussian distribution__ at *__initialization__*  
            <button>Plot of 20 random initialization of $$f_{\theta}$$ on the unit circle</button>{: .showText value="show" onclick="showTextPopHide(event);"}
            ![img](https://cdn.mathpix.com/snip/images/dWbTf3G6bbXIF7jMNZMD9wbRv2fwXgGYRvvvLCRyjPM.original.fullsize.png){: width="55%" hidden=""}  
        * The effect of GD on a single point $$\boldsymbol{x}_ 0$$ at initialization is to move that point and nearby points slightly  
            <button>graph</button>{: .showText value="show" onclick="showTextPopHide(event);"}
            ![img](https://cdn.mathpix.com/snip/images/O3g9y_EIlF4v0KDqkvs3uG3MJC9UG28M0BzkgVseyJY.original.fullsize.png){: width="55%" hidden=""}  
        * The difference between the two time-steps results in a __smooth spike__ centered at $$\boldsymbol{x}_ 0$$  
            <button>graph</button>{: .showText value="show" onclick="showTextPopHide(event);"}
            ![img](https://cdn.mathpix.com/snip/images/q4Hiw3g9THS93MVV_eBJvWLfmEeNuui81mYfzKf-lzM.original.fullsize.png){: width="55%" hidden=""}  
        * The difference is the same for different initializations.  
            <button>graph</button>{: .showText value="show" onclick="showTextPopHide(event);"}
            ![img](https://cdn.mathpix.com/snip/images/wi4MRjf0aCh4hIquTJxG-Bqg8Pztg_sIYDOXDJoEwLw.original.fullsize.png){: width="55%" hidden=""}  
        * As we increase the __width__ of the network, they differences become even more similar  
            <button>graph</button>{: .showText value="show" onclick="showTextPopHide(event);"}
            ![img](https://cdn.mathpix.com/snip/images/KytLYBbrNPzO76F4dlFYKDf_HcIZ1ZFHbLcIIUxjhd4.original.fullsize.png){: width="55%" hidden=""}  
        * The behavior is __linear__ i.e. adding another datapoint $$\boldsymbol{x}_ 1$$  results in the two spikes being __added up__  
            <button>graph</button>{: .showText value="show" onclick="showTextPopHide(event);"}
            ![img](https://cdn.mathpix.com/snip/images/H4sVN01wI0Tc2GWXUmRwM9tgjoUrJb9MeM-VvvXLLfI.original.fullsize.png){: width="100%" hidden=""}   
    * This behavior in the limit can be nicely described by a __kernel__.  
        The __Neural Tangent Kernel (NTK)__:  
        ![img](https://cdn.mathpix.com/snip/images/Rym-odIEPt0sZJuKmvccyeBFasKNM_LZWm060ONv_cI.original.fullsize.png){: width="30%"}{: .center-image}  
        * __Defined__: in terms of the <span>derivatives of the function wrt the parameters $$\theta$$</span>{: style="color: purple"}  
        * __Describes__: how <span>*modifying* the __network function $$f_{\theta}$$__ at the point $$\boldsymbol{x}$$ will *influence* another point $$\boldsymbol{y}$$</span>{: style="color: purple"}  
    * __Properties__:  
        * __Finite Width__:  
            *__Depends__* on the __parameters__, thus it is:  
            {: #lst-p}
            * <span>__Random__ at initialization  </span>{: style="color: purple"} 
            * <span>__Time-dependent__</span>{: style="color: purple"}: varies during training  
        * __Infinite width limit__ :  
            <p>$$\theta^{(L)}(x, y) \rightarrow \theta_{\infty}^{(L)}(x, y)  \:\: n_i \rightarrow \infty \forall i \in [1, ..., L-1]$$</p>  
            *__Independent__* on the __parameters__, thus it is:   
            {: #lst-p}
            * <span>Deterministic</span>{: style="color: purple"}: converges to a deterministic limit at initialization    
            * <span>Fixed</span>{: style="color: purple"}: its rate of change during training $$\rightarrow 0$$  

            This explains why the effect of GD was so similar for different initializations.    
            <button>graph</button>{: .showText value="show" onclick="showTextPopHide(event);"}
            ![img](https://cdn.mathpix.com/snip/images/Pp0Hxm5V_iEZ4U6hbTl5ihRwKKnE7ZpKUaokDEjgls4.original.fullsize.png){: width="50%" hidden=""}  
    * Now we have all the tools to fully describe the behavior of the network function during training:   
        * __Ex. Least-Squares Regression on 3 points__:  
            * Start w/ __random Gaussian Process__  
            * Follow the __kernel gradient of the cost__ wrt __NTK__  
    * <span>__Kernel GD__ is simply a *__generalization__* of __GD__ to</span>{: style="color: purple"} __Function Spaces__{: style="color: goldenrod"}  
        * Because the cost is __convex__ in function space the function will converge to the minimum if the kernel is __Positive Definite__  
    * As width (of NN) $$\rightarrow \infty$$, trajectory approaches the trajectory of GD for a kernel regression problem, where the (fixed) kernel in question is the so-called Neural Tangent Kernel (NTK). (For convolutional nets the kernel is Convolutional NTK or CNTK.)  


    __Notes:__  
    {: #lst-p}
    * __Intuition of why DL Works__:  
        __Circuit Theory:__ There are function you can compute with a "small" L-layer deep NN that shallower networks require exponentially more hidden units to compute. (comes from looking at networks as logic gates).  
        * __Example__:  
            Computing $$x_1 \text{XOR} x_2 \text{XOR} ... \text{XOR} x_n$$  takes:   
            * $$\mathcal{O}(log(n))$$ in a tree representation.  
                ![img](/main_files/concepts/7.png){: width="40%"}  
            * $$\mathcal{O}(2^n)$$ in a one-hidden-layer network because you need to exhaustively enumerate all possible $$2^N$$ configurations of the input bits that result in the $$\text{XOR}$$ being $${1, 0}$$.   
                ![img](/main_files/concepts/8.png){: width="40%"}  
    * __[Curse of Dimensionality (ipynb)](https://github.com/josh-tobin/cs189-su18/blob/master/lecture7.ipynb)__  
    * __The Hypothesis space of Neural Networks is Convex__:  
        Composition of affine-relu functions; induction.  
    * __[Generalization in Deep Learning](https://arxiv.org/pdf/1710.05468.pdf)__  
    * __Catastrophic Forgetting:__  
        * mitigating catastrophic forgetting [McCloskey and Cohen, 1989, Ratcliff, 1990, Kemker et al., 2017] by penalizing the norm of parameters when training on a new task [Kirkpatrick et al., 2017], the norm of the difference between parameters for previously learned tasks during parameter updates [Hashimoto et al., 2016], incrementally matching modes [Lee et al., 2017], rehearsing on old tasks [Robins, 1995], using adaptive memory buffers [Gepperth and Karaoguz, 2016], finding task-specific paths through networks [Fernando et al., 2017], and packing new tasks into already trained networks [Mallya and Lazebnik, 2017].  
        * [Overcoming catastrophic forgetting in neural networks (paper)](https://arxiv.org/abs/1612.00796)  
    <br>

2. **The Big Formulations:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents62}  
    __ML Formulation:__{: style="color: red"}  
    Improve on __TASK T__ with respect to __PERFORMANCE METRIC P__ based on __EXPERIENCE E__.  

    __Problems in ML:__{: style="color: red"}  
    <button>Show</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
    * __T:__ Categorize email messages as spam or legitimate 
        __P:__ Percentage of email messages correctly classified 
        __E:__ Database of emails, some with human-given labels  

    * __T:__ Recognizing hand-written words 
        __P:__ Percentage of words correctly classified 
        __E:__ Database of human-labeled images of  handwritten words 

    * __T:__ playing checkers 
        __P:__ percentage of games won against an arbitrary opponent 
        __E:__ Playing practice games against itself 

    * __T:__ Driving on four-lane highways using vision sensors 
        __P:__ Average distance traveled before a human-judged error 
        __E:__ A seq of images and steering commands recorded while observing a human driver  
    * __Sequence Labeling__: 
        * *__Problems__*:  
            * Speech Recognition 
            * OCR
            * Semantic Segmentation
        * *__Approaches__*:  
            * CTC - Bi-directional LSTM
            * Listen Attend and Spell (LAS)
            * HMMs 
            * CRFs  
    {: hidden=""}

            
<!-- 3. **What is ML?:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents63}   -->


4. **Types of Learning:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents64}  
    * __Multi-Task Learning__: general term for training on multiple tasks  
        * _Joint Learning:_ by choosing mini-batches from two different tasks simultaneously/alternately
        * _Pre-Training:_ first train on one task, then train on another  
            > widely used for __word embeddings__  
    * __Transfer Learning__:  
        a type of multi-task learning where we are focused on one task; by learning on another task then applying those models to our main task  
    * __Domain Adaptation__:  
        a type of transfer learning, where the output is the same, but we want to handle different inputs/topics/genres  
    * __Zero-Shot Learning__:  


    __Notes:__  
    {: #lst-p}
    * __Relationship between Supervised and Unsupervised Learning__:  
        Many ml algorithms can be used to perform both tasks. E.g., the chain rule of probability states that for a vector $$x \in \mathbb{R}^n$$, the joint distribution can be decomposed as:  
        $$p(\mathbf{x})=\prod_{i=1}^{n} p\left(\mathrm{x}_{i} \vert \mathrm{x}_{1}, \ldots, \mathrm{x}_{i-1}\right)$$  
        which implies that we can solve the Unsupervised problem of modeling $$p(x)$$ by splitting it into $$n$$ supervised learning problems.  
        Alternatively, we can solve the supervised learning problem of learning $$p(y \vert x)$$ by using traditional unsupervised learning technologies to learn the joint distribution $$p(x, y)$$, then inferring:  
        $$p(y \vert \mathbf{x})=\frac{p(\mathbf{x}, y)}{\sum_{y} p\left(\mathbf{x}, y^{\prime}\right)}$$  
    * __Intuition on Why Unsupervised Learning works__:  
        * Goal: Learn Portuguese
        * For 1 month you listen to Portuguese on the radio (this is unlabeled data)
        * You develop an intuition for the language, phrases, and grammar (a model in your head)
        * It is easier to learn now from a tutor because you have a better (higher representation) of the data/language  

                

5. **Linear Models:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents65}  
    A __Linear Model__ takes an input $$x$$ and computes a signal $$s = \sum_{i=0}^d w_ix_i$$ that is a _linear combination_ of the input with weights, then apply a scoring function on the signal $$s$$.  
    * __Linear Classifier as a Parametric Model__:  
        Linear classifiers $$f(x, W)=W x+b$$  are an example of a parametric model that sums up the knowledge of the training data in the parameter: weight-matrix $$W$$.  
    * __Scoring Function__:  
        * *__Linear Classification__*:  
            $$h(x) = sign(s)$$  
        * *__Linear Regression__*:  
            $$h(x) = s$$  
        * *__Logistic Regression__*:  
            $$h(x) = \sigma(s)$$  

    __Notes:__{: style="color: red"}  
    {: #lst-p}
    {: #lst-p}
    * __The Weight vector of a linear signal is orthogonal to the decision boundary__:  
        The weight vector $$\mathbf{w}$$ is orthogonal to the separating-plane/decision-boundary, defined by $$\mathbf{w}^T\mathbf{x} + b = 0$$, in the $$\mathcal{X}$$ space; Reason:  
        Since if you take any two points $$\mathbf{x}^\prime$$ and $$\mathbf{x}^{\prime \prime}$$ on the plane, and create the vector $$\left(\mathbf{x}^{\prime}-\mathbf{x}^{\prime \prime}\right)$$  parallel to the plane by subtracting the two points, then the following equations must hold:  
        <p>$$\mathbf{w}^{\top} \mathbf{x}^{\prime}+b=0 \wedge \mathbf{w}^{\top} \mathbf{x}^{\prime \prime}+b=0 \implies \mathbf{w}^{\top}\left(\mathbf{x}^{\prime}-\mathbf{x}^{\prime \prime}\right)=0$$</p>  

    <!-- 6. **Learning Probabilities with Logistic Regression and Sigmoids:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents66}   -->
          

    <!-- 7. **Papers:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents67}   -->

    <!-- 8. **Activation Functions:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents68}    -->

9. **Bias-Variance Decomposition Theory:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents69}   
    __Bias-Variance for Neural-Networks:__{: style="color: red"}  
    {: #lst-p}
    ![img](/main_files/concepts/9.png){: width="60%"}  
    __Dealing with Bias and Variance for NN:__  
    * __High Bias__ ($$E_{\text{train}}$$) $$\rightarrow$$ (1) Bigger Net (2) Train longer (3) Different NN archit  
    * __High Variance__ ($$E_{\text{dev}}$$) $$\rightarrow$$ (1) More Data (2) Regularization (3) Different NN archit  
    <br>

10. **Models:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents610}   
    __Parametric Models:__{: style="color: red"}  
    A __parametric model__ is a set of probability distributions indexed by a parameter $$\theta \in \Theta$$. We denote this as:  
    <p>$$\{p(y ; \theta) \vert \theta \in \Theta\},$$</p>  
    where $$\theta$$ is the __parameter__ and $$\Theta$$ is the __Parameter-Space__.  
    <br>


11. **Output Units/Functions:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents611}   
    <button>Output Units: Linear and Sigmoid units</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](/main_files/concepts/10.jpg){: hidden=""}  


12. **Model Varieties - Regression and Classification:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents612}  
    __Generalized Regression__ also known as __Conditional Distribution Estimation:__{: style="color: red"}    
    {: #lst-p}
    * Given $$x$$, predict probability distribution $$p(y\vert x)$$  
    * How do we represent the probability distribution?
        * We'll consider parametric families of distributions
            * distribution represented by parameter vector
        * Examples:  
            * Generalized Linear Models (GLM)
                * Logistic regression (Bernoulli distribution)
                * Probit regression (Bernoulli distribution)
                * Poisson regression (Poisson distribution)
                * Linear regression (Normal distribution, fixed variance)
            * Generalized Additive Models (GAM)
            * Gradient Boosting Machines (GBM) / AnyBoost  


    __Probabilistic Binary Classifiers:__{: style="color: red"}  
    {: #lst-p}
    * Setting: $$X=\mathrm{R}^{d}, y=\{0,1\}$$  
    * For each $$x$$, need to predict a distribution on $$y=\{0,1\}$$  
    * To define a distribution supported on $$\{0,1\}$$, it is sufficient to specify the __Bernoulli parameter__ $$\theta=p(y=1 \vert x)$$  
    * We can refer to this distribution as $$\text{Bernoulli}(\theta)$$  

    __Linear Probabilistic Classifiers:__{: style="color: red"}  
    {: #lst-p}
    * Setting: $$X=\mathrm{R}^{d}, y=\{0,1\}$$  
    * Want prediction function to map each $$x \in \mathrm{R}^{d}$$ to the right $$\theta \in[0,1]$$  
    * We first extract information from $$ x \in \mathrm{R}^{d}$$ and summarize in a single number  
        * That number is analogous to the __Score__ in _classification_  
    * For a __linear method/model__, this extraction is done with a __linear function__;  
        <p>$$\underbrace{x}_{\in \mathbb{R}^{D}} \mapsto \underbrace{w^{T} x}_{\in \mathrm{R}}$$</p>  
    * As usual, $$x \mapsto w^{T} x$$ will include __affine functions__ if we include a constant features in $$x$$  
    * $$w^Tx$$ is called the __linear predictor__ 
    * Still need to map this to $$[0, 1]$$; we do so by __Transfer/Response/Inverse-Link function__; usually the *__logistic function (Sigmoid)__*   
        > Its a function to map the linear predictor in $$\mathbb{R}$$ to $$[0,1]$$:  
            $$\underbrace{x}_ {\in \mathbf{R}^{D}} \mapsto \underbrace{w^{T}}_{\in R} \mapsto \underbrace{f\left(w^{T} x\right)}_{\in[0,1]}=\theta = p(y=1 \vert x)$$   

    __Learning:__  
    The hypothesis space/set:  
    <p>$$\mathcal{H}=\left\{x \mapsto f\left(w^{T} x\right) \vert w \in \mathbb{R}^{d}\right\}$$</p>  
    where the **only _"parameter"_** in this model is $$w \in \mathbb{R}^d$$.   
    We can choose $$w$$ using __maximum likelihood:__  
    __Likelihood Scoring \| Bernoulli Regression:__  
    * Suppose we have data $$\mathcal{D}=\left\{\left(x_{1}, y_{1}\right), \ldots,\left(x_{n}, y_{n}\right)\right\}$$  
    * The model likelihood for $$\mathcal{D}$$:  
        <p>$$\begin{aligned} p_{w}(\mathcal{D}) &=\prod_{i=1}^{n} p_{w}\left(y_{i} \vert x_{i}\right)[\text { by independence }] \\ &=\prod_{i=1}^{n}\left[f\left(w^{T} x_{i}\right)\right]^{y_{i}}\left[1-f\left(w^{T} x_{i}\right)\right]^{1-y_{i}} \end{aligned}$$</p>  
        * This probability of each data-point $$p_w(y_i\|x_i)$$ can be summed in the equation $$\left[f\left(w^{T} x_{i}\right)\right]^{y_{i}}\left[1-f\left(w^{T} x_{i}\right)\right]^{1-y_{i}}$$ which capture both cases $$p_w(y_i = 1) = f\left(w^{T} x_{i}\right)$$ and $$p_w(y_i = 0) = 1 - f\left(w^{T} x_{i}\right)$$ 
    * The __log likelihood__:  
        <p>$$\log p_{w}(\mathcal{D})=\sum_{i=1}^{n} y_{i} \log f\left(w^{T} x_{i}\right)+\left(1-y_{i}\right) \log \left[1-f\left(w^{T} x_{i}\right)\right]$$</p>  
    * Equivalently, minimize the objective function:  
        <p>$$J(w)=-\left[\sum_{i=1}^{n} y_{i} \log f\left(w^{T} x_{i}\right)+\left(1-y_{i}\right) \log \left[1-f\left(w^{T} x_{i}\right)\right]\right]$$</p>  


    __Gaussian Linear Regression/Conditional Gaussian Regression:__{: style="color: red"}  
    {: #lst-p}
    * [**Gaussian Linear Regression**](https://www.youtube.com/embed/JrFj0xpGd2Q?start=1965){: value="show" onclick="iframePopA(event)"}
    <a href="https://www.youtube.com/embed/JrFj0xpGd2Q?start=1965"></a>
        <div markdown="1"> </div>    

    __Generalized Regression as Statistical Learning:__{: style="color: red"}  
    {: #lst-p}
    * [**Generalized Regression as Statistical Learning**](https://www.youtube.com/embed/JrFj0xpGd2Q?start=2609){: value="show" onclick="iframePopA(event)"}
    <a href="https://www.youtube.com/embed/JrFj0xpGd2Q?start=2609"></a>
        <div markdown="1"> </div>    

    __Generalized Linear Models:__{: style="color: red"}  
    {: #lst-p}
    * [**Generalized Linear Models (Andrew NG)**](https://www.youtube.com/embed/nLKOQfKLUks?list=PLA89DCFA6ADACE599){: value="show" onclick="iframePopA(event)"}
    <a href="https://www.youtube.com/embed/nLKOQfKLUks?list=PLA89DCFA6ADACE599"></a>
        <div markdown="1"> </div>    
    * [GLM Probabilistic Development](http://bjlkeng.github.io/posts/a-probabilistic-view-of-regression/)  
    <br>



13. **Bayesian Conditional Probabilistic Models:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents613}  
    * [**Bayesian Conditional Probabilistic Models**](https://www.youtube.com/embed/Mo4p2B37LwY){: value="show" onclick="iframePopA(event)"}
    <a href="https://www.youtube.com/embed/Mo4p2B37LwY"></a>
        <div markdown="1"> </div>    
    <br>


15. **Recommendation Systems:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents615}  
    * <button>Recommendation Systems</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](/main_files/concepts/9.jpg){: hidden=""}  
    * [Winning the Netflix Prize: A Summary (blog!)](https://blog.echen.me/2011/10/24/winning-the-netflix-prize-a-summary/)  
    * [Moving Beyond CTR: Better Recommendations Through Human Evaluation (blog)](https://blog.echen.me/2014/10/07/moving-beyond-ctr-better-recommendations-through-human-evaluation/)  
    <br>

16. **Regularization:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents616}  
    * __Overfitting and Regularization__:  
        To address over-fitting:
        * Increase size of training dataset  
        * Reduce number of features  
        * Do Regularization:  
            * Keep all the features but reduce the magnitude/values of the weights/parameters  
            * Works well when we have a lot of features, each of which contributes a bit to predicting $$y$$  
    * __Regularization Theory__:  
        * [link1](https://www.youtube.com/watch?v=DCvXYD6xQYw)
        
    * __Theoretical Justification for Regularization__:  
        A theoretical justification for regularization is that it attempts to impose Occam's razor on the solution.  
        From a Bayesian point of view, many regularization techniques correspond to imposing certain prior distributions on model parameters.  
    * __Tikhonov Regularization__: is essentially a trade-off between fitting the data and reducing a norm of the solution.  

    __Data Regularization:__{: style="color: red"}  
    {: #lst-p}
    * The __Design Matrix__ contains sample points in each *__row__* 
    * __Feature Scaling/Mean Normalization (of data)__:  
        * Define the mean $$\mu_j$$ of each feature of the datapoints $$x^{(i)}$$:  
        <p>$$\mu_{j}=\frac{1}{m} \sum_{i=1}^{m} x_{j}^{(i)}$$</p>  
        * Replace each $$x_j^{(i)}$$ with $$x_j - \mu_j$$  
    * __Centering__:  subtracting $$\mu$$ from each row of $$X$$ 
    * __Sphering__:  applying the transform $$X' = X \Sigma^{-1/2}$$  
    * __Whitening__:  Centering + Sphering (also known as *__Decorrelating feature space__*)  

    <button>Why Normalize the Data/Signal?</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/8aNuJetgTgCtv4pvqaI0dr96pDyUmfuX_d1aLK1lmaw.original.fullsize.png){: width="80%" hidden=""}  


    [Pre-processing for Deep Learning (data regularization)](https://hadrienj.github.io/posts/Preprocessing-for-deep-learning/)          

    [Ch.7 dl-book summary](https://github.com/dalmia/Deep-Learning-Book-Chapter-Summaries/blob/master/07%20-%20Regularization%20for%20Deep%20Learning.ipynb)  
    <br>


17. **Aggregation - Ensemble Methods:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents617}  

    * __Boosting__: create different hypothesis $$h_i$$s sequentially + make each new hypothesis __decorrelated__ with previous hypothesis.  
        * Assumes that this will be combined/ensembled  
        * Ensures that each new model/hypothesis will give a different/independent output  


18. **Kernels:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents618}  
    * __Kernels__:  
        * __Polynomial Kernel of degree, exactly, $$d$$__:  
            <p>$$K(\mathbf{u}, \mathbf{v})=(\mathbf{u} \cdot \mathbf{v})^{d}$$</p>  
        * __Polynomial Kernel of degree, up to, $$d$$__:  
            <p>$$K(\mathbf{u}, \mathbf{v})=(\mathbf{u} \cdot \mathbf{v}+1)^{d}$$</p>  
        * __Gaussian Kernel__:  
            <p>$$K(\vec{u}, \vec{v})=\exp \left(-\frac{\|\vec{u}-\vec{v}\|_ {2}^{2}}{2 \sigma^{2}}\right)$$</p>  
        * __Sigmoid Kernel__:  
            <p>$$K(\mathbf{u}, \mathbf{v})=\tanh (\eta \mathbf{u} \cdot \mathbf{v}+\nu)$$</p>  

    * __Local Kernels__: a kernel where $$k(u, v)$$ is large when $$u=v$$ and decreases as $$u$$ and $$v$$ grow further apart from each other.  
        A local kernel can be thought of as a __similarity function__ that performs __template matching__, by measuring how closely a test example $$x$$ resembles each training example $$x^{(i)}$$.  
    * The kernel trick can NOT be applied to any learning algorithm  

    * [Kernel Regression Introduction](http://mccormickml.com/2014/02/26/kernel-regression/)  
            


21. **Curse of Dimensionality:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents621}  
    __The Curse of Dimensionality__, in general, refers to various phenomena, that arise when analyzing and organizing data in high-dimensional spaces, that do not occur in low-dimensional settings such as the three-dimensional physical space of everyday experience.  

    __Common Theme:__{: style="color: red"}  
    When the dimensionality increases, the _volume of the space increases so fast_ that the available _data become sparse_. This __sparsity__ is problematic for any method that requires __statistical significance__. In order to obtain a statistically sound and reliable result, the _amount of data needed_ to support the result often _grows exponentially with the dimensionality_. Also, organizing and searching data often relies on detecting areas where objects form groups with similar properties (_clustering_); in high dimensional data, however, all objects appear to be sparse and dissimilar in many ways, which prevents common data organization strategies from being efficient.  

    __Sampling:__{: style="color: red"}  
    The sampling density is proportional to $$N^{1/p}$$, where $$p$$ is the dimension of the input space and $$N$$ is the sample size. Thus, if $$N_1 = 100$$ represents a dense sample for a single input problem, then $$N_{10} = 100^{10}$$ is the sample size required for the same sampling density with $$10$$ inputs. Thus in high dimensions all feasible training samples sparsely populate the input space.  

    [Story on Geometry in high-dimensional spaces](https://marckhoury.github.io/counterintuitive-properties-of-high-dimensional-space/)  


0. **Notes:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents60}  
    * __Complexity__:  
        * __Caching the activations of a NN__:  
        We need to cache the activation vectors of a NN after each layer $$Z^{[l]}$$ because they are required in the backward computation.  
    * __Initializations__:  
        * __Initializing NN__:  
            * Don't initialize the weights to Zero. The symmetry of hidden units results in a similar computation for each hidden unit, making all the rows of the weight matrix to be equal (by induction).  
            * It's OK to initialize the bias term to zero.  
            * Since a neuron takes the sum of $$N$$ inputsXweights, if $$N$$ is large, you want smaller $$w_i$$s. You want to initialize with a __variance__ $$\propto \dfrac{1}{n}$$ (i.e. multiply by $$\dfrac{1}{\sqrt{n}}$$; $$n$$ is the number of weights in *__previous layer__*).  
                This doesnt solve but reduces vanishing/exploding gradient problem because $$z$$ would take a similar distribution.  
                * __Xavier Initialization:__ assumes $$\tanh$$ activation; ^ uses logic above; samples from normal distribution and multiplies by $$\dfrac{1}{\sqrt{n}}$$.  
                * If __ReLU__ activation, it turns out to be better to make variance $$\propto \dfrac{2}{n}$$ instead.  
    * __Training__:  
        * [A Recipe for Training Neural Networks](http://karpathy.github.io/2019/04/25/recipe/)  
        * [Tips for Training Deep Networks](http://rishy.github.io/ml/2017/01/05/how-to-train-your-dnn/)  
        * [Why Train a Model BOTH Generatively and Discriminatively](http://www.chioka.in/why-train-a-model-generatively-and-discriminatively/)  
    * __Feature Importance__:  
        * In linear models, feature importance can be calculated by the scale of the coefficients  
        * In tree-based methods (such as random forest), important features are likely to appear closer to the root of the tree. We can get a feature's importance for random forest by computing the averaging depth at which it appears across all trees in the forest   
    * __Probabilistic Calibration__:  
        * [Plot and Explanation](https://scikit-learn.org/stable/modules/calibration.html)  
        * [Blog on How to do it](http://alondaks.com/2017/12/31/the-importance-of-calibrating-your-deep-model/)  
    * __Complexity in ML__:  
        * __Definitions of the complexity of an object ($$h$$)__:  
            * __Minimum Description Length (MDL)__: the number of bits for specifying an object.  
            * __Order of a Polynomial__  
        * __Definitions of the complexity of a class of objects ($$\mathcal{H}$$)__:  
            * __Entropy__  
            * __VC-dim__  
    * __Gaussian Discriminant Analysis__:  
        * models $P(Y=y \vert X)$ as a logistic function. 
        * is a generative model.
        * can be used to classify points without ever computing an exponential
        * __decision boundary shapes:__  
            * Hyperplane
            * Nonlinear quadric surface (quadric = the isosurface of a quadratic function)
            * The empty set (the classifier always returns the same class)  
        * [Logistic Regression vs LDA? (ESL)](https://web.stanford.edu/~hastie/Papers/ESLII.pdf#page=146)  
    * __Geometry of Gaussian Distributions__:  
        * Multivariate Normal Distribution:  
            * Isotropic:  
                * I.E. Isosurfaces are spheres
                * Covariance Matrix $$\Sigma = \sigma^2 I$$  
                    where $$\sigma^2$$ is the variance of any one feature.  
    * The __Bias Parameter__:  
        * [Role of Bias in a NN](https://stackoverflow.com/questions/2480650/role-of-bias-in-neural-networks)  
    * __When is does an ML problem become a *Research Problem*__:  
        A problem that you are trying to solve using ML becomes a __research problem__ as opposed to those solved by __applied practitioners__ when the only way to learn the problem is to <span>improve the __learning algorithm__ itself</span>{: style="color: purple"}. This happens in two situations:  
        1. You can fit the __training data__ well but cannot improve __generalization error__:  
            This happens when: It is not feasible to gather more data  
        2. You cannot fit the __training data__ well even when you increase the capacity of your models as much as you _"feasibly"_ can  
    * <button>Designing Human-Centered AI</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        ![img](https://cdn.mathpix.com/snip/images/QMFDyvhLtOO4V5sJ5UXNzc5ykwllgkghEmpqncZ0P4Y.original.fullsize.png){: width="100%" hidden=""}    
    * __Bayesian Deep Learning__:  
        <button>List of Topics</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        * Uncertainty in deep learning,
        * Applications of Bayesian deep learning,
        * Probabilistic deep models (such as extensions and application of Bayesian neural networks),
        * Deep probabilistic models (such as hierarchical Bayesian models and their applications),
        * Generative deep models (such as variational autoencoders),
        * Information theory in deep learning,
        * Deep ensemble uncertainty,
        * NTK and Bayesian modelling,
        * Connections between NNs and GPs,
        * Incorporating explicit prior knowledge in deep learning (such as posterior regularisation with logic rules),
        * Approximate inference for Bayesian deep learning (such as variational Bayes / expectation propagation / etc. in Bayesian neural networks),
        * Scalable MCMC inference in Bayesian deep models,
        * Deep recognition models for variational inference (amortised inference),
        * Bayesian deep reinforcement learning,
        * Deep learning with small data,
        * Deep learning in Bayesian modelling,
        * Probabilistic semi-supervised learning techniques,
        * Active learning and Bayesian optimisation for experimental design,
        * Kernel methods in Bayesian deep learning,
        * Implicit inference,
        * Applying non-parametric methods, one-shot learning, and Bayesian deep learning in general.  
        {: hidden=""}  
    * __Learning Problems__:  
        * Counting/Arithmetic  
        * Copying
        * Identity Mapping
        * Pointing (Copying?)  
        * 
    * __Learning Features__:  
        * Higher-Order/k-Order Interactions  
        * Global Dependencies
        * Local Dependencies
        * Self-Similarity
        * Non-Locality ([Non-local Neural Networks (paper!)](https://arxiv.org/pdf/1711.07971.pdf))  
        * Long-Range Dependencies  
        * Memory: Long-Term, Short-Term (working memory)  
            * Associative Retrieval  
        * Mathematical (Symbolic?) Manipulation: Arithmetic?: Counting  
    * __Input Representations__:  
        * Localist Representations  
        * Point Attractors
    <br>


***
***

## Computer Vision
{: #content7}

<!-- 

1. **Edge Detection Filters:**{: style="color: SteelBlue"}{: .bodyContents7 #bodyContents71}  
    * __Sobel Filter:__  
        <p>$$\begin{array}{|c|c|c|}\hline 1 & {0} & {-1} \\ \hline 2 & {0} & {-2} \\ \hline 1 & {0} & {-1} \\ \hline\end{array}$$</p>  
    * __Schorr Filter__:  
        <p>$$\begin{array}{|c|c|c|}\hline 3 & {0} & {-3} \\ \hline 10 & {0} & {-10} \\ \hline 3 & {0} & {-3} \\ \hline\end{array}$$</p>  
            

2. **Aliasing:**{: style="color: SteelBlue"}{: .bodyContents7 #bodyContents72}  
    Aliasing is an effect that causes different signals to become indistinguishable (or aliases of one another) when sampled. It also refers to the distortion or artifact that results when the signal reconstructed from samples is different from the original continuous signal.  

    Aliasing can occur in signals sampled in time, for instance digital audio, and is referred to as __temporal aliasing__. Aliasing can also occur in spatially sampled signals, for instance moiré patterns in digital images. Aliasing in spatially sampled signals is called __spatial aliasing__.  
        -->

<!-- 3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents7 #bodyContents73}  
4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents7 #bodyContents74}  
  -->

***
***

## NLP
{: #content8}

[The Norvig-Chomsky Debate](https://sites.tufts.edu/models/files/2019/04/Norvig.pdf)  
[Modern Deep Learning Techniques Applied to Natural Language Processing (Amazing Resource)](https://nlpoverview.com)  
[Deep Learning for NLP: Advancements & Trends](https://tryolabs.com/blog/2017/12/12/deep-learning-for-nlp-advancements-and-trends-in-2017/?utm_campaign=Revue%20newsletter&utm_medium=Newsletter&utm_source=The%20Wild%20Week%20in%20AI)  


1. **Language Modeling:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents81}  
    __Towards Better Language Modeling (Lec.9 highlight, 38m):__{: style="color: red"}  
    {: #lst-p}
    To improve a _Language Model_:  
    1. __Better Inputs__: 
        Word $$\rightarrow$$ Subword $$\rightarrow$$ Char  
        <button>Slide</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        ![img](/main_files/concepts/2.png){: width="100%" hidden=""}  
        _Subword Language Modeling , Mikolov et al. 2012_  
        _Character-Aware Neural Language Model , Kim et al. 2015_.  
    2. __Better Regularization/Preprocessing__:  
        Similar to computer vision, we can do both Regularization and Preprocessing on the data to increase its relevance to the true distribution.  
        Preprocessing acts as a *__data augmentation__* technique. This allows us to achieve a __Smoother__ distribution, since we are removing more common words and re-enforcing rarer words.  
        _Zoneout, Kruger et al. 2016_  
        _Data Noising as Smoothing, Xie et al. 2016_       
        * *__Regularization__*:  
            * Use Dropout (Zaremba, et al. 2014). 
            * Use Stochastic FeedForward depth (Huang et al. 2016)
            * Use Norm Stabilization (Memisevic 2015)
            ...  
        * *__Preprocessing__*:  
             * Randomly replacing words in a sentence with other words  
             * Use bigram statistics to generate _Kneser-Ney_ inspired replacement (Xie et al. 2016). 
             * Replace a word with __fixed__ drop rate
             * Replace a word with __adaptive__ drop rate, by how rare two words appear together (i.e. "Humpty Dumpty"), and replace by a unigram draw over vocab
             * Replace a word with __adaptive__ drop rate, and draw word from a __proposal distribution__ (i.e. "New York") 
    3. __Better Model__ (+ all above)  


    __Recurrent Neural Networks as Language Models:__{: style="color: red"}  
    {: #lst-p}
    * <button>RNN-LM</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](/main_files/concepts/7.jpg){: hidden=""}  


    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * __The ML-Estimate of $$p(w_i \vert w_{i-1})$$__ $$ = \dfrac{c(w_{i-1}\:, w_i)}{\sum_{w_i} c(w_{i-1}\:, w_i)}$$  
    <br>

    <!-- 2. **:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents82}   -->
            

3. **Neural Text Generation:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents83}
    * __Traditionally__:  
        * Often Auto-regressive language models (ie. seq2seq)
        * These models generate text by sampling words sequentially, with each word conditioned on the previous word
        * Benchmarked on validation perplexity even though this is not a direct measure of the quality of the generated text 
        * The models are typically trained via __maximum likelihood__ and __teacher forcing__  
            > These methods are well-suited to optimizing perplexity but can result in poor sample quality since generating text requires conditioning on sequences of words that may have never been observed at training time  

4. **NLP & DL (R. Sorcher):**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents84}  
    * <button>Common DL-NLP Tasks/Problems in NLP w/ DL</button>{: .showText value="show"
     onclick="showTextPopHide(event);"}
    ![img](/main_files/concepts/1_1.jpg){: hidden=""}  
    * <button>Problems in NLP w/ DL contd</button>{: .showText value="show"
     onclick="showTextPopHide(event);"}
    ![img](/main_files/concepts/2.jpg){: hidden=""}  

5. **Text Classification:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents85}  
    __Word-Window Classification:__{: style="color: red"}  
    {: #lst-p}
    * <button>Classification Setup</button>{: .showText value="show"
     onclick="showTextPopHide(event);"}
    ![img](/main_files/concepts/3.jpg){: hidden=""}  
    * <button>Cross-Entropy and Softmax</button>{: .showText value="show"
     onclick="showTextPopHide(event);"}
    ![img](/main_files/concepts/3_1.jpg){: hidden=""}  
    * <button>Classification over a full dataset</button>{: .showText value="show"
     onclick="showTextPopHide(event);"}
    ![img](/main_files/concepts/4.jpg){: hidden=""}  
    * <button>General ML vs DL Optimization</button>{: .showText value="show"
     onclick="showTextPopHide(event);"}
    ![img](/main_files/concepts/4_1.jpg){: hidden=""}  
    * <button>Window Classification</button>{: .showText value="show"
     onclick="showTextPopHide(event);"}
    ![img](/main_files/concepts/5.jpg){: hidden=""}  
    * <button>Softmax limitations and considerations</button>{: .showText value="show"
     onclick="showTextPopHide(event);"}
    ![img](/main_files/concepts/6.jpg){: hidden=""}  
    * <button>The Max-Margin Loss</button>{: .showText value="show"
     onclick="showTextPopHide(event);"}
    ![img](/main_files/concepts/6_1.jpg){: hidden=""}  

    __CNN Text Classification:__{: style="color: red"}  
    {: #lst-p}
    * <button>The Problem Set-up and the Pooling Layer</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](/main_files/concepts/8.jpg){: hidden=""}  
    * <button>Classification and Tips for Learning</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](/main_files/concepts/8_1.jpg){: hidden=""}  


    * [CNN Text Classification](http://www.wildml.com/2015/11/understanding-convolutional-neural-networks-for-nlp)  
    * [1d CNNs for Time-Sequences](https://blog.goodaudience.com/introduction-to-1d-convolutional-neural-networks-in-keras-for-time-sequences-3a7ff801a2cf)  
    * [LSI document similarity](http://mccormickml.com/2016/11/04/interpreting-lsi-document-similarity/)  
    * [Latent Semantic Analysis (LSA) for Text Classification Tutorial](http://mccormickml.com/2016/03/25/lsa-for-text-classification-tutorial/)  
    * [A Comprehensive Guide to Understand and Implement Text Classification in Python (All Models for Txt Cls. - very useful)](https://www.analyticsvidhya.com/blog/2018/04/a-comprehensive-guide-to-understand-and-implement-text-classification-in-python/)  

    <!-- 6. **:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents86}   -->


7. **Coreference Resolution:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents87}  
    __Coreference Resolution:__ Identify all mentions that refer to the same real world entity.  

    __Applications:__{: style="color: red"}  
    {: #lst-p}
    {: #lst-p}
    * __Full text understanding__:  
        * information extraction, question answering, summarization, ...  
        * “He was born in 1961” (Who?)  
    * __Machine Translation__:  
        * languages have different features for gender, number, dropped pronouns, etc.  
    * __Dialogue Systems__:  
        “Book tickets to see <span>James Bond</span>{: style="color: red"}”  
        “<span>Spectre</span>{: style="color: red"} is playing near you at 2:00 and <span>3:00</span>{: style="color: blue"} today. <span>How many tickets</span>{: style="color: orange"} would you like?”  
        “<span>Two</span>{: style="color: orange"} tickets for the showing at <span>three</span>{: style="color: blue"}”  


    __An approach for Coref-Res in 2 steps:__{: style="color: red"}  
    {: #lst-p}
    {: #lst-p}
    1. __Detect the Mentions__ (easy)  
        “Book tickets to see <span>James Bond</span>{: style="color: gray"}”  
        “<span>Spectre</span>{: style="color: gray"} is playing near you at 2:00 and <span>3:00</span>{: style="color: gray"} today. <span>How many tickets</span>{: style="color: gray"} would you like?”  
        “<span>Two</span>{: style="color: gray"} tickets for the showing at <span>three</span>{: style="color: gray"}”  
    2. __Cluster the Mentions__ (hard)  
        “Book tickets to see <span>James Bond</span>{: style="color: red"}”  
        “<span>Spectre</span>{: style="color: red"} is playing near you at 2:00 and <span>3:00</span>{: style="color: blue"} today. <span>How many tickets</span>{: style="color: orange"} would you like?”  
        “<span>Two</span>{: style="color: orange"} tickets for the showing at <span>three</span>{: style="color: blue"}”  


    __Mention Detection:__{: style="color: red"}  
    __Mention:__ span of text referring to some entity.  

    __Types of Mention:__  
    {: #lst-p}
    1. __Pronouns__  
        "I", "your", "it", "she", "him"  
    2. __Named Entities__  
        People, places, etc.  
    3. __Noun Phrases__  
        "a dog", "the big fluffy cat stuck in the tree"  

    __Detection:__  
    Use other NLP systems for the detection task:  
    {: #lst-p}
    1. Pronouns: __POS-Tagger__  
    2. Named Entities: __NER__  
    3. Noun Phrases: __(Constituency) Parser__  

    __Problem with Detection - Extra/bad mentions:__  
    Notice that the systems above will overmatch on possible mentions that don't have a concrete entity that they refer to: e.g. [It] is sunny, [Every student], [No student], [The best donut in the world], [100 miles].  

    __Dealing with bad mentions:__  
    {: #lst-p}
    * Train a classifier to filter out spurious mentions
    * (more commonly) keep all mentions as “candidate mentions”  
        * After your coreference system is done running discard all singleton mentions (i.e., ones that have not been marked as coreference with anything else)  

    [Continue Lecture (CS224N)](https://www.youtube.com/watch?v=i19m4GzBhfc&list=PLoROMvodv4rOhcuXMZkNm7j3fVwBBY42z&index=17&t=1320s) 
    <br>


8. **Word Embeddings:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents88}  
    __Word Vectors:__{: style="color: red"}  
    {: #lst-p}
    * <button>Learning Word Vectors and Word2Vec</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](/main_files/concepts/11.jpg){: hidden=""}  
    * <button>Word Vectors and Polysemy</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](/main_files/concepts/11_1.jpg){: hidden=""}  


    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * __Categorization__ is a method for Evaluating w2v Embeddings by creating categorize by clustering, then measuring the purity of the clusters  


__Notes:__{: style="color: red"}  
{: #lst-p}
* [Ilya Sutskever Pubs/Vids](http://www.cs.toronto.edu/~ilya/pubs/)  
* Can all NLP tasks be cast as QA problems?!  
* [Survey of the State of the Art in Natural Language Generation](https://arxiv.org/pdf/1703.09902.pdf)  


<!-- 
***
***

## Physics
{: #content9} 
-->

<!-- 
1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents91}  
2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents92}  
3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents93}  
-->

***
***

<!-- ## Algorithms
{: #content10}

1. **DFS:**{: style="color: SteelBlue"}{: .bodyContents10 #bodyContents101}  
    __Applications__:  
    * Finding (strongly or not) connected components.
    * Topological sorting.
    * Finding the bridges of a graph.
    * Generating words in order to plot the limit set of a group.
    * Finding strongly connected components.
    * Planarity testing.
    * Solving puzzles with only one solution, such as mazes. (DFS can be adapted to find all solutions to a maze by only including nodes on the current path in the visited set.)
    * Maze generation may use a randomized depth-first search.
    * Finding biconnectivity in graphs.  

    __Code:__  
    ```python
    # RECURSIVE
    def dfs(n, visit, graph, s):
        # print('n: ', n);print('visit: ', visit);print('graph: ', graph);print('s: ', s)# print("HERE: ", len(visit), len(graph))
        visit[s] = 1
        print(s)
        for v in graph[s]:
            if not visit[v]:
                dfs(n, visit, graph, v)
    ```   

    ```python
    # Pseudo-Code
    procedure DFS-iterative(G,v):
        let S be a stack
        S.push(v)
        while S is not empty
            v = S.pop()
            if v is not labeled as discovered:
                label v as discovered
                for all edges from v to w in G.adjacentEdges(v) do 
                    S.push(w)
    ```
        

2. **Complexity of common Data-Structures:**{: style="color: SteelBlue"}{: .bodyContents10 #bodyContents102}  
    :   ![img](/main_files/concepts/bigo.png){: width="100%"}  

3. **Data-Structures:**{: style="color: SteelBlue"}{: .bodyContents10 #bodyContents103}  
    * __Stack__:  
        * __Implementations__:  
            (1) Arrays  $$\:\:$$ (2) Linked-Lists  
        

4. **Maps and Networks - The Four Color Problem:**{: style="color: SteelBlue"}{: .bodyContents10 #bodyContents104}  
* All maps can be colored with only 4 colors
* All maps are networks (__planar graphs__) but not all networks (non-planar) are maps

5. **Recurrence (complexity):**{: style="color: SteelBlue"}{: .bodyContents10 #bodyContents105}  
    * __Master Theorem__:  
    Given the Recurrence:  
    $$T(n) = aT(n/b) + cn^k,\:\: T(1) = c$$,  
    where a, b, c, and k are all constants. solves to:  
    $$T(n) \in \Theta(n^k)$$ if $$a < b^k$$  
    $$T(n) \in \Theta(n^k \log{n})$$ if $$a = b^k$$  
    $$T(n) \in \Theta(n^{\log_b(a)})$$ if $$a > b^k$$  
    * <button>General Master Theorem</button>{: .showText value="show"
     onclick="showTextPopHide(event);"}
    ![img](/main_files/concepts/general_master_thm.jpg){: hidden=""}  
    * __Recursion Out-of-form__:  
    $$T(n) = T(n − 1) + c^n$$, where $$c$$ is a constant; solves to:  
    Expands to: $$T(n) = \sum_{i=0}^n c^i$$  
    Where the solution is $$\Theta(1), \Theta(n), or \Theta(c^n)$$, depending on if $$c < 1, c = 1, or c > 1$$  
    * __The height of the binary recursion tree__:  
    Given $$T(n) = aT(n^{1/k}) + f(n)$$, the height $$h$$ is the solution to:  
    $$n^{1/{k^h}} = 2$$  
    * __Solution from Recursion Tree__:  
    The solution of a recursion is defined as:  
    1. The number of nodes in the tree: $$= 2^{h+1}-1$$, where $$h$$ is the height of the tree  
    2. Multiplied by the amount of work done at every node: $$f(n)$$     

6. **Proofs for Algorithms:**{: style="color: SteelBlue"}{: .bodyContents10 #bodyContents106}  
    * __Strong Induction:__ e.g. dijkstras

7. **Data Structures:**{: style="color: SteelBlue"}{: .bodyContents10 #bodyContents107}  
    * __Array__  
    * __Stack (LIFO)__  
    * __Queue (FIFO)__  
    * __(min/max) Heap__  
    * __Hash Table__  
    * __Binary Tree__  
    * __(single/double) Linked List__  


    * __Array__:  
    * __Stack__:  
        * __Operations O(1)__:  
            1. Push
            2. Pop
            3. Top
            4. IsEmpty
        * __Implementations__:  
            1. (cyclic) Array: w/ modular indices
            2. (doubly) Linked List
    * __Queue__:  
        * __Operations O(1)__:  
            1. Enqueue
            2. Dequeue
            3. Front
            4. IsEmpty
        * __Implementations__:  
            1. (cyclic) Array: w/ modular indices
            2. (doubly) Linked List
    * __(min/max) Heap__:  
    * __Hash Table__:  
        * __Implementations__:  
            1. Array of Linked Lists (access=O(1))
            2. Balanced BST (access=O(log(n)))
    * __Binary Tree__:  
    * __(single/double) Linked List__:  

    

    8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents10 #bodyContents108}  
    :

0. **Notes:**{: style="color: SteelBlue"}{: .bodyContents10 #bodyContents100}  
    * __Matrices Trick:__ matrices ($$A,\  B$$) can be put in a larger matrix (to create one big matrix) for efficient computation/multiplication:  
        $$\begin{bmatrix}
            A & 0 \\
            0 & B \\
        \end{bmatrix}$$  
    * [Computable Functions and Turing Machines](https://marckhoury.github.io/on-computable-functions/)   

***
***
 -->

<!-- ## Misc.
{: #content11}

1. **Philosophy:**{: style="color: SteelBlue"}{: .bodyContents11 #bodyContents111}  
    __Occam's Razor:__  Suppose there exist two explanations for an occurrence. In this case the one that requires the least speculation is usually better.  
    Another way of saying it is that the more assumptions you have to make, the more unlikely an explanation.  
    > It is neither _precise_ nor _self evident_.    -->

<!-- 2. **Misc:**{: style="color: SteelBlue"}{: .bodyContents11 #bodyContents112}  
3. **Misc:**{: style="color: SteelBlue"}{: .bodyContents11 #bodyContents113}   -->

[^1]: Remember that the chain-rule will multiply the local gradient (of sigmoid) with the whole object. Thus, when gradient is small/zero, it will "kill" the gradient $$\rightarrow$$ no signal will flow through the neuron to its weights or to its data.  


__Resources:__{: style="color: red"}  
{: #lst-p}
* [Reinforcement Learning Course Lectures UCL](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html)  
* [Advanced Robotics Lecture CS287 Berk](https://people.eecs.berkeley.edu/~pabbeel/cs287-fa15/)
* [Full-Stack DL (productionization of DL) Bootcamp Peter Abbeel](https://fullstackdeeplearning.com/march2019)
* [Deep Unsupervised Learning CS294 Berk](https://sites.google.com/view/berkeley-cs294-158-sp19/home)
* [Deep RL WS1](https://sites.google.com/view/deep-rl-bootcamp/lectures)
* [Deep RL WS2](https://sites.google.com/view/deep-rl-workshop-nips-2018/home)
* [Deep RL Lec CS294 Berk](http://rail.eecs.berkeley.edu/deeprlcourse/)
* [DeepLearning Book (dive into dl) Berkeley](https://en.d2l.ai/d2l-en.pdf)
    * [d2l course website](https://www.d2l.ai/)  
* [Mathematics of DL](https://www.youtube.com/watch?v=Mdp9uC3gXUU)  
* [Deep Learning Linear Algebra](https://jhui.github.io/2017/01/05/Deep-learning-linear-algebra/)  
* [Intro to Causal Inference (do-Calculus)](https://www.inference.vc/untitled/)  
* [DL and Physics](https://www.technologyreview.com/s/602344/the-extraordinary-link-between-deep-neural-networks-and-the-nature-of-the-universe/)  
* [EE227C: Convex Optimization and Approximation](https://ee227c.github.io/)  
* [Boyd Cvx-Opt](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf)  
* [Tibshirani Cvx-Opt](http://www.stat.cmu.edu/~ryantibs/convexopt/)  
* [Efficient DL](https://docs.google.com/document/d/1w_fcJKNyXUMhMS328w7qiOr-P1dSOHALuBnOjEbiZYA/edit)  
* [Probabilistic Graphical Models CS-708 (CMU!)](https://sailinglab.github.io/pgm-spring-2019/)  
* [Deep learning courses at UC Berkeley!](https://berkeley-deep-learning.github.io)  
* [CS182/282A Designing, Visualizing and Understanding Deep Neural Networks Spring 2019](https://bcourses.berkeley.edu/courses/1478831/pages/cs182-slash-282a-designing-visualizing-and-understanding-deep-neural-networks-spring-2019)  
* [Quantum Computing Learning Resource (Blog!)](https://quantum.country/qcvc)  