---
layout: NotesPage
title: CNN Architectures
permalink: /work_files/research/dl/arcts
prevLink: /work_files/research/dl/cv.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [AlexNet](#content1)
  {: .TOC1}
  * [VGG16](#content2)
  {: .TOC2}
  * [GoogLeNet](#content3)
  {: .TOC3}
  * [ResNet](#content4)
  {: .TOC4}
  * [Comparisons](#content5)
  {: .TOC5}
  * [Interesting Architectures](#content6)
  {: .TOC6}
</div>

***
***

*__LeNet-5__*: _(LeCun et al., 1998)_  
![img](/main_files/cs231n/9/1.png){: width="70%"}  
* __Architecture__: [CONV-POOL-CONV-POOL-FC-FC]  
* __Parameters__: 
    * CONV: F=5, S=1
    * POOL: F=2, S=2

## AlexNet _(Krizhevsky et al. 2012)_
{: #content1}

![img](/main_files/cs231n/9/2.png){: width="70%"}  

1. **Architecture:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    :   [CONV1-MAX-POOL1-NORM1-CONV2-MAX-POOL2-NORM2-CONV3-CONV4-CONV5-Max-POOL3-FC6-FC7-FC8]  

2. **Parameters:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    :   * __First Layer (CONV1)__: 
            * __F__: second     
    :   ![img](/main_files/cs231n/9/3.png){: width="50%"}  

3. **Key Insights:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    :   * first use of ReLU
        * used Norm layers (not common anymore)
        * heavy data augmentation
        * dropout 0.5
        * batch size 128
        * SGD Momentum 0.9
        * Learning rate 1e-2, reduced by 10
        manually when val accuracy plateaus
        * L2 weight decay 5e-4
        * 7 CNN ensemble: 18.2% -> 15.4%

4. **Results:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    :   ![img](/main_files/cs231n/9/4.png){: width="70%"}  

5. **ZFNet _(Zeiler and Fergus, 2013)_:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  
    :   ![img](/main_files/cs231n/9/5.png){: width="70%"}
    :   ![img](/main_files/cs231n/9/6.png){: width="70%"}

***

## VGGNet _(Simonyan and Zisserman, 2014)_
{: #content2}

![img](/main_files/cs231n/9/7.png){: width="60%"}  

2. **Parameters:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}  
    :   * __CONV__: F=1, S=1, P=1
        * __POOL__: F=2, S=2  
        > For all layers   
    :   ![img](/main_files/cs231n/9/8.png){: width="80%"}  
    :   > Notice:  
            __Parameters__ are mostly in the *__FC Layers__*  
            __Memory__ mostly in the *__CONV Layers__*

3. **Key Insights:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}  
    :   * Smaller Filters
        * Deeper Networks  
        * Similar Training as AlexNet
        * No LRN Layer
        * Both __VGG16__ and __VGG19__
        * Uses Ensembles for Best Results

4. **Smaller Filters Justification:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}  
    :   * A Stack of three 3x3 conv (stride 1) layers has same effective receptive field as one 7x7 conv layer  
        * However, now, we have deeper nets and more non-linearities
        * Also, fewer parameters:  
            3 * (3^2*C^2 ) vs. 7^2*C^2 for C channels per layer

5. **Properties:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}  
    :   * __FC7__ Features *__generalize__* well to other tasks

6. **VGG16 vs VGG19:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents26}  
    :   __VGG19__ is only slightly better and uses _more memory_ 

7. **Results:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents27}  
    :   ILSVRC’14 2nd in classification, 1st in localization  
    :   ![img](/main_files/cs231n/9/9.png){: width="70%"}  

***

## GoogLeNet _(Szegedy et al., 2014)_
{: #content3}

![img](/main_files/cs231n/9/13.png){: width="80%"}  

1. **Architecture:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}  
    :   ![img](/main_files/cs231n/9/14.png){: width="85%"}  

2. **Parameters:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}  
    :   Parameters as specified in the Architecture and the Inception Modules

3. **Key Insights:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}  
    :   * (Even) Deeper Networks
        * Computationally Efficient
        * 22 layers
        * Efficient “Inception” module
        * No FC layers
        * Only 5 million parameters: 12x less than AlexNet

4. **Inception Module:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents34}  
    :   * __Idea__: design a good local network topology (network within a network) and then stack these modules on top of each other   
    :   ![img](/main_files/cs231n/9/10.png){: width="50%"}
    :   * __Architecture__:  
            * Apply _parallel filter operations_ on the input from previous layer:  
                * Multiple receptive field sizes for convolution (1x1, 3x3, 5x5)   
                * Pooling operation (3x3)  
            * Concatenate all filter outputs together depth-wise  
    :   * __Issue__: *__Computational Complexity__* is very high  
        ![img](/main_files/cs231n/9/12.png){: width="70%"}  
        * __Solution__: use *__BottleNeck Layers__* that use 1x1 convolutions to reduce feature depth   
            > preserves spatial dimensions, reduces depth!
    :   ![img](/main_files/cs231n/9/11.png){: width="50%"}  

7. **Results:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents37}  
    :   ILSVRC’14 classification winner 
    :   ![img](/main_files/cs231n/9/9.png){: width="70%"}

***

## ResNet _(He et al., 2015)_
{: #content4}

* [Residual Blocks (Blog)](https://towardsdatascience.com/residual-blocks-building-blocks-of-resnet-fd90ca15d6ec)  

1. **Architecture:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents41}  
    :   ![img](/main_files/cs231n/9/17.png){: width="85%"}

3. **Key Insights:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents43}  
    :   * Very Deep Network: 152-layers
        * Uses Residual Connections
        * Deep Networks have very bad performance __NOT__ because of overfitting but because of a lack of adequate optimization  

