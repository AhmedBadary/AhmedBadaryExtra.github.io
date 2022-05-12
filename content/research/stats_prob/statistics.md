---
layout: NotesPage
title: Statistics
permalink: /work_files/research/dl/stat_prob/stats
prevLink: /work_files/research/dl/theory.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Applications of Statistics in Machine Learning](#content1)
  {: .TOC1}
  * [Introduction to Statistics](#content2)
  {: .TOC2}
  * [Statistical Hypothesis Tests](#content3)
  {: .TOC3}
  * [Estimation Statistics](#content4)
  {: .TOC4}
  * [Statistical Tests](#content5)
  {: .TOC5}
</div>

***
***

* [Statistics for Machine Learning (7-Day Mini-Course) (Blog)](https://machinelearningmastery.com/statistics-for-machine-learning-mini-course/)  
* [Digital textbook on probability and statistics (!)](https://www.statlect.com/)  
* [Statisticians say the darndest things (Blog)](https://explained.ai/statspeak/index.html)  
* [Intro to Descriptive Statistics (Blog!)](https://towardsdatascience.com/intro-to-descriptive-statistics-252e9c464ac9)  


## Applications of Statistics in Machine Learning
{: #content1}

1. **Statistics in Data Preparation:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    Statistical methods are required in the preparation of train and test data for your machine learning model.  

    __Tasks:__{: style="color: red"}  
    {: #lst-p}
    * Outlier detection
    * Missing Value Imputation
    * Data Sampling
    * Data Scaling
    * Variable Encoding  

    A basic understanding of data distributions, descriptive statistics, and data visualization is required to help you identify the methods to choose when performing these tasks.  


2. **Statistics in Model Evaluation:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    Statistical methods are required when evaluating the skill of a machine learning model on data not seen during training.  

    __Tasks:__{: style="color: red"}  
    {: #lst-p}
    * Data Sampling
    * Data Re-Sampling
    * Experimental Design

    Re-Sampling Techniques include <span>k-fold</span>{: style="color: goldenrod"} and <span>cross-validation</span>{: style="color: goldenrod"}.  

3. **Statistics in Model Selection:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    Statistical methods are required when selecting a final model or model configuration to use for a predictive modeling problem.  

    __Tasks:__{: style="color: red"}  
    {: #lst-p}
    * Checking for a significant difference between results
    * Quantifying the size of the difference between results  

    Techniques include <span>statistical hypothesis tests</span>{: style="color: goldenrod"}.  


4. **Statistics in Model Presentation:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    Statistical methods are required when presenting the skill of a final model to stakeholders.  

    __Tasks:__{: style="color: red"}  
    {: #lst-p}
    * Summarizing the expected skill of the model on average
    * Quantifying the expected variability of the skill of the model in practice
    
    Techniques include __estimation statistics__ such as <span>confidence intervals</span>{: style="color: goldenrod"}.  

5. **Statistics in Prediction:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  
    Statistical methods are required when making a prediction with a finalized model on new data.  
    
    __Tasks:__{: style="color: red"}  
    {: #lst-p}
    * Quantifying the expected variability for the prediction.  

    Techniques include __estimation statistics__ such as <span>prediction intervals</span>{: style="color: goldenrod"}.  


    <!-- 6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}   -->

7. **Summary:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}
    * __Data Preparation:__{: style="color: red"}  
        * Outlier detection
        * Missing Value Imputation
        * Data Sampling
        * Data Scaling
        * Variable Encoding
    * __Model Evaluation:__{: style="color: red"}  
        * Data Sampling
        * Data Re-Sampling
        * Experimental Design
    * __Model Selection:__{: style="color: red"}  
        * Checking for a significant difference between results
        * Quantifying the size of the difference between results
    * __Model Presentation:__{: style="color: red"}  
        * Summarizing the expected skill of the model on average
        * Quantifying the expected variability of the skill of the model in practice
    * __Prediction:__{: style="color: red"}  
        * Quantifying the expected variability for the prediction.  

<!-- 8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18}   -->


***

## Introduction to Statistics
{: #content2}

1. **Statistics:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    __Statistics__ is a subfield of mathematics. It refers to a collection of methods for working with data and using data to answer questions.  

2. **Statistical Tools:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}     
    Statistical Tools can be divided into two large groups of methods:  
    {: #lst-p}
    * __Descriptive Statistics:__ methods for summarizing _raw observations_ into information that we can understand and share.  
    * __Inferential Statistics:__  methods for quantifying properties of the population from a smaller set of obtained observations called a sample.  


3. **Descriptive Statistics:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}  
    __Descriptive Statistics__ is the process of using and analyzing summary statistics that quantitatively describe or summarize features from raw observations.  

    Descriptive Statistics are broken down into (__Techniques__):  
    {: #lst-p}
    * __Measures of *Central Tendency*:__ mean, mode, median  
    * __Measures of *Variability/Dispersion*:__ variance, std, minimum, maximum, kurtosis, skewness  


    __Contrast with Inferential Statistics:__{: style="color: red"}  
    {: #lst-p}
    * __Descriptive Statistics__ aims to <span>__summarize__ a _sample_</span>{: style="color: goldenrod"}.  
        Descriptive statistics is solely concerned with <span>properties of the observed data</span>{: style="color: purple"}, and it does not rest on the assumption that the data come from a larger population.  
    * __Inferential Statistics__ uses the <span>_sample_</span>{: style="color: goldenrod"} to <span>__learn__ about the *__population__*</span>{: style="color: goldenrod"}.  
        It is assumed that the observed data set is sampled from a larger population.  


4. **Inferential Statistics:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}  
    __Inferential Statistics__ is the process of using data analysis to deduce properties of an underlying distribution of probability by analyzing a smaller set of observations, drawn from the population, called a sample.  
    Inferential statistical analysis infers properties of a population, for example by testing hypotheses and deriving estimates.  

    __Techniques:__  
    {: #lst-p}
    * AUC
    * Kappa-Statistics Test
    * Confusion Matrix
    * F-1 Score  


    <!-- 5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}   -->


***

## Statistical Hypothesis Tests
{: #content3}

1. **Statistical Hypothesis Tests:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}  
    Statistical hypothesis tests can be used to indicate whether the difference between two samples is due to random chance, but cannot comment on the size of the difference.  


7. **Statistical Hypothesis Tests Types:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents37}  
    [Statistical Hypothesis Tests in Python (Blog)](https://machinelearningmastery.com/statistical-hypothesis-tests-in-python-cheat-sheet/)  
    
    * __Normality Tests:__  
        1. Shapiro-Wilk Test
        2. D'Agostino's K^2 Test
        3. Anderson-Darling Test
    * __Correlation Tests:__  
        1. Pearson's Correlation Coefficient
        2. Spearman's Rank Correlation
        3. Kendall's Rank Correlation
        4. Chi-Squared Test
    * __Stationary Tests:__  
        1. Augmented Dickey-Fuller
        2. Kwiatkowski-Phillips-Schmidt-Shin
    * __Parametric Statistical Hypothesis Tests:__  
        1. Student's t-test
        2. Paired Student's t-test
        3. Analysis of Variance Test (ANOVA)
        4. Repeated Measures ANOVA Test
    * __Nonparametric Statistical Hypothesis Tests:__  
        1. Mann-Whitney U Test
        2. Wilcoxon Signed-Rank Test
        3. Kruskal-Wallis H Test
        4. Friedman Test


<!-- 2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}  

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}  

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents34}  

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents35}  

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents36}  

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents37}  

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents38}   -->

***

## Estimation Statistics
{: #content4}

<!-- 1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents41}   -->

2. **Estimation:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents42}  
    
    * __Effect Size:__ Methods for quantifying the size of an effect given a treatment or intervention.  
    * __Interval Estimation:__ Methods for quantifying the amount of uncertainty in a value.  
    * __Meta-Analysis:__ Methods for quantifying the findings across multiple similar studies.  

    The most useful methods in applied Machine Learning are <span>Interval Estimation</span>{: style="color: goldenrod"} methods.  

    __Types of Intervals:__{: style="color: red"}  
    {: #lst-p}
    * __Tolerance Interval:__ The bounds or coverage of a <span>*proportion of a distribution*</span>{: style="color: purple"} with a specific <span>level of *confidence*</span>{: style="color: purple"}.  
    * __Confidence Interval__: The bounds on the <span>estimate of a population parameter</span>{: style="color: purple"}.  
    * __Prediction Interval__: The bounds on a <span>*__single__* observation</span>{: style="color: purple"}.  


    __Confidence Intervals in ML:__  
    A simple way to calculate a confidence interval for a classification algorithm is to calculate the binomial proportion confidence interval, which can provide an interval around a model’s estimated accuracy or error.  

<!-- 3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents43}  

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents44}  

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents45}   -->



Hypotheses are about population parameters. 
The Null Hypothesis includes __Equality__; others include __Inequalities__.  

__Significance Level ($$\alpha$$):__ is the probability that we reject the Null Hypothesis when in-reality it is correct.  

People will buy more chocolate if we give away a free gift with the chocolate.
* Population: All days we sell chocolate
* Sample: the days in the next month (not so random - oh well..)
* Set-up: on each day, __randomly__ give out a gift with the chocolate or not (toss a coin)

* Treatments: 
    * Offering a gift
    * Not offering a gift
* Hypotheses: 
    * $$H_0$$: There is no difference in <span>*__mean__* sales</span>{: style="color: purple"} (for the population) for the two treatments.  
        * Math: $$\mathrm{H}_{0}: \mu_{\text {free sticker}}=\mu_{\text {no sticker}}$$  
            $$\iff$$  
            $$\mathrm{H}_{0}: \mu_{\text {free sticker }}-\mu_{\text {no sticker }}=0$$  
        * English: There is no difference in the sales for the two treatments.  
    * $$H_0$$: There is a difference in <span>*__mean__* sales</span>{: style="color: purple"} (for the population) for the two treatments.  
        * Math: $$\mathrm{H}_{1}: \mu_{\text {free sticker }} \neq \mu_{\text {no sticker }}$$
            $$\iff$$  
            $$\mathrm{H}_{1}: \mu_{\text {free sticker }}-\mu_{\text {no sticker }} \neq 0$$  


One-Tailed: the hypotheses have an inequality ($$\leq$$ or $$\geq$$) and an inequality ($$>$$ or $$<$$).  
Two-Tailed: the hypotheses have an equality ($$=$$) and a non-equality ($$\neq$$).  


* P-Value: is a probability. Precisely, it is the probability that we would get our sample result _by chance_, IF there is NO effect in the population.  
    * How likely is it to get the results that you observe, IF the Null Hypothesis is true.  
        * If very likely: The Null Hypothesis is probably True.  
        * If very unlikely: The Null Hypothesis is probably False.  
    * [Understanding where the p-value comes from (Vid)](https://www.youtube.com/watch?v=0-fEKHSeRR0)  

A small p-value indicates a significant result. The smaller the p-value the more confident we are that the Null Hypothesis is wrong.  



Statistical Significance: We have evidence that the result we see in the *__sample__* also exist in the *__population__* (as opposed to chance, or sampling errors).  
Thus, when you get a p-value less than a certain significance level ($$\alpha$$) and you reject the Null Hypothesis; you have a __statistically significant result__.  
The __larger the sample__ the more *__likely__* the results will be statistically significant.  
The __smaller the sample__ the more *__unlikely__* the results will be statistically significant.  


The Null Hypothesis for Regression Analysis reads: The slope coefficient of variable-2 is 0. Variable-2 does not influence variable-1.  



Types of Data:
* __Nominal__: AKA __Categorical__, __Qualitative__. E.g. color, gender, preferred chocolate
    * __Summary Statistics:__ Use Frequency, Percentages. Can't calculate Mean, etc. 
    * __Graphs:__ Pie Chart, Bar Chart, Stacked Bar Chart.  
    * __Analysis:__ 
* __Ordinal__: E.g. Rank, Satisfaction, Agreement 
    * __Summary Statistics:__ Use Frequency, Proportions. Shouldn't use Means etc. Can use Mean for data like user-emotion.  
    * __Graphs:__ Bar Chart, Stacked Bar Chart, Histogram
* __Interval/Ratio__: AKA __Scale__, __Quantitative__, __Parametric__. Types: __Discrete__, __Continuous__. E.g. height, weight, age.  
    * __Summary Statistics:__ Use Mean, Median, StD.  
    * __Graphs:__ Bar Chart, Stacked Bar Chart, Histogram; Boxplots; Scatters.
    * __Analysis:__ 

- Column: Variable/Feature  
- Row   : Observation  

<!-- 6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents46}  

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents47}  

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents48}   -->

***

## Statistical Tests
{: #content5}

Choosing a Statistical Test depends on three factors:  
{: #lst-p}
* __Data__ (level of measurement?): 
    * __Nominal/Categorical:__ 
        * Test for __Proportion__ 
        * Test for __Difference of Two Proportions__ 
        * __Chi-Squared__ Test for __Independence__  
    * __Interval/Ratio:__ 
        * Test for the __Mean__  
        * Test for __Difference of Two Means (independent samples)__ 
        * Test for __Difference of Two Means (paired)__ 
        * Test for __Regression Analysis__ 
    * __Ordinal__:  
        Ordinal data can be classified with one of the other two depending on the context.  
* __Samples__ (how many?):  
    * __One Sample__: If we wish to compare a proportion or a mean against a given value, this will involve __One Sample__.  
        * Test for the __Mean__  
        * Test for the __Proportion__  
    * __Two Samples__: If we are comparing two different lots of things (e.g. men and women, people from different departments).  
        * Test for __Difference of Two Proportions__ 
        * Test for __Difference of Two Means (independent samples)__ 
    * __One Sample, Two Measurements__: If we have two sets of information on the same people/things, we have one sample with two variables.  
        * __Chi-Squared__ Test for __Independence__  
        * Test for __Regression Analysis__  
        * Test for __Difference of Two Means (paired)__  
* __Purpose__ (of analysis?):  
    * __Testing Against a Hypothesized Value__:  
        * Test for __Proportion__ 
        * Test for the __Mean__  
        * Test for __Difference of Two Means (paired)__  
    * __Comparing Two Statistics__:  
        * Test for __Difference of Two Proportions__  
        * Test for __Difference of Two Means (independent samples)__  
    * __Looking for a Relationship between Two Variables__: 
        * __Chi-Squared__ Test for __Independence__  
        * Test for __Regression Analysis__  










Other Statistical Tests:
{: #lst-p}
* ANOVA
* __Spearman:__ The Spearman rank-order correlation coefficient is a nonparametric measure of the monotonicity of the relationship between two datasets.  
    Unlike the Pearson correlation, the Spearman correlation does not assume that both datasets are normally distributed.  
* __Kruskal-Wallis:__ The Kruskal-Wallis H-test tests the null hypothesis that the population median of all of the groups are equal.  
    It is a non-parametric version of ANOVA.  
* __Mann-Whitney:__ 
* __Anderson-Darling__: The Anderson-Darling tests the null hypothesis that a sample is drawn from a population that follows a particular distribution.  
    This function works for __normal__, __exponential__, __logistic__, or __Gumbel__ distributions.  

Considerations:  
{: #lst-p}
* Residuals
* Bias
* Independence
* Post-Hoc
* Normality







