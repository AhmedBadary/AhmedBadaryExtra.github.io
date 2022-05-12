---
layout: NotesPage
title: CNNs <br /> Convolutional Neural Networks
permalink: /work_files/research/dl/conv_net_vis_recog
prevLink: /work_files/research/dl/cv.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Introduction](#content1)
  {: .TOC1}
  * [Architecture and Design](#content2)
  {: .TOC2}
  * [THIRD](#content3)
  {: .TOC3}

</div>

***
***

## Image Classification
{: #content1}

1. **The Problem:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11} 
    :   Assigning a semantic label from a fixed set of categories to a sub-grid of an image.
    :   The problem is often referred to as __The Semantic Gap__.

2. **The Challenges:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12} 
    :   1. Viewpoint Variation  
        ![img](/main_files/cs231n/2/1.png){: width="50%"}  
        2. Illumination Conditions  
        ![img](/main_files/cs231n/2/2.png){: width="50%"}  
        3. Deformation  
        ![img](/main_files/cs231n/2/3.png){: width="50%"}  
        4. Occlusion  
        ![img](/main_files/cs231n/2/4.png){: width="50%"}  
        5. Background Clutter  
        ![img](/main_files/cs231n/2/5.png){: width="50%"}  
        6. Intra-class variation  
        ![img](/main_files/cs231n/2/6.png){: width="50%"}  
        7. Scale Variation  
        ![img](/main_files/cs231n/2/7.png){: width="50%"}  

3. **Attempts:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13} 
    :   1. 

4. **The Data-Driven Approach:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14} 
    :   1. Collect a dataset of images and labels.  
        2. Use Machine Learning to train a classifier.  
        3. Evaluate the classifier on new images.  

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15} 

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16} 

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17} 

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18} 

***

## Classifiers
{: #content2}

1. **K-Nearest-Neighbors:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21} 
    :   

    :   __Complexity__:  
        :   * _Training_: $$\:\:\:\:\mathcal{O}(1)$$   
            * _Predict_: $$\:\:\:\:\mathcal{O}(N)$$ 

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22} 

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23} 

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24} 

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25} 

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents26} 

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents27} 

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents28} 

***

## Metrics
{: #content3}

1. **L1 Distance:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31} 
    :   $$d_1(I_1, I_2) = \sum_p{\|I_1^p - I_2^p\|}$$  
    :   Pixel-wise absolute value differences.  

2. **L2 Distance:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32} 
    :   $$d_2 (I_1, I_2) = \sqrt{\sum_{p} \left( I^p_1 - I^p_2 \right)^2}$$
    :   

3. **L1 vs. L2:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33} 
    :   The L2 distance penalizes errors (pixel differences) much more than the L1 metric does.  
    The L2 distnace will be small iff there are man small differences in the two vectors but will explode if there is even one big difference between them.  
    :   Another difference we highlight is that the L1 distance is dependent on the corrdinate system frame, while the L2 distance is coordinate-invariant.

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents34} 

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents35} 

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents36} 

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents37} 

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents38} 