---
layout: NotesPage
title: Introduction to NLP <br /> Natural Language Processing
permalink: /work_files/research/dl/nlp/intro
prevLink: /work_files/research/dl/nlp.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Introduction](#content1)
  {: .TOC1}
  * [NLP and Deep Learning](#content2)
  {: .TOC2}
  * [Representations of NLP Levels](#content3)
  {: .TOC3}
  * [NLP Tools](#content4)
  {: .TOC4}
  * [NLP Applications](#content5)
  {: .TOC5}

</div>

***
***

## Introduction
{: #content1}

0. **NLP:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents10}  
    :   __Natural Language Processing__ is a field at the intersection of computer science, artificial intelligence, and linguistics concerned with the interactions between computers and human (natural) languages, and, in particular, concerned with programming computers to fruitfully process large natural language data.

1. **Problems in NLP:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11} 
    :   * Question Answering (QA) 
        * Information Extraction (IE)    
        * Sentiment Analysis  
        * Machine Translation (MT)  
        * Spam Detection  
        * Parts-of-Speech (POS) Tagging  
        * Named Entity Recognition (NER)
        * Conference Resolution  
        * Word Sense Disambiguation (WSD)  
        * Parsing  
        * Paraphrasing  
        * Summarization  
        * Dialog  
    :   * __Fully understanding and representing the meaning of language__ (or even defining it) is a difficult goal.
            * Perfect language understanding is __AI-complete__  

2. **(mostly) Solved Problems in NLP:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12} 
    :   * Spam Detection  
        * Parts-of-Speech (POS) Tagging  
        * Named Entity Recognition (NER)  


3. **Within-Reach Problems:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13} 
    :   * Sentiment Analysis  
        * Conference Resolution    
        * Word Sense Disambiguation (WSD)  
        * Parsing  
        * Machine Translation (MT)  
        * Information Extraction (IE)    


4. **Open Problems in NLP:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14} 
    :   * Question Answering (QA)   
        * Paraphrasing  
        * Summarization  
        * Dialog  

5. **Issues in NLP (why nlp is hard?):**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15} 
    :   * __Non-Standard English__: "Great Job @ahmed_badary! I luv u 2!! were SOO PROUD of dis."  
        * __Segmentation Issues__: "New York-New Haven" vs "New-York New-Haven"  
        * __Idioms__: "dark horse", "getting cold feet", "losing face"  
        * __Neologisms__: "unfriend", "retweet", "google", "bromance"  
        * __World Knowledge__: "Ahmed and Zach are brothers", "Ahmed and Zach are fathers"    
        * __Tricky Entity Names__: "Where is _Life of Pie_ playing tonight?", "_Let it be_ was a hit song!"  

6. **Tools we need for NLP:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16} 
    :   * Knowledge about Language.  
        * Knowledge about the World.   
        * A way to combine knowledge sources.  

7. **Methods:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17} 
    :   In general we need to construct __Probabilistic Models__ built from _language data_.    
    :   We do so by using _rough text features_.  
        > All the names models, methods, and tools mentioned above will be introduced later as you progress in the text.  

8. **NLP in the Industry:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18}  
    :   * Search
        * Online ad Matching
        * Automated/Assisted Translation
        * Sentiment analysis for marketing   or finance/trading
        * Speech recognition
        * Chatbots/Dialog Agents
            * Automatic Customer Support
            * Controlling Devices
            * Ordering Goods

***

## NLP and Deep Learning
{: #content2}

1. **What is Special about Human Language:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    :   * Human Language is a system specifically constructed to convey the speaker/writer's meaning.
        > It is a deliberate communication, not just an environmental signal.  
        * Human Language is a __discrete/symbolic/categorical signaling system__  
        * The categorical symbols of a language can be encoded as a signal for communication in several ways:  
            * Sound
            * Gesture 
            * Images (Writing)  
            Yet, __the symbol is invariant__ across different encodings!  
            ![img](/main_files/dl/nlp/1/1.png){: width="80%"}

        * However, a brain encoding appears to be a __continuous pattern of activation__, and the symbols are transmitted via __continuous signals__ of sound/vision.  

2. **Issues of NLP in Machine Learning:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}  
    :   * According to the above passage; we see that although human language is largely symbolic; it is still interpreted by the brain as a continuous signal.  
        This means that we cannot encode this information in a discrete manner; and rather must learn in a sequential, continuous way.  
        * The large vocabulary, symbolic encoding of words creates a problem for machine learning – __sparsity__!

