---
layout: NotesPage
title: Text Processing
permalink: /work_files/research/nlp/txt_proc
prevLink: /work_files/research/nlp.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Introduction and Definitions](#content1)
  {: .TOC1}
  * [Tokenization](#content2)
  {: .TOC2}
  * [Word-Normalization (Stemming)](#content3)
  {: .TOC3}
  * [Sentence Segmentation](#content4)
  {: .TOC4}

</div>

***
***

## Introduction and Definitions
{: #content1}

1. **Text Normalization:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    :   Every NLP process starts with a task called _Text Normalization_.  
    :   __Text Normaliization__ is the process of transforming text into a single canonical form that it might not have had before.  
    :   __Importance:__ Normalizing text before storing or processing it allows for _separation of concerns_, since input is guaranteed to be consistent before operations are performed on it.  
    :   __Steps:__  
        1. Segmenting/Tokenizing words in running text.  
        2. Normalizing word formats.  
        3. Segmenting sentences in running text.  

0. **Methods for Normalization:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents10}  
    :   * __Case-Folding__: reducing all letters to lower case.  
            > Possibly, with the exception of capital letters mid-sentence.  
        * __Lemmatization__: reducing inflections or variant forms to base form.  
            > Basically, finding the correct dictionary headword form.  

9. **Morphology:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents19}  
    :   The study of words, how they are formed, and their relationship to other words in the same language.  
    :   * __Morphemes__: the small meaningfuk units that make up words.  
        * __Stems__: the core meaning-bearing units of words.  
        * __Affixes__: the bits and pieces that adhere to stems (often with grammatical functions).     


2. **Word Equivalence in NLP:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    :   Two words have the same  
        * __Lemma__, if they have the same:  
            * Stem  
            * POS  
            * Rough Word-Sense  
            > _cat_ & _cats_ -> same Lemma  
        * __Wordform__, if they have the same:  
            * full inflected surface form  
            > _cat_ & _cats_ -> different wordforms   

3. **Types and Tokens:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    :   * __Type__: an element of the vocabulary.  
            It is the class of all _tokens containing the same character sequence.  
        * __Token__: an instance of that type in running text.  
            It is an instance of a sequence of characters that are grouped together.  

4. **Notation:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    :   * __N__ = Number of _Tokens_.  
        * __V__ = Vocabulary = set of _Types_.     
        * __$$\|V\|$$__ = size/cardinality of the vocabulary.  

5. **Growth of the Vocabulary:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  
    :   Church and Gale (1990) suggested that the size of the vocabulary grows larger than the square root of the number of tokens in a piece of text:  
    :   $$\|V\| > \mathcal{O}(N^{1/2})$$  
  

***

## Tokenization
{: #content2}

1. **Tokenization:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    :   It is the task of chopping up a character sequence and a defined document unit into pieces, called [_tokens_](#bodyContents13).  
        It may involve throwing away certain characters, such as punctuation.  

2. **Methods for Tokenization:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}  
    :   * __Regular Expressions__  
        * __A Flag__: Specific squences of characters.  
        * __Delimiters__: pecific separating characters.  
        * __Dictionary__: exlicit definitions by a dictionary.     


3. **Categorization:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}  
    :   Tokens are categorized by:  
        * Character Content  
        * Context  
    within a data stream.  
    :   __Categories__:  
        * _Identifiers_: names the programmer chooses  
        * _keywords_: names already in the programming language.  
        * _Operators_: symbols that operate on arguments and produce results.    
        * _Grouping Symbols_ 
        * _Data Types_
    :   _Categories_ are used for post-processing of the tokens either by the parser or by other functions in the program.  
   

***

## Word-Normalization (Stemming)
{: #content3}

1. **Stemming:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}  
    :   is the process of reducing inflected (or sometimes derived) words to their word stem, base or root form.  
    :   The stem need __not__ map to a valid root in the language.  
    :   > Basically, Stemming is a crude chopping of [affixes](#bodyContents19)
    :   > __Example__: "automate", "automatic", "automation" -> "automat".  

2. **Porter's Algorithm:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}  
    :   The most common English stemmer.  
    :   It is an iterated series of simple _replace_ rules.  


3. **Algorithms:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}  
    :   * __The Production Technique__: we produce the lookup table, that is used by a naive stemmer, semi-automaically.  
        * __Suffix-Stripping Algorithms__: those algorithms avoid using lookup tables; instead they use a small list of rules to navigate through the text and find theroot forms from word forms.  
        * __Lemmatisation Algorithms__: the _lemmatization_ process starts determining the _part of speech_ of a word and, then, applying normalization rules to for each part-of-speech.   
        * __Stochastic Algorithms__: those algorithms are trained on a table of root form-to-inflected form relations to develop a probablistic model.  
           The model looks like a set of rules, similar to the suffic-stripping list of rules.      

***

## Sentence Segmentation
{: #content4}

1. **Sentence Segmentation:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents41}  
    :   It is the problem of diving a piece of text into its component sentences.  

2. **Identifiers:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents42}  
    :   Identifiers such as "!", "?" are unambiguous; they usually signify the end of a sentence.  
    :   The period "." is quite ambiguous, since it can be used in other ways, such as in abbreviations and in decimal number notation.  

3. **Dealing with Ambiguous Identifiers:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents43}  
    :   One way of dealing with ambiguous identifiers is by building a __Binary Classifier__.  
        On a given occurrence of a period, the classifier has to decide between one of "Yes, this is the end of a sentence" or "No, this is not the end of a sentence".  
    :   __Types of Classifiers:__  
        * _Decision Trees_  
        * _Logistic Regression_  
        * _SVM_  
        * _Neural-Net_  
    :   _Decision Trees_ are a common classifier used for this problems.   
