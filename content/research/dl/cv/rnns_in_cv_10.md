---
layout: NotesPage
title: Recurrent Neural Networks <br /> Applications in Computer Vision
permalink: /work_files/research/dl/rnns_cv
prevLink: /work_files/research/dl/cv.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [RNNs](#content1)
  {: .TOC1}
  * [Applications in CV](#content2)
  {: .TOC2}
  * [Implementations and Training (LSTMs and GRUs)](#content3)
  {: .TOC3}
</div>

***
***

## RNNs
{: #content1}

### [Refer to this section on RNNs](ahmedbadary.ml/work_files/research/dl/nlp/rnns)

1. **Process Sequences:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    :   * __One-to-One__  
        * __One-to-Many__: 
            Image Captioning: image -> seq of words
        * __Many-to-One__: 
            Sentiment Classification: seq of words -> Sentiment
        * __Many-to-Many__:   
            Machine Translation: seq of words -> seq of words
        * __(Discrete) Many-to-Many__:  
            Frame-Level Video Classification: seq. of frames -> seq of classes per frame  
    :   ![img](/main_files/cs231n/10/1.png){: width="80%"}  


2. **RNN Structure:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    :   We can process a sequence of vectors $$\vec{x}$$ by applying a recurrence formula__ at every time step:  
    :   $$h_t = f_W(h_{t-1}, x_t)$$
    :   where $$h_t$$ is the new state, $$f_W$$ is some function with weights $$W$$, $$h_{t-1}$$ is the old state, and $$x_t$$ is the input vector at some time step $$t$$.   
        > The __same__ _function_ and _set of parameters (weights)_ are used at every time step.  

3. **A Vanilla Architecture of an RNN:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    :   $$
        \begin{align}
        h_t &= f_W(h_{t-1}, x_t)
        h_t &= tanh(W_{hh}h_t{t-1} + W_{xh}x_t)  
        y_t &= W_{hy}h_t
        \end{align}
        $$

4. **The RNN Computational Graph:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    :   * __Many-to-Many__:       
    :   ![img](/main_files/cs231n/10/2.png){: width="80%"}
    :   * __One-to-Many__:  
    :  ![img](/main_files/cs231n/10/3.png){: width="80%"} 
    :   * __Seq-to-Seq__:   
    :   ![img](/main_files/cs231n/10/4.png){: width="80%"}

5. **Example Architecture: Character-Level Language Model:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  
    :   ![img](/main_files/cs231n/10/5.png){: width="80%"}
    :   ![img](/main_files/cs231n/10/6.png){: width="80%"}

6. **The Functional Form of a Vanilla RNN (Gradient Flow):**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}  
    :   ![img](/main_files/cs231n/10/7.png){: width="80%"}

***

## Applications in CV
{: #content2}

### Coming Soon!

***

## Implementations and Training (LSTMs and GRUs)
{: #content3}

### Coming Soon!