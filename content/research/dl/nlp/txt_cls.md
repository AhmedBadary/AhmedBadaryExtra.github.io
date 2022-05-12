---
layout: NotesPage
title: Text Classification
permalink: /work_files/research/dl/nlp/txt_cls
prevLink: /work_files/research/dl/nlp.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Introduction](#content1)
  {: .TOC1}
<!--   * [SECOND](#content2)
  {: .TOC2}
  * [THIRD](#content3)
  {: .TOC3} -->
</div>

***
***

[Convolutional Neural Networks for Language (CMU)](https://www.youtube.com/watch?v=HBcr5jCBynI&t=7s)  
[Text Classification (Oxford)](https://www.youtube.com/watch?v=0qG7gjTNhwM&list=PL613dYIGMXoZBtZhbyiBqb0QtgK6oJbpm&index=8)  

* [Googles Text Classification Guide (Blog)](https://developers.google.com/machine-learning/guides/text-classification)  




## Introduction
{: #content1}

1. **Text Classification Breakdown:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    We can think of text classification as being broken down into a two stage process:  
    1. __Representation:__ Process text into some (fixed) representation -> How to learn $$\mathbf{x}'$$.  
    2. __Classification:__ Classify document given that representation $$\mathbf{x}'$$ -> How to learn $$p(c\vert x')$$.  


2. **Representation:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    __Bag of Words (BOW):__{: style="color: red"}  
    * __Pros:__  
        * Easy, no effort
    * __Cons__:  
        * Variable size, ignores sentential structure, sparse representations  

    __Continuous BOW:__{: style="color: red"}  
    * __Pros:__  
        * Continuous Repr.
    * __Cons__:  
        * Ignores word ordering  

    __Deep CBOW:__{: style="color: red"}  
    * __Pros:__  
        * Can learn feature combinations (e.g. "not" AND "hate")  
    * __Cons__:  
        * Cannot learn word-ordering (positional info) directly (e.g. "not hate")  

    __Bag of n-grams:__{: style="color: red"}  
    * __Pros:__  
        * Captures (some) combination features and word-ordering (e.g. "not hate"), works well  
    * __Cons__:  
        * Parameter Explosion, no sharing between similar words/n-grams


3. **CNNs for Text:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    Two main paradigms:  
    1. __Context-window modeling:__ for *__tagging__* etc. get the surrounding context before tagging.  
    2. __Sentence modeling:__ do convolution to extract n-grams, pooling to combine over whole sentence.  

<!-- 
4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18}

***

## SECOND
{: #content2}

1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents26}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents27}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents28}

***

## THIRD
{: #content3}

1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents34}

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents35}

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents36}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents37}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents38}

 -->