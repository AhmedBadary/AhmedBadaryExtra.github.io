---
layout: NotesPage
title: Text Classification
permalink: /work_files/research/nlp/txt_clss
prevLink: /work_files/research/nlp.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Introduction and Definitions](#content1)
  {: .TOC1}
  * [The Naive Bayes Classifier](#content2)
  {: .TOC2}
  * [Evalutaion of Text Classification](#content3)
  {: .TOC3}
  * [General Discussion of Issues in Text Classification](#content4)
  {: .TOC4}
</div>

***
***

* [Googles Text Classification Guide (Blog)](https://developers.google.com/machine-learning/guides/text-classification)  

## Introduction and Definitions
{: #content1}

1. **Text Classification:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}   
    :    The task of assigning a piece of text to one or more classes or categories.  

2. **Applications:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    * __Spam Filtering__: discerning spam emails form legitimate emails.  
    * __Email Routing__: sending an email sento to a genral address to a specfic affress based on the topic.  
    * __Language Identification__: automatiacally determining the genre of a piece of text.  
    * Readibility Assessment__: determining the degree of readability of a piece of text.  
    * __Sentiment Analysis__: determining the general emotion/feeling/attitude of the author of a piece of text.  
    * __Authorship Attribution__: determining which author wrote which piece of text.  
    * __Age/Gender Identification__: determining the age and/or gender of the author of a piece of text.      

3. **Classification Methods:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    :   * __(Hand-Coded)Rules-Based Algorithms__: use rules based on combinations of words or other features.   
            * Can have high accuracy if the rules are carefully refined and maintained by experts.  
            * However, building and maintaining these rules is very hard.  
        * __Supervised Machine Learning__: using an ML algorithm that trains on a training set of (document, class) elements to train a classifier.  
            * _Types of Classifiers_:  
                * Naive Bayes  
                * Logistic Regression
                * SVMs
                * K-NNs  
   
***

## The Naive Bayes Classifier
{: #content2}

1. **Naive Bayes Classifiers:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}   
    :   are a family of simple probabilistic classifiers based on applying [_Bayes' Theorem_](https://en.wikipedia.org/wiki/Bayes%27_theorem) with strong (naive) independence assumptions between the features.  
    :   __The Probabilistic Model__:  
        Abstractly, naive Bayes is a conditional probability model: given a problem instance to be classified, represented by a vector $${\displaystyle \mathbf{x} =(x_{1},\dots ,x_{n})}=(x_{1},\dots ,x_{n})$$ representing some n features (independent variables), it assigns to this instance probabilities  
    :   $${\displaystyle p(C_{k}\mid x_{1},\dots ,x_{n})\,}$$
    :   for each of the $$k$$ possible outcome or classes $$C_k$$.  
    :   Now, using _Bayes' Theorem_ we decompose the conditional probability as:  
    :   $${\displaystyle p(C_{k}\mid \mathbf {x} )={\frac {p(C_{k})\ p(\mathbf {x} \mid C_{k})}{p(\mathbf {x} )}}\,}$$
    :   Or, equivalenty, and more intuitively:  
    :   $${\displaystyle {\mbox{posterior}}={\dfrac{\text{prior} \times \text{likelihood}}{\text{evidence}}}\,}$$  
    :   We can disregard the _Denomenator_ since it does __not__ depend on the classes $$C$$, making it a constant.  
    :   Now, using the _Chain-Rule_ for repeated application of the conditional probability,   the joint probability model can be rewritten as:  
    :   $$p(C_{k},x_{1},\dots ,x_{n})\, = p(x_{1}\mid x_{2},\dots ,x_{n},C_{k})p(x_{2}\mid x_{3},\dots ,x_{n},C_{k})\dots p(x_{n-1}\mid x_{n},C_{k})p(x_{n}\mid C_{k})p(C_{k})$$  
    :   Applying the naive conditional independence assumptions,  
        >   i.e. assume that each feature $${\displaystyle x_{i}}$$ is conditionally independent of every other feature $${\displaystyle x_{j}} $$ for $${\displaystyle j\neq i}$$, given the category $${\displaystyle C}$$  
    :   $$\implies \\ 
    {\displaystyle p(x_{i}\mid x_{i+1},\dots ,x_{n},C_{k})=p(x_{i}\mid C_{k})\,}.$$
    :   Thus, we can write the join probability model as:  
    :   $${\displaystyle p(C_{k}\mid x_{1},\dots ,x_{n})={\frac {1}{Z}}p(C_{k})\prod _{i=1}^{n}p(x_{i}\mid C_{k})}$$
    :   Where, $${\displaystyle Z=p(\mathbf {x} )=\sum _{k}p(C_{k})\ p(\mathbf {x} \mid C_{k})}$$ is a __constant__ scaling factor, a function of the, _known_, feature variables.  

    :   __The Decision Rule__: we commonly use the [_Maximum A Posteriori (MAP)_](https://en.wikipedia.org/wiki/Maximum_a_posteriori_estimation) hypothesis, as the decision rule.  
    :   Thus, __the classifier__ becomes:  
    :   $${\displaystyle {\hat {y}}={\underset {k\in \{1,\dots ,K\}}{\operatorname {argmax} }}\ p(C_{k})\displaystyle \prod _{i=1}^{n}p(x_{i}\mid C_{k}).}$$
    :   A function that assigns a class label $${\displaystyle {\hat {y}}=C_{k}}$$ for some $$k$$.

2. **Multinomial Naive Bayes:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}   
    :   With a multinomial event model, samples (feature vectors) represent the frequencies with which certain events have been generated by a multinomial $${\displaystyle (p_{1},\dots ,p_{n})}$$ where $${\displaystyle p_{i}}$$ is the probability that event $$i$$ occurs.  
    :   The likelihood of observing a feature vector (histogram) $$\mathbf{x}$$ is given by:  
    :   $${\displaystyle p(\mathbf {x} \mid C_{k})={\frac {(\sum _{i}x_{i})!}{\prod _{i}x_{i}!}}\prod _{i}{p_{ki}}^{x_{i}}}$$  
    :   The multinomial naive Bayes classifier becomes a linear classifier when expressed in log-space:  
    :   $${\displaystyle {\begin{aligned}\log p(C_{k}\mid \mathbf {x} )&\varpropto \log \left(p(C_{k})\prod _{i=1}^{n}{p_{ki}}^{x_{i}}\right)\\&=\log p(C_{k})+\sum _{i=1}^{n}x_{i}\cdot \log p_{ki}\\&=b+\mathbf {w} _{k}^{\top }\mathbf {x} \end{aligned}}}$$  
    :   where $${\displaystyle b=\log p(C_{k})}$$ and $${\displaystyle w_{ki}=\log p_{ki}}$$.  

3. **Bag-of-Words:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}   
    :   The __bag-of-words model__ (or __vector-space-model__) is a simplifying representation of text/documents.  
    :   A text is represented as the bag (Multi-Set) of its words with multiplicity, disregarding any grammatrical rules and word-orderings.

4. **The Simplifying Assumptions Used:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}   
    :   * __Bag-of-Words__: we assume that the position of the words does _not_ matter.  
        * __Naive Independence__: the feature probabilities are indpendenet given a class $$c$$.   

5. **Learning the Multi-Nomial Naive Bayes Model:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}   
    :   * __The Maximum Likelihood Estimate__: we simply use the frequencies in the date.
            * $$\hat{P}(c_j) = \dfrac{\text{doc-count}(C=c_j)}{N_\text{doc}}$$  
            > The _Prior Probability_ of a document being in class $$c_j$$, is the fraction of the documents in the training data that are in class $$c_j$$.  
            * $$\hat{P}(w_i | c_i) = \dfrac{\text{count}(w_i,c_j)}{\sum_{w \in V} \text{count}(w, c_j)}$$  
            > The _likelihood_ of the word $$w_i$$ given a class $$c_j$$, is the fraction of the occurunces of the word $$w_i$$ in class $$c_j$$ over all words in the class.    
    :   * __The Problem with Maximum Likelihood__:  
            If a certain word occurs in the test-set but __not__ in the training set, the likelihood of that word given the equation above will be set to $$0$$.  
            Now, since we are multiplying all the likelihood terms together, the MAP estimate will be set to $$0$$ as well, regardless of the other values.  

6. **Solutions to the MLE Problem:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents26}   
    :   Usually the problem of reducing the estimate to zero is solved by adding a regularization technique known as _smoothing_. 

7. **Lidstone Smoothing (additive smoothing):**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents27}   
    :   is a technique used to smooth categorical data as the following:  
    :   Given an observation vector $$x = (x_1, \ldots, x_d)$$ from a multinomial distribution with $$N$$ trials, a _smoothed_ version of the data produces the estimators:  
    :   $${\hat {\theta }}_{i}={\frac {x_{i}+\alpha }{N+\alpha d}}\qquad (i=1,\ldots ,d),$$


8. **Laplace Smoothing:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents28}   
    :   is a special case of additive smoothing (Lidstone Smoothing) with $$\alpha = 1$$:  
    :   $${\hat {\theta }}_{i}={\frac {x_{i}+1 }{N+ d}}\qquad (i=1,\ldots ,d),$$   
