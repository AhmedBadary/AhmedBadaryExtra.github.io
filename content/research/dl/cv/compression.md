---
layout: NotesPage
title: Generative Compression
permalink: /work_files/research/dl/compression
prevLink: /work_files/research/dl/cv.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Introduction](#content1)
  {: .TOC1}
  * [WaveOne](#content2)
  {: .TOC2}
  * [Proposed Changes](#content3)
  {: .TOC3}
</div>

***
***


[Feature Extraction (Notes - Docs)](https://docs.google.com/document/d/12yb9bhZfr84e6tPJwwJrKXpNKVEhhbmoMgOGl_gGbBY/edit)  
[Audio Compression](https://docs.google.com/document/d/1TUHWxU3TPR1mRCDF1kUM9xgNmvVHe5f9KxvBb4sPu_Q/edit)  
* [A Deep Learning Approach to Data Compression (Blog+Paper!)](https://bair.berkeley.edu/blog/2019/09/19/bit-swap/)  


## Introduction
{: #content1}
 

5. **ML-based Compression:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  
    :   The main idea behind ML-based compression is that structure is __automatically discovered__ instead of __manually engineered__.  
    :   * __Examples__: 
            * *__DjVu__*: employs segmentation and K-means clustering to separate foreground from background and analyze the documents contents.     

***

## WaveOne 
{: #content2}

[Further Reading](https://arxiv.org/pdf/1705.05823.pdf)

WaveOne is a machine learning-based approach to lossy image compression.  

1. **Main Idea:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    :   An ML-based approach to compression that utilizes the older techniques for quantization but with an encoder-decoder model that depends on adversarial training for a higher quality reconstruction.   

2. **Model:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}  
    :   The model includes three main steps that are layered together in one pipeline:  
        * __Feature Extraction__: an approach that aims to recognize the different types of structures in an image.  
            * __Structures__: 
                * Across input channels
                * Within individual scales
                * Across Scales
            * __Methods__: 
                * *__Pyramidal Decomposition__*: for analyzing individual scales 
                * *__Interscale Alignment Procedure__*:  for exploiting structure shared across scales   
        * __Code Computation and Regularization__: a module responsible for further compressing the extracted features by *quantizing the features and encoding them via two methods.  
            * __Methods__: 
                * *__Adaptive Arithmetic Coding Scheme__*: applied on the features binary expansions
                * *__Adaptive Codelength Regularization__*:  to penalize the entropy of the features to achieve better compression   
        * __Adversarial Training (Discriminator Loss)__: a module responsible for enforcing realistic reconstructions.
            * __Methods__: 
                * *__Adaptive Arithmetic Coding Scheme__*: applied on the features binary expansions
                * *__Adaptive Codelength Regularization__*:  to penalize the entropy of the features to achieve better compression   


3. **Feature Extraction:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}  
    :   * __Pyramidal Decomposition__:   
            Inspired by _the use of wavelets for multiresolution analysis, in which an input is analyzed recursively via feature extraction and downsampling operators_, the pyramidal decomposition encoder generalizes the wavelet decomposition idea to _learn optimal, nonlinear extractors individually for each scale_.  
            For each input $$\mathbf{x}$$ to the model, and a total of $$M$$ scales, denote the input to scale $$m$$ by $$\mathbf{x}_m$$.   
            * *__Algorithm__*:  
               * Set input to first scale $$\mathbf{x}_1 = \mathbf{x}$$
               * For each scale $$m$$:  
                    * Extract coefficients $$\mathbf{c}_m = \mathbf{f}_m(\mathbf{x}_m) \in \mathbb{R}^{C_m \times H_m \times W_m}$$ via some parametrized function $$\mathbf{f}_m(\dot)$$ for output channels $$C_m$$, height $$H_m$$ and width $$W_m$$  
                    * Compute the input to the next scale as $$\mathbf{x}_{m+1} = \mathbf{D}_m(\mathbf{x}_m)$$, where $$\mathbf{D}_m(\dot)$$ is some _downsampling operator_ (either fixed or learned)

            Typically, $$M$$ is chosen to be $$ = 6$$ scales.  
            The __feature extractors for the individual scales__ are composed of *__a sequence of convolutions with kernels $$3 \times 3$$ or $$1 \times 1$$ and ReLUs with a leak of $$0.2$$__*.  
            All _downsamplers_ are learned as $$4 \times 4$$ convolutions with a stride of $$2$$. 
    :   ![img](/main_files/cv/compression/1.png){: width="80%"}  
    :   * __Interscale Alignment__:   
            Designed to leverage information shared across different scales — a benefit not offered by the classic wavelet analysis.  
            * *__Structure__*:  
                * __Input__: the set of coefficients extracted from the different scales $$\{\mathbf{c}_m\}_{m=1}^M \subset \mathbb{R}^{C_m \times H_m \times W_m}$$     
                * __Output__: a tensor $$\mathbf{y} \in \mathbb{R}^{C \times H \times W}$$
            * *__Algorithm__*:  
                * Map each input tensor $$\mathbf{c}_m$$ to the target dimensionality via some parametrized function $$\mathbf{g}_m(·)$$:  this involves ensuring that this function spatially resamples $$\mathbf{c}_m$$ to the appropriate output map size $$H \times W$$, and ouputs the appropriate number of channels $$C$$  
                * Sum $$\mathbf{g}_m(\mathbf{c}_m) = 1, \ldots, M$$, and apply another parameterized non-linear transformation $$\mathbf{g}(·)$$ for _joint processing_  
        $$\mathbf{g}_m(·)$$ is chosen as a __convolution__ or a __deconvolution__ with an appropriate stride to produce the target spatial map size $$H \times W$$.  
        $$\mathbf{g}(·)$$ is choses as a __sequence of $$3 \times 3$$ convolutions__.  


4. **Code Computation and Regularization:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}  
    :   Given the output tensor $$\mathbf{y} \in \mathbb{R}^{C \times H \times W}$$ of the _feature extraction step_ (namely alignment), we proceed to __quantize and encode__ it.  
    :   * __Quantization__: the tensor $$\mathbf{y}$$ is quantized to bit precision $$B$$:    
            ![img](/main_files/cv/compression/2.png){: width="50%"}  
            Given a desired precision of $$B$$ bits, we quantize the feature tensor into $$2^B$$ equal-sized bins as:  
            ![img](/main_files/cv/compression/3.png){: width="80%"}  
            For the special case $$B = 1$$, this reduces exactly to a binary quantization scheme.  
            In-practice $$B = 6$$ is chosen as a smoother quantization method.  
            * __Reason__:   
                Mapping the _continuous input values_ representing the image signal to a _smaller countable set_ to achieve a desired precision of $$B$$ bits
    :   * __Bitplane Decomposition__: we transform the _quantized tensor_ $$\mathbf{\hat{y}}$$ into a _binary tensor_ suitable for encoding via a lossless bitplane decomposition:  
            ![img](/main_files/cv/compression/4.png){: width="80%"}  
            $$\mathbf{\hat{y}}$$ is decomposed into _bitplanes_ by a transformation that maps each value $$\hat{y}_{chw}$$ into its _binary expansion_ of $$B$$ bits.  
            Hence, each of the $$C$$ spatial maps $$\mathbf{\hat{y}}_c \in \mathbb{R}^{H \times W}$$ of $$\mathbf{\hat{y}}$$ expands into $$B$$ _binary bitplanes_.  

            * __Reason__:   
                This decomposition enables the entropy coder to exploit structure in the distribution of the activations in $$\mathbf{y}$$ to achieve a compact representation.  
    :   * __Adaptive Arithmetic Encoding__: encodes $$\mathbf{b}$$ into its final _variable-length binary sequence_ $$\mathbf{s}$$ of length $$\mathcal{l}(\mathbf{s})$$:  
            ![img](/main_files/cv/compression/5.png){: width="65%"}  
            * The _binary tensor_ $$\mathbf{b}$$ that is produced by the bitplane decomposition contains significant structure (e.g. higher bitplanes are sparser, and spatially neighboring bits often have the same value).  
                This structure can be exploited by using Adaptive Arithmetic Encoding.  
            * __Method__:  
                * *__Encoding__*:     
                    Associate each bit location in the _binary tensor_ $$\mathbf{b}$$ with a _context_, which comprises a set of features indicative of the bit value.  
                    The _features_ are based on the _position of the bit_ and the _values of neighboring bits.  
                    To predict the value of each bit from its context features, we _train a classifier_ and use _its output probabilities_ to compress $$\mathbf{b}$$ via _arithmetic coding_.   
                * *__Decoding__*:    
                    At decoding time, we perform the _inverse operation_ to _decompress the code_.  
                    We interleave between:  
                    * Computing the context of a particular bit using the values of previously decoded bits  
                    * Using this context to retrieve the activation probability of the bit and decode it  
                    > This operation constrains the context of each bit to only include features composed of bits already decoded   
            * __Reason__:   
                We aim to leverage the structure in the data, specifically in the _binary tensor_ $$\mathbf{b}$$ produced by the _bitplane decomposition_ which has _low entropy_ 
    :   * __Adaptive Codelength Regularization__: modulates the distribution of the quantized representation $$\mathbf{\hat{y}}$$ to achieve a target expected bit count across inputs:  
            ![img](/main_files/cv/compression/6.png){: width="60%"}  
            * __Goal__: regulate the expected codelength $$\mathbb{E}_x[\mathcal{l}(\mathbf{s})]$$ to a target value $$\mathcal{l}_{\text{target}}$$.
            * __Method__:  
                We design a penalty that encourages a structure that the __AAC__ is able to encode.  
                Namely, we *__regularize__* the _quantized tensor_ $$\mathbf{\hat{y}}$$ with:  
                ![img](/main_files/cv/compression/7.png){: width="60%"}  
                for iteration $$t$$ and difference index set $$S = \{(0,1), (1,0), (1,1), (-1,1)\}$$.  
                > The __first term__ _penalizes the magnitude of each tensor element_  
                > The __Second Term__ _penalizes deviations between spatial neighbors_  

            * __Reason__:   
                The _Adaptive Codelength Regularization_ is designed to solve one problem; the non-variability of the latent space code, which is what controls (defines) the bitrate.  
                It, essentially, allows us to have latent-space codes with different lengths, depending on the complexity of the input, *by enabling better prediction by the __AAX__*  
            In practice, a __total-to-target ratio__ $$ = BCHW/\mathcal{l}_{\text{target}} = 4$$ works well.  

5. **Adversarial Train:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}  
    :   * __GAN Architecture__:   
            * *__Generator__*: Encoder-Decoder Pipeline  
            * *__Discriminator__*: Classification ConvNet 
    :   * __Discriminator Design__:  




7. **Architecture:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents27}  
    :   * __Problem__: Regression Problem
        * __Goal__: Learn a function $$\psi(x;\theta)$$ that is trained and used to regress to a pose vector.   
        * __Estimation__: $$\psi$$ is based on (learned through) Deep Neural Net
        * __Deep Neural Net__: is a Convolutional Neural Network; namely, __AlexNet__  
            * *__Input__*: image with pre-defined size $$ = \:$$ #-pixels $$\times 3$$-color channels  
                > $$(220 \times 220)$$ with a stride of $$4$$  
            * *__Output__*: target value of the regression$$ = 2k$$ joint coordinates  
    :   > Denote by $$\mathbf{C}$$ a convolutional layer, by $$\mathbf{LRN}$$ a local response normalization layer, $$\mathbf{P}$$ a pooling layer and by $$\mathbf{F}$$ a fully connected layer  
    :   > For $$\mathbf{C}$$ layers, the size is defined as width $$\times$$ height $$\times$$ depth, where the first two dimensions have a spatial meaning while the depth defines the number of filters.  
    :   * __Alex-Net__: 
            * *__Architecture__*:     $$\mathbf{C}(55 \times 55 \times 96) − \mathbf{LRN} − \mathbf{P} − \mathbf{C}(27 \times 27 \times 256) − \mathbf{LRN} − \mathbf{P} − \\\mathbf{C}(13 \times 13 \times 384) − \mathbf{C}(13 \times 13 \times 384) − \mathbf{C}(13 \times 13 \times 256) − \mathbf{P} − \mathbf{F}(4096) − \mathbf{F}(4096)$$   
            * *__Filters__*:  
                * $$\mathbf{C}_{1} = 11 \times 11$$,  
                * $$\mathbf{C}_{2} = 5 \times 5$$,  
                * $$\mathbf{C}_{3-5} = 3 \times 3$$.
            * *__Total Number of Parameters__* $$ = 40$$M   
            * *__Training Dataset__*:  
                Denote by $$D$$ the training set and $$D_N$$ the normalized training set:   
                $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$ $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$  $$D_N = \{(N(x),N(\mathbf{y}))\vert (x,\mathbf{y}) \in D\}$$   
            * *__Loss__*: the Loss is modified; instead of a _classification loss_, we train a linear regression on top of the last network layer to predict a pose vector by minimizing $$L_2$$ distance between the prediction and the true pose vector,  
    :   $$\arg \min_\theta \sum_{(x,y) \in D_N} \sum_{i=1}^k \|\mathbf{y}_i - \psi_i(x;\theta)\|_2^2$$  
    :   * __Optimization__:  
            * *__BackPropagation__* in a distributed online implementation
            * *__Adaptive Gradient Updates__*
            * *__Learning Rate__* $$ = 0.0005 = 5\times 10^{-4}$$
            * *__Data Augmentation__*: randomly translated image crops, left/right flips
            * *__DropOut Regularization__* for the $$\mathbf{F}$$ layers $$ = 0.6$$

9. **Architecture:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents29}  
    :   * __Motivation__:   
            Although, the pose formulation of the DNN has the advantage that the joint estimation is based on the full image and thus relies on context, due its fixed input size of $$220 \times 220$$, the network has _limited capacity to look at detail_ - it _learns filters capturing pose properties at coarse scale_.  
            The _pose properties_ are necessary to _estimate rough pose_ but __insufficient__ to always _precisely localize the body joints_.  
            Increasing the input size is infeasible since it will increase the already large number of parameters.  
            Thus, a _cascade of pose regressors_ is used to achieve better precision.  
        * __Structure and Training__:   
            At the first stage: 
            * The cascade starts off by estimating an initial pose as outlined in the previous section.  
            At subsequent stages:  
            * Additional DNN regressors are trained to predict a displacement of the joint locations from previous stage to the true location.  
                > Thus, each subsequent stage can be thought of as a refinement of the currently predicted pose.   
            * Each subsequent stage uses the predicted joint locations to focus on the relevant parts of the image – subimages are cropped around the predicted joint location from previous stage and the pose displacement regressor for this joint is applied on this sub-image.  
                > Thus, subsequent pose regressors see higher resolution images and thus learn features for finer scales which ultimately leads to higher precision  
        * __Method and Architecture__:  
            * The same network architecture is used for all stages of the cascade but learn different parameters.   
            * Start with a bounding box $$b^0$$: which either encloses the full image or is obtained by a person detector
            * Obtain an initial pose:  
                Stage 1: $$\mathbf{y}^1 \leftarrow N^{-1}(\psi(N(x;b^0);\theta_1);b^0)$$  
            * At stages $$s \geq 2$$, for all joints:
                * Regress first towards a refinement displacement $$\mathbf{y}_i^s - \mathbf{y}_i^{(s-1)}$$ by applying a regressor on the sub image defined by $$b_i^{(s-1)}$$ 
                * Estimate new joint boxes $$b_i^s$$:  
                Stage $$s$$: $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \mathbf{y}_i^s \leftarrow \mathbf{y}_i^{(2-1)} + N^{-1}(\psi(N(x;b^0);\theta_s);b)  \:\: (6)  \\
 \ \ \ \ \ \ \ \ \ \ \ \ \ \                  \:\:\:\: \text{for } b = b_i^(s-1) \\
  \ \ \ \ \ \ \ \ \ \ \ \ \ \ 
                b_i^s \leftarrow (\mathbf{y}_i^s, \sigma diam(\mathbf{y}^s), \sigma diam(\mathbf{y}^s))) \:\: (7)$$  
                where we considered a joint bounding box $$b_i$$ capturing the sub-image around $$\mathbf{y}_i: b_i(\mathbf{y}; \sigma) = (\mathbf{y}_i, \sigma diam(\mathbf{y}), \sigma diam(\mathbf{y}))$$ having as center the i-th joint and as dimension the pose diameter scaled by $$\sigma$$, to refine a given joint location $$\mathbf{y}_i$$.    
            * Apply the cascade for a fixed number of stages $$ = S$$  
        * __Loss__: (at each stage $$s$$)   
    :  $$\theta_s = \arg \min_\theta \sum_{(x,\mathbf{y}_i) \in D_A^s} \|\mathbf{y}_i - \psi_i(x;\theta)\|_2^2 \:\:\:\:\: (8)$$


6. **Advantages:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents26}  
    :   * The DNN is capable of capturing the full context of each body joint  
        * The approach is simpler to formulate than graphical-models methods - no need to explicitly design feature representations and detectors for parts or to explicitly design a model topology and interactions between joints.   
            > Instead a generic ConvNet learns these representations

8. **Notes:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents28}  
    :   * The use of a generic DNN architecture is motivated by its outstanding results on both classification and localization problems and translates well to pose estimation  
        * Such a model is a truly holistic one — the final joint location estimate is based on a complex nonlinear transformation of the full image  
        * The use of a DNN obviates the need to design a domain specific pose model
        * Although the regression loss does not model explicit interactions between joints, such are implicitly captured by all of the 7 hidden layers – all the internal features are shared by all joint regressors  

