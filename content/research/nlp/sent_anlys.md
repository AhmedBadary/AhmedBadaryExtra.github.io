---
layout: NotesPage
title: Sentiment Analysis
permalink: /work_files/research/nlp/sent_anlys
prevLink: /work_files/research/nlp.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Introduction](#content1)
  {: .TOC1}
  * [Algorithms](#content2)
  {: .TOC2}
  * [Sentiment Lexicons ](#content3)
  {: .TOC3}
</div>

***
***

## Introduction
{: #content1}

1. **Sentiment Analysis:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    :   is the automated identification and quantification of affective states and subjective information in textual data.

2. **Applications:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    :   

3. **Formulating the Problem:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    :   *__Tasks to Extract__*:  
        * __Holder (source)__: of the attitude.  
        * __Target (aspect)__: of the attitude.  
        * __Type__: of the attitude.  
    :   __*Input*__:  
        * __Text__: Contains the attitude  
            * Sentence Analysis  
            * Entire-Document Analysis  
        * __main__: second   

***

## Algorithms
{: #content2}

1. **Binarized (Boolean Feature) Multinomial Naive Bayes:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    :   This algorithm works exactly the same as the [Multinomial Naive Bayes](http://ahmedbadary.ml/work_files/research/nlp/txt_clss#content2) algorithm.  
    :   However, the features (Tokens) used in this algorithm are counted based on _occurrence_ rather than _frequency_,  
        > i.e. if a certain word occurs in the text then its count is always one, regardless of the number of occurrences of the word in the text.  
    :   __Justification:__ The reason behind the binarized version is evident, intuitively, in the nature of the problem.  
        The sentiment behind a certain piece of text is usually represented in just one occurrence of a word that represents that sentiment (e.g. "Fantastic") rather than how many times did that word actually appear in the sentence.  
2. **Better Algorithms:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}  
    :   * Max-Entropy  
        * SVMs


***

## Sentiment Lexicons
{: #content3}

1. **Sentiment Lexicons:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}  
    :   Specific key-words that are related to specific polarities.  
        They are much more useful to be used instead of analyzing all of the words (tokens) in a piece of text. 