9. **The Algorithm:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents29}  
    :   * Extract the _Vocabulary_ from the trianing data  
        * Calculate $$P(c_j)$$ terms  
            * For each $$c_j \in C$$ do  
                * $$\text{docs}_j \leftarrow$$ all docs with class $$=c_j$$  
                * $$P(c_j) \leftarrow \dfrac{\|\text{docs}_j\|}{\|\text{total # docs}\|}$$
        * Calculate $$P(w_k \| c_j)$$ terms  
            * $$\text{Text}_j \leftarrow$$ single doc containing all $$\text{docs}_j$$  
            * For each word $$w_k \in$$ Vocab.  
                * $$n_k \leftarrow$$ # of occurunces of $$w_k \in \text{Text}_j$$  
                * $$P(w_k \| c_j) \leftarrow \dfrac{n_k + \alpha}{n + \alpha \|Vocab.\|}$$  
10. **Summary:**{: style="color: SteelBlue"}{: .bodyContents210}  
    :   * Very fast  
        * Low storage requirements
        * Robust to Irrelevant Features  
            * Irrelevant features cancel each other out.  
        * Works well in domains with many equally important features  
            * Decision Trees_ suffer from fragmentation in such cases - especially if there is little data.  
        * It is _Optimal_ if the independence conditions hold.  

***

## Evaluation of Text Classification  
{: #content3}

1. **The $$2x2$$ Contingency Table:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}  
    :   | | __correct__ (Spam) | __not correct__ (not Spam)    
        __selected__ (Spam) | tp | fp  
        __not selected__ (not Spam) | fn | tn  

2. **Accuracy:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}   
    :   $$ \text{Acc} = \dfrac{\text{tp} + \text{tn}}{\text{tp} + \text{fp} + \text{fn} + \text{tn}}$$
    :   __The Problem__:  
        Accuracy can be easily fooled (i.e. produce a very high number) in a scenario where the number of occurrences of a class we desire is much less than the data we are searching.  

3. **Precision (positive predictive value (PPV)):**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}  
    :   is the fraction of relevant instances among the retrieved instances.  
    :   __Equivalently__,  
        the % of selected items that are correct.    

    :   $${\displaystyle {\text{Precision}}={\frac {tp}{tp+fp}}\,}$$     

