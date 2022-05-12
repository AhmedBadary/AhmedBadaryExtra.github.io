---
layout: NotesPage
title: Image Segmentation <br /> with Deep Learning
permalink: /work_files/research/dl/seg
prevLink: /work_files/research/dl/cv.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Semantic Segmentation](#content1)
  {: .TOC1}
  * [Approaches (The Pre-DeepLearning Era)](#content2)
  {: .TOC2}
  * [Approaches (The Deep Learning Era)](#content3)
  {: .TOC3}
  * [Methods, Approaches and Algorithms in Training DL Models](#content4)
  {: .TOC4}
</div>

***
***

## Semantic Segmentation
{: #content1}

1. **Semantic Segmentation:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    :   __Semantic Segmentation__ is the task of understanding an image at the pixel level. It seeks to assign an object class to each pixel in the image.  
    :   ![img](/main_files/cs231n/11/1.png){: width="20%"}


2. **The Structure:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    :   * __Input__: Image  
        * __Output__: A class for each pixel in the image.  

3. **Properties:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    :   In Semantic Segmentation, we don't differentiate among the instances, instead, we only care about the pixels.
    :   ![img](/main_files/cs231n/11/2.png){: width="40%"}  

***

## Approaches (The Pre-DeepLearning Era)
{: #content2}

1. **Semantic Texton Forests:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    :   This approach consists of ensembles of decision trees that act directly on image pixels.  
    :   Semantic Texton Forests (STFs) 
are randomized decision forests that use only simple pixel comparisons on local image patches, performing both an
implicit hierarchical clustering into semantic textons and an explicit local classification of the patch category.  
    :   STFs allow us to build powerful texton codebooks without computing expensive filter-banks or descriptors, and without performing costly k-means clustering and nearest-neighbor assignment.
    :   _Semantic Texton Forests for Image Categorization and Segmentation, Shawton et al. (2008)_

2. **Random Forest-based Classifiers:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}  
    :   Random Forests have also been used to perform semantic segmentation for a variety of tasks.

3. **Conditional Random Fields:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}  
    :   CRFs provide a probabilistic framework for labeling and segmenting structured data.  
    :   They try to model the relationship between pixels, e.g.:
        1. nearby pixels more likely to have same label
        2. pixels with similar color more likely to have same label
        3. the pixels above the pixels "chair" more likely to be "person" instead of "plane"
        4. refine results by iterations
    :   _W. Wu, A. Y. C. Chen, L. Zhao and J. J. Corso (2014): "Brain Tumor detection and segmentation in a CRF framework with pixel-pairwise affinity and super pixel-level features"_
    :   _Plath et al. (2009): "Multi-class image segmentation using conditional random fields and global classification"_

4. **SuperPixel Segmentation:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}  
    :   The concept of superpixels was first introduced by Xiaofeng Ren and Jitendra Malik in 2003.  
    :   __Superpixel__ is a group of connected pixels with similar colors or gray levels.  
        They produce an image patch which is better aligned with intensity edges than a rectangular patch.  
    :   __Superpixel segmentation__ is the idea of dividing an image into hundreds of non-overlapping superpixels.  
        Then, these can be fed into a segmentation algorithm, such as __Conditional Random Fields__ or __Graph Cuts__, for the purpose of segmentation.  
    :   _Efficient graph-based image segmentation, Felzenszwalb, P.F. and Huttenlocher, D.P. International Journal of Computer Vision, 2004_
    :   _Quick shift and kernel methods for mode seeking, Vedaldi, A. and Soatto, S. European Conference on Computer Vision, 2008_
    :   _Peer Neubert & Peter Protzel (2014). Compact Watershed and Preemptive_  

***

## Approaches (The Deep Learning Era)
{: #content3}

1. **The Sliding Window Approach:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}  
    :   We utilize _classification_ for _segmentation_ purposes.  
    :   * __Algorithm__:    
            * We break up the input image into tiny "crops" of the input image.  
            * Use Classification to find the class of the center pixel of the crop.  
                > Using the same machinery for classification.
    :   Basically, we do classification on each crop of the image.
    :   * __DrawBacks:__  
            * Very Inefficient and Expensive:  
                To label every pixel in the image, we need a separate "crop" for each pixel in the image, which would be quite a huge number.  
            * Disregarding Localized Information:  
                This approach does __not__ make use of the shared features between overlapping patches in the image.  
                Further, it does not make use of the spatial information between the pixels.  
    :   _Farabet et al, “Learning Hierarchical Features for Scene Labeling,” TPAMI 2013_
    :   _Pinheiro and Collobert, “Recurrent Convolutional Neural Networks for Scene Labeling”, ICML 2014_

2. **Fully Convolutional Networks:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}  
    :   We make use of convolutional networks by themselves, trained end-to-end, pixels-to-pixels.  
    :   * __Structure__:  
            * _Input_: Image vector  
            * _Output_: A Tensor $$(C \times H \times W)$$, where $$C$$ is the number of classes.  
    :   The key observation is that one can view __Fully Connected Layers__ as __Convolutions__ over the entire image.  
        Thus, the structure of the ConvNet is just a stacked number of convolutional layers that __preserve the size of the image__.  
        * __Issue with the Architecture:__   
            The proposed approach of preserving the size of the input image leads to an exploding number of hyperparamters.  
            This makes training the network very tedious and it almost never converges.  
        * __Solution__:  
            We allow the network to perform an encoding of the image by   
            first __Downsampling__ the image,  
            then, __Upsampling__ the image back, inside the network.  
            The __Upsampling__ is __not__ done via _bicubic interpolation_, instead, we use __Deconvolutional__ layers (Unpooling) for learning the upsampling.   
            However, (even learnable)upsampling produces coarse segmentation maps because of loss of information during pooling. Therefore, shortcut/skip connections are introduced from higher resolution feature maps. 
    :   _Long et. al (2014)_  
    :   ![img](/main_files/cs231n/11/3.png){: width="80%"}

***

## Methods, Approaches and Algorithms in Training DL Models
{: #content4}

1. **Upsampling:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents41}  
    :   Also, known as __"Unpooling"__.  
    :   * __Nearest Neighbor__: fill each region with the corresponding pixel value in the original image.  
            ![img](/main_files/cs231n/11/4.png){: width="40%"}  
    :   * __Bed of Nails__: put each corresponding pixel value in the original image into the upper-left corner in each new sub-region, and fill the rest with zeros.   
            ![img](/main_files/cs231n/11/5.png){: width="40%"}  
    :   * __Max-Unpooling__: The same idea as _Bed of Nails_, however, we re-place the pixel values from the original image into their original values that they were extracted from in the _Max-Pooling_ step.  
            ![img](/main_files/cs231n/11/6.png){: width="80%"}

2. **Learnable Upsampling: Deconvolutional Layers (Transpose Convolution):**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents42}  
    :   * __Transpose Convolution__: is a convolution performed on a an _input_ of a small size, each element in the input acts a _scalar_ that gets multiplied by the filter, and then gets placed on a, larger, _output_ matrix, where the regions of overlap get summed.   
        ![img](/main_files/cs231n/11/7.png){: width="80%"}
    :   Also known as:  
        * Deconvolution
        * UpConvolution
        * Fractionally Strided Convolution  
            > Reason: if you think of the stride as the ratio in step between the input and the output; this is equivalent to a stride one-half convolution, because of the ratio of 1-to-2 between the input and the output.  
        * Backward Strided Convolution
            > Reason: The forward pass of a Transpose Convolution is the same mathematical operation as the backward pass of a normal convolution.   
    :   * __1-D Example:__  
            ![img](/main_files/cs231n/11/8.png){: width="60%"}
    :   * __Convolution as Tensor Multiplication__: All Convolutions (with stride and padding) can be framed as a __Tensor Product__ by placing the filters intelligently in a tensor.  
            The name __Transpose Convolution__ comes from the fact that the __Deconvolution__ operation, viewed as a __Tensor Product__, is just the __Transpose__ of the Convolution operation.  
            * 1-D Example:   
                ![img](/main_files/cs231n/11/9.png){: width="90%"}  
            * In-fact, the name __Deconvolution__ is a mis-nomer exactly because of this interpretation:  
                The __Transpose__ matrix of the Convolution operation is a convolution __iff__ the __stride__ is equal to 1.  
                If the stride>1, then the transpose matrix no longer represents a convolution.  
                    ![img](/main_files/cs231n/11/10.png){: width="90%"}
    :   * __Issues with Transpose Convolution:__    
            * Since we sum the values that overlap in the region of the upsampled image, the magnitudes in the output will __vary depending on the number of receptive fields in the output__.  
                This leads to some _checkerboard artifacts_.  
        * __Solution:__ 
            * Avoid (3x3) stride two deconvolutions.  
            * Use (4x4) stride two, or (2x2) stride two deconvolutions. 