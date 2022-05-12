---
layout: NotesPage
title: Object Detection <br /> with Deep Learning
permalink: /work_files/research/dl/dec
prevLink: /work_files/research/dl/cv.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Object Detection](#content1)
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

## Object Detection
{: #content1}

1. **Object Detection:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    :   __Object Detection__ is the process of finding multiple instances of real-world objects such as faces, vehicles, and animals in images.  
    :   ![img](/main_files/cs231n/11_3/1.png){: width="28%"}  


2. **The Structure:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    :   * __Input__: Image  
        * __Output__: A pair of (box-co-ords, class) of all the objects in a fixed number of classes that appear in the image.  

3. **Properties:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    :   In the problem of object detection, we normally do not know the number of objects that we need to detect.  
        This leads to a problem when trying to model the problem as a __regression__ problem due to the undefined number of coordinates of boxes.  
    :   Thus, this problem is mainly modeled as a classification problem.  

4. **Applications:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    :   * Image Retrieval
        * Surveillance 
        * Face Detection
        * Face Recognition
        * Pedestrian Detection
        * Self-Driving Cars

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

2. **Region Proposals:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}  
    :   
    :   * __Algorithm__:  
            * Find "blobby" image regions that are likely to contain objects  
    :   These are relatively fast algorithms.   
    :   _Alexe et al, “Measuring the objectness of image windows”, TPAMI 2012_  
        _Uijlings et al, “Selective Search for Object Recognition”, IJCV 2013_  
        _Cheng et al, “BING: Binarized normed gradients for objectness estimation at 300fps”, CVPR 2014_  
        _Zitnick and Dollar, “Edge boxes: Locating object proposals from edges”, ECCV 2014_

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
    :   We utilize _classification_ for _detection_ purposes.  
    :   * __Algorithm__:    
            * We break up the input image into tiny "crops" of the input image.  
            * Use Classification+Localization to find the class of the center pixel of the crop, or classify it as background.  
                > Using the same machinery for classification+Localization.  
            * Slide the window and look at more "crops"
    :   Basically, we do classification+Localization on each crop of the image.
    :   * __DrawBacks:__  
            * Very Inefficient and Expensive:  
                We need to apply a CNN to a huge number of locations and scales.   
    :   _Sermant et. al 2013: "OverFeat"_

2. **Region Proposal Networks (R-CNNs):**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}  
    :   A framework for object detection, that utilizes Region Proposals (Regions of Interest (ROIs)), consisting of three separate architectures.   
    :   ![img](/main_files/cs231n/11_3/3.png){: width="82%"}
    :   * __Structure__:  
            * _Input_: Image vector  
            * _Output_: A vector of bounding boxes coordinates and a class prediction for each box     
    :   * __Strategy__:  
            Propose a number of "bounding boxes", then check if any of them, actually, corresponds to an object.  
            > The bounding boxes are created using __Selective Search__.
    :   * __Selective Search__: A method that looks at the image through windows of different sizes, and for each size tries to group together adjacent pixels by texture, color, or intensity to identify objects.    
            ![img](/main_files/cs231n/11_3/2.png){: width="100%"}
    :   * __Key Insights__:  
            1. One can apply high-capacity convolutional neural networks (CNNs) to bottom-up region proposals in order to localize and segment objects  
            2. When labeled training data is scarce, supervised pre-training for an auxiliary task, followed by domain-specific fine-tuning, yields a significant performance boost.        
    :   * __Algorithm__:   
            * Create _Region Proposals (Regions of Interest (ROIs))_ of bounding boxes  
            * Warp the regions to a standard square size to fit the "cnn classification models", due to the FCNs    
            * Pass the warped images to a modified version of _AlexNet_ to _extract image features_  
            * Pass the _image features_ to an SVM to _classify the image regions_ into a _class_ or _background_
            * Run the bounding box coordinates in a __Linear Regression__ model to "tighten" the bounding boxes
                * *__Linear Regression__*: 
                    * __Structure__:   
                        * _Input_: sub-regions of the image corresponding to objects  
                        * _Output_: New bounding box coordinates for the object in the sub-region.
    :   * __Issues__:   
            * Ad hoc training objectives:  
                * Fine-tune network with softmax classifier (log loss)
                * Train post-hoc linear SVMs (hinge loss)
                * Train post-hoc bounding-box regressions (least squares)
            * Training is slow (84h), takes a lot of disk space
            * Inference (detection) is slow
                * 47s / image with VGG16 [Simonyan & Zisserman. ICLR15]
                * Fixed by SPP-net [He et al. ECCV14]
    :   R-CNN is slow because it performs a ConvNet forward pass for each region proposal, without sharing computation.  
    :   _R. Girshick, J. Donahue, T. Darrell, J. Malik. (2014): "Rich feature hierarchies for accurate object detection and semantic segmentation"_  

