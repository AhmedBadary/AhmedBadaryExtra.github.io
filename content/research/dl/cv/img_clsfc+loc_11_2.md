---
layout: NotesPage
title: Image Classification and Localization <br /> with Deep Learning
permalink: /work_files/research/dl/loc
prevLink: /work_files/research/dl/cv.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Image Localization](#content1)
  {: .TOC1}
  * [Approaches](#content2)
  {: .TOC2}
  * [Training Methods, Approaches and Algorithms](#content3)
  {: .TOC3}
</div>

***
***

* [The evolution of image classification explained (blog!)](https://stanford.edu/~shervine/blog/evolution-image-classification-explained)  
* [Image Classification on ImageNet - Leaderboards](https://paperswithcode.com/sota/image-classification-on-imagenet)  
* [Image Classification on CIFAR-100 - Leaderboards](https://paperswithcode.com/sota/image-classification-on-cifar-100)  
* [Image Classification on MNIST - Leaderboards](https://paperswithcode.com/sota/image-classification-on-mnist)  


## Image Localization
{: #content1}

1. **Image Localization:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    :   __Localization__ is the task of finding a single object in an image.  
    :   ![img](/main_files/cs231n/11_2/1.png){: width="25%"}  

2. **Image Classification+Localization:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    :   __Localization__ can be combined with classification to, not only find the location of an object but, also, to classify it into one of different classes. 
    :   ![img](/main_files/cs231n/11_2/2.png){: width="35%"}  

3. **Structure:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    :   * __Input__: Image  
        * __Output__: A vector of 4 coordinates of the bounding box.  

4. **Applications:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    :   * Smart Cropping
        * Regular Object Extraction (as a pre-processing step)  
        * Human Pose Estimation: Represent pose as a set of 14 joint positions 

***

## Approaches
{: #content2}

1. **Localization as a Regression Problem:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    :   Since we are concerned with returning real-valued numbers (the bounding box coordinates), we use a method that is suitable for the task, __Regression__.   
    :   ![img](/main_files/cs231n/11_2/3.png){: width="80%"}
    :   * __Algorithm__:    
            * Use any classification architecture  
            * Attach two _Fully Connected Layers_, one for __Classification__ and one for __Localization__  
            * Backpropagate through the whole network using _cross-entropy loss_ and _L2 loss_ respectively.  
    :   * __Evaluation Metric:__ Intersection over Union.  

***

## Training Methods, Approaches and Algorithms 
{: #content4}

### Updated Soon!