4. **Recall (True Positive Rate), (Sensitivity):**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents34}  
    :   Also referred to as the __true positive rate__ or __sensitivity__. 
    :    is the fraction of relevant instances that have been retrieved over the total amount of relevant instances.  
    :   __Equivalently__,  
        the % of correct items that are selected.  
    :   $${\displaystyle {\text{Recall}}={\frac {tp}{tp+fn}}\,}$$

5. **The Trade-Off:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents35}   
    :   Usually, the two measures discusses above have an inverse relation between them due to the quantities they measure.  

6. **The F-measure:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents36}   
    :   is a measure that combines _precision_ and _recall_.  
    :   It is the _harmonic mean_ of precision and recall:  
    :   $${\displaystyle F=2\cdot {\frac {\mathrm {precision} \cdot \mathrm {recall} }{\mathrm {precision} +\mathrm {recall} }}}$$ 
   
***

## General Discussion of Issues in Text Classification
{: #content4}

1. **Very Little Data:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents41}   
    :   * Use Naive Bayes  
            * Naive Bayes is a "high-bias" algorithm; it tends to __not__ overfit the data.  
        * Use Semi-Supervised Learning  
            * Try Bootstrapping or EM over unlabeled documents  

2. **Reasonable Amount of Data:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents42}   
    :   * Use:  
            * SVM  
            * Regularized Logistic Regression  
            * (try) Decision Trees  

3. **Huge Amount of Data:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents43}   
    :   Be careful of the run-time:  
        * SVM: slow train time  
        * KNN: slow test time  
        * Reg. Log. Regr.: somewhat faster  
        * Naive-Bayes: might be good to be used.

4. **Underflow Prevention:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents44}   
    :   __Problem:__ Due to the "_multiplicative_" nature of the algorithms we are using, we might run into a floating-point underflow problem.  
    :   __Solution__: transfer the calculations to the _log-space_ where all the multiplications are transformed into additions.  

5. **Tweaking the Performance of the Algorithms:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents45}   
    :   * Utilize __*Domain-Specific* features__ and weights  
        * __Upweighting__: counting a word as if it occurred multiple times.  
   