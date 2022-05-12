---
layout: NotesPage
title: FeedForward Neural Networks and Multilayer Perceptron
permalink: /work_files/research/dl/archits/fnn&mlp
prevLink: /work_files/research/dl/archits.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [FeedForward Neural Network](#content1)
  {: .TOC1}
  * [Multilayer Perceptron](#content2)
  {: .TOC2}
  * [Deep FeedForward Neural Network](#content3)
  {: .TOC3}
  * [(Gradient-Based) Learning for FNNs](#content4)
  {: .TOC4}
</div>

***
***

![img](https://cdn.mathpix.com/snip/images/ijocrRQow82xG79k_kuSaZuJgOPfpPW4v8SYvbHSXXU.original.fullsize.png){: width="80%"}  


## FeedForward Neural Network
{: #content1}

1. **FeedForward Neural Network:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    The __FeedForward Neural Network (FNN)__ is an _artificial neural network_ wherein the connections between the nodes do _not_ form a _cycle_, allowing the information to move only in one direction, forward, from the input layer to the subsequent layers.  
    <br>

2. **Architecture:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}    
    An FNN consists of one or more layers, each consisting of nodes (simulating biological neurons) that hold a certain _wight value $$w_{ij}$$._ Those weights are usually multiplied by the input values (in the input layer) in each node and, then, summed; finally, one can apply some sort of activation function on the multiplied values to simulate a response (e.g. 1-0 classification).  
    <br>

3. **Classes of FNNs:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}    
    There are many variations of FNNs. As long as they utilize FeedForward control signals and have a layered structure (described above) they are a type of FNN:  
    * [__Single-Layer Perceptron__](http://localhost:8889/work_files/research/ml/1/2):  
        A <span>linear binary classifier</span>{: style="color: purple"}, the __single-layer perceptron__ is the simplest feedforward neural network. It consists of a single layer of output nodes; the inputs are multiplied by a series of weights, effectively, being fed directly to the outputs where they values are summed in each node, and if the value is above some threshold (typically 0) the neuron fires and takes the activated value (typically 1); otherwise it takes the deactivated value (typically 0).  
        <p>$$f(\mathbf{x})=\left\{\begin{array}{ll}{1} & {\text { if } \mathbf{w} \cdot \mathbf{x}+b>0} \\ {0} & {\text { otherwise }}\end{array}\right.$$</p>  
        In the context of neural networks, a perceptron is an artificial neuron using the [__Heaviside step function__](https://en.wikipedia.org/wiki/Heaviside_step_function) as the activation function.   
    * [__Multi-Layer Perceptron__](#content2):  
        This class of networks consists of multiple layers of computational units, usually interconnected in a feed-forward way. Each neuron in one layer has directed connections to the neurons of the subsequent layer. In many applications the units of these networks apply a sigmoid function as an activation function.  
        

<!-- 4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  
6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}  
7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}  
8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18} -->  

***

## Multilayer Perceptron
{: #content2}

1. **Multilayer Perceptron:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    The __Multilayer Perceptron (MLP)__ is a class of _FeedForward Neural Networks_ that is used for learning from data.  
    <br>

2. **Architecture:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}    
    The MLP consists of at least three layers of nodes: *__input layer__*, *__hidden layer__*, and an *__output layer__*.  

    The layers in a neural network are connected by certain weights and the MLP is known as a __fully-connected network__ where each neuron in one layer is connected with a weight $$w_{ij}$$ to every node in the following layer.  
    
    Each node (except for the input nodes) uses a __non-linear activation function__ that were developed to _model the frequency of **action potential** (firing) of biological neurons_.  
    <br>

3. **Learning:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}    
    The MLP employs a __supervised learning__ technique called __backpropagation__.  
    Learning occurs by changing the weights, connecting the layers, based on the amount of error in the output compared to the expected result. Those weights are changed by using _gradient-methods_ to optimize a, given, objective function (called the __loss function__).  
    <br>

4. **Properties:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}  
    * Due to their _non-linearity_, MLPs can distinguish and model non-linearly-separable data    
    * According to [__Cybenko's Theorem__](https://pdfs.semanticscholar.org/05ce/b32839c26c8d2cb38d5529cf7720a68c3fab.pdf), MLPs are *__universal function approximators__*; thus, they can be used for _regression analysis_ and, by extension, _classification_  
    * Without the _non-linear activation functions_, MLPs will be identical to __Perceptrons__, since Linear Algebra shows that the linear transformations in many hidden layers can be collapsed into one linear-transformation  
    <br>

<!-- 5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}  

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents26}  

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents27}  

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents28} -->  

***

## [Deep FeedForward Neural Network](/work_files/research/dl/theory/dl_book_pt2#content1)
{: #content3}

***

## [(Gradient-Based) Learning for FNNs](/work_files/research/dl/theory/dl_book_pt2#content2)
{: #content4}

***

<!-- ## [Activation Functions for FNNs](/work_files/research/dl/theory/dl_book_pt2#content2)
{: #content4} -->