3. **Fast R-CNNs:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}  
    :   A single, end-to-end, architecture for object detection based on R-CNNs, that vastly improves on its speed and accuracy by utilizing shared computations of features.     
    :   ![img](/main_files/cs231n/11_3/4.png){: width="82%"}
    :   * __Structure__:  
            * _Input_: Image vector  
            * _Output_: A vector of bounding boxes coordinates and a class prediction for each box     
    :   * __Key Insights__:  
            1. Instead of running the ConvNet on __each region proposal separately__, we run the ConvNet on the __entire image__.  
            2. Instead of taking __crops of the original image__, we __project the regions of interest__ onto the __ConvNet Feature Map__, corresponding to each RoI, and then use the __projected regions in the feature map__ _for classification_.  
                This allows us to __reuse__ a lot of the expensive computation of the features.  
            3. Jointly train the CNN, classifier, and bounding box regressor in a single model. Where earlier we had different models to extract image features (CNN), classify (SVM), and tighten bounding boxes (regressor), Fast R-CNN instead used a single network to compute all three.
    :   * __Algorithm__:   
            * Create _Region Proposals (Regions of Interest (ROIs))_ of bounding boxes       
            * Pass the entire image to a modified version of _AlexNet_ to _extract image features_ by creating an _image feature map_ for the __entire image__.  
            * Project each _RoI_ to the _feature map_ and crop each respective projected region
            * Apply __RoI Pooling__ to the _regions extracted from the feature map_ to a standard square size to fit the "cnn classification models", due to the FCNs
            * Pass the _image features_ to an SVM to _classify the image regions_ into a _class_ or _background_
            * Run the bounding box coordinates in a __Linear Regression__ model to "tighten" the bounding boxes
                * *__Linear Regression__*: 
                    * __Structure__:   
                        * _Input_: sub-regions of the image corresponding to objects  
                        * _Output_: New bounding box coordinates for the object in the sub-region.  
    :   * __RoI Pooling__: is a pooling technique aimed to perform max pooling on inputs of nonuniform sizes to obtain fixed-size feature maps (e.g. 7×7).  
            * *__Structure__*:   
                * _Input_: A fixed-size feature map obtained from a deep convolutional network with several convolutions and max pooling layers.  
                * _Output_: An N x 5 matrix of representing a list of regions of interest, where N is a number of RoIs. The first column represents the image index and the remaining four are the coordinates of the top left and bottom right corners of the region.  
            For every region of interest from the input list, it takes a section of the input feature map that corresponds to it and scales it to some pre-defined size.  
            * *__Scaling__*:    
                1. Divide the RoI into equal-sized sections (the number of which is the same as the dimension of the output)  
                2. Find the largest value in each section  
                3. Copy these max values to the output buffer  
            The __dimension of the output__ is determined solely by _the number of sections we divide the proposal_ into.   
            ![img](/main_files/cs231n/11_3/5.png){: width="90%"}
    :   * __The Bottleneck__:   
            It appears that Fast R-CNNs are capable of object detection at test time in:  
            * _Including RoIs_: 2.3s
            * _Excluding RoIs_: 0.3s  
            Thus, __the bottleneck__ for the speed seems to be the method of creating the RoIs, _Selective Search_
    :   _[1] Girshick, Ross (2015). "Fast R-CNN"_  

4. **Faster R-CNNs:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents34}  
    :   A single, end-to-end, architecture for object detection based on Fast R-CNNs, that tackles the bottleneck in speed (i.e. computing RoIs) by introducing __Region Proposal Networks (RPNs)__ to make a CNN predict proposals from features.     
        Region Proposal Networks share full-image convolutional features with the detection network, thus enabling nearly cost-free region proposals.   
        The network is jointly trained with 4 losses:
            1. RPN classify object / not object
            2. RPN regress box coordinates
            3. Final classification score (object classes)
            4. Final box coordinates
    :   ![img](/main_files/cs231n/11_3/6.png){: width="60%"}
    :   * __Region Proposal Network (RPN)__: is an, end-to-end, fully convolutional network that simultaneously predicts object bounds and objectness scores at each position.  
        RPNs work by passing a sliding window over the CNN feature map and at each window, outputting k potential bounding boxes and scores for how good each of those boxes is expected to be. 
    :   * __Structure__:  
            * _Input_: Image vector  
            * _Output_: A vector of bounding boxes coordinates and a class prediction for each box     
    :   * __Key Insights__:  
            1. Replace __Selective Search__ for finding RoIs by a __Region Proposal Network__ that shares the features, and thus reduces the computation and time, of the pipeline.  
    :   * __Algorithm__:   
            * Pass the entire image to a modified version of _AlexNet_ to _extract image features_ by creating an _image feature map_ for the __entire image__.  
            * Pass the __CNN Feature Map__ to the RPN to generate bounding boxes and a score for each bounding box 
            * Pass each such bounding box that is likely to be an object into Fast R-CNN to generate a classification and tightened bounding boxes. 
    :   _Ren et al, (2015). “Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks”_  

***

## Methods, Approaches and Algorithms in Training DL Models
{: #content4}
