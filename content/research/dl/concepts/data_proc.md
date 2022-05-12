---
layout: NotesPage
title: Data Processing
permalink: /work_files/dl/concepts/data_proc
prevLink: /work_files/research/dl/concepts
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Dimensionality Reduction](#content1)
  {: .TOC1}
  * [Feature Selection](#content2)
  {: .TOC2}
  * [Feature Extraction](#content3)
  {: .TOC3}
  * [Feature Importance](#content4)
  {: .TOC4}
  * [Imputation](#content5)
  {: .TOC5}
  * [Normalization](#content6)
  {: .TOC6}
  * [Outliers Handling](#content7)
  {: .TOC7}
</div>

***
***

* [Data Wrangling Techniques (Blog!)](https://theprofessionalspoint.blogspot.com/2019/03/data-wrangling-techniques-steps.html)  

* [Non-Negative Matrix Factorization NMF Tutorial](http://mlexplained.com/2017/12/28/a-practical-introduction-to-nmf-nonnegative-matrix-factorization/)  
* [How to Use t-SNE Effectively (distill blog!)](https://distill.pub/2016/misread-tsne/)  

* [UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction [better than t-sne?] (Library Code!)](https://umap-learn.readthedocs.io/en/latest/)  


## Dimensionality Reduction
{: style="font-size: 1.60em"}
{: #content1}


### **Dimensionality Reduction**{: style="color: SteelBlue; font-size: 1.15em"}{: .bodyContents1 #bodyContents11}  
__Dimensionality Reduction__ is the process of reducing the number of random variables under consideration by obtaining a set of principal variables. It can be divided into __feature selection__{: style="color: goldenrod"} and __feature extraction__{: style="color: goldenrod"}.  
<br>

**Dimensionality Reduction Methods:**
{: #lst-p}
* PCA
* Heatmaps
* t-SNE
* Multi-Dimensional Scaling (MDS)

### **t-SNE \| T-distributed Stochastic Neighbor Embeddings**{: style="color: SteelBlue; font-size: 1.15em"}{: .bodyContents1 #bodyContents12}  

<button>Paper</button>{: .showText value="show"
     onclick="showText_withParent_PopHide(event);"}
<iframe hidden="" src="https://docs.google.com/viewer?url=http://jmlr.org/papers/volume9/vandermaaten08a/vandermaaten08a.pdf&amp;embedded=true" frameborder="0" height="840" width="646" title="Layer Normalization" scrolling="auto"></iframe>

[Understanding t-SNE Part 1: SNE algorithm and its drawbacks](https://medium.com/@layog/i-dont-understand-t-sne-part-1-50f507acd4f9)  
[Understanding t-SNE Part 2: t-SNE improvements over SNE](https://medium.com/@layog/i-do-not-understand-t-sne-part-2-b2f997d177e3)  
[t-SNE (statwiki)](https://wiki.math.uwaterloo.ca/statwiki/index.php?title=visualizing_Data_using_t-SNE)  
[t-SNE tutorial (video)](https://www.youtube.com/watch?v=W-9L6v_rFIE)  
[series (deleteme)](https://www.youtube.com/watch?v=FQmCzpKWD48&list=PLupD_xFct8mHqCkuaXmeXhe0ajNDu0mhZ)  



__SNE - Stochastic Neighbor Embeddings:__{: style="color: red"}  
__SNE__ is a method that aims to _match_ __distributions of distances__ between points in high and low dimensional space via __conditional probabilities__.  
It Assumes distances in both high and low dimensional space are __Gaussian-distributed__.  
* [**Algorithm**](https://www.youtube.com/embed/ohQXphVSEQM?start=130){: value="show" onclick="iframePopA(event)"}
<a href="https://www.youtube.com/embed/ohQXphVSEQM?start=130"></a>
    <div markdown="1"> </div>    
    ![img](/main_files/dl/concepts/data_proc/2.png){: width="65%"}  
<br> 


__t-SNE:__{: style="color: red"}  
__t-SNE__ is a machine learning algorithm for visualization developed by Laurens van der Maaten and Geoffrey Hinton.  
It is a *__nonlinear__* *__dimensionality reduction__* technique well-suited for _embedding high-dimensional data for visualization in a low-dimensional space_ of _two or three dimensions_.  
Specifically, it models each high-dimensional object by a two- or three-dimensional point in such a way that <span>similar objects are modeled by nearby points</span>{: style="color: goldenrod"} and <span>dissimilar objects are modeled by distant points</span>{: style="color: goldenrod"}  __with high probability__.  
> It tends to *preserve __local structure__*, while at the same time, *preserving the __global structure__* as much as possible.  

<br>

__Stages:__{: style="color: red"}  
{: #lst-p}
1. It Constructs a probability distribution over pairs of high-dimensional objects in such a way that similar objects have a high probability of being picked while dissimilar points have an extremely small probability of being picked.  
2. It Defines a similar probability distribution over the points in the low-dimensional map, and it minimizes the __Kullback–Leibler divergence__ between the two distributions with respect to the locations of the points in the map.  
<br>

__Key Ideas:__{: style="color: red"}  
It solves two big problems that __SNE__ faces:  
{: #lst-p}
1. __The Crowding Problem:__  
    The "crowding problem" that are addressed in the paper is defined as: "the area of the two-dimensional map that is available to accommodate moderately distant datapoints will not be nearly large enough compared with the area available to accommodate nearby datepoints". This happens when the datapoints are distributed in a region on a high-dimensional manifold around i, and we try to model the pairwise distances from i to the datapoints in a two-dimensional map. For example, it is possible to have 11 datapoints that are mutually equidistant in a ten-dimensional manifold but it is not possible to model this faithfully in a two-dimensional map. Therefore, if the small distances can be modeled accurately in a map, most of the moderately distant datapoints will be too far away in the two-dimensional map. In SNE, this will result in very small attractive force from datapoint i to these too-distant map points. The very large number of such forces collapses together the points in the center of the map and prevents gaps from forming between the natural clusters. This phenomena, crowding problem, is not specific to SNE and can be observed in other local techniques such as Sammon mapping as well.  
    * __Solution - Student t-distribution for $$q$$__:  
        Student t-distribution is used to compute the similarities between data points in the low dimensional space $$q$$.  
2. __Optimization Difficulty of KL-div:__  
    The KL Divergence is used over the conditional probability to calculate the error in the low-dimensional representation. So, the algorithm will be trying to minimize this loss and will calculate its gradient:  
    <p>$$\frac{\delta C}{\delta y_{i}}=2 \sum_{j}\left(p_{j | i}-q_{j | i}+p_{i | j}-q_{i | j}\right)\left(y_{i}-y_{j}\right)$$</p>  
    This gradient involves all the probabilities for point $$i$$ and $$j$$. But, these probabilities were composed of the exponentials. The problem is that: We have all these exponentials in our gradient, which can explode (or display other unusual behavior) very quickly and hence the algorithm will take a long time to converge.  
    * __Solution - Symmetric SNE__:  
        The Cost Function is a __symmetrized__ version of that in SNE. i.e. $$p_{i\vert j} = p_{j\vert i}$$ and $$q_{i\vert j} = q_{j\vert i}$$.  
<br>

__Application:__{: style="color: red"}  
It is often used to visualize high-level representations learned by an __artificial neural network__.  
<br>

__Motivation:__{: style="color: red"}  
There are a lot of problems with traditional dimensionality reduction techniques that employ _feature projection_; e.g. __PCA__. These techniques attempt to *__preserve the global structure__*, and in that process they *__lose the local structure__*. Mainly, projecting the data on one axis or another, may (most likely) not preserve the _neighborhood structure_ of the data; e.g. the clusters in the data:  
![img](/main_files/dl/concepts/data_proc/1.png){: width="70%"}  
t-SNE finds a way to project data into a low dimensional space (1-d, in this case) such that the clustering ("local structure") in the high dimensional space is preserved.  
<br>


__t-SNE Clusters:__{: style="color: red"}  
While t-SNE plots often seem to display clusters, the visual clusters can be influenced strongly by the chosen parameterization and therefore a good understanding of the parameters for t-SNE is necessary. Such "clusters" can be shown to even appear in non-clustered data, and thus may be false findings.  
It has been demonstrated that t-SNE is often able to _recover well-separated clusters_, and with special parameter choices, [approximates a simple form of __spectral clustering__](https://arxiv.org/abs/1706.02582).  
<br>

__Properties:__{: style="color: red"}  
{: #lst-p}
* It preserves the _neighborhood structure_ of the data  
* Does NOT preserve _distances_ nor _density_  
* Only to some extent preserves _nearest-neighbors_?  
    [discussion](https://stats.stackexchange.com/questions/263539/clustering-on-the-output-of-t-sne/264647#264647)  
* It learns a __non-parametric mapping__, which means that it does NOT learn an _explicit function_ that maps data from the input space to the map  
<br>

__Algorithm:__{: style="color: red"}  
<button>Algorithm Details (wikipedia)</button>{: .showText value="show"
     onclick="showText_withParent_PopHide(event);"}
<iframe hidden="" src="https://www.wikiwand.com/en/T-distributed_stochastic_neighbor_embedding#/Details" frameborder="0" height="840" width="646" title="Layer Normalization"></iframe>

<br>

__Issues/Weaknesses/Drawbacks:__{: style="color: red"}  
{: #lst-p}
1. The paper only focuses on the date visualization using t-SNE, that is, embedding high-dimensional date into a two- or three-dimensional space. However, this behavior of t-SNE presented in the paper cannot readily be extrapolated to $$d>3$$ dimensions due to the heavy tails of the Student t-distribution.  
2. It might be less successful when applied to data sets with a high intrinsic dimensionality. This is a result of the *__local linearity assumption__ on the manifold* that t-SNE makes by employing Euclidean distance to present the similarity between the datapoints. 
3. The cost function is __not convex__. This leads to the problem that several optimization parameters (hyperparameters) need to be chosen (and tuned) and the constructed solutions depending on these parameters may be different each time t-SNE is run from an initial random configuration of the map points.  
4. It cannot work __"online"__. Since it learns a non-parametric mapping, which means that it does not learn an explicit function that maps data from the input space to the map. Therefore, it is not possible to embed test points in an existing map. You have to re-run t-SNE on the full dataset.  
    A potential approach to deal with this would be to train a multivariate regressor to predict the map location from the input data.  
    Alternatively, you could also [make such a regressor minimize the t-SNE loss directly (parametric t-SNE)](https://lvdmaaten.github.io/publications/papers/AISTATS_2009.pdf).  

<br>

__t-SNE Optimization:__{: style="color: red"}  
{: #lst-p}
* [Accelerating t-SNE using Tree-Based Algorithms](https://lvdmaaten.github.io/publications/papers/JMLR_2014.pdf)  
* [Barnes-Hut-SNE Optimization](https://arxiv.org/pdf/1301.3342.pdf)  

<br>

__Discussion and Information:__{: style="color: red"}  
{: #lst-p}
* __What is perplexity?__  
    Perplexity is a measure for information that is defined as 2 to the power of the Shannon entropy. The perplexity of a fair die with k sides is equal to k. In t-SNE, the perplexity may be viewed as a knob that sets the number of effective nearest neighbors. It is comparable with the number of nearest neighbors k that is employed in many manifold learners.  
* __Choosing the perplexity hp:__   
    The performance of t-SNE is fairly robust under different settings of the perplexity. The most appropriate value depends on the density of your data. Loosely speaking, one could say that a larger / denser dataset requires a larger perplexity. Typical values for the perplexity range between $$5$$ and $$50$$.  
* __Every time I run t-SNE, I get a (slightly) different result?__  
    In contrast to, e.g., PCA, t-SNE has a non-convex objective function. The objective function is minimized using a gradient descent optimization that is initiated randomly. As a result, it is possible that different runs give you different solutions. Notice that it is perfectly fine to run t-SNE a number of times (with the same data and parameters), and to select the visualization with the lowest value of the objective function as your final visualization.  
* __Assessing the "Quality of Embeddings/visualizations":__  
    Preferably, just look at them! Notice that t-SNE does not retain distances but probabilities, so measuring some error between the Euclidean distances in high-D and low-D is useless. However, if you use the same data and perplexity, you can compare the Kullback-Leibler divergences that t-SNE reports. It is perfectly fine to run t-SNE ten times, and select the solution with the lowest KL divergence.  
        



<!-- __Advantages:__{: style="color: red"}  
{: #lst-p}
1. Reduces time and 

### **Feature Selection**{: style="color: SteelBlue; font-size: 1.15em"}{: .bodyContents1 #bodyContents12}   -->
<br>

<!--  
### **Asynchronous**{: style="color: SteelBlue; font-size: 1.15em"}{: .bodyContents1 #bodyContents13}  
<br>
### **Asynchronous**{: style="color: SteelBlue; font-size: 1.15em"}{: .bodyContents1 #bodyContents14}  
<br>
### **Asynchronous**{: style="color: SteelBlue; font-size: 1.15em"}{: .bodyContents1 #bodyContents15}  
<br>
### **Asynchronous**{: style="color: SteelBlue; font-size: 1.15em"}{: .bodyContents1 #bodyContents16}  
<br>
### **Asynchronous**{: style="color: SteelBlue; font-size: 1.15em"}{: .bodyContents1 #bodyContents17}  
<br>
### **Asynchronous**{: style="color: SteelBlue; font-size: 1.15em"}{: .bodyContents1 #bodyContents18}  
 -->

***
***

## Feature Selection
{: style="font-size: 1.60em"}
{: #content2}


### **Feature Selection**{: style="color: SteelBlue; font-size: 1.15em"}{: .bodyContents2 #bodyContents21}  
__Feature Selection__ is the process of selecting a subset of relevant features (variables, predictors) for use in model construction.  

__Applications:__{: style="color: red"}  
{: #lst-p}
* Simplification of models to make them easier to interpret by researchers/users  
* Shorter training time  
* A way to handle _curse of dimensionality_  
* Reduction of Variance $$\rightarrow$$ Reduce Overfitting $$\rightarrow$$ Enhanced Generalization  

__Strategies/Approaches:__{: style="color: red"}  
{: #lst-p}
* __Wrapper Strategy__:  
    Wrapper methods use a predictive model to score feature subsets. Each new subset is used to train a model, which is tested on a hold-out set. Counting the number of mistakes made on that hold-out set (the error rate of the model) gives the score for that subset. As wrapper methods train a new model for each subset, they are very computationally intensive, but usually provide the best performing feature set for that particular type of model.  
    __e.g.__ __Search Guided by Accuracy__{: style="color: goldenrod"}, __Stepwise Selection__{: style="color: goldenrod"}   
* __Filter Strategy__:  
    Filter methods use a _proxy measure_ instead of the error rate _to score a feature subset_. This measure is chosen to be fast to compute, while still capturing the usefulness of the feature set.  
    Filter methods produce a feature set which is _not tuned to a specific model_, usually giving lower prediction performance than a wrapper, but are more general and more useful for exposing the relationships between features.  
    __e.g.__ __Information Gain__{: style="color: goldenrod"}, __pointwise-mutual/mutual information__{: style="color: goldenrod"}, __Pearson Correlation__{: style="color: goldenrod"}    
* __Embedded Strategy:__  
    Embedded methods are a catch-all group of techniques which perform feature selection as part of the model construction process.  
    __e.g.__ __LASSO__{: style="color: goldenrod"}  


<br>

### **Correlation Feature Selection**{: style="color: SteelBlue; font-size: 1.15em"}{: .bodyContents2 #bodyContents22}  
The __Correlation Feature Selection (CFS)__ measure evaluates subsets of features on the basis of the following hypothesis:  
"__Good feature subsets contain features highly correlated with the classification, yet uncorrelated to each other__{: style="color: goldenrod"}".  

The following equation gives the __merit of a feature subset__ $$S$$ consisting of $$k$$ features:  
<p>$${\displaystyle \mathrm {Merit} _{S_{k}}={\frac {k{\overline {r_{cf}}}}{\sqrt {k+k(k-1){\overline {r_{ff}}}}}}.}$$</p>  
where, $${\displaystyle {\overline {r_{cf}}}}$$ is the average value of all feature-classification correlations, and $${\displaystyle {\overline {r_{ff}}}}$$ is the average value of all feature-feature correlations.  

The __CFS criterion__ is defined as follows:  
<p>$$\mathrm {CFS} =\max _{S_{k}}\left[{\frac {r_{cf_{1}}+r_{cf_{2}}+\cdots +r_{cf_{k}}}{\sqrt {k+2(r_{f_{1}f_{2}}+\cdots +r_{f_{i}f_{j}}+\cdots +r_{f_{k}f_{1}})}}}\right]$$</p>  

<br>

### **Feature Selection Embedded in Learning Algorithms**{: style="color: SteelBlue; font-size: 1.15em"}{: .bodyContents2 #bodyContents23}  
* $$l_{1}$$-regularization techniques, such as sparse regression, LASSO, and $${\displaystyle l_{1}}$$-SVM
* Regularized trees, e.g. regularized random forest implemented in the RRF package
* Decision tree
* Memetic algorithm
* Random multinomial logit (RMNL)
* Auto-encoding networks with a bottleneck-layer
* Submodular feature selection

<br>

### **Information Theory Based Feature Selection Mechanisms**{: style="color: SteelBlue; font-size: 1.15em"}{: .bodyContents2 #bodyContents24}  
There are different Feature Selection mechanisms around that __utilize mutual information for scoring the different features__.  
They all usually use the same algorithm:  
1. Calculate the mutual information as score for between all features ($${\displaystyle f_{i}\in F}$$) and the target class ($$c$$)
1. Select the feature with the largest score (e.g. $${\displaystyle argmax_{f_{i}\in F}(I(f_{i},c))}$$) and add it to the set of selected features ($$S$$)
1. Calculate the score which might be derived form the mutual information
1. Select the feature with the largest score and add it to the set of select features (e.g. $${\displaystyle {\arg \max }_{f_{i}\in F}(I_{derived}(f_{i},c))}$$)
5. Repeat 3. and 4. until a certain number of features is selected (e.g. $${\displaystyle \vert S\vert =l}$$)  


<!-- <br> ### **Asynchronous**{: style="color: SteelBlue; font-size: 1.15em"}{: .bodyContents2 #bodyContents25}  
### **Asynchronous**{: style="color: SteelBlue; font-size: 1.15em"}{: .bodyContents2 #bodyContents26}   -->

***
***

## Feature Extraction
{: style="font-size: 1.60em"}
{: #content3}

### **Feature Extraction**{: style="color: SteelBlue; font-size: 1.15em"}{: .bodyContents3 #bodyContents31}  
__Feature Extraction__ starts from an initial set of measured data and builds derived values (features) intended to be informative and non-redundant, facilitating the subsequent learning and generalization steps, and in some cases leading to better human interpretations.  

In __dimensionality reduction__, feature extraction is also called __Feature Projection__, which is a method that transforms the data in the high-dimensional space to a space of fewer dimensions. The data transformation may be linear, as in principal component analysis (PCA), but many nonlinear dimensionality reduction techniques also exist.  

__Methods/Algorithms:__{: style="color: red"}  
{: #lst-p}
* Independent component analysis  
* Isomap  
* Kernel PCA  
* Latent semantic analysis  
* Partial least squares  
* Principal component analysis  
* Autoencoder  
* Linear Discriminant Analysis (LDA)  
* Non-negative matrix factorization (NMF)


<br>

<!-- ### ****{: style="color: SteelBlue; font-size: 1.15em"}{: .bodyContents3 #bodyContents32}  
### ****{: style="color: SteelBlue; font-size: 1.15em"}{: .bodyContents3 #bodyContents33}   -->

* [How to Make Your Machine Learning Models Robust to Outliers (Blog!)](https://heartbeat.fritz.ai/how-to-make-your-machine-learning-models-robust-to-outliers-44d404067d07)  



[Outliers](https://en.wikipedia.org/wiki/Outlier#Working_with_outliers)  
[Replacing Outliers](https://en.wikipedia.org/wiki/Robust_statistics#Replacing_outliers_and_missing_values)  
[Data Transformation - Outliers - Standardization](https://en.wikipedia.org/wiki/Data_transformation_(statistics))  
[PreProcessing in DL - Data Normalization](https://hadrienj.github.io/posts/Preprocessing-for-deep-learning/)  
[Imputation and Feature Scaling](https://towardsdatascience.com/the-complete-beginners-guide-to-data-cleaning-and-preprocessing-2070b7d4c6d)  
[Missing Data - Imputation](https://en.wikipedia.org/wiki/Missing_data#Techniques_of_dealing_with_missing_data)  
[Dim-Red - Random Projections](https://en.wikipedia.org/wiki/Random_projection)  
[F-Selection - Relief](https://en.wikipedia.org/wiki/Relief_(feature_selection))  
[Box-Cox Transf - outliers](https://www.statisticshowto.datasciencecentral.com/box-cox-transformation/)  
[ANCOVA](https://en.wikipedia.org/wiki/Analysis_of_covariance)  
[Feature Selection Methods](https://www.analyticsvidhya.com/blog/2016/12/introduction-to-feature-selection-methods-with-an-example-or-how-to-select-the-right-variables/)  