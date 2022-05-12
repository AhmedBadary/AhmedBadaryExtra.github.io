---
layout: NotesPage
title: Representation Learning
permalink: /work_files/research/dl/theory/representation_learning
prevLink: /work_files/research/dl/theory.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Representation Learning](#content1)
  {: .TOC1}
  * [Unsupervised Representation Learning](#content2)
  {: .TOC2}
  * [Supervised Representation Learning](#content3)
  {: .TOC3}
  * [Transfer Learning and Domain Adaptation](#content4)
  {: .TOC4}
  * [Causal Factor Learning](#content5)
  {: .TOC5}
  <!--     * [SIXTH](#content6)
  {: .TOC6} -->
</div>

***
***

* [My Presentation on Representation Learning](https://docs.google.com/presentation/d/1asNbolA4VgTdhp7x84hfj5-GB2M8yApJylc01WhiOo0/edit#slide=id.gc7d6ca60f0_0_0)  


* [From Deep Learning of Disentangled Representations to Higher-level Cognition (Bengio Lec)](https://www.youtube.com/watch?v=Yr1mOzC93xs)  
* [Representation Learning (CMU Lec!)](https://www.youtube.com/watch?v=754vWvIimPo)  
* [Representation Learning and Deep Learning (Bengio Talk)](https://www.youtube.com/watch?v=O6itYc2nnnM)  
* [Deep Learning and Representation Learning (Hinton Talk)](https://www.youtube.com/watch?v=7kAlBa7yhDM)  
* [Goals and Principles of Representation Learning (inFERENCe!)](https://www.inference.vc/goals-and-principles-of-representation-learning/)  
* [DALI Goals and Principles of Representation Learning (vids!)](https://www.youtube.com/playlist?list=PL-tWvTpyd1VAlbzhCpljlREd76Nlo1pOo)  
* [Deep Learning of Representations: Looking Forward (Bengio paper!)](https://arxiv.org/pdf/1305.0445.pdf)  
* [On Learning Invariant Representations for Domain Adaptation (blog!)](https://blog.ml.cmu.edu/2019/09/13/on-learning-invariant-representations-for-domain-adaptation/)  
* [Contrastive Unsupervised Learning of Semantic Representations: A Theoretical Framework (Blog!)](http://www.offconvex.org/2019/03/19/CURL/)  


__Notes (Move Inside):__{: style="color: red"}  
{: #lst-p}
* Representation Learning (Feature Learning) is a set of techniques that allows a system to automatically discover the representations needed for feature detection or classification from raw data.  
    This replaces manual feature engineering and allows a machine to both learn the features and use them to perform a specific task.  
* Hypothesis - Main Idea:  
    The core hypothesis for representation learning is that the unlabeled data can be used to learn a good representation.  
* Types:  
    Representation learning can be either supervised or unsupervised.  
<br>


## Representation Learning
{: #content1}

1. **Representation Learning:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    __Representation Learning__ (__Feature Learning__) is a set of techniques that allows a system to automatically discover the representations needed for feature detection or classification from raw data.  
    This replaces manual feature engineering and allows a machine to both learn the features and use them to perform a specific task.  


    __Hypothesis - Main Idea:__{: style="color: red"}  
    The core __hypothesis__ for representation learning is that <span>the *unlabeled* data can be used to learn a *good* representation</span>{: style="color: goldenrod"}.  
    
    
    __Types:__{: style="color: red"}  
    Representation learning can be either [__supervised__](#bodyContents14) or [__unsupervised__](#bodyContents13).  


    __Representation Learning Approaches:__{: style="color: red"}  
    There are various ways of learning different representations:  
    {: #lst-p}
    * __Probabilistic Models__: the goal is to learn a representation that captures the probability distribution of the underlying explanatory features for the observed input. Such a learnt representation can then be used for prediction.  
    * __Deep Learning__: the representations are formed by composition of multiple non-linear transformations of the input data with the goal of yielding abstract and useful representations for tasks like classification, prediction etc.  


    __Representation Learning Tradeoff:__{: style="color: red"}  
    Most representation learning problems face a tradeoff between <span>preserving as much information about the input</span>{: style="color: purple"} as possible and <span>attaining nice properties</span>{: style="color: purple"} (such as independence).  


    __The Problem of Data (Semi-Supervised Learning\*):__{: style="color: red"}  
    We often have very large amounts of unlabeled training data and relatively little labeled training data. Training with supervised learning techniques on the labeled subset often results in severe overfitting. Semi-supervised learning offers the chance to resolve this overfitting problem by also learning from the unlabeled data. Specifically, we can learn good representations for the unlabeled data, and then use these representations to solve the supervised learning task.  


    __Learning from Limited Data:__{: style="color: red"}  
    Humans and animals are able to learn from very few labeled examples.   
    Many factors could explain improved human performance — for example, the brain may use <span>very large ensembles of classifiers</span>{: style="color: purple"} or <span>Bayesian inference</span>{: style="color: purple"} techniques.  
    One popular hypothesis is that the brain is able to <span>leverage unsupervised or semi-supervised learning</span>{: style="color: purple"}.  

    
    __Motivation/Applications:__{: style="color: red"}  
    {: #lst-p}
    1. ML tasks such as _classification_ often require input that is mathematically and computationally convenient to process.  
        However, real-world data such as images, video, and sensor data has not yielded to attempts to algorithmically define specific features.  
    2. Learning [good representations]() enables us to perform certain (specific) tasks in a more optimal manner.  
        * E.g. linked lists $$\implies$$ $$\mathcal{O}(n)$$ insertion \| red-black tree $$\implies$$ $$\mathcal{O}(\log n)$$ insertion.  
        * <button>Ex: Learning Language Representations</button>{: .showText value="show" onclick="showTextPopHide(event);"}
            * Goal: Learn Portuguese
            * For 1 month you listen to Portuguese on the radio (this is unlabeled data)
            * You develop an intuition for the language, phrases, and grammar (a model in your head)
            * It is easier to learn now from a tutor because you have a better (higher representation) of the data/language    
            {: hidden=""}
    3. Representation Learning is particularly interesting because it <span>provides (one) way to perform __unsupervised__ and __semi-supervised learning__</span>{: style="color: purple"}.  
    4. __Feature Engineering__ is hard. Representation Learning allows us to avoid having to engineer features, manually.  
    5. In general, representation learning can allow us to <span>achieve __multi-task learning__, __transfer learning__, and __domain adaptation__</span>{: style="color: purple"} through <span>shared representations</span>{: style="color: goldenrod"}.  


    __The Quality of Representations:__{: style="color: red"}  
    Generally speaking, a good representation is one that makes a subsequent learning task easier.  
    The choice of representation will usually depend on the choice of the subsequent learning task.  


    __Success of Representation Learning:__{: style="color: red"}  
    The success of representation learning can be attributed to many factors, including:  
    {: #lst-p}
    * Theoretical advantages of __*distributed* representations__ _(Hinton et al., 1986)_  
    * Theoretical advantages of __*deep* representations__ _(Hinton et al., 1986)_   
    * The __Causal Factors Hypothesis__: a general idea of underlying assumptions about the data generating process, in particular about underlying causes of the observed data.  



    __Representation Learning Domain Applications:__{: style="color: red"}  
    {: #lst-p}
    * __Computer Vision__: CNNs.  
    * __Natural Language Processing__: Word-Embeddings.  
    * __Speech Recognition__: Speech-Embeddings.  



    <button>__Representation Quality__</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
    * <span>__“What is a *good* representation?”__</span>{: style="color: purple"}   
        * Generally speaking, a __good representation__ is one that makes a subsequent learning task easier.  
            The choice of representation will usually depend on the choice of the subsequent learning task.  

    * <span>__“What makes one representation better than another?”__</span>{: style="color: purple"}   
        * __Causal Factors Hypothesis:__  
            An __ideal representation__ is one in which <span>the __features__ within the representation _correspond_ to the underlying __causes__ of the observed data</span>{: style="color: purple"}, with __*separate* features__ or __directions__ in _feature space_ corresponding to __*different* causes__, so that <span>the __representation__ *__disentangles__* the __causes__ from one another</span>{: style="color: purple"}.  
            * __Why__:  
                * __Ease of Modeling:__ A representation that __cleanly separates the underlying causal factors__ is, also, one that is __easy to model__.  
                    * For *__many__* __AI tasks__ the two properties __coincide__: once we are able to <span>obtain the underlying explanations for the observations</span>{: style="color: purple"}, it generally becomes <span>easy to isolate individual attributes</span>{: style="color: purple"} from the others.  
                    * Specifically, __if__ a <span>__representation $$\boldsymbol{h}$$__ _represents_ many of the *__underlying causes__* of the __observed $$\boldsymbol{x}$$__</span>{: style="color: purple"}, __and__ the <span>__outputs $$\boldsymbol{y}$$__ are among the __most *salient causes*__</span>{: style="color: purple"}, __then__ it is <span>easy to __predict__ $$\boldsymbol{y}$$ from $$\boldsymbol{h}$$</span>{: style="color: purple"}.  
        * __Summary__ of the *Causal Factors Hypothesis*:  
            An __ideal representation__ is one in which <span>the __features__ within the representation _correspond_ to the underlying __causes__ of the observed data</span>{: style="color: purple"}, with __*separate* features__ or __directions__ in _feature space_ corresponding to __*different* causes__, so that <span>the __representation__ *__disentangles__* the __causes__ from one another</span>{: style="color: purple"}, especially those factors that are relevant to our applications.  

    * <span>__“What is a *"salient factor"*?”__</span>{: style="color: purple"}   
        * A __*"salient factor"*__ is a causal factor (latent variable) that explains, *__well__*, the observed variations in $$X$$.  
            * <button>Illustration: Statistical Saliency</button>{: .showText value="show" onclick="showTextPopHide(event);"}
                ![img](https://cdn.mathpix.com/snip/images/TTMVZWgnTfvYTrRbqLCW5VGoOZSUPC21oMaPDhijp-c.original.fullsize.png){: width="100%" hidden=""}  
            * What makes a feature _"salient"_ for humans?  
                It could be something really simple like __correlation__ or __predictive power__.  
                Ears are a salient feature of Humans because in a majority of cases, presence of one implies presence of another.  
            * Discriminative features as salient features:  
                Note that in object detection case, the predictive power is only measured in:  
                (ear $$\rightarrow$$ person) direction, not (person $$\rightarrow$$ ear) direction.  
                E.g. if your task was to discriminate between males and females, presence of ears would not be a useful feature even though all humans have ears. Compare this to the pimples case: in human vs dog classification, pimples are a really good predictor of 'human', even though they are not a salient feature of Humans.  
                Basically I think discriminative =/= salient  
    {: hidden=""}


    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * Representation Learning can be done with both, __generative__ and __discriminative__ models.  
    * In DL, representation learning uses a composition of __transformations__ of the input data (features) to create learned features.  
    <br>

    <!-- 2. **Shared Representations:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12} -->

7. **Distributed Representation:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}  
    __Distributed Representations__ of concepts are representations composed of many elements that can be set separately from each other.  
    
    __Distributed representations of concepts__ are one of the most important tools for __representation learning__:  
    {: #lst-p}
    * Distributed representations are __powerful__ because <span>they can use $$n$$ __features__ with $$k$$ __values__ to *__describe__* $$k^{n}$$ __different concepts__</span>{: style="color: purple"}.  
    * Both __neural networks with multiple hidden units__ and __probabilistic models with multiple latent variables__ make use of the strategy of distributed representation.  
    * __Motivation for using Distributed Representations:__   
        Many __deep learning algorithms__ are motivated by the assumption that the <span>hidden units can *learn to represent* the underlying __causal factors__ that *explain* the data</span>{: style="color: goldenrod"}.  
        Distributed representations are natural for this approach, because each direction in representation space can correspond to the value of a different underlying configuration variable.  
    * __Distributed vs Symbolic Representations__:  
        * __Number of "Representable" Configurations - by example__:  
            * An example of a __distributed representation__ is a <span>vector of $$n$$ binary features</span>{: style="color: purple"}.  
                It can take $$2^{n}$$ configurations, each potentially corresponding to a different region in input space.  
                <button>Illustration</button>{: .showText value="show" onclick="showTextPopHide(event);"}
                ![img](https://cdn.mathpix.com/snip/images/aSpsvuJ06k0ls64IxpaAcv31EdfpEubzymZhuD6H5ZE.original.fullsize.png){: width="100%" hidden=""}  
            * An example of a __symbolic representation__, is <span>one-hot representation</span>{: style="color: purple"}[^6] where the input is associated with a single symbol or category.  
                If there are $$n$$ symbols in the dictionary, one can imagine $$n$$ feature detectors, each corresponding to the detection of the presence of the associated category.  
                In that case only $$n$$ different configurations of the representation space are possible, carving $$n$$ different regions in input space.  
                <button>Illustration</button>{: .showText value="show" onclick="showTextPopHide(event);"}
                ![img](https://cdn.mathpix.com/snip/images/LENWWJMJ5SNBNMLyIzxdYGLIMVqSEk9fGtkv0XQoi5s.original.fullsize.png){: width="100%" hidden=""}  
                A symbolic representation is a specific example of the broader class of non-distributed representations, which are representations that may contain many entries but without significant meaningful separate control over each entry.  
        * __Generalization__:  
            An important related concept that distinguishes a distributed representation from a symbolic one is that <span>__generalization__ arises due to *__shared attributes between different concepts__*</span>{: style="color: purple"}.  
            * <button>Discussion/Analysis</button>{: .showText value="show" onclick="showTextPopHide(event);"}
                * As pure symbols, “cat” and “dog” are as far from each other as any other two symbols.  
                    However, if one associates them with a meaningful distributed representation, then many of the things that can be said about cats can generalize to dogs and vice-versa.  
                    * For example, our distributed representation may contain entries such as “has_fur” or “number_of_legs” that have the same value for the embedding of both “cat ” and “dog.”  
                        __Neural language models__ that operate on distributed representations of words generalize much better than other models that operate directly on one-hot representations of words _(section 12.4)_.  
                        <span>Distributed representations induce a rich similarity space, in which semantically close concepts (or inputs) are close in distance, a property that is absent from purely symbolic representations.</span>{: style="color: purple"}    
                {: hidden=""}
            <span>Distributed representations induce a rich similarity space, in which semantically close concepts (or inputs) are close in distance, a property that is absent from purely symbolic representations.</span>{: style="color: purple"}  
            [__\[Analysis: Generalization of Distributed Representations\]__](#bodyContents17gen)
    * <button>Examples of __learning algorithms__ based on __non-distributed representations__:</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        * __Clustering methods, including the $$k$$-means algorithm__: each input point is assigned to exactly one cluster.
        * __k-nearest neighbors algorithms__: one or a few templates or prototype examples are associated with a given input. In the case of $$k>1$$, there are multiple values describing each input, but they can not be controlled separately from each other, so this does not qualify as a true distributed representation.  
        * __Decision trees__: only one leaf (and the nodes on the path from root to leaf) is activated when an input is given.
        * __Gaussian mixtures and mixtures of experts__: the templates (cluster centers) or experts are now associated with a degree of activation. As with the k-nearest neighbors algorithm, each input is represented with multiple values, but those values cannot readily be controlled separately from each other.  
        * __Kernel machines with a Gaussian kernel (or other similarly local kernel)__: although the degree of activation of each “support vector” or template example is now continuous-valued, the same issue arises as with Gaussian mixtures.  
        * __Language or translation models based on n-grams__: The set of contexts (sequences of symbols) is partitioned according to a tree structure of suffixes. A leaf may correspond to the last two words being w1 and w2, for example. Separate parameters are estimated for each leaf of the tree (with some sharing being possible).  
        {: hidden=""}
    > For some of these non-distributed algorithms, the output is not constant by parts but instead interpolates between neighboring regions. The relationship between the number of parameters (or examples) and the number of regions they can define remains linear.  
    

    __Generalization of Distributed Representations:__{: style="color: red"}{: #bodyContents17gen}  
    We know that for __distributed representations__, <span>__Generalization__ arises due to __*shared attributes* between different concepts__</span>{: style="color: purple"}.  

    But an important question is:  
    <span>**"When and why can there be a statistical advantage from using a distributed representation as part of a learning algorithm?"**</span>{: style="color: purple"}   
    {: #lst-p}
    * Distributed representations can have a __statistical advantage__ when an <span>__apparently complicated structure__ can be *__compactly__* __represented__ using a __*small number* of parameters__</span>{: style="color: goldenrod"}.  
    * Some traditional nondistributed learning algorithms generalize only due to the __smoothness assumption__, which states that if $$u \approx v,$$ then the target function $$f$$ to be learned has the property that $$f(u) \approx f(v),$$ in general.  
        There are many ways of formalizing such an assumption, but the end result is that if we have an example $$(x, y)$$ for which we know that $$f(x) \approx y,$$ then we choose an estimator $$\hat{f}$$ that approximately satisfies these constraints while changing as little as possible when we move to a nearby input $$x+\epsilon$$.  
        * This assumption is clearly very useful, but it _suffers_ from the __curse of dimensionality__: in order to learn a target function that increases and decreases many times in many different regions,1 we may need a number of examples that is at least as large as the number of distinguishable regions.  
            One can think of each of these regions as a category or symbol: by having a separate degree of freedom for each symbol (or region), we can learn an arbitrary decoder mapping from symbol to value.  
            However, this does not allow us to generalize to new symbols for new regions.  
    * If we are lucky, there may be some __*regularity*__ in the __target function__, besides being _smooth_.  
        For example, a __convolutional network__ with __max-pooling__ can recognize an object regardless of its location in the image, even though spatial translation of the object may not correspond to smooth transformations in the input space.  

    __Justifying Generalization in distributed representations:__{: style="color: red"}  
    {: #lst-p}
    * __Geometric justification (by analyzing binary, linear feature extractors (units)):__  
        Let us examine a special case of a distributed representation learning algorithm, that extracts __binary features__ by thresholding __linear functions__ of the input:   
        <button>Discussion</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        * Each binary feature in this representation *__divides__* $$\mathbb{R}^{d}$$ into a __pair__ of __half-spaces__.  
        * The *__exponentially large__* __number__ of __intersections__ of $$n$$ of the corresponding half-spaces _determines_ the <span>number of regions this distributed representation learner can distinguish</span>{: style="color: purple"}.  
        * The __number of regions generated by an arrangement of $$n$$ hyperplanes in $$\mathbb{R}^{d}$$__:  
            By applying a general result concerning the intersection of hyperplanes _(Zaslavsky, } 1975)_, one can show _(Pascanu et al, 2014b)_ that the number of regions this binary feature representation can distinguish is:  
            <p>$$\sum_{j=0}^{d}\left(\begin{array}{l}{n} \\ {j}\end{array}\right)=O\left(n^{d}\right)$$</p>  
        * Therefore, we see a <span>__growth__ that is *__exponential__* in the __input size__ and *__polynomial__* in the __number of hidden units__</span>{: style="color: purple"}.  
        * This provides a __geometric argument__ to _explain_ the <span>generalization power of distributed representation</span>{: style="color: purple"}:  
            with $$\mathcal{O}(n d)$$ parameters (for $$n$$ linear-threshold features in $$\mathbb{R}^{d}$$) we can distinctly represent $$\mathcal{O}\left(n^{d}\right)$$ regions in input space.  
            * If instead we made no assumption at all about the data, and used a representation with unique symbol for each region, and separate parameters for each symbol to recognize its corresponding portion of $$\mathbb{R}^{d},$$ then,  
                specifying $$\mathcal{O}\left(n^{d}\right)$$ regions would require $$\mathcal{O}\left(n^{d}\right)$$ examples.  
        * More generally, the argument in favor of the distributed representation could be extended to the case where instead of using linear threshold units we use __nonlinear__, possibly __continuous__, __feature extractors__ for each of the attributes in the distributed representation.  
            The argument in this case is that if a parametric transformation with $$k$$ parameters can learn about $$r$$ regions in input space, with $$k \ll r,$$ and if obtaining such a representation was useful to the task of interest, then we could potentially generalize much better in this way than in a non-distributed setting where we would need $$\mathcal{O}(r)$$ examples to obtain the same features and associated partitioning of the input space into $$r$$ regions.  
            Using fewer parameters to represent the model means that we have fewer parameters to fit, and thus require far fewer training examples to generalize well.  
        {: hidden=""}
    * __VC-Theory justification - Fixed Capacity__:  
        <button>Discussion</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        <div hidden="" markdown="1">
        The __capacity__ remains *__limited__* despite being able to distinctly encode so many different regions.  
        For example, the __VC-dimension__ of a __neural network of linear threshold units__ is only $$\mathcal{O}(w \log w),$$ where $$w$$ is the number of weights _(Sontag, 1998_.  

        This limitation arises because, while we can assign very many unique codes to representation space, we __cannot__:  
        {: #lst-p}
        * Use absolutely all of the code space
        * Learn arbitrary functions mapping from the representation space $$h$$ to the output $$y$$ using a linear classifier.  

        The <span>use of a __distributed representation__ _combined_ with a __linear classifier__</span>{: style="color: purple"} thus __*expresses* a prior belief__ that <span>the classes to be recognized are __linearly separable__ as a __function__ of the underlying __causal factors__ captured by $$h$$</span>{: style="color: purple"}.  

        > We will typically want to learn categories such as the set of all images of all green objects or the set of all images of cars, but not categories that require nonlinear, $$\mathrm{XOR}$$ logic. For example, we typically do not want to partition the data into the set of all red cars and green trucks as one class and the set of all green cars and red trucks as another class.  
        </div>
    * __Experimental justification__:  
        <button>Discussion</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        Though the above ideas have been abstract, they may be experimentally validated:  
        * _Zhou et al. (2015)_ find that __hidden units in a deep convolutional network__ trained on the ImageNet and Places benchmark datasets <span>learn features that are very often interpretable, corresponding to a label that humans would naturally assign</span>{: style="color: purple"}.  
            In practice it is certainly not always the case that hidden units learn something that has a simple linguistic name, but it is interesting to see this emerge near the top levels of the best computer vision deep networks. What such features have in common is that one could imagine learning about each of them without having to see all the configurations of all the others.  
        * _Radford et al. (2015)_ demonstrated that a __generative model__ can <span>learn a representation of images of faces, with separate directions in representation space capturing different underlying factors of variation</span>{: style="color: purple"}.  
            The following illustration demonstrates that one direction in representation space corresponds to whether the person is male or female, while another corresponds to whether the person is wearing glasses.  
            <button>Illustration: linear structure of latent variables</button>{: .showText value="show" onclick="showTextPopHide(event);"}
            ![img](https://cdn.mathpix.com/snip/images/zCy3LJD1DqrdXwzCvbZeuG1DyuuPwR6xdHZoClbwN4o.original.fullsize.png){: width="100%" hidden=""}  
            These features were discovered automatically, not fixed a priori.  
            There is no need to have labels for the hidden unit classifiers: gradient descent on an objective function of interest naturally learns semantically interesting features, so long as the task requires such features.  
            We can learn about the distinction between male and female, or about the presence or absence of glasses, without having to characterize all of the configurations of the $$n − 1$$ other features by examples covering all of these combinations of values.  
            <span>This form of __statistical separability__ is what allows one to generalize to new configurations of a person’s features that have never been seen during training.</span>{: style="color: goldenrod"}  
        {: hidden=""}


    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * `page 542` As a counter-example, recent research from DeepMind ([Morcos et al., 2018](https://arxiv.org/abs/1803.06959)) suggests that while some hidden units might appear to learn an interpretable feature, 'these interpretable neurons are no more important than confusing neurons with difficult-to-interpret activity'.  
        Moreover, 'networks which generalise well are much less reliant on single directions [ie. hidden units] than those which memorise'. See more in the DeepMind [blog post](https://deepmind.com/blog/understanding-deep-learning-through-neuron-deletion/).  
    * <span>Distributed representations based on latent variables can obtain all of the advantages of representation learning that we have seen with deep feedforward and recurrent networks.</span>{: style="color: goldenrod"}  
    * __Food for Thought (F2T):__  
        _"since feature engineering was made obsolete by deep learning, algorithm engineering will be made obsolete by meta-learning"_ - Sohl-Dickstein  
    <br>

8. **Deep Representations - Exponential Gain from Depth:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18}  

    __Exponential Gain in MLPs:__{: style="color: red"}  
    We have seen in (section 6.4.1) that multilayer perceptrons are __universal approximators__, and that some functions can be represented by __exponentially smaller *deep* networks__ compared to *__shallow__* __networks__.  
    This __decrease in model size__ leads to _improved_ __statistical efficiency__.  

    Similar results apply, more generally, to other kinds of __models with__ <span>__*distributed* hidden representations__</span>{: style="color: purple"}.  

    __Justification/Motivation:__{: style="color: red"}  
    In this and other AI tasks, <span>the __factors__ that can be *chosen almost __independently__ from each other* yet still *correspond to __meaningful inputs__* are more likely to be __*very high-level*__ and __related__ in __*highly nonlinear ways*__ to the __input__</span>{: style="color: purple"}.  
    _Goodfellow et al._ argue that this <span>demands **deep distributed representations**</span>{: style="color: purple"}, where the __higher level features__ (seen as functions of the input) or __factors__ (seen as generative causes) are *obtained through the __composition__ of many __nonlinearities__*.  
    > E.g. the example of a generative model that learned about the explanatory factors underlying images of faces, including the person’s gender and whether they are wearing glasses.  
        It would not be reasonable to expect a shallow network, such as a linear network, to learn the complicated relationship between these abstract explanatory factors and the pixels in the image.  

    __Universal Approximation property in Models (from Depth):__{: style="color: red"}  
    {: #lst-p}
    * It has been proven in many different settings that <span>__organizing computation through the composition of many nonlinearities__ and a __hierarchy of reused features__ can give an *__exponential boost__* to __statistical efficiency__</span>{: style="color: purple"}, on top of the *__exponential boost__* given by using a __distributed representation__.  
    * Many kinds of networks (e.g., with saturating nonlinearities, Boolean gates, sum/products, or RBF units) with a __single hidden layer__ can be shown to be __universal approximators__.  
        A model family that is a universal approximator can approximate a large class of functions (including all continuous functions) up to any non-zero tolerance level, given enough hidden units.  
        However, the required number of hidden units may be very large.  
    * Theoretical results concerning the __expressive power of deep architectures__ state that <span>there are families of functions that can be represented efficiently by an architecture of depth $$k$$</span>{: style="color: purple"}, but would require an *__exponential number__* of __hidden units__ (wrt. __input size__) with *__insufficient__* __depth__ (depth $$2$$ or depth $$k − 1$$).  
    
    __Exponential Gains in Structured Probabilistic Models:__{: style="color: red"}  
    {: #lst-p}
    * __PGMs as Universal Approximators__:  
        * Just like __deterministic feedforward networks__ are __universal approximators__ of __*functions*__{: style="color: goldenrod"}.  
            Many __structured probabilistic models__ with a __single hidden layer__ of __latent variables__, including restricted Boltzmann machines and deep belief networks, are __universal approximators__ of __*probability distributions*__{: style="color: goldenrod"} _(Le Roux and Bengio, 2008, 2010; Montúfar and Ay, 2011; Montúfar, 2014; Krause et al., 2013)_.  
    * __Exponential Gain from Depth in PGMs__: 
        * Just like a _sufficiently_ *__deep__* __feedforward network__ can have an *__exponential__* __advantage__ over a network that is too *__shallow__*.    
            Such results can also be obtained for other models such as __probabilistic models__.  
            * E.g. The __sum-product network (SPN)__ _(Poon and Domingos, 2011)_.  
                These models use polynomial circuits to compute the probability distribution over a set of random variables.  
                * _Delalleau and Bengio (2011)_ showed that there exist probability distributions for which a minimum depth of SPN is required to avoid needing an exponentially large model.  
                * Later, _Martens and Medabalimi (2014)_ showed that there are significant differences between every two finite depths of SPN, and that some of the constraints used to make SPNs tractable may limit their representational power.  

    __Expressiveness of Convolutional Networks:__{: style="color: red"}  
    Another interesting development is a set of theoretical results for the expressive power of families of deep circuits related to convolutional nets:  
    They highlight an *__exponential advantage__* for the deep circuit even when the <span>shallow circuit is allowed to *only* __approximate__ the function computed by the deep circuit</span>{: style="color: purple"}  (Cohen et al., 2015).  
    By comparison, previous theoretical work made claims regarding only the case where the shallow circuit must exactly replicate particular functions.  


    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * [Universal Approximation Theorem (wiki)](https://en.wikipedia.org/wiki/Universal_approximation_theorem)  
    * [Stone–Weierstrass Approximation Theorem](https://en.wikipedia.org/wiki/Stone–Weierstrass_theorem)  
    <br>

***

## Unsupervised Representation Learning
{: #content2}

11. **Unsupervised Representation Learning:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents211}  
    In __Unsupervised feature learning__, features are learned with *__unlabeled__* __data__.  

    The __Goal__ of unsupervised feature learning is often to <span>discover low-dimensional features that captures some structure underlying the high-dimensional input data</span>{: style="color: purple"}.  

    <button>Examples:</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
    <div hidden="" markdown="1">
    * (Unsupervised) Dictionary Learning  
    * ICA/PCA  
    * AutoEncoders 
    * Matrix Factorization  
    * Clustering Algorithms
    </div>

    __Learning:__{: style="color: red"}  
    Unsupervised deep learning algorithms have a main training objective but also <span>__learn a representation__ as a *__side effect__*</span>{: style="color: purple"}.  

    __Unsupervised Learning for Semisupervised Learning:__{: style="color: red"}  xw
    When the feature learning is performed in an unsupervised way, it enables a form of __semisupervised learning__ where features learned from an unlabeled dataset are then employed to improve performance in a supervised setting with labeled data.  
    <br>

1. **Greedy Layer-Wise Unsupervised Pretraining:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    __(Greedy Layer-Wise) Unsupervised Pretraining__ 

    {: #lst-p}
    * __Greedy__: it is a __greedy algorithm__.  
        It optimizes each piece of the solution independently, one piece at a time, rather than jointly optimizing all pieces.  
    * __Layer-Wise__: the independent pieces are the layers of the network[^1].  
    * __Unsupervised__: each layer is trained with an unsupervised representation learning algorithm.  
    * __Pretraining__[^2]: it is supposed to be only a first step before a joint training algorithm is applied to fine-tune all the layers together.  

    This procedure is a canonical example of how a representation learned for one task (unsupervised learning, trying to capture the shape of the input distribution) can sometimes be useful for another task (supervised learning with the same input domain).  


    __Algorithm/Procedure:__{: style="color: red"}  
    <button>Algorithm</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/1wrL7C3u0dxHDgsAnbJi7tXljo56azdawSlLh7m1tk4.original.fullsize.png){: width="100%" hidden=""}  
    {: #lst-p}
    * __Supervised Learning Phase:__  
        It may involve:  
        1. Training a simple classifier on top of the features learned in the pretraining phase.  
        2. Supervised __fine-tuning__ of the entire network learned in the pretraining phase.  


    __Interpretation in Supervised Settings:__{: style="color: red"}  
    In the context of a __supervised learning__ task, the procedure can be viewed as:  
    {: #lst-p}
    * A __Regularizer__.  
        In some experiments, pretraining decreases test error without decreasing training error.  
    * A form of __Parameter Initialization__.  


    __Applications:__{: style="color: red"}  
    {: #lst-p}
    * __Training Deep Models__:  
        Greedy layer-wise training procedures based on unsupervised criteria have long been used to sidestep the difficulty of jointly training the layers of a deep neural net for a supervised task.  
        The deep learning renaissance of 2006 began with the discovery that this greedy learning procedure could be used to find a good initialization for a joint learning procedure over all the layers, and that this approach could be used to successfully train even fully connected architectures.  
        Prior to this discovery, only convolutional deep networks or networks whose depth resulted from recurrence were regarded as feasible to train.  
    * __Parameter Initialization__:  
        THey can also be used as initialization for other unsupervised learning algorithms, such as:  
        * __Deep Autoencoders__ _(Hinton and Salakhutdinov, 2006)_  
        * __Probabilistic mModels__ with __*many layers of latent variables*__:  
            E.g. __deep belief networks (DBNs)__ _(Hinton et al., 2006)_ and __deep Boltzmann machines (DBMs)__ _(Salakhutdinov and Hinton, 2009a)_.  

    <br>

2. **Clustering \| K-Means:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}  
3. **Local Linear Embeddings:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}  
4. **Principal Components Analysis (PCA):**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}  
5. **Independent Components Analysis (ICA):**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}  
6. **(Unsupervised) Dictionary Learning:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents26}  

<!-- 7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents27}
8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents28} -->

***

## Supervised Representation Learning
{: #content3}

11. **Supervised Representation Learning:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents311}  
    In __Supervised feature learning__, features are learned using *__labeled__* __data__.  

    __Learning:__{: style="color: red"}  
    The data label allows the system to compute an error term, the degree to which the system fails to produce the label, which can then be used as feedback to correct the learning process (reduce/minimize the error).  

    __Examples:__  
    {: #lst-p}
    * Supervised Neural Networks  
    * Supervised Dictionary Learning  

    __FFNs as Representation Learning Algorithms:__{: style="color: red"}  
    <button>Discussion</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
    * We can think of __Feed-Forward Neural Networks__ trained by _supervised learning_ as performing a kind of representation learning.  
    * All the layers except the last layer (usually a linear classifier), are basically producing representations (featurizing) of the input.  
    * Training with a supervised criterion naturally leads to the representation at every hidden layer (but more so near the top hidden layer) taking on properties that make the classification task easier:  
        E.g. Making classes linearly separable in the latent space.  
    * The features in the penultimate layer should learn different properties depending on the type of the last layer.  
    * Supervised training of feedforward networks does not involve explicitly imposing any condition on the learned intermediate features.  
    * We can, however, explicitly impose certain desirable conditions.  
        <button>Example: Learning Independent Representations</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
        <p hidden="" markdown="1">
        Suppose we want to learn a representation that makes density estimation easier. Distributions with more independences are easier to model, so we could design an objective function that encourages the elements of the representation vector $$\boldsymbol{h}$$ to be independent.  
        </p>  
    {: hidden=""}

1. **Greedy Layer-Wise Supervised Pretraining:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}  
    As discussed in section __8.7.4__, it is also possible to have greedy layer-wise supervised pretraining.  
    This builds on the __premise__ that <span>training a shallow network is easier than training a deep one</span>{: style="color: goldenrod"}, which seems to have been validated in several contexts (Erhan et al., 2010).<br>

2. **Neural Networks:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}  
3. **Supervised Dictionary Learning:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}  

<!-- 4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents34}
5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents35} -->  

***

## Transfer Learning and Domain Adaptation
{: #content4}

<button>Resources</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
* [ICML 2018: Advances in transfer, multitask, and semi-supervised learning (blog)](https://towardsdatascience.com/icml-2018-advances-in-transfer-multitask-and-semi-supervised-learning-2a15ef7208ec)  
* [Transfer Learning (Ruder Blog!)](http://ruder.io/transfer-learning/)  
* [Multi-Task Learning Objectives for Natural Language Processing (Ruder Blog)](http://ruder.io/multi-task-learning-nlp/)  
* [An Overview of Multi-Task Learning in Deep Neural Networks (Ruder Blog!)](http://ruder.io/multi-task/index.html)  
* [Transfer Learning Overview (paper!)](http://ftp.cs.wisc.edu/machine-learning/shavlik-group/torrey.handbook09.pdf)  
* [Transfer Learning for Deep Learning (Blog! - Resources!)](https://machinelearningmastery.com/transfer-learning-for-deep-learning/)  
* [How transferable are features in deep neural networks? (paper)](https://arxiv.org/abs/1411.1792)  
* [On Learning Invariant Representations for Domain Adaptation (blog!)](https://blog.ml.cmu.edu/2019/09/13/on-learning-invariant-representations-for-domain-adaptation/)  
* [A Comprehensive Hands-on Guide to Transfer Learning with Real-World Applications in Deep Learning (blog)](https://towardsdatascience.com/a-comprehensive-hands-on-guide-to-transfer-learning-with-real-world-applications-in-deep-learning-212bf3b2f27a)  
{: hidden=""}

![img](https://cdn.mathpix.com/snip/images/Qk1gQN3lvxom7rIa4o9ZUDHnlPfJZCVDiM6pAvkiq3s.original.fullsize.png){: width="50%"}  

1. **Introduction - Transfer Learning and Domain Adaptation:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents41}  
    __Transfer Learning__ and __Domain Adaptation__ refer to the situation where what has been learned in one setting (i.e., distribution $$P_{1}$$) is exploited to improve generalization in another setting (say distribution $$P_{2}$$).  

    This is a generalization of __unsupervised pretraining__, where we transferred representations between an unsupervised learning task and a supervised learning task.  

    In __Supervised Learning__: __transfer learning__, __domain adaptation__, and __concept drift__ can be viewed as particular forms of __Multi-Task Learning__.  
    > However, __Transfer Learning__ is a more general term that applies to both __Supervised__ and __Unsupervised Learning__, as well as, __Reinforcement Learning__.  

    __Goal/Objective and Relation to Representation Learning:__{: style="color: red"}  
    In the cases of __Transfer Learning__, __Multi-Task Learning__, and __Domain Adaptation__: 
    The __Objective/Goal__ is to <span>take advantage of data from the first setting to extract information that may be useful when learning or even when directly making predictions in the second setting</span>{: style="color: purple"}.  

    The __core idea__ of __Representation Learning__ is that <span>the same representation may be useful in both settings</span>{: style="color: purple"}.  

    Thus, we can use <span>shared representations</span>{: style="color: goldenrod"} to accomplish Transfer Learning etc.  
    __Shared Representations__ are useful to handle multiple modalities or domains, or to transfer learned knowledge to tasks for which few or no examples are given but a task representation exists.  

    <button>Transfer Learning</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/VNQ1uX35tE4SKhEHGuTA53A03GOb9Ttb_LWI6QdOjkg.original.fullsize.png){: width="80%"}  
    <br>


2. **Transfer Learning:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents42}  
    __Transfer Learning__ (in ML) is the problem of storing knowledge gained while solving one problem and applying it to a different but related problem.  

    __Definition:__  
    __Formally,__ the definition of transfer learning is given in terms of:  
    {: #lst-p}
    * A __Domain $$\mathcal{D}=\{\mathcal{X}, P(X)\}$$__, $$\:\:$$ consisting of:  
        * __Feature Space $$\mathcal{X}$$__  
        * __Marginal Probability Distribution $$P(X)$$__,  
            where $$X=\left\{x_{1}, \ldots, x_{n}\right\} \in \mathcal{X}$$.  
    * A __Task $$\mathcal{T}=\{\mathcal{Y}, f(\cdot)\}$$__,  
        (given a specific domain $$\mathcal{D}=\{\mathcal{X}, P(X)\}$$) consisting of:  
        * A __label space $$\mathcal{Y}$$__   
        * An __objective predictive function $$f(\cdot)$$__  
            It is learned from the training data, which consist of pairs $$\left\{x_ {i}, y_{i}\right\}$$, where $$x_{i} \in X$$ and $$y_{i} \in \mathcal{Y}$$.  
            It can be used to predict the corresponding label, $$f(x)$$, of a new instance $$x$$.  

    Given a source domain $$\mathcal{D}_ {S}$$ and learning task $$\mathcal{T}_ {S}$$, a target domain $$\mathcal{D}_ {T}$$ and learning task $$\mathcal{T}_ {T}$$, __transfer learning__ aims to help improve the learning of the target predictive function $$f_ {T}(\cdot)$$ in $$\mathcal{D}_ {T}$$ using the knowledge in $$\mathcal{D}_ {S}$$ and $$\mathcal{T}_ {S}$$, where $$\mathcal{D}_ {S} \neq \mathcal{D}_ {T}$$, or $$\mathcal{T}_ {S} \neq \mathcal{T}_ {T}$$.  
    <br>


    In Transfer Learning, the learner must perform two or more different tasks, but we assume that many of the factors that explain the variations in $$P_1$$ are relevant to the variations that need to be captured for learning $$P_2$$. This is typically understood in a supervised learning context, where the input is the same but the target may be of a different nature.  
    <button>Example: visual features</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
    <div hidden="" markdown="1">
    We may learn about one set of visual categories, such as cats and dogs, in the first setting, then learn about a different set of visual categories, such as ants and wasps, in the second setting.  
    If there is significantly more data in the first setting (sampled from $$P_1$$), then that may help to learn representations that are useful to quickly generalize from only very few examples drawn from $$P_2$$.  
    Many visual categories share low-level notions of edges and visual shapes, the effects of geometric changes, changes in lighting, etc.  
    </div>


    __Types of Transfer Learning:__{: style="color: red"}  
    {: #lst-p}
    * __Inductive Transfer Learning__:  
        $$\mathcal{D}_ {S} = \mathcal{D}_ {T} \:\:\: \text{  and  }\:\:\: \mathcal{T}_ {S} \neq \mathcal{T}_ {T}$$  
        __e.g.__ $$\left(\mathcal{D}_ {S} = \text{ Wikipedia } = \mathcal{D}_ {T}\right) \:\: \text{  and  } \:\: \left(\mathcal{T}_ {S} = \text{ Skip-Gram }\right) \neq \left(\mathcal{T}_ {T} = \text{ Classification }\right)$$  
    * __Transductive Transfer Learning (Domain Adaptation)__:  
        $$\mathcal{D}_ {S} \neq \mathcal{D}_ {T} \:\:\: \text{  and  }\:\:\: \mathcal{T}_ {S} = \mathcal{T}_ {T}$$  
        __e.g.__ $$\left(\mathcal{D}_ {S} = \text{ Reviews }\right) \neq \left(\mathcal{D}_ {T} = \text{ Tweets }\right) \:\: \text{  and  } \:\: \left(\mathcal{T}_ {S} = \text{ Sentiment Analysis } = \mathcal{T}_ {T}\right)$$  
    * __Unsupervised Transfer Learning__:  
        $$\mathcal{D}_ {S} \neq \mathcal{D}_ {T} \:\:\: \text{  and  }\:\:\: \mathcal{T}_ {S} \neq \mathcal{T}_ {T}$$  
        __e.g.__ $$\left(\mathcal{D}_ {S} = \text{ Animals}\right) \neq \left(\mathcal{D}_ {T} = \text{ Cars}\right) \: \text{  and  } \: \left(\mathcal{T}_ {S} = \text{ Recog.}\right) \neq \left(\mathcal{T}_ {T} = \text{ Detection}\right)$$  
    * <button>Transfer Learning</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        ![img](https://cdn.mathpix.com/snip/images/VNQ1uX35tE4SKhEHGuTA53A03GOb9Ttb_LWI6QdOjkg.original.fullsize.png){: width="60%" hidden=""}  

    
    __Concept Drift:__{: style="color: red"}  
    __Concept Drift__ is a phenomena where the statistical properties of the target variable, which the model is trying to predict, change over time in unforeseen ways. This causes problems because the predictions become less accurate as time passes.  

    It can be viewed as a form of __transfer learning__ due to <span>gradual changes in the data distribution</span>{: style="color: purple"} over time.  

    <button>Concept Drift in __RL__</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    <div hidden="" markdown="1">
    Another example is in reinforcement learning. Since the agent's policy affects the environment, the agent learning and updating its policy directly results in a changing environment with shifting data distribution.  
    </div>

    
    __Unsupervised Deep Learning for Transfer Learning:__{: style="color: red"}  
    <button>Discussion</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
    <div hidden="" markdown="1">
    Unsupervised Deep Learning for Transfer Learning has seen success in some machine learning competitions _(Mesnil et al., 2011; Goodfellow et al., 2011)_.  
    In the first of these competitions, the experimental setup is the following:  
    {: #lst-p}
    * Each participant is first given a dataset from the first setting (from distribution $$P_1$$), illustrating examples of some set of categories.  
    * The participants must use this to learn a good feature space (mapping the raw input to some representation), such that when we apply this learned transformation to inputs from the transfer setting (distribution $$P_2$$ ), a linear classifier can be trained and generalize well from very few labeled examples.  

    One of the most striking results found in this competition is that as an architecture makes use of deeper and deeper representations (learned in a purely unsupervised way from data collected in the first setting, $$P_1$$), the learning curve on the new categories of the second (transfer) setting $$P_2$$ becomes much better.  
    For __deep representations__, *fewer labeled examples* of the *transfer tasks* are necessary to achieve the apparently __asymptotic generalization__ performance.  
    </div><br>

3. **Domain Adaptation:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents43}  
    __Domain Adaptation__ is a form of *__transfer learning__* where we aim at learning from a source data distribution a well performing model on a different (but related) target data distribution.  
    
    It is a *__sequential__* process.  
    
    In __domain adaptation__, the task (and the optimal input-to output mapping) remains the same between each setting, but the input distribution is slightly different.  
    <button>Example: Sentiment Analysis</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
    <div hidden="" markdown="1">
    Consider the task of sentiment analysis, which consists of determining whether a comment expresses positive or negative sentiment. Comments posted on the web come from many categories. A domain adaptation scenario can arise when a sentiment predictor trained on customer reviews of media content such as books, videos and music is later used to analyze comments about consumer electronics such as televisions or smartphones.   
    One can imagine that there is an underlying function that tells whether any statement is positive, neutral or negative, but of course the vocabulary and style may vary from one domain to another, making it more difficult to generalize across domains.  
    Simple unsupervised pretraining (with denoising autoencoders) has been found to be very successful for sentiment analysis with domain adaptation _(Glorot et al., 2011b)_.  
    </div>


4. **Multitask Learning:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents44}  
    __Multitask Learning__ is a *__transfer learning__* where multiple learning tasks are solved at the same time, while exploiting commonalities and differences across tasks.  

    In particular, it is an approach to __inductive transfer__ that improves generalization by using the domain information contained in the training signals of related tasks as an inductive bias. It does this by learning tasks in parallel while using a shared representation; what is learned for each task can help other tasks be learned better.  

    It is a *__parallel__* process.  

    __Multitask vs Transfer Learning:__{: style="color: red"}  
    ![img](https://cdn.mathpix.com/snip/images/Qk1gQN3lvxom7rIa4o9ZUDHnlPfJZCVDiM6pAvkiq3s.original.fullsize.png){: width="50%"}
    1. __Multi-Task Learning__: general term for training on multiple tasks  
        1. __Joint Learning:__ by choosing mini-batches from two different tasks simultaneously/alternately
        1. __Pre-Training:__ first train on one task, then train on another  
            widely used for __word embeddings__.  
    1. __Transfer Learning__:  
        a type of multi-task learning where we are focused on one task; by learning on another task then applying those models to our main task  
    <br>


5. **Representation Learning for the Transfer of Knowledge:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents45}  
    We can use __Representation Learning__ to achieve __Multi-Task Learning__, __Transfer Learning__, and __Domain Adaptation__.  

    In general, __Representation Learning__ can be used to achieve __Multi-Task Learning__, __Transfer Learning__, and __Domain Adaptation__, <span>when there exist __features__ that are *useful for the different settings or tasks*, corresponding to __underlying factors__ that *appear in more than one setting*</span>{: style="color: purple"}.    
    This applies in two cases:  
    {: #lst-p}
    * __Shared *Input* Semantics__:   
        <button>E.g. Shared Visual Features</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        <div hidden="" markdown="1">
        We may learn about one set of visual categories, such as cats and dogs, in the first setting, then learn about a different set of visual categories, such as ants and wasps, in the second setting.  
        If there is significantly more data in the first setting (sampled from $$P_1$$), then that may help to learn representations that are useful to quickly generalize from only very few examples drawn from $$P_2$$.  
        Many visual categories share low-level notions of edges and visual shapes, the effects of geometric changes, changes in lighting, etc.  
        </div>
        In this case, we __share__ the __*lower* layers__, and have a __task-dependent__ __*upper* layers__.  
        <button>Illustration:</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        ![img](https://cdn.mathpix.com/snip/images/717fBbHzwKW71RWB9Lc6gA8gdFmVzymEWs_klK6t-w4.original.fullsize.png){: width="100%" hidden=""}  
    * __Shared *Output* Semantics__:  
        <button>E.g. __Speech Recognition Systems__</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        <div hidden="" markdown="1">
        A speech recognition system needs to produce valid sentences at the output layer, but the earlier layers near the input may need to recognize very different versions of the same phonemes or sub-phonemic vocalizations depending on which person is speaking.  
        </div>
        In cases like these, it makes more sense to __share__ the __*upper* layers__ (near the output) of the neural network, and have a __task-specific__ *__preprocessing__*.  
        <button>Illustration:</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        ![img](https://cdn.mathpix.com/snip/images/pFAT7AVYii3xvvOrZvGwn_lcnTZV4EVqCacUebAegYc.original.fullsize.png){: width="100%" hidden=""}
    <br>

6. **K-Shot Learning:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents46}  
    __K-Shot (Few-Shot) Learning__ is a _supervised_ learning setting (problem) where the goal is to learn from an extremely small number $$k$$ of labeled examples (called __shots__).  

    __General Setting:__  
    We first train a model on a __*large* dataset__ $$\mathcal{D}=\left\{\widetilde{\mathbf{x}}_ {i}, \widetilde{\gamma}_ {i}\right\}_ {i=1}^{N}$$ of __inputs__ $$\widetilde{\mathbf{x}}_ {i}$$ and __labels__ $$\widetilde{y}_ {i} \in\{1, \ldots, \widetilde{C}\}$$ that indicate which of the $$\widetilde{C}$$ __classes__ each input belongs to.  
    Then, using knowledge from the model trained on the large dataset, we perform $$\mathrm{k}$$-shot learning with a __*small* dataset__ $$\mathcal{D}=\left\{\mathbf{x}_ {i}, y_ {i}\right\}_ {i=1}^{N}$$ with $$C$$ __*new* classes__, labels $$y_ {i} \in\{\widetilde{C}+1, \widetilde{C}+C\}$$ and __*$$k$$* examples (inputs)__ from each new class.  
    During test time we classify unseen examples (inputs) $$\mathbf{x}^{* }$$ from the new classes $$C$$ and evaluate the predictions against ground truth labels $$y^{* }$$.  


    __Comparison to alternative Learning Paradigms:__{: style="color: red"}  
    ![img](https://cdn.mathpix.com/snip/images/UcWrNybNWHVrfmFVHkf69cc6UiIivyatymeq-e99MSI.original.fullsize.png){: width="60%"}  


    __As Transfer Learning:__{: style="color: red"}  
    Two extreme forms of __transfer learning__ are __One-Shot Learning__ and __Zero-Shot Learning__; they provide only *__one__* and *__zero__* labeled examples of the transfer task, respectively.  


    __One-Shot Learning:__{: style="color: red"}  
    __One-Shot Learning__ _(Fei-Fei et al., 2006)_ is a form of __k-shot learning__ where $$k=1$$.  
    
    It is possible because the representation learns to cleanly separate the underlying classes during the first stage.  
    During the transfer learning stage, only one labeled example is needed to infer the label of many possible test examples that all cluster around the same point in representation space.  
    This works to the extent that the factors of variation corresponding to these invariances have been cleanly separated from the other factors, in the learned representation space, and we have somehow learned which factors do and do not matter when discriminating objects of certain categories.  


    __Zero-Shot Learning:__{: style="color: red"}  
    __Zero-Shot Learning__ _(Palatucci et al., 2009; Socher et al., 2013b)_ or __Zero-data learning__ _(Larochelle et al., 2008)_ is a form of __k-shot learning__ where $$k=0$$.  

    __Example: Zero-Shot Learning Setting__  
    Consider the problem of having a learner read a large collection of text and then solve object recognition problems.  
    It may be possible to recognize a specific object class even without having seen an image of that object, if the text describes the object well enough.  
    For example, having read that a cat has four legs and pointy ears, the learner might be able to guess that an image is a cat, without having seen a cat before.  


    __Justification and Interpretation:__  
    Zero-Shot Learning is only possible because <span>__additional information__ has been exploited during training</span>{: style="color: purple"}.  

    We can think of think of the zero-data learning scenario as including __*three* random variables__:  
    {: #lst-p}
    1. (Traditional) __Inputs__ $$x$$  
    2. (Traditional) __Outputs__ or __Targets__ $$\boldsymbol{y}$$
    3. (Additional) __Random Variable *describing the task*__, $$T$$  

    The model is trained to estimate the conditional distribution $$p(\boldsymbol{y} \vert \boldsymbol{x}, T)$$.  
    {: #lst-p}
    * <button>Example: _updated_ zero-shot learning setting</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        <div hidden="" markdown="1">
        In the example of recognizing cats after having read about cats, the output is a binary variable $$y$$ with $$y=1$$ indicating "yes" and $$y=0$$ indicating "no".  
        The task variable $$T$$ then represents questions to be answered such as "Is there a cat in this image?".  
        If we have a training set containing unsupervised examples of objects that live in the Same space as $$T$$, we may be able to infer the meaning of unseen instances of $$T$$.  
        In our example of recognizing cats without having seen an image of the cat, it is important that we have had unlabeled text data containing sentences such as "cats have four legs" or "cats have pointy ears".  
        </div>

    __Representing the task $$T$$:__  
    Zero-shot learning requires $$T$$ to be represented in a way that <span>allows some sort of __generalization__</span>{: style="color: purple"}.  
    For example, $$T$$ cannot be just a _one-hot code_ indicating an object category.  
    > _Socher et al. (2013 b)_ provide instead a distributed representation of object categories by using a learned word embedding for the word associated with each category.  

    
    __Representation Learning for Zero-Shot Learning:__{: style="color: red"}  
    The principle, underlying __zero-shot learning__ as a form of __transfer learning__: <span>capturing a __representation__ in __*one* modality__</span>{: style="color: purple"}, <span>a __representation__ in __*another* modality__</span>{: style="color: purple"}, and the <span>__relationship__</span>{: style="color: purple"} (in general a __joint distribution__) <span>between pairs $$(\boldsymbol{x}, \boldsymbol{y})$$</span>{: style="color: purple"} consisting of _one observation $$\boldsymbol{x}$$ in one modality_ and _another observation $$\boldsymbol{y}$$ in the other modality_, _(Srivastava and Salakhutdinov, 2012)_.   
    By learning all three sets of parameters (from $$\boldsymbol{x}$$ to its representation, from $$\boldsymbol{y}$$ to its representation, and the relationship between the two representations), concepts in one representation are anchored in the other, and vice-versa, allowing one to meaningfully generalize to new pairs.  

    In particular, <span>Transfer learning between two domains $$x$$ and $$y$$ enables zero-shot learning</span>{: style="color: goldenrod"}.  

    <button>Illustration</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/FhmatT_1_acHctjXuwq9kRjPlpqPCwLyOnMP0aSHzXI.original.fullsize.png){: width="100%" hidden=""}  


    __Zero-Shot Learning in Machine Translation:__  
    <button>Discussion - Example</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
    <div hidden="" markdown="1">
    A similar phenomenon happens in machine translation _(Klementiev et al., 2012; Mikolov et al., 2013b; Gouws et al., 2014)_:  
    we have words in one language, and the relationships between words can be learned from unilingual corpora; on the other hand, we have translated sentences which relate words in one language with words in the other. Even though we may not have labeled examples translating word $$A$$ in language $$X$$ to word $$B$$ in language $$Y$$, we can generalize and guess a translation for word $$A$$ because we have learned a distributed representation for words in language $$X$$, a distributed representation for words in language $$Y$$, and created a link (possibly two-way) relating the two spaces, via training examples consisting of matched pairs of sentences in both languages.  
    This transfer will be most successful if all three ingredients (the two representations and the relations between them) are learned jointly.  
    </div>

    __Relation to Multi-modal Learning:__  
    Zero-Shot Learning can be performed using __Multi-model Learning__, and vice-versa.  
    The same principle of __transfer learning__ with __representation learning__ explain how one can perform either tasks.  



    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * [K-Shot Learning (Thesis!)](https://pdfs.semanticscholar.org/8fc6/4f04a94033704453255c905796872e16f284.pdf?_ga=2.177121317.1868310785.1568811982-246730594.1555910960)  
    * [One Shot Learning and Siamese Networks in Keras (Code - Tutorial)](https://sorenbouma.github.io/blog/oneshot/)  
    * __Zero-Shot Learning__: is a form of extending supervised learning to a setting of solving for example a classification problem when not enough labeled examples are available for all classes.   
        > "Zero-shot learning is being able to solve a task despite not having received any training examples of that task." - Goodfellow  
    * __Detecting *Gravitational Waves*__ is a form of __Zero-Shot Learning__   
    * Few-shot, one-shot or zero-shot learning are encompassed in a recently emerging field known as __meta-learning__.  
        While traditionally including mainly classification, recent works in meta-learning have included regression and reinforcement learning ([Vinyals et al., 2016](https://arxiv.org/abs/1606.04080)) ([Andrychowicz et al., 2016](https://arxiv.org/abs/1606.04474)) ([Ravi & Larochelle, 2017](https://openreview.net/forum?id=rJY0-Kcll)) ([Duan et al., 2017](https://arxiv.org/abs/1611.02779)) ([Finn et al., 2017](https://arxiv.org/pdf/1703.03400.pdf)).  
        Works in this area seems to be primarily motivated by the notion of human-level AI, since humans appear to be able to require far fewer training data than most deep learning models.  
    <br>


7. **Multi-Modal Learning:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents47}  
    __Multi-Modal Learning__   


    __Representation Learning for Multi-modal Learning:__{: style="color: red"}  
    The same principle, underlying __zero-shot learning__ as a form of __transfer learning__, explains how one can perform multi-modal learning; capturing a representation in one modality, a representation in the other, and the relationship (in general a joint distribution) between pairs $$(\boldsymbol{x}, \boldsymbol{y})$$ consisting of one observation $$\boldsymbol{x}$$ in one modality and another observation $$\boldsymbol{y}$$ in the other modality _(Srivastava and Salakhutdinov, 2012)_.   
    By learning all three sets of parameters (from $$\boldsymbol{x}$$ to its representation, from $$\boldsymbol{y}$$ to its representation, and the relationship between the two representations), concepts in one representation are anchored in the other, and vice-versa, allowing one to meaningfully generalize to new pairs.  




***

## Causal Factor Learning
{: #content5}

<!-- 1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents51}
2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents52}
 -->

3. **Semi-Supervised Disentangling of Causal Factors:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents53}  
    
    __Quality of Representations:__{: style="color: red"}  
    \- An important question in Representation Learning is:  
    <span>_“what makes one representation better than another?”_</span>{: style="color: purple"}   
    {: #lst-p}
    1. One answer to that is the __Causal Factors Hypothesis:__  
        An __ideal representation__ is one in which <span>the __features__ within the representation _correspond_ to the underlying __causes__ of the observed data</span>{: style="color: purple"}, with __*separate* features__ or __directions__ in _feature space_ corresponding to __*different* causes__, so that <span>the __representation__ *__disentangles__* the __causes__ from one another</span>{: style="color: purple"}.  
        * This hypothesis *motivates* approaches in which we first <span>seek a __*good* representation__ for $$p(\boldsymbol{x})$$</span>{: style="color: purple"}.  
            This representation may also be a *good* representation for __computing $$p(\boldsymbol{y} \vert \boldsymbol{x})$$__ if $$\boldsymbol{y}$$ is among the __most *salient*__ __causes__ of $$\boldsymbol{x}$$[^3] [^4].  
    2. __Ease of Modeling:__  
        In many approaches to representation learning, we are often concerned with a representation that is __easy to model__ (e.g. sparse entries, independent entries etc.).  
        It is not directly observed, however, that <span>a representation that __cleanly separates the underlying causal factors__ is, also, one that is __easy to model__</span>{: style="color: purple"}.  
        The answer to that is an __*extension*__ of the __Causal Factor Hypothesis:__  
        For *__many__* __AI tasks__ the two properties __coincide__: once we are able to <span>obtain the underlying explanations for the observations</span>{: style="color: purple"}, it generally becomes <span>easy to isolate individual attributes</span>{: style="color: purple"} from the others.  
        Specifically, __if__ a <span>__representation $$\boldsymbol{h}$$__ _represents_ many of the *__underlying causes__* of the __observed $$\boldsymbol{x}$$__</span>{: style="color: purple"}, __and__ the <span>__outputs $$\boldsymbol{y}$$__ are among the __most *salient causes*__</span>{: style="color: purple"}, __then__ it is <span>easy to __predict__ $$\boldsymbol{y}$$ from $$\boldsymbol{h}$$</span>{: style="color: purple"}.  

    
    <div class="borderexample" markdown="1">
    <span> The complete __Causal Factors Hypothesis__ <span>*motivates* __Semi-Supervised Learning__ via __Unsupervised Representation Learning__</span>{: style="color: goldenrod"}.</span>
    </div>


    __Analysis - When does Semi-Supervised Learning Work:__{: style="color: red"}  
    <button>Full Analysis</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
    <div hidden="" markdown="1">
    * __When does Semi-Supervised Disentangling of Causal Factors *Work*?__  
        Let's start by considering two scenarios where Semi-Supervised Learning via Unsupervised Representation Learning Fails and Succeeds:  
        * <button>Failure</button>{: .showText value="show" onclick="showTextPopHide(event);"}
            <div hidden="" markdown="1">
            Let us see how semi-supervised learning can fail because <span>__unsupervised learning__ of $$p(\mathbf{x})$$ is of __*no help* to learn__ $$p(\mathbf{y} \vert \mathbf{x})$$</span>{: style="color: purple"}.  
            Consider the case where $$p(\mathbf{x})$$ is __uniformly distributed__ and we want to learn $$f(\boldsymbol{x})=\mathbb{E}[\mathbf{y} \vert \boldsymbol{x}]$$.  
            Clearly, __observing a training set__ of $$\boldsymbol{x}$$ values *__alone__* gives us __no information__ about $$p(\mathbf{y} \vert \mathbf{x})$$.  
            </div>
        * <button>Success</button>{: .showText value="show" onclick="showTextPopHide(event);"}
            <div hidden="" markdown="1">
            Consider the case where $$x$$ arises from a mixture, with one mixture component per value of $$y$$.  
            If the mixture components are __well-separated__, then modeling $$p(x)$$ reveals precisely where each component is, and <span>a __single labeled example__ of *each class* will then be *__enough__* to perfectly __learn__ $$p(\mathbf{y} \vert \mathbf{x})$$</span>{: style="color: purple"}.    
            <button>Illustration: Well-Separated Mixture</button>{: .showText value="show" onclick="showTextPopHide(event);"}
            ![img](https://cdn.mathpix.com/snip/images/ctuu5i3mZUhHsIdzpRMp4SJXHz_iWb_5_YnCfWXuCZg.original.fullsize.png){: width="100%" hidden=""}  
            </div>

        <div class="borderexample" markdown="1">
        <span>Thus, we conclude that semi-supervised learning works <span>when $$p(\mathbf{y} \vert \mathbf{x})$$ and $$p(\mathbf{x})$$ are __tied__ together</span>{: style="color: goldenrod"}.</span>  
        </div>
    * __When are $$p(\mathbf{y} \vert \mathbf{x})$$ and $$p(\mathbf{x})$$ tied?__  
        This happens when $$\mathbf{y}$$ is closely associated with one of the causal factors of $$\mathbf{x}$$, then $$p(\mathbf{x})$$ and $$p(\mathbf{y} \vert \mathbf{x})$$ will be strongly tied.  
        * Thus, unsupervised representation learning that tries to disentangle the underlying factors of variation is likely to be useful as a semi-supervised learning strategy.  

    Now, Consider the assumption that $$\mathbf{y}$$ is one of the causal factors of $$\mathbf{x}$$, and let $$\mathbf{h}$$ represent all those factors:  
    {: #lst-p}
    * The __"true" generative process__ can be conceived as <span>*__structured__* according to this __directed graphical model__</span>{: style="color: purple"}, with $$\mathbf{h}$$ as the __parent__ of $$\mathbf{x}$$:  
        <p>$$p(\mathbf{h}, \mathbf{x})=p(\mathbf{x} \vert \mathbf{h}) p(\mathbf{h})$$</p>  
        * As a consequence, the __data__ has __marginal probability__:  
            <p>$$p(\boldsymbol{x})=\mathbb{E}_ {\mathbf{h}} p(\boldsymbol{x} \vert \boldsymbol{h})$$</p>  

        From this straightforward observation, we __conclude__ that:  
        <div class="borderexample" markdown="1">
        <span>The <span>__best possible model__ of $$\mathbf{x}$$ (wrt. __generalization__) is the one that *__uncovers__* the above __"true" structure__, with $$\boldsymbol{h}$$ as a __latent variable__ that *__explains__* the __observed variations__ in $$\boldsymbol{x}$$</span>{: style="color: goldenrod"}.</span>  
        </div>  
        I.E. The __"ideal" representation learning__ discussed above should thus __recover these latent factors__.  
        If $$\mathbf{y}$$ is one of these (or closely related to one of them), then it will be very easy to learn to predict $$\mathbf{y}$$ from such a representation.  
    * We also see that the __conditional distribution__ of $$\mathbf{y}$$ given $$\mathbf{x}$$ is <span>tied by *Bayes' rule* to the __components in the above equation__</span>{: style="color: purple"}:  
        <p>$$p(\mathbf{y} \vert \mathbf{x})=\frac{p(\mathbf{x} \vert \mathbf{y}) p(\mathbf{y})}{p(\mathbf{x})}$$</p>  

        <div class="borderexample" markdown="1">
        <span>Thus the <span>__marginal__ $$p(\mathbf{x})$$ is *__intimately tied__* to the __conditional__ $$p(\mathbf{y} \vert \mathbf{x})$$, and knowledge of the structure of the former should be helpful to learn the latter</span>{: style="color: purple"}.</span>  
        </div>
    <br>
    <div class="borderexample" markdown="1">
    <span>Therefore, __in situations respecting these assumptions, semi-supervised learning should improve performance__.</span>  
    </div>  
    </div>

    __Justifying the setting where Semi-Supervised Learning Works:__  
    {: #lst-p}
    * __Semi-Supervised Learning[^5] *Works*__ when: <span>$$p(\mathbf{y} \vert \mathbf{x})$$ and $$p(\mathbf{x})$$ are *__tied together__*</span>{: style="color: goldenrod"}.  
    * __$$p(\mathbf{y} \vert \mathbf{x})$$ and $$p(\mathbf{x})$$ are *Tied*__ when: $$\mathbf{y}$$ is *__closely associated__* with one of the __causal factors__ of $$\mathbf{x}$$, or it is a __causal factor itself__.  
        * Let $$\mathbf{h}$$ represent all the __causal factors__ of $$\mathbf{x}$$, and let $$\mathbf{y} \in \mathbf{h}$$ (be a __causal factor__ of $$\mathbf{x}$$), then:  
            The __"true" generative process__ can be conceived as <span>*__structured__* according to this __directed graphical model__</span>{: style="color: purple"}, with $$\mathbf{h}$$ as the __parent__ of $$\mathbf{x}$$:  
            <p>$$p(\mathbf{h}, \mathbf{x})=p(\mathbf{x} \vert \mathbf{h}) p(\mathbf{h})$$</p>  
            * __Thus__, the __Marginal Probability of the Data $$p(\mathbf{x})$$__ is:  
                1. <span>*__Tied__* to the __conditional__ $$p(\mathbf{x} \vert \mathbf{h})$$</span>{: style="color: purple"} as:  
                    <p>$$p(\boldsymbol{x})=\mathbb{E}_ {\mathbf{h}} p(\boldsymbol{x} \vert \boldsymbol{h})$$</p>  
                    $$\implies$$  
                    * The <span>__best possible model__ of $$\mathbf{x}$$ (wrt. __generalization__)</span>{: style="color: goldenrod"} is the one that <span>*__uncovers__* the above __"true" structure__</span>{: style="color: goldenrod"}, with <span>$$\boldsymbol{h}$$ as a __latent variable__ that *__explains__* the __observed variations__ in $$\boldsymbol{x}$$</span>{: style="color: goldenrod"}.  
                        I.E. The __“ideal” representation learning__ discussed above __should__ thus __*recover*__ these __latent factors__.  
                2. <span>*__(intimately) Tied__* to the __conditional__ $$p(\mathbf{y} \vert \mathbf{x})$$</span>{: style="color: purple"} (by __Bayes' rule__) as:  
                    <p>$$p(\mathbf{y} \vert \mathbf{x})=\frac{p(\mathbf{x} \vert \mathbf{y}) p(\mathbf{y})}{p(\mathbf{x})}$$</p>  

    <div class="borderexample" markdown="1">
    <span>Therefore, __in situations respecting these assumptions, semi-supervised learning should improve performance__.</span>  
    </div>


    __Encoding/Learning Causal Factors:__{: style="color: red"}  
    {: #lst-p}
    * __Problem - Number of Causal Factors:__{: style="color: DarkRed"}  
        An important research problem regards the fact that <span>most observations are formed by an _extremely_ __*large number* of underlying causes__</span>{: style="color: purple"}.  
        * Suppose $$\mathbf{y}=\mathrm{h}_ {i}$$, but the unsupervised learner does not know which $$\mathrm{h}_ {i}$$:  
            * The __brute force solution__ is for an unsupervised learner to <span>learn a representation that __captures *all* the reasonably salient generative factors__ $$\mathrm{h}_ {j}$$ and disentangles them from each other</span>{: style="color: purple"}, thus making it easy to predict $$\mathbf{y}$$ from $$\mathbf{h}$$, regardless of which $$\mathrm{h}_ {i}$$ is associated with $$\mathbf{y}$$.  
                * In practice, the brute force solution is __not feasible__ because it is _not possible to capture all or most of the factors of variation that influence an observation_.  
                    For example, in a visual scene, should the representation always encode all of the smallest objects in the background?  
                    It is a well-documented psychological phenomenon that human beings fail to perceive changes in their environment that are not immediately relevant to the task they are performing _Simons and Levin (1998)_.  
    * __Solution - Determining which causal factor to encode/learn:__{: style="color: DarkRed"}   
        An important research frontier in semi-supervised learning is determining <span>_"what to encode in each situation"_</span>{: style="color: purple"}.  
        * Currently, there are __two main strategies__ for _dealing with a large number of underlying causes_:  
            1. Use a __supervised learning signal__ at the same time as the __(*"plus"*) unsupervised learning signal__,  
                so that the model will choose to capture the most relevant factors of variation. 
            2. Use __much larger representations__ if using *purely unsupervised learning*.  
        * __New (Emerging) Strategy__ for __unsupervised learning__:  
            <span>Redefining the *definition* of "__salient__" factors</span>{: style="color: goldenrod"}.  

    <!-- __Modifying the definition of "*Salient*" Factors:__{: style="color: red"}   -->

    __The definition of "*Salient*":__{: style="color: red"}  
    {: #lst-p}
    * The _current_ __definition of *"salient"* factors:__  
        In practice, we _encode_ the definition of _"salient"_ by using the __objective criterion__ (e.g. MSE).  
        > Historically, autoencoders and generative models have been trained to optimize a fixed criterion, often similar to MSE.  

        * __Problem with current definition__:  
            Since these fixed criteria determine which causes are considered salient, they will be emphasizing different factors depending on their e.g. effects on the error:    
            * E.g. MSE applied to the pixels of an image implicitly specifies that an underlying cause is only salient if it significantly changes the brightness of a large number of pixels.  
                This can be problematic if the task we wish to solve involves interacting with small objects.  
                <button>Illustration: AutoEncoder w/ MSE</button>{: .showText value="show" onclick="showTextPopHide(event);"}
                ![img](https://cdn.mathpix.com/snip/images/mEJX8pk5A1QENzLNvH4WLOzEzWaH61y-wpq6iIraGA0.original.fullsize.png){: width="100%" hidden=""}  
    * __Learned (pattern-based) "Saliency"__:  
        Certain factors could be considered *"salient"* if they follow a __*highly recognizable* pattern__.  
        E.g. if a group of pixels follow a highly recognizable pattern, even if that pattern does not involve extreme brightness or darkness, then that pattern could be considered extremely salient.  

        * This definition is _implemented_ by __Generative Adversarial Networks (GANs)__.  
            In this approach, a generative model is trained to fool a feedforward classifier. The feedforward classifier attempts to recognize all samples from the generative model as being fake, and all samples from the training set as being real.  
            In this framework, <span>any *__structured pattern__* that the feedforward network can *recognize* is __highly salient__</span>{: style="color: purple"}.  
            They <span>*__learn__* how to determine what is salient</span>{: style="color: goldenrod"}.  
            <button>Example: Advantages of Adversarial Framework in Learning Ears</button>{: .showText value="show" onclick="showTextPopHide(event);"}
            <div hidden="" markdown="1">
            _Lotter et al. (2015)_ showed that models trained to generate images of human heads will often neglect to generate the ears when trained with mean squared error, but will successfully generate the ears when trained with the adversarial framework.  
            Because the ears are not extremely bright or dark compared to the surrounding skin, they are not especially salient according to mean squared error loss, but their highly recognizable shape and consistent position means that a feedforward network can easily learn to detect them, making them highly salient under the generative adversarial framework.    
            <button>Illustration: Generating Faces w/ Ears</button>{: .showText value="show" onclick="showTextPopHide(event);"}
            ![img](https://cdn.mathpix.com/snip/images/f23z_MZr459udxGiWj0dqEV7ai-QcU9ru7a67utkDJ8.original.fullsize.png){: width="100%" hidden=""}  
            </div>
    
    Generative adversarial networks are only one step toward __determining *which factors should be represented*__.  
    We expect that __future research__{: style="color: goldenrod"} will discover <span>better ways of determining __which factors to represent__</span>{: style="color: purple"}, and develop <span>mechanisms for __*representing* different factors__ *depending on the task*</span>{: style="color: purple"}.  

    __Robustness to Change - Causal Invariance:__{: style="color: red"}  
    A __benefit__ of learning the underlying causal factors _(Schölkopf et al. (2012))_ is that:  
    if the __true generative process__ has <span>$$\mathbf{x}$$ as an *__effect__*</span>{: style="color: purple"} and <span>$$\mathbf{y}$$ as a *__cause__*</span>{: style="color: purple"}, then __modeling $$p(\mathbf{x} \vert \mathbf{y})$$__ is <span>robust to changes in $$p(\mathbf{y})$$</span>{: style="color: goldenrod"}.  
    > If the cause-effect relationship was reversed, this would not be true, since by Bayes' rule, $$p(\mathbf{x} \vert \mathbf{y})$$ would be sensitive to changes in $$p(\mathbf{y})$$.  

    Very often, when we consider changes in distribution due to __different domains__, __temporal non-stationarity__, or __changes in the nature of the task__, __*the causal mechanisms remain invariant*__{: style="color: goldenrod"} (the laws of the universe are constant) while the __marginal distribution over the underlying causes__ can *__change__*.  
    Hence, better __generalization and robustness__ to all kinds of changes can be expected via __learning a generative model that attempts to recover the causal factors__{: style="color: goldenrod"} $$\mathbf{h}$$ and $$p(\mathbf{x} \vert \mathbf{h})$$.  
    <br>

4. **Providing Clues to Discover Underlying Causes:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents54}  
    __Quality of Representations:__{: style="color: red"}  
    The answer to the following question:  
    <span>_“what makes one representation better than another?”_</span>{: style="color: purple"}   
    was the __Causal Factors Hypothesis:__  
    An __ideal representation__ is one in which <span>the __features__ within the representation _correspond_ to the underlying __causes__ of the observed data</span>{: style="color: purple"}, with __*separate* features__ or __directions__ in _feature space_ corresponding to __*different* causes__, so that <span>the __representation__ *__disentangles__* the __causes__ from one another</span>{: style="color: purple"}, especially those factors that are relevant to our applications.  

    __Clues for Finding the Causal Factors of Variation:__{: style="color: red"}  
    Most strategies for representation learning are based on:  
    <span>Introducing clues that help the learning to find these underlying factors of variations</span>{: style="color: purple"}.  
    The clues can help the learner separate these observed factors from the others.  
    
    __Supervised learning__ provides a *__very strong__* __clue__: a __label__ $$\boldsymbol{y},$$ presented with each $$\boldsymbol{x},$$ that usually specifies the value of at least one of the factors of variation directly.  

    More generally, to make use of abundant unlabeled data, representation learning makes use of other, less direct, hints about the underlying factors.  
    These hints take the form of __implicit prior beliefs__ that we, the designers of the learning algorithm, impose in order to <span>guide the learner</span>{: style="color: purple"}.  

    __Clues in the form of Regularization:__{: style="color: red"}  
    Results such as the __no free lunch theorem__ show that <span>__regularization__ strategies are necessary to obtain __good generalization__</span>{: style="color: purple"}.  
    While it is impossible to find a universally superior regularization strategy, one goal of deep learning is to find a __set of fairly generic regularization strategies__ that are *applicable to a wide variety of AI tasks*, similar to the tasks that people and animals are able to solve.  

    We can <span>use _generic_ __regularization strategies__ to _encourage_ learning algorithms to discover __features__ that *__correspond__* to __underlying factors__</span>{: style="color: goldenrod"}, E.G. _(Bengio et al. (2013d))_:  
    {: #lst-p}
    * __Smoothness__: This is the assumption that $$f(\boldsymbol{x}+\epsilon \boldsymbol{d}) \approx f(\boldsymbol{x})$$ for unit $$\boldsymbol{d}$$ and small $$\epsilon$$. This assumption allows the learner to generalize from training examples to nearby points in input space. Many machine learning algorithms leverage this idea, but it is insufficient to overcome the curse of dimensionality.  
    * __Linearity__: Many learning algorithms assume that relationships between some variables are linear. This allows the algorithm to make predictions even very far from the observed data, but can sometimes lead to overly extreme predictions. Most simple machine learning algorithms that do not make the smoothness assumption instead make the linearity assumption. These are in fact different assumptions—<span>linear functions with large weights applied to high-dimensional spaces may not be very smooth</span>{: style="color: goldenrod"}[^7].
    * __Multiple explanatory factors__: Many representation learning algorithms are motivated by the assumption that the data is generated by multiple underlying explanatory factors, and that most tasks can be solved easily given the state of each of these factors. Section 15.3 describes how this view motivates semisupervised learning via representation learning. Learning the structure of $$p(\boldsymbol{x})$$ requires learning some of the same features that are useful for modeling $$p(\boldsymbol{y} \vert \boldsymbol{x})$$ because both refer to the same underlying explanatory factors. Section 15.4 describes how this view motivates the use of distributed representations, with separate directions in representation space corresponding to separate factors of variation. 
    * __Causal factors__: the model is constructed in such a way that it treats the factors of variation described by the learned representation $$\boldsymbol{h}$$ as the causes of the observed data $$\boldsymbol{x}$$, and not vice-versa. As discussed in section 15.3, this is advantageous for semi-supervised learning and makes the learned model more robust when the distribution over the underlying causes changes or when we use the model for a new task. 
    * __Depth, or a hierarchical organization of explanatory factors__: High-level, abstract concepts can be defined in terms of simple concepts, forming a hierarchy. From another point of view, the use of a deep architecture expresses our belief that the task should be accomplished via a multi-step program, with each step referring back to the output of the processing accomplished via previous steps.  
    * __Shared factors across tasks__: In the context where we have many tasks, corresponding to different $$y_{i}$$ variables sharing the same input $$\mathbf{x}$$ or where each task is associated with a subset or a function $$f^{(i)}(\mathbf{x})$$ of a global input $$\mathbf{x},$$ the assumption is that each $$\mathbf{y}_ {i}$$ is associated with a different subset from a common pool of relevant factors $$\mathbf{h}$$. Because these subsets overlap, learning all the $$P\left(y_{i} \vert \mathbf{x}\right)$$ via a shared intermediate representation $$P(\mathbf{h} \vert \mathbf{x})$$ allows sharing of statistical strength between the tasks.  
    * __Manifolds__: Probability mass concentrates, and the regions in which it concentrates are locally connected and occupy a tiny volume. In the continuous case, these regions can be approximated by low-dimensional manifolds with a much smaller dimensionality than the original space where the data lives. Many machine learning algorithms behave sensibly only on this manifold (Goodfellow et al., 2014b). Some machine learning algorithms, especially autoencoders, attempt to explicitly learn the structure of the manifold. 
    * __Natural clustering__: Many machine learning algorithms assume that each connected manifold in the input space may be assigned to a single class. The data may lie on many disconnected manifolds, but the class remains constant within each one of these. This assumption motivates a variety of learning algorithms, including tangent propagation, double backprop, the manifold tangent classifier and adversarial training. 
    * __Temporal and spatial coherence__: Slow feature analysis and related algorithms make the assumption that the most important explanatory factors change slowly over time, or at least that it is easier to predict the true underlying explanatory factors than to predict raw observations such as pixel values. See section 13.3 for further description of this approach. 
    * __Sparsity__: Most features should presumably not be relevant to describing most inputs—there is no need to use a feature that detects elephant trunks when representing an image of a cat. It is therefore reasonable to impose a prior that any feature that can be interpreted as “present” or “absent” should be absent most of the time. 
    * __Simplicity of Factor Dependencies__: In good high-level representations, the factors are related to each other through simple dependencies. The simplest possible is marginal independence, $$P(\mathbf{h})=\prod_{i} P\left(\mathbf{h}_ {i}\right)$$, but linear dependencies or those captured by a shallow autoencoder are also reasonable assumptions. This can be seen in many laws of physics, and is assumed when plugging a linear predictor or a factorized prior on top of a learned representation.  
        * <span>_Consciousness Prior_</span>{: style="color: goldenrod"}:    
            * <button>Discussion</button>{: .showText value="show" onclick="showTextPopHide(event);"}
                * __Key Ideas:__  
                    (1) Seek Objective Functions defined purely in abstract space (no decoders)   
                    (2) _"Conscious"_ thoughts are *__low-dimensional__*.  
                    * Conscious thoughts are very *__low-dimensional__* objects compared to the full state of the (unconscious) brain  
                    * Yet they have unexpected predictive value or usefulness  
                        $$\rightarrow$$ strong constraint or prior on the underlying representation  
                        > e.g. we can plan our lives by only thinking of simple/short sentences at a time, that can be expressed with few variables (words); short-term memory is only 7 words (underutilization? no, rather, __prior__).  

                        * __Thought__: composition of few selected factors / concepts (key/value) at the highest level of abstraction of our brain.  
                        * Richer than but closely associated with short verbal expression such as a __sentence__ or phrase, a __rule__ or __fact__ (link to classical symbolic Al & knowledge representation)  
                    * Thus, <span>*__true__* __statements__ about the __very complex__ world, could be conveyed with very *__low-dimensional__* representations</span>{: style="color: goldenrod"}.  
                * __How to select a few *relevant* abstract concepts making a thought__:  
                    <span>Content-based __Attention__</span>{: style="color: goldenrod"}.  
                    * Thus, <span>__Abstraction__ is *related to* __Attention__:</span>{: style="color: purple"}  
                        <button>Relation between __Abstraction__ and __Attention__</button>{: .showText value="show" onclick="showTextPopHide(event);"}
                        ![img](https://cdn.mathpix.com/snip/images/f-kwoXKJhtC3oGzLt8HQfdcl3-x8T9-aULdanqZaqnI.original.fullsize.png){: width="100%" hidden=""}  
                * __Two Levels of Representations__:  
                    * High-dimensional abstract representation space (all known concepts and factors) $$h$$  
                    * Low-dimensional conscious thought $$c,$$ extracted from $$h$$  
                        * $$c$$ includes names (keys) and values of factors  
                    ![img](https://cdn.mathpix.com/snip/images/TwwbkSLzeI_DT6oFP1Y1DWkIQXjQOsHGs9bcT3f4cfE.original.fullsize.png){: width="50%"}  
                    * The __Goal__ of <span>using attention on the unconscious states</span>{: style="color: purple"}:  
                        is to put pressure (constraint) on the _mapping between input and representations (Encoder)_ and the _unconscious states representations $$h$$_ such that the Encoder is encouraged to learn representations that have the property that <span>that if I pick just a few elements of it, I can make a true statement or very highly probable statement about the world, (e.g. a highly probable prediction)</span>{: style="color: purple"}.  
                {: hidden=""}

    * __Causal/Mechanism Independence__:  
        * <span>_Controllable Factors_</span>{: style="color: purple"}.  

    
    The concept of representation learning ties together all of the many forms of deep learning.  
    Feedforward and recurrent networks, autoencoders and deep probabilistic models all learn and exploit representations. Learning the best possible representation remains an exciting avenue of research.  
    <br>


<!-- 4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents54}
5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents55}
 -->



[^1]: It proceeds one layer at a time, training the k -th layer while keeping the previous ones fixed. In particular, the lower layers (which are trained first) are not adapted after the upper layers are introduced.  
[^2]: Commonly, “pretraining” to refer not only to the pretraining stage itself but to the entire two phase protocol that combines the pretraining phase and a supervised learning phase.  
[^3]: This idea has guided a large amount of deep learning research since at least the 1990s _(Becker and Hinton, 1992; Hinton and Sejnowski, 1999)_, in more detail.  
[^4]: For other arguments about when <span>__semi-supervised__ learning can outperform pure __supervised__ learning</span>{: style="color: purple"}, we refer the reader to _section 1.2_ of _Chapelle et al. (2006)_.
[^5]: Using __unsupervised representation learning__ that tries to *__disentangle__* the __underlying factors of variation__.  
[^6]: It is also called a one-hot representation, since it can be captured by a binary vector with $$n$$ bits that are mutually exclusive (only one of them can be active).  
[^7]: See _Goodfellow et al. (2014b)_ for a further discussion of the limitations of the linearity assumption.  