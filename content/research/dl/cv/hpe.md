---
layout: NotesPage
title: Articulated Body Pose Estimation <br /> (Human Pose Estimation)
permalink: /work_files/research/dl/pose_est
prevLink: /work_files/research/dl/cv.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Introduction](#content1)
  {: .TOC1}
  * [SECOND](#content2)
  {: .TOC2}
  * [THIRD](#content3)
  {: .TOC3}
  * [FOURTH](#content4)
  {: .TOC4}
</div>

***
***

## Introduction
{: #content1}
 
***

## DeepPose 
{: #content2}

[Further Reading](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/42237.pdf)

1. **Main Idea:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    :   Pose Estimation is formulated as a __DNN-based regression problem__ towards __body joints__.  
        The __DNN regressors__ are presented as a cascade for higher precision in pose estimates.    

2. **Structure:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}  
    :   * __Input__: 
            * Full Image
            * 7-layered generic Convolutional DNN    
        > Each Joint Regressor uses the full image as a signal.   


3. **Key Insights:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}  
    :   * Replace the __explicitly designed feature representations and detectors for the parts, the model topology, and the interactions between joints__ by a *__learned representation through a ConvNet__*  
        * The (DNN-based) Pose Predictors are presented as a __cascade__ to increase the precision of _joint localization_  
        * Although the regression loss does not model explicit interactions between joints, such are implicitly captured by all of the 7 hidden layers – all the internal features are shared by all joint regressors

4. **Method:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}  
    :   * Start with an initial pose estimation (based on the full image)
        * Learn DNN-based regressors which refine the joint predictions by using higher resolution sub-images


5. **Notation:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}  
    :   * __Pose Vector__ = $$\mathbf{y} = \left(\ldots, \mathbf{y}_i^T, \ldots\right)^T, \: i \in \{1, \ldots, k\}$$  
        * __Joint Co-ordinates__ = $$\mathbf{y}_i^T = (x_i, y_i)$$ of the $$i$$-th joint  
        * __Labeled Image__ = $$(x, \mathbf{y})$$  
            * $$x = $$ Image Data  
            * $$\mathbf{y} = $$ Ground-Truth Pose Vector
        * __Bounding Box__ = $$b$$: a box bounding the human body or parts of it   
        * __Normalization Function__ $$= N(\mathbf{y}_i; b)$$: normalizes the *joint coordinates* w.r.t a bounding box $$b$$  
            > Since the joint coordinates are in absolute image coordinates, and poses vary in size from image to image   

            ![img](/main_files/cv/pose_est/3.png){: width="60%"}  
            * _Translate_ by _box center_
            * _Scale_ by _box size_  
        * __Normalized pose vector__ = $$N(\mathbf{y}; b) = \left(\ldots, N(\mathbf{y}_i; b)^T, \ldots\right)^T$$  
        * __A crop of image $$x$$ by bounding box $$b$$__ = $$N(x; b)$$
        * *__Learned Function__* = $$\psi(x;\theta) \in \mathbb{R}^2k$$ is a functions that regresses to normalized pose vector, given an image:  
            * __Input__: image $$x$$
            * __Output__: Normalized pose vector $$N(\mathbf{y})$$                 
        * *__Pose Prediction__*:   
        :   $$y^\ast = N^{-1}(\psi(N(x);\theta))$$   

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

## 
{: #content3}

1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}  
    :   


2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}  
    :   


3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}  
    :   


4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents34}  
    :   


5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents35}  
    :   


6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents36}  
    :   


7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents37}  
    :   


8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents38}  
    :   


***

## FOURTH
{: #content4}

1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents41}  
    :   


2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents42}  
    :   


3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents43}  
    :   


4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents44}  
    :   


5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents45}  
    :   


6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents46}  
    :   
