---
layout: NotesPage
title: Generative Adversarial Networks
permalink: /work_files/research/dl/archits/gans
prevLink: /work_files/research/dl/cv.html
---

<div markdown="1" class = "TOC">
# Table of Contents
  * [Generative Adversarial Networks (GANs)](#content1)
  {: .TOC1}
</div>

***
***

* [Generative Adversarial Networks (CS236 pdf)](https://deepgenerativemodels.github.io/notes/gan/)  
* [GANs (Goodfellow)](https://www.youtube.com/watch?v=AJVyzd0rqdc)  
* [GANs (tutorial lectures)](https://sites.google.com/view/cvpr2018tutorialongans/)  
* [GAN ZOO (Blog)](https://github.com/hindupuravinash/the-gan-zoo)  


## Generative Adversarial Networks (GANs)
{: #content1}

0. **Auto-Regressive Models VS Variational Auto-Encoders VS GANs:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents10}  
    __Auto-Regressive Models__ defined a *__tractable__* (discrete) density function and, then, optimized the likelihood of training data:   
    <p>$$p_\theta(x) = p(x_0) \prod_1^n p(x_i | x_{i<})$$  </p>  
    
    While __VAEs__ defined an *__intractable__* (continuous) density function with latent variable $$z$$:  
    <p>$$p_\theta(x) = \int p_\theta(z) p_\theta(x|z) dz$$</p>  
    but cannot optimize directly; instead, derive and optimize a lower bound on likelihood instead.  
    
    On the other hand, __GANs__ rejects explicitly defining a probability density function, in favor of only being able to sample.     
    <br>

1. **Generative Adversarial Networks:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    __GANs__ are a class of AI algorithms used in unsupervised machine learning, implemented by a system of two neural networks contesting with each other in a zero-sum game framework.  
    <br>

2. **Motivation:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    * __Problem__: we want to sample from complex, high-dimensional training distribution; there is no direct way of doing this.  
    * __Solution__: we sample from a simple distribution (e.g. random noise) and learn a transformation that maps to the training distribution, by using a __neural network__.  

    ![img](https://cdn.mathpix.com/snip/images/28l-qxaMy4eTm9gBce5VKfd4K98boqFs0eNOTCkMnog.original.fullsize.png){: width="40%"}  


    * __Generative VS Discriminative__: discriminative models had much more success because deep generative models suffered due to the difficulty of approximating many intractable probabilistic computations that arise in maximum likelihood estimation and related strategies, and due to difficulty of leveraging the benefits of piecewise linear units in the generative context.  
        GANs propose a new framework for generative model estimation that sidesteps these difficulties.      
    <br>

3. **Structure:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    * __Goal__:  
        estimating generative models that capture the training data distribution  
    * __Framework__:  
        an adversarial process in which two models are simultaneously trained a generative model $$G$$ that captures the data distribution, and a discriminative model $$D$$ that estimates the probability that a sample came from the training data rather than $$G$$.  
    * __Training__:  
        $$G$$ maximizes the probability of $$D$$ making a mistake       

4. **Training:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    __Generator network:__ try to fool the discriminator by generating real-looking images  
    __Discriminator network:__ try to distinguish between real and fake images  
    ![img](https://cdn.mathpix.com/snip/images/12HQ0mKEIlrX4e2EanOSjUhjgdTpW6nV2gyn8G7-s0A.original.fullsize.png){: width="67%"}  

    * Train __jointly__ in __minimax game__.  
        * Minimax objective function:  
            <p>$$\min _{\theta_{g}} \max _{\theta_{d}}\left[\mathbb{E}_{x \sim p_{\text {data }}} \log D_{\theta_{d}}(x)+\mathbb{E}_{z \sim p(z)} \log \left(1-D_{\theta_{d}}\left(G_{\theta_{g}}(z)\right)\right)\right]$$</p>  
            \- Discriminator outputs likelihood in $$(0,1)$$ of real image  
            \- $$D_{\theta_{d}}(x)$$: Discriminator output for real data $$\boldsymbol{x}$$  
            \- $$D_{\theta_{d}}\left(G_{\theta_{g}}(z)\right)$$: Discriminator output for generated fake data $$G(z)$$  
            \- Discriminator $$\left(\theta_{d}\right)$$ wants to maximize objective such that $$\mathrm{D}(\mathrm{x})$$ is close to $$1$$ (real) and $$\mathrm{D}(\mathrm{G}(\mathrm{z}))$$ is close to $$0$$ (fake)  
            \- Generator $$\left(\mathrm{f}_ {\mathrm{g}}\right)$$ "wants to minimize objective such that $$\mathrm{D}(\mathrm{G}(\mathrm{z}))$$ is close to $$1$$ (discriminator is fooled into thinking generated $$\mathrm{G}(\mathrm{z})$$ is real)  
    * Alternate between\*:  
        1. __Gradient Ascent__ on Discriminator:  
            <p>$$\max _{\theta_{d}}\left[\mathbb{E}_{x \sim p_{\text {data}}} \log D_{\theta_{d}}(x)+\mathbb{E}_{z \sim p(z)} \log \left(1-D_{\theta_{d}}\left(G_{\theta_{g}}(z)\right)\right)\right]$$</p>  
        2. __Gradient Ascent__ on Generator (different objective):  
            <p>$$\max _{\theta_{g}} \mathbb{E}_{z \sim p(z)} \log \left(D_{\theta_{d}}\left(G_{\theta_{g}}(z)\right)\right)$$</p>  

    __GAN Training Algorithm:__{: style="color: red"}  
    <button>Algorithm</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/vJzBJcFh5ASuKowEV6B5OMklS-PPNIgqvnnDclMMu3g.original.fullsize.png){: width="100%" hidden=""}  
    \- __\# of Training steps $$\mathrm{k}$$:__ some find $$\mathrm{k}=1$$ more stable, others use $$\mathrm{k}>1$$ no best rule.  
    {: #lst-p}
    * Recent work (e.g. Wasserstein GAN) alleviates this problem, better stability!  


    ![img](https://cdn.mathpix.com/snip/images/nFIqQ5afG4h-GIcPQSbOwUxro5zj55HY9rAOf_f3C_Q.original.fullsize.png){: width="67%"}  


    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * \* Instead of minimizing likelihood of discriminator being correct, now maximize likelihood of discriminator being wrong. Same objective of fooling discriminator, but now higher gradient signal for bad samples => works much better! Standard in practice.  
        * Previously we used to do gradient __descent__ on generator:  
            <p>$$\min _{\theta_{g}} \mathbb{E}_{z \sim p(z)} \log \left(1-D_{\theta_{d}}\left(G_{\theta_{g}}(z)\right)\right)$$</p>  
            In practice, optimizing this generator objective does not work well.  
            ![img](/main_files/cs231n/gans/2.png){: width="40%"}  
        * Now we are doing gradient *__ascent__* on the generator:  
            <p>$$\max _{\theta_{g}} \mathbb{E}_{z \sim p(z)} \log \left(D_{\theta_{d}}\left(G_{\theta_{g}}(z)\right)\right)$$</p>  
            ![img](/main_files/cs231n/gans/1.png){: width="40%"}  
    * Jointly training two networks is challenging, can be unstable. Choosing objectives with better loss landscapes helps training, is an active area of research.  
    * __The representations have nice structure:__  
        * Average $$\boldsymbol{z}$$ vectors, do arithmetic:  
            ![img](https://cdn.mathpix.com/snip/images/iNB2WF_B-fA6AUeNPkqjaPCQRzCi1iEp9O7AmNsNGX0.original.fullsize.png){: width="40%"}  
            <button>Glasses</button>{: .showText value="show" onclick="showTextPopHide(event);"}
            ![img](https://cdn.mathpix.com/snip/images/It81yGTPcd7AtoxXUL6zmFRv475nN_ryCP8EL2SsPUs.original.fullsize.png){: width="60%" hidden=""}  
        * Interpolating between random points in latent space is possible  
    <br>

5. **Generative Adversarial Nets: Convolutional Architectures:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  
    \- __Discriminator__ is a standard __convolutional network__.  
    \- __Generator__ is an __upsampling network__ with __fractionally-strided convolutions__.  
    ![img](https://cdn.mathpix.com/snip/images/sPjqzCuh41DM_xCX9RYshgKPi1TDZsFpZxELmngXn9g.original.fullsize.png){: width="40%"}  

    __Architecture guidelines for stable Deep Convolutional GANs:__{: style="color: red"}  
    {: #lst-p}
    * Replace any pooling layers with strided convolutions (discriminator) and fractional-strided convolutions (generator).
    * Use batchnorm in both the generator and the discriminator.
    * Remove fully connected hidden layers for deeper architectures.
    * Use ReLU activation in generator for all layers except for the output, which uses Tanh.
    * Use LeakyReLU activation in the discriminator for all layers.  
    <br>

6. **Pros, Cons and Research:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents46}  
    * __Pros__:  
        * Beautiful, state-of-the-art samples!  
    * __Cons__:  
        * Trickier / more unstable to train
        * Can’t solve inference queries such as $$p(x), p(z\vert x)$$  
    * __Active areas of research:__  
        * Better loss functions, more stable training (Wasserstein GAN, LSGAN, many others)
        * Conditional GANs, GANs for all kinds of applications


__Notes:__{: style="color: red"}  
{: #lst-p}
* **Generative Adversarial Network (GAN).** This has been one of the most popular models (research-wise) in recent years ([Goodfellow et al., 2014](https://arxiv.org/abs/1406.2661)). This OpenAI [blogpost](https://blog.openai.com/generative-models/) gives a good overview of a few architectures based on the GAN (although only from OpenAI). Other interesting models include pix2pix ([Isola et al., 2017](https://arxiv.org/abs/1611.07004)), CycleGAN ([Zhu et al., 2017](https://arxiv.org/abs/1703.10593)) and WGAN ([Arjovsky et al., 2017](https://arxiv.org/abs/1701.07875)). The first two deal with image-to-image translation (eg. photograph to Monet/Van Gogh or summer photo to winter photo), while the last work focuses on using Wasserstein distance as a metric for stabilizing the GAN (since GANs are known to be unstable and difficult to train).  
* __Limitation of GANs__:  
    * [A Classification–Based Study of Covariate Shift in GAN Distributions (paper)](https://arxiv.org/pdf/1711.00970.pdf)  
    * [On the Limitations of First-Order Approximation in GAN Dynamics (paper)](https://arxiv.org/pdf/1706.09884.pdf)  
    * [Limitations of Encoder-Decoder GAN architectures (4) (Blog+Paper!)](http://www.offconvex.org/2018/03/12/bigan/)  
    * [Do GANs actually do distribution learning? (3) (Blog+Paper!)](http://www.offconvex.org/2017/07/06/GANs3/)  
    * [Generative Adversarial Networks (2), Some Open Questions (Blog+Paper)](http://www.offconvex.org/2017/03/15/GANs/)  
    * [Generalization and Equilibrium in Generative Adversarial Networks (1) (Blog+Papers)](http://www.offconvex.org/2017/03/30/GANs2/)  
    * [GANs are Broken in More than One Way: The Numerics of GANs (Blog!)](inference.vc/my-notes-on-the-numerics-of-gans/)  
* __Cool GAN papers__:  
    Cycle-GAN, BigGAN, PGGAN, WGAN-GP, StyleGAN, SGAN, 
* [GAN discussion usefulness and applications (twitter)](https://twitter.com/fhuszar/status/1046469743480373248)  
<br>