---
layout: NotesPage
title: The Theory of Learning
permalink: /work_files/research/dl/theory/theory_of_learning
prevLink: /work_files/research/dl/theory.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Learning](#content1)
  {: .TOC1}
  * [Types of Learning](#content2)
  {: .TOC2}
  * [Theories of Learning](#content3)
  {: .TOC3}
</div>

***
***

* [Learning (wiki)](https://en.wikipedia.org/wiki/Learning)  
* [Hebbian Theory (wiki)](https://en.wikipedia.org/wiki/Hebbian_theory)  
* [Learning Exercises](https://neuronaldynamics-exercises.readthedocs.io/en/latest/exercises/hopfield-network.html)  
* [Neuronal Dynamics - From single neurons to networks and models of cognition](https://neuronaldynamics.epfl.ch/online/index.html)  
* [Theoretical Impediments to ML With Seven Sparks from the Causal Revolution (J Pearl Paper!)](https://arxiv.org/abs/1801.04016)  
* [ML Intro (Slides!)](https://web.engr.oregonstate.edu/~tgd/classes/534/slides/part1.pdf)  
* [A Few Useful Things to Know About Machine Learning (Blog!)](https://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf)  
* [Introduction to Intelligence, Learning, and AI (Blog)](https://www.iro.umontreal.ca/~pift6266/H10/notes/mlintro.html)  
* [What does it mean for a machine to “understand”? (Blog!)](https://medium.com/@tdietterich/what-does-it-mean-for-a-machine-to-understand-555485f3ad40)  


* What’s the difference between learning statistical properties of a dataset and understanding?  
    * Statistical properties tell you the correlations (associations) between things , which enables you to predict the future.  Understanding is the ability to imagine counterfactuals (things that *could* happen) in order to plan for and reflect on the past, future and present.  
    * In short, learning statistical properties only lets you passively predict the external world (prediction). Understanding lets you actively interact with it via formulation of symbolic plans representing the world (including yourself) as objects, events and relations (reflection)  
* Can we have real understanding if we confined ourselves in language? I think even for human, language understanding means knowing what each word would mean in the world (physical or non-physical). Right?  




## Learning
{: #content1}

1. **Learning:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    __Learning__ is the process of acquiring new, or modifying existing, knowledge, behaviors, skills, values, or preferences.  
    <br>

<!-- 2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}
3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}
4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}
5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}
6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16} -->

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}  

***

## Types of Learning
{: #content2}

1. **Hebbian (Associative) Learning:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    __Hebbian/Associative Learning__ is the process by which a person or animal learns an association between two stimuli or events, in which, simultaneous activation of cells leads to pronounced increases in synaptic strength between those cells.  

    __Hebbian Learning in Artificial Neural Networks:__{: style="color: red"}  
    From the pov of ANNs, Hebb's principle can be described as a method of __determining how to alter the weights between model neurons__.  
    {: #lst-p}
    * The weight between two neurons:  
        * Increases if the two neurons activate simultaneously,  
        * Reduces if they activate separately.  
    * Nodes that tend to be either both positive or both negative at the same time have strong positive weights, 
        while those that tend to be opposite have strong negative weights.  

    __Hebb's Rule:__  
    The change in the $i$ th synaptic weight $w_{i}$ is equal to a learning rate $\eta$ times the $i$ th input $x_{i}$ times the postsynapic response $y$:  
    <p>$$\Delta w_{i}=\eta x_{i} y$$</p>  
    where in the case of a linear neuron:  
    <p>$$y=\sum_{j} w_{j} x_{j}$$</p>  


    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * It is regarded as the neuronal basis of __unsupervised learning__.  
    <br>


2. **Supervised Learning:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}
    __Supervised Learning__: the task of learning a function that maps an input to an output based on example input-output pairs.  
    ![img](/main_files/dl/theory/caltech/4.png){: width="70%"}  
    <br>

3. **Unsupervised Learning:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}  
    __Unsupervised Learning__: the task of making inferences, by learning a better representation, from some datapoints that do not have any labels associated with them.  
    ![img](/main_files/dl/theory/caltech/5.png){: width="70%"}  
    > Unsupervised Learning is another name for [Hebbian Learning](https://en.wikipedia.org/wiki/Hebbian_theory)  

    <button>Unsupervised Learning Algorithms</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    * Clustering
        * hierarchical clustering
        * k-means
        * mixture models
        * DBSCAN
    * Anomaly Detection: Local Outlier Factor
    * Neural Networks
        * Autoencoders
        * Deep Belief Nets
        * Hebbian Learning
        * Generative Adversarial Networks
        * Self-organizing map
    * Approaches for learning latent variable models such as
        * Expectation–maximization algorithm (EM)
        * Method of moments
        * Blind signal separation techniques
            * Principal component analysis
            * Independent component analysis
            * Non-negative matrix factorization
            * Singular value decomposition
    {: hidden=""}

    <br>

4. **Reinforcement Learning:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}  
    __Reinforcement Leaning__: the task of learning how software agents ought to take actions in an environment so as to maximize some notion of cumulative reward.  
    ![img](/main_files/dl/theory/caltech/6.png){: width="70%"}  
    <br>

5. **Semi-supervised Learning:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}  


6. **Zero-Shot Learning:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents26}  

7. **Transfer Learning:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents27}  

8. **Multitask Learning:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents28}  

9. **Domain Adaptation:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents29}  

***

## Theories of Learning
{: #content3}

<!-- 1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31} -->


<!-- 2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32} -->

<!-- 3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents34}

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents35}

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents36}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents37}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents38}

 -->