4. **Motivation:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents44}  
    :   ![img](/main_files/cs231n/9/15.png){: width="70%"}  
    :   * __Observation__: Deeper Networks perform badly on the test error *__but also on the training error__*  
        * __Assumption__: Deep Layers should be able to perform at least as well as the shallower models   
        * __Hypothesis__: the problem is an optimization problem, deeper models are harder to optimize  
        * __Solution (work-around)__: Use network layers to fit a residual mapping instead of directly trying to fit a desired underlying mapping   

5. **Residuals:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents45}  
    :   ![img](/main_files/cs231n/9/16.png){: width="70%"}

6. **BottleNecks:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents46}  
    :   ![img](/main_files/cs231n/9/18.png){: width="70%"}

7. **Training:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents47}  
:      * Batch Normalization after every CONV layer
        * Xavier/2 initialization from He et al.
        * SGD + Momentum (0.9)
        * Learning rate: 0.1, divided by 10 when validation error plateaus
        * Mini-batch size 256
        * Weight decay of 1e-5
        * No dropout used

8. **Results:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents48}  
    :   * ILSVRC’15 classification winner (3.57% top 5 error)  
        * Swept all classification and detection competitions in ILSVRC’15 and COCO’15  
        * Able to train very deep networks without degrading (152 layers on ImageNet, 1202 on Cifar)
        * Deeper networks now achieve lowing training error as expected
    :   ![img](/main_files/cs231n/9/19.png){: width="60%"}
    :   ![img](/main_files/cs231n/9/20.png){: width="64%"}

***

## Comparisons
{: #content5}

1. **Complexity:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents51}
    :   ![img](/main_files/cs231n/9/21.png){: width="70%"}
    :   ![img](/main_files/cs231n/9/22.png){: width="70%"}

2. **Forward-Pass Time and Power Consumption:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents52}  
    :   ![img](/main_files/cs231n/9/23.png){: width="70%"}
    :   ![img](/main_files/cs231n/9/24.png){: width="70%"}


*** 

## Interesting Architectures
{: #content6}

1. **Network in Network (NiN) _[Lin et al. 2014]_:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents61}  
    :   * Mlpconv layer with “micronetwork” within each conv layer to compute more abstract features for local patches
        * Micronetwork uses multilayer perceptron (FC, i.e. 1x1 conv layers)
        * Precursor to GoogLeNet and ResNet “bottleneck” layers
        * Philosophical inspiration for GoogLeNet  
    :   ![img](/main_files/cs231n/9/25.png){: width="70%"}

2. **Identity Mappings in Deep Residual Networks (Improved ResNets) _[He et al. 2016]_:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents62}  
    :   * Improved ResNet block design from creators of ResNet
        * Creates a more direct path for propagating information throughout network (moves activation to residual mapping pathway)
        * Gives better performance
    :   ![img](/main_files/cs231n/9/26.png){: width="40%"}

3. **Wide Residual Networks (Improved ResNets) _[Zagoruyko et al. 2016]_:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents63}  
    :   * Argues that residuals are the important factor, not depth
        * User wider residual blocks (F x k filters instead of F filters in each layer)
        * 50-layer wide ResNet outperforms 152-layer original ResNet
        * Increasing width instead of depth more computationally efficient (parallelizable)
    :   ![img](/main_files/cs231n/9/27.png){: width="50%"}

4. **Aggregated Residual Transformations for Deep Neural Networks (ResNeXt) _[Xie et al. 2016]_:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents64}  
    :   * Also from creators of ResNet
        * Increases width of residual block through multiple parallel pathways (“cardinality”)
        * Parallel pathways similar in spirit to Inception module
    :   ![img](/main_files/cs231n/9/28.png){: width="60%"}

5. **Deep Networks with Stochastic Depth (Improved ResNets) _[Huang et al. 2016]_:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents65}  
    :   * Motivation: reduce vanishing gradients and training time through short networks during training
        * Randomly drop a subset of layers during each training pass
        * Bypass with identity function
        * Use full deep network at test time
    :   ![img](/main_files/cs231n/9/29.png){: width="30%"}

#### Beyond ResNets

6. **FractalNet: Ultra-Deep Neural Networks without Residuals _[Larsson et al. 2017]_:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents66}  
    :   * Argues that key is transitioning effectively from shallow to deep and residual representations are not necessary
        * Fractal architecture with both shallow and deep paths to output
        * Trained with dropping out sub-paths 
        * Full network at test time
    :   ![img](/main_files/cs231n/9/30.png){: width="70%"}

7. **Densely Connected Convolutional Networks _[Huang et al. 2017]_:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents67}  
    :   * Dense blocks where each layer is connected to every other layer in feedforward fashion
        * Alleviates vanishing gradient, strengthens feature propagation, encourages feature reuse
    ;   ![img](/main_files/cs231n/9/31.png){: width="65%"}

8. **SqueezeNet (Efficient NetWork) _[Iandola et al. 2017]_:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents68}  
    :   *  AlexNet-level Accuracy With 50x Fewer Parameters and <0.5Mb Model Size
        * Fire modules consisting of a ‘squeeze’ layer with 1x1 filters feeding an ‘expand’ layer with 1x1 and 3x3 filters
        * Can compress to 510x smaller than AlexNet (0.5Mb)
    :   ![img](/main_files/cs231n/9/32.png){: width="60%"}
