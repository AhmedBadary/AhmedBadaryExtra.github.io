---
layout: NotesPage
title: Auto-Encoders
permalink: /work_files/research/dl/archits/aencdrs
prevLink: /work_files/research/dl.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Introduction and Architecture](#content1)
  {: .TOC1}
  * [DL Book - AEs](#content2)
  {: .TOC2}
  * [Regularized Autoencoders](#content3)
  {: .TOC3}
  * [Learning Manifolds with Autoencoders](#content4)
  {: .TOC4}
</div>

***
***

## Introduction and Architecture
{: #content1}

0. **From PCA to Auto-Encoders:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents10}   
    \- <span>__High dimensional data__ can often be _represented_ using a much __lower dimensional code__</span>{: style="color: purple"}.  
    \- This happens when the <span>data lies near a __linear manifold__</span>{: style="color: purple"} in the high dimensional space.  
    \- Thus, if we can <span>find this _linear manifold_</span>{: style="color: purple"}, we can <span>*__project__* the data on the manifold</span>{: style="color: purple"} and, then, <span>*__represent__* the data by its __position on the manifold__ without losing much information</span>{: style="color: purple"} because _in the directions orthogonal to the manifold there isn't much variation in the data_.  

    __Finding/Learning the Manifold:__  
    Often, __PCA__ is used as a method to determine this _linear manifold_ to reduce the dimensionality of the data from $$N$$-dimensions to, say, $$M$$-dimensions, where $$M < N$$.  
    \- However, what if the manifold that the data is close to, is __non-linear__?  
    Obviously, we need someway to find this non-linear manifold.  

    Deep-Learning provides us with Deep __AutoEncoders__.  
    __Auto-Encoders__ allows us to deal with _curved manifolds_ in the input space by using deep layers, where the <span>__code__ is a _non-linear function_ of the __input__</span>{: style="color: purple"}, and the <span>**_reconstruction_ of the data** from the code is, also, a _non-linear function_ of the __code__</span>{: style="color: purple"}.  

    __Using Backpropagation to implement PCA (inefficiently):__{: style="color: red"}  
    <button>Procedure</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
    * Try to make the output be the same as the input in a network with a central bottleneck.  
        ![img](https://cdn.mathpix.com/snip/images/1mzm8wkDbwLtru-N98SJYffFfFJdjiTv1sl2fczwIGM.original.fullsize.png){: width="30%"}  
    * The activities of the hidden units in the bottleneck form an efficient code.  
    * If the hidden and output layers are linear, it will learn hidden units that are a linear function of the data and minimize the squared reconstruction error.  
        * This is exactly what PCA does.  
    * The $$M$$ hidden units will span the same space as the first $$M$$ components found by PCA  
        * Their weight vectors may not be orthogonal.  
        * They might be skews or rotations of the PCs.  
        * They will tend to have equal variances.  
    {: hidden=""}

    \- The reason to use backprop to implement PCA is that it allows us to <span>generalize PCA</span>{: style="color: goldenrod"}.  
    \- With non-linear layers before and after the code, it should be possible to efficiently represent data that lies on or near a non-linear manifold.  
    <br>

1. **Auto-Encoders:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    An __AutoEncoder__ is an artificial neural network used for unsupervised learning of efficient codings.   
    It aims to learn a representation (encoding) for a set of data, typically for the purpose of _dimensionality reduction_.  
    ![img](/main_files/cs231n/aencdrs/1.png){: width="50%"}  

22. **Deep Auto-Encoders:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents122}  
    They provide a really nice way to do <span>**_non-linear_ dimensionality reduction**</span>{: style="color: goldenrod"}:  
    * They provide __flexible mappings__ **_both_** ways  
    * The <span>learning time is linear</span>{: style="color: goldenrod"} (or better) in the number of training examples  
    * The final encoding model/__Encoder__ is fairly *__compact__* and *__fast__*  
    <br>

33. **Advantages of Depth:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents133}  
    Autoencoders are often trained with only a single layer encoder and a single layer decoder, but using deep encoders and decoders offers many advantages:  
    * Depth can __exponentially reduce the computational cost__ of representing some functions
    * Depth can __exponentially decrease the amount of training data__ needed to learn some functions
    * Experimentally, deep Autoencoders yield __better compression__ compared to shallow or linear Autoencoders  
    <br>

44. **Learning Deep Autoencoders:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents144}  
    Training Deep Autoencoders is very challenging:  
    {: #lst-p}
    * It is difficult to optimize deep Autoencoders using backpropagation  
    * With small initial weights the backpropagated gradient dies  
    
    There are two main methods for training:  
    {: #lst-p}
    * Just initialize the weights carefully as in Echo-State Nets. (No longer used)  
    * Use unsupervised layer-by-layer pre-training. (_Hinton_)  
        This method involves treating each neighbouring set of two layers as a restricted Boltzmann machine so that the pretraining approximates a good solution, then using a backpropagation technique to fine-tune the results. This model takes the name of __deep belief network__.  
    * Joint Training (most common)  
        This method involves training the whole architecture together with a single global reconstruction objective to optimize.  

    A study published in 2015 empirically showed that the joint training method not only learns better data models, but also learned more representative features for classification as compared to the layerwise method.  
    The success of joint training, however, is mostly attributed (depends heavily) on the __regularization strategies__ adopted in the modern variants of the model.  

    [Is Joint Training Better for Deep Auto-Encoders? (paper)](https://arxiv.org/pdf/1405.1380.pdf)
    <br>

2. **Architecture:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    An auto-encoder consists of:  
    * An Encoding Function 
    * A Decoding Function 
    * A Distance Function   

    We choose the __encoder__ and __decoder__ to be <span>parametric functions</span>{: style="color: purple"} (typically <span>neural networks</span>{: style="color: purple"}), and to be <span>differentiable</span>{: style="color: purple"} with respect to the distance function, so the parameters of the encoding/decoding functions can be optimized to minimize the reconstruction loss, using Stochastic Gradient Descent.  
    
    The simplest form of an Autoencoder is a __feedforward neural network__ (similar to the multilayer perceptron (MLP)) – having an input layer, an output layer and one or more hidden layers connecting them – but with the output layer having the same number of nodes as the input layer, and with the purpose of reconstructing its own inputs (instead of predicting the target value $${\displaystyle Y}$$ given inputs $${\displaystyle X}$$).  

3. **Structure and Mathematics:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    The _encoder_ and the _decoder_ in an auto-encoder can be defined as [transitions](https://en.wikipedia.org/wiki/Atlas_(topology)#Transition_maps) $$\phi$$ and $$ {\displaystyle \psi ,}$$ such that:  
    <p>$$ {\displaystyle \phi :{\mathcal {X}}\rightarrow {\mathcal {F}}} \\ 
        {\displaystyle \psi :{\mathcal {F}}\rightarrow {\mathcal {X}}} \\ 
        {\displaystyle \phi ,\psi =\arg \min_{\phi ,\psi }\|X-(\psi \circ \phi )X\|^{2}}$$
    </p>
    where $${\mathcal {X} = \mathbf{R}^d}$$ is the input space, and $${\mathcal {F} = \mathbf{R}^p}$$ is the latent (feature) space, and $$ p < d$$.   
    
    The encoder takes the input $${\displaystyle \mathbf {x} \in \mathbb {R} ^{d}={\mathcal {X}}}$$ and maps it to $${\displaystyle \mathbf {z} \in \mathbb {R} ^{p}={\mathcal {F}}} $$:  
    <p>$${\displaystyle \mathbf {z} =\sigma (\mathbf {Wx} +\mathbf {b} )}$$</p>  
    * The image $$\mathbf{z}$$ is referred to as _code_, _latent variables_, or _latent representation_.  
    *  $${\displaystyle \sigma }$$ is an element-wise activation function such as a sigmoid function or a rectified linear unit.
    * $${\displaystyle \mathbf {W} }$$ is a weight matrix
    * $${\displaystyle \mathbf {b} }$$ is the bias.  

    The Decoder maps  $${\displaystyle \mathbf {z} }$$ to the reconstruction $${\displaystyle \mathbf {x'} } $$  of the same shape as $${\displaystyle \mathbf {x} }$$:  
    <p>$${\displaystyle \mathbf {x'} =\sigma '(\mathbf {W'z} +\mathbf {b'} )}$$</p>  
    where $${\displaystyle \mathbf {\sigma '} ,\mathbf {W'} ,{\text{ and }}\mathbf {b'} } $$ for the decoder may differ in general from those of the encoder.  
    
    Autoencoders minimize reconstruction errors, such as the L-2 loss:  
    <p>$${\displaystyle {\mathcal {L}}(\mathbf {x} ,\psi ( \phi (\mathbf {x} ) ) ) =  {\mathcal {L}}(\mathbf {x} ,\mathbf {x'} )=\|\mathbf {x} -\mathbf {x'} \|^{2}=\|\mathbf {x} -\sigma '(\mathbf {W'} (\sigma (\mathbf {Wx} +\mathbf {b} ))+\mathbf {b'} )\|^{2}}$$</p>  
    where $${\displaystyle \mathbf {x} }$$ is usually averaged over some input training set.  
    <br>

4. **Applications:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    The applications of auto-encoders have changed overtime.  
    This is due to the advances in the fields that auto-encoders were applied in, or to the incompetency of the auto-encoders.  
    Recently, auto-encoders are applied to:  
    * __Data-Denoising__ 
    * __Dimensionality Reduction__ (for data visualization)  
    
    > With appropriate dimensionality and sparsity constraints, Autoencoders can learn data projections that are more interesting than PCA or other basic techniques.  

    > For 2D visualization specifically, t-SNE is probably the best algorithm around, but it typically requires relatively low-dimensional data. So a good strategy for visualizing similarity relationships in high-dimensional data is to start by using an Autoencoder to compress your data into a low-dimensional space (e.g. 32 dimensional) (by an auto-encoder), then use t-SNE for mapping the compressed data to a 2D plane.  

    * [Deep Autoencoders for document retrieval (Hinton)](https://www.youtube.com/watch?v=ARQ6PZh8vgE&list=PLoRl3Ht4JOcdU872GhiYWf6jwrk_SNhz9&index=71)  
    * [Semantic Hashing (Hinton)](https://www.youtube.com/watch?v=swjncYpcLsk&list=PLoRl3Ht4JOcdU872GhiYWf6jwrk_SNhz9&index=72)  
    * [Learning binary codes for image retrieval (Hinton)](https://www.youtube.com/watch?v=MSYmyJgYOnU&list=PLoRl3Ht4JOcdU872GhiYWf6jwrk_SNhz9&index=73)  
    * [Shallow Autoencoders for pre-training (Hinton)](https://www.youtube.com/watch?v=e_n2hht9Yc8&list=PLoRl3Ht4JOcdU872GhiYWf6jwrk_SNhz9&index=74)  
    <br>

5. **Types of Auto-Encoders:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  
    * Vanilla Auto-Encoder
    * Sparse Auto-Encoder
    * Denoising Auto-Encoder
    * Variational Auto-Encoder (VAE)
    * Contractive Auto-Encoder  
    <br>

6. **Auto-Encoders for initializing Neural-Nets:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}  
    After training an auto-encoder, we can use the _encoder_ to compress the input data into it's latent representation (which we can view as _features_) and input those to the neural-net (e.g. a classifier) for prediction.  
    ![img](/main_files/cs231n/aencdrs/2.png){: width="70%"} 
    <br>

7. **Representational Power, Layer Size and Depth:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}  
    The universal approximator theorem guarantees that a feedforward neural network with at least one hidden layer can represent an approximation of any function (within a broad class) to an arbitrary degree of accuracy, provided that it has enough hidden units. This means that an Autoencoder with a single hidden layer is able to represent the identity function along the domain of the data arbitrarily well.  
    However, __the mapping from input to code is shallow__. This means that we are not able to enforce arbitrary constraints, such as that the code should be sparse.  
    A deep Autoencoder, with at least one additional hidden layer inside the encoder itself, can approximate any mapping from input to code arbitrarily well, given enough hidden units.  
    <br>

__Notes:__{: style="color: red"}  
{: #lst-p}
* Progression of AEs (in CV?):  
    * _Originally:_ Linear + nonlinearity (sigmoid)  
    * _Later:_ Deep, fully-connected  
    * _Later:_ ReLU CNN (UpConv)  



***

## DL Book - AEs
{: #content2}

1. **Undercomplete Autoencoders:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    An __Undercomplete Autoencoder__ is one whose code dimension is less than the input dimension.  
    Learning an undercomplete representation forces the Autoencoder to capture the most salient features of the training data.  
    <br>

2. **Challenges:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}  
    * If an Autoencoder succeeds in simply learning to set $$\psi(\phi (x)) = x$$ everywhere, then it is not especially useful.  
        Instead, Autoencoders are designed to be <span>unable to learn to copy perfectly</span>{: style="color: purple"}. Usually they are restricted in ways that allow them to copy only __approximately__, and to copy only __input that resembles the training data__.  
    * In [__Undercomplete Autoencoders__](#bodyContents21) If the <span>Encoder and Decoder are allowed __too much capacity__</span>{: style="color: purple"}, the Autoencoder can learn to <span>perform the copying task __without extracting useful information about the distribution of the data__</span>{: style="color: purple"}.  
        Theoretically, one could imagine that an Autoencoder with a one-dimensional code but a very powerful nonlinear encoder could learn to represent each training example $$x^{(i)}$$ with the code $$i$$. This specific scenario does not occur in practice, but it illustrates clearly that an Autoencoder trained to perform the copying task can fail to learn anything useful about the dataset if the capacity of the Autoencoder is allowed to become too great.  
    * A similar problem occurs in __complete AEs__  
    * As well as in the __overcomplete__ case, in which the hidden code has dimension greater than the input.  
        In complete and overcomplete cases, even a linear encoder and linear decoder can learn to copy the input to the output without learning anything useful about the data distribution.  
    <br>

3. **Regularized AutoEncoders:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}  
    To address the challenges in learning useful representations; we introduce __Regularized Autoencoders__.  

    __Regularized Autoencoders__ allow us to train any architecture of Autoencoder successfully, choosing the code dimension and the capacity of the encoder and decoder based on the complexity of distribution to be modeled.  

    Rather than limiting the model capacity by keeping the encoder and decoder shallow and the code size small, regularized Autoencoders use a loss function that encourages the model to have other properties besides the ability to copy its input to its output:   
    * Sparsity of the representation 
    * Smallness of the derivative of the representation
    * Robustness to noise or to missing inputs.  

    A regularized Autoencoder can be __nonlinear__ and __overcomplete__ but still learn something useful about the data distribution even if the model capacity is great enough to learn a trivial identity function.  
    <br>

4. **Generative Models as (unregularized) Autoencoders:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}  
    In addition to the traditional AEs described here, nearly any __generative model__ with __latent variables__ and equipped with an __inference procedure__ (for computing latent representations given input) may be viewed as a particular form of Autoencoder; most notably the descendants of the __Helmholtz machine__ _(Hinton et al., 1995b)_, such as:  
    {: #lst-p}
    * Variational Autoencoders  
    * Generative Stochastic Networks  

    These models naturally learn _high-capacity_, _overcomplete encodings_ of the input and do NOT require regularization for these encodings to be useful. Their <span>encodings are naturally useful</span>{: style="color: goldenrod"} because the models were <span>trained to _approximately maximize the probability of the training data_ rather than to _copy the input to the output_</span>{: style="color: goldenrod"}.  
    <br>

5. **Stochastic Encoders and Decoders:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}  
    <button>Discussion</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](/main_files/cs231n/aencdrs/3.png){: width="100%" hidden=""}  
    <br>


***

## Regularized Autoencoders
{: #content3}

1. **Sparse Autoencoders:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}  
    __Sparse Autoencoders__ are simply Autoencoders whose training criterion involves a sparsity penalty $$\Omega(\boldsymbol{h})$$ on the code layer $$\boldsymbol{h},$$ in addition to the reconstruction error:  
    <p>$${\displaystyle {\mathcal {L}}(\mathbf {x} ,\psi ( \phi (\mathbf {x} ) ) ) + \Omega(\boldsymbol{h})}$$</p>  
    where typically we have $$\boldsymbol{h}=\phi(\boldsymbol{x})$$, the encoder output.   


    __Regularization Interpretation:__{: style="color: red"}  
    We can think of the penalty $$\Omega(\boldsymbol{h})$$ simply as a regularizer term added to a feedforward network whose primary task is to copy the input to the output (unsupervised learning objective) and possibly also perform some supervised task (with a supervised learning objective) that depends on these sparse features.  


    __Bayesian Interpretation of Regularization:__{: style="color: red"}  
    Unlike other regularizers such as weight decay, there is not a straightforward Bayesian interpretation to this regularizer.  
    Regularized Autoencoders defy such an interpretation because __the regularizer depends on the data__ and is therefore by definition not a prior in the formal sense of the word.  
    We can still think of these regularization terms as _implicitly expressing a preference over functions_.   


    __Latent Variable Interpretation:__{: style="color: red"}  
    Rather than thinking of the sparsity penalty as a regularizer for the copying task, we can think of the entire sparse Autoencoder framework as <span>approximating maximum likelihood training of a generative model that has latent variables</span>{: style="color: goldenrod"}.  

    __Correspondence between Sparsity and a Directed Probabilistic Model:__  
    Suppose we have a model with visible variables $$\boldsymbol{x}$$ and latent variables $$\boldsymbol{h},$$ with an explicit joint distribution $$p_{\text {model }}(\boldsymbol{x}, \boldsymbol{h})=p_{\text {model }}(\boldsymbol{h}) p_{\text {model }}(\boldsymbol{x} \vert \boldsymbol{h}) .$$ We refer to $$p_{\text {model }}(\boldsymbol{h})$$ as the model's prior distribution over the latent variables, representing the model's beliefs prior to seeing $$\boldsymbol{x}$$[^1].  
    The log-likelihood can be decomposed as:  
    <p>$$\log p_{\text {model }}(\boldsymbol{x})=\log \sum_{\boldsymbol{h}} p_{\text {model }}(\boldsymbol{h}, \boldsymbol{x})$$</p>  
    We can think of the Autoencoder as approximating this sum with a point estimate for just one highly likely value for $$\boldsymbol{h}$$.  
    This is similar to the __sparse coding generative model__ (section 13.4), but with $$\boldsymbol{h}$$ being the _output of the parametric encoder_ rather than the result of an optimization that infers the most likely $$\boldsymbol{h}$$. From this point of view, with this chosen $$\boldsymbol{h}$$, we are maximizing:  
    <p>$$\log p_{\text {model }}(\boldsymbol{h}, \boldsymbol{x})=\log p_{\text {model }}(\boldsymbol{h})+\log p_{\text {model }}(\boldsymbol{x} \vert \boldsymbol{h})$$</p>  
    The $$\log p_{\text {model }}(\boldsymbol{h})$$ term can be sparsity-inducing. For example, the __Laplace prior__,  
    <p>$$p_{\text {model }}\left(h_{i}\right)=\frac{\lambda}{2} e^{-\lambda\left|h_{i}\right|}$$</p>  
    __corresponds to an absolute value sparsity penalty__.  
    Expressing the log-prior as an absolute value penalty, we obtain  
    <p>$$\begin{aligned} \Omega(\boldsymbol{h}) &=\lambda \sum_{i}\left|h_{i}\right| \\-\log p_{\text {model }}(\boldsymbol{h}) &=\sum_{i}\left(\lambda\left|h_{i}\right|-\log \frac{\lambda}{2}\right)=\Omega(\boldsymbol{h})+\text { const } \end{aligned}$$</p>  
    where the constant term depends only on $$\lambda$$ and not $$\boldsymbol{h} .$$ We typically treat $$\lambda$$ as a hyperparameter and discard the constant term since it does not affect the parameter learning.  
    Other priors such as the __Student-t prior__ can also induce sparsity.  
    From this point of view of __sparsity__ as <span>resulting from the effect of $$p_{\text {model}}(\boldsymbol{h})$$ on approximate maximum likelihood learning</span>{: style="color: goldenrod"}, the sparsity penalty is __not a regularization term at all__. It is just a <span>consequence of the model’s distribution over its latent variables</span>{: style="color: goldenrod"}. This view provides a __different motivation for training an Autoencoder__: <span>it is a way of approximately training a generative model</span>{: style="color: goldenrod"}. It also provides a different __reason for why the features learned by the Autoencoder are useful__: <span>they describe the latent variables that explain the input</span>{: style="color: goldenrod"}.  

    __Correspondence between Sparsity and an Undirected Probabilistic Model:__  
    Early work on sparse Autoencoders _(Ranzato et al., 2007a, 2008)_ explored various forms of sparsity and proposed a connection between the sparsity penalty and the log $$Z$$ term that arises when applying maximum likelihood to an undirected probabilistic model $$p(\boldsymbol{x})=\frac{1}{Z} \tilde{p}(\boldsymbol{x})$$.  
    The idea is that __minimizing $$\log Z$$ prevents a probabilistic model from having high probability everywhere__, and __imposing sparsity on an Autoencoder prevents the Autoencoder from having low reconstruction error everywhere__. In this case, the connection is on the _level of an intuitive understanding of a general mechanism_ rather than a _mathematical correspondence_.  

    The interpretation of the sparsity penalty as corresponding to $$\log p_{\text {model }}(\boldsymbol{h})$$ in a directed model $$p_{\text {model}}(\boldsymbol{h}) p_{\text {model}} \left(\boldsymbol{x} \vert \boldsymbol{h}\right)$$ is more mathematically straightforward.   

    __Achieving actual zeros in $$\boldsymbol{h}$$:__  
    One way to achieve actual zeros in $$\boldsymbol{h}$$ for sparse (and denoising) Autoencoders was introduced in Glorot et al. (2011b). The idea is to use rectified linear units to produce the code layer. With a prior that actually pushes the representations to zero (like the absolute value penalty), one can thus indirectly control the average number of zeros in the representation.  


    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * [Sparse Autoencoder and Unsupervised Feature Learning #1 (Ng)](https://www.youtube.com/watch?v=vfnxKO2rMq4)  
    * [Sparse Autoencoder and Unsupervised Feature Learning #2 (Ng)](https://www.youtube.com/watch?v=wqhZaWR-J94)  
    <br>


2. **Denoising Autoencoders:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}  
    __Denoising Autoencoders (DAEs)__ is an Autoencoder that receives a corrupted data point as input and is trained to predict the original, uncorrupted data point as its output.  
    It minimizes:  
    <p>$$L(\boldsymbol{x}, g(f(\tilde{\boldsymbol{x}})))$$</p>  
    where $$\tilde{\boldsymbol{x}}$$ is a copy of $$\boldsymbol{x}$$ that has been corrupted by some form of noise.  

    Denoising Autoencoders must therefore learn to __undo this corruption__ rather than simply copying their input.  
    Denoising training forces $$\psi$$ and $$\phi$$ to implicitly learn the structure of $$p_{\text {data}}(\boldsymbol{x}),$$ as shown by _Alain and Bengio (2013)_ and _Bengio et al. (2013c)_.  
    \- Provide yet another example of how <span>useful properties can emerge as a byproduct of __minimizing reconstruction error__</span>{: style="color: purple"}.  
    \- Also an example of, how <span>__overcomplete__, __high-capacity__ models may be used as Autoencoders so long as care is taken to prevent them from learning the identity function</span>{: style="color: purple"}.  

    We introduce a __corruption process__ $$C(\tilde{\mathbf{x}} \vert \mathbf{x})$$ which represents a __conditional distribution over corrupted samples $$\tilde{\boldsymbol{x}}$$__, given a data sample $$\boldsymbol{x}$$.  
    The Autoencoder then learns a __reconstruction distribution__ $$p_{\text {reconstruct}}(\mathrm{x} \vert \tilde{\mathrm{x}})$$ estimated from training pairs $$(\boldsymbol{x}, \tilde{\boldsymbol{x}}),$$ as follows:  
    {: #lst-p}
    * Sample a training example $$\boldsymbol{x}$$ from the training data.
    * Sample a corrupted version $$\tilde{\boldsymbol{x}}$$ from $$C(\tilde{\mathbf{x}} \vert \mathbf{x}=\boldsymbol{x})$$
    * Use $$(\boldsymbol{x}, \tilde{\boldsymbol{x}})$$ as a training example for estimating the Autoencoder reconstruction distribution $$p_{\text {reconstruct}}(\boldsymbol{x} \vert \tilde{\boldsymbol{x}})=p_{\text {decoder}}(\boldsymbol{x} \vert \boldsymbol{h})$$ with $$\boldsymbol{h}$$ the output of encoder $$f(\tilde{\boldsymbol{x}})$$ and $$p_{\text {decoder}}$$ typically defined by a decoder $$g(\boldsymbol{h})$$.  

    __Learning:__  
    Typically we can simply perform gradient-based approximate minimization (such as minibatch gradient descent) on the negative log-likelihood $$-\log p_{\text {decoder}}(\boldsymbol{x} \vert \boldsymbol{h})$$.  
    So long as the encoder is deterministic, the denoising Autoencoder is a feedforward network and may be trained with exactly the same techniques as any other FFN.  
    We can therefore view the DAE as __performing stochastic gradient descent on the following expectation__:  
    <p>$$-\mathbb{E}_{\mathbf{x} \sim \hat{p}_{\text {data }}(\mathbf{x})} \mathbb{E}_{\tilde{\mathbf{x}} \sim C(\tilde{\mathbf{x}} \vert \boldsymbol{x})} \log p_{\text {decoder}}(\boldsymbol{x} \vert \boldsymbol{h}=f(\tilde{\boldsymbol{x}}))$$</p>  
    where $$\hat{p}_ {\text {data}}(\mathrm{x})$$ is the training distribution.  


    __Score Matching - Estimating the Score:__{: style="color: red"}{: #bodyContents32sm}  
    __Score Matching__ _(Hyvärinen, 2005)_ is an alternative to maximum likelihood. It provides a __consistent estimator of probability distributions__ based on _encouraging the model to have the same score as the data distribution at every training point $$\boldsymbol{x}$$_. In this context, the score is a particular __gradient field__    
    <p>$$\nabla_{\boldsymbol{x}} \log p(\boldsymbol{x})$$</p>   
    For Autoencoders, it is sufficient to understand that <span>learning the gradient field of $$\log p_{\text {data}}$$ is one way to learn the structure of $$p_{\text {data itself}}$$</span>{: style="color: goldenrod"}.  

    A very important property of DAEs is that <span>their training criterion (with $$\text { conditionally Gaussian } p(\boldsymbol{x} \vert \boldsymbol{h}))$$ makes the Autoencoder learn a __vector field__ $$(f(\boldsymbol{x}))-\boldsymbol{x}$$) that estimates the __score of the data distribution__</span>{: style="color: goldenrod"}.  
    <button>Vector Field Learning and the Score of $$p_{\text{data}}$$</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/QSRS3G3sT_oO--ZqNJMU8Oub6_etW0n4gHg-0EPSRd8.original.fullsize.png){: width="100%" hidden=""}   
    __Continuous Valued $$\boldsymbol{x}$$:__  
    For continuous-valued $$\boldsymbol{x}$$, the denoising criterion with __Gaussian corruption__ and __reconstruction distribution__ yields an __estimator of the score that is applicable to general encoder and decoder parametrizations__ _(Alain and Bengio, 2013)_.  
    This means a _generic encoder-decoder architecture_ may be made to _estimate the score_ by training with the __squared error criterion__,   
    <p>$$\|g(f(\tilde{x}))-x\|^{2}$$</p>  
    and __corruption__,  
    <p>$$C(\tilde{\mathbf{x}}=\tilde{\boldsymbol{x}} \vert \boldsymbol{x})=\mathcal{N}\left(\tilde{\boldsymbol{x}} ; \mu=\boldsymbol{x}, \Sigma=\sigma^{2} I\right)$$</p>  
    with noise variance $$\sigma^{2}$$.  
    <button>Illustration for continuous $$\boldsymbol{x}$$</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/nboAnloEXDY7mMvx9vXkkm5Zt-jf46fRNPieG_mAh78.original.fullsize.png){: width="100%" hidden=""}   
    __Guarantees:__  
    In general, there is no guarantee that the reconstruction $$g(f(\boldsymbol{x}))$$ minus the input $$\boldsymbol{x}$$ corresponds to the gradient of any function, let alone to the score. That is why the early results (Vincent, 2011) are specialized to particular parametrizations where $$g(f(\boldsymbol{x}))-\boldsymbol{x}$$ may be obtained by taking the derivative of another function. Kamyshanska and Memisevic $$(2015)$$ generalized the results of Vincent $$(2011)$$ by identifying a family of shallow Autoencoders such that $$g(f(\boldsymbol{x}))-\boldsymbol{x}$$ corresponds to a score for all members of the family.  


    __DAEs as representing Probability Distributions and Variational AEs:__{: style="color: red"}  
    So far we have described only how the DAE learns to represent a probability distribution. More generally, one may want to use the Autoencoder as a generative model and draw samples from this distribution. This is knows as the __Variational Autoencoder__.  


    __Denoising AutoEncoders and RBMs:__{: style="color: red"}  
    Denoising training of a specific kind of Autoencoder (sigmoidal hidden units, linear reconstruction units) using Gaussian noise and mean squared error as the reconstruction cost is equivalent (Vincent, 2011) to training a specific kind of undirected probabilistic model called an RBM with Gaussian visible units. This kind of model will be described in detail in section 20.5.1; for the present discussion it suffices to know that it is a model that provides an explicit $$p_{\text {model }}(\boldsymbol{x} ; \boldsymbol{\theta})$$. When the RBM is trained using __denoising score matching__ _(Kingma and LeCun, 2010)_, its learning algorithm is equivalent to denoising training in the corresponding Autoencoder. With a fixed noise level, regularized score matching is not a consistent estimator; it instead recovers a blurred version of the distribution. However, if the noise level is chosen to approach $$0$$ when the number of examples approaches infinity, then consistency is recovered. Denoising score matching is discussed in more detail in section 18.5.  
    Other connections between Autoencoders and RBMs exist. Score matching applied to RBMs yields a cost function that is identical to reconstruction error combined with a regularization term similar to the contractive penalty of the CAE (Swersky et al., 2011). Bengio and Delalleau (2009) showed that an Autoencoder gradient provides an approximation to contrastive divergence training of RBMs.  


    __Historical Perspective:__{: style="color: red"}  
    <button>Discussion</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/w3Nopzr4Q_GY4rYMFqN1s8eq-aiGy47eYyOCOcLHQqo.original.fullsize.png){: width="100%" hidden=""}  
    <br>


3. **Regularizing by Penalizing Derivatives:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}  
    Another strategy for regularizing an Autoencoder is to use a penalty $$\Omega$$ as in sparse Autoencoders,  
    <p>$$L(\boldsymbol{x}, g(f(\boldsymbol{x})))+\Omega(\boldsymbol{h}, \boldsymbol{x})$$</p>  
    but with a different form of $$\Omega$$:  
    <p>$$\Omega(\boldsymbol{h}, \boldsymbol{x})=\lambda \sum_{i}\left\|\nabla_{\boldsymbol{x}} h_{i}\right\|^{2}$$</p>  

    This forces the model to learn a function that does not change much when $$\boldsymbol{x}$$ changes slightly. Because this penalty is applied only at training examples, it forces the Autoencoder to learn features that capture information about the training distribution.  
    An Autoencoder regularized in this way is called a [__contractive Autoencoder (CAE)__](#bodyContents34). This approach has theoretical connections to denoising Autoencoders, manifold learning and probabilistic modeling.  
    <br>


4. **Contractive Autoencoders:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents34}  
    __Contractive Autoencoders (CAEs)__ _(Rifai et al., 2011a,b)_ introduces an explicit regularizer on the code $$\boldsymbol{h}=\phi(\boldsymbol{x}),$$ encouraging the derivatives of $$\phi$$ to be as small as possible:  
    <p>$$\Omega(\boldsymbol{h})=\lambda\left\|\frac{\partial \phi(\boldsymbol{x})}{\partial \boldsymbol{x}}\right\|_ {F}^{2}$$</p>  
    The __penalty__ $$\Omega(\boldsymbol{h})$$ is the *__squared Frobenius norm__*  (sum of squared elements) of __the Jacobian matrix__ of partial derivatives associated with the encoder function.  

    __Connection to Denoising Autoencoders:__{: style="color: red"}  
    There is a connection between the denoising Autoencoder and the contractive Autoencoder: Alain and Bengio _(2013)_ showed that in the limit of small Gaussian input noise, the denoising reconstruction error is equivalent to a contractive penalty on the reconstruction function that maps $$\boldsymbol{x}$$ to $$\boldsymbol{r}=\psi(\phi(\boldsymbol{x}))$$.  
    In other words:  
    \- __Denoising Autoencoders:__ make the reconstruction function resist small but finite-sized perturbations of the input  
    \- __Contractive Autoencoders:__ make the feature extraction function resist infinitesimal perturbations of the input.  
    When using the Jacobian-based contractive penalty to pretrain features $$\phi(\boldsymbol{x})$$ for use with a classifier, the best classification accuracy usually results from applying the contractive penalty to $$\phi(\boldsymbol{x})$$ rather than to $$\psi(\phi(\boldsymbol{x}))$$.  
    A contractive penalty on $$\phi(\boldsymbol{x})$$ also has close [connections to __score matching__](#bodyContents32sm).  

    __Contractive - Definition and Analysis:__{: style="color: red"}  
    The name __contractive__ arises from the way that the CAE _warps space_. Specifically, because the CAE is trained to resist perturbations of its input, it is encouraged to map a neighborhood of input points to a smaller neighborhood of output points. We can think of this as contracting the input neighborhood to a smaller output neighborhood.  

    To clarify, the CAE is contractive only *__locally__*-all perturbations of a training point $$\boldsymbol{x}$$ are mapped near to $$\phi(\boldsymbol{x})$$. *__Globally__*, two different points $$\boldsymbol{x}$$ and $$\boldsymbol{x}^{\prime}$$ may be mapped to $$\phi(\boldsymbol{x})$$ and $$\psi\left(\boldsymbol{x}^{\prime}\right)$$ points that are farther apart than the original points.  

    __As a linear operator:__  
    We can think of the _Jacobian matrix_ $$J$$ at a point $$x$$ as <span>_approximating_ the __nonlinear encoder $$\phi(x)$$__ as being a __linear operator__</span>{: style="color: goldenrod"}. This allows us to use the word _"contractive"_ more formally.  
    In the theory of linear operators, a linear operator is said to be _contractive_ if the norm of $$J x$$ remains less than or equal to 1 for all unit-norm $$x$$. In other words, __$$J$$ is contractive if it shrinks the unit sphere__.  
    We can think of the CAE as _penalizing the Frobenius norm of the local linear approximation of $$\phi(x)$$ at every training point $$x$$_ in order _to encourage each of these local linear operator to become a **contraction**_.  


    __Manifold Learning:__{: style="color: red"}  
    Regularized Autoencoders learn manifolds by balancing two opposing forces.  
    In the case of the CAE, these two forces are reconstruction error and the contractive penalty $$\Omega(\boldsymbol{h}) .$$ Reconstruction error alone would encourage the CAE to learn an identity function. The contractive penalty alone would encourage the CAE to learn features that are constant with respect to $$\boldsymbol{x}$$.  
    The compromise between these two forces yields an Autoencoder whose derivatives $$\frac{\partial f(\boldsymbol{x})}{\partial \boldsymbol{x}}$$ are mostly tiny. Only a small number of hidden units, corresponding to a small number of directions in the input, may have significant derivatives.  

    The __goal__ of the CAE is to _learn the manifold structure of the data_.  
    Directions $$x$$ with large $$J x$$ rapidly change $$h,$$ so these are likely to be directions which approximate the tangent planes of the manifold.  
    Experiments by _Rifai et al. (2011 a,b)_ show that training the CAE results in:  
    {: #lst-p}
    1. Most singular values of $$J$$ dropping below $$1$$ in magnitude and therefore becoming _contractive_  
    2. However, some singular values remain above $$1,$$ because the reconstruction error penalty encourages the CAE to encode the directions with the most local variance.  

    * The directions corresponding to the largest singular values are interpreted as the tangent directions that the contractive Autoencoder has learned.  
    * Visualizations of the experimentally obtained singular vectors do seem to correspond to meaningful transformations of the input image.  
        Since, Ideally, these tangent directions should correspond to real variations in the data.  
        For example, a CAE applied to images should learn tangent vectors that show how the image changes as objects in the image gradually change pose.  
        <button>Estimated Tangent Vectors of the Manifold</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        ![img](https://cdn.mathpix.com/snip/images/2KaOUhQBjXy2N_cP2DgVDA5PI1ggqOK1StFn2NR8t0c.original.fullsize.png){: width="100%" hidden=""}  


    __Issues with Contractive Penalties:__{: style="color: red"}{: #bodyContents35issues_ctrctv_pnlt}  
    Although it is cheap to compute the CAE regularization criterion, in the case of a single hidden layer Autoencoder, it becomes much _more expensive_ in the case of _deeper_ Autoencoders.  
    The strategy followed by _Rifai et al. (2011a)_ is to:  
    \- Separately train a series of single-layer Autoencoders, each trained to reconstruct the previous Autoencoder’s hidden layer.  
    \- The composition of these Autoencoders then forms a deep Autoencoder.  
    * Because each layer was separately trained to be locally contractive, the deep Autoencoder is contractive as well.  
    * The result is not the same as what would be obtained by _jointly training_ the entire architecture with a penalty on the Jacobian of the deep model, but it captures many of the desirable qualitative characteristics.  

    Another issue is that the contractive penalty can obtain _useless results_ if we do not impose some sort of *__scale__* on the _decoder_.  
    \- For example, the encoder could consist of multiplying the input by a small constant $$\epsilon$$ and the decoder could consist of dividing the code by $$\epsilon$$.  
    As $$\epsilon$$ approaches $$0$$, the encoder drives the contractive penalty $$\Omega(\boldsymbol{h})$$ to approach $$0$$ without having learned anything about the distribution.  
    Meanwhile, the decoder maintains perfect reconstruction.  
    \- In _Rifai et al. (2011a)_, this is prevented by __tying the weights__ of $$\phi$$ and $$\psi$$. Both $$\phi$$ and $$\psi$$ are standard neural network layers consisting of an affine transformation followed by an element-wise nonlinearity, so it is straightforward to set the weight matrix of $$\psi$$ to be the transpose of the weight matrix of $$\phi$$.  



5. **Predictive Sparse Decomposition:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents35}  
    <button>Discussion</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](/main_files/cs231n/aencdrs/4.png){: width="100%" hidden=""}  


***

## Learning Manifolds with Autoencoders
{: #content4}  

<button>PDF</button>{: .showText value="show"
     onclick="showText_withParent_PopHide(event);"}
<iframe hidden="" src="/main_files/cs231n/aencdrs/chapter-14-manifold-learning.pdf" frameborder="0" height="840" width="646" title="Layer Normalization" scrolling="auto"></iframe>


<!-- 1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents41} -->


[^1]: This is different from the way we have previously used the word "prior," to refer to the distribution $$p(\boldsymbol{\theta})$$ encoding our beliefs about the model's parameters before we have seen the training data.  