***

## Proposed Changes
{: #content3}

1. **Gated-Matrix Selection for Latent Space dimensionality estimation and Dynamic bit-rate modification:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}  
    :   


2. **Conditional Generative-Adversarial Training with Random-Forests for Generalizable domain-compression:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}  
    :   


3. **Adversarial Feature Learning for Induced Natural Representation and Artifact Removal:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}  
    :   


***

__Papers:__  
* __Generative Compression__
    * WaveOne: https://arxiv.org/pdf/1705.05823.pdf
    * MIT Generative Compression: https://arxiv.org/pdf/1703.01467.pdf

* __Current Standards__
    * An overview of the JPEG2000 still image compression standard
        * Paper:http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.128.9040&rep=rep1&type=pdf
        * Notes: Pretty in-depth, by Eastman Kodak Company, from early 2000s (maybe improvements since then?)

1. WaveOne
    Paper: https://arxiv.org/pdf/1705.05823.pdf
    Site: http://www.wave.one/
    Post: http://www.wave.one/icml2017
2. Generative Compression -- Santurker, Budden, Shavit (MIT)
    Paper: https://arxiv.org/pdf/1703.01467.pdf
3. Toward Conceptual Compression -- DeepMind
    Paper: https://papers.nips.cc/paper/6542-towards-conceptual-compression.pdf


* Generative Compression:  
    Generative Compression (https://arxiv.org/pdf/1703.01467.pdf and http://www.wave.one/icml2017/ ), think about streaming videos with orders of magnitude better compression. The results are pretty insane, and this could possibly be the key to bringing AR/VR into the everyday market. If we can figure out how to integrate this into real-time systems, like lets say a phone, you could take hidef video, buffer it and encode it to compress it (the above waveone model can compress 100 img/sec from the Kodak dataset -- not shabby at all), we could save massive amounts of data with order of magnitude less storage. We could easily create a mobile app as a proof of concept, but this shit could be huge. These can be also trained to be domain specific, because they are learned not hardcoded. We could create an API allowing any device to connect to it and dynamically compress data, think drones, etc. We can also build in encryption into the system, which adds a layer of security.


