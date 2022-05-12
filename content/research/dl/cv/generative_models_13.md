---
layout: NotesPage
title: Generative Models <br /> Unsupervised Learning
permalink: /work_files/research/dl/gm
prevLink: /work_files/research/dl/cv.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Unsupervised Learning](#content1)
  {: .TOC1}
  * [Generative Models](#content2)
  {: .TOC2}
  * [PixelRNN and PixelCNN](#content3)
  {: .TOC3}
  * [Variational Auto-Encoders](#content4)
  {: .TOC4}
  * [Generative Adversarial Networks (GANs)](#content5)
  {: .TOC5}
</div>

***
***

[Learning Deep Generative Models (pdf)](https://www.cs.cmu.edu/~rsalakhu/papers/annrev.pdf)  
[AutoRegressive Models (CS236 pdf)](https://deepgenerativemodels.github.io/notes/autoregressive/)  
[Deep Generative Models (CS236 pdf)](https://deepgenerativemodels.github.io/notes/index.html)  
[Deep Generative Models (Lecture)](https://www.youtube.com/watch?v=JrO5fSskISY)  
[CS294 Berkeley - Deep Unsupervised Learning](https://sites.google.com/view/berkeley-cs294-158-sp19/home)  



## Unsupervised Learning
{: #content1}

1. **Unsupervised Learning:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    __Data:__ $$x$$ Just data, no labels!   
    __Goal:__ Learn some underlying hidden _structure_ of the data  
    __Examples:__ Clustering, dimensionality reduction, feature learning, density estimation, etc.  
    <br>

***

## Generative Models
{: #content2}

Given some data $$\{(d,c)\}$$ of paired observations $$d$$ and hidden classes $$c$$:  

1. **Generative (Joint) Models:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    __Generative Models__ are __Joint Models__.  
    __Joint Models__ place probabilities $$\left(P(c,d)\right)$$ over both the observed data and the "target" (hidden) variables that can only be computed from those observed.  
    
    Generative models are typically probabilistic, specifying a joint probability distribution ($$P(d,c)$$) over observation and target (label) values, and tries to __Maximize__ this __joint Likelihood__.  
    > Choosing weights turn out to be trivial: chosen as the __relative frequencies__.  

    They address the problem of __density estimation__, a core problem in unsupervised learning.  

    __Examples:__  
    {: #lst-p}
    * Gaussian Mixture Model
    * Naive Bayes Classifiers  
    * Hidden Markov Models (HMMs)
    * Restricted Boltzmann Machines (RBMs)
    * AutoEncoders
    * Generative Adversarial Networks (GANs)


2. **Discriminative (Conditional) Models:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}  
    :   __Discriminative Models__ are __Conditional Models__.  
    :   __Conditional Models__ provide a model only for the "target" (hidden) variabless.  
        They take the data as given, and put a probability $$\left(P(c \vert d)\right)$$ over the "target" (hidden) structures given the data.  
    :   Conditional Models seek to __Maximize__ the __Conditional Likelihood__.  
        > This (maximization) task is usually harder to do.  
    :   __Examples:__  
        * Logistic Regression
        * Conditional LogLinear/Maximum Entropy Models  
        * Condtional Random Fields  
        * SVMs  
        * Perceptrons  
        * Neural Networks

3. **Generative VS Discriminative Models:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}  
    Basically, _Discriminative Models_ infer outputs based on inputs,  
    while _Generative Models_ generate, both, inputs and outputs (typically given some hidden paramters).  
    
    However, notice that the two models are usually viewed as complementary procedures.  
    One does __not__ necessarily outperform the other, in either classificaiton or regression tasks.   

4. **Example Uses of Generative Models:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}  
    :   * Clustering
        * Dimensionality Reduction
        * Feature Learning
        * Density Estimation

5. **Density Estimation:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}  
    :   __Generative Models__, given training data, will generate new samples from the same distribution.   
    :   They address the __Density Estimation__ problem, a core problem in unsupervised learning.  
    :   * __Types__ of Density Estimation:  
            * *__Explicit__*: Explicitly define and solve for $$p_\text{model}(x)$$  
            * *__Implicit__*: Learn model that can sample from $$p_\text{model}(x)$$ without explicitly defining it     

6. **Applications of Generative Models:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents26}  
    :   * Realistic samples for artwork
        * Super-Resolution
        * Colorization
        * Generative models of time-series data can be used for simulation and planning  
            > reinforcement learning applications  
        * Inference of __Latent Representations__ that can be useful as general feature descriptors 

7. **Taxonomy of Generative Models:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents27}  
    :   ![img](/main_files/cs231n/13/1.png){: width="100%"}  

***

## AutoRegressive Models - PixelRNN and PixelCNN
{: #content3}

[AutoRegressive Models (pdf)](https://deepgenerativemodels.github.io/notes/autoregressive/)  

1. **Fully Visible (Deep) Belief Networks:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}  
    __Deep Belief Network (DBNs)__ are generative graphical models, or alternatively a class of deep neural networks, composed of multiple layers of latent variables ("hidden units"), with connections between the layers but not between units within each layer.  
    
    DBNs undergo unsupervised training to _learn to probabilistically reconstruct the inputs_.  

    They generate an __Explicit Density Model__.  

    They use the __chain rule__ to _decompose the _likelihood of an image_ $$x$$ into products of 1-d distributions:  
    ![img](/main_files/cs231n/13/2.png){: width="70%"}    
    then, they __Maximize__ the __Likelihood__ of the training data.  

    The __conditional distributions over pixels__ are very _complex_.  
    We model them using a __neural network__. 

2. **PixelRNN:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}  
    :   is a proposed architecture (part of the class of __Auto-Regressive__ models) to model an explicit distribution of natural images in an _expressive, tractable,_ and _scalable_ way.  
    :   It sequentially predicts the pixels in an image along two spatial dimensions.  
    :   The Method __models__ the __discrete probability of the raw pixel values__ and __encodes the complete set of dependencies__ in an image.  
    :   The approach is to use probabilistic density models (like Gaussian or Normal distribution) to quantify the pixels of an image as a product of conditional distributions.  
        This approach turns the modeling problem into a sequence problem where the next pixel value is determined by all the previously generated pixel values.  
    :   * __Key Insights__:  
            * Generate image pixels starting from corner  
            * Dependency on previous pixels is modeled using an _LSTM_  
    :   ![img](/main_files/cs231n/13/3.png){: width="100%"}  
    :   * __The Model__:  
            * Scan the image, one row at a time and one pixel at a time (within each row)
            * Given the scanned content, predict the distribution over the possible values for the next pixel
            * Joint distribution over the pixel values is factorized into a product of conditional distributions thus causing the problem as a sequence problem
            * Parameters used in prediction are shared across all the pixel positions
            * Since each pixel is jointly determined by 3 values (3 colour channels), each channel may be conditioned on other channels as well
    :   * __Drawbacks__:   
            * Sequential training is __slow__
            * Sequential generation is __slow__   
    :   [Further Reading](https://gist.github.com/shagunsodhani/e741ebd5ba0e0fc0f49d7836e30891a7)

3. **PixelCNN:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}  
    :   Similar to the __PixelRNN__ model, the __PixelCNN__ models  the *__Pixel Distribution__* $$p(\vec{x})$$, where $$\vec{x} = (x_0, \ldots, x_n)$$ is the vector of pixel values of a given image.  
    :   Similarly, we use the chain rule for join distribution: $$p(x) = p(x_0) \prod_1^n p(x_i | x_{i<})$$.  
        > such that, the first pixel is independent, the second depends on the first, and the third depends on, both, the first and second, etc.  
    :   ![img](/main_files/cs231n/13/4.png){: width="40%"}  
    :   * __Key Insights__:  
            * Still generate image pixels starting from corner
            * Dependency on previous pixels now modeled using a CNN over context region
            * Training: maximize likelihood of training images  
    :   * __Upsides__:  
            * Training is faster than __PixelRNN__: since we can parallelize the convolutions because the context region values are known from the training images.  
    :   * __Issues__:  
            * Generation is still sequential, thus, slow.
    :   [Further Reading](http://sergeiturukin.com/2017/02/22/pixelcnn.html)


4. **Improving PixelCNN Performance:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents34}  
    * Gated Convolutional Layers 
    * Short-cut connections
    * Discretized logistic loss
    * Multi-scale
    * Training tricks

    __Further Reading__:  
    {: #lst-p}
    * *__PixelCNN++__* \| _Salimans et al. 2017_    
    * _Van der Oord et al. NIPS 2016_
    * __Pixel-Snail__  

5. **Pros and Cons of Auto-Regressive Models:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents35}  
    * __Pros__:   
        * Can explicitly compute likelihood $$p(x)$$
        * Explicit likelihood of training data gives good evaluation metric
        * Good Samples
    * __Cons__:  
        * Sequential Generation is __Slow__  

***

## Variational Auto-Encoders
{: #content4}

[__Auto-Encoders__](http://ahmedbadary.ml/work_files/research/dl/aencdrs) (_click to read more_) are unsupervised learning methods that aim to learn a representation (encoding) for a set of data in a smaller dimension.  
Auto-Encoders generate __Features__ that capture _factors of variation_ in the training data.

0. **Auto-Regressive Models VS Variational Auto-Encoders:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents40}  
    :   __Auto-Regressive Models__ defined a *__tractable__* (discrete) density function and, then, optimized the likelihood of training data:   
    :   $$p_\theta(x) = p(x_0) \prod_1^n p(x_i | x_{i<})$$  
    :   On the other hand, __VAEs__ defines an *__intractable__* (continuous) density function with latent variable $$z$$:  
    :   $$p_\theta(x) = \int p_\theta(z) p_\theta(x|z) dz$$
    :   but cannot optimize directly; instead, derive and optimiz a lower bound on likelihood instead.  

1. **Variational Auto-Encoders (VAEs):**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents41}  
    :   __Variational Autoencoder__ models inherit the autoencoder architecture, but make strong assumptions concerning the distribution of latent variables.  
    :   They use variational approach for latent representation learning, which results in an additional loss component and specific training algorithm called Stochastic Gradient Variational Bayes (SGVB).  

2. **Assumptions:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents42}  
    :   VAEs assume that: 
        * The data is generated by a directed __graphical model__ $$p(x\vert z)$$ 
        * The encoder is learning an approximation $$q_\phi(z|x)$$ to the posterior distribution $$p_\theta(z|x)$$  
            where $${\displaystyle \mathbf {\phi } }$$ and $${\displaystyle \mathbf {\theta } }$$ denote the parameters of the encoder (recognition model) and decoder (generative model) respectively.  
        * The training data $$\left\{x^{(i)}\right\}_{i=1}^N$$ is generated from underlying unobserved (latent) representation $$\mathbf{z}$$

3. **The Objective Function:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents43}    
    :   $${\displaystyle {\mathcal {L}}(\mathbf {\phi } ,\mathbf {\theta } ,\mathbf {x} )=D_{KL}(q_{\phi }(\mathbf {z} |\mathbf {x} )||p_{\theta }(\mathbf {z} ))-\mathbb {E} _{q_{\phi }(\mathbf {z} |\mathbf {x} )}{\big (}\log p_{\theta }(\mathbf {x} |\mathbf {z} ){\big )}}$$
    :   where $${\displaystyle D_{KL}}$$ is the __Kullback–Leibler divergence__ (KL-Div).  

4. **The Generation Process:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents44}  
    :   
    :   ![img](/main_files/cs231n/13/5.png){: width="40%"} 

5. **The Goal:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents45}  
    :   The goal is to estimate the true parameters $$\theta^\ast$$ of this generative model.

6. **Representing the Model:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents46}  
    :   * To represent the prior $$p(z)$$, we choose it to be simple, usually __Gaussian__  
        * To represent the conditional (which is very complex), we use a neural-network  

7. **Intractability:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents47}  
    :   The __Data Likelihood__:  
    :   $$p_\theta(x) = \int p_\theta(z) p_\theta(x|z) dz$$
    :   is intractable to compute for every $$z$$.  
    :   Thus, the __Posterior Density__:  
    :   $$p_\theta(z|x) = \dfrac{p_\theta(x|z) p_\theta(z)}{p_\theta(x)} = \dfrac{p_\theta(x|z) p_\theta(z)}{\int p_\theta(z) p_\theta(x|z) dz}$$ 
    :   is, also, intractable

8. **Dealing with Intractability:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents48}  
    :   In addition to decoder network modeling $$p_\theta(x\vert z)$$, define additional encoder network $$q_\phi(z\vert x)$$ that approximates $$p_\theta(z\vert x)$$
    :   This allows us to derive a __lower bound__ on the data likelihood that is tractable, which we can optimize.  

