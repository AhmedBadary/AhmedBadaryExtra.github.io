---
layout: NotesPage
title: Prep Questions (Learning)
permalink: /work_files/research/prep_qs
prevLink: /work_files/research.html
---



## Gradient-Based Optimization
* __Define Gradient Methods:__{: style="color: red"}  

* __Give examples of Gradient-Based Algorithms:__{: style="color: red"}  
* __What is Gradient Descent:__{: style="color: red"}  
* __Explain it intuitively:__{: style="color: red"}  
* __Give its derivation:__{: style="color: red"}  
* __What is the learning rate?__{: style="color: red"}  
    * __Where does it come from?__{: style="color: blue"}  

    <button>Show</button>{: .showText value="show"
    onclick="showText_withParent_PopHide(event);"}
    * __How does it relate to the step-size?__{: style="color: blue"}  
    * __We go from having a fixed step-size to [blank]:__{: style="color: blue"}  
    {: hidden=""}

    * __How do we choose the learning rate?__{: style="color: blue"}  

    <button>Show</button>{: .showText value="show"
    onclick="showText_withParent_PopHide(event);"}
    * __Compare Line Search vs Trust Region:__{: style="color: blue"}  
    {: hidden=""}
* __Describe the convergence of the algorithm:__{: style="color: red"}  
* __How does GD relate to Euler?__{: style="color: red"}  

* __List the variants of GD:__{: style="color: red"}  
    * __How do they differ?:__{: style="color: blue"}  

    <button>Define the Following w/ parameter updates:</button>{: .showText value="show"
    onclick="showText_withParent_PopHide(event);"}
    * __BGD:__{: style="color: blue"}  
    * __SGD:__{: style="color: blue"}  
        * __How should we handle the lr in this case? Why?__{: style="color: blue"}  
        * __What conditions guarantee convergence of SGD?__{: style="color: blue"}  

    * __M-BGD:__{: style="color: blue"}  
        * __What advantages does it have?__{: style="color: blue"}  

    * __Explain the different kinds of gradient-descent optimization procedures:__{: style="color: blue"}  
        1. __Batch Gradient Descent__ AKA __Vanilla Gradient Descent__, computes the gradient of the objective wrt. the parameters $$\theta$$ for the entire dataset:  
            <p>$$\theta=\theta-\epsilon \cdot \nabla_{\theta} J(\theta)$$</p>  
        2. __SGD__ performs a parameter update for each data-point:  
            <p>$$\theta=\theta-\epsilon \cdot \nabla_{\theta} J\left(\theta ; x^{(i)} ; y^{(i)}\right)$$</p>  
        3. __Mini-batch Gradient Descent__ a hybrid approach that perform updates for a, pre-specified, mini-batch of $$n$$ training examples:  
            <p>$$\theta=\theta-\epsilon \cdot \nabla_{\theta} J\left(\theta ; x^{(i : i+n)} ; y^{(i : i+n)}\right)$$</p>  
    * __State the difference between SGD and GD?__{: style="color: blue"}  
        __Gradient Descent__’s cost-function iterates over ALL training samples.  
        __Stochastic Gradient Descent__’s cost-function only accounts for ONE training sample, chosen at random.  
    * __When would you use GD over SDG, and vice-versa?__{: style="color: blue"}  
        GD theoretically minimizes the error function better than SGD. However, SGD converges much faster once the dataset becomes large.  
        That means GD is preferable for small datasets while SGD is preferable for larger ones.  
    {: hidden=""}

* __What is the problem of vanilla approaches to GD?__{: style="color: red"}  
    <button>Show</button>{: .showText value="show"
    onclick="showTextPopHide(event);"}
    * __List the challenges that account for the problem above:__{: style="color: blue"}  
    {: hidden=""}
* __List the different strategies for optimizing GD:__{: style="color: red"}  
* __List the different variants for optimizing GD:__{: style="color: red"}  

<button>Show</button>{: .showText value="show"
onclick="showText_withParent_PopHide(event);"}
* __Momentum:__{: style="color: red"}  
    * __Motivation:__{: style="color: blue"}  
    * __Definitions/Algorithm:__{: style="color: blue"}  
    * __Intuition:__{: style="color: blue"}  
    * __Parameter Settings:__{: style="color: blue"}  
* __Nesterov Accelerated Gradient (Momentum):__{: style="color: red"}  
    * __Motivation:__{: style="color: blue"}  
    * __Definitions/Algorithm:__{: style="color: blue"}  
    * __Intuition:__{: style="color: blue"}  
    * __Parameter Settings:__{: style="color: blue"}  
    * __Successful Applications:__{: style="color: blue"}  
* __Adagrad__{: style="color: red"}  
    * __Motivation:__{: style="color: blue"}  
    * __Definitions/Algorithm:__{: style="color: blue"}  
    * __Intuition:__{: style="color: blue"}  
    * __Parameter Settings:__{: style="color: blue"}  
    * __Successful Application:__{: style="color: blue"}  
    * __Properties:__{: style="color: blue"}  
* __Adadelta__{: style="color: red"}  
    * __Motivation:__{: style="color: blue"}  
    * __Definitions/Algorithm:__{: style="color: blue"}  
    * __Intuition:__{: style="color: blue"}  
    * __Parameter Settings:__{: style="color: blue"}  
    * __Properties:__{: style="color: blue"}  
* __RMSprop__{: style="color: red"}  
    * __Motivation:__{: style="color: blue"}  
    * __Definitions/Algorithm:__{: style="color: blue"}  
    * __Intuition:__{: style="color: blue"}  
    * __Parameter Settings:__{: style="color: blue"}  
    * __Properties:__{: style="color: blue"}  
* __Adam__{: style="color: red"}  
    * __Motivation:__{: style="color: blue"}  
    * __Definitions/Algorithm:__{: style="color: blue"}  
    * __Intuition:__{: style="color: blue"}  
    * __Parameter Settings:__{: style="color: blue"}  
    * __Properties:__{: style="color: blue"}  
* __Which methods have trouble with saddle points?__{: style="color: red"}  
* __How should you choose your optimizer?__{: style="color: red"}  
* __Summarize the different variants listed above. How do they compare to each other?__{: style="color: red"}  
* __What's a common choice in many research papers?__{: style="color: red"}  

* __List additional strategies for optimizing SGD:__{: style="color: red"}  
{: hidden=""}



***

## Maximum Margin Classifiers
1. __Define Margin Classifiers:__{: style="color: red"}  
1. __What is a Margin for a linear classifier?__{: style="color: red"}  
1. __Give the motivation for margin classifiers:__{: style="color: red"}  
1. __Define the notion of the "best" possible classifier__{: style="color: red"}  
1. __How can we achieve the "best" classifier?__{: style="color: red"}  
1. __What unique vector is orthogonal to the hp? Prove it:__{: style="color: red"}  
1. __What do we mean by "signed distance"? Derive its formula:__{: style="color: red"}  
1. __Given the formula for signed distance, calculate the "distance of the point closest to the hyperplane":__{: style="color: red"}  
1. __Use geometric properties of the hp to Simplify the expression for the distance of the closest point to the hp, above__{: style="color: red"}  
1. __Characterize the margin, mathematically:__{: style="color: red"}  
1. __Characterize the "Slab Existence":__{: style="color: red"}  
1. __Formulate the optimization problem of *maximizing the margin* wrt analysis above:__{: style="color: red"}  
1. __Reformulate the optimization problem above to a more "friendly" version (wrt optimization -> put in standard form):__{: style="color: red"}  
    1. __Give the final (standard) formulation of the "Optimization problem for maximum margin classifiers":__{: style="color: blue"}  
    1. __What kind of formulation is it (wrt optimization)? What are the parameters?__{: style="color: blue"}  

***

## Hard-Margin SVMs
1. __Define:__{: style="color: red"}  
    1. __SVMs:__{: style="color: blue"}  
    1. __Support Vectors:__{: style="color: blue"}  
    1. __Hard-Margin SVM:__{: style="color: blue"}  
1. __Define the following wrt hard-margin SVM:__{: style="color: red"}  
    1. __Goal:__{: style="color: blue"}  
    1. __Procedure:__{: style="color: blue"}  
    1. __Decision Function:__{: style="color: blue"}  
    1. __Constraints:__{: style="color: blue"}  
    1. __The Optimization Problem:__{: style="color: blue"}  
    1. __The Optimization Method:__{: style="color: blue"}  
1. __Elaborate on the generalization analysis:__{: style="color: red"}  
1. __List the properties:__{: style="color: red"}  
1. __Give the solution to the optimization problem for H-M SVM:__{: style="color: red"}  
    1. __What method does it require to be solved:__{: style="color: blue"}  
    1. __Formulate the Lagrangian:__{: style="color: blue"}  
    1. __Optimize the objective for each variable:__{: style="color: blue"}  
    1. __Get the *Dual Formulation* w.r.t. the (_tricky_) constrained variable $$\alpha_n$$:__{: style="color: blue"}  
    1. __Set the problem as a *Quadratic Programming* problem:__{: style="color: blue"}  
    1. __What are the inputs and outputs to the Quadratic Program Package?__{: style="color: blue"}  
    1. __Give the final form of the optimization problem in standard form:__{: style="color: blue"}  

***

## Soft-Margin SVM
1. __Motivate the soft-margin SVM:__{: style="color: red"}  
1. __What is the main idea behind it?__{: style="color: red"}  
1. __Define the following wrt soft-margin SVM:__{: style="color: red"}  
    1. __Goal:__{: style="color: blue"}  
    1. __Procedure:__{: style="color: blue"}  
    1. __Decision Function:__{: style="color: blue"}  
    1. __Constraints:__{: style="color: blue"}  
        1. __Why is there a non-negativity constraint?__{: style="color: blue"}     
    1. __Objective/Cost Function:__{: style="color: blue"}  
    1. __The Optimization Problem:__{: style="color: blue"}  
    1. __The Optimization Method:__{: style="color: blue"}  
    1. __Properties:__{: style="color: blue"}  
