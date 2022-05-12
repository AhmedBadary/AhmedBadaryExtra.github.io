---
layout: NotesPage
title: Sentence and Contextualized Word Representations <br /> (Multi-Task/Transfer Learning)
permalink: /work_files/research/dl/nlp/sent_embeds
prevLink: /work_files/research/dl/nlp.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Sentence Representations](#content1)
  {: .TOC1}
  * [Training Sentence Representations](#content2)
  {: .TOC2}
  * [Contextualized Word Representations](#content3)
  {: .TOC3}
<!--   * [FOURTH](#content4)
  {: .TOC4}
  * [FIFTH](#content5)
  {: .TOC5}
  * [SIXTH](#content6)
  {: .TOC6}
 -->
</div>

***
***

## Sentence Representations
{: #content1}

1. **What?:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    Sentence Representation/Embedding Learning is focused on producing one feature vector to represent a sentence in a latent (semantic) space, while preserving linear properties (distances, angles).  
    <br>

2. **Tasks:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    * Sentence Classification
    * Paraphrase Identification
    * Semantic Similarity
    * Textual Entailment (i.e. Natural Language Inference)
    * Retrieval  
    <br>

3. **Methods:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    __Multi-Task Learning__:  
    In particular, people do __*Pre-Training*__ on other tasks, and then use the pre-trained weights and fine-tune them on a new task.
    <br>

4. **End-To-End VS Pre-Training:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    We can always use End-To-End objectives, however, there are two problems that arise, and can be mitigated by pre-training:  
    {: #lst-p}
    * Paucity of Training Data  
    * Weak Feedback from end of sentence only for text classification (explain?)
    <br>

<!-- 5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18}
 -->
***

## Training Sentence Representations
{: #content2}

1. **Language Model Transfer _(Dai and Le 2015)_:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    * __Model:__ LSTM
    * __Objective:__ Language modeling objective
    * __Data:__ Classification data itself, or Amazon reviews
    * __Downstream:__ On text classification, initialize weights and continue training
    <br>

2. **Unidirectional Training + Transformer - OpenAI GPT _(Radford et al. 2018)_:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}  
    * __Model:__  Masked self-attention
    * __Objective:__  Predict the next word left->right
    * __Data:__  BooksCorpus
    * __Downstream:__  Some task fine-tuning, other tasks additional multi-sentence training
    <br>

3. **Auto-encoder Transfer _(Dai and Le 2015)_:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}  
    * __Model:__ LSTM
    * __Objective:__ From single sentence vector, reconstruct the sentence
    * __Data:__ Classification data itself, or Amazon reviews
    * __Downstream:__ On text classification, initialize weights and continue training
    <br>

4. **Context Prediction Transfer - SkipThought Vectors _(Kiros et al. 2015)_:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}  
    * __Model:__  LSTM
    * __Objective:__  Predict the surrounding sentences
    * __Data:__  Books, important because of context
    * __Downstream:__  Train logistic regression on $$[\|u-v\|; u * v]$$ (component-wise)
    <br>

5. **Paraphrase ID Transfer _(Wieting et al. 2015)_:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}
    * __Model:__ Try many different ones
    * __Objective:__ Predict whether two phrases are paraphrases or not from
    * __Data:__ Paraphrase database (http://paraphrase.org), created from bilingual data  
        * **Large Scale Paraphrase Data - ParaNMT-50MT _(Wieting and Gimpel 2018)_:**  
            * Automatic construction of large paraphrase DB:
                * Get large parallel corpus (English-Czech) 
                * Translate the Czech side using a SOTA NMT system 
                * Get automated score and annotate a sample  
            * Corpus is huge but includes noise, 50M sentences (about 30M are high quality) 
            * Trained representations work quite well and generalize  
    * __Downstream Usage:__ Sentence similarity, classification, etc.
    * __Result:__ Interestingly, LSTMs work well on in-domain data, but word averaging generalizes better
    <br>

7. **Entailment Transfer - InferSent _(Conneau et al. 2017)_:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents27}  
    * __Previous objectives__ use no human labels, but what if:
    * __Objective:__ supervised training for a task such as entailment learn generalizable embeddings?  
        * Task is more difficult and requires capturing nuance → yes?, or data is much smaller → no?  
    * __Model:__ Bi-LSTM + max pooling  
    * __Data:__ Stanford NLI, MultiNLI
    * __Results:__ Tends to be better than unsupervised objectives such as SkipThought  

<!-- 8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents28} -->

***

## Contextualized Word Representations
{: #content3}

<!-- 1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents34}

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents35}

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents36}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents37}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents38}
 -->

***


<!-- ## FOURTH
{: #content4}

1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents41}

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents42}

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents43}

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents44}

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents45}

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents46}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents47}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents48}

-->