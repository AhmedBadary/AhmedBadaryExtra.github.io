---
layout: NotesPage
title: Ensemble Learning - Aggregating
permalink: /work_files/research/ml/ens_lern
prevLink: /work_files/research/dl/ml.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Ensemble Learning](#content1)
  {: .TOC1}
  * [Bayes optimal classifier (Theoretical)](#content2)
  {: .TOC2}
  * [Bootstrap Aggregating (Bagging)](#content3)
  {: .TOC3}
  * [Boosting](#content4)
  {: .TOC4}
  * [Stacking](#content5)
  {: .TOC5}
  <!-- * [SIXTH](#content6)
  {: .TOC6} -->
</div>

***
***


* [Ensemble methods: bagging, boosting and stacking (in detail!)](https://towardsdatascience.com/ensemble-methods-bagging-boosting-and-stacking-c9214a10a205)  
* [Bagging Boosting (Lec Slides)](http://www.cs.cornell.edu/courses/cs578/2005fa/CS578.bagging.boosting.lecture.pdf)  
* [Aggregation Methods (Lec! - Caltech)](https://www.youtube.com/watch?v=ihLwJPHkMRY&t=2692)  
* [Aggregation in the context of Deep Learning and Representation Learning (Lec - Hinton)](https://www.youtube.com/watch?v=7kAlBa7yhDM)  
* [Why it helps to combine models (hinton Lec!)](https://www.youtube.com/watch?v=JacgCGtxoj0&list=PLiPvV5TNogxKKwvKb1RKwkq2hm7ZvpHz0&index=61)  



## Ensemble Learning
{: #content1}

1. **Ensemble Learning:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    In machine learning, __Ensemble Learning__ is a set of __ensemble methods__ that use multiple learning algorithms to obtain better predictive performance than could be obtained from any of the constituent learning algorithms alone.  
    <br>

3. **Ensemble Theory:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    An _ensemble_ is itself a __supervised learning algorithm__, because it can be trained and then used to make predictions. The trained ensemble, therefore, represents a single hypothesis. This hypothesis, however, is not necessarily contained within the hypothesis space of the models from which it is built. Thus, ensembles can be shown to have more flexibility in the functions they can represent. This flexibility can, in theory, enable them to over-fit the training data more than a single model would, but in practice, some ensemble techniques (especially __bagging__) tend to reduce problems related to over-fitting of the training data.  

    Empirically, ensembles tend to yield better results when there is a significant diversity among the models. Many ensemble methods, therefore, seek to promote diversity among the models they combine.  
    Although perhaps non-intuitive, more random algorithms (like random decision trees) can be used to produce a stronger ensemble than very deliberate algorithms (like entropy-reducing decision trees).  
    Using a variety of strong learning algorithms, however, has been shown to be more effective than using techniques that attempt to dumb-down the models in order to promote diversity.  
    <br>

    * In any network, the bias can be reduced at the cost of increased variance
    * In a group of networks, the variance can be reduced at no cost to bias

4. **Types of Ensembles:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    * Bayes optimal classifier (Theoretical)
    * Bootstrap aggregating (bagging)
    * Boosting
    * Bayesian parameter averaging
    * Bayesian model combination
    * Bucket of models
    * Stacking
    <br>

5. **Applications:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  
    * Remote sensing
        * Land cover mapping
        * Change detection
    * Computer security
        * Distributed denial of service
        * Malware Detection
        * Intrusion detection
    * Face recognition
    * Emotion recognition
    * Fraud detection
    * Financial decision-making
    * Medicine
    <br>

7. **Ensemble Size:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}  
    It is an important problem that hasn't been well studied/addressed.  

    More recently, a [theoretical framework](https://static.aminer.org/pdf/fa/cikm2016/shp1026-r.-bonabA.pdf) suggested that there is an ideal number of component classifiers for an ensemble such that having more or less than this number of classifiers would deteriorate the accuracy. It is called __"the law of diminishing returns in ensemble construction"__. Their theoretical framework shows that [using the same number of independent component classifiers as class labels gives the highest accuracy](https://arxiv.org/pdf/1709.02925.pdf).  
    <br>

8. **Notes:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18}  
    * Averaging models __increases capacity__.  


    __Ensemble Averaging:__{: style="color: red"}  
    Relies 

***

## Bayes optimal classifier (Theoretical)
{: #content2}

1. **Bayes Optimal Classifier:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    [Bayes Optimal Classifier](https://en.wikipedia.org/wiki/Ensemble_learning#Bayes_optimal_classifier)  
    <br>

***

## Bootstrap Aggregating (Bagging)
{: #content3}

1. **Bootstrap Aggregating (Bagging):**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}  
    __Bootstrap Aggregating (Bagging)__ is an ensemble meta-algorithm designed to improve the stability and accuracy of ml algorithms. It is designed to __reduce variance__ and help to __avoid overfitting__.  

    It is applicable to both __classification__ and __regression__ problems.  
    
    Although it is usually applied to __decision tree methods__, it can be used with any type of method. Bagging is a special case of the model averaging approach.  
    <br>

2. **Bootstrapping:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}  
    __Bootstrapping__ is a sampling technique. From a set $$D$$ of $$n$$ sample points, it constructs $$m$$ subsets $$D_i$$, each of size $$n'$$, by sampling from $$D$$ __uniformly__{: style="color: goldenrod"} and __with replacement__{: style="color: goldenrod"}.  
    * By sampling with replacement, __some observations may be repeated__ in each $${\displaystyle D_{i}}$$.  
    * If $$n'=n$$, then for large $$n$$ the set $$D_{i}$$ is expected to have the fraction ($$1 - 1/e$$) ($$\approx 63.2\%$$) of the unique examples of $$D$$, the rest being duplicates.  

    The point of sampling with replacement is to make the re-sampling truly random. If done without replacement, the samples drawn will be dependent on the previous ones and thus not be random.  
    <br>

3. **Aggregating:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}  
    The predictions from the above models are aggregated to make a final combined prediction. This aggregation can be done on the basis of predictions made or the probability of the predictions made by the bootstrapped individual models.  
    <br>


4. **The Algorithm:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents34}  
    Bagging uses multiple weak models and aggregates the predictions from each of them to get the final prediction. The weak models should be such that each specialize in a particular part of the feature space thus enabling us to leverage predictions from each model to maximum use. As suggested by the name, it consists of two parts, bootstrapping and aggregation.  

    * Given a set $$D$$ of $$n$$ sample points, 
    * __Bootstrapping:__ Construct $$m$$ __bootstap samples__ (subsets) $$D_i$$.  
    * Fit $$m$$ models using the $$m$$ bootstrap samples
    * __Aggregating:__ Combine the models by:  
        * __Regression__: <span>Averaging</span>{: style="color: goldenrod"}  
        * __Classification__: <span>Voting</span>{: style="color: goldenrod"}  
    <br>

    [Bagging and Random Forests (Shewchuk)](https://people.eecs.berkeley.edu/~jrs/189/lec/16.pdf)  

5. **Advantages:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents35}  
    * Improves __"unstable" procedures__  
    * Reduces variance $$\rightarrow$$ helps avoid overfitting  
    * Ensemble models can be used to capture the linear as well as the non-linear relationships in the data.This can be accomplished by using 2 different models and forming an ensemble of the two.  
    <br>

6. **Disadvantages:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents36}  
    * On the other hand, it can mildly degrade the performance of "stable" methods such as K-NN  
    * It causes a Reduction in the interpretability of the model  
    * Prone to high bias if not modeled properly  
    * Though improves accuracy, it is computationally expensive and hard to design:  
        It is not good for real time applications.    
    <br>

7. **Examples (bagging algorithms):**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents37}  
    * __Random Forests:__ is a bagging algorithm that further reduces variance by selecting a __subset of features__   
        1. Suppose there are N observations and M features. A sample from observation is selected randomly with replacement(Bootstrapping).
        1. A subset of features are selected to create a model with sample of observations and subset of features.
        1. Feature from the subset is selected which gives the best split on the training data.(Visit my blog on Decision Tree to know more of best split)
        1. This is repeated to create many models and every model is trained in parallel
        Prediction is given based on the aggregation of predictions from all the models.
    <br>

***

## Boosting
{: #content4}

1. **Boosting:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents41}  
    __Boosting__ is an ensemble meta-algorithm for primarily __reducing bias__, but _also variance_ in supervised learning. It belongs to a family of machine learning algorithms that __convert weak learners to strong ones__.  

    It is an __iterative__ technique which adjusts the weight of an observation based on the last classification. If an observation was classified incorrectly, it tries to increase the weight of this observation and vice versa. Thus, <span>future weak learners focus more on the examples that previous weak learners misclassified</span>{: style="color: goldenrod"}.  

    Boosting in general decreases the bias error and builds strong predictive models. However, they may sometimes over fit on the training data.  

    Boosting *__increases the capacity__*.  

    __Summary__{: style="color: red"}  
    __Boosting__: create different hypothesis $$h_i$$s sequentially + make each new hypothesis __decorrelated__ with previous hypothesis.  
    * Assumes that this will be combined/ensembled  
    * Ensures that each new model/hypothesis will give a different/independent output  
    <br>

2. **Motivation - "The Hypothesis Boosting Problem":**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents42}  
    Boosting is based on a question posed by _Kearns_ and _Valiant_ (1988):  
    > <span>"Can a set of __weak learners__ create a _single_ __strong learner__?":</span>{: style="color: blue"}  

    This question was formalized as a hypothesis called "The Hypothesis Boosting Problem".  

    __The Hypothesis Boosting Problem:__{: style="color: red"}  
    Informally, [the hypothesis boosting] problem asks whether an efficient learning algorithm […] that outputs a hypothesis whose performance is only slightly better than random guessing [i.e. a weak learner] implies the existence of an efficient algorithm that outputs a hypothesis of arbitrary accuracy [i.e. a strong learner].  


    * A __weak learner__ is defined to be a classifier that is only slightly correlated with the true classification (it can label examples better than random guessing).  
    * A __strong learner__ is a classifier that is arbitrarily well-correlated with the true classification.  
    <br>

    __Countering BAgging Limitations:__{: style="color: red"}  
    Bagging suffered from some limitations; namely, that the models can be dependent/correlated which cause the voting to be trapped in the wrong hypothesis of the weak learners. This  motivated the intuition behind Boosting:  
    * Instead of training parallel models, one needs to train models sequentially &
    * Each model should focus on where the previous classifier performed poorly  
    <br>

3. **Boosting Theory and Convexity:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents43}  
    Only algorithms that are provable boosting algorithms in the __probably approximately correct (PAC) learning__ formulation can accurately be called boosting algorithms. Other algorithms that are similar in spirit to boosting algorithms are sometimes called __"leveraging algorithms"__, although they are also sometimes incorrectly called boosting algorithms.  
    <br>

    __Convexity:__{: style="color: red"}  
    Boosting algorithms can be based on convex or non-convex optimization algorithms:  
    * __Convex Algorithms__:  
        such as __AdaBoost__ and __LogitBoost__, can be <span>"defeated" by random noise</span>{: style="color: goldenrod"} such that they can't learn basic and learnable combinations of weak hypotheses.  
        This limitation was pointed out by _Long & Servedio_ in _2008_.   
    * __Non-Convex Algorithms__:  
        such as __BrownBoost__, was shown to be able to learn from noisy datasets and can specifically learn the underlying classifier of the _"Long–Servedio dataset"_.  
    <br>

33. **The Boosting MetaAlgorithm:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents433}  
    * __Finding (defining) Weak Learners__:  
        The algorithm defines weak learners as those that have __weak rules__ (rules that are not powerful enough for accurate classification)    
    * __Identifying Weak Rules:__  
        * To find weak rule, we apply base learning (ML) algorithms with a different distribution. Each time base learning algorithm is applied, it generates a new weak prediction rule. This is an iterative process. After many iterations, the boosting algorithm combines these weak rules into a single strong prediction rule.
    * __Choosing different distribution for each round:__  
        1. The base learner takes all the distributions and assign equal weight or attention to each observation.
        2. If there is any prediction error caused by first base learning algorithm, then we pay higher attention to observations having prediction error. Then, we apply the next base learning algorithm.
        3. Iterate Step 2 till the limit of base learning algorithm is reached or higher accuracy is achieved.
    * __Aggregating Outputs:__  
        Finally, it combines the outputs from weak learner and creates a strong learner which eventually improves the prediction power of the model. Boosting pays higher focus on examples which are mis-classiﬁed or have higher errors by preceding weak rules.  
    <br>


44. **Boosting Algorithms:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents444}  
    * AdaBoost (Adaptive Boosting)
    * Gradient Tree Boosting
    * XGBoost
    <br>

4. **The AdaBoost Algorithm - Adaptive Boosting:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents44}  
    __AdaBoost:__ It works on similar method as discussed above. It fits a sequence of weak learners on different weighted training data. It starts by predicting original data set and gives equal weight to each observation. If prediction is incorrect using the first learner, then it gives higher weight to observation which have been predicted incorrectly. Being an iterative process, it continues to add learner(s) until a limit is reached in the number of models or accuracy.

    Mostly, we use decision stamps with AdaBoost. But, we can use any machine learning algorithms as base learner if it accepts weight on training data set. We can use AdaBoost algorithms for both classification and regression problem.  


    * [The AdaBoost Boosting Algorithm in detail](https://maelfabien.github.io/machinelearning/adaboost/#the-limits-of-bagging)  
    * [AdaBoost (Shewchuk)](https://people.eecs.berkeley.edu/~jrs/189/lec/24.pdf)  
    * [Boosting (MIT Lecture)](https://www.youtube.com/watch?v=UHBmv7qCey4)  
    <br>

    __Notes:__{: style="color: red"}  
    * order of trees matter in AdaBoost  
    <br>
            

5. **Advantages:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents45}  
    * Decreases the Bias  
    * Better accuracy over Bagging (e.g. Random Forest)  
    * Boosting can lead to learning complex non-linear decision boundaries   
    * [Why does Gradient boosting work so well for so many Kaggle problems? (Quora!)](https://www.quora.com/Why-does-Gradient-boosting-work-so-well-for-so-many-Kaggle-problems)  
    <br>

6. **Disadvantages:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents46}  
    * Reduced interpretability  
    * Harder to tune than other models, because you have so many hyperparameters and you can __easily overfit__  
    * Computationally expensive for training (sequential) and inference   
    <br>

8. **Bagging VS Boosting:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents48}   
    ![Bagging VS Boosting](https://cdn.mathpix.com/snip/images/fBJbH_Ej-9puFnO9piKuoN5ULBmPkMIbnhA6Qo64CU8.original.fullsize.png){: width="80%"}  

***

## Stacking
{: #content5}

1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents51}  

<!-- 2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents52}  

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents53}  

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents54}  

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents55}  

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents56}  

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents57}  

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents58}   -->

*** 

<!-- ## Sixth
{: #content6}

1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents61}   -->

<!-- 2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents62}  

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents63}  

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents64}   -->