## Reasoning and Inference
{: #content4}

1. **Logical Reasoning:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents41}  
    ![img](https://cdn.mathpix.com/snip/images/vIoP1W7b3o_HHfP_qSux2x4EbCcJGoF2TPL2moWAUeQ.original.fullsize.png){: width="80%"}  

    * __Inductive Learning__ is the process of using observations to draw conclusions  
        * It is a method of reasoning in which the __premises are viewed as supplying <span>some</span>{: style="color: goldenrod"} evidence__ for the truth of the conclusion.  
        * It goes from <span>specific</span>{: style="color: goldenrod"} to <span>general</span>{: style="color: goldenrod"} (_"bottom-up logic"_).    
        * The truth of the conclusion of an inductive argument may be __probable__{: style="color: goldenrod"}, based upon the evidence given.  
    * __Deductive Learning__ is the process of using conclusions to form observations.  
        * It is the process of reasoning from one or more statements (premises) to reach a logically certain conclusion.  
        * It goes from <span>general</span>{: style="color: goldenrod"} to <span>specific</span>{: style="color: goldenrod"} (_"top-down logic"_).    
        * The conclusions reached ("observations") are necessarily __True__.  
    * __Abductive Learning__ is a form of __inductive learning__ where we use observations to draw the *__simplest__* and __most__ *__likely__* conclusions.  
        It can be understood as "__inference to the best explanation__".  
        It is used by _Sherlock Holmes_.  


    __In Mathematical Modeling (ML):__{: style="color: red"}  
    In the context of __Mathematical Modeling__ the three kinds of reasoning can be described as follows:  
    {: #lst-p}
    * The <span>construction/creation of the structure of the model</span>{: style="color: purple"} is __abduction__.  
    * <span>Assigning values (or probability distributions) to the parameters of the model</span>{: style="color: purple"} is __induction__.  
    * <span>Executing/running the model</span>{: style="color: purple"} is __deduction__.  

    <br>


2. **Inference:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents42}  
    __Inference__ has two definitions:  
    {: #lst-p}
    1. A conclusion reached on the basis of evidence and reasoning.  
    2. The process of reaching such a conclusion.  
    <br>


3. **Transductive Inference/Learning (Transduction):**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents43}  

    The __Goal__ of Transductive Learning is to “simply” <span>add labels to the unlabeled data by exploiting labelled samples</span>{: style="color: purple"}.  
    While, the goal of _inductive learning_ is to infer the correct mapping from $$X$$ to $$Y$$.  

    __Transductive VS Semi-supervised Learning:__{: style="color: red"}  
    __Transductive Learning__ is only concerned with the *__unlabeled__* data.   

    __Transductive Learning:__  
    ![img](https://cdn.mathpix.com/snip/images/vJc503Mbxku0OQ6C3ctRjIGvz5QVc56Z5ksmjxn_gi4.original.fullsize.png){: width="50%"}  
    __Inductive Learning:__  
    ![img](https://cdn.mathpix.com/snip/images/HcXQ1dT1_y6Vdxsm8TZL7jU408bHTuHLn492WVe3B-Q.original.fullsize.png){: width="50%"}  

    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * [Transductive Inference (wiki)](https://en.wikipedia.org/wiki/Transduction_(machine_learning))  
    <br>



<!-- 3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents43}

4. **Statistical Inference:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents44}  
-->