1. __Specify the effects of the regularization hyperparameter $$C$$:__{: style="color: red"}  
    1. __Describe the effect wrt over/under fitting:__{: style="color: blue"}   
1. __How do we choose $$C$$?__{: style="color: red"}  
1. __Give an equivalent formulation in the standard form objective for function estimation (what should it minimize?)__{: style="color: red"}  

***

## Loss Functions
1. __Define:__{: style="color: red"}  
    1. __Loss Functions:__{: style="color: blue"}  
    1. __Distance-Based Loss Functions:__{: style="color: blue"}  
        1. __Describe an important property of dist-based losses:__{: style="color: blue"}  
        1. __What are they used for?__{: style="color: blue"}  
    1. __Relative Error - What does it lack?__{: style="color: blue"}  
1. __List 3 Regression Loss Functions__{: style="color: red"}  

<button>Show the rest of the questions</button>{: .showText value="show"
onclick="showText_withParent_PopHide(event);"}
1. __MSE__{: style="color: red"}  
    1. __What does it minimize:__{: style="color: blue"}  
    1. __Formula:__{: style="color: blue"}  
    1. __Graph:__{: style="color: blue"}  
    1. __Derivation:__{: style="color: blue"}  
1. __MAE__{: style="color: red"}  
    1. __What does it minimize:__{: style="color: blue"}  
    1. __Formula:__{: style="color: blue"}  
    1. __Graph:__{: style="color: blue"}  
    1. __Derivation:__{: style="color: blue"}  
    1. __List properties:__{: style="color: blue"}  
1. __Huber Loss__{: style="color: red"}  
    1. __AKA:__{: style="color: blue"}  
    1. __Formula:__{: style="color: blue"}  
    1. __Graph:__{: style="color: blue"}  
    1. __Derivation:__{: style="color: blue"}  
    1. __List properties:__{: style="color: blue"}  
1. __Analyze MSE vs MAE:__{: style="color: red"}  
{: hidden=""}

1. __List 7 Classification Loss Functions__{: style="color: red"}  

<button>Show the rest of the questions</button>{: .showText value="show"
onclick="showText_withParent_PopHide(event);"}
1. __$$0-1$$ loss__{: style="color: red"}  
    1. __What does it minimize:__{: style="color: blue"}  
    1. __Formula:__{: style="color: blue"}  
    1. __Graph:__{: style="color: blue"}  
1. __MSE__{: style="color: red"}  
    1. __Formula:__{: style="color: blue"}  
    1. __Graph:__{: style="color: blue"}  
    1. __Derivation (for classification) - give assumptions:__{: style="color: blue"}  
    1. __Properties:__{: style="color: blue"}  
1. __Hinge Loss__{: style="color: red"}  
    1. __What does it minimize:__{: style="color: blue"}  
    1. __Formula:__{: style="color: blue"}  
    1. __Graph:__{: style="color: blue"}  
    1. __Describe the Properties of the Hinge loss and why it is used?__{: style="color: blue"}  
1. __Logistic Loss__{: style="color: red"}
    1. __AKA:__{: style="color: blue"}    
    1. __What does it minimize:__{: style="color: blue"}  
    1. __Formula:__{: style="color: blue"}  
    1. __Graph:__{: style="color: blue"}  
    1. __Derivation:__{: style="color: blue"}  
    1. __Properties:__{: style="color: blue"}  
1. __Cross-Entropy__{: style="color: red"}  
    1. __What does it minimize:__{: style="color: blue"}  
    1. __Formula:__{: style="color: blue"}  
    1. __Binary Cross-Entropy:__{: style="color: blue"}  
    1. __Graph:__{: style="color: blue"}  
    1. __CE and Negative-Log-Probability:__{: style="color: blue"}  
    1. __CE and Log-Loss:__{: style="color: blue"}  
        1. __Derivation:__{: style="color: blue"}  
    1. __CE and KL-Div:__{: style="color: blue"}  
1. __Exponential Loss__{: style="color: red"}  
    1. __Formula:__{: style="color: blue"}  
    1. __Properties:__{: style="color: blue"}  
1. __Perceptron Loss__{: style="color: red"}  
    1. __Formula:__{: style="color: blue"}  
1. __Analysis__{: style="color: red"}  
    1. __Logistic vs Hinge Loss:__{: style="color: blue"}  
    1. __Cross-Entropy vs MSE:__{: style="color: blue"}  
{: hidden=""}


***

## Information Theory
1. __What is Information Theory? In the context of ML?__{: style="color: red"}  
1. __Describe the Intuition for Information Theory. Intuitively, how does the theory quantify information (list)?__{: style="color: red"}  
1. __Measuring Information - Definitions and Formulas:__{: style="color: red"}  
    1. __In Shannons Theory, how do we quantify *"transmitting 1 bit of information"*?__{: style="color: blue"}  
    1. __What is *the amount of information transmitted*?__{: style="color: blue"}  
    1. __What is the *uncertainty reduction factor*?__{: style="color: blue"}  
    1. __What is the *amount of information in an event $$x$$*?__{: style="color: blue"}  
1. __Define the *Self-Information*:__{: style="color: red"}  
    1. __What is it defined with respect to?__{: style="color: blue"}  
1. __Define *Shannon Entropy* - what is it used for?__{: style="color: red"}  
    1. __Describe how Shannon Entropy relate to distributions with a graph:__{: style="color: blue"}  
1. __Define *Differential Entropy*:__{: style="color: red"}  
1. __How does entropy characterize distributions?__{: style="color: red"}  
1. __Define *Relative Entropy*:__{: style="color: red"}  
    1. __Give an interpretation:__{: style="color: blue"}  
    1. __List the properties:__{: style="color: blue"}  
    1. __Describe it as a distance:__{: style="color: blue"}  
    1. __List the applications of relative entropy:__{: style="color: blue"}  

    <button>Show</button>{: .showText value="show"
    onclick="showText_withParent_PopHide(event);"}
    1. __How does the direction of minimization affect the optimization:__{: style="color: blue"}  
    {: hidden=""}
1. __Define *Cross Entropy*:__{: style="color: red"}  
    1. __What does it measure?__{: style="color: blue"}  
    1. __How does it relate to *relative entropy*?__{: style="color: blue"}  
    1. __When are they equivalent (wrt. optimization)?__{: style="color: blue"}  
1. __Mutual Information:__{: style="color: red"}  
    1. __Definition:__{: style="color: blue"}  
    1. __What does it measure?__{: style="color: blue"}  
    1. __Intuitive Definitions:__{: style="color: blue"}  
    1. __Interpretations XXX:__{: style="color: blue"}   
    1. __Properties:__{: style="color: blue"}  
    1. __Applications:__{: style="color: blue"}  

    <button>Show</button>{: .showText value="show"
    onclick="showText_withParent_PopHide(event);"}
    1. __As KL-Divergence:__{: style="color: blue"}  
    1. __In-terms of PMFs for discrete distributions:__{: style="color: blue"}  
    1. __In terms of PDFs for continuous distributions:__{: style="color: blue"}  
    1. __Relation to PMI:__{: style="color: blue"}  
    {: hidden=""}
1. __Pointwise Mutual Information (PMI):__{: style="color: red"}  
    1. __Definition:__{: style="color: blue"}  
    1. __Relation to MI:__{: style="color: blue"}  

***



## Recommendation Systems
1. __Describe the different algorithms for recommendation systems:__{: style="color: red"}  

***

## Ensemble Learning
1. __What are the two paradigms of ensemble methods?__{: style="color: red"}  
1. __Random Forest VS GBM?__{: style="color: red"}  

***

## Data Processing and Analysis
1. __What are 3 data preprocessing techniques to handle outliers?__{: style="color: red"}  
1. __Describe the strategies to dimensionality reduction:__{: style="color: red"}  
1. __What are 3 ways of reducing dimensionality?__{: style="color: red"}  
1. __List methods for Feature Selection__{: style="color: red"}  
1. __List methods for Feature Extraction__{: style="color: red"}  
1. __How to detect correlation of "categorical variables"?__{: style="color: red"}  
1. __Feature Importance__{: style="color: red"}  
1. __Capturing the correlation between continuous and categorical variable? If yes, how?__{: style="color: red"}  
1. __What cross validation technique would you use on time series data set?__{: style="color: red"}  
1. __How to deal with missing features? (Imputation?)__{: style="color: red"}  
1. __Do you suggest that treating a categorical variable as continuous variable would result in a better predictive model?__{: style="color: red"}  
1. __What are collinearity and multicollinearity?__{: style="color: red"}  
1. __What is data normalization and why do we need it?__{: style="color: red"}  

***

## ML/Statistical Models
1. __What are parametric models?__{: style="color: red"}  
1. __What is a classifier?__{: style="color: red"}  


***

## K-NN

***

## PCA
1. __What is PCA?__{: style="color: red"}  
1. __What is the Goal of PCA?__{: style="color: red"}  
1. __List the applications of PCA:__{: style="color: red"}  
1. __Give formulas for the following:__{: style="color: red"}  
    1. __Assumptions on $$X$$:__{: style="color: blue"}  
    1. __SVD of $$X$$:__{: style="color: blue"}  
    1. __Principal Directions/Axes:__{: style="color: blue"}  
    1. __Principal Components (scores):__{: style="color: blue"}  
    1. __The $$j$$-th principal component:__{: style="color: blue"}  
1. __Describe how to find the principal components:__{: style="color: red"}  
1. __Define the transformation, mathematically:__{: style="color: red"}  
1. __What does PCA produce/result in?__{: style="color: red"}  
    <button>Show</button>{: .showText value="show"
    onclick="showTextPopHide(event);"}
    1. __Finds a lower dimensional subspace spanned by what?:__{: style="color: blue"}  
    1. __Finds a lower dimensional subspace that minimizes what?:__{: style="color: blue"}  
    1. __What does each PC have (properties)?__{: style="color: blue"}  
    1. __What does the procedure find in terms of a "basis"?__{: style="color: blue"}  
    1. __What does the procedure find in terms of axes? (where do they point?):__{: style="color: blue"}  
    {: hidden=""}