9. **The Model:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents49}  
    :   * The __Encoder__ (recognition/inference) and __Decoder__ (generation) networks are probabilistic and output means and variances of each the conditionals respectively:  
            ![img](/main_files/cs231n/13/6.png){: width="70%"}   
        * The generation (forward-pass) is done via sampling as follows:  
            ![img](/main_files/cs231n/13/7.png){: width="72%"}   

10. **The Log-Likelihood of Data:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents410}  
    :   * Deriving the Log-Likelihood:  
    :   ![img](/main_files/cs231n/13/8.png){: width="100%"}   

11. **Training the Model:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents411}  
    :   

12. **Pros, Cons and Research:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents412}  
    :   * __Pros__: 
            * Principled approach to generative models
            * Allows inference of $$q(z\vert x)$$, can be useful feature representation for other tasks  
    :   * __Cons__: 
            * Maximizing the lower bound of likelihood is okay, but not as good for evaluation as Auto-regressive models
            * Samples blurrier and lower quality compared to state-of-the-art (GANs)
    :   * __Active areas of research__:   
            * More flexible approximations, e.g. richer approximate posterior instead of diagonal Gaussian
            * Incorporating structure in latent variables


***

## Generative Adversarial Networks (GANs)
{: #content5}

0. **Auto-Regressive Models VS Variational Auto-Encoders VS GANs:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents40}  
    :   __Auto-Regressive Models__ defined a *__tractable__* (discrete) density function and, then, optimized the likelihood of training data:   
    :   $$p_\theta(x) = p(x_0) \prod_1^n p(x_i | x_{i<})$$  
    :   While __VAEs__ defined an *__intractable__* (continuous) density function with latent variable $$z$$:  
    :   $$p_\theta(x) = \int p_\theta(z) p_\theta(x|z) dz$$
    :   but cannot optimize directly; instead, derive and optimize a lower bound on likelihood instead.  
    :   On the other hand, __GANs__ rejects explicitly defining a probability density function, in favor of only being able to sample.     

1. **Generative Adversarial Networks:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents51}  
    :   are a class of AI algorithms used in unsupervised machine learning, implemented by a system of two neural networks contesting with each other in a zero-sum game framework.

2. **Motivation:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents52}  
    :   * __Problem__: we want to sample from complex, high-dimensional training distribution; there is no direct way of doing this.  
        * __Solution__: we sample from a simple distribution (e.g. random noise) and learn a transformation that maps to the training distribution, by using a __neural network__.  
    :   * __Generative VS Discriminative__: discriminative models had much more success because deep generative models suffered due to the difficulty of approximating many intractable probabilistic computations that arise in maximum likelihood estimation and related strategies, and due to difficulty of leveraging the benefits of piecewise linear units in the generative context.  
        GANs propose a new framework for generative model estimation that sidesteps these difficulties.      

3. **Structure:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents53}  
    :   * __Goal__: estimating generative models that capture the training data distribution  
        * __Framework__: an adversarial process in which two models are simultaneously trained a generative model $$G$$ that captures the data distribution, and a discriminative model $$D$$ that estimates the probability that a sample came from the training data rather than $$G$$.  
        * __Training__:  
            * $$G$$ maximizes the probability of $$D$$ making a mistake       
