---
layout: NotesPage
title: PGMs <br /> Probabilistic Graphical Models
permalink: /work_files/research/dl/archits/pgm
prevLink: /work_files/research/dl/nlp.html
---



<div markdown="1" class = "TOC">
# Table of Contents

  * [Graphical Models](#content1)
  {: .TOC1}
  * [Bayesian Networks](#content2)
  {: .TOC2}
<!--   * [THIRD](#content3)
  {: .TOC3} -->
  * [Random Field Techniques](#content4)
  {: .TOC4}
</div>

***
***

__Resources:__{: style="color: red"}  
{: #lst-p}
* [An Introduction to Probabilistic Graphical Models: Conditional Independence and Factorization (M Jordan)](http://people.eecs.berkeley.edu/~jordan/prelims/chapter2.pdf)  
* [An Intro to PGMs: The Elimination Algorithm (M Jordan)](http://people.eecs.berkeley.edu/~jordan/prelims/chapter3.pdf)  
* [An Intro to PGMs: Probability Propagation and Factor Graphs](http://people.eecs.berkeley.edu/~jordan/prelims/chapter4.pdf)  
* [An Intro to PGMs: The EM algorithm](http://people.eecs.berkeley.edu/~jordan/prelims/chapter11.pdf)  
* [An Intro to PGMs: Hidden Markov Models](http://people.eecs.berkeley.edu/~jordan/prelims/chapter12.pdf)  
* [A Brief Introduction to Graphical Models and Bayesian Networks (Paper!)](https://www.cs.ubc.ca/~murphyk/Bayes/bnintro.html)  
* [Deep Learning vs Probabilistic Graphical Models vs Logic (Blog!)](http://www.computervisionblog.com/2015/04/deep-learning-vs-probabilistic.html)  
* [Probabilistic Graphical Models CS-708 (CMU!)](https://sailinglab.github.io/pgm-spring-2019/)  
* [Graphical Models, Exponential Families, and Variational Inference (M. Jordan)](https://people.eecs.berkeley.edu/~wainwrig/Papers/WaiJor08_FTML.pdf)  


## Graphical Models
{: #content1}

<button>Taxonomy of Graphical Models</button>{: .showText value="show" onclick="showTextPopHide(event);"}
![img](https://cdn.mathpix.com/snip/images/_wohJaHgQzjzawD16m9vaHl-7jvkyn4IcpBHGDltoKc.original.fullsize.png){: width="100%" hidden=""}  


0. **Motivation:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents10}  
    Machine learning algorithms often involve probability distributions over a very large number of random variables. Often, these probability distributions involve direct interactions between relatively few variables. Using a single function to describe the entire joint probability distribution can be very inefficient (both computationally and statistically).  

    > A description of a probability distribution is _exponential_ in the number of variables it models.  


1. **Graphical Model:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    A __graphical model__ or __probabilistic graphical model (PGM)__ or __structured probabilistic model__ is a probabilistic model for which a graph expresses the conditional dependence structure (factorization of a probability distribution) between random variables.  
    > Generally, this is one of the most common _statistical models_  

    __Properties:__{: style="color: red"}  
    {: #lst-p}
    * __Factorization__  
    * __Independence__  

    __Graph Structure:__  
    A PGM uses a graph $$\mathcal{G}$$ in which each _node_ in the graph corresponds to a _random variable_, and an _edge_ connecting two r.vs means that the probability distribution is able to _represent interactions_ between those two r.v.s.  

    
    __Types:__  
    {: #lst-p}
    * __Directed__:  
        Directed models use graphs with directed edges, and they represent factorizations into conditional probability distributions.  
        They contain one factor for every random variable $$x_i$$ in the distribution, and that factor consists of the conditional distribution over $$x_i$$ given the parents of $$x_i$$.  
    * __Undirected__:  
        Undirected models use graphs with undirected edges, and they represent factorizations into a set of functions; unlike in the directed case, these functions are usually not probability distributions of any kind.  


    __Core Idea of Graphical Models:__{: style="color: red"}  
    <span>The probability distribution factorizes according to the cliques in the graph, with the potentials usually being of the exponential family (and a graph expresses the conditional dependence structure between random variables).</span>{: style="color: goldenrod"}    
    <br>
            
2. **Neural Networks and Graphical Models:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    __Deep NNs as PGMs:__{: style="color: red"}  
    You can view a deep neural network as a graphical model, but here, the CPDs are not probabilistic but are deterministic. Consider for example that the input to a neuron is $$\vec{x}$$ and the output of the neuron is $$y .$$ In the CPD for this neuron we have, $$p(\vec{x}, y)=1,$$ and $$p(\vec{x}, \hat{y})=0$$ for $$\hat{y} \neq y .$$ Refer to the section 10.2 .3 of Deep Learning Book for more details.  
    <br>

<!-- 3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  
6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}  
7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}  
8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18}  
--> 

***

## Bayesian Network
{: #content2}

<button>Bayes Nets</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
1. **Bayesian Network:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    A __Bayesian network__, __Bayes network__, __belief network__, or __probabilistic directed acyclic graphical model__ is a probabilistic graphical model that represents a set of variables and their conditional dependencies via a directed acyclic graph (__DAG__).  
    > E.g. a Bayesian network could represent the probabilistic relationships between diseases and symptoms.  


    __Bayes Nets (big picture):__{: style="color: red"}  
    __Bayes Nets:__ a technique for describing complex joint distributions (models) using simple, local distributions (conditional probabilities).  

    In other words, they are a device for describing a complex distribution, over a large number of variables, that is built up of small pieces (_local interactions_); with the assumptions necessary to conclude that the product of those local interactions describe the whole domain.  

    __Formally,__ a Bayes Net consists of:  
    {: #lst-p}
    1. A __directed acyclic graph of nodes__, one per variable $$X$$ 
    2. A __conditional distribution for each node $$P(X\vert A_1\ldots A_n)$$__, where $$A_i$$ is the $$i$$th parent of $$X$$, stored as a *__conditional probability table__* or *__CPT__*.  
        Each CPT has $$n+2$$ columns: one for the values of each of the $$n$$ parent variables $$A_1 \ldots A_n$$, one for the values of $$X$$, and one for the conditional probability of $$X$$.  

    Each node in the graph represents a single random variable and each directed edge represents one of the conditional probability distributions we choose to store (i.e. an edge from node $$A$$ to node $$B$$ indicates that we store the probability table for $$P(B\vert A)$$).  
    <span>Each node is conditionally independent of all its ancestor nodes in the graph, given all of its parents.</span>{: style="color: goldenrod"} Thus, if we have a node representing variable $$X$$, we store $$P(X\vert A_1,A_2,...,A_N)$$, where $$A_1,\ldots,A_N$$ are the parents of $$X$$.   


    __The _local probability tables (of conditional distributions)_ and the _DAG_ together encode enough information to compute any probability distribution that we could have otherwise computed given the entire joint distribution.__{: style="color: goldenrod"}  


    __Motivation:__{: style="color: red"}  
    There are problems with using full join distribution tables as our probabilistic models:  
    {: #lst-p}
    * Unless there are only a few variables, the joint is WAY too big to represent explicitly
    * Hard to learn (estimate) anything empirically about more than a few variables at a time  


    __Examples of Bayes Nets:__{: style="color: red"}  
    {: #lst-p}
    * __Coin Flips__:  
        img1
    * __Traffic__:  
        img2
    * __Traffic II__:  
        img3
    * __Alarm Network__:  
        img4


    __Probabilities in BNs:__{: style="color: red"}  
    {: #lst-p}
    * Bayes Nets *__implicitly__* encode <span>__joint distributions__</span>{: style="color: purple"}:  
        Encoded as a <span>*__product__* of _local_ __conditional distributions__</span>{: style="color: purple"}:  
        <p>$$p(x_1, x_2, \ldots, x_n) = \prod_{i=1}^{n} p(x_i \vert \text{parents}(X_i)) \tag{1.1}$$</p>  
    * We are guaranteed that $$1.1$$ results in a proper joint distribution:  
        1. Chain Rule is valid for all distributions:  
            <p>$$p(x_1, x_2, \ldots, x_n) = \prod_{i=1}^{n} p(x_i \vert x_1, \ldots, x_{i-1})$$</p>  
        2. Conditional Independences Assumption:  
            <p>$$p(x_1, x_2, \ldots, x_{i-1}) = \prod_{i=1}^{n} p(x_i \vert \text{parents}(X_i))$$</p>
            $$\implies$$  
            <p>$$p(x_1, x_2, \ldots, x_n) = \prod_{i=1}^{n} p(x_i \vert \text{parents}(X_i)) \tag{1.1}$$</p>  

    Thus (from above) Not every BN can represent every joint distribution.  
    The topology enforces certain conditional independencies that need to be met.  
    > e.g. Only distributions whose variables are _absolutely independent_ can be represented by a Bayes Net with no arcs  


    __Causality:__{: style="color: red"}  
    Although the structure of the BN might be in a way that encodes causality, it is not necessary to define the joint distribution graphically. The two definitions below are the same:  
    img5  
    To summarize:  
    {: #lst-p}
    * When BNs reflect the true causal patterns:  
        * Often simpler (nodes have fewer parents)
        * Often easier to think about
        * Often easier to elicit from experts 
    * BNs need NOT be causal:  
        * Sometimes no causal net exists over the domain (especially if variables are missing)  
            * e.g. consider the variables $$\text{Traffic}$$ and $$\text{Drips}$$  
        * Results in arrows that reflect __correlation__, not __causation__  
    * The meaning of the arrows:  
        * The topology may happen to encode causal structure
        * But, the <span>topology really encodes conditional independence </span>{: style="color: goldenrod"}   
            <p>$$p(x_1, x_2, \ldots, x_{i-1}) = \prod_{i=1}^{n} p(x_i \vert \text{parents}(X_i))$$</p>
    <br>

    __Questions we can ask__{: style="color: red"}  
    Since a BN encodes a __joint distribution__ we can ask any questions a joint distribution can answer:  
    {: #lst-p}
    * __Inference:__ given a fixed BN, what is $$P(X \vert \text { e)? }$$
    * __Representation:__ given a BN graph, what kinds of distributions can it encode?
    * __Modeling:__ what BN is most appropriate for a given domain?  


    __Size of a BN:__{: style="color: red"}  
    {: #lst-p}
    - Size of a full __joint distribution__ over $$N$$ (boolean) variables: $$2^N$$  
    - Size of an __$$N$$-node net__ with nodes having up to $$k$$ parents: $$\mathcal{O}(N \times 2^{k+1}$$  


    __Advantages of BN over full joint distribution:__{: style="color: red"}  
    {: #lst-p}
    * Both will model (calculate) $$p(X_1, X_2, \ldots, X_N)$$  
    * BNs give you huge space savings  
    * It is easier to elicit local CPTs  
    * Is faster to answer queries      
    <br>


    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * The __acyclicity__ gives an order to the (order-less) chain-rule of conditional probabilities  
    * Think of the conditional distribution for each node as a _description of a noisy "causal" process_  
    * The graph of the BN represents certain independencies directly, but also contains extra independence assumptions that can be "inferred" from the shape of the graph  
        ![img](https://cdn.mathpix.com/snip/images/kZDOC0zRNk2bHppVoSor5oVJXp1YkcVdem6Sqd77bCE.original.fullsize.png){: width="34%"}  
    * There could be extra independence relationships in the distribution that are not represented by the BN graph structure but can be read in the CPT. This happens when the structure of the BN is not "optimal" for the assumptions between the variables.  
    <br>

2. **Independence / D-Separation:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}  
    Goal is to find a graph algorithm that can show independencies between variables in BNs. Steps:    
    1. Study independence properties for triples  
    2. Analyze complex cases (configurations) in terms of member triples  
    3. D-separation: a condition / algorithm for answering such queries  

    
    __Causal Chains:__{: style="color: red"}  
    ![img](https://cdn.mathpix.com/snip/images/C14nDRwzxp3kdGjCGvBCfdT5wQT3-5ejjNUWa6aCElg.original.fullsize.png){: width="34%"}  
    A Causal Chain is a configuration of __three nodes__ that expresses the following representation of the joint distribution over $$X$$, $$Y$$ and $$Z$$:  
    <p>$$P(x, y, z)=P(z \vert y) P(y \vert x) P(x)$$</p>  

    Let's try to see if we can guarantee independence between $$X$$ and $$Z$$:  
    * __No Observations:__  
        ![img](https://cdn.mathpix.com/snip/images/vCusDjGbyWit9iVXoCw-ZDdK5JGdx32uk7qsKe0xCAc.original.fullsize.png){: width="38%"}  
        $$X$$ and $$Z$$ are __not guaranteed independent__.  
        * __Proof__:  
            By Counterexample:  
            <p>$$P(y \vert x)=\left\{\begin{array}{ll}{1} & {\text { if } x=y} \\ {0} & {\text { else }}\end{array} \quad P(z \vert y)=\left\{\begin{array}{ll}{1} & {\text { if } z=y} \\ {0} & {\text { else }}\end{array}\right.\right.$$</p>  
            $$\text { In this case, } P(z \vert x)=1 \text { if } x=z \text { and } 0 \text { otherwise, so } X \text { and } Z \text { are not independent.}$$  

    * __$$Y$$ Observed:__  
        ![img](https://cdn.mathpix.com/snip/images/W1ji7bFRCqCmTeO_sFPz3BZXnIaY2zRlLtpv1vIKiUw.original.fullsize.png){: width="38%"}  
        $$X$$ and $$Z$$ are __independent given $$Y$$__. i.e. $$P(X \vert Z, Y)=P(X \vert Y)$$  
        * __Proof:__  
            <p>$$\begin{aligned} P(X \vert Z, y) &=\frac{P(X, Z, y)}{P(Z, y)}=\frac{P(Z \vert y) P(y \vert X) P(X)}{\sum_{x} P(X, y, Z)}=\frac{P(Z \vert y) P(y \vert X) P(X)}{P(Z \vert y) \sum_{x} P(y \vert x) P(x)} \\ &=\frac{P(y \vert X) P(X)}{\sum_{x} P(y \vert x) P(x)}=\frac{P(y \vert X) P(X)}{P(y)}=P(X \vert y) \end{aligned}$$</p>  
    An analogous proof can be used to show the same thing for the case where X has multiple parents.  

    To summarize, <span>in the causal chain chain configuration, $$X \perp Z \vert Y$$ </span>{: style="color: goldenrod"}.  

    > Evidence along the chain "blocks" the influence.  

    * [**Causal Chains (188)**](https://www.youtube.com/embed/FUnOdyZZAaE?start=1698){: value="show" onclick="iframePopA(event)"}
    <a href="https://www.youtube.com/embed/FUnOdyZZAaE?start=1698"></a>
        <div markdown="1"> </div>    

    
    __Common Cause:__{: style="color: red"}  
    __Common Cause__ is another configuration for a triple. It expresses the following representation:  
    <p>$$P(x, y, z)=P(x \vert y) P(z \vert y) P(y)$$</p>  
    ![img](https://cdn.mathpix.com/snip/images/CduaPDNSTAmqr_VCjz80jm0h8KUAPQogTozW5-zxe8s.original.fullsize.png){: width="34%"}  

    Let's try to see if we can guarantee independence between $$X$$ and $$Z$$:  
    * __No Observations:__  
        ![img](https://cdn.mathpix.com/snip/images/5WPHMjwgo5l-on6MzOi4urmfDQixe1crSlo38pSfhDY.original.fullsize.png){: width="38%"}  
        $$X$$ and $$Z$$ are __not guaranteed independent__.  
        * __Proof__:  
            By Counterexample:  
            <p>$$P(x \vert y)=\left\{\begin{array}{ll}{1} & {\text { if } x=y} \\ {0} & {\text { else }}\end{array} \quad P(z \vert y)=\left\{\begin{array}{ll}{1} & {\text { if } z=y} \\ {0} & {\text { else }}\end{array}\right.\right.$$</p>  
            \text { Then } P(x \vert z)=1 \text { if } x=z \text { and } 0 \text { otherwise, so } X \text { and } Z \text { are not independent. }  

    * __$$Y$$ Observed:__  
        ![img](https://cdn.mathpix.com/snip/images/Uu8LonpCanIwyab_QKVW_DDx6GR8z7d2fvl1oh5uNtc.original.fullsize.png){: width="38%"}  
        $$X$$ and $$Z$$ are __independent given $$Y$$__. i.e. $$P(X \vert Z, Y)=P(X \vert Y)$$  
        * __Proof:__  
            <p>$$P(X \vert Z, y)=\frac{P(X, Z, y)}{P(Z, y)}=\frac{P(X \vert y) P(Z \vert y) P(y)}{P(Z \vert y) P(y)}=P(X \vert y)$$</p>  

    > Observing the cause blocks the influence.  

    * [**Common Cause (188)**](https://www.youtube.com/embed/FUnOdyZZAaE?start=1922){: value="show" onclick="iframePopA(event)"}
    <a href="https://www.youtube.com/embed/FUnOdyZZAaE?start=1922"></a>
        <div markdown="1"> </div>    


    __Common Effect:__{: style="color: red"}  
    __Common Effect__ is the last configuration for a triplet. Expressing the representation:  
    <p>$$P(x, y, z)=P(y \vert x, z) P(x) P(z)$$</p>  
    ![img](https://cdn.mathpix.com/snip/images/bHoFq74CVLvVJNrj13GmsoiVlJrVuskee1qaDPB5ZZc.original.fullsize.png){: width="34%"}  

    Let's try to see if we can guarantee independence between $$X$$ and $$Z$$:  
    * __No Observations:__  
        ![img](https://cdn.mathpix.com/snip/images/CTuUmWXjwo4kqxrotATNnYossKNqwl6mfjB2H7OPQi8.original.fullsize.png){: width="38%"}  
        $$X$$ and $$Z$$ are, readily, __guaranteed to be independent__: $$X \perp Z$$.  

    * __$$Y$$ Observed:__  
        ![img](https://cdn.mathpix.com/snip/images/wfOTQbsydA4ZTpN0tW0tQtRbfDyNGrokp1xk9nC8JfE.original.fullsize.png){: width="38%"}  
        $$X$$ and $$Z$$ are __not necessarily independent given $$Y$$__. i.e. $$P(X \vert Z, Y)\neq P(X \vert Y)$$  
        * __Proof:__  
            By Counterexample:  
            $$\text { Suppose all three are binary variables. } X \text { and } Z \text { are true and false with equal probability: }$$  
            <p>$$\begin{array}{l}{P(X=\text {true})=P(X=\text { false })=0.5} \\ {P(Z=\text {true})=P(Z=\text { false })=0.5}\end{array}$$</p>  
            $$ \text { and } Y \text { is determined by whether } X \text { and } Z \text { have the same value: } $$  
            <p>$$P(Y \vert X, Z)=\left\{\begin{array}{ll}{1} & {\text { if } X=Z \text { and } Y=\text { true }} \\ {1} & {\text { if } X \neq Z \text { and } Y=\text { false }} \\ {0} & {\text { else }}\end{array}\right.$$</p>  
            $$ \text { Then } X \text { and } Z \text { are independent if } Y \text { is unobserved. But if } Y \text { is observed, then knowing } X \text { will }\\ 
            \text { tell us the value } {\text { of } Z, \text { and vice-versa. } \text{So } X \text { and } Z \text { are } \text {not} \text { conditionally independent given } Y \text {. }} $$  

    Common Effect can be viewed as __"opposite" to Causal Chains and Common Cause__-$$X$$ and $$Z$$ are guaranteed to be independent if $$Y$$ is not conditioned on. But when conditioned on $$Y, X$$ and $$Z$$ may be dependent depending on the specific probability values for $$P(Y \vert X, Z)$$).  

    This same logic applies when conditioning on descendants of $$Y$$ in the graph. If one of $$Y$$ 's descendent nodes is observed, as in Figure $$7, X$$ and $$Z$$ are not guaranteed to be independent.  
    ![img](https://cdn.mathpix.com/snip/images/UBploFCx8ITyj_Yp20s9iAS_tXmj-0-DmF2neJp2alY.original.fullsize.png){: width="34%"}  

    > Observing an effect activates influence between possible causes.  

    * [**Common Effect (188)**](https://www.youtube.com/embed/FUnOdyZZAaE?start=2115){: value="show" onclick="iframePopA(event)"}
    <a href="https://www.youtube.com/embed/FUnOdyZZAaE?start=2115"></a>
        <div markdown="1"> </div>    
    <br>

    __General Case, and D-Separation:__{: style="color: red"}  
    We can use the previous three cases as building blocks to help us answer conditional independence questions on an arbitrary Bayes’ Net with more than three nodes and two edges.  We formulate the problem as follows:  
    __Given a Bayes Net $$G,$$ two nodes $$X$$ and $$Y,$$ and a (possibly empty) set of nodes $$\left\{Z_{1}, \ldots Z_{k}\right\}$$ that represent observed variables, must the following statement be true: $$X \perp Y |\left\{Z_{1}, \ldots Z_{k}\right\} ?$$__  

    __D-Separation:__ (directed separation) is a property of the structure of the Bayes Net graph that implies this conditional independence relationship, and generalizes the cases we’ve seen above. If a set of variables $$Z_{1}, \cdots Z_{k} d-$$ -separates $$X$$ and $$Y,$$ then $$X \perp Y \vert\left\{Z_{1}, \cdots Z_{k}\right\}$$ in all possibutions that can be encoded by the Bayes net.  


    __D-Separation Algorithm:__  
    1. Shade all observed nodes $$\left\{Z_{1}, \ldots, Z_{k}\right\}$$ in the graph.
    2. Enumerate all undirected paths from $$X$$ to $$Y$$ .
    3. For each path:
        * Decompose the path into triples (segments of 3 nodes).
        * If all triples are active, this path is active and $$d$$ -connects $$X$$ to $$Y$$.
    4. If no path d-connects $$X$$ and $$Y$$ and $$Y$$ are d-separated, so they are conditionally independent
    given $$\left\{Z_{1}, \ldots, Z_{k}\right\}$$  

    Any path in a graph from $$X$$ to $$Y$$ can be decomposed into a set of 3 consecutive nodes and 2 edges - each of which is called a triple. A triple is active or inactive depending on whether or not the middle node is observed. If all triples in a path are active, then the path is active and $$d$$ -connects $$X$$ to $$Y,$$ meaning $$X$$ is not guaranteed to be conditionally independent of $$Y$$ given the observed nodes. If all paths from $$X$$ to $$Y$$ are inactive, then $$X$$ and $$Y$$ are conditionally independent given the observed nodes.  

    __Active Triples:__ We can enumerate all possibilities of active and inactive triples using the three canonical graphs we presented above in Figure 8 and 9.  
    ![img](https://cdn.mathpix.com/snip/images/-833dBM_DnuIFc9csn1KJYNu-IH-4TntVXDfprkEvTk.original.fullsize.png){: width="80%" .center-image}  

    * [**General Case and D-Separation (188)**](https://www.youtube.com/embed/FUnOdyZZAaE?start=2331){: value="show" onclick="iframePopA(event)"}
    <a href="https://www.youtube.com/embed/FUnOdyZZAaE?start=2331"></a>
        <div markdown="1"> </div>    


    __Examples:__  
    {: #lst-p}
    * <button>Ex.1</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/vveQfEygnrmDXO3u1dmq5qIg0WFuLlgUwuli1UuWGWE.original.fullsize.png){: width="100%" hidden=""}  
    * <button>Ex.2</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/6kxQgkDxD1oQVhNBNOdEG9Knv0aVcsL6lbHBOpB-opk.original.fullsize.png){: width="100%" hidden=""}  
    * <button>Ex.3</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/LpfPhSioro_8eMua-mQ6oQ9yFtbmHEnaXhJWaOmXGss.original.fullsize.png){: width="100%" hidden=""}  
    * [**Examples (188)**](https://www.youtube.com/embed/FUnOdyZZAaE?start=2840){: value="show" onclick="iframePopA(event)"}
    <a href="https://www.youtube.com/embed/FUnOdyZZAaE?start=2840"></a>
        <div markdown="1"> </div>    
    <br>  

    __Structure Implications:__{: style="color: red"}  
    Given a Bayes net structure, can run d-separation algorithm to build a complete list of conditional independences that are necessarily true of the form.  
    <p>$$X_{i} \perp X_{j} |\left\{X_{k_{1}}, \ldots, X_{k_{n}}\right\}$$</p>  
    This list determines the set of probability distributions that can be represented.  

    __Topology Limits Distributions:__{: style="color: red"}  
    {: #lst-p}
    ![img](https://cdn.mathpix.com/snip/images/gyXj8tjBdUlkWuBYJvVScXjnh_Qsvb7cj6LKTqQL9pc.original.fullsize.png){: width="60%"}  
    * Given some graph topology $$G$$, only certain joint distributions can be encoded  
    * The graph structure guarantees certain (conditional) independences
    * (There might be more independence)
    * Adding arcs increases the set of distributions, but has several costs
    * Full conditioning can encode any distribution  
    * The more assumptions you make the fewer the number of distributions you can represent  

    __Bayes Nets Representation Summary:__{: style="color: red"}  
    {: #lst-p}
    * Bayes nets compactly encode joint distributions
    * Guaranteed independencies of distributions can be deduced from BN graph structure
    * D-separation gives precise conditional independence guarantees from graph alone
    * A Bayes nets joint distribution may have further (conditional) independence that is not detectable until you inspect its specific distribution

    <br>

3. **Inference:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}  
    [Lecture (188)](https://www.youtube.com/watch?v=A1hYXGAUdmU&list=PL7k0r4t5c108AZRwfW-FhnkZ0sCKBChLH&index=15)  

    __Inference__ is the process of calculating the joint PDF for some set of query variables based on some set of observed variables.  
    For example:  
    {: #lst-p}
    * __Posterior Probability__ inference:  
        <p>$$P\left(Q \vert E_{1}=e_{1}, \ldots E_{k}=e_{k}\right)$$</p>  
    * __Most Likely Explanation__ inference:  
        <p>$$\operatorname{argmax}_{q} P\left(Q=q \vert E_{1}=e_{1} \ldots\right)$$</p>  

    __Notation - General Case:__  
    <p>$$ \left.\begin{array}{ll}{\textbf { Evidence variables: }} & {E_{1} \ldots E_{k}=e_{1} \ldots e_{k}} \\ {\textbf { Query}^{* } \textbf { variable: }} & {Q} \\ {\textbf { Hidden variables: }} & {H_{1} \ldots H_{r}}\end{array}\right\} \begin{array}{l}{X_{1}, X_{2}, \ldots X_{n}} \\ {\text { All variables }}\end{array} $$</p>  


    __Inference by Enumeration:__{: style="color: red"}  
    We can solve this problem _naively_ by forming the joint PDF and using __inference by enumeration__ as described above. This requires the creation of and iteration over an exponentially large table.   
    __Algorithm:__  
    * Select the entries consistent with the evidence
    * Sum out $$\mathrm{H}$$ to get join of Query and evidence  
    * Normalize: $$\times \dfrac{1}{Z} = \dfrac{1}{\text{sum of entries}}$$  
    * [**Inference by Enumeration (188)**](https://www.youtube.com/embed/A1hYXGAUdmU?start=980){: value="show" onclick="iframePopA(event)"}
    <a href="https://www.youtube.com/embed/A1hYXGAUdmU?start=980"></a>
        <div markdown="1"> </div>    



    __Variable Elimination:__{: style="color: red"}  
    Alternatively, we can use __Variable Elimination__: __eliminate__ variables one by one.  
    To eliminate a variable $$X$$, we:  
    {: #lst-p}
    1. Join (multiply together) all factors involving $$X$$.
    2. Sum out $$X$$.  

    A __factor__ is an unnormalized probability; represented as a multidimensional array:  
    {: #lst-p}
    * __Joint Distributions__: $$P(X,Y) \in \mathbb{R}^2$$  
        * Entries $$P(x, y)$$ for all $$x, y$$  
        * Sums to $$1$$  
    * __Selected Joint__: $$P(x,Y) \in \mathbb{R}$$ 
        * A slice of the joint distribution
        * Entries $${P}({x}, {y})$$ for fixed $${x},$$ all $${y}$$  
        * Sums to $$P(x)$$  

    * __Single Conditional__: $$P(Y \vert x)$$  
        * Entries $${P}({y} \vert {x})$$ for fixed $${x},$$ all $${y}$$  
        * Sums to $$1$$ 
    * __Family of Conditionals__: $$P(Y \vert X)$$ 
        * Multiple Conditionals
        * Entries $${P}({y} \vert {x})$$ for all $${x}, {y}$$  
        * Sums to $$\vert X\vert$$  

    * __Specified family__: $$P(y \vert X)$$
        * Entries $$P(y \vert x)$$ for fixed $$y$$ but for all $$x$$
        * Sums to random number; not a distribution  

    > For Joint Distributions, the \# __capital variables__ dictates the _"dimensionality"_ of the array.  


    At all points during variable elimination, each factor will be proportional to the probability it corresponds to but the underlying distribution for each factor won’t necessarily sum to $$1$$ as a probability distribution should.  

    __Inference by Enumeration vs. Variable Elimination:__  
    __Inference by Enumeration__ is very *__slow__*: You must join up the whole joint distribution before you sum out the hidden variables.  
    __Variable Elimination:__ Interleave __joining__ and __marginalization__.  
    Still NP-hard, but usually much faster.  
    ![img](https://cdn.mathpix.com/snip/images/X9wU1le8_K5c9X2lm59mNGaEkJW8DZnnWHiz-3h4eVw.original.fullsize.png){: width="70%"}  
    Notice that $$\sum_r P(r) P(t \vert r) = P(t)$$, thus, in VE, you end up with $$\sum_{t} P(L \vert t) P(t)$$.   


    __General Variable Elimination - Algorithm:__  
    ![img](/main_files/ml/kmeans/12.png){: width="90%"}  



    __VE - Computational and Space Complexity:__  
    {: #lst-p}
    * The computational and space complexity of variable elimination is determined by the largest factor.  
    * The __elimination ordering__ can greatly affect the size of the largest factor.  
    * There does NOT always exist an ordering that only results in small factors.  
    * __VE__ is <span>NP-Hard</span>{: style="color: goldenrod"}:  
        * __Proof__:  
            We can reduce *__3-Sat__* to a BN-Inference problem.  
            We can encode a _Constrained Satisfiability Problem (CSP)_ in a BN and use it to give a solution to the CSP; if the CSP consists of 3 clauses, then finding a solution for the CSP via BN-Inference is equivalent to solving 3-Sat.  
            <button>Analysis</button>{: .showText value="show" onclick="showTextPopHide(event);"}
            ![img](https://cdn.mathpix.com/snip/images/8ZMywFLFKbZr7mhjmbryM_Mr7sny3j2Bmjb_-gr2kS0.original.fullsize.png){: width="100%" hidden=""}  
    * Thus, __inference in Bayes’ nets is NP-hard__{: style="color: goldenrod"}.  
        __No known efficient probabilistic inference in general.__  

    __Polytrees:__  
    A __Polytree__ is a directed graph with no undirected cycles.  
    For polytrees we can always find an ordering that is efficient.  
    * __Cut-set conditioning for Bayes’ net inference:__ Choose set of variables such that if removed only a polytree remains.   
    <br>  


4. **Sampling:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}  
    __Sampling__ is the process of generating observations/_samples_ from a distribution.  
    \- Sampling is like doing _repeated_ (probabilistic) __simulation__.  
    \- Sampling could be used for __learning__ (e.g. RL). But in the context of BNs, it is used for __Inference__.  
    \- Sampling provides a way to do _efficient_ inference, by presenting us with a <span>tradeoff between accuracy and computation (time)</span>{: style="color: goldenrod"}.  
    \- The __Goal__ is to prove that as the number of samples you generate $$N$$ goes to $$\infty$$, the approximation converges to the true probability you are trying to compute.  
    \- Using sampling in a BN from the entire network is necessary, because listing all the outcomes is too expensive even if we can create them given infinite time.  

    __Idea/Algorithm for Inference:__  
    {: #lst-p}
    * Draw $$N$$ samples from a sampling distribution $$S$$  
    * Compute an approximate posterior probability
    * Show this converges to the true probability $$P$$   

    __Sampling from a given distribution:__  
    {: #lst-p}
    * Get sample $$u$$ from __uniform distribution__ over $$[0,1)$$  
    * Convert this sample $$u$$ into an outcome for the given distribution by having each target outcome associated with a sub-interval of $$[0,1)$$ with sub-interval size equal to probability of the outcome  
    ![img](https://cdn.mathpix.com/snip/images/64k37lx3GpRcNnLpuyn9WgIzIN6GUi1kC3GisMc-iEo.original.fullsize.png){: width="70%"}  

    __Sampling Algorithms in BNs:__  
    {: #lst-p}
    * Prior Sampling
    * Rejection Sampling
    * Likelihood Weighting
    * Gibbs Sampling


    __Prior Sampling:__{: style="color: red"}  


    __Algorithm:__  
    {: #lst-p}
    * For $$i=1,2, \ldots, n$$  
        * Sample $$x_{i}$$ from $$P\left(X_{i} \vert \text { Parents }\left(X_{i}\right)\right)$$  
    * Return $$\left(x_{1}, x_{2}, \ldots, x_{n}\right)$$  

    __Notes:__  
    {: #lst-p}
    * This process generates samples with probability:  
        <p>$$
        \begin{aligned} S_{P S}\left(x_{1} \ldots x_{n}\right)=\prod_{i=1}^{n} P\left(x_{i} \vert \text { Parents }\left(X_{i}\right)\right)=P\left(x_{1} \ldots x_{n}\right) \\ \text { ...i.e. the BN's joint probability } \end{aligned}
        $$</p>  
    * Let the number of samples of an event be $$N_{P S}\left(x_{1} \cdots x_{n}\right)$$  
    * Thus,  
        <p>$$\begin{aligned} \lim _{N \rightarrow \infty} \widehat{P}\left(x_{1}, \ldots, x_{n}\right) &=\lim _{N \rightarrow \infty} N_{P S}\left(x_{1}, \ldots, x_{n}\right) / N \\ &=S_{P S}\left(x_{1}, \ldots, x_{n}\right) \\ &=P\left(x_{1} \ldots x_{n}\right) \end{aligned}$$</p>   
    * I.e., the sampling procedure is *__consistent__*   


    __Rejection Sampling:__{: style="color: red"}  
    __Rejection Sampling__  

    It is also *__consistent__*.  

    __Idea:__  
    {: #lst-p}
    Same as Prior Sampling, but no point in keeping all of the samples. We just tally the outcomes that match our evidence and __reject__ the rest.  

    __Algorithm:__  
    {: #lst-p}
    * Input: evidence instantiation  
    * For $$i=1,2, \ldots, n$$  
        * Sample $$x_{i}$$ from $$P\left(X_{i} \vert \text { Parents }\left(X_{i}\right)\right)$$  
        * If $x_{i}$ not consistent with evidence  
            * Reject: return - no sample is generated in this cycle  
    * Return $$\left(x_{1}, x_{2}, \ldots, x_{n}\right)$$   



    __Likelihood Weighting:__{: style="color: red"}  
    __Likelihood Weighting__  


    __Key Ideas:__  
    {: #lst-p}
    Fixes a problem with Rejection Sampling:  
    * If evidence is unlikely, rejects lots of samples  
    * Evidence not exploited as you sample  
    __Idea__: __*fix* evidence variables__ and sample the rest.  
    * __Problem:__ sample distribution not consistent!  
    * __Solution__: weight by probability of evidence given parents.  


    __Algorithm:__  
    {: #lst-p}
    * Input: evidence instantiation  
    * $$w=1.0$$  
    * for $$i=1,2, \dots, n$$  
        * if $$\mathrm{x}_ {\mathrm{i}}$$ is an evidence variable  
            * $$\mathrm{n} \mathrm{x} _  {\mathrm{i}}=$$ observation $$\mathrm{x}_ {\mathrm{i}}$$ for $$\mathrm{x}_ {\mathrm{i}}$$  
            * $$\operatorname{set} \mathrm{w}=\mathrm{w} * \mathrm{P}\left(\mathrm{x}_ {\mathrm{i}} \vert \text { Parents(X.) }\right.$$    
        * else  
            * Sample $$x_ i$$ from $$P\left(X _ {i} \vert \text { Parents }\left(X _ {i}\right)\right)$$  
    * Return $$\left(\mathrm{x}_ {1}, \mathrm{x}_ {2}, \ldots, \mathrm{x}_ {\mathrm{n}}\right), \mathrm{w}$$  


    __Notes:__  
    {: #lst-p}
    * Sampling distribution if $$z$$ sampled and $$e$$ fixed evidence  
        <p>$$S_{W S}(\mathbf{z}, \mathbf{e})=\prod_{i=1}^{l} P\left(z_{i} \vert \text { Parents }\left(Z_{i}\right)\right)$$</p>  
    * Now, samples have weights  
        <p>$$w(\mathbf{z}, \mathbf{e})=\prod_{i=1}^{m} P\left(e_{i} \vert \text { Parents }\left(E_{i}\right)\right)$$</p>  
    * Together, weighted sampling distribution is consistent  
        <p>$$\begin{aligned} S_{\mathrm{WS}}(z, e) \cdot w(z, e) &=\prod_{i=1}^{l} P\left(z_{i} \vert \text { Parents }\left(z_{i}\right)\right) \prod_{i=1}^{m} P\left(e_{i} \vert \text { Parents }\left(e_{i}\right)\right) \\ &=P(\mathrm{z}, \mathrm{e}) \end{aligned}$$</p>   
    * Likelihood weighting is good
        * We have taken evidence into account as we generate the sample  
        * E.g. here, $$W$$’s value will get picked based on the evidence values of $$S$$, $$R$$  
        * More of our samples will reflect the state of the world suggested by the evidence   
    * Likelihood weighting doesn’t solve all our problems  
        * Evidence influences the choice of downstream variables, but not upstream ones (C isn’t more likely to get a value matching the evidence)  
    * We would like to consider evidence when we sample every variable (leads to __Gibbs sampling__)   


    __Gibbs Sampling:__{: style="color: red"}  
    __Gibbs Sampling__  

    * Procedure: keep track of a full instantiation $$x_1, x_2, \ldots, x_n$$. Start with an arbitrary instantiation consistent with the evidence. Sample one variable at a time, conditioned on all the rest, but keep evidence fixed. Keep repeating this for a long time.
    * Property: in the limit of repeating this infinitely many times the resulting samples come from the correct distribution (i.e. conditioned on evidence).
    * Rationale: both upstream and downstream variables condition on evidence.
    * In contrast: likelihood weighting only conditions on upstream evidence, and hence weights obtained in likelihood weighting can sometimes be very small. Sum of weights over all samples is indicative of how many “effective” samples were obtained, so we want high weight.   

    * Gibbs sampling produces sample from the query distribution $$P(Q \vert \text { e })$$ in limit of re-sampling infinitely often  
    * Gibbs sampling is a special case of more general methods called __Markov chain Monte Carlo (MCMC)__ methods  
        * __Metropolis-Hastings__ is one of the more famous __MCMC__ methods (in fact, Gibbs sampling is a special case of Metropolis-Hastings)  
    * __Monte Carlo Methods__ are just sampling  

    __Algorithm by Example:__  
    {: #lst-p}
    ![img](https://cdn.mathpix.com/snip/images/KSV3YwhhYal5g8aKVludJcV2vA6BYyBsUPJxVmHP_h4.original.fullsize.png){: width="80%"}  

    __Efficient Resampling of One Variable:__   
    {: #lst-p}
    * Sample from $$\mathrm{P}(\mathrm{S} \vert+\mathrm{c},+\mathrm{r},-\mathrm{w})$$:  
        <p>$$\begin{aligned} P(S \vert+c,+r,-w) &=\frac{P(S,+c,+r,-w)}{P(+c,+r,-w)} \\ &=\frac{P(S,+c,+r,-w)}{\sum_{s} P(s,+c,+r,-w)} \\ &=\frac{P(+c) P(S \vert+c) P(+r \vert+c) P(-w \vert S,+r)}{\sum_{s} P(+c) P(s \vert+c) P(+r \vert+c) P(-w \vert s,+r)} \\ &=\frac{P(+c) P(S \vert+c) P(+r \vert+c) P(-w \vert S,+r)}{P(+c) P(+r \vert+c) \sum_{s} P(s \vert+c)} \\ &=\frac{P(S \vert+c) P(-w \vert S,+r)}{\sum_{s} P(s \vert+c) P(-w \vert s,+r)} \end{aligned}$$</p>  
    * Many things cancel out – only CPTs with $$S$$ remain!  
    * More generally: only CPTs that have resampled variable need to be considered, and joined together  


    __Bayes’ Net Sampling Summary:__{: style="color: red"}  
    <button>Summary</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/U2mYDfFzMnaqL7fI4uA1hSlp5XWAq2OXLYW9RN9JlsA.original.fullsize.png){: width="100%" hidden=""}  
    <br>

5. **Decision Networks / VPI (Value of Perfect Information):**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}  
    [Decision Networks / VPI (188)](https://www.youtube.com/watch?v=19sr7yKV56I&list=PL7k0r4t5c108AZRwfW-FhnkZ0sCKBChLH&index=17)  
    <br>
{: hidden=""}


<!--6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents26}  
7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents27}  
8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents28}  
-->

***

<!-- ## THIRD
{: #content3} -->

<!-- 1. **HMMs:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}  
    <button>Markov Models and HMMs</button>{: .showText value="show"
     onclick="showText_withParent_PopHide(event);"}
    <iframe hidden="" src="https://inst.eecs.berkeley.edu/~cs188/fa18/assets/notes/n8.pdf" frameborder="0" height="780" width="600" title="Weight Normalization" scrolling="auto"></iframe> -->

<!-- 2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}   -->
<!-- 3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}     
4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents34}     
5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents35}    
6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents36}     
7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents37}     
8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents38}     
 -->

***

## Random Field Techniques
{: #content4}

<button>Discriminative/Generative Model Relationships</button>{: .showText value="show" onclick="showTextPopHide(event);"}
![img](https://cdn.mathpix.com/snip/images/VLm509wFwY3vY91C6YDrgt2hv1cE5YrjCnwC5LkFDS0.original.fullsize.png){: width="100%" hidden=""}  

* [An Introduction to Conditional Random Fields & graphical models (Thesis!)](https://www.research.ed.ac.uk/portal/files/10482724/crftut_fnt.pdf)  
* [Classical Probabilistic Models and Conditional Random Fields (Technical Report!)](https://my.eng.utah.edu/~cs6961/papers/klinger-crf-intro.pdf)  
* [HMM, MEMM, and CRF: A Comparative Analysis of Statistical Modeling Methods (Blog)](https://medium.com/@Alibaba_Cloud/hmm-memm-and-crf-a-comparative-analysis-of-statistical-modeling-methods-49fc32a73586)  
* [Intro to Conditional Random Field (blog!)](http://blog.echen.me/2012/01/03/introduction-to-conditional-random-fields/)  



1. **Random Field:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents41}  
    A __Random Field__ is a random function over an arbitrary domain (usually a multi-dimensional space such as $$\mathbb{R}^{n}$$ ). That is, it is a function $$f(x)$$ that takes on a random value at each point $$x \in \mathbb{R}^{n}$$ (or some other domain). It is also sometimes thought of as a synonym for a stochastic process with some restriction on its index set. That is, by modern definitions, a random field is a generalization of a stochastic process where the underlying parameter need no longer be real or integer valued "but can instead take values that are multidimensional vectors on some manifold.  

    __Formally__  
    Given a probability space $$(\Omega, \mathcal{F}, P),$$ an $$X$$ -valued random field is a collection of $$X$$ -valued random variables indexed by elements in a topological space $$T$$. That is, a random field $$F$$ is a collection  
    <p>$$\left\{F_{t} : t \in T\right\}$$</p>  
    where each $$F_{t}$$ is an $$X$$-valued random variable.  

    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * [Random Field (wiki)](https://en.wikipedia.org/wiki/Random_field)  
    * __Generative vs Discriminative Models for Sequence Labeling Tasks:__  
        Generative model makes more restrictive assumption about the distribution of $$x$$.  
        "Unlike traditional generative random fields, CRFs only model the conditional distribution $$p(t | x)$$ and do not explicitly model the marginal $$p(x)$$. Note that the labels $$t i$$ are globally conditioned on the whole observation $$x$$ in CRF. Thus, we do not assume that the observed data $$x$$ are conditionally independent as in a generative random field." - Minka  
    <br>

<!-- 2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents42}   -->

<!--
4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents44}     
5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents45}    
6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents46}     
7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents47}     
8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents48}     
 -->