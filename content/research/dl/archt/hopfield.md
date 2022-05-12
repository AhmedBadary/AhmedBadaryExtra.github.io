---
layout: NotesPage
title: Hopfield Networks
permalink: /work_files/research/dl/archits/hopfield
prevLink: /work_files/research/dl.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Hopfield Networks](#content1)
  {: .TOC1}
  <!-- * [SECOND](#content2)
  {: .TOC2} -->
</div>

***
***


[Hopfield Networks Exercises](https://neuronaldynamics-exercises.readthedocs.io/en/latest/exercises/hopfield-network.html)  
[Hopfield Networks Example and Code (medium)](https://medium.com/100-days-of-algorithms/day-80-hopfield-net-5f18d3dbf6e6)  
[INTRODUCTION TO HOPFIELD NEURAL NETWORKS (blog)](https://www.doc.ic.ac.uk/~sd4215/hopfield.html)  
[The Hopfield Model (paper!)](http://page.mi.fu-berlin.de/rojas/neural/chapter/K13.pdf)  
[Hopfield Network Demo (github)](https://github.com/drussellmrichie/hopfield_network)  
[Hopfield Networks Tutorial + Code (blog)](http://koaning.io/intro-to-hopfield-networks.html)  
[Why learn Hopfield Nets and why they work (blog)](https://towardsdatascience.com/hopfield-networks-are-useless-heres-why-you-should-learn-them-f0930ebeadcd)  
[Hopfield Networks (Quantum ML Book)](https://www.sciencedirect.com/topics/computer-science/hopfield-network)  
* [A Tutorial on Energy-Based Learning (LeCun)](http://yann.lecun.com/exdb/publis/pdf/lecun-06.pdf)  
* [Hopfield Nets (Hinton Lecs)](https://www.youtube.com/watch?v=DS6k0PhBjpI&list=PLoRl3Ht4JOcdU872GhiYWf6jwrk_SNhz9&index=50&t=0s)  
* [Hopfield Nets (CMU Lecs!)](https://www.youtube.com/watch?v=yl8znINLXdg)  
* [Hopfield Nets - Proof of Decreasing Energy (vid)](https://www.youtube.com/watch?v=gfPUWwBkXZY)  
* [On the Convergence Properties of the Hopfield Model (paper)](http://www.paradise.caltech.edu/CNS188/bruck90-conv.pdf)  




## Hopfield Networks
{: #content1}

1. **Hopfield Networks:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    __Hopfield Networks__ are a form of _recurrent_ artificial neural networks that serve as <span>content-addressable ("associative") memory</span>{: style="color: purple"} systems with binary threshold nodes.  

    They are __energy models__ i.e. their properties derive from a global __energy function__.  
    * A Hopfield net is composed of binary threshold units with recurrent connections between them.  

    __Motivation:__{: style="color: red"}  
    __Recurrent networks of *non-linear* units__ are generally very hard to analyze.  
    They can behave in many different ways:  
    {: #lst-p}
    * Settle to a stable state
    * Oscillate
    * Follow chaotic trajectories that cannot be predicted far into the future  

    __Main Idea:__{: style="color: red"}  
    _John Hopfield_ realized that <span>if the __connections are__ *__symmetric__*, there is a __global *energy* function__</span>{: style="color: goldenrod"}:  
    {: #lst-p}
    * Each binary "configuration" of the whole network has an energy.  
        * __Binary Configuration:__ is an assignment of binary values to each neuron in the network.  
            Every neuron has a particular binary value in a configuration.  
    * The <span>binary threshold decision rule</span>{: style="color: purple"} causes the network to <span>settle to a __minimum__ of this energy function</span>{: style="color: purple"}.  
        The rule causes the network to go downhill in energy, and by repeatedly applying the rule, the network will end-up in an energy minimum.  


    __The Energy Function:__{: style="color: red"}  
    {: #lst-p}
    * The global energy is the sum of many contributions:  
        <p>$$E=-\sum_{i} s_{i} b_{i}-\sum_{i< j} s_{i} s_{j} w_{i j}$$</p>  
        * Each contribution depends on:  
            * *One* __connection weight__: $$w_{i j}$$  
                A *__symmetric__* connection between two neurons; thus, have the following restrictions:  
                * $$w_{i i}=0, \forall i$$ (no unit has a connection with itself)  
                * $$w_{i j}=w_{j i}, \forall i, j$$ (connections are symmetric)  
            and 
            * The __binary states__ of *two* __neurons__: $$s_{i}$$ and $$s_{j}$$
                where $$s_{j} \in \{-1, 1\}$$ (or $$\in \{0, 1\}$$) is the state of unit $$j$$, and $$\theta_{j}$$ is the threshold of unit $$j$$.  
        * To make up the following terms:  
            * The __quadratic term__ $$s_{i} s_{j} \in \{-1, 1\}$$, involving the states of *__two__* units and  
            * The __bias term__ $$s_i b_i \in \{-\theta, \theta\}$$, involving the states of individual units.  
    * This simple *__quadratic__* energy function makes it possible for each unit to compute __locally__ how it's state affects the global energy:  
        The __Energy Gap__ is the difference in the global energy of the whole configuration depending on whether $$i$$ is on:  
        <p>$$\begin{align}
            \text{Energy Gap} &= \Delta E_{i} \\
              &= E\left(s_{i}=0\right)-E\left(s_{i}=1\right) \\
              &= b_{i}+\sum_{j} s_{j} w_{i j} 
            \end{align}
            $$</p>  
        i.e. the difference between the __energy when $$i$$ is *on*__ and the __energy when $$i$$ is *off*__.  
        * __The Energy Gap and the Binary Threshold Decision Rule:__  
            * This difference (__energy gap__) is exactly what the __binary threshold decision rule__ computes.  
            * <span>The Binary Decision Rule is the</span>{: style="color: goldenrod"} __*derivative* of the energy gap wrt the state of the $$i$$-th unit $$s_i$$__{: style="color: goldenrod"}.  

    __Settling to an Energy Minimum:__{: style="color: red"}  
    To find an energy minimum in this net:  
    {: #lst-p}
    * Start from a _random state_, then  
    * Update units <span>one at a time</span>{: style="color: purple"} in _random_ order:  
        * Update each unit to whichever of its two states gives the lowest global energy.  
            i.e. use <span>__binary threshold units__</span>{: style="color: goldenrod"}.  

    __A Deeper Energy Minimum:__{: style="color: red"}  
    The net has two triangles in which the three units mostly support each other.  
    {: #lst-p}
    - Each triangle mostly hates the other triangle.  
    The triangle on the left differs from the one on the right by having a weight of $$2$$ where the other one has a weight of $$3$$.  
    - So turning on the units in the triangle on the right gives the deepest minimum.  

    __Sequential Updating - Justification:__{: style="color: red"}  
    {: #lst-p}
    * If units make __simultaneous__ decisions the energy could go up.  
    * With simultaneous parallel updating we can get *__oscillations__*.  
        - They always have a __period__ of $$2$$ (bi-phasic oscillations).  
    * If the updates occur in parallel but with random timing, the oscillations are usually destroyed.  

    __Using Energy Models (with binary threshold rule) for Storing Memories:__  
    {: #lst-p}
    * _Hopfield (1982)_ proposed that <span>memories could be __energy minima__ of a neural net</span>{: style="color: goldenrod"} (w/ symmetric weights).  
        - <span>The __binary threshold decision rule__ can then be used to _"clean up"_ __incomplete__ or __corrupted__ memories</span>{: style="color: purple"}.  
            Transforms _partial_ memories to _full_ memories.   
    * The idea of memories as energy minima was proposed by _I. A. Richards (1924)_ in "Principles of Literary Criticism".  
    * Using energy minima to represent memories gives a <span>__content-addressable ("associative") memory__</span>{: style="color: purple"}:  
        - An item can be accessed by just knowing part of its content.  
            - This was really amazing in the year 16 BG (Before Google).  
        - It is robust against hardware damage. 
        - It's like reconstructing a dinosaur from a few bones.  
            Because you have an idea about how the bones are meant to fit together.  


    __Storing memories in a Hopfield net:__{: style="color: red"}  
    {: #lst-p}
    * If we use activities of $$1$$ and $$-1$$ we can store a binary state vector by incrementing the weight between any two units by the product of their activities.  
        <p>$$\Delta w_{i j}=s_{i} s_{j}$$</p>   
        * This is a very simple rule that is __*not* error-driven__ (i.e. does not learn by correcting errors).  
            That is both its strength and its weakness:  
            * It is an __online__ rule  
            * It is not very efficient to store things  
        * We treat __biases__ as weights from a __*permanently on* unit__.    
    * With states of $$0$$ and $$1$$ the rule is slightly more complicated:  
        <p>$$\Delta w_{i j}=4\left(s_{i}-\frac{1}{2}\right)\left(s_{j}-\frac{1}{2}\right)$$</p>  



    __Summary - Big Ideas of Hopfield Networks:__{: style="color: red"}  
    {: #lst-p}
    * __Idea #1__: we can find a local energy minimum by using a network of symmetrically connected binary threshold units.  
    * __Idea #2__: these local energy minima might correspond to memories.  


    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * They were responsible for resurgence of interest in Neural Networks in 1980s
    * They can be used to store memories as distributed patterns of activity
    * The constraint that weights are symmetric guarantees that the energy function decreases monotonically while following the activation rules  
    * The Hopfield Network is a *__non-linear dynamical system__* that converges to an *__attractor__*.  
    * A Hopfield net the size of a brain (connectivity patterns are quite diff, of course) could store a memory per second for 450 years.  
    <br>


2. **Structure:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    The __Hopfield Network__ is formally described as a __complete Undirected graph__{: style="color: goldenrod"} $$G=\langle V, f\rangle,$$ where $$V$$ is a set of McCulloch-Pitts neurons and $$f : V^{2} \rightarrow \mathbb{R}$$ is a function that links pairs of units to a real value, the connectivity weight.  
    {: #lst-p}
    * The __Units__:  
        The units in a Hopfield Net are __binary threshold units__,  
        i.e. the <span>units only take on __two different values__ for their states</span>{: style="color: purple"} and the <span>value is determined by whether or not the units' __input__ *__exceeds__* __their threshold__</span>{: style="color: purple"}.  
    * The __States:__  
        The state $$s_i$$ for unit $$i$$ take on values of $$1$$ or $$-1$$,  
        i.e. $$s_i \in \{-1, 1\}$$.  
    * The __Weights:__  
        Every pair of units $$i$$ and $$j$$ in a Hopfield network has a connection that is described by the __connectivity weight__ $$w_{i j}$$.   
        * __Symmetric Connections (weights)__:  
            * The connections in a Hopfield net are constrained to be symmetric by making the following restrictions:  
                * $$w_{i i}=0, \forall i$$ (no unit has a connection with itself)  
                * $$w_{i j}=w_{j i}, \forall i, j$$ (connections are symmetric)  
            * The <span>constraint that weights are *__symmetric__* guarantees that the __energy function decreases monotonically__ while following the activation rules</span>{: style="color: purple"}.  
                A network with __*asymmetric* weights__ may exhibit some periodic or chaotic behaviour; however, Hopfield found that this behavior is confined to relatively small parts of the phase space and does not impair the network's ability to act as a content-addressable associative memory system.  



3. **Update Rule:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    Updating one unit (node in the graph simulating the artificial neuron) in the Hopfield network is performed using the following rule:  
    <p>$$s_{i} \leftarrow\left\{\begin{array}{ll}{+1} & {\text { if } \sum_{j} w_{i j} s_{j} \geq \theta_{i}} \\ {-1} & {\text { otherwise }}\end{array}\right.$$</p>  

    Updates in the Hopfield network can be performed in two different ways:  
    {: #lst-p}
    * __Asynchronous:__ Only one unit is updated at a time. This unit can be picked at random, or a pre-defined order can be imposed from the very beginning.  
    * __Synchronous:__ All units are updated at the same time. This requires a central clock to the system in order to maintain synchronization.  
        This method is viewed by some as less realistic, based on an absence of observed global clock influencing analogous biological or physical systems of interest.  

    __Neural Attraction and Repulsion (in state-space):__{: style="color: red"}  
    Neurons "attract or repel each other" in state-space.  
    The weight between two units has a powerful impact upon the values of the neurons. Consider the connection weight $$w_{ij}$$ between two neurons $$i$$ and $$j$$.  
    If $$w_{{ij}}>0$$, the updating rule implies that:  
    {: #lst-p}
    * when $$s_{j}=1,$$ the contribution of $$j$$ in the weighted sum is positive. Thus, $$s_{i}$$ is pulled by $$j$$ towards its value $$s_{i}=1$$
    * when $$s_{j}=-1,$$ the contribution of $$j$$ in the weighted sum is negative. Then again, $$s_{i}$$ is pushed by $$j$$ towards its value $$s_{i}=-1$$  
    
    Thus, the __values of neurons $$i$$ and $$j$$__ will <span>__converge__ if the weight between them is *positive*</span>{: style="color: purple"}.  
    Similarly, they will <span>__diverge__ if the weight is *negative*</span>{: style="color: purple"}.  
    <br>

4. **Energy:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    Hopfield nets have a scalar value associated with each state of the network, referred to as the __"energy", $$E$$,__ of the network, where:  
    <p>$$E=-\frac{1}{2} \sum_{i, j} w_{i j} s_{i} s_{j}+\sum_{i} \theta_{i} s_{i}$$</p>  
    <button>Energy Landscape of Hopfield Net</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/VgVFJGoT4ogbRvkb1SO-HbUS6i0M94Xte6gIgcYJUbw.original.fullsize.png){: width="100%" hidden=""}  
    This quantity is called *__"energy"__* because it either decreases or stays the same upon network units being updated.  
    Furthermore, under repeated updating the network will eventually converge to a state which is a local minimum in the energy function.  
    Thus, <span>if a state is a __*local minimum* in the energy function__ it is a __*stable state* for the network__</span>{: style="color: purple"}.  
    
    __Relation to Ising Models:__{: style="color: red"}  
    Note that this energy function belongs to a general class of models in physics under the name of [__Ising models__](https://en.wikipedia.org/wiki/Ising_model).  
    These in turn are a special case of [__Markov Random Fields (MRFs)__](https://en.wikipedia.org/wiki/Markov_random_field), since the associated probability measure, the __Gibbs measure__, has the *__Markov property__*.  
    <br>

44. **Initialization and Running:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents144}  
    __Initialization__ of the Hopfield Networks is done by <span>setting the values of the units to the desired __start pattern__</span>{: style="color: purple"}.  
    Repeated updates are then performed until the network converges to an __attractor pattern__.  
    <br>

55. **Convergence:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents155}  
    The Hopfield Network converges to an __attractor pattern__ describing a stable state of the network (as a non-linear dynamical systems).  
    
    __Convergence__ is generally __assured__, as Hopfield proved that the attractors of this nonlinear dynamical system are <span>stable</span>{: style="color: goldenrod"}, <span>non-periodic</span>{: style="color: goldenrod"} and <span>non-chaotic</span>{: style="color: goldenrod"} as in some other systems.  

    Therefore, in the context of Hopfield Networks, an __attractor pattern__ is a final *__stable state__*, a pattern that cannot change any value within it under updating.  
    <br>


66. **Training:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents166}  
    * Training a Hopfield net involves __*lowering the energy* of states that the net should "remember"__.  
    * This allows the net to serve as a __content addressable memory system__, 
        I.E. the network will converge to a "remembered" state if it is given only part of the state.  
    * The net can be used to recover from a distorted input to the trained state that is most similar to that input.  
        This is called __associative memory__ because it recovers memories on the basis of similarity.  
    * Thus, the network is properly trained when the energy of states which the network should remember are local minima.  
    * Note that, in contrast to __Perceptron training__, the thresholds of the neurons are never updated.  
    <br>


5. **Learning Rules:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  
    There are various different learning rules that can be used to store information in the memory of the Hopfield Network.  

    __Desirable Properties:__{: style="color: red"}  
    {: #lst-p}
    * __Local:__ A learning rule is _local_ if each weight is updated using information available to neurons on either side of the connection that is associated with that particular weight.  
    * __Incremental:__ New patterns can be learned without using information from the old patterns that have been also used for training.  
        That is, when a new pattern is used for training, the new values for the weights only depend on the old values and on the new pattern.  

    These properties are desirable, since a learning rule satisfying them is more biologically plausible.  
    > For example, since the human brain is always learning new concepts, one can reason that human learning is incremental. A learning system that were not incremental would generally be trained only once, with a huge batch of training data.  

    __Hebbian Learning Rule:__{: style="color: red"}  
    The Hebbian rule is both __local__ and __incremental__.  
    For the Hopfield Networks, it is implemented in the following manner, when learning $$n$$ binary patterns:  
    <p>$$w_{i j}=\frac{1}{n} \sum_{\mu=1}^{n} \epsilon_{i}^{\mu} \epsilon_{j}^{\mu}$$</p>  
    where $$\epsilon_{i}^{\mu}$$ represents bit $$i$$ from pattern $$\mu$$.  

    \- If the bits corresponding to neurons $$i$$ and $$j$$ are equal in pattern $$\mu,$$ then the product $$\epsilon_{i}^{\mu} \epsilon_{j}^{\mu}$$ will be positive.  
    This would, in turn, have a positive effect on the weight $$w_{i j}$$ and the values of $$i$$ and $$j$$ will tend to become equal.  
    \- The opposite happens if the bits corresponding to neurons $$i$$ and $$j$$ are different.  

    __The Storkey Learning Rule:__{: style="color: red"}  
    This rule was introduced by _Amos Storkey (1997)_ and is both __local__ and __incremental__.  
    The weight matrix of an attractor neural network is said to follow the Storkey learning rule if it obeys:  
    <p>$$w_{i j}^{\nu}=w_{i j}^{\nu-1}+\frac{1}{n} \epsilon_{i}^{\nu} \epsilon_{j}^{\nu}-\frac{1}{n} \epsilon_{i}^{\nu} h_{j i}^{\nu}-\frac{1}{n} \epsilon_{j}^{\nu} h_{i j}^{\nu}$$</p>  
    where $$h_{i j}^{\nu}=\sum_{k=1}^{n} \sum_{i \neq k \neq j}^{n} w_{i k}^{\nu-1} \epsilon_{k}^{\nu}$$ is a form of __local field__ at neuron $$i$$.  

    This learning rule is __local__, since the <span>synapses take into account only neurons at their sides</span>{: style="color: purple"}.  


    __Storkey vs Hebbian Learning Rules:__  
    Storkey showed that a Hopfield network trained using this rule has a __greater capacity__ than a corresponding network trained using the Hebbian rule.  
    The Storkey rule makes use of more information from the patterns and weights than the generalized Hebbian rule, due to the __effect of the *local field*__.  
    <br>

6. **Spurious Patterns:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}  
    * Patterns that the network uses for training (called __retrieval states__) become *__attractors__* of the system.  
    * Repeated updates would eventually lead to convergence to one of the retrieval states.  
    * However, sometimes the network will converge to spurious patterns (different from the training patterns).  
    * __Spurious Patterns__ arise due to *__spurious minima__*.  
        The energy in these spurious patterns is also a local minimum:  
        * For each stored pattern $$x,$$ the negation $$-x$$ is also a spurious pattern.  
        * A spurious state can also be a linear combination of an odd number of retrieval states. For example, when using $$3$$ patterns $$\mu_{1}, \mu_{2}, \mu_{3},$$ one can get the following spurious state:  
        <p>$$\epsilon_{i}^{\operatorname{mix}}=\pm \operatorname{sgn}\left( \pm \epsilon_{i}^{\mu_{1}} \pm \epsilon_{i}^{\mu_{2}} \pm \epsilon_{i}^{\mu_{3}}\right)$$</p>  
    * Spurious patterns that have an *__even__* __number of states__ cannot exist, since they might sum up to zero.  

    * Spurious Patterns (memories) occur when two nearby energy minima combine to make a new minimum in the wrong place.  
    * Physicists, in trying to increase the capacity of Hopfield nets, rediscovered the __Perceptron convergence procedure__.  
    <br>

7. **Capacity:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}  
    The Network capacity of the Hopfield network model is determined by neuron amounts and connections within a given network. Therefore, the number of memories that are able to be stored is dependent on neurons and connections.  
    
    __Capacity:__  
    {: #lst-p}
    * It was shown that the recall accuracy between vectors and nodes was $$0.138$$ (approximately $$138$$ vectors can be recalled from storage for every $$1000$$ nodes) _(Hertz et al. 1991)_.  
    * Using __Hopfield's storage rule__ the capacity of a totally connected net with $$N$$ units is only about $$0.15N$$ memories:  
        * At $$N$$ bits per memory the __total information stored__ is only $$0.15 N^{2}$$ bits.  
        * This does not make efficient use of the bits required to store the weights.  
        * It <span>depends on a constant $$0.15$$</span>{: style="color: purple"} 
    * __Capacity Requirements for Efficient Storage__: 
        * The net has $$N^{2}$$ weights and biases.  
        * After storing $$M$$ memories, each connection weight has an integer value in the range $$[-M, M]$$.  
        * So the __number of bits required to *Efficiently* store the weights and biases__ is:  
            <p>$$ N^{2} \log (2 M+1)$$</p>  
        * It <span>scales __logarithmically__ with the number of stored memories $$M$$</span>{: style="color: purple"}.  

    __Effects of Limited Capacity:__  
    {: #lst-p}
    * Since the capacity of Hopfield Nets is limited to $$\approx 0.15N$$, it is evident that many mistakes will occur if one tries to store a large number of vectors.  
        When the Hopfield model does not recall the right pattern, it is possible that an intrusion has taken place, since semantically related items tend to confuse the individual, and recollection of the wrong pattern occurs.  
        Therefore, the Hopfield network model is shown to confuse one stored item with that of another upon retrieval.  
    * Perfect recalls and high capacity, $$>0.14$$, can be loaded in the network by __Storkey learning method__.  
        Ulterior models inspired by the Hopfield network were later devised to raise the storage limit and reduce the retrieval error rate, with some being capable of one-shot learning.  
        * [A study of retrieval algorithms of sparse messages in networks of neural cliques](https://hal.archives-ouvertes.fr/hal-01058303/)  

    __Spurious Minima Limit the Capacity:__{: style="color: red"}  
    {: #lst-p}
    * Each time we memorize a configuration, we hope to create a new energy minimum.  
    * The problem is if <span>two nearby minima *__merge__* to create a minimum at an intermediate location</span>{: style="color: purple"}[^1]:  
        ![img](https://cdn.mathpix.com/snip/images/UL_iey6sV1ZUu36LhhJrMDAivSzfUaZMyuxNMc2Y8BE.original.fullsize.png){: width="60%"}  
        * Then we would get a blend of them rather than individual memories.  
        * The __Merging of Nearby Minima__ limits the capacity of a Hopfield Net.  


    __Avoiding Spurious Minima by Unlearning:__{: style="color: red"}  
    __Unlearning__ is a strategy proposed by _Hopfield, Feinstein and Palmer_ to avoid spurious minima.  
    It involves applying the opposite of the storage rule of the binary state the network settles to.  
    
    __Strategy:__  
    {: #lst-p}
    * Let the net settle from a random initial state and then do __Unlearning__.  
        Whatever binary state it settles to, apply the opposite of the storage rule.  
        Starting from _red_ merged minimum, doing unlearning will produce the two separate minima:  
        ![img](https://cdn.mathpix.com/snip/images/PNO7sSTFKv3MGDiAE5jxf3nTr4h7CBCNGS2rtI3erxA.original.fullsize.png){: width="40%"}  
    * This will get rid of deep, spurious minima and increase memory capacity.    
    * The strategy was shown to work but with no good analysis.  

    __Unlearning and Biological Dreaming:__  
    The question of why do we dream/what is the function of dreaming is a long standing question:  
    {: #lst-p}
    * When dreaming, the state of the brain is extremely similar to the state of the brain when its awake; except its not driven by real input, rather, its driven by a relay station.  
    * We dream for several hours a day, yet we actually don't remember most if not all of our dreams at all.  

    Crick and Mitchison proposed unlearning as a model of what dreams are for:  
    {: #lst-p}
    * During the day, we store a lot of things and get spurious minima.  
    * At night, we put the network (brain) in a random state, settle to a minimum, and then __unlearn__ what we settled to.  
    * The function of dreams is to get rid of those spurious minima.  
    * That's why we don't remember them, even though we dream for many hours (unless we wake up during the dream).  
        I.E. __We don't *store* our dreams__{: style="color: goldenrod"}.  
    
    __Optimal Amount of Unlearning:__  
    From a mathematical pov, we want to derive exactly how much unlearning we need to do.  
    Unlearning is part of the process of fitting a model to data, and doing maximum likelihood fitting of that model, then unlearning should automatically come out of fitting the model AND the amount of unlearning needed to be done.   
    Thus, the solution is to <span>derive unlearning as the right way to minimize some cost function</span>{: style="color: purple"}, where the cost function is "_how well your network models the data that you saw during the day_".  


    __The Maximal Capacity of a given network architecture, over all possible learning rules:__{: style="color: red"}  
    _Elizabeth Gardner_ showed that the capacity of _fully connected networks_ of _binary neurons_ with _dense patterns_ [__scales as $$2N$$__](https://pdfs.semanticscholar.org/7346/d681807bf0852695caa42dbecae5265b360a.pdf), a storage capacity which is much larger than the one of the Hopfield model.  
    __Learning Rules that are able to saturate the Gardner Bound:__  
    A simple learning rule that is guaranteed to achieve this bound is the __Perceptron Learning Algorithm (PLA)__ <span>applied to each neuron independently</span>{: style="color: purple"}.  
    However, unlike the rule used in the Hopfield model, PLA is a *__supervised__* rule that needs an explicit “error signal” in order to achieve the Gardner bound.  

    __Increasing the Capacity of Hopfield Networks:__{: style="color: red"}  
    Elizabeth Gardner showed that there was a much better storage rule that uses the full capacity of the weights:  
    {: #lst-p}
    * Instead of trying to store vectors in _one shot_, <span>cycle through the training set many times</span>{: style="color: purple"}.  
    * Use the __Perceptron Learning Algorithm (PLA)__ to train each unit to have the correct state given the states of all the other units in that vector.  
    * It loses the __online learning__ property in the interest of more __efficient storage__.  
    * Statisticians call this technique *__"pseudo-likelihood"__*.  
    * __Procedure Description__:  
        * Set the network to the memory state you want to store
        * Take each unit separately and check if this unit adopts the state we want for it given the states of all the other units: 
            * if it would you, leave its incoming weights alone  
            * if it wouldn't, you change its incoming weights in the way specified by the PLA   
                Notice those will be __*integer* changes__ to the weights  
        * Repeat several times, as needed.  
    * __Convergence:__  
        * If there are too many memories the Perceptron Convergence Procedure won't converge  
        * PLA __converges__, only, if there is a set of weights that will solve the problem   
            Assuming there is, this is a much more efficient way to store memories.  
    <br>

8. **Hopfield Networks with Hidden Units:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18}  
    We add some __hidden units__ to the network with the goal of <span>making the states of those hidden units represent an interpretation of the perceptual input that's shown on the visible units</span>{: style="color: purple"}.  
    The idea is that the <span>__weights__ between units represent __*constraints* on good interpretations__</span>{: style="color: purple"} and <span>by finding a __low energy state__ we find a __good interpretation of the input data__</span>{: style="color: purple"}.  

    __Different Computational Role for Hopfield Nets:__{: style="color: red"}{: #bodyContents18dcr}  
    Instead of using the Hopfield Net to store memories, we can use it to <span>construct interpretations of sensory input</span>{: style="color: purple"}, where  
    {: #lst-p}
    * The __input__ is represented by the _visible units_.  
    * The __interpretation__ is represented by the _states_ of the _hidden units_.  
    * The __Quality__ of the interpretations is represented by the (negative) _Energy_ function.  

    ![img](https://cdn.mathpix.com/snip/images/xkAmrsy0dyoXGJBvHVi4d1LDQKlWdZ3K_bP41Qvc7LI.original.fullsize.png){: width="40%"}  

    [__Example - Interpreting a Line Drawing__](https://www.youtube.com/watch?v=vVEju0zMCaA&list=PLoRl3Ht4JOcdU872GhiYWf6jwrk_SNhz9&index=52)  

    __Two Difficult Computational Issues:__{: style="color: red"}  
    Using the states of the hidden units to represent an interpretation of the input raises two difficult issues:  
    {: #lst-p}
    * __Search__: How do we avoid getting trapped in poor local minima of the energy function?  
        Poor minima represent sub-optimal interpretations.  
    * __Learning__: How do we learn the weights on the connections to the hidden units? and between the hidden units?  
        Notice that there is no supervision in the problem.  


9. **Stochastic Units to improve Search:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents19}  
    Adding noise helps systems escape local energy minima.  

    __Noisy Networks Find Better Energy Minima:__{: style="color: red"}  
    {: #lst-p}
    * A Hopfield net always makes decisions that reduce the energy.
        - This makes it impossible to escape from local minima.  
    * We can use random noise to escape from poor minima.
        - Start with a lot of noise so its easy to cross energy barriers.
        - Slowly reduce the noise so that the system ends up in a deep minimum.  
            This is __"simulated annealing"__ _(Kirkpatrick et.al. 1981)_.  

    __Effects of Temperature on the Transition Probabilities:__  
    The temperature in a physical system (or a simulated system with an Energy Function) affects the transition probabilities.  
    {: #lst-p}
    * __High Temperature System__:  
        ![img](https://cdn.mathpix.com/snip/images/X1dg3rSIy6tVYNCyni5L1yVBoghnLIg88MFCCixV3Gc.original.fullsize.png){: width="60%"}  
        * The __probability of *crossing barriers*__ is <span>high</span>{: style="color: purple"}.  
            I.E. The __probability__ of going *__uphill__* from $$B$$ to $$A$$ is lower than the probability of going *__downhill__* from $$A$$ to $$B$$; but not much lower.  
            * In effect, the temperature _flattens the energy landscape_.    
        * So, the __Ratio of the Probabilities__ is <span>low</span>{: style="color: purple"}.  
            Thus,  
            * It is easy to cross barriers  
            * It is hard to stay in a deep minimum once you've got there  
    * __Low Temperature System__:  
        ![img](https://cdn.mathpix.com/snip/images/slyGgdTvzQogdm6EhkfEUNolozpN8S9gmbTusznV714.original.fullsize.png){: width="60%"}  
        * The __probability of *crossing barriers*__ is <span>much __smaller__</span>{: style="color: purple"}.  
            I.E. The __probability__ of  going *__uphill__* from $$B$$ to $$A$$ is _much_ lower than the probability of going *__downhill__* from $$A$$ to $$B$$.  
        * So, the __Ratio of the Probabilities__ is <span>much __higher__</span>{: style="color: purple"}.  
            Thus,  
            * It is harder to cross barriers  
            * It is easy to stay in a deep minimum once you've got there  
        * Thus, if we run the system long enough, we expect all the particles to end up in $$B$$.  
            However, if we run it at a low temperature, it will take a very long time for particles to escape from $$A$$.  
        * To increase the speed of convergence, starting at a high temperature then gradually decreasing it, is a good compromise.  

    __Stochastic Binary Units:__{: style="color: red"}  
    To <span>__inject noise__ in a Hopfield Net</span>{: style="color: purple"}, we replace the binary threshold units with binary __binary stochastic units__ that make _biased random decisions_.  
    \- The __Temperature__ controls the _amount of noise_.  
    \- <span>__*Raising* the noise level__ is equivalent to __*decreasing* all the energy gaps__ between configurations</span>{: style="color: purple"}.  
    <p>$$p\left(s_{i}=1\right)=\frac{1}{1+e^{-\Delta E_{i} / T}}$$</p>  
    * This is a normal __logistic equation__, but with the <span>__energy gap__ *__scaled__* by a __temperature__ $$T$$</span>{: style="color: purple"}:  
        * __High Temperature:__ the exponential will be $$\approx 0$$ and $$p\left(s_{i}=1\right)= \dfrac{1}{2}$$.  
            I.E. the __probability of a unit turning *on*__ is about a <span>half</span>{: style="color: purple"}.  
            It will be in its _on_ and _off_ states, equally often.  
        * __Low Temperature__: depending on the sign of $$\Delta E_{i}$$, the unit will become _more firmly on_ or _more firmly off_.  
        * __Zero Temperature__: (e.g. in Hopfield Nets) the sign of $$\Delta E_{i}$$ determines whether RHS is $$0$$ or $$1$$.  
            I.E. the unit will behave *__deterministically__*; a standard binary threshold unit, that will always adopt whichever of the two states gives the lowest energy.  
    * __Boltzmann Machines__ use stochastic binary units, with temperature $$T=1$$ (i.e. standard logistic equation).    


    __Thermal Equilibrium at a fixed temperature $$T=1$$:__{: style="color: red"}  
    {: #lst-p}
    * Thermal Equilibrium does not mean that the system has settled down into the lowest energy configuration.  
        I.E. not the states of the individual units that settle down.  
        The individual units still rattle around at Equilibrium, unless the temperature is zero $$T=0$$.  
    * What settles down is the <span>__probability distribution__ over configurations</span>{: style="color: purple"}.  
        * It settles to the __stationary distribution__.  
            * The stationary distribution is determined by the __energy function__ of the system.  
            * In the stationary distribution, the __probability of any configuration__ is $$\propto e^{-E}$$.  
    * __Intuitive Interpretation of Thermal Equilibrium__:  
        - Imagine a huge ensemble of systems that all have exactly the same energy function.  
        - The __probability of a configuration__ is just the _fraction of the systems_ that have that configuration.  
    * __Approaching Thermal Equilibrium__:  
        * Start with any distribution we like over all the identical systems.  
            - We could start with all the systems in the same configuration (__Dirac distribution__).  
            - Or with an equal number of systems in each possible configuration (__uniform distribution__).  
        * Then we keep applying our stochastic update rule to pick the next configuration for each individual system.  
        * After running the systems stochastically in the right way, we may eventually reach a situation where the fraction of systems in each configuration remains constant.  
            - This is the stationary distribution that physicists call thermal equilibrium.  
            - Any given system keeps changing its configuration, but the <span>__fraction of systems__ in each configuration does not change</span>{: style="color: purple"}.  
    * __Analogy__:  
        <button>Analogy - Card Shuffling</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        * Imagine a casino in Las Vegas that is full of card dealers (we need many more than $$52!$$ of them).  
        * We start with all the card packs in standard order and then the dealers all start shuffling their packs.  
            - After a few shuffling steps, the king of spades. still has a good chance of being next to the queen of spades. The packs have not yet forgotten where they stated.  
            - After prolonged shuffling, the packs will have forgotten where they! started. There will be an equal number of packs in each of the $$52!$$ possible orders.  
            - Once equilibrium has been reached, the number of packs that leave a configuration at each time step will be equal to the number that enter the configuration.  
        * The only thing wrong with this analogy is that all the configurations have equal energy, so they all end up with the same probability.  
            * We are generally interested in reaching equilibrium for systems where certain configurations have lower energy than others.  
        {: hidden=""}


    __As Boltzmann Machines:__{: style="color: red"}  
    __Boltzmann Machines__ are just _Stochastic Hopfield Nets_ with _Hidden Units_.  
    <br>



***
***
***


How a Boltzmann machine models a set of binary data vectors  
Why model a set of binary data vectors and what we could do with such a model if we had it
The probabilities assigned to binary data vectors are determined by the weights in a Boltzmann machine

__BMs__ are good at modeling binary data 

__Modeling Binary Data:__{: style="color: red"}  
Given a training set of binary vectors, fit a model that will assign a probability to every possible binary vector.  
- This is useful for deciding if other binary vectors come from the same distribution (e.g. documents represented by binary features that represents the occurrence of a particular word).  
- It can be used for monitoring complex systems to detect unusual behavior.  
- If we have models of several different distributions it can be used to compute the posterior probability that a particular distribution produced the observed data:  
    <p>$$p(\text {Model}_ i | \text { data })=\dfrac{p(\text {data} | \text {Model}_ i)}{\sum_{j} p(\text {data} | \text {Model}_ j)}$$</p>  


__Models for Generating Data:__{: style="color: red"}  
There are different kinds of models to generate data:  
{: #lst-p}
* __Causal Models__  
* __Energy-based Models__  



__How a Causal Model Generates Data:__{: style="color: red"}  
{: #lst-p}
* In a __Causal Model__ we generate data in two _sequential_ steps:  
    * First pick the hidden states from their prior distribution.  
        > in causal models, often __independent__ in the prior.  
    * Then pick the visible states from their conditional distribution given the hidden states.  
    ![img](https://cdn.mathpix.com/snip/images/caikJVJyPI9RUHOvw_XhbndekKG1XMBtELTSeVDFC54.original.fullsize.png){: width="50%"}  
* The probability of generating a visible vector, $$\mathrm{v},$$ is computed by summing over all possible hidden states. Each hidden state is an 'explanation" of $$\mathrm{v}$$:  
    <p>$$p(\boldsymbol{v})=\sum_{\boldsymbol{h}} p(\boldsymbol{h}) p(\boldsymbol{v} | \boldsymbol{h})$$</p>  

> Generating a binary vector: first generate the states of some latent variables, and then use the latent variables to generate the binary vector.  


__How a Boltzmann Machine Generates Data:__{: style="color: red"}  
{: #lst-p}
* It is __not__ a causal generative model.  
* Instead, everything is defined in terms of the <span>__energies of joint configurations__ of the visible and hidden units</span>{: style="color: purple"}. 
* The __energies of joint configurations__ are <span>related</span>{: style="color: purple"} to their __probabilities__ in two ways:  
    * We can simply define the probability to be:  
        <p>$$p(\boldsymbol{v}, \boldsymbol{h}) \propto e^{-E(\boldsymbol{v}, \boldsymbol{h})}$$</p>  
    * Alternatively, we can define the probability to be the probability of finding the network in that joint configuration after we have updated all of the stochastic binary units many times (until thermal equilibrium).  

    These two definitions agree - analysis below.  
* __The Energy of a joint configuration__:  
    <p>$$\begin{align}
        E(\boldsymbol{v}, \boldsymbol{h}) &= - \sum_{i \in v_{i s}} v_{i} b_{i}-\sum_{k \in h_{i d}} h_{k} b_{k}-\sum_{i< j} v_{i} v_{j} w_{i j}-\sum_{i, k} v_{i} h_{k} w_{i k}-\sum_{k< l} h_{k} h_{l} w_{k l} \\
        &= -\boldsymbol{v}^{\top} \boldsymbol{R} \boldsymbol{v}-\boldsymbol{v}^{\top} \boldsymbol{W} \boldsymbol{h}-\boldsymbol{h}^{\top} \boldsymbol{S} \boldsymbol{h}-\boldsymbol{b}^{\top} \boldsymbol{v}-\boldsymbol{c}^{\top} \boldsymbol{h}   
        \end{align}
        $$</p>  
    where $$v_{i} b_{i}$$ __binary state__ of _unit $$i$$_ in $$\boldsymbol{v}$$, $$h_k b_k$$ is the __bias__ of _unit $$k$$_, $$i< j$$ indexes every non-identical pair of $$i$$ and $$j$$ once (avoid self-interactions and double counting), and $$w_{i k}$$ is the __weight__ between visible unit $$i$$ and hidden unit $$k$$.  
* __Using Energies to define Probabilities__:  
    * The __probability of a *joint* configuration__ over both _visible_ and _hidden_ units depends on the energy of that joint configuration compared with the energy of all other joint configurations:  
        <p>$$p(\boldsymbol{v}, \boldsymbol{h})=\dfrac{e^{-E(\boldsymbol{v}, \boldsymbol{h})}}{\sum_{\boldsymbol{u}, \boldsymbol{g}} e^{-E(\boldsymbol{u}, \boldsymbol{g})}}$$</p>  
    * The __probability of a configuration of the *visible* units__ is the sum of the probabilities of all the joint configurations that contain it:  
        <p>$$p(\boldsymbol{v})=\dfrac{\sum_{\boldsymbol{h}} e^{-E(\boldsymbol{v}, \boldsymbol{h})}}{\sum_{\boldsymbol{u}, \boldsymbol{g}} e^{-E(\boldsymbol{u}, \boldsymbol{g})}}$$</p>  

    where the _denomenators_ are the __partition function__ $$Z$$.  
    * <button>Example - How Weights define a Distribution</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        ![img](https://cdn.mathpix.com/snip/images/FlB10QoVtoitDn8bOQAx4Muo-Myp2aTQAKXFc_BPZEo.original.fullsize.png){: width="100%" hidden=""}  
* __Sampling from the *Model*__:  
    * If there are <span>more than a few hidden units</span>{: style="color: purple"}, we cannot compute the normalizing term (the partition function) because it has *__exponentially__* many terms i.e. __intractable__.  
    * So we use Markov Chain Monte Carlo to get samples from the model starting from a random global configuration:  
        - Keep picking units at random and allowing them to stochastically update their states based on their energy gaps.  
    * Run the Markov chain until it reaches its stationary distribution (thermal equilibrium at a temperature of $$1$$).  
        - The probability of a global configuration is then related to its energy by the, __Boltzmann Distribution:__   
            <p>$$p(\mathbf{v}, \mathbf{h}) \propto e^{-E(\mathbf{v}, \mathbf{h})}$$</p>  
* __Sampling from the *Posterior distribution* over *hidden* configurations (for a given Data vector)__:  
    * The __number of possible hidden configurations__ is *__exponential__* so we need __MCMC__ to sample from the *posterior*.  
        - It is just the same as getting a sample from the model, except that we <span>keep the visible units _clamped_ to the given data vector</span>{: style="color: purple"}.  
            I.E. Only the __hidden units__ are allowed to change states (updated)  
    * Samples from the posterior are required for learning the weights.  
        Each __hidden configuration__ is an <span>_"explanation"_</span>{: style="color: goldenrod"} of an observed __visible configuration__.  
        Better explanations have lower energy.  


__The Goal of Learning:__{: style="color: red"}  
We want to maximize the product of the probabilities (sum of log-probabilities) that the Boltzmann Machine assigns to the binary vectors in the training set.  
This is Equivalent to maximizing the probability of obtaining exactly $$N$$ training cases if we ran the BM as follows:  
{: #lst-p}
* For $$i$$ in $$[1, \ldots, N]$$:  
    * Run the network with __no external input__ and let it settle to its *__stationary distribution__*    
    * Sample the *__visible vector__*  

__Possible Difficulty in Learning - Global Information:__{: style="color: red"}  
Consider a chain of units with visible units at the ends:  
![img](https://cdn.mathpix.com/snip/images/vEznkdbLrzZMR8Tn76VEAv-iymx2azcZtYlDl76vYYQ.original.fullsize.png){: width="60%"}  
If the training set is $$(1,0)$$ and $$(0,1)$$ we want the product of all the weights to be negative.  
So to know how to change w1 or w5 we must know w3.  

__Learning with Local Information:__{: style="color: red"}  
A very surprising fact is the following:  
<span>Everything that one weight needs to know about the other weights and the data is contained in the difference of two correlations</span>{: style="color: purple"}.  
The __derivative of *log probability* of one training vector__ wrt. one weight $$w_{ij}$$:  
<p>$$\dfrac{\partial \log p(\mathbf{v})}{\partial w_{i j}}=\left\langle s_{i} s_{j}\right\rangle_{\mathbf{v}}-\left\langle s_{i} s_{j}\right\rangle_{\text {free}}$$</p>  
where:  
{: #lst-p}
* $$\left\langle s_{i} s_{j}\right\rangle_{\mathbf{v}}$$: is the expected value of product of states at thermal equilibrium when the training vector is clamped on the visible units.  
    This is the __positive phase__{: style="color: goldenrod"} of learning.
    * __Effect:__ Raise the weights in proportion to the product of the activities the units have when you are presenting data.  
    * __Interpretation:__ similar to the <span>__storage__ term</span>{: style="color: purple"} for a Hopfield Net.   
        It is a __Hebbian Learning Rule__{: style="color: goldenrod"}.  
* $$\left\langle s_{i} s_{j}\right\rangle_{\text {free}}$$: is the expected value of product of states at thermal equilibrium when nothing is clamped.  
    This is the __negative phase__{: style="color: goldenrod"} of learning.
    * __Effect:__ Reduce the weights in proportion to _"how often the two units are **on** together when sampling from the **models distribution**"_.  
    * __Interpretation:__ similar to the <span>__Unlearning__ term</span>{: style="color: purple"} i.e. the <span>_opposite of the storage rule_</span>{: style="color: purple"} for <span>avoiding</span>{: style="color: goldenrod"} (getting rid of) <span>spurious minima</span>{: style="color: goldenrod"}.  
        Moreover, this rule specifies the __exact amount of *unlearning*__ to be applied.  

So, the __change in the weight__ is _proportional to_ the expected product of the activities averaged over all visible vectors in the training set that's what we call data MINUS the product of the same two activities when there is no clamping and the network has reached thermal equilibrium with no external interference:  
<p>$$\Delta w_{i j} \propto\left\langle s_{i} s_{j}\right\rangle_{\text{data}}-\left\langle s_{i} s_{j}\right\rangle_{\text{model}}$$</p>  

<span class="borderexample">Thus, the learning algorithm only requires __local information__.</span>  


__Effects of the Positive and Negative Phases of Learning:__{: style="color: red"}  
Given the __probability of a training data vector $$\boldsymbol{v}$$__:  
<p>$$p(\boldsymbol{v})=\dfrac{\sum_{\boldsymbol{h}} e^{-E(\boldsymbol{v}, \boldsymbol{h})}}{\sum_{\boldsymbol{u}} \sum_{\boldsymbol{g}} e^{-E(\boldsymbol{u}, \boldsymbol{g})}}$$</p>   
and the __log probability__:  
<p>$$\begin{align}
    \log p(\boldsymbol{v}) &= \log \left(\dfrac{\sum_{\boldsymbol{h}} e^{-E(\boldsymbol{v}, \boldsymbol{h})}}{\sum_{\boldsymbol{u}} \sum_{\boldsymbol{g}} e^{-E(\boldsymbol{u}, \boldsymbol{g})}}\right) \\
    &= \log \left(\sum_{\boldsymbol{h}} e^{-E(\boldsymbol{v}, \boldsymbol{h})}\right) - \log \left(\sum_{\boldsymbol{u}} \sum_{\boldsymbol{g}} e^{-E(\boldsymbol{u}, \boldsymbol{g})}\right) \\
    &= \left( \sum_{\boldsymbol{h}} \log e^{-E(\boldsymbol{v}, \boldsymbol{h})}\right) - \left(\sum_{\boldsymbol{u}} \sum_{\boldsymbol{g}} \log e^{-E(\boldsymbol{u}, \boldsymbol{g})}\right) \\
    &= \left(\sum_{\boldsymbol{h}} -E(\boldsymbol{v}, \boldsymbol{h})\right) - \left(\sum_{\boldsymbol{u}} \sum_{\boldsymbol{g}} -E(\boldsymbol{u}, \boldsymbol{g})\right)
    \end{align}
    $$</p>   
{: #lst-p}
* __Positive Phase:__   
    * The first term is <span>decreasing the energy of terms in that sum that are already large</span>{: style="color: purple"}. 
        * It finds those terms by settling to thermal equilibrium with the vector $$\boldsymbol{v}$$ clamped so they can find an $$\boldsymbol{h}$$ that __produces a low energy__ with $$\boldsymbol{v}$$).  
    * Having sampled those vectors $$\boldsymbol{h}$$, it then <span>changes the weights to make that energy even lower</span>{: style="color: purple"}.  
    * __Summary:__  
        The positive phase finds hidden configurations that work well with $$\boldsymbol{v}$$ and lowers their energies.  
* __Negative Phase__:  
    * The second term is <span>doing the same thing but for the __partition function__</span>{: style="color: purple"}.  
        It's <span>finding global configurations (combinations of visible and hidden states) that give low energy and therefore are large contributors to the partition function</span>{: style="color: purple"}.   
    * Having found those global configurations $$(\boldsymbol{v}', \boldsymbol{h}')$$, it <span>tries to raise their energy so that they contribute less</span>{: style="color: purple"}.    
    * __Summary:__  
        The negative phase finds the joint configurations that are the best competitors and raises their energies.  

Thus, the positive term is making the top term in $$p(\boldsymbol{v})$$ __bigger__ and the negative term is making the bottom term in $$p(\boldsymbol{v})$$ __smaller__.  

<button>Effects of only using the Hebbian Rule (Positive phase)</button>{: .showText value="show" onclick="showTextPopHide(event);"}
<span hidden="">If we only use the Hebbian rule (positive phase) without the unlearning term (negative phase) the synapse strengths will keep getting stronger and stronger, the weights will all become very positive, and the whole system will blow up.  
The Unlearning counteracts the positive phase's tendency to just add a large constant to the unnormalized probability everywhere.</span>


__Learning Rule Justification - Why the Derivative is so simple:__{: style="color: red"}  
{: #lst-p}
* The __probability of a *global* configuration__ <span>at __thermal equilibrium__</span>{: style="color: purple"} is an <span>__exponential function__ of its energy</span>{: style="color: goldenrod"}.  
    - Thus, <span>settling to equilibrium makes the __log probability__ a *__linear__* __function__ of the __energy__</span>{: style="color: goldenrod"}.  
* The __energy__ is a *__linear__* __function__ of the __weights__ and __states__:  
    <p>$$\dfrac{\partial E}{\partial w_{i j}}=s_{i} s_{j}$$</p>  
    It is a __log-linear model__.  
    This an important fact because we are trying to manipulate the log probabilities by manipulating the weights.  
* The <span>__process of settling to thermal equilibrium__ _propagates information_ about the __weights__</span>{: style="color: goldenrod"}.  
    * We don't need an explicit __back-propagation__ stage.  
    * We still need __two stages__:  
        1. Settle with the data
        2. Settle with NO data 
    * However, the network behaves, basically, in the same way in the two phases[^1]; while the forward and backprop stages are very different.  

__The Batch Learning Algorithm - An inefficient way to collect the Learning Statistics:__{: style="color: red"}  
{: #lst-p}
* __Positive phase:__  
    - Clamp a data-vector on the visible units.
    - Let the hidden units reach thermal equilibrium at a temperature of 1 (may use annealing to speed this up)  
        by updating the hidden units, one at a time.  
    - Sample $$\left\langle s_{i} s_{j}\right\rangle$$ for all pairs of units
    - Repeat for all data-vectors in the training set.
* __Negative phase:__  
    - Do not clamp any of the units
    - Set all the units to random binary states.
    - Let the whole network reach thermal equilibrium at a temperature of 1, by updating all the units, one at a time.  
        * __Difficulty__: where do we start? 
    - Sample $$\left\langle s_{i} s_{j}\right\rangle$$ for all pairs of units
    - Repeat many times to get good estimates  
        * __Difficulty__: how many times? (especially w/ multiple modes) 
* __Weight updates:__  
    - Update each weight by an amount proportional to the difference in $$\left\langle s_{i} s_{j}\right\rangle$$ in the two phases.  




[^1]: The state space is the corners of a hypercube. Showing it as a $$1-D$$ continuous space is a misrepresentation.  