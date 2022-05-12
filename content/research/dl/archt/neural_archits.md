---
layout: NotesPage
title: Neural Networks <br> Architectures & Interpretations
permalink: /work_files/research/dl/archits/nns
prevLink: /work_files/research/dl.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Neural Architectures](#content1)
  {: .TOC1}
  <!-- * [SECOND](#content2)
  {: .TOC2} -->
</div>

***
***


__Resources:__{: style="color: red"}  
{: #lst-p}
* [Types of artificial neural networks (wiki!)](https://en.wikipedia.org/wiki/Types_of_artificial_neural_networks)  
* [Artificial Neural Networks Complete Description (wiki!)](https://en.wikipedia.org/wiki/Artificial_neural_network)  
* [History of ANNs (wiki!)](https://en.wikipedia.org/wiki/History_of_artificial_neural_networks)  
* [Mathematics of ANNs (wiki)](https://en.wikipedia.org/wiki/Mathematics_of_artificial_neural_networks)  
* [Deep Learning vs Probabilistic Graphical Models vs Logic (Blog!)](http://www.computervisionblog.com/2015/04/deep-learning-vs-probabilistic.html)  
* [A Cookbook for Machine Learning: Vol 1 (Blog!)](https://www.inference.vc/design-patterns/)  


__Interpretation of NNs:__{: style="color: red"}  
{: #lst-p}
* Schmidhuber was a pioneer for the view of "neural networks as programs", which is claimed in his blog post. As opposed to the "representation learning view" by Hinton, Bengio, and other people, which is currently dominant in deep learning.   




## Neural Architectures
{: #content1}

<!-- 1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}   -->

2. **Neural Architectures - Graphical and Probabilistic Properties:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  

    <button>Properties</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
    * __FFN__ 
        * Directed
        * Acyclic
        * ?
    * __MLP__ 
        * Directed
        * Acyclic
        * Fully Connected (Complete?)
    * __CNN__ 
        * Directed
        * Acyclic
        * ?
    * __RNN__ 
        * Directed
        * Cyclic
        * ?
    * __Hopfield__ 
        * Undirected
        * Cyclic
        * Complete
    * __Boltzmann Machine__ 
        * Undirected
        * Cyclic
        * Complete
    * __RBM__ 
        * Undirected
        * Cyclic
        * Bipartite
    * __Bayesian Networks__ 
        * Directed
        * Acyclic
        * ?
    * __HMMs__ 
        * Directed
        * Acyclic
        * ?
    * __MRF__ 
        * Undirected
        * Cyclic
        * ?
    * __CRF__ 
        * Undirected
        * Cyclic
        * ?
    * __DBN__ 
        * Directed
        * Acyclic
        * ?
    * __GAN__ 
        * ?
        * ?
        * Bipartite-Complete
    {: hidden=""}

    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * [NNs Graphical VS Functional view (wiki!)](https://en.wikipedia.org/wiki/Mathematics_of_artificial_neural_networks#Neural_networks_as_functions)  
    <br>

22. **Neural Architectures:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents122}  
    __FeedForward Network:__{: style="color: red"}  
    {: #lst-p}
    * __Representations__: 
        * __Representational-Power:__ Universal Function Approximator.  
            Learns non-linear features.  
    * __Input Structure__: 
        * 
        * __Size:__ Fixed-Sized Inputs.  
    * __Transformation/Operation__: Linear-Transformations (Matrix-Multiplication).  
    * __Inductive Biases__: 
    * __Computational Power__: 

    __Convolutional Network:__{: style="color: red"}  
    {: #lst-p}
    * __Representations__:  
        * __Representational-Power:__ Universal Function Approximator.  
        * __Representations Properties__:  
            * __Translational-Equivariance__ via Convolutions (Translational-Equivariant Representations)  
            * __Translational-Invariance__ via Pooling  

    * __Input Structure__:  
        * Inputs with grid-like topology.  
            Images, Time-series, Sentences.  
        * __Size:__ Variable-Sized Inputs.  
    * __Transformation/Operation__: Convolution.  
    * __Inductive Biases__:  
        * __Local-Connectivity__: Spatially Local Correlations.  


    __Recurrent Network:__{: style="color: red"}  
    {: #lst-p}
    * __Representations__:  
        * __Representational-Power:__
    * __Input Structure__:  
        * Sequential Data.  
            Sentences, Time-series, Images.  
    * __Transformation/Operation__: Gated Linear-Transformations (Matrix-Multiplication).  
    * __Inductive Biases__: 
    * __Computational Power (Model of Computation)__: Turing Complete (Universal Turing Machine).  
        
    * __Mathematical Model/System__: Non-Linear Dynamical System.  


    __Transformer Network:__{: style="color: red"}  
    {: #lst-p}
    * __Representations__:  
        * __Representational-Power:__
    * __Input Structure__:  


    __Recursive Network:__{: style="color: red"}  
    {: #lst-p}
    * __Representational-Power:__
    * __Input Structure__: Any Hierarchical Structure.  


    __Further Network Architectures (More Specialized):__{: style="color: red"}  
    <button>List</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    * __Residual Network__: 
    * __Highway Network__: 
    * __Reversible Network__: 
    * __Generative Adversarial Network__: 
    * __Autoencoder Network__: 
    * __Symmetrically Connected Networks__:  
        * __Hopfield Network__: 
        * __Boltzmann Machines__: 
    {: hidden=""}

    * [Types of ANNs (wiki)](https://en.wikipedia.org/wiki/Types_of_artificial_neural_networks)  
    <br>

33. **Types/Taxonomy of Neural Networks:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents133}  
    <button>List</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    * __FeedForward Neural Networks__{: style="color: red"}  
        * __Group method of data handling (GMDH) Network__{: style="color: blue"}  
        * __Autoencoder Network__{: style="color: blue"}  
        * __Probabilistic Neural Network__{: style="color: blue"}  
        * __Time Delay Neural Network__{: style="color: blue"}  
        * __Convolutional Neural Network__{: style="color: blue"}  
        * __(Vanilla/Tensor) Deep Stacking Network__{: style="color: blue"}  
    * __Recurrent Neural Networks:__{: style="color: red"}  
        * __Fully Recurrent Neural Network__{: style="color: blue"}  
        * __Hopfield Network__{: style="color: blue"}  
        * __Boltzmann Machine Network__{: style="color: blue"}  
        * __Self-Organizing Map__{: style="color: blue"}  
        * __Learning Vector Quantization__{: style="color: blue"}  
        * __Simple Recurrent__{: style="color: blue"}  
        * __Reservoir Computing__{: style="color: blue"}  
        * __Echo State__{: style="color: blue"}  
        * __Long Short-term Memory (LSTM)__{: style="color: blue"}  
        * __Bi-Directional__{: style="color: blue"}  
        * __Hierarchical__{: style="color: blue"}  
        * __Stochastic__{: style="color: blue"}  
        * __Genetic Scale__{: style="color: blue"}  
    * __Memory Networks__{: style="color: red"}  
        * __One-Shot Associative Memory__{: style="color: blue"}  
        * __Hierarchical Temporal Memory__{: style="color: blue"}  
        * __Holographic Associative Memory__{: style="color: blue"}  
        * __LSTM-related Differentiable Memory Structures__{: style="color: blue"}  
            <button>List</button>{: .showText value="show" onclick="showTextPopHide(event);"}
            * Differentiable push and pop actions for alternative memory networks called neural stack machines
            * Memory networks where the control network's external differentiable storage is in the fast weights of another network
            * LSTM forget gates
            * Self-referential RNNs with special output units for addressing and rapidly manipulating the RNN's own weights in differentiable fashion (internal storage)
            * Learning to transduce with unbounded memory  
            {: hidden=""}
        * __Neural Turing Machines__{: style="color: blue"}  
        * __Semantic Hashing__{: style="color: blue"}  
        * __Pointer Networks__{: style="color: blue"}  
    {: hidden=""}
    <br>


3. **Neural Networks and Graphical Models:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    __Deep NNs as PGMs:__{: style="color: red"}  
    You can view a deep neural network as a graphical model, but here, the CPDs are not probabilistic but are deterministic. Consider for example that the input to a neuron is $$\vec{x}$$ and the output of the neuron is $$y .$$ In the CPD for this neuron we have, $$p(\vec{x}, y)=1,$$ and $$p(\vec{x}, \hat{y})=0$$ for $$\hat{y} \neq y .$$ Refer to the section 10.2 .3 of Deep Learning Book for more details.  
    <br>

3. **Neural Networks as Gaussian Processes:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    It's long been known that these deep tools can be related to Gaussian processes, the ones I mentioned above. Take a neural network (a recursive application of weighted linear functions followed by non-linear functions), put a probability distribution over each weight (a normal distribution for example), and with infinitely many weights you recover a Gaussian process (see [Neal](http://www.cs.toronto.edu/pub/radford/thesis.pdf) or [Williams](http://papers.nips.cc/paper/1197-computing-with-infinite-networks.pdf) for more details).  

    We can think about the finite model as an approximation to a Gaussian process.  
    When we optimise our objective, we minimise some "distance" (KL divergence to be more exact) between your model and the Gaussian process.  
    
    <button>Illustration</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/9AhiNOhdojUkjscIHxrF6VDwDB6C87sJQk0te27ahY4.original.fullsize.png){: width="100%" hidden=""}  

4. **Neural Layers and Block Architectures:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    * __Feed-Forward Layer__:  
        * __Representational-Power:__ Universal Function Approximator.  
            Learns non-linear features.  
        * __Input Structure__: 
    * __Convolutional Layer__:  
        * __Representational-Power:__ 
        * __Input Structure__:
    * __Recurrent Layer__:  
        * __Representational-Power:__ 
        * __Input Structure__:
    * __Recursive Layer__:  
        * __Representational-Power:__ 
    * __Attention Layer__: 
        * __Representational-Power:__ 
        * __Input Structure__: 
    * __Attention Block__: 
        * __Representational-Power:__ 
    * __Residual Block__: 
        * __Representational-Power:__ 
    * __Reversible Block__: 
        * __Representational-Power:__ 
    * __Reversible Layer__: 
        * __Representational-Power:__ 
    <br>

0. **Notes:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents10}  
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
    * The __Bias Parameter__:  
        * [Role of Bias in a NN](https://stackoverflow.com/questions/2480650/role-of-bias-in-neural-networks)  
    * __Failures of Neural Networks__:  
        * [Vanilla Sequence-to-Sequence Neural Nets cannot Model Reduplication (paper)](https://scholarworks.umass.edu/cgi/viewcontent.cgi?article=1001&context=ics_owplinguist)  
    * __Bayesian Deep Learning__:  
        <button>List of Topics</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        * Uncertainty in deep learning,
        * Applications of Bayesian deep learning,
        * Probabilistic deep models (such as extensions and application of Bayesian neural networks),
        * Deep probabilistic models (such as hierarchical Bayesian models and their applications),
        * Generative deep models (such as variational autoencoders),
        * Information theory in deep learning,
        * Deep ensemble uncertainty,
        * NTK and Bayesian modeling,
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
    <br>




<!-- 5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18}
 -->