3. **Machine Learning vs Deep Learning:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}  
    :   * Most Machine Learning methods work well because of __human-designed representations__ and __input features__.  
            Thus, the _learning_ here is done, mostly, by the people/scientists/engineers who are designing the features and __not__ by the machines.  
            This, rendered Machine Learning to become just a __numerical optimization method__ for __optimizing weights__ to best make a final prediction.   
    :   * How does that differ with Deep Learning (DL)?  
            * __Representation learning__ attempts to automatically learn good features or representations
            * __Deep learning__ algorithms attempt to learn (multiple levels of) representation and an output  
            * __Raw Inputs__: DL can deal directly with _raw_ inputs (e.g. sound, characters, words)  

4. **Why Deep-Learning?**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}  
    :   * Manually designed features are often over-specified, incomplete and take a long time to design and validate
        * Manually designed features are often over-specified, incomplete and take a long time to design and validate
        * Deep learning provides a very flexible, (almost?) universal, learnable framework for representing world, visual and linguistic information.
        * Deep learning can learn unsupervised (from raw text) and supervised (with specific labels like positive/negative)
        * In ~2010 deep learning techniques started outperforming other machine learning techniques.


5. **Why is NLP Hard (revisited):**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}  
    :   * Complexity in representing, learning and using linguistic/situational/world/visual knowledge
        * Human languages are ambiguous (unlike programming and other formal languages)
        * Human language interpretation depends on real world, common sense, and contextual knowledge

6. **Improvements in _Recent Years_ in NLP:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents26}  
    :   spanning different:  
        * __Levels__: speech, words, syntax, semantics  
        * __Tools__: POS, entities, parsing  
        * __Applications__: MT, sentiment analysis, dialogue agents, QA      

***

## Representations of NLP Levels
{: #content3}

1. **Morphology:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}  
    :   * __Traditionally__: Words are made of morphemes.  
            * uninterested -> un (prefix) + interest (stem) + ed (suffix)
        * __DL__:
            * Every morpheme is a vectors
            * A Neural Network combines two vectors into one vector
            * Luong et al. 2013  
            ![img](/main_files/dl/nlp/1/2.png){: width="33%"}  

2. **Semantics:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}  
    :   * __Traditionally__: Lambda Calculus  
            * Carefully engineered functions
            * Take as inputs specific other functions
            * No notion of similarity or fuzziness of language  
        * __DL__:
            * Every word and every phrase and every logical expression is a vector 
            * A Neural Network combines two vectors into one vector  
            * Bowman et al. 2014  
            ![img](/main_files/dl/nlp/1/3.png){: width="45%"}  

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}  
    :   

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents34}  
    :   

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents35}  
    :   

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents36}  
    :   

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents37}  
    :   

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents38}  
    :   

***

## NLP Tools
{: #content4}

1. **Parsing for Sentence Structure:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents41}  
    :   Neural networks can accurately determine the structure of sentences, supporting interpretation.  
    ![img](/main_files/dl/nlp/1/4.png){: width="70%"}

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents42}  
    :   

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents43}  
    :   

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents44}  
    :   

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents45}  
    :   

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents46}  
    :   

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents47}  
    :   

***

## NLP Applications
{: #content5}

1. **Sentiment Analysis:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents51}  
    :   * __Traditional__: Curated sentiment dictionaries combined with either bag-of-words representations (ignoring word order) or hand-designed negation features (ain’t gonna capture everything)
        * __DL__: Same deep learning model that was used for morphology, syntax and logical semantics can be used;  
        __RecursiveNN__.        

2. **Question Answering:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents52}  
    :   * __Traditional__: A lot of feature engineering to capture world and other knowledge, e.g., regular expressions, Berant et al. (2014)
        * __DL__: Facts are stored in vectors.  FILL-IN  
        __FILL-IN__.      


3. **Machine Translation:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents53}  
    :   * __Traditional__: Complex approaches with very high error rates.  
        * __DL__: _Neural Machine Translation_.  
            Source sentence is mapped to _vector_, then output sentence generated.  
            [Sutskever et al. 2014, Bahdanau et al. 2014, Luong and Manning 2016]  
        __FILL-IN__.   
        ![img](/main_files/dl/nlp/1/5.png){: width="70%"}

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents54}  
    :   

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents55}  
    :   

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents56}  
    :   