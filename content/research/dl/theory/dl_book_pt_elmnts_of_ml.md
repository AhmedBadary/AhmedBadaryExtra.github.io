---
layout: NotesPage
title: Elements of Machine Learning
permalink: /work_files/research/dl/theory/dl_book_pt1
prevLink: /work_files/research/dl/theory.html
---


<div markdown="1" class = "TOC">
# Table of Contents

  * [Machine Learning Basics](#content1)
  {: .TOC1}
  * [The Mathematics of Neural Networks](#content2)
  {: .TOC2}
  * [Challenges in Machine Learning](#content3)
  {: .TOC3}
<!--   * [FOURTH](#content4)
  {: .TOC4}
  * [FIFTH](#content5)
  {: .TOC5}
  * [SIXTH](#content6)
  {: .TOC6} -->
</div>

***
***


* [Outline of Machine Learning - Wikipedia!](https://en.wikipedia.org/wiki/Outline_of_machine_learning)  


## Machine Learning Basics
{: #content1}

1. **Introduction and Definitions:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}
    * __Two Approaches to Statistics__:  
        * Frequentest Estimators  
        * Bayesian Inference  
    * __The Design Matrix__:  
        A common way for describing a dataset where it is a matrix containing a different example in each row. Each column of the matrix corresponds to a different feature.
    <br>

2. **Learning Algorithms:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}
    * __Learning__:  
        A computer program is said to learn from *__experience__* $$E$$ with respect to some class of *__tasks__* $$T$$ and *__performance measure__* $$P$$, if its performance at tasks in $$T$$, as measured by $$P$$, improves with experience $$E$$.  
    * __The Task $$T$$__:  
        <button>Show List</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        * *__Classification__*:  
            A task where the computer program is asked to specify which of $$k$$ categories some input belongs to.  
            To solve this task, the learning algorithm is usually asked to produce a function $$f:\mathbb{R}^n \rightarrow {1, . . . , k}$$.  
            When $$y=f(x)$$, the model assigns an input described by vector $$x$$ to a category identified by numeric code $$y$$.  
            > e.g. Object Recognition
        * *__Classification with Missing Inputs__*:  
            Classification becomes more challenging if the computer program is not guaranteed that every measurement in its input vector will always be provided.  
            To solve this task, rather than providing a single classification function (as in the normal classification case), the learning algorithm must learn a set of functions, each corresponding to classifying $$x$$ with a different subset of its inputs missing.  

            One way to efficiently define such a large set of functions is to learn a probability distribution over all the relevant variables, then solve the classification task by marginalizing out the missing variables.  
            With $$n$$ input variables, we can now obtain all $$2^n$$ different classification functions needed for each possible set of missing inputs, but the computer program needs to learn only a single function describing the joint probability distribution.  
            > e.g. Medical Diagnosis (where some tests weren't conducted for any reason)  
        * *__Regression__*:  
            A computer is asked to predict a numerical value given some input.  
            To solve this task, the learning algorithm is asked to output a function $$f:\mathbb{R}^n \rightarrow R$$  
            > e.g. Object Localization
        * *__Transcription__*:  
            In this type of task, the machine learning system is asked to observe a relatively unstructured representation of some kind of data and transcribe the information into discrete textual form.  
            > e.g. OCR
        * *__Machine Translation__*:  
            In a machine translation task, the input already consists of a sequence of symbols in some language, and the computer program must convert this into a sequence of symbols in another language.  
            > e.g. Google Translate  
        * *__Structured Output__*:  
            Structured output tasks involve any task where the output is a vector (or other data structure containing multiple values) with important relationships between the different elements.  
            This is a broad category and subsumes the transcription and translation tasks described above, as well as many other tasks.  
            These tasks are called structured output tasks because the program must output several values that are all tightly interrelated. For example, the words produced by an image captioning program must form a valid sentence.  
            > e.g. Syntax Parsing, Image Segmentation  
        * *__Anomaly Detection__*:  
            In this type of task, the computer program sifts through a set of events or objects and ﬂags some of them as being unusual or atypical.  
            > e.g. Insider Trading Detection
        * *__Synthesis and Sampling__*:  
            In this type of task, the machine learning algorithm is asked to generate new examples that are similar to those in the training data.  
            This is a kind of structured output task, but with the added qualification that there is no single correct output for each input, and we explicitly desire a large amount of variation in the output, in order for the output to seem more natural and realistic.  
            > e.g. Image Synthesis, Speech Synthesis
        * *__Imputation__*:  
            In this type of task, the machine learning algorithm is given a new example $$x \in \mathbb{R}^n$$, but with some entries $$x_i$$ of $$x$$ missing. The algorithm must provide a prediction of the values of the missing entries.  
        * *__Denoising__*:  
            In this type of task, the machine learning algorithm is given as input a corrupted example $$\tilde{x} \in \mathbb{R}^n$$ obtained by an unknown corruption process from a clean example $$x \in \mathbb{R}^n$$. The learner must predict the clean example $$x$$ from its corrupted version $$\tilde{x}$$, or more generally predict the conditional probability distribution $$p(x |\tilde{x})$$.  
            > e.g. Signal Reconstruction, Image Artifact Removal  
        * *__Density (Probability Mass Function) Estimation__*:  
            In the density estimation problem, the machine learning algorithm is asked to learn a function $$p_\text{model}: \mathbb{R}^n \rightarrow R$$, where $$p_\text{model}(x)$$ can be interpreted as a probability density function (if $$x$$ is continuous) or a probability mass function (if $$x$$ is discrete) on the space that the examples were drawn from.  
            To do such a task well, the algorithm needs to learn the structure of the data it has seen. It must know where _examples cluster tightly_ and where they are _unlikely to occur_.  
            Most of the tasks described above require the learning algorithm to at least implicitly capture the structure of the probability distribution (i.e. it can be computed but we don't have an equation for it). Density estimation enables us to explicitly capture that distribution.  
            In principle,we can then perform computations on that distribution to solve the other tasks as well.  
            For example, if we have performed density estimation to obtain a probability distribution p(x), we can use that distribution to solve the missing value imputation task. Equivalently, if a value $$x_i$$ is missing, and all the other values, denoted $$x_{−i}$$, are given, then we know the distribution over it is given by $$p(x_i| x_{−i})$$.  
                In practice, density estimation does not always enable us to solve all these related tasks, because in many cases the required operations on p(x) are computationally intractable.  
            > e.g. Language Modeling  
        * *__A Lot More__*:  
            Their are many more tasks that could be defined for and solved by Machine Learning. However, this is a list of the most common problems, which have a well-known set of methods for handling them.  
        {: hidden=""}
    * __The Performance Measure $$P$$__:  
        A quantitative measure of the performance of a machine learning algorithm.  
        We often use __accuracy__ or __error rate__.  
    <br>

55. **Machine Learning Methods:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents155}  
    * <button>[List of Machine Learning Methods](https://en.wikipedia.org/wiki/Outline_of_machine_learning#Machine_learning_methods)</button>{: .showText value="show" onclick="showTextPopHide(event);"}  
        * __Instance-based algorithm__
            * [K-nearest neighbors algorithm](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) (KNN)
            * [Learning vector quantization](https://en.wikipedia.org/wiki/Learning_vector_quantization) (LVQ)
            * [Self-organizing map](https://en.wikipedia.org/wiki/Self-organizing_map) (SOM)
        * __[Regression analysis](https://en.wikipedia.org/wiki/Regression_analysis)__
            * [Logistic regression](https://en.wikipedia.org/wiki/Logistic_regression)
            * [Ordinary least squares regression](https://en.wikipedia.org/wiki/Ordinary_least_squares_regression) (OLSR)
            * [Linear regression](https://en.wikipedia.org/wiki/Linear_regression)
            * [Stepwise regression](https://en.wikipedia.org/wiki/Stepwise_regression)
            * [Multivariate adaptive regression splines](https://en.wikipedia.org/wiki/Multivariate_adaptive_regression_splines) (MARS)
            * Regularization algorithm
                * [Ridge regression](https://en.wikipedia.org/wiki/Ridge_regression)
                * [Least Absolute Shrinkage and Selection Operator](https://en.wikipedia.org/wiki/Least_Absolute_Shrinkage_and_Selection_Operator) (LASSO)
                * [Elastic net](https://en.wikipedia.org/wiki/Elastic_net)
                * [Least-angle regression](https://en.wikipedia.org/wiki/Least-angle_regression) (LARS)
            * [Classifiers](https://en.wikipedia.org/wiki/Statistical_classification)
                * [Probabilistic classifier](https://en.wikipedia.org/wiki/Probabilistic_classifier)
                    * [Naive Bayes classifier](https://en.wikipedia.org/wiki/Naive_Bayes_classifier)
                * [Binary classifier](https://en.wikipedia.org/wiki/Binary_classifier)
                * [Linear classifier](https://en.wikipedia.org/wiki/Linear_classifier)
                * [Hierarchical classifier](https://en.wikipedia.org/wiki/Hierarchical_classifier)
        * [__Dimensionality reduction__](https://en.wikipedia.org/wiki/Dimensionality_reduction)
            * [Canonical correlation analysis](https://en.wikipedia.org/wiki/Canonical_correlation_analysis) (CCA)
            * [Factor analysis](https://en.wikipedia.org/wiki/Factor_analysis)
            * [Feature extraction](https://en.wikipedia.org/wiki/Feature_extraction)
            * [Feature selection](https://en.wikipedia.org/wiki/Feature_selection)
            * [Independent component analysis](https://en.wikipedia.org/wiki/Independent_component_analysis) (ICA)
            * [Linear discriminant analysis](https://en.wikipedia.org/wiki/Linear_discriminant_analysis) (LDA)
            * [Multidimensional scaling](https://en.wikipedia.org/wiki/Multidimensional_scaling) (MDS)
            * [Non-negative matrix factorization](https://en.wikipedia.org/wiki/Non-negative_matrix_factorization) (NMF)
            * [Partial least squares regression](https://en.wikipedia.org/wiki/Partial_least_squares_regression) (PLSR)
            * [Principal component analysis](https://en.wikipedia.org/wiki/Principal_component_analysis) (PCA)
            * [Principal component regression](https://en.wikipedia.org/wiki/Principal_component_regression) (PCR)
            * [Projection pursuit](https://en.wikipedia.org/wiki/Projection_pursuit)
            * [Sammon mapping](https://en.wikipedia.org/wiki/Sammon_mapping)
            * [t-distributed stochastic neighbor embedding](https://en.wikipedia.org/wiki/T-distributed_stochastic_neighbor_embedding) (t-SNE)
        * [__Ensemble learning__](https://en.wikipedia.org/wiki/Ensemble_learning)
            * [AdaBoost](https://en.wikipedia.org/wiki/AdaBoost)
            * [Boosting](https://en.wikipedia.org/wiki/Boosting_(machine_learning))
            * [Bootstrap aggregating](https://en.wikipedia.org/wiki/Bootstrap_aggregating) (Bagging)
            * [Ensemble averaging](https://en.wikipedia.org/wiki/Ensemble_averaging_(machine_learning)) – process of creating multiple models and combining them to produce a desired output, as opposed to creating just one model. Frequently an ensemble of models performs better than any individual model, because the various errors of the models "average out."
            * [Gradient boosted decision tree](https://en.wikipedia.org/wiki/Gradient_boosted_decision_tree) (GBDT)
            * [Gradient boosting](https://en.wikipedia.org/wiki/Gradient_boosting) machine (GBM)
            * [Random Forest](https://en.wikipedia.org/wiki/Random_Forest)
            * [Stacked Generalization](https://en.wikipedia.org/wiki/Stacked_Generalization) (blending)
        * [__Meta learning__](https://en.wikipedia.org/wiki/Meta_learning_(computer_science))
            * [Inductive bias](https://en.wikipedia.org/wiki/Inductive_bias)
            * [Metadata](https://en.wikipedia.org/wiki/Metadata)
        * [__Reinforcement learning__](https://en.wikipedia.org/wiki/Reinforcement_learning)
            * [Q-learning](https://en.wikipedia.org/wiki/Q-learning)
            * [State–action–reward–state–action](https://en.wikipedia.org/wiki/State%E2%80%93action%E2%80%93reward%E2%80%93state%E2%80%93action) (SARSA)
            * [Temporal difference learning](https://en.wikipedia.org/wiki/Temporal_difference_learning) (TD)
            * [Learning Automata](https://en.wikipedia.org/wiki/Learning_Automata)
        * [__Supervised learning__](https://en.wikipedia.org/wiki/Supervised_learning)
            * [AODE](https://en.wikipedia.org/wiki/AODE)
            * [Artificial neural network](https://en.wikipedia.org/wiki/Artificial_neural_network)
            * [Association rule learning](https://en.wikipedia.org/wiki/Association_rule_learning) algorithms
                * [Apriori algorithm](https://en.wikipedia.org/wiki/Apriori_algorithm)
                * [Eclat algorithm](https://en.wikipedia.org/wiki/Eclat_algorithm)
            * [Case-based reasoning](https://en.wikipedia.org/wiki/Case-based_reasoning)
            * [Gaussian process regression](https://en.wikipedia.org/wiki/Gaussian_process_regression)
            * [Gene expression programming](https://en.wikipedia.org/wiki/Gene_expression_programming)
            * [Group method of data handling](https://en.wikipedia.org/wiki/Group_method_of_data_handling) (GMDH)
            * [Inductive logic programming](https://en.wikipedia.org/wiki/Inductive_logic_programming)
            * [Instance-based learning](https://en.wikipedia.org/wiki/Instance-based_learning)
            * [Lazy learning](https://en.wikipedia.org/wiki/Lazy_learning)
            * [Learning Automata](https://en.wikipedia.org/wiki/Learning_Automata)
            * [Learning Vector Quantization](https://en.wikipedia.org/wiki/Learning_Vector_Quantization)
            * [Logistic Model Tree](https://en.wikipedia.org/wiki/Logistic_Model_Tree)
            * [Minimum message length](https://en.wikipedia.org/wiki/Minimum_message_length) (decision trees, decision graphs, etc.)
                * [Nearest Neighbor Algorithm](https://en.wikipedia.org/wiki/Nearest_neighbor_(pattern_recognition))
                * [Analogical modeling](https://en.wikipedia.org/wiki/Analogical_modeling)
            * [Probably approximately correct learning](https://en.wikipedia.org/wiki/Probably_approximately_correct_learning) (PAC) learning
            * [Ripple down rules](https://en.wikipedia.org/wiki/Ripple_down_rules), a knowledge acquisition methodology
            * Symbolic machine learning algorithms
            * [Support vector machines](https://en.wikipedia.org/wiki/Support_vector_machine)
            * [Random Forests](https://en.wikipedia.org/wiki/Random_forest)
            * [Ensembles of classifiers](https://en.wikipedia.org/wiki/Ensembles_of_classifiers)
                * [Bootstrap aggregating](https://en.wikipedia.org/wiki/Bootstrap_aggregating) (bagging)
                * [Boosting (meta-algorithm)](https://en.wikipedia.org/wiki/Boosting_(meta-algorithm))
            * [Ordinal classification](https://en.wikipedia.org/wiki/Ordinal_classification)
            * [Information fuzzy networks](https://en.wikipedia.org/wiki/Information_Fuzzy_Networks) (IFN)
            * [Conditional Random Field](https://en.wikipedia.org/wiki/Conditional_Random_Field)
            * [ANOVA](https://en.wikipedia.org/wiki/ANOVA)
            * [Quadratic classifiers](https://en.wikipedia.org/wiki/Quadratic_classifier)
            * [k-nearest neighbor](https://en.wikipedia.org/wiki/Nearest_neighbor_(pattern_recognition))
            * [Boosting](https://en.wikipedia.org/wiki/Boosting_(machine_learning))
                * SPRINT
            * [Bayesian networks](https://en.wikipedia.org/wiki/Bayesian_network)
                * [Naive Bayes](https://en.wikipedia.org/wiki/Naive_Bayes)
            * [Hidden Markov models](https://en.wikipedia.org/wiki/Hidden_Markov_model)
                * [Hierarchical hidden Markov model](https://en.wikipedia.org/wiki/Hierarchical_hidden_Markov_model)
        * [__Bayesian statistics__](https://en.wikipedia.org/wiki/Bayesian_statistics)
            * Bayesian knowledge base
            * [Naive Bayes](https://en.wikipedia.org/wiki/Naive_Bayes)
            * [Gaussian Naive Bayes](https://en.wikipedia.org/wiki/Gaussian_Naive_Bayes)
            * [Multinomial Naive Bayes](https://en.wikipedia.org/wiki/Multinomial_Naive_Bayes)
            * [Averaged One-Dependence Estimators](https://en.wikipedia.org/wiki/Averaged_One-Dependence_Estimators) (AODE)
            * [Bayesian Belief Network](https://en.wikipedia.org/wiki/Bayesian_Belief_Network) (BBN)
            * [Bayesian Network](https://en.wikipedia.org/wiki/Bayesian_Network) (BN)
        * __Decision tree algorithms__  
            * [Decision tree](https://en.wikipedia.org/wiki/Decision_tree)
            * [Classification and regression tree](https://en.wikipedia.org/wiki/Classification_and_regression_tree) (CART)
            * [Iterative Dichotomiser 3](https://en.wikipedia.org/wiki/Iterative_Dichotomiser_3) (ID3)
            * [C4.5 algorithm](https://en.wikipedia.org/wiki/C4.5_algorithm)
            * [C5.0 algorithm](https://en.wikipedia.org/wiki/C5.0_algorithm)
            * [Chi-squared Automatic Interaction Detection](https://en.wikipedia.org/wiki/Chi-squared_Automatic_Interaction_Detection) (CHAID)
            * [Decision stump](https://en.wikipedia.org/wiki/Decision_stump)
            * Conditional decision tree
            * [ID3 algorithm](https://en.wikipedia.org/wiki/ID3_algorithm)
            * [Random forest](https://en.wikipedia.org/wiki/Random_forest)
            * SLIQ
        * [__Linear classifier__](https://en.wikipedia.org/wiki/Linear_classifier)
            * [Fisher's linear discriminant](https://en.wikipedia.org/wiki/Fisher%27s_linear_discriminant)
            * [Linear regression](https://en.wikipedia.org/wiki/Linear_regression)
            * [Logistic regression](https://en.wikipedia.org/wiki/Logistic_regression)
            * [Multinomial logistic regression](https://en.wikipedia.org/wiki/Multinomial_logistic_regression)
            * [Naive Bayes classifier](https://en.wikipedia.org/wiki/Naive_Bayes_classifier)
            * [Perceptron](https://en.wikipedia.org/wiki/Perceptron)
            * [Support vector machine](https://en.wikipedia.org/wiki/Support_vector_machine)
        * [__Unsupervised learning__](https://en.wikipedia.org/wiki/Unsupervised_learning)
            * [Expectation-maximization algorithm](https://en.wikipedia.org/wiki/Expectation-maximization_algorithm)
            * [Vector Quantization](https://en.wikipedia.org/wiki/Vector_Quantization)
            * [Generative topographic map](https://en.wikipedia.org/wiki/Generative_topographic_map)
            * [Information bottleneck method](https://en.wikipedia.org/wiki/Information_bottleneck_method)
        * [__Artificial neural network__](https://en.wikipedia.org/wiki/Artificial_neural_network)
            * [Feedforward neural network](https://en.wikipedia.org/wiki/Feedforward_neural_network)
                * [Extreme learning machine](https://en.wikipedia.org/wiki/Extreme_learning_machine)
                * [Convolutional neural network](https://en.wikipedia.org/wiki/Convolutional_neural_network)
            * [Recurrent neural network](https://en.wikipedia.org/wiki/Recurrent_neural_network)
                * [Long short-term memory (LSTM)](https://en.wikipedia.org/wiki/Long_short-term_memory)
            * [Logic learning machine](https://en.wikipedia.org/wiki/Logic_learning_machine)
            * [Self-organizing map](https://en.wikipedia.org/wiki/Self-organizing_map)
        * [__Association rule learning__](https://en.wikipedia.org/wiki/Association_rule_learning)
            * [Apriori algorithm](https://en.wikipedia.org/wiki/Apriori_algorithm)
            * [Eclat algorithm](https://en.wikipedia.org/wiki/Eclat_algorithm)
            * [FP-growth algorithm](https://en.wikipedia.org/wiki/Association_rule_learning#FP-growth_algorithm)
        * [__Hierarchical clustering__](https://en.wikipedia.org/wiki/Hierarchical_clustering)
            * [Single-linkage clustering](https://en.wikipedia.org/wiki/Single-linkage_clustering)
            * [Conceptual clustering](https://en.wikipedia.org/wiki/Conceptual_clustering)
        * [__Cluster analysis__](https://en.wikipedia.org/wiki/Cluster_analysis)
            * [BIRCH](https://en.wikipedia.org/wiki/BIRCH)
            * [DBSCAN](https://en.wikipedia.org/wiki/DBSCAN)
            * [Expectation-maximization (EM)](https://en.wikipedia.org/wiki/Expectation-maximization_algorithm)
            * [Fuzzy clustering](https://en.wikipedia.org/wiki/Fuzzy_clustering)
            * [Hierarchical Clustering](https://en.wikipedia.org/wiki/Hierarchical_Clustering)
            * [K-means clustering](https://en.wikipedia.org/wiki/K-means_clustering)
            * [K-medians](https://en.wikipedia.org/wiki/K-medians)
            * [Mean-shift](https://en.wikipedia.org/wiki/Mean-shift)
            * [OPTICS algorithm](https://en.wikipedia.org/wiki/OPTICS_algorithm)
        * [__Anomaly detection__](https://en.wikipedia.org/wiki/Anomaly_detection)
            * [k-nearest neighbors classification](https://en.wikipedia.org/wiki/K-nearest_neighbors_classification) (_k_-NN)
            * [Local outlier factor](https://en.wikipedia.org/wiki/Local_outlier_factor)
        * [__Semi-supervised learning__](https://en.wikipedia.org/wiki/Semi-supervised_learning)
            * [Active learning](https://en.wikipedia.org/wiki/Active_learning_(machine_learning)) – special case of semi-supervised learning in which a learning algorithm is able to interactively query the user (or some other information source) to obtain the desired outputs at new data points.[[5]](https://en.wikipedia.org/wiki/Outline_of_machine_learning#cite_note-settles-5)[[6]](https://en.wikipedia.org/wiki/Outline_of_machine_learning#cite_note-rubens2016-6)
            * [Generative models](https://en.wikipedia.org/wiki/Semi-supervised_learning#Generative_models)
            * [Low-density separation](https://en.wikipedia.org/wiki/Semi-supervised_learning#Low-density_separation)
            * [Graph-based methods](https://en.wikipedia.org/wiki/Semi-supervised_learning#Graph-based_methods)
            * [Co-training](https://en.wikipedia.org/wiki/Co-training)
            * [Transduction](https://en.wikipedia.org/wiki/Transduction_(machine_learning))
        * [__Deep learning__](https://en.wikipedia.org/wiki/Deep_learning)
            * [Deep belief networks](https://en.wikipedia.org/wiki/Deep_belief_network)
            * Deep [Boltzmann machines](https://en.wikipedia.org/wiki/Boltzmann_machine)
            * Deep [Convolutional neural networks](https://en.wikipedia.org/wiki/Convolutional_neural_network)
            * Deep [Recurrent neural networks](https://en.wikipedia.org/wiki/Recurrent_neural_network)
            * [Hierarchical temporal memory](https://en.wikipedia.org/wiki/Hierarchical_temporal_memory)
            * [Generative Adversarial Networks](https://en.wikipedia.org/wiki/Generative_adversarial_network)
            * [Deep Boltzmann Machine](https://en.wikipedia.org/wiki/Deep_Boltzmann_Machine) (DBM)
            * [Stacked Auto-Encoders](https://en.wikipedia.org/wiki/Stacked_Auto-Encoders)
        * __Other machine learning methods and problems__
            * [Anomaly detection](https://en.wikipedia.org/wiki/Anomaly_detection)
            * [Association rules](https://en.wikipedia.org/wiki/Association_rule_learning)
            * [Bias-variance dilemma](https://en.wikipedia.org/wiki/Bias-variance_dilemma)
            * [Classification](https://en.wikipedia.org/wiki/Statistical_classification)
                * [Multi-label classification](https://en.wikipedia.org/wiki/Multi-label_classification)
            * [Clustering](https://en.wikipedia.org/wiki/Cluster_analysis)
            * [Data Pre-processing](https://en.wikipedia.org/wiki/Data_Pre-processing)
            * [Empirical risk minimization](https://en.wikipedia.org/wiki/Empirical_risk_minimization)
            * [Feature engineering](https://en.wikipedia.org/wiki/Feature_engineering)
            * [Feature learning](https://en.wikipedia.org/wiki/Feature_learning)
            * [Learning to rank](https://en.wikipedia.org/wiki/Learning_to_rank)
            * [Occam learning](https://en.wikipedia.org/wiki/Occam_learning)
            * [Online machine learning](https://en.wikipedia.org/wiki/Online_machine_learning)
            * [PAC learning](https://en.wikipedia.org/wiki/PAC_learning)
            * [Regression](https://en.wikipedia.org/wiki/Regression_analysis)
            * [Reinforcement Learning](https://en.wikipedia.org/wiki/Reinforcement_Learning)
            * [Semi-supervised learning](https://en.wikipedia.org/wiki/Semi-supervised_learning)
            * [Statistical learning](https://en.wikipedia.org/wiki/Statistical_learning)
            * [Structured prediction](https://en.wikipedia.org/wiki/Structured_prediction)
                * [Graphical models](https://en.wikipedia.org/wiki/Graphical_model)
                    * [Bayesian network](https://en.wikipedia.org/wiki/Bayesian_network)
                    * [Conditional random field](https://en.wikipedia.org/wiki/Conditional_random_field) (CRF)
                    * [Hidden Markov model](https://en.wikipedia.org/wiki/Hidden_Markov_model) (HMM)
            * [Unsupervised learning](https://en.wikipedia.org/wiki/Unsupervised_learning)
            * [VC theory](https://en.wikipedia.org/wiki/VC_theory)
        {: hidden=""}
    <br>


11. **Learning vs Optimization:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents111}  
    __Generalization:__ is the ability to perform well on previously unobserved inputs.  
    __Generalization (Test) Error:__ is defined as the expected value of the error on a new input.  

    __Learning vs Optimization:__{: style="color: red"}  
    {: #lst-p}
    * The problem of Reducing the __training error__ on the __training set__ is one of *__optimization__*.  
    * The problem of Reducing the __training error__, as well as, the __generalization (test) error__ is one of *__learning__*.  
    <br>

22. **Statistical Learning Theory:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents122}  
    It is a framework that, under certain assumptions, allows us to study the question of "
    How can we affect performance on the test set when we can observe only the training set?"  

    __Assumptions:__  
    {: #lst-p}
    * The training and test data are generated by a _probability distribution over datasets_ called the __data-generating process__.  
    * The __i.i.d. assumptions:__  
        * The examples in each dataset are __independent__ from each other  
        * The _training set_ and _test set_ are __identically distributed__ (drawn from the same probability distribution as each other)  

        This assumption enables us to describe the data-generating process with a probability distribution over a single example. The same distribution is then used to generate every train example and every test example.  
    * We call that shared underlying distribution the __data-generating distribution__, denoted $$p_{\text{data}}$$  

    This probabilistic framework and the i.i.d. assumptions enable us to mathematically study the relationship between training error and test error.  

33. **Capacity, Overfitting, and Underfitting:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents133}  
    The __ML process:__  
    We sample the training set, then use it to choose the parameters to reduce training set error, then sample the test set.  
    Under this process, the __expected test error is greater than or equal to the expected value of training error__.  

    The factors determining how well a machine learning algorithm will perform are its ability to:  
    {: #lst-p}
    1. Make the training error small
    2. Make the gap between training and test error small  
    
    These two factors correspond to the two central challenges in machine learning: __underfitting__ and __overfitting__.  
    __Underfitting:__  occurs when the model is not able to obtain a sufficiently low error value on the training set.  
    __Overfitting:__ occurs when the gap between the training error and test error is too large.  

    We can control whether a model is more likely to overfit or underfit by altering its __capacity__.  
    __Capacity:__ a models capacity is its ability to fit a wide variety of functions.  
    {: #lst-p}
    * Models with __low capacity__ may struggle to fit the training set. 
    * Models with __high capacity__ can overfit by memorizing properties of the training set that do not serve them well on the test set. 

    One way to control the __capacity__ of a learning algorithm is by choosing its __hypothesis space__.  
    __Hypothesis Space:__ the set of functions that the learning algorithm is allowed to select as being the solution.  

    Statistical learning theory provides various means of quantifying model capacity.Among these, the most well known is the __Vapnik-Chervonenkis (VC) dimension__.  
    __The VC Dimension:__ is defined as being the largest possible value of $$m$$ for which there exists a training set of $$m$$ different $$\mathbf{x}$$ points that the classifier can label arbitrarily.  
    It measure the *__capacity of a binary classifier__*.  

    Quantifying the capacity of the model enables statistical learning theory to make quantitative predictions. The most important results in statistical learning theory show that the *__discrepancy between training error and generalization error is bounded from above by a quantity that grows as the model capacity grows but shrinks as the number of training examples increases__*.  

    ![img](/main_files/dl_book/10.png){: width="90%"}   



    > Effective capacity and Representational Capacity...  


33. **Regularization:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents133}  
    __Regularization__ is a (more general) way of controlling a models capacity by allowing us to express _preference_ for one function over another in the same hypothesis space; instead of including or excluding members from the hypothesis space completely.  
    > We can think of excluding a function from a hypothesis space as expressing an infinitely strong preference against that function.  

    __Regularization__ can be defined as any modification we make to a learning algorithm that is intended to reduce its generalization error but not its training error.  

    __Example: Weight Decay__  
    It is a regularization form that adds the $$L^2$$ norm of the __weights__ to the cost function; allowing us to express preference for smaller weights. It is controlled by a hyperparameter $$\lambda$$.  
    <p>$$J(\boldsymbol{w})=\mathrm{MSE}_ {\mathrm{train}}+\lambda \boldsymbol{w}^{\top} \boldsymbol{w}$$</p>   
    This gives us solutions that have a smaller slope, or that put weight on fewer of the features.  

    More generally, the __regularizer__ penalty of __weight decay__ is:  
    <p>$$\Omega(\boldsymbol{w})=\boldsymbol{w}^{\top} \boldsymbol{w}$$</p>   

    <br>

34. **Point Estimation:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents134}  
    Point estimation is the attempt to provide the single “best” prediction of some quantity of interest.  In general the quantity of interest can be a single parameter or a vector of parameters in some parametric model, such as the *__weights in linear regression__*, but it can also be a *__whole function__*.  
    <br>

3. **Estimators:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    A __Point Estimator__ or __statistic__ is any function of the data:  
    <p>$$\hat{\boldsymbol{\theta}}_{m}=g\left(\boldsymbol{x}^{(1)}, \ldots, \boldsymbol{x}^{(m)}\right)$$</p>  
    such that a good estimator is a function whose output is close to the true underlying $$ \theta $$ that generated the training data.  
    > We assume that the true $$\boldsymbol{\theta}$$ is fixed, and that $$\hat{\boldsymbol{\theta}}$$ is a function of the data, which is drawn from a random process, making $$\hat{\boldsymbol{\theta}}$$ a __random variable__.  


    __Function Estimation/Approximation__ refers to estimation of the relationship between _input_ and _target data_.  
    I.E. We are trying to predict a variable $$y$$ given an input vector $$x$$, and we assume that there is a function $$f(x)$$ that describes the approximate relationship between $$y$$ and $$x$$.  
    If we assume that: $$y = f(x) + \epsilon$$, where $$\epsilon$$ is the part of $$y$$ that is not predictable from $$x$$; then we are interested in approximating $$f$$ with a model or estimate $$ \hat{f} $$.  
    > Function estimation is really just the same as estimating a parameter $$\boldsymbol{\theta}$$; the function estimator $$ \hat{f} $$ is simply a point estimator in function space.  

    Linear Regression and Polynomial Regression both illustrate scenarios that may be interpreted as either estimating a parameter $$\boldsymbol{w}$$ or estimating a function $$f$$ mapping from $$\boldsymbol{x}$$ to $$y$$.

    * [**Estimators as statistics and their probability distributions**](https://www.youtube.com/embed/lr5WH-JVT5I){: value="show" onclick="iframePopA(event)"}
    <a href="https://www.youtube.com/embed/lr5WH-JVT5I"></a>
        <div markdown="1"> </div>    
    * [Estimators in ML](https://deepai.org/machine-learning-glossary-and-terms/estimator)  
    * [Plain and Simple Estimators (TF)](https://towardsdatascience.com/plain-and-simple-estimators-d8d3f4c185c1)  


    __Notes:__  
    {: #lst-p}
    * weights $$\boldsymbol{w}$$ == parameters $$\theta$$
    * parameter/point estimation == function estimation
        Linear Regression and Polynomial Regression both illustrate scenarios that may be interpreted as either estimating a parameter $$\boldsymbol{w}$$ or estimating a function $$f$$ mapping from $$\boldsymbol{x}$$ to $$y$$.  
    * we can use the theory and tools for analyzing point estimators and apply them to function estimators (e.g. bias/var decomp etc.)

    <br>


4. **Properties of Estimators - Bias and Variance:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    The __Bias__ of an estimator is:  
    <p>$$ \operatorname{bias}\left(\hat{\boldsymbol{\theta}}_{m}\right)=\mathbb{E}\left(\hat{\boldsymbol{\theta}}_{m}\right)-\boldsymbol{\theta} $$</p>  
    where the expectation is over the data (seen as samples from a random variable) and $$ \theta $$ is the true underlying value of $$ \theta $$ used to define the data-generating distribution.  
    * __Unbiased Estimators:__ An estimator $$\hat{\boldsymbol{\theta}}_{m}$$ is said to be __unbiased__ if $$\operatorname{bias}\left(\hat{\boldsymbol{\theta}}_{m}\right)=\mathbf{0}$$, which implies that $$ \mathbb{E}\left(\hat{\boldsymbol{\theta}}_{m}\right)=\boldsymbol{\theta} $$.  
    * __Asymptotically Unbiased Estimators:__ An estimator is said to be __asymptotically unbiased__ if $$ \lim _{m \rightarrow \infty} \operatorname{bias}\left(\hat{\boldsymbol{\theta}}_{m}\right)=\mathbf{0},$$ which implies that $$\lim _{m \rightarrow \infty} \mathbb{E}\left(\hat{\boldsymbol{\theta}}_{m}\right)=\boldsymbol{\theta} $$  

    The __Variance__ of an estimator is a way to measure how much we expect the estimator to vary as a function of the data sample, defined, simply, as the variance over the training set random variable $$\hat{\theta}$$:  
    <p>$$ \operatorname{Var}(\hat{\theta}) $$</p>  

    The __Standard Error__ $$\operatorname{SE}(\hat{\theta})$$, of an estimator, is the square root of the variance.  
    * E.g. __The Standard Error of the (Sample) Mean:__  
        $$\operatorname{SE}\left(\hat{\mu}_{m}\right)=\sqrt{\operatorname{Var}\left[\frac{1}{m} \sum_{i=1}^{m} x^{(i)}\right]}=\frac{\sigma}{\sqrt{m}}$$  
        Where $$\sigma^2$$ is the true variance of the samples $$x^i$$.  

        <button>Derivation</button>{: .showText value="show"
        onclick="showText_withParent_PopHide(event);"}
        <p hidden="">$$\begin{aligned} \operatorname{Var}\left[\overline{X}_{n}\right] &=\operatorname{Var}\left[\frac{1}{n} \sum_{i=1}^{n} X_{i}\right] \\ &=\frac{1}{n^{2}} \operatorname{Var}\left[\sum_{i=1}^{n} X_{i}\right] \\ &=\frac{1}{n^{2}} \sum_{i=1}^{n} \operatorname{Var}\left[X_{i}\right] \\ &=\frac{1}{n^{2}} \sum_{i=1}^{n} \sigma^{2} \\ &=\frac{1}{n^{2}} n \sigma^{2}=\frac{\sigma^{2}}{n} \end{aligned}$$</p>  

    > Unfortunately, neither the square root of the sample variance nor the square root of the unbiased estimator of the variance provide an unbiased estimate of the standard deviation.  

    * [Properties of the Sample Mean Estimator (Derivations)](https://www.statlect.com/fundamentals-of-statistics/mean-estimation)  
    <br>

5. **Generalization Error from Standard Error (of the mean):**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  
    We often estimate the __generalization error__ by computing the __sample mean__ of the error on the test set.  
    Taking advantage of the central limit theorem, which tells us that the mean will be approximately distributed with a normal distribution, we can use the standard error to compute the probability that the true expectation falls in any chosen interval.  
    For example, the 95 percent confidence interval centered on the mean $$\hat{\mu}_ {m}$$ is:  
    <p>$$\left(\hat{\mu}_{m}-1.96 \mathrm{SE}\left(\hat{\mu}_{m}\right), \hat{\mu}_{m}+1.96 \mathrm{SE}\left(\hat{\mu}_{m}\right)\right)$$</p>  
    under the normal distribution with mean $$\hat{\mu}_{m}$$ and variance $$\mathrm{SE}\left(\hat{\mu}_{m}\right)^{2}$$.  
    We say that algorithm $$\boldsymbol{A}$$ is __better than__ algorithm $$\boldsymbol{B}$$ if the _upper bound_ of the $$95$$ percent confidence interval for the error of algorithm $$\boldsymbol{A}$$ is __less than__ the _lower bound_ of the $$95$$ percent confidence interval for the error of algorithm $$\boldsymbol{B}$$.  

6. **The Bias Variance Trade-off:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}  
    Bias and variance measure two different sources of error in an estimator:  
    * __Bias__: measures the expected deviation from the true value of the function or parameter  
    * __Variance__: provides a measure of the deviation from the expected estimator value that any particular sampling of the data is likely to cause  

    __Evaluating Models - Trading off Bias and Variance:__  
    {: #lst-p}
    * The most common way to negotiate this trade-off is to use __cross-validation__
    * Alternatively, we can also compare the __mean squared error (MSE)__ of the estimates:  
        <p>$$\begin{aligned} \mathrm{MSE} &=\mathbb{E}\left[\left(\hat{\theta}_{m}-\theta\right)^{2}\right] \\ &=\operatorname{Bias}\left(\hat{\theta}_{m}\right)^{2}+\operatorname{Var}\left(\hat{\theta}_{m}\right) \end{aligned}$$</p>  
        The __MSE__ measures the overall expected deviation — in a squared error sense — between the estimator and the true value of the parameter $$\theta$$.  

    <button>Capacity and Bias/Variance</button>{: .showText value="show"
     onclick="showTextPopHide(event);"}
    ![img](/main_files/dl_book/1.png){: hidden=""}  


7. **Properties of Estimators - Consistency:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}  
    __Consistency__ is a property implying that as the number of data points $$m$$ in our dataset increases, our point estimates converge to the true value of the corresponding parameters. Formally:  
    <p>$$\mathrm{plim}_{m \rightarrow \infty} \hat{\theta}_{m}=\theta$$</p>  
    Where:    
    $${\text { The symbol plim indicates convergence in probability, meaning that for any } \epsilon>0,}$$ 
    <p>$${P\left(\vert\hat{\theta}_ {m}-\theta \vert>\epsilon\right) \rightarrow 0 \text { as } m \rightarrow \infty}$$</p>  
    > Sometimes referred to as __Weak Consistency__  

    __Strong Consistency__ applies to *__almost sure convergence__* of $$\hat{\theta}$$ to $$\theta$$.  

    __Consistency and Asymptotic Bias:__  
    {: #lst-p}
    * Consistency ensures that the bias induced by the estimator diminishes as the number of data examples grows.  
    * However, asymptotic unbiasedness does __not__ imply consistency  
        * It is also useful to note that by Chebyshev's inequality, if the variance tends to zero then asymptotic unbiasedness implies consistency [stex](https://math.stackexchange.com/questions/239146/consistency-and-asymptotically-unbiasedness).  

    | Consistency implies both unbiasedness and low variance and therefore, unbiasedness alone is not sufficient to imply consistency.

    <br>

8. **Maximum Likelihood Estimation (MLE):**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18}  
    __MLE__ is a method/principle from which we can derive specific functions that are *__good estimators__* for different models.  

    > Likelihood is the probability of the data given the parameters of the model  

    Let $$\mathbb{X}=\left\{\boldsymbol{x}^{(1)}, \ldots, \boldsymbol{x}^{(m)}\right\}$$ be a set of $$m$$ examples drawn _independently_ from the true but unknown data-generating distribution $$p_{\text{data}}(\mathbf{x})$$, and let $$p_{\text{model}}(\mathbf{x} ; \boldsymbol{\theta})$$ be a _parametric_ family of probability distributions over the same space indexed by $$\boldsymbol{\theta}$$[^4],  
    The Maximum Likelihood Estimator for $$\boldsymbol{\theta}$$ is:  
    <p>$$\begin{aligned} \boldsymbol{\theta}_{\mathrm{ML}} &=\underset{\boldsymbol{\theta}}{\arg \max } \: p_{\text{model}}(\mathbb{X} ; \boldsymbol{\theta}) \\ &=\underset{\boldsymbol{\theta}}{\arg \max } \prod_{i=1}^{m} p_{\text{model}}\left(\boldsymbol{x}^{(i)} ; \boldsymbol{\theta}\right) \end{aligned}$$</p>  
    We take the $$log$$ for _numerical stability_:  
    <p>$$\boldsymbol{\theta}_{\mathrm{ML}}=\underset{\boldsymbol{\theta}}{\arg \max } \sum_{i=1}^{m} \log p_{\text{model}}\left(\boldsymbol{x}^{(i)} ; \boldsymbol{\theta}\right) \tag{5.58}$$</p>  
    Because the $$\text { arg max }$$ does not change when we rescale the cost function, we can divide by $$m$$ to obtain a version of the criterion that is expressed as an __expectation with respect to the empirical distribution $$\hat{p}_ {\text{data}}$$__  defined by the training data:  
    <p>$$\boldsymbol{\theta}_{\mathrm{ML}}=\underset{\boldsymbol{\theta}}{\arg \max } \: 
        \underset{\mathbf{x} \sim \hat{p}_\text{data}}{\mathbb{E}} [\log p_{\text{model}}(\boldsymbol{x} ; \boldsymbol{\theta})] \tag{5.59}$$</p>  

    __MLE as Minimizing KL-Divergence between the Empirical dist. and the model dist.:__{: style="color: red"}  
    We can interpret maximum likelihood estimation as _minimizing the dissimilarity_ between the __empirical distribution $$\hat{p}_ {\text{data}}$$__, defined by the training set, and the __model distribution__, with the degree of dissimilarity between the two measured by the __KL divergence__.  
    * The __KL-divergence__ is given by:  
        <p>$$D_{\mathrm{KL}}\left(\hat{p}_{\text{data}} \| p_{\text{model}}\right)=\mathbb{E}_{\mathbf{x} \sim \hat{p}_{\text{data}}}\left[\log \hat{p}_{\text{data}}(\boldsymbol{x})-\log p_{\text{model}}(\boldsymbol{x})\right] \tag{5.60}$$</p>  
    The term on the left is a function only of the data-generating process, not the model. This means when we train the model to minimize the KL divergence, we need only minimize:  
    <p>$$-\mathbb{E}_{\mathbf{x} \sim \hat{p}_{\text{data}}}\left[\log p_{\text{model}}(\boldsymbol{x})\right] \tag{5.61}$$</p>  
    which is of course the same as the _maximization_ in equation $$5.59$$.  

    Minimizing this KL-divergence corresponds exactly to __minimizing the cross-entropy between the distributions__.  
    > Any loss consisting of a negative log-likelihood is a cross-entropy between the empirical distribution defined by the training set and theprobability distribution defined by model.  
    > E.g. __MSE__ is the _cross-entropy_ between the __empirical distribution__ and a __Gaussian model__.  

    We can thus see maximum likelihood as an attempt to _make the model distribution match the empirical distribution $$\hat{p} _ {\text{data}}$$_[^5].  

    Maximum likelihood thus becomes minimization of the negative log-likelihood(NLL), or equivalently, minimization of the cross-entropy[^6].  

    * [MLE as Minimizing KL-div](http://www.jessicayung.com/maximum-likelihood-as-minimising-kl-divergence/)  


    __Conditional Log-Likelihood (MLE for Supervised Learning):__{: style="color: red"}  
    The maximum likelihood estimator can readily be generalized to estimate a _conditional probability $$P(\mathbf{y} | \mathbf{x} ; \boldsymbol{\theta})$$_ in order to predict $$\mathbf{y}$$  given $$\mathbf{x}$$. If $$X$$ represents all our inputs and $$Y$$ all our observed targets, then the conditional maximum likelihood estimator is:  
    <p>$$\boldsymbol{\theta}_ {\mathrm{ML}}=\underset{\boldsymbol{\theta}}{\arg \max } \: P(\boldsymbol{Y} | \boldsymbol{X} ; \boldsymbol{\theta}) \tag{5.62}$$</p>  
    and the log-likelihood estimator is:  
    <p>$$\boldsymbol{\theta}_{\mathrm{ML}}=\underset{\boldsymbol{\theta}}{\arg \max } \sum_{i=1}^{m} \log P\left(\boldsymbol{y}^{(i)} | \boldsymbol{x}^{(i)} ; \boldsymbol{\theta}\right) \tag{5.63}$$</p>  


    __Properties of Maximum Likelihood Estimator:__{: style="color: red"}  
    The main appeal of the maximum likelihood estimator is that it can be shown to be the _best estimator asymptotically_, as the number of examples $$m \rightarrow \infty$$, in terms of its _rate of convergence_ as $$m$$ increases.  
    * __Consistency__: as the number of training examples approaches infinity, the maximum likelihood estimate of a parameter converges to the true value of the parameter, under the following conditions:  
        * The true distribution $$p_{\text{data}}$$ must lie within the model family $$p_{\text{model}}(\cdot ; \boldsymbol{\theta})$$. Otherwise, no estimator can recover $$p_{\text{data}}$$.  
        * The true distribution $$p_{\text{data}}$$ must correspond to exactly one value of $$\boldsymbol{\theta}$$. Otherwise, maximum likelihood can recover the correct $$p_{\text{data}}$$ but will not be able to determine which value of $$\boldsymbol{\theta}$$ was used by the data-generating process.   
    * __Statistical Efficiency__: meaning that one consistent estimator may obtain lower generalization error for a fixed number of samples $$m$$, or equivalently, may require fewer examples to obtain a fixed level of _generalization error_.[^7]  
        The __Cramér-Rao lower bound__ shows that _no consistent estimator has a lower MSE than the maximum likelihood estimator._  
    <br>

9. **Maximum A Posteriori (MAP) Estimation:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents19}  
    The __MAP estimate__ chooses the point of _maximal posterior probability_ by allowing the prior to influence the choice of the point estimate:  
    <p>$$\boldsymbol{\theta}_ {\mathrm{MAP}}=\underset{\boldsymbol{\theta}}{\arg \max } p(\boldsymbol{\theta} | \boldsymbol{x})=\underset{\boldsymbol{\theta}}{\arg \max } \log p(\boldsymbol{x} | \boldsymbol{\theta})+\log p(\boldsymbol{\theta}) \tag{5.79}$$</p>  

    Many regularized estimation strategies, such as maximum likelihood learning regularized with weight decay, can be interpreted as making the MAP approximation to Bayesian inference.  
    > E.g. MAP Bayesian inference with a __Gaussian prior__ on the weights corresponds to __weight decay__ Regularization:  
        consider a linear regression model with a Gaussian prior on the weights $$\mathbf{w}$$. If this prior is given by $$\mathcal{N}\left(\boldsymbol{w} ; \mathbf{0}, \frac{1}{\lambda} \boldsymbol{I}^{2}\right)$$, then the log-prior term in equation $$5.79$$ is *__proportional__* to the familiar $$\lambda w^{T} w$$ weight decay penalty, plus a constant.    

    This view applies when the regularization consists of adding an extra term to the objective function that corresponds to $$\log p(\boldsymbol{\theta})$$ (i.e. logarithm of a probability distribution).  
        


[^4]: In other words, $$p_{\text{model}}(x ; \boldsymbol{\theta})$$ maps any configuration $$x$$ to a real number estimating the true probability $$p_{\text{data}}(x)$$.  
[^5]: Ideally, we would like to match the true data-generating distribution $$p_{\text{ data }}$$, but we have no direct access to this distribution.  
[^6]: The perspective of maximum likelihood as minimum KL divergence becomes helpful in this case because the KL divergence has a known minimum value of zero. The negative log-likelihood can actually become negative when $$x$$ is real-valued.  
[^7]: Statistical efficiency (measured by the MSE between the estimated and true parameter) is typically studied in the __parametric case__ (as in linear regression), where our goal is to estimate the value of a parameter (assuming it is possible to identify the true parameter), not the value of a function.  


***

## The Mathematics of Neural Networks
{: #content2}

0. **Derivative:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents20}  
    The derivative of a function is the amount that the value of a function changes when the input changes by an $$\epsilon$$ amount:  
    <p>$$f'(a)=\lim_{h\to 0}{\frac {f(a+h)-f(a)}{h}}. \\
    \text{i.e. } f(x + \epsilon)\approx f(x)+\epsilon f'(x)
    $$</p>  
    
    __The Chain Rule__ is a way to compute the derivative of _composite functions_.  
    If $$y = f(x)$$ and $$z = g(y)$$:  
    <p>$$\dfrac{\partial z}{\partial x} = \dfrac{\partial z}{\partial y} \dfrac{\partial y}{\partial x}$$</p>       

1. **Gradient: (Vector in, Scalar out)**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    Gradients generalize derivatives to __*scalar functions*__ of several variables  
    ![Gradient](/main_files/math/calc/1.png){: width="80%"}  

    __Property:__ the gradient of a function $$\nabla f(x)$$ points in the direction of __steepest ascent__ from $$x$$.  
    <br>

2. **The Jacobian: (Vector in, Vector out)**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}  
:   The __Jacobian__ of $$f: \mathbb{R}^n \rightarrow \mathbb{R}^m $$ is a matrix of _first-order partial derivatives_ of a __*vector-valued function*__:  
:  ![Jacobian](/main_files/math/calc/2.png){: width="80%"}  
:   __The Chain Rule:__  
    Let $$f : \mathbb{R}^N \rightarrow \mathbb{R}^M$$ and $$g : \mathbb{R}^M \rightarrow \mathbb{R}^ K$$; and let  $$x \in \mathbb{R}^N, y \in \mathbb{R}^M$$, and $$z \in \mathbb{R}^K$$ with $$y = f(x)$$ and $$z = g(y)$$:  
:  $$\dfrac{\partial z}{\partial x} = \dfrac{\partial z}{\partial y} \dfrac{\partial y}{\partial x}$$    
:   where, $$\dfrac{\partial z}{\partial y} \in \mathbb{R}^{K \times M}$$ matrix, $$\dfrac{\partial y}{\partial x} \in \mathbb{R}^{M \times N}$$ matrix, and $$\dfrac{\partial z}{\partial x} \in \mathbb{R}^{K \times N}$$  matrix;  
    the multiplication of $$\dfrac{\partial z}{\partial y}$$  and $$\dfrac{\partial y}{\partial x}$$ is a matrix multiplication.  

2. **The Generalized Jacobian: (Tensor in, Tensor out)**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}
:   __A Tensor__ is a D-dimensional grid of number.  
:   Suppose that $$f: \mathbb{R}^{N_1 \times \cdots \times N_{D_x}} \rightarrow \mathbb{R}^{M_1 \times \cdots \times M_{D_y}} $$.  
    If $$y = f(x)$$ then the derivative $$\dfrac{\partial y}{\partial x}$$ is a __generalized Jacobian__ - an object with shape:  
:   $$(M_1 \times \cdots \times M_{D_y}) \times (N_1 \times \cdots \times N_{D_x})$$ 
:   >  we can think of the generalized Jacobian as generalization of a matrix, where each “row” has the same shape as $$y$$  and each “column” has the same shape as $$x$$.  
:    Just like the standard Jacobian, the generalized Jacobian tells us the relative rates of change between all elements of $$x$$  and all elements of $$y$$:  
:   $$(\dfrac{\partial y}{\partial x})_{i,j} = \dfrac{\partial y_i}{\partial x_j} \in \mathbb{R}$$
:   Just as the derivative, the generalized Jacobian gives us the relative change in $$y$$ given a small change in $$x$$:  
:   $$f(x + \delta x)\approx f(x)+ f'(x) \delta x = y + \dfrac{\partial y}{\partial x}\delta x$$  
:   where now, $$\delta x$$ is a tensor in $$\mathbb{R}{N_1 \cdots N_{d_x}}$$ and $$\dfrac{\partial y}{\partial x}$$ is a generalized matrix in $$\mathbb{R}^{(M_1 \times \cdots \times M_{D_y}) \times (N_1 \times \cdots \times N_{D_x})} $$.  
    The product $$\dfrac{\partial y_i}{\partial x_j} \delta x$$ is, therefore, a __*generalized matrix-vector multiply*__, which results in a tensor in $$\mathbb{R}^{M_1 \times \cdots \times M_{D_y}}$$.  
:   The __generalized matrix-vector multiply__ follows the same algebraic rules as a traditional matrix-vector multiply:  
:   ![matrix-vector mult](/main_files/math/calc/4.png){: width="80%"}  
:   ![matrix-vector mult-2](/main_files/math/calc/5.png){: width="100%"}  
:   __The Chain Rule:__  
:   ![chain rule](/main_files/math/calc/6.png){: width="100%"}  


3. **The Hessian:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}
:   The __Hessian__ Matrix of a _scalar function_ $$f: \mathbb{R}^d \rightarrow \mathbb{R} $$ is a matric of _second-order partial derivatives_:
:  ![Hessian](/main_files/math/calc/3.png){: width="80%"}
:   __Properties:__ 
        * The Hessian matrix is __*symmetric*__ - since we usually work with smooth/differentiable functions - due to _Clairauts Theorem_.  
        > __Clairauts Theorem:__ if the partial derivatives are continuous, the order of differentiation can be interchanged  
        * The Hessian is used in some optimization algorithms such as Newton’s method  
        * It is expensive to calculate but can drastically reduce the number of iterations needed to converge to a local minimum by providing information about the curvature of $$f$$


4. **Matrix Calculus:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}
:   __Important Identities:__  
:   $${\frac  {\partial {\mathbf  {a}}^{\top }{\mathbf  {x}}}{\partial {\mathbf  {x}}}}={\frac  {\partial {\mathbf  {x}}^{\top }{\mathbf  {a}}}{\partial {\mathbf  {x}}}}= a \\ 
    {\frac  {\partial {\mathbf  {x}}^{\top }{\mathbf  {A}}{\mathbf  {x}}}{\partial {\mathbf  {x}}}}=  ({\mathbf  {A}}+{\mathbf  {A}}^{\top }){\mathbf  {x}} \\ 
    {\frac  {\partial {\mathbf  {x}}^{\top }{\mathbf  {A}}{\mathbf  {x}}}{\partial {\mathbf  {x}}}}=  2{\mathbf  {A}}{\mathbf  {x}} \:\:\:\:\: \text{[Symmetric } A\text{]}$$
:   [Identities](https://en.wikipedia.org/wiki/Matrix_calculus)
:   __The Product Rule:__  
:   $${\displaystyle {\begin{aligned}\nabla (\mathbf {A} \cdot \mathbf {B} )&=(\mathbf {A} \cdot \nabla )\mathbf {B} +(\mathbf {B} \cdot \nabla )\mathbf {A} +\mathbf {A} \times (\nabla \times \mathbf {B} )+\mathbf {B} \times (\nabla \times \mathbf {A} )\\&=\mathbf {J} _{\mathbf {A} }^{\mathrm {T} }\mathbf {B} +\mathbf {J}_{\mathbf {B} }^{\mathrm {T} }\mathbf {A} \\&=\nabla \mathbf {A} \cdot \mathbf {B} +\nabla \mathbf {B} \cdot \mathbf {A} \ \end{aligned}}}\\ 
    \implies \\ 
    \nabla (fg) = (f')^T g + (g')^T f$$ 
:   Thus, we set our function $$h(x) = \langle f(x), g(x) \rangle = f(x)^T g(x)$$; then,  
:   $$\nabla h(x) = f'(x)^T g(x) + g'(x)^T f(x).$$


The answer to the product rule is as follows:
:   $$    \nabla (f^Tg) = f'g + g'f$$  
or
:   $$    \nabla (x^TAx) = \nabla (x)^T(Ax)  =  (x)'(Ax) + (Ax)'x = Ax + A^Tx = (A+A^T)x$$ 


<!-- 5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents26}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents27}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents28} -->


***

## Challenges in Machine Learning
{: #content3}

1. **The Curse of Dimensionality:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}  
    It is a phenomena where many machine learning problems become exceedingly difficult when the number of dimensions in the data is high.  

    * The number of possible distinct configurations of a set of variables increases exponentially as the number of variables increases:  
        <button>Capacity and Bias/Variance</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        ![img](/main_files/dl_book/2.png){: hidden=""}  
        * __Statistical Challenge:__ the number of possible configurations of $$x$$ is much larger than the number of training examples  
    * [Further Reading (Concepts)](/concepts_#bodyContents621)  
    * [Yoshua Bengio on Curse of Dimensionality (Quora)](https://www.quora.com/What-is-the-curse-of-dimensionality/answer/Yoshua-Bengio)  
    <br>

2. **Local Constancy and Smoothness Regularization:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}  
    Prior believes about the particular data-set/learning-problem can be incorporated as:  
    * Beliefs about the __distribution__ of __parameters__ 
    * Beliefs about the __properties__ of the estimating __function__  
        Expressed implicitly by choosing algorithms that are biased toward choosing some class of functions over another, even though these biases may not be expressed (or even be possible to express) in terms of a probability distribution representing our degree of belief in various functions.  

    __The Local Constancy (Smoothness) Prior:__ states that the function we learn should not change very much within a small region.  
    Mathematically, traditional ML methods are designed to encourage the learning process to learn a function $$f^\ast$$ that satisfies the condition:  
    $$\:\:\:\:\:\:\:$$ $$\:\:\:\:\:\:\:$$ $$f^{*}(\boldsymbol{x}) \approx f^{*}(\boldsymbol{x}+\epsilon)$$  
    for most configurations $$x$$ and small change $$\epsilon$$.  
    * <button>Example: K-Means</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        ![img](/main_files/dl_book/7.png){: hidden=""}  


    A [__Local Kernel__](/concepts_#bodyContents60) can be thought of as a similarity function that performs template matching, by measuring how closely a test example $$x$$ resembles each training example $$x^{(i)}$$.  
    Much of the modern motivation for Deep Learning is derived from studying the limitations of local template matching and how deep models are able to succeed in cases where local template matching fails _(Bengio et al., 2006b)_.  
    * [The Curse of Dimensionality for Local Kernel Machines (paper!)](https://pdfs.semanticscholar.org/9bfc/f812b249d570823c6a0dff4a4781a40524d1.pdf)  

    <button>Example: Decision Trees</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    _Decision trees also suffer from the limitations of exclusively smoothness-based learning, because they break the input space into as many regions as there are leaves and use a separate parameter (or sometimes many parameters for extensions of decision trees) in each region. If the target function requires a tree with at least $$n$$ leaves to be represented accurately, then at least $$n$$ training examples are required to fit the tree. A multiple of $$n$$ is needed to achieve some level of statistical confidence in the predicted output._{: hidden=""}  

    In general, to distinguish $$\mathcal{O}(k)$$ regions in input space, all these methods require $$\mathcal{O}(k)$$ examples. Typically there are $$\mathcal{O}(k)$$ parameters, with $$\mathcal{O}(1)$$ parameters associated with each of the $$\mathcal{O}(k)$$ regions.  

    
    __Key Takeaways:__   
    {: #lst-p}
    * *__Is there a way to represent a complex function that has many more regions to be distinguished than the number of training examples?__*  
        Clearly, assuming only smoothness of the underlying function will not allow a learner to do that.  
        The smoothness assumption and the associated nonparametric learning algorithms work extremely well as long as there are enough examples for the learning algorithm to observe high points on most peaks and low points on most valleys of the true underlying function to be learned.  
    * *__Is it possible to represent a complicated function efficiently? and if it is complicated, Is it possible for the estimated function to generalize well to new inputs?__*  
        Yes.  
        The key insight is that a very large number of regions, such as $$\mathcal{O}(2^k)$$, can be defined with $$\mathcal{O}(k)$$ examples, so long as we <span>introduce some __dependencies between the regions__ through additional __assumptions__ about the underlying __data-generating distribution__</span>{: style="color: purple"}.  
        In this way, we can actually __generalize *non-locally*__ _(Bengio and Monperrus, 2005; Bengio et al., 2006c)_.  
        Many different deep learning algorithms provide implicit or explicit assumptions that are reasonable for a __broad range of AI tasks__ in order to capture these advantages.  
        * <button>Non-Local Generalization (for an Algorithm)</button>{: .showText value="show" onclick="showTextPopHide(event);"}
            * I mean that the algorithm should be able to provide good generalizations even for inputs that are far from those it has seen during training. It should be able to generalize to new combinations of the underlying concepts that explain the data. Nearest-neighbor methods and related ones like kernel SVMs and decision trees can only generalize in some neighborhood around the training examples, in a way that is simple (like linear interpolation or linear extrapolation). Because the number of possible configurations of the underlying concepts that explain the data is exponentially large, this kind of generalization is good but not sufficient at all. Non-local generalization refers to the ability to generalize to a huge space of possible configurations of the underlying causes of the data, potentially very far from the observed data, going beyond linear combinations of training examples that have been seen in the neighborhood of the given input.    
            {: hidden=""}
        * <span>Non-Local VS Local Generalization correspond to __Distributed__ VS __Local__ Representations</span>{: style="color: purple"}   
    * *__Deep Learning VS Machine Learning:__*  
        The core idea in deep learning is that we assume that the data was generated by the <span>__composition__ of __factors__, or __features__, potentially at _multiple levels_ in a __hierarchy__</span>{: style="color: purple"}.  
        These apparently mild assumptions allow an exponential gain in the relationship between the number of examples and the number of regions that can be distinguished.  
        The exponential advantages conferred by the use of deep distributed representations counter the exponential challenges posed by the curse of dimensionality.  
        (Many other similarly generic assumptions can further improve deep learning algorithms).  
        * __Further Reading:__ (on the exponential gain) Sections: 6.4.1, 15.4 and 15.5.  
        * <button>Why generic assumptions not specific assumptions!</button>{: .showText value="show" onclick="showTextPopHide(event);"}
            ![img](https://cdn.mathpix.com/snip/images/DTU41jDkYGq9GOYNcjQIlWKb9DuU-CSiEMczWRg4fAM.original.fullsize.png){: width="100%" hidden=""}  

    

3. **Manifold Learning:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}  
    A __Manifold__ - a connected region - is a set of points associated with a neighborhood around each point. From any given point, the manifold locally appears to be a Euclidean space.  
    ![img](/main_files/dl_book/8.png){: width="100%"}  

    __Manifolds in ML:__  
    In ML, the term is used loosely to designate a connected set of points that can be approximated well by considering only a small number of degrees of freedom, or dimensions, embedded in a higher-dimensional space. Each dimension corresponds to a local direction of variation.  
    In the context of machine learning, we allow the dimensionality of the manifold to vary from one point to another. This often happens when a manifold intersects itself. For example, a figure eight is a manifold that has a single dimension in most places but two dimensions at the intersection at the center.  
    __Manifold Assumptions:__  
    <button>Discussion</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    _Many machine learning problems seem hopeless if we expect the machine learning algorithm to learn functions with interesting variations across all of $$\mathbb{R}^n$$. Manifold learning algorithms surmount this obstacle by assuming that most of $$\mathbb{R}^n$$ consists of invalid inputs, and that interesting inputs occur only a long a collection of manifolds containing a small subset of points, with interesting variations in the output of the learned function occurring only along directions that lie on the manifold, or with interesting variations happening only when we move from one manifold to another. Manifold learning was introduced in the case of continuous-valued data and in the unsupervised learning setting, although this probability concentration idea can be generalized to both discrete data and the supervised learning setting: the key assumption remains that probability mass is highly concentrated._{: hidden=""}  
    We assume that the *__data lies along a low-dimensional manifold__*:  
    {: #lst-p}
    * May not always be correct or useful  
    * In the context of AI tasks (e.g. processing images, sounds, or text): At least approximately correct.  
        To show that is true we need to argue two points:  
        * The probability distribution over images, text strings, and sounds that occur in real life is highly concentrated.  
            <button>Example/proof: The Manifold of Natural Images</button>{: .showText value="show" onclick="showTextPopHide(event);"}
            ![img](/main_files/dl_book/9.png){: hidden=""}   
            > Uniform noise essentially never resembles structured inputs from these domains.   
        * We must, also, establish that the examples we encounter are connected to each other by other examples, with each example surrounded by other highly similar examples that can be reached by applying transformations to traverse the manifold:  
            _Informally,_ we can imagine such neighborhoods and transformations:  
            In the case of images, we can think of many possible transformations that allow us to trace out a manifold in image space: we can gradually dim or brighten the lights, gradually move or rotate objects in the image, gradually alter the colors on the surfaces of objects, and so forth.  
            > Multiple manifolds are likely involved in most applications. For example,the manifold of human face images may not be connected to the manifold of cat face images.  
            > Rigorous Results: _(Cayton, 2005; Narayanan and Mitter,2010; Schölkopf et al., 1998; Roweis and Saul, 2000; Tenenbaum et al., 2000; Brand,2003; Belkin and Niyogi, 2003; Donoho and Grimes, 2003; Weinberger and Saul,2004)_  

    __Benefits:__  
    When the data lies on a low-dimensional manifold, it can be most natural for machine learning algorithms to represent the data in terms of coordinates on the manifold, rather than in terms of coordinates in $$\mathbb{R}^n$$.  
    E.g. In everyday life, we can think of roads as 1-D manifolds embedded in 3-D space. We give directions to specific addresses in terms of address numbers along these 1-D roads, not in terms of coordinates in 3-D space.  
    > Learning Manifold Structure: _figure 20.6_  


<!-- ## Activation Functions
{: #content4}

1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents41}

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents42}

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents43}

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents44}

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents45}

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents46}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents47}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents48}

*** -->