1. __Describe the PCA algorithm:__{: style="color: red"}  
    <button>Show specifics</button>{: .showText value="show"
    onclick="showTextPopHide(event);"}
    1. __What Data Processing needs to be done?__{: style="color: blue"}  
    1. __How to compute the Principal Components?__{: style="color: blue"}  
    1. __How do you compute the Low-Rank Approximation Matrix $$X_k$$?__{: style="color: blue"}  
    {: hidden=""}
1. __Describe the Optimality of PCA:__{: style="color: red"}  
1. __List limitations of PCA:__{: style="color: red"}  
1. __Intuition:__{: style="color: red"}  
    <button>Show specifics</button>{: .showText value="show"
    onclick="showTextPopHide(event);"}
    1. __What property of the internal structure of the data does PCA reveal/explain?__{: style="color: blue"}  
    1. __What object does it fit to the data?:__{: style="color: blue"}  
    {: hidden=""}
1. __How does PCA relate to CCA?__{: style="color: red"}  
1. __How does PCA relate to ICA?__{: style="color: red"}  
1. __Should you remove correlated features b4 PCA?__{: style="color: red"}  
1. __How can we measure the "Total Variance" of the data?__{: style="color: red"}  
1. __How can we measure the "Total Variance" of the *projected data*?__{: style="color: red"}  
1. __How can we measure the *"Error in the Projection"*?__{: style="color: red"}  
    1. __What does it mean when this ratio is high?__{: style="color: blue"}  

***


## The Centroid Method
* **Define "The Centroid":**{: style="color: red"}    
* **Describe the Procedure:**{: style="color: red"}    
* **What is the Decision Function:**{: style="color: red"}    
* **Describe the Decision Boundary:**{: style="color: red"}    


***


## K-Means
1. __What is K-Means?__{: style="color: red"}  
1. __What is the idea behind K-Means?__{: style="color: red"}  
1. __What does K-Mean find?__{: style="color: red"}  
1. __Formal Description of the Model:__{: style="color: red"}  
    1. __What is the Objective?__{: style="color: blue"}  
1. __Description of the Algorithm:__{: style="color: red"}  
1. __What is the Optimization method used? What class does it belong to?__{: style="color: red"}  
    <button>Show</button>{: .showText value="show"
    onclick="showTextPopHide(event);"}
    1. __How does the optimization method relate to EM?__{: style="color: blue"}  
    {: hidden=""}
1. __What is the Complexity of the algorithm?__{: style="color: red"}  
1. __Describe the convergence and prove it:__{: style="color: red"}  
1. __Describe the Optimality of the Algorithm:__{: style="color: red"}  
1. __Derive the estimated parameters of the algorithm:__{: style="color: red"}  
    1. __Objective Function:__{: style="color: blue"}  
    1. __Optimization Objective:__{: style="color: blue"}  
    1. __Derivation:__{: style="color: blue"}  
1. __When does K-Means fail to give good results?__{: style="color: red"}  

***

## Naive Bayes
1. __Define:__{: style="color: red"}  
    1. __Naive Bayes:__{: style="color: blue"}  
    1. __Naive Bayes Classifiers:__{: style="color: blue"}  
    1. __Bayes Theorem:__{: style="color: blue"}  
1. __List the assumptions of Naive Bayes:__{: style="color: red"}  
1. __List some properties of Naive Bayes:__{: style="color: red"}  
    <button>Show</button>{: .showText value="show"
    onclick="showTextPopHide(event);"}
    1. __Is it a Bayesian Method or Frequentest Method?__{: style="color: blue"}  
    1. __Is it a Bayes Classifier? What does that mean?:__{: style="color: blue"}  
    {: hidden=""}
1. __Define the Probabilistic Model for the method:__{: style="color: red"}    
    <button>Show</button>{: .showText value="show"
    onclick="showTextPopHide(event);"}
    1. __What kind of model is it?__{: style="color: blue"}  
    1. __What is a conditional probability model?__{: style="color: blue"}  
    1. __Decompose the conditional probability w/ Bayes Theorem:__{: style="color: blue"}  
    1. __How does the new expression incorporate the joint probability model?__{: style="color: blue"}  
    1. __Use the chain rule to re-write the joint probability model:__{: style="color: blue"}  
    1. __Use the Naive Conditional Independence assumption to rewrite the joint model:__{: style="color: blue"}  
    1. __What is the conditional distribution over the class variable $$C_k$$:__{: style="color: blue"}  
    {: hidden=""}
1. __Construct the classifier. What are its components? Formally define it.__{: style="color: red"}  
    <button>Show</button>{: .showText value="show"
    onclick="showTextPopHide(event);"}
    1. __What's the decision rule used?__{: style="color: blue"}  
    1. __List the difference between the Naive Bayes Estimate and the MAP Estimate:__{: style="color: blue"}  
    {: hidden=""}
1. __What are the parameters to be estimated for the classifier?:__{: style="color: red"}  
1. __What method do we use to estimate the parameters?:__{: style="color: red"}  
1. __What are the estimates for each of the following parameters?:__{: style="color: red"}  
    <button>Show</button>{: .showText value="show"
    onclick="showTextPopHide(event);"}
    1. __The prior probability of each class:__{: style="color: blue"}  
    1. __The conditional probability of each feature (word) given a class:__{: style="color: blue"}  
    {: hidden=""}


***


## CNNs
1. __What is a CNN?__{: style="color: red"}  
1. __What are the layers of a CNN?__{: style="color: red"}  
1. __What are the four important ideas and their benefits that the convolution affords CNNs:__{: style="color: red"}  
1. __What is the inspirational model for CNNs:__{: style="color: red"}  
1. __Describe the connectivity pattern of the neurons in a layer of a CNN:__{: style="color: red"}  
1. __Describe the process of a ConvNet:__{: style="color: red"}  
1. __Convolution Operation:__{: style="color: red"}  
    1. __Define:__{: style="color: blue"}  
    1. __Formula (continuous):__{: style="color: blue"}  
    1. __Formula (discrete):__{: style="color: blue"}  
    1. __Define the following:__{: style="color: blue"}  
        1. __Feature Map:__{: style="color: blue"}  
    1. __Does the operation commute?__{: style="color: blue"}  
1. __Cross Correlation:__{: style="color: red"}  
    1. __Define:__{: style="color: blue"}  
    1. __Formulae:__{: style="color: blue"}  
    1. __What are the differences/similarities between convolution and cross-correlation:__{: style="color: blue"}  
1. __Write down the Convolution operation and the cross-correlation over two axes and:__{: style="color: red"}  
    1. __Convolution:__{: style="color: blue"}  
    1. __Convolution (commutative):__{: style="color: blue"}  
    1. __Cross-Correlation:__{: style="color: blue"}  
1. __The Convolutional Layer:__{: style="color: red"}  
    1. __What are the parameters and how do we choose them?__{: style="color: blue"}  
    1. __Describe what happens in the forward pass:__{: style="color: blue"}  
    1. __What is the output of the forward pass:__{: style="color: blue"}  
    1. __How is the output configured?__{: style="color: blue"}  
1. __Spatial Arrangements:__{: style="color: red"}  
    1. __List the Three Hyperparameters that control the output volume:__{: style="color: blue"}  
    1. __How to compute the spatial size of the output volume?__{: style="color: blue"}  
    1. __How can you ensure that the input & output volume are the same?__{: style="color: blue"}  
    1. __In the output volume, how do you compute the $$d$$-th depth slice:__{: style="color: blue"}  
1. __Calculate the number of parameters for the following config:__{: style="color: red"}  
    > Given:  
        1. __Input Volume__:  $$64\times64\times3$$  
        1. __Filters__:  $$15 7\times7$$  
        1. __Stride__:  $$2$$  
        1. __Pad__:  $$3$$  
1. __Definitions:__{: style="color: red"}  
    1. __Receptive Field:__{: style="color: blue"}  
