---
layout: NotesPage
title: Clustering
permalink: /work_files/research/ml/clustering
prevLink: /work_files/research/dl/ml.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Clustering - Introduction](#content1)
  {: .TOC1}
<!--   * [SECOND](#content2)
  {: .TOC2}
  * [THIRD](#content3)
  {: .TOC3} -->
</div>

***
***


* [Deep Clustering](https://deepnotes.io/deep-clustering)  


## Clustering - Introduction
{: #content1}

1. **Clustering:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  


<!-- 2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17} -->

8. **Notes:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18}  
    
    [EM Algorithm Video](https://www.youtube.com/watch?v=REypj2sy_5U)  


    __Clustering Types:__{: style="color: red"}  
    * __Hard Clustering__: clusters do not overlap
        * Elements either belong to a cluster or it doesn't
    * __Soft Clustering__: cluster may overlap  
        * Computes a strength of association between clusters and instances  
        
    __Mixture Models:__{: style="color: red"}  
    {: #lst-p}
    * probabilistically-grounded way of doing soft clustering 
    * each cluster: a generative model (Gaussian or multinomial) 
    * parameters (e.g. mean/covariance are unknown) 

    __Mixture Models as Latent Variable Models:__  
    A mixture model can be described more simply by assuming that each observed data point has a corresponding unobserved data point, or latent variable, specifying the mixture component to which each data point belongs.  
    <br>


    __Expectation Maximization (EM):__{: style="color: red"}  
    {: #lst-p}
    * Chicken and egg problem:  
        * need $$\left(\mu_{a}, \sigma_{a}^{2}\right),\left(\mu_{b}, \sigma_{b}^{2}\right)$$ to guess source of points 
        * need to know source to estimate $$\left(\mu_{a}, \sigma_{a}^{2}\right),\left(\mu_{b}, \sigma_{b}^{2}\right)$$  
    * EM algorithm 
        * start with two randomly placed Gaussians $$\left(\mu_{a}, \sigma_{a}^{2}\right),\left(\mu_{b}, \sigma_{b}^{2}\right)$$
        * for each point: $$P(b \vert x_i)$$ does it look like it came from $$b$$?  
        * adjust $$\left(\mu_{a}, \sigma_{a}^{2}\right),\left(\mu_{b}, \sigma_{b}^{2}\right)$$ to fit points assigned to them  




<!-- 
***

## SECOND
{: #content2}

1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents26}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents27}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents28}
 -->