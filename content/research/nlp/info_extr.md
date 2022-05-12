---
layout: NotesPage
title: Information Extraction <br \> Named Entity Recognition
permalink: /work_files/research/nlp/info_extr
prevLink: /work_files/research/nlp.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Introduction to Information Extraction](#content1)
  {: .TOC1}
  * [Named Entity Recognition (NER)](#content2)
  {: .TOC2}
  * [Sequence Models for Named Entity Recognition](#content3)
  {: .TOC3}
  * [Maximum Entropy Sequence Models](#content4)
  {: .TOC4}
</div>

***
***

## Introduction to Information Extraction
{: #content1}

1. **Information Extraction (IE):**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    :   is the task of automatically extracting structured information from a (non/semi)-structured piece of text.  

2. **Structured Representations of Inforamtion:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    :   Usually, the extracted information is represented as:  
        * Relations (in the DataBase sense)  
        * A Knowledge Base

3. **Goals:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    :   1. Organize information in a way that is useful to humans. 
        2. Put information in a semantically precise form that allows further inference to be made by other computer algorithms. 

4. **Common Applications:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    :   * Gathering information (earning, profits, HQs, etc.) from reports  
        * Learning drug-gene product interactions from medical research literature  
        * Low-Level Information Extraction:  
            * Information about possible dates, schedules, activites gathered by companys (e.g. google, facebook)  

5. **Tasks and Sub-tasks:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  
    :   * __Named entity extraction__:   
            * __Named Entity Recognition__: recognition of known entity names (for people and organizations), place names, temporal expressions, and certain types of numerical expressions.     
            * __Coreference Resolution__:  detection of coreference and anaphoric links between text entities.  
            * __Relationship Extraction__: identification of relations between entities.  
        * __Semi-structured information extraction__:
            * *__Table Extraction__*: finding and extracting tables from documents.  
            * *__Comments extraction__*: extracting comments from actual content of article in order to restore the link between author of each sentence.
        * __Language and Vocabulary Analysis__:   
            * *__Terminology extraction__*: finding the relevant terms for a given corpus.          

6. **Methods:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}  
    :   There are three standard approaches for tackling the problem of IE:  
        * __Hand-written Regular Expressions__: usually stacked.  
        * __Classifiers__:   
            * *__Generative__*:   
                * Naive Bayes Classifier
            * *__Discriminative__*:   
                * MaxEnt Models (Multinomial Logistic Regr.)
        * __Sequence Models__:   
            * Hidden Markov Models
            * Conditional Markov model (CMM) / Maximum-entropy Markov model (MEMM)
            * Conditional random fields (CRF)

***

## Named Entity Recognition (NER)
{: #content2}

1. **Named Entity Recognition:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    :   is the recognition of known entity names (for people and organizations), place names, temporal expressions, and certain types of numerical expressions;  
    this is usually done by employing existing knowledge of the domain or information extracted from other sentences.    

2. **Applications:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}  
    :   * Named entities can be indexed, linked off, etc.
        * Sentiment can be attributed to companies or products  
        * They define a lot of the IE relations, as associations between the named entities
        * In QA, answers are often named entities  


3. **Evaluation of NER Tasks:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}  
    :   Evaluation is usually done at the level of __Entities__ and not of __Tokens__.  
    :   One common issue with the metrics defined for text classification, namely, (Precision/Recall/F1) is that they penalize the system based on a binary evaluation on how the system did; however, let's demonstrate why that would be problamitic.  
    :   * Consider the following text:  
            "The _First **Bank of Chicago**_ announced earnings..."  
            Let the italic part of the text be the enitity we want to recognize and let the bolded part of the text, be the entitiy that our model identified.  
            The (Precision/Recall/F1) metrics would penalize the model twice, once as a false-positive (for having picked an incorrect entitiy name), and again as a false-negative (for not having picked the actual entitiy name).   
            However, we notice that our system actually picked $$3/4$$ths of the actual entity name to be recognized.  
        * This leads us seeking an evaluation metric that awards partial credit for this task.  
    :   * The __MUC Scorer__ is one, such, metric for giving partial credit.  
    :   Albeit such complications and issues with the metrics described above, the field has, unfortunately, continued using the F1-Score as a metric for NER systems due to the complexity of formulating a metric that  gives partial credit.  

***

## Sequence Models for Named Entity Recognition
{: #content3}

1. **Approach:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}  
    :   * __Training__:   
            1. Collect a set of representative training documents
            2. Label each token for its entity class or other (O)
            3. Design feature extractors appropriate to the text and classes
            4. Train a sequence classifier to predict the labels from the data
    :   * __Testing__:  
            1. Receive a set of testing documents
            2. Run sequence model inference to label each token  
            3. Appropriately output the recognized entities   

2. **Encoding Classes for Sequence Labeling:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}  
    :   There are two common ways to encode the classes:  
        * __IO Encoding__: this encoding will only encode only the entitiy of the token disregarding its order/position in the text (PER).  
            * For $$C$$ classes, IO produces ($$C+1$$ ) labels.  
        * __IOB Encoding__: this encoding is similar to IO encoding, however, it, also, keeps track to whether the token is the beginning of an entitiy-name (B-PER) or a continuation of such an entity-name (I-PER).  
            * For $$C$$ classes, IO produces ($$2C+1$$ ) labels.
    :   The __IO__ encoding, thus, is much lighter, and thus, allows the algorithm to run much faster than the __IOB__ encoding.  
        Moreover, in practice, the issue presented for IO encoding rarely occurs and is only limited to instances where the entities that occur next to each other, are the same entity.   
        __IOB__ encoded systems, also, tend to not learn quite as well due to the huge number of labels and are usually still prone to the same issues
    :   Thus, due to the reasons mentioned above, the __IO Encoding__ scheme is the one most commonly used.            

3. **Features for Sequence Labeling:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}  
    :   * __Words__:   
            * Current word (like a learned dictionary)
            * Previous/Next word (context)
        * __Other kinds of Inferred Linguistic Classification__:    
            * Part-of-Speech Tags (POS-Tags)   
        * __Label-Context__:   
            * Previous (and perhaps next) label
            > This is usually what allows for sequence modeling 
    :   Other useful features:  
        * __Word Substrings__: usually there are substrings in words that are _categorical_ in nature  
            * Examples:  
                "oxa" -> Drug  
                "(noun): (noun)" -> Movie  
                "(noun)-field" -> (usually) place  
        * __Word Shapes__: the idea is to map words to simplified representations that encode attributes such as:  
           length, capitalization, numerals, Greek-Letters, internal punctuation, etc.  
           * Example:  
                The representation below shows only the first two letters and the last two letters; for everything else, it will add the capitalization and the special characters, and for longer words, it will represent them in set notation.   

                | Varicella-zoster | Xx-xxx  
                | mRNA | xXXX   
                | CPA1 | XXXd  


***

## Maximum Entropy Sequence Models
{: #content4}

1. **Maximum-Entropy (Conditional) Markov Model:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents41}  
    :   is a discriminative graphical model for sequence labeling that combines features of hidden Markov models (HMMs) and maximum entropy (MaxEnt) models.  
    :   It is a discriminative model that extends a standard maximum entropy classifier by assuming that the unknown values to be learned are connected in a Markov chain rather than being conditionally independent of each other.
    :   It makes a single decision at a time, conditioned on evidence from observations and previous decisions.  
    :   > A larger space of sequences is usually explored via search.  

2. **Inference:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents42}  
    ![img](/main_files/nlp/1.png){: width="100%"} 

3. **Exploring the Sequence Space (Search Methods):**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents43}  
    :   * __Beam Inference__:  
            * *__Algorithm__*:  
                * At each position keep the top $$k$$ complete sequences.  
                * Extend each sequence in each local way.  
                * The extensions compete for the $$k$$ slots at the next position.  
            * *__Advantages__*:   
                * Fast. Beam sizes of 3-5 are almost as good as exact inference in many cases.  
                * Easy. Implementation does not require dynamic programming.  
            * *__Disadvantages__*:    
                * Inexact. The globally best sequence can fall off the beam.   
    :   * __Viterbi Inference__:  
            * *__Algorithm__*:  
                * Dynamic Programming or Memoization.  
                * Requires small window of state influence (eg. past two states are relevant)  
            * *__Advantages__*:  
                * Exact. the global best sequence is returned.  
            * *__Disadvantages__*:  
                * Hard. Harder to implement long-distance state-state interactions. 


4. **Conditional Random Fields (CRFs):**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents44}  
    :   are a type of discriminative undirected probabilistic graphical model.   
    :   They can take context into account; and are commonly used to encode known relationships between observations and construct consistent interpretations.