1. __Suppose the input volume has size  $$[ 32 × 32 × 3 ]$$  and the receptive field (or the filter size) is  $$5 × 5$$ , then each neuron in the Conv Layer will have weights to a *\_\_Blank\_\_* region in the input volume, for a total of  *\_\_Blank\_\_* weights:__{: style="color: red"}  
1. __How can we achieve the greatest reduction in the spatial dims of the network (for classification):__{: style="color: red"}  
1. __Pooling Layer:__{: style="color: red"}  
    1. __Define:__{: style="color: blue"}  
    1. __List key ideas/properties and benefits:__{: style="color: blue"}  
    1. __List the different types of Pooling:__{: style="color: blue"}  
        [Answer](http://localhost:8889/work_files/research/dl/nlp/cnnsNnlp#bodyContents12)  
    1. __List variations of pooling and their definitions:__{: style="color: blue"}  
        <button>Show Questions</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        1. __What is "Learned Pooling":__{: style="color: blue"}  
        1. __What is "Dynamical Pooling":__{: style="color: blue"}  
        {: hidden=""}
    1. __List the hyperparams of Pooling Layer:__{: style="color: blue"}  
    1. __How to calculate the size of the output volume:__{: style="color: blue"}  
    1. __How many parameters does the pooling layer have:__{: style="color: blue"}    
    1. __What are other ways to perform downsampling:__{: style="color: blue"}  
1. __Weight Priors:__{: style="color: red"}  
    1. __Define "Prior Prob Distribution on the parameters":__{: style="color: blue"}  
    1. __Define "Weight Prior" and its types/classes:__{: style="color: blue"}  
        <button>Show Questions</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        1. __Weak Prior:__{: style="color: blue"}  
        1. __Strong Prior:__{: style="color: blue"}  
        1. __Infinitely Strong Prior:__{: style="color: blue"}  
        {: hidden=""}
    1. __Describe the Conv Layer as a FC Layer using priors:__{: style="color: blue"}  
    1. __What are the key insights of using this view:__{: style="color: blue"}  
        <button>Show Questions</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        1. __When is the prior imposed by convolution INAPPROPRIATE:__{: style="color: blue"}  
        1. __What happens when the priors imposed by convolution and pooling are not suitable for the task?__{: style="color: blue"}  
        1. __What kind of other models should Convolutional models be compared to? Why?:__{: style="color: blue"}  
        {: hidden=""}
1. __When do multi-channel convolutions commute?__{: style="color: red"}  
[Answer](/work_files/research/dl/archits/convnets#bodyContents61)
1. __Why do we use several different kernels in a given conv-layer?__{: style="color: red"}  
1. __Strided Convolutions__{: style="color: red"}    
    1. __Define:__{: style="color: blue"}  
    1. __What are they used for?__{: style="color: blue"}  
    1. __What are they equivalent to?__{: style="color: blue"}  
    1. __Formula:__{: style="color: blue"}  
1. __Zero-Padding:__{: style="color: red"}  
    1. __Definition/Usage:__{: style="color: blue"}  
    1. __List the types of padding:__{: style="color: blue"}  
1. __Locally Connected Layers/Unshared Convolutions:__{: style="color: red"}  
1. __Bias Parameter:__{: style="color: red"}  
    1. __How many bias terms are used per output channel in the tradional convolution:__{: style="color: blue"}  
1. __Dilated Convolutions__{: style="color: red"}    
    1. __Define:__{: style="color: blue"}  
    1. __What are they used for?__{: style="color: blue"}  
1. __Stacked Convolutions__{: style="color: red"}    
    1. __Define:__{: style="color: blue"}  
    1. __What are they used for?__{: style="color: blue"}  
1. __What is the rule of Bias(es) in CNNs:__{: style="color: red"}  
* [Archits](http://localhost:8889/work_files/research/dl/arcts)


***

## Theory


## RNNs
1. __What is an RNN?__{: style="color: red"}  
    1. __Definition:__{: style="color: blue"}  
    1. __What machine-type is the standard RNN:__{: style="color: blue"}  
1. __What is the big idea behind RNNs?__{: style="color: red"}  
1. __Dynamical Systems:__{: style="color: red"}  
    1. __Standard Form:__{: style="color: blue"}  
    1. __RNN as a Dynamical System:__{: style="color: blue"}  
1. __Unfolding Computational Graphs__{: style="color: red"}  
    1. __Definition:__{: style="color: blue"}  
    1. __List the Advantages introduced by unfolding and the benefits:__{: style="color: blue"}  
    1. __Graph and write the equations of Unfolding hidden recurrence:__{: style="color: blue"}    
1. __Describe the State of the RNN, its usage, and extreme cases of the usage:__{: style="color: red"}  
1. __RNN Architectures:__{: style="color: red"}  
    1. __List the three standard architectures of RNNs:__{: style="color: blue"}  
        1. __Graph:__{: style="color: blue"}  
        1. __Architecture:__{: style="color: blue"}  
        1. __Equations:__{: style="color: blue"}  
        1. __Total Loss:__{: style="color: blue"}  
        1. __Complexity:__{: style="color: blue"}  
        1. __Properties:__{: style="color: blue"}  
1. __Teacher Forcing:__{: style="color: red"}  
    1. __Definition:__{: style="color: blue"}  
    1. __Application:__{: style="color: blue"}  
    1. __Disadvantages:__{: style="color: blue"}  
    1. __Possible Solutions for Mitigation:__{: style="color: blue"}  


***

## Optimization
1. __Define the *sigmoid* function and some of its properties:__{: style="color: red"}  
1. __Backpropagation:__{: style="color: red"}  
    1. __Definition:__{: style="color: blue"}  
    1. __Derive Gradient Descent Update:__{: style="color: blue"}  
    1. __Explain the difference kinds of gradient-descent optimization procedures:__{: style="color: blue"}  
    1. __List the different optimizers and their properties:__{: style="color: blue"}  
1. __Error-Measures:__{: style="color: red"}  
    1. __Define what an error measure is:__{: style="color: blue"}  
    1. __List the 5 most common error measures and where they are used:__{: style="color: blue"}  
    1. __Specific Questions:__{: style="color: blue"}  
        <button>Show Questions</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
        1. __Derive MSE carefully:__{: style="color: blue"}  
        1. __Derive the Binary Cross-Entropy Loss function:__{: style="color: blue"}  
        1. __Explain the difference between Cross-Entropy and MSE and which is better (for what task)?__{: style="color: blue"}  
        1. __Describe the properties of the Hinge loss and why it is used?__{: style="color: blue"}  
        {: hidden=""}  
1. __Show that the weight vector of a linear signal is orthogonal to the decision boundary?__{: style="color: red"}  
1. __What does it mean for a function to be *well-behaved* from an optimization pov?__{: style="color: red"}  
1. __Write $$\|\mathrm{Xw}-\mathrm{y}\|^{2}$$ as a summation__{: style="color: red"}  
1. __Compute:__{: style="color: red"}  
    1. __$$\dfrac{\partial}{\partial y}\vert{x-y}\vert=$$__{: style="color: blue"}  
1. __State the difference between SGD and GD?__{: style="color: red"}  
1. __When would you use GD over SDG, and vice-versa?__{: style="color: red"}  
1. __What is convex hull ?__{: style="color: red"}  
1. __OLS vs MLE__{: style="color: red"}  



***

## ML Theory
1. __Explain intuitively why Deep Learning works?__{: style="color: red"}  
1. __List the different types of Learning Tasks and their definitions:__{: style="color: red"}  
[answer](/concepts_#bodyContents64)  
1. __Describe the relationship between supervised and unsupervised learning?__{: style="color: red"}  
[answer](/concepts_#bodyContents64)  
1. __Describe the differences between Discriminative and Generative Models?__{: style="color: red"}  
1. __Describe the curse of dimensionality and its effects on problem solving:__{: style="color: red"}  
1. __How to deal with curse of dimensionality__{: style="color: red"}  
1. __Describe how to initialize a NN and any concerns w/ reasons:__{: style="color: red"}  
1. __Describe the difference between Learning and Optimization in ML:__{: style="color: red"}  
1. __List the 12 Standard Tasks in ML:__{: style="color: red"}  
1. __What is the difference between inductive and deductive learning?__{: style="color: red"}  


***

## Statistical Learning Theory
1. __Define Statistical Learning Theory:__{: style="color: red"}  
    <button>Show</button>{: .showText value="show"
     onclick="showTextPopHide(event);"}
    1. __What field is it the theory for?__:  
    1. __What fields does it draw from?__:  
    1. __What does it allow us to do?__:  
    1. __What question does it answer?__:  
    1. __What is it a subfield-of/approach-to?__:  
    {: hidden=""}
1. __What assumptions are made by the theory?__{: style="color: red"}  
    <button>Show</button>{: .showText value="show"
    onclick="showTextPopHide(event);"}
    1. __Define the i.i.d assumptions?__{: style="color: blue"}  
    1. __Why assume a *joint* probability distribution $$p(x,y)$$?__{: style="color: blue"}  
    1. __Why do we need to model $$y$$ as a target-distribution and not a target-function?__{: style="color: red"}  
    {: hidden=""}
1. __Give the Formal Definition of SLT:__{: style="color: red"}  
    <button>Show</button>{: .showText value="show"
     onclick="showTextPopHide(event);"}
    1. __The Definitions:__{: style="color: blue"}  
    1. __The Assumptions:__{: style="color: blue"}  
    1. __The Inference Problem:__{: style="color: blue"}  
    1. __The Expected Risk:__{: style="color: blue"}  
    1. __The Target Function:__{: style="color: blue"}  
    1. __The Empirical Risk:__{: style="color: blue"}  
    {: hidden=""}
1. __Define Empirical Risk Minimization:__{: style="color: red"}  
1. __What is the Complexity of ERM?__{: style="color: red"}  
    <button>Show</button>{: .showText value="show"
     onclick="showTextPopHide(event);"}
    1. __How do you Cope with the Complexity?__{: style="color: blue"}  
    {: hidden=""}
1. __Definitions:__{: style="color: red"}  
    1. __Generalization:__{: style="color: blue"}  
    1. __Generalization Error:__{: style="color: blue"}  
    1. __Generalization Gap:__{: style="color: blue"}  
        1. __Computing the Generalization Gap:__{: style="color: blue"}  
        1. __What is the goal of SLT in the context of the Generalization Gap given that it can't be computed?__{: style="color: blue"}  
    1. __Achieving ("good") Generalization:__{: style="color: blue"}  
        An _algorithm_ is said to __generalize__ when 
    1. __Empirical Distribution:__{: style="color: blue"}  
1. __Describe the difference between Learning and Optimization in ML:__{: style="color: red"}  
1. __Describe the difference between Generalization and Learning in ML:__{: style="color: red"}  
1. __How to achieve Learning?__{: style="color: red"}   
1. __What does the (VC) Learning Theory Achieve?__{: style="color: red"}  
1. __Why do we need the probabilistic framework?__{: style="color: red"}  
1. __Give the Formal Definition of SLT:__{: style="color: red"}  
1. __What is the *Approximation-Generalization Tradeoff*? How is it characterized?:__{: style="color: red"}  
1. __What are the factors determining how well an ML-algo will perform?__{: style="color: red"}  
1. __Define the following and their usage/application & how they relate to each other:__{: style="color: red"}  
    1. __Underfitting:__{: style="color: blue"}  
    1. __Overfitting:__{: style="color: blue"}  
    1. __Capacity:__{: style="color: blue"}  
        * Models with __Low-Capacity:__{: style="color: blue"}  
        * Models with __High-Capacity:__{: style="color: blue"}  
    1. __Hypothesis Space:__{: style="color: blue"}  
    1. __VC-Dimension:__{: style="color: red"}  
        1. __What does it measure?__{: style="color: blue"}  
    1. __Graph the relation between Error, and Capacity in the ctxt of (Underfitting, Overfitting, Training Error, Generalization Err, and Generalization Gap):__{: style="color: blue"}  
1. __What is the most important result in SLT that show that learning is feasible?__{: style="color: red"}  




***

## Bias-Variance Decomposition Theory
1. __What is the Bias-Variance Decomposition Theory:__{: style="color: red"}  
1. __What are the Assumptions made by the theory?__{: style="color: red"}  
1. __What is the question that the theory tries to answer? How do you achieve the answer to this question? What assumption is important?__{: style="color: red"}
1. __What is the Bias-Variance Decomposition:__{: style="color: red"}  
1. __Define each term w.r.t. source of the error (error from):__{: style="color: red"}  
    1. __Bias:__{: style="color: blue"}  
    1. __Variance:__{: style="color: blue"}  
    1. __Irreducible Error:__{: style="color: blue"}  
1. __What does each of the following measure (error in)? Describe this measured quantity in words, mathematically. Describe Bias&Variance in Words as a question statement. Give their AKA in statistics.__{: style="color: red"}  
    1. __Bias:__{: style="color: blue"}  
    1. __Variance:__{: style="color: blue"}  
    1. __Irreducible Error:__{: style="color: blue"}  
1. __Give the Formal Definition of the Decomposition (Formula):__{: style="color: red"}  
    1. __What is the Expectation over?__{: style="color: blue"}  
1. __Define the *Bias-Variance Tradeoff*:__{: style="color: red"}  
    1. __Effects of Bias:__{: style="color: blue"}  
        1. __High Bias__:  
        1. __Low Bias__:  
    1. __Effects of Variance:__{: style="color: blue"}  
        1. __High Variance__:  
        1. __Low Variance__:  
    1. __Draw the Graph of the Tradeoff (wrt model capacity):__{: style="color: blue"}  
1. __Derive the Bias-Variance Decomposition with explanations:__{: style="color: red"}  
1. __What are the key Takeaways from the Tradeoff?__{: style="color: red"}  
1. __What are the most common ways to negotiate the Tradeoff? (i.e. selecting/comparing models)__{: style="color: red"}  
1. __How does the decomposition relate to Classification?__{: style="color: red"}  
1. __Increasing/Decreasing Bias&Variance:__{: style="color: red"}    
    1. __Adding Good Feature__: 
    1. __Adding Bad Feature__: 
    1. __Adding ANY Feature__: 
    1. __Adding more Data__: 
    1. __Noise in Test Set__: 
    1. __Noise in Training Set__: 
    1. __Dimensionality Reduction__: 
    1. __Feature Selection__: 
    1. __Regularization__: 
    1. __Increasing # of Hidden Units in ANNs__: 
    1. __Increasing # of Hidden Layers in ANNs__: 
    1. __Increasing $$k$$ in K-NN__: 
    1. __Increasing Depth in Decision-Trees__: 
    1. __Boosting__: 
    1. __Bagging__: 
    


***

## Activation Functions
1. __Describe the Desirable Properties for activation functions:__{: style="color: red"}  
    <button>Explain the specifics of the desirability of each of the following</button>{: .showText value="show"
    onclick="showTextPopHide(event);"}
    1. __Non-Linearity:__{: style="color: blue"}  
    1. __Range:__{: style="color: blue"}  
    1. __Continuously Differentiable:__{: style="color: blue"}  
    1. __Monotonicity:__{: style="color: blue"}  
    1. __Smoothness with Monotonic Derivatives:__{: style="color: blue"}  
    1. __Approximating Identity near Origin:__{: style="color: blue"}  
    1. __Zero-Centered Range:__{: style="color: blue"}  
    {: hidden=""}
1. __Describe the NON-Desirable Properties for activation functions:__{: style="color: red"}  
    <button>Explain the specifics of the non-desirability of each of the following</button>{: .showText value="show"
    onclick="showTextPopHide(event);"}
    1. __Saturation:__{: style="color: blue"}  
    1. __Vanishing Gradients:__{: style="color: blue"}  
    1. __Range Not Zero-Centered:__{: style="color: blue"}  
    {: hidden=""}
1. __List the different activation functions used in ML?__{: style="color: red"}  
    __Names, Definitions, Properties (pros&cons), Derivatives, Applications, pros/cons:__{: style="color: blue"}  

<button>Show Questions</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
1. __Fill in the following table:__{: style="color: red"}  
    ![img](/main_files/dl/concepts/act_funcs/0.png){: width="100%"}  
1. __Tanh VS Sigmoid for activation?__{: style="color: red"}  
1. __ReLU:__{: style="color: red"}  
    1. __What makes it superior/advantageous?__{: style="color: red"}  
    1. __What problems does it have?__{: style="color: red"}  
        1. __What solution do we have to mitigate the problem?__{: style="color: red"}  
1. __Compute the derivatives of all activation functions:__{: style="color: red"}  
1. __Graph all activation functions and their derivatives:__{: style="color: red"}  
{: hidden=""}

***

## Kernels
1. __Define "Local Kernel" and give an analogy to describe it:__{: style="color: red"}  
1. __Write the following kernels:__{: style="color: red"}  
    1. __Polynomial Kernel of degree, up to, $$d$$:__{: style="color: blue"}  
    1. __Gaussian Kernel:__{: style="color: blue"}  
    1. __Sigmoid Kernel:__{: style="color: blue"}  
    1. __Polynomial Kernel of degree, exactly, $$d$$:__{: style="color: blue"}  
    


***

## Math
1. __What is a metric?__{: style="color: red"}  
[Metric](http://localhost:8889/concepts_#bodyContents31)

1. __Describe Binary Relations and their Properties?__{: style="color: red"}  
[answer](/concepts_#bodyContents32)


1. __Formulas:__{: style="color: red"}  
    1. __Set theory:__{: style="color: blue"}  
        1. __Number of subsets of a set of $$N$$ elements:__{: style="color: blue"}  
        1. __Number of pairs $$(a,b)$$ of a set of N elements:__{: style="color: blue"}  
    1. __Binomial Theorem:__{: style="color: blue"}  
    1. __Binomial Coefficient:__{: style="color: blue"}  
    1. __Expansion of $$x^n - y^n = $$__{: style="color: blue"}  
    1. __Number of ways to partition $$N$$ data points into $$k$$ clusters:__{: style="color: blue"}  
    1. __$$\log_x(y) =$$__{: style="color: blue"}  
    1. __The length of a vector $$\mathbf{x}$$  along a direction (projection):__{: style="color: blue"}  
        1. Along a unit-length vector $$\hat{\mathbf{w}}$$: 
        2. Along an unnormalized vector $$\mathbf{w}$$: 
    1. __$$\sum_{i=1}^{n} 2^{i}=$$__{: style="color: blue"}  

1. __List 6 proof methods:__{: style="color: red"}  
[answer](/concepts_#bodyContents34)

1. __Something__{: style="color: red"}  

***

## Statistics
1. __ROC curve:__{: style="color: red"}  
    1. __Definition:__{: style="color: blue"}  
    1. __Purpose:__{: style="color: blue"}  
    1. __How do you create the plot?__{: style="color: blue"}  
    1. __How to identify a good classifier:__{: style="color: blue"}  
    1. __How to identify a bad classifier:__{: style="color: blue"}  
    1. __What is its application in tuning the model?__{: style="color: blue"}  
1. __AUC - AUROC:__{: style="color: red"}  
    1. __Definition:__{: style="color: blue"}  
    1. __Range:__{: style="color: blue"}  
    1. __What does it measure:__{: style="color: blue"}  
    1. __Usage in ML:__{: style="color: blue"}  
1. __Define Statistical Efficiency (of an estimator)?__{: style="color: red"}  
    * __Intuitive Difference:__{: style="color: blue"}  
    * __How do we define Efficiency?__{: style="color: blue"}  
    * __What's the difference between an efficient and inefficient estimators?__{: style="color: blue"}  
    * __How's the use of an inefficient estimator bad compared to an efficient one?__{: style="color: blue"}  
1. __Whats the difference between *Errors* and *Residuals*:__{: style="color: red"}  
    1. __Compute the statistical errors and residuals of the univariate, normal distribution defined as $$X_{1}, \ldots, X_{n} \sim N\left(\mu, \sigma^{2}\right)$$:__{: style="color: blue"}  
1. __What is a biased estimator?__{: style="color: red"}  
    1. __Why would we prefer biased estimators in some cases?__{: style="color: blue"}  
1. __What is the difference between "Probability" and "Likelihood":__{: style="color: red"}  
1. __Estimators:__{: style="color: red"}  
    1. __Define:__{: style="color: blue"}  
    1. __Formula:__{: style="color: blue"}  
    1. __Whats a good estimator?__{: style="color: blue"}  
    1. __What are the Assumptions made regarding the estimated parameter:__{: style="color: blue"}  
1. __What is Function Estimation:__{: style="color: red"}  
    1. __Whats the relation between the Function Estimator $$\hat{f}$$ and Point Estimator:__{: style="color: blue"}  
1. __Define "marginal likelihood" (wrt naive bayes):__{: style="color: red"}  


***


## (Statistics) - MLE
1. __Clearly Define MLE and derive the final formula:__{: style="color: red"}  
    1. __Write MLE as an expectation wrt the Empirical Distribution:__{: style="color: blue"}  
    1. __Describe formally the relationship between MLE and the KL-divergence:__{: style="color: blue"}  
    1. __Extend the argument to show the link between MLE and Cross-Entropy. Give an example of a well-known loss function:__{: style="color: blue"}  
    1. __How does the form of the model (model family) affect the MLE Estimate?__{: style="color: blue"}  
    1. __How does MLE relate to the model distribution and the empirical distribution?__{: style="color: blue"}  
    1. __What is the intuition behind using MLE?__{: style="color: blue"}  
    1. __What does MLE find/result in?__{: style="color: blue"}  
    1. __What kind of problem is MLE and how to solve for it?__{: style="color: blue"}  
    1. __How does it relate to SLT:__{: style="color: blue"}   
    1. __Explain clearly why we maximize the natural log of the likelihood__{: style="color: blue"}  


***


## Text-Classification \| Classical
1. __List some Classification Methods:__{: style="color: red"}  
1. __List some Applications of Txt Classification:__{: style="color: red"}  

***

## NLP
1. __List some problems in NLP:__{: style="color: red"}  
1. __List the Solved Problems in NLP:__{: style="color: red"}  
1. __List the "within reach" problems in NLP:__{: style="color: red"}  
1. __List the Open Problems in NLP:__{: style="color: red"}  
1. __Why is NLP hard? List Issues:__{: style="color: red"}  
1. __Define:__{: style="color: red"}  
    1. __Morphology:__{: style="color: blue"}  
    1. __Morphemes:__{: style="color: blue"}  
    1. __Stems:__{: style="color: blue"}  
    1. __Affixes:__{: style="color: blue"}  
    1. __Stemming:__{: style="color: blue"}  
    1. __Lemmatization:__{: style="color: blue"}  

***

## Language Modeling
1. __What is a Language Model?__{: style="color: red"}  
1. __List some Applications of LMs:__{: style="color: red"}  
1. __Traditional LMs:__{: style="color: red"}  
    1. __How are they setup?__{: style="color: blue"}  
    1. __What do they depend on?__{: style="color: blue"}  
    1. __What is the Goal of the LM task? (in the ctxt of the problem setup)__{: style="color: blue"}  
    1. __What assumptions are made by the problem setup? Why?__{: style="color: blue"}  
    1. __What are the MLE Estimates for probabilities of the following:__{: style="color: blue"}  
        1. __Bi-Grams:__{: style="color: blue"}  
            <p>$$p(w_2\vert w_1) = $$</p>  
        1. __Tri-Grams:__{: style="color: blue"}  
            <p>$$p(w_3\vert w_1, w_2) = $$</p>  
    1. __What are the issues w/ Traditional Approaches?__{: style="color: red"}  
1. __What+How can we setup some NLP tasks as LM tasks:__{: style="color: red"}  
1. __How does the LM task relate to Reasoning/AGI:__{: style="color: red"}  
1. __Evaluating LM models:__{: style="color: red"}  
    1. __List the Loss Functions (+formula) used to evaluate LM models? Motivate each:__{: style="color: blue"}  
    1. __Which application of LM modeling does each loss work best for?__{: style="color: blue"}  
    <button>Show Questions</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
    1. __Why Cross-Entropy:__{: style="color: blue"}  
    1. __Which setting it used for?__{: style="color: blue"}  
    1. __Why Perplexity:__{: style="color: blue"}  
    1. __Which setting used for?__{: style="color: blue"}  
    1. __If no surprise, what is the perplexity?__{: style="color: blue"}  
    1. __How does having a good LM relate to Information Theory?__{: style="color: blue"}  
    {: hidden=""}
1. __LM DATA:__{: style="color: red"}  
    1. __How does the fact that LM is a time-series prediction problem affect the way we need to train/test:__{: style="color: blue"}  
    1. __How should we choose a subset of articles for testing:__{: style="color: blue"}  
1. __List three approaches to Parametrizing LMs:__{: style="color: red"}  
    <button>Show Questions</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
    1. __Describe "Count-Based N-gram Models":__{: style="color: blue"}  
    1. __What distributions do they capture?:__{: style="color: blue"}  
    1. __Describe "Neural N-gram Models":__{: style="color: blue"}  
    1. __What do they replace the captured distribution with?__{: style="color: blue"}  
    1. __What are they better at capturing:__{: style="color: blue"}  
    1. __Describe "RNNs":__{: style="color: blue"}  
    1. __What do they replace/capture?__{: style="color: blue"}  
    1. __How do they capture it?__{: style="color: blue"}  
    1. __What are they best at capturing:__{: style="color: blue"}  
    {: hidden=""}
1. __What's the main issue in LM modeling?__{: style="color: red"}  
    <button>Show Questions</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
    1. __How do N-gram models capture/approximate the history?:__{: style="color: blue"}  
    1. __How do RNNs models capture/approximate the history?:__{: style="color: blue"}  
    {: hidden=""}
    1. __The Bias-Variance Tradeoff of the following:__{: style="color: blue"}  
        1. __N-Gram Models:__{: style="color: blue"}  
        1. __RNNs:__{: style="color: blue"}  
        1. __An Estimate s.t. it predicts the probability of a sentence by how many times it has seen it before:__{: style="color: blue"}  
            1. __What happens in the limit of infinite data?__{: style="color: blue"}  
1. __What are the advantages of sub-word level LMs:__{: style="color: red"}  
1. __What are the disadvantages of sub-word level LMs:__{: style="color: red"}  
1. __What is a "Conditional LM"?__{: style="color: red"}  
1. __Write the decomposition of the probability for the Conditional LM:__{: style="color: red"}  
1. __Describe the Computational Bottleneck for Language Models:__{: style="color: red"}  
1. __Describe/List some solutions to the Bottleneck:__{: style="color: red"}  
1. __Complexity Comparison of the different solutions:__{: style="color: red"}  
    <button>Show Questions</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](/main_files/qs/1.png){: width="100%" hidden=""}   

***

## Regularization
1. __Define Regularization both intuitively and formally:__{: style="color: red"}  
1. __Define "well-posedness":__{: style="color: red"}  
1. __Give four aspects of justification for regularization (theoretical):__{: style="color: red"}  
    <button>Show</button>{: .showText value="show"
    onclick="showTextPopHide(event);"}
    1. __From a philosophical pov:__{: style="color: blue"}  
    1. __From a probabilistic pov:__{: style="color: blue"}  
    1. __From an SLT pov:__{: style="color: blue"}  
    1. __From a practical pov (relating to the real-world):__{: style="color: blue"}  
    {: hidden=""}
1. __Describe an overview of regularization in DL. How does it usually work?__{: style="color: red"}  
    1. __Intuitively, how can a regularizer be effective?__{: style="color: blue"}  
1. __Describe the relationship between regularization and capacity. How does regularization work in this case?__{: style="color: red"}  
1. __Describe the different approaches to regularization:__{: style="color: red"}  
1. __List 9 regularization techniques:__{: style="color: red"}  

<button>Show</button>{: .showText value="show"
onclick="showText_withParent_PopHide(event);"}
1. __Describe Parameter Norm Penalties (PNPs):__{: style="color: red"}  
    <button>Show</button>{: .showText value="show"
    onclick="showTextPopHide(event);"}
    1. __Describe the parameter $$\alpha$$:__{: style="color: blue"}  
    1. __How does it influence the regularization:__{: style="color: blue"}  
    1. __What is the effect of minimizing the regularized objective?__{: style="color: blue"}  
    {: hidden=""}
1. __How do we deal with the Bias parameter in PNPs? Explain.__{: style="color: red"}  
1. __Describe the tuning of the $$\alpha$$ HP in NNs for different hidden layers:__{: style="color: red"}  
1. __Formally describe the $$L^2$$ parameter regularization:__{: style="color: red"}  
    1. __AKA:__{: style="color: blue"}  
    1. __Describe the regularization contribution to the gradient in a single step.__{: style="color: blue"}  
    1. __Describe the regularization contribution to the gradient. How does it scale?__{: style="color: blue"}  
    1. __How does weight decay relate to shrinking the individual weight wrt their size? What is the measure/comparison used?__{: style="color: blue"}  
1. __Draw a graph describing the effects of $$L^2$$ regularization on the weights:__{: style="color: red"}  
1. __Describe the effects of applying weight decay to linear regression__{: style="color: red"}  
1. __Derivation:__{: style="color: red"}  
    <button>Show</button>{: .showText value="show"
    onclick="showTextPopHide(event);"}
    1. __What is $$L^2$$ regularization equivalent to?__{: style="color: blue"}  
    1. __What are we maximizing?__{: style="color: blue"}  
    1. __Derive the MAP Estimate:__{: style="color: blue"}  
    1. __What kind of prior do we place on the weights? What are its parameters?__{: style="color: blue"}  
    {: hidden=""}
1. __List the properties of $$L^2$$ regularization:__{: style="color: red"}  
1. __Formally describe the $$L^1$$ parameter regularization:__{: style="color: red"}  
    1. __AKA:__{: style="color: blue"}  
    1. __Whats the regularized objective function?__{: style="color: blue"}  
    1. __What is its gradient?__{: style="color: blue"}  
    1. __Describe the regularization contribution to the gradient compared to L2. How does it scale?__{: style="color: blue"}  
1. __List the properties and applications of $$L^1$$ regularization:__{: style="color: red"}  
    <button>Show</button>{: .showText value="show"
    onclick="showTextPopHide(event);"}
    1. __How is used as a feature selection mechanism?__{: style="color: blue"}  
    {: hidden=""}
1. __Derivation:__{: style="color: red"}  
    <button>Show</button>{: .showText value="show"
    onclick="showTextPopHide(event);"}
    1. __What is $$L^1$$ regularization equivalent to?__{: style="color: blue"}  
    1. __What kind of prior do we place on the weights? What are its parameters?__{: style="color: blue"}  
    {: hidden=""}
1. __Analyze $$L^1$$ vs $$L^2$$ regularization:__{: style="color: red"}  
    <button>Show</button>{: .showText value="show"
    onclick="showTextPopHide(event);"}
    1. __For Sparsity:__{: style="color: blue"}  
    1. __For correlated features:__{: style="color: blue"}  
    1. __For optimization:__{: style="color: blue"}  
    1. __Give an example that shows the difference wrt sparsity:__{: style="color: blue"}  
    1. __For sensitivity:__{: style="color: blue"}  
    {: hidden=""}
1. __Describe Elastic Net Regularization. Why was it devised?__{: style="color: red"}  
1. __Motivate Regularization for ill-posed problems:__{: style="color: red"}  
    1. __What is the property that needs attention?__{: style="color: blue"}  
    1. __What would the regularized solution correspond to in this case?__{: style="color: blue"}  
    1. __Are there any guarantees for the solution to be well-posed? How/Why?__{: style="color: blue"}  

    <button>Show</button>{: .showText value="show"
    onclick="showText_withParent_PopHide(event);"}
    1. __What is the Linear Algebraic property that needs attention?__{: style="color: blue"}  
    1. __What models are affected by this?__{: style="color: blue"}  
    1. __What would the sol correspond to in terms of inverting $$X^TX$$:__{: style="color: blue"}  
    1. __When would $$X^TX$$ be singular?__{: style="color: blue"}  
    1. __Describe the Linear Algebraic Perspective. What does it correspond to? [LAP]__{: style="color: blue"}  
    1. __Can models with no closed-form solution be underdetermined? Explain. [CFS]__{: style="color: blue"}  
    1. __What models are affected by this? [CFS]__{: style="color: blue"}  
    {: hidden=""}

    <button>Show [LAP] Problems</button>{: .showText value="show"
    onclick="showText_withParent_PopHide(event);"}
    1. __Define the Moore-Penrose Pseudoinverse:__{: style="color: blue"}  
    1. __What can it solve?__{: style="color: blue"}  
    1. __What does it correspond to in terms of regularization?__{: style="color: blue"}  
    1. __What is the limit wrt?__{: style="color: blue"}  
    1. __How can we interpret the pseudoinverse wrt regularization?__{: style="color: blue"}  
    {: hidden=""}

    <button>Show [CFS] Problems</button>{: .showText value="show"
    onclick="showText_withParent_PopHide(event);"}
    1. __Explain the problem with Logistic Regression:__{: style="color: blue"}  
    1. __What are the possible solutions?__{: style="color: blue"}  
    1. __Are there any guarantees that we achieve with regularization?__{: style="color: blue"}  
    {: hidden=""}
1. __Describe dataset augmentation and its techniques:__{: style="color: red"}  
1. __When is dataset augmentation applicable?__{: style="color: red"}  
1. __When is it not?__{: style="color: red"}  
1. __Motivate Noise Robustness property:__{: style="color: red"}  
1. __How can Noise Robustness motivate a regularization technique?__{: style="color: red"}  
1. __How can we enhance noise robustness in NN?__{: style="color: red"}  
    <button>Show</button>{: .showText value="show"
    onclick="showTextPopHide(event);"}
    1. __Where can noise be injected?__{: style="color: blue"}  
    1. __Give Motivation, Interpretation and Applications of injecting noise in the different components (from above):__{: style="color: blue"}  
    {: hidden=""}

    <button>Show further questions</button>{: .showText value="show"
    onclick="showText_withParent_PopHide(event);"}
    1. __Motivate the injecting of noise:__{: style="color: blue"}  
    1. __Give an interpretation for injecting noise in the Input layer:__{: style="color: blue"}  
    1. __Give an interpretation for injecting noise in the Hidden layers:__{: style="color: blue"}  
    1. __What is the most successful application of this technique:__{: style="color: blue"}  
    1. __Describe the Bayesian View of learning:__{: style="color: blue"}  
    1. __How does it motivate injecting noise in the weight matrices?__{: style="color: blue"}  
    1. __Describe a different interpretation of injecting noise to matrices. What are its effects on the function to be learned?__{: style="color: blue"}  
    1. __Whats the biggest application for this kind of regularization?__{: style="color: blue"}  
    1. __Motivate injecting noise in the Output layer:__{: style="color: blue"}  
    1. __What is the biggest application of this technique?__{: style="color: blue"}  
    1. __How does it compare to weight-decay when applied to MLE problems?__{: style="color: blue"}  
    {: hidden=""}
1. __Define "Semi-Supervised Learning":__{: style="color: red"}  
    1. __What does it refer to in the context of DL:__{: style="color: blue"}  
    1. __What is its goal?__{: style="color: blue"}  
    1. __Give an example in classical ML:__{: style="color: blue"}  
1. __Describe an approach to applying semi-supervised learning:__{: style="color: red"}  
1. __How can we interpret dropout wrt data augmentation?__{: style="color: red"}  
{: hidden=""}

1. __When is Ridge regression favorable over Lasso regression? for correlated features?__{: style="color: red"}  

***

## Misc.
1. __Explain Latent Dirichlet Allocation (LDA)__{: style="color: red"}  
1. __How to deal with curse of dimensionality__{: style="color: red"}  
1. __How to detect correlation of "categorical variables"?__{: style="color: red"}  
1. __Define "marginal likelihood" (wrt naive bayes):__{: style="color: red"}  
1. __KNN VS K-Means__{: style="color: red"}  
1. __When is Ridge regression favorable over Lasso regression for correlated features?__{: style="color: red"}  
1. __Capturing the correlation between continuous and categorical variable? If yes, how?__{: style="color: red"}  
1. __Random Forest VS GBM?__{: style="color: red"}  
1. __What is convex hull ?__{: style="color: red"}  
1. __What cross validation technique would you use on time series data set?__{: style="color: red"}  
1. __How to deal with missing features? (Imputation?)__{: style="color: red"}  
1. __Describe the different algorithms for recommendation systems:__{: style="color: red"}  
1. __Do you suggest that treating a categorical variable as continuous variable would result in a better predictive model?__{: style="color: red"}  
1. __OLS vs MLE__{: style="color: red"}  
1. __What is the difference between inductive and deductive learning?__{: style="color: red"}  
1. __What are collinearity and multicollinearity?__{: style="color: red"}  
1. __What are the two paradigms of ensemble methods?__{: style="color: red"}  
1. __Describe Label Smoothing as a regularization technique:__{: style="color: red"}  
    1. __Give its motivation:__{: style="color: blue"}   
* __What is data normalization and why do we need it?:__{: style="color: blue"}  
* __Weight initialization in neural networks?:__{: style="color: blue"}  
* __How to improve Generalization__{: style="color: red"}  
* __How to prevent Overfitting__{: style="color: red"}  
* __How to control the capacity__{: style="color: red"}  
* __Why small weights in NN lead to lower capacity:__{: style="color: red"}  

__INTERVIEWS__  
* __Can they derive the back-propagation and weights update?:__{: style="color: blue"}  
* __Extend the above question to non-trivial layers such as convolutional layers, pooling layers, etc.:__{: style="color: blue"}  
* __How to implement dropout:__{: style="color: blue"}  
* __Their intuition when and why some tricks such as max pooling, ReLU, maxout, etc. work. There are no right answers but it helps to understand their thoughts and research experience.:__{: style="color: blue"}  
* __Can they abstract the forward, backward, update operations as matrix operations, to leverage BLAS and GPU?:__{: style="color: blue"}  
* __What is an auto-encoder? Why do we "auto-encode"? Hint: it's really a misnomer.:__{: style="color: blue"}  
* __What is a Boltzmann Machine? Why a Boltzmann Machine?:__{: style="color: blue"}  
* __Why do we use sigmoid for an output function? Why tanh? Why not cosine? Why any function in particular?:__{: style="color: blue"}  
* __Why are CNNs used primarily in imaging and not so much other tasks?:__{: style="color: blue"}  
* __Explain backpropagation. Seriously. To the target audience described above.:__{: style="color: blue"}  
* __Is it OK to connect from a Layer 4 output back to a Layer 2 input?:__{: style="color: blue"}  
* __A data-scientist person recently put up a YouTube video explaining that the essential difference between a Neural Network and a Deep Learning network is that the former is trained from output back to input, while the latter is trained from input toward output. Do you agree? Explain.:__{: style="color: blue"}  
* [Interview Qs (Quora)](https://www.quora.com/What-are-the-toughest-neural-networks-and-deep-learning-interview-questions)  
* [NLP-Interview](https://docs.google.com/document/d/1eYcKSc5NcaWL0TdQD1l5iypfW27S1d9SDrvaUnGEENE/edit)  
* [Robin-Interview](https://docs.google.com/document/d/1ORo2m8cCr5ZnwAH_VHHOpj6jxL6-xuxeIXu2QJA0LbA/edit)  
* [Robin](https://docs.google.com/document/d/1WqSkunRb0Bue1LX3nZYUXEJMQt7-sHikVtZ96qwE6zs/edit)  
* [CV-Inter](https://docs.google.com/document/d/1-F52-xt4O57Ut75DfF6bx-XYcWWZtRhQKVAMcZrMAes/edit)  
* [Polarr-Inter](https://docs.google.com/document/d/1Yipw1BsW9-BO4FuBKG2SvtH-PIiZN_MQ78P1n9QT3_s/edit)  


***


## FeedForward Neural Network
1. __What is a *"FeedForward"* Neural Network:__{: style="color: red"}  
1. __What is the Architecture of an FFN (components and how they work together):__{: style="color: red"}  
1. __List two examples of FFNs:__{: style="color: red"}  
    <button>Further Questions</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    1. __Describe the "Single-Layer Perceptron":__{: style="color: blue"}  
    1. __Describe the "Multi-Layer Perceptron" (vaguely describe the components of the architecture and how they fit together):__{: style="color: blue"}  
    {: hidden=""}

***

## Multilayer Perceptron
1. __What model class does the "Multi-Layer Perceptron" belong to:__{: style="color: red"}  
1. __What is the Architecture of an MLP:__{: style="color: red"}  
    <button>Further Questions</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    1. __What are the Layers names/types:__{: style="color: blue"}  
    1. __What do the Connections between the nodes represent:__{: style="color: blue"}  
    1. __What else is important to make it multi-layer? why/motivation (biologically and mathematically)?__{: style="color: blue"}  
    {: hidden=""}
1. __Describe "Learning" of an MLP (Learning Algorithm and brief description of the procedure and optimization):__{: style="color: red"}  
1. __List the properties of the MLP:__{: style="color: red"}  

***

## Deep Feedforward Neural Networks
1. __Describe the Deep Feedforward Neural Networks:__{: style="color: red"}  
    <button>Further Questions</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    1. __As a "Classifier" (from what does it learn and what does it define?):__{: style="color: blue"}  
    1. __What is its function?__{: style="color: blue"}  
        1. __How does it model the targets? (describe the underlying model and what it learns)__{: style="color: blue"}  
        1. __What does it learn?__{: style="color: blue"}  
    1. __What is its goal (besides trying to approximate the function on the training data)?__{: style="color: blue"}  
    1. __Why are they called "networks"/how are they represented?:__{: style="color: blue"}  
    {: hidden=""}

    <button>Further Further Questions</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
    1. __How are the Functions composed together?__{: style="color: blue"}    
    1. __How is this composition described?__{: style="color: blue"}  
    1. __What is the common structure for connecting the functions (from layer to layer)?__{: style="color: blue"}  
    1. __How do we define Depth:__{: style="color: blue"}  
    1. __What does the Training Data provide? and how do we learn from it?__{: style="color: blue"}  
    {: hidden=""}
1. __Describe the Motivation for Deep FFNs:__{: style="color: red"}  
    <button>Further Questions</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    1. __topic:__{: style="color: blue"}    
    {: hidden=""}
1. __How can we interpret Deep Neural Networks (in SLT):__{: style="color: red"}  


***

## AutoEncoders
1. __What is an AutoEncoder? What is its goal? (draw a diagram)__{: style="color: red"}  
1. __What type of NN is the Autoencoder?__{: style="color: red"}  
1. __Give Motivation for AutoEncoders:__{: style="color: red"}  
1. __Why Deep AutoEncoders? What do they allow us to do?__{: style="color: red"}  
1. __List the Advantages of Deep AutoEncoders:__{: style="color: red"}  
1. __List the Applications of AutoEncoders:__{: style="color: red"}  
1. __Describe the Training of Deep AutoEncoders:__{: style="color: red"}  
    <button>Extra</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    1. __What are the challenges if any?__{: style="color: blue"}  
    1. __What are the main methods for training Deep AutoEncoders?__{: style="color: blue"}  
    1. __Which one is the most superior method?__{: style="color: blue"}  
    {: hidden=""}

    <button>Extra Extra</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
    1. __How is Joint Training better:__{: style="color: blue"}  
    1. __Why is Joint Training better:__{: style="color: blue"}  
    {: hidden=""}
1. __Describe the Architecture of AutoEncoders:__{: style="color: red"}  
    1. __What is the simplest form of an AE:__{: style="color: blue"}  
    1. __What realm of "Learning" is employed for AEs?__{: style="color: blue"}  
1. __Mathematical Description of the Structure of AutoEncoders:__{: style="color: red"}  
    
    <button>Extra Extra</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
    1. __How do we define the "Encoder" and "Decoder"?__{: style="color: blue"}  
    1. __The Encoder maps what to what?__{: style="color: blue"}  
    1. __The Decoder maps what to what?__{: style="color: blue"}  
    1. __What is the type of loss?__{: style="color: blue"}  
    {: hidden=""}

    <button>Extra Extra</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
    1. __What are "Transition Functions"?__{: style="color: blue"}  
    {: hidden=""}
1. __Compare AutoEncoders and PCA (wrt what they learn):__{: style="color: red"}  
1. __List the different Types of AEs__{: style="color: red"}  
1. __How can we use AEs for Initialization?__{: style="color: red"}  
1. __Describe the Representational Power of AEs:__{: style="color: red"}  
    <button>Extra</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    1. __(wrt Layer Size and Depth):__{: style="color: red"}  
    1. __Why is Depth Important?__{: style="color: blue"}    
    {: hidden=""}
1. __Describe the progression (stages) of AE Architectures in CV:__{: style="color: red"}  

1. __What are *Undercomplete* AutoEncoders?__{: style="color: red"}  
1. __What's the motivation behind *Undercomplete* AEs?__{: style="color: red"}  
1. __List the Challenges of Utilizing Undercomplete AEs:__{: style="color: red"}  
1. __What is the Main Method/Approach of addressing the Challenges above (Training AEs)?__{: style="color: red"}  


<button>Further Questions</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
1. __Define Regularized Autoencoders:__{: style="color: red"}  
    1. __What does it allow us to do?__{: style="color: blue"}  
    1. __How does it address the Challenges?__{: style="color: blue"}  

    <button>Extra</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
    1. __What other Properties does it encourage to be learned?__{: style="color: blue"}    
    1. __What kind of technique (also type) of AEs can be "non-linear" and still learn useful codes?__{: style="color: blue"}  
    1. __What kind of technique-needed for (also type-of) AEs can be "overcomplete" and still learn useful codes?__{: style="color: blue"}  
    1. __What kind of technique-needed for (also type-of) AEs can be "nonlinear" AND "overcomplete" and still learn useful codes?__{: style="color: blue"}  
    1. __What are the ways to learn useful encodings/representations?__{: style="color: red"}  
        Defining an appropriate <span>__Objective and Objective Function__</span>{: style="color: purple"}.  
        1. __What types of objectives help learn useful encodings/representations?__{: style="color: red"}  
            __(regularized/approximate) Auto-Encoding__ - __Maximizing the Probability of training Data (NLL)__  
            [Further Info](/work_files/research/dl/archits/aencdrs#bodyContents24)  
    {: hidden=""}

1. __Describe the Relationship between Generative Models and AEs:__{: style="color: red"}  
    <button>Extra</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    1. __What are the components needed for the Generative Model?:__{: style="color: blue"}  
    1. __What notable types? List:__{: style="color: blue"}. 
    1. __Compare Generative Models & AEs in how they learn codings/representations:__{: style="color: blue"}  
    {: hidden=""}
    
    <button>Extra Extra</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
    1. __Why are their representations "naturally" useful?__{: style="color: blue"}  
    {: hidden=""}

1. __List the Different Types of Regularized Autoencoders:__{: style="color: red"}  
{: hidden=""}

<button>Further Further Questions (Regularized AEs)</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}  
1. __Define Sparse Autoencoders (w/ equation):__{: style="color: red"}  
1. __How can we interpret Sparse AEs? (Hint: 3 interpretations)__{: style="color: red"}  
    <button>Extra</button>{: .showText value="show" onclick="showTextPopHide(event);"}  
    1. __Give the "Regularization" Interpretation of Sparse AEs:__{: style="color: red"}  
    1. __Give the "Bayesian" Interpretation of Regularized AEs:__{: style="color: red"}  
    1. __Give the "Latent Variable" Interpretation of Sparse AEs:__{: style="color: red"}  
        <button>Extra Extra</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}  
        1. __What do Sparse AEs approximate?__{: style="color: blue"}  
        1. __How do they (does that) relate to MLE?__{: style="color: blue"}  
        {: hidden=""}  
    {: hidden=""}  
1. __Define Denoising Autoencoders:__{: style="color: red"}  
1. __What do they minimize? (canonical loss)__{: style="color: red"}  
1. __What do they learn? How? (compare)__{: style="color: red"}  
1. __How do we generate the inputs?__{: style="color: red"}  
    <button>Extra</button>{: .showText value="show" onclick="showTextPopHide(event);"}  
    1. __What does the "Corruption Process" represent/define?__{: style="color: blue"}  
    {: hidden=""}  
1. __How do we generate the training examples (input-output pair)? (process)__{: style="color: red"}  
1. __What does the Denoising AE learn specifically? (mathematically)__{: style="color: red"}  
    <button>Extra</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}  
    1. __What do we use as an estimate for the "Reconstruction Distribution"?__{: style="color: blue"}  
    1. __What is the output of the encoder $$f$$?__{: style="color: blue"}  
    1. __What is the output of the decoder $$g$$?__{: style="color: blue"}  
    1. __What is the "Reconstruction Distribution" equal to?__{: style="color: blue"}  
    {: hidden=""}  
1. __How do we Train the Denoising AE?__{: style="color: red"}  
    1. __What is the Loss?__{: style="color: blue"}  
    1. __What is the Optimization Method?__{: style="color: blue"}  
    1. __What is the Training similar to?__{: style="color: blue"}  
    1. __Is the Encoder Deterministic?__{: style="color: blue"}  
        1. __Would change if it was one or the other?__{: style="color: blue"}  
1. __How can we view the function of DAEs (wrt learning/training) from a Probabilistic pov?__{: style="color: red"}  
    <button>Extra</button>{: .showText value="show" onclick="showTextPopHide(event);"}  
    1. __What Expectation is it minimizing? Over what?__{: style="color: blue"}  
    1. __Can we re-write the Objective/Loss wrt the Empirical Distribution?__{: style="color: blue"}  
    {: hidden=""}  
1. __What other ways exist for learning/training DAEs?__{: style="color: red"}  
1. __How do DAEs and VAEs relate to each other?__{: style="color: red"}  

1. __Define Contractive Autoencoders__{: style="color: red"}  
    <button>Extra</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
    1. __What is the regularizer/penalty used?__{: style="color: blue"}    
    1. __What does it encourage the system to do?__{: style="color: blue"}  
    {: hidden=""}
1. __How is the Contractive AE connected to the DAE:__{: style="color: red"}  
1. __Why is the CAE called "Contractive"?__{: style="color: red"}  
    <button>Extra</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
    1. __Is it contractive locally or globally or both?__{: style="color: blue"}  
    1. __Give the Interpretation of the CAE as a Linear Operator:__{: style="color: blue"}  
    {: hidden=""}
1. __List the Issues associated with using a "Contractive Penalty":__{: style="color: red"}  
{: hidden=""}  
