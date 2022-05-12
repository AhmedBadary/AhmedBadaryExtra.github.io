---
layout: NotesPage
title: Uncertainty in Neural Networks
permalink: /work_files/research/dl/theory/uncertainty_nns
prevLink: /work_files/research/dl/theory.html
---




* [Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles (paper)](https://arxiv.org/pdf/1612.01474.pdf)  
* [On Calibration of Modern Neural Networks](https://arxiv.org/pdf/1706.04599.pdf)  
* [state of the art in confidence scoring, calibration and out of distribution detection](https://www.reddit.com/r/MachineLearning/comments/907p7a/d_what_is_the_current_state_of_the_art_in/)  
* [Uncertainty in Deep Learning (PhD Thesis - Yarin Gal)](http://mlg.eng.cam.ac.uk/yarin/blog_2248.html)  




__Uncertainty Types:__{: style="color: red"}  
{: #lst-p}
* __Aleatoric Uncertainty__: AKA __Statistical Uncertainty__  
    It is representative of unknowns that differ each time we run the same experiment.  
    It describes the variance of the conditional distribution of our target variable given our features. 
    It arises due to hidden variables or measurement errors, and cannot be reduced by collecting more data under the same experimental conditions.  
    Aleatoric uncertainty arises when, for data in the training set, data points with very similar feature vectors (x) have targets (y) with substantially different values. No matter how good your model is at fitting the average trend, there is just no getting around the fact that it will not be able to fit every datapoint perfectly when aleatoric uncertainty is present.  
* __Epistemic Uncertainty__: AKA __Systematic/Model Uncertainty__.  
    It captures our ignorance about which model generated our collected data. This uncertainty can be explained away given enough data.  
