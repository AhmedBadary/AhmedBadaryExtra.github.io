---
layout: NotesPage
title: Word Vector Representations <br /> word2vec
permalink: /work_files/research/dl/nlp/wordvec
prevLink: /work_files/research/dl/nlp.html
---


<div markdown="1" class = "TOC">
# Table of Contents

  * [Word Meaning](#content1)
  {: .TOC1}
  * [Word Embeddings](#content2)
  {: .TOC2}
  * [Word2Vec](#content3)
  {: .TOC3}
  * [FOURTH](#content4)
  {: .TOC4}
</div>

***
***

[W2V Detailed Tutorial - Skip Gram (Stanford)](http://mccormickml.com/2016/04/19/word2vec-tutorial-the-skip-gram-model/)  
[W2V Detailed Tutorial - Negative Sampling (Stanford)](http://mccormickml.com/2017/01/11/word2vec-tutorial-part-2-negative-sampling/)  
[Commented word2vec C code](https://github.com/chrisjmccormick/word2vec_commented)  
[W2V Resources](http://mccormickml.com/2016/04/27/word2vec-resources/)  
[An overview of word embeddings and their connection to distributional semantic models
](http://blog.aylien.com/overview-word-embeddings-history-word2vec-cbow-glove/)  
[On Word Embeddings (Ruder)](http://ruder.io/word-embeddings-1/)  
* [Eigenwords: Spectral Word Embeddings (paper!)](http://jmlr.org/papers/volume16/dhillon15a/dhillon15a.pdf)  
* [Stop Using word2vec (blog)](https://multithreaded.stitchfix.com/blog/2017/10/18/stop-using-word2vec/)  
* [Word2vec Inspired Recommendations In Production (blog)](https://medium.com/building-creative-market/word2vec-inspired-recommendations-in-production-f2c6a6b5b0bf)  




## Word Meaning
{: #content1}

1. **Representing the Meaning of a Word:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    Commonest linguistic way of thinking of meaning:  
    Signifier $$\iff$$ Signified (idea or thing) = denotation
    
2. **How do we have usable meaning in a computer:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    Commonly:  Use a taxonomy like WordNet that has hypernyms (is-a) relationships and synonym sets
    
3. **Problems with this discrete representation:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    * __Great as a resource but missing nuances__:  
        * Synonyms:  
            adept, expert, good, practiced, proficient, skillful
    * __Missing New Words__
    * __Subjective__  
    * __Requires human labor to create and adapt__  
    * __Hard to compute accurate word similarity__:  
        * _One-Hot Encoding_: in vector space terms, this is a vector with one 1 (at the position of the word) and a lot of zeroes (elsewhere).  
            * It is a __localist__ representation   
            * There is __no__ natural __notion of similarity__ in a set of one-hot vectors   
    
4. **Distributed Representations of Words:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    A method where vectors encode the similarity between the words.  
    
    The meaning is represented with real-valued numbers and is "_smeared_" across the vector.  
    
    > Contrast with __one-hot encoding__.  
    

5. **Distributional Similarity:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  
    is an idea/hypothesis that one can describe the meaning of words by the context in which they appear in.   
    
    > Contrast with __Denotational Meaning__ of words.  
    
6. **The Big Idea:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}  
    We will build a dense vector for each word type, chosen so that it is good at predicting other words appearing in its context.  
    
7. **Learning Neural Network Word Embeddings:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}  
    We define a model that aims to predict between a center word $$w_t$$ and context words in terms of word vectors.    
    <p>$$p(\text{context} \vert  w_t) = \ldots$$</p>   

    __The Loss Function__:    
    <p>$$J = 1 - p(w_{-t} \vert  w_t)$$</p>    

    We look at many positions $$t$$ in a big language corpus  
    We keep adjusting the vector representations of words to minimize this loss  

    
8. **Relevant Papers:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18}  
    * Learning representations by back-propagating errors (Rumelhart et al., 1986) 
    * A neural probabilistic language model (Bengio et al., 2003) 
    * NLP (almost) from Scratch (Collobert & Weston, 2008) 
    * A recent, even simpler and faster model: word2vec (Mikolov et al. 2013) à intro now
    
***

## Word Embeddings
{: #content2}

1. **Main Ideas:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    * Words are represented as vectors of real numbers
    * Words with similar vectors are _semantically_ similar 
    * Sometimes vectors are low-dimensional compared to the vocabulary size  
    
2. **The Clusterings:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}  
    __Relationships (attributes) Captured__:    
    * __Synonyms:__ car, auto
    * __Antonyms:__ agree, disagree
    * __Values-on-a-scale:__ hot, warm, cold
    * __Hyponym-Hypernym:__ "Truck" is a type of "car", "dog" is a type of "pet"
    * __Co-Hyponyms:__ "cat"&"dog" is a type of "pet"
    * __Context:__ (Drink, Eat), (Talk, Listen)

3. **Word Embeddings Theory:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}  
    Distributional Similarity Hypothesis

4. **History and Terminology:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}  
    Word Embeddings = Distributional Semantic Model = Distributed Representation = Semantic Vector Space = Vector Space Model  

5. **Applications:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}  
    * Word Similarity
    * Word Grouping
    * Features in Text-Classification
    * Document Clustering
    * NLP:  
        * POS-Tagging
        * Semantic Analysis
        * Syntactic Parsing

6. **Approaches:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents26}  
    * __Count__: word count/context co-occurrences   
        * *__Distributional Semantics__*:    
            1. Summarize the occurrence statistics for each word in a large document set:   
                ![img](/main_files/dl/nlp/1/1.png){: width="40%"}  
            2. Apply some dimensionality reduction transformation (SVD) to the counts to obtain dense real-valued vectors:   
                ![img](/main_files/dl/nlp/1/2.png){: width="40%"}  
            3. Compute similarity between words as vector similarity:  
                ![img](/main_files/dl/nlp/1/3.png){: width="40%"}  
    * __Predict__: word based on context  
        * __word2vec__:  
            1. In one setup, the goal is to predict a word given its context.  
                ![img](/main_files/dl/nlp/1/4.png){: width="80%"}   
            2. Update word representations for each context in the data set  
            3. Similar words would be predicted by similar contexts

7. **Parameters:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents27}
    * Underlying Document Set   
    * Context Size
    * Context Type

8. **Software:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents28}  
    ![img](/main_files/dl/nlp/1/5.png){: width="80%"}  
    
***

## Word2Vec
{: #content3}

11. **Word2Vec:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents311}  
    __Word2Vec__ _(Mikolov et al. 2013)_ is a framework for learning word representations as vectors. It is based on the idea of _distributional similarity_.  
    <br>

1. **Main Idea:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}  
    * Given a large corpus of text
    * Represent every word, in a fixed vocabulary, by a _vector_ 
    * Go through each position $$t$$ in the text, which has a __center word__ $$c$$ and __context words__ $$o$$ 
    * Use the *__similarity of the word vectors__* for $$c$$ and $$o$$ to *__calculate the probability__* of $$o$$ given $$c$$ (SG)  
    * *__Keep adjusting the word vectors__* to __maximize this probability__  

    ![img](/main_files/dl/nlp/1/6.png){: width="80%"}  
    
2. **Algorithms:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}  
    1. __Skip-grams (SG)__:  
        Predict context words given target (position independent)
    2. __Continuous Bag of Words (CBOW)__:  
        Predict target word from bag-of-words context  
    <br>
    
3. **Training Methods:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}  
    * __Basic__:    
        1. Naive Softmax  
    * __(Moderately) Efficient__:  
        1. Hierarchical Softmax
        2. Negative Sampling   
    <br>
    
4. **Skip-Gram Prediction Method:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents34}  
    Skip-Gram Models aim to predict the _distribution (probability)_ of context words from a center word.  
    > CBOW does the opposite, and aims to predict a center word from the surrounding context in terms of word vectors.   

    __The Algorithm__:    
    1. We generate our one hot input vector $$x \in \mathbf{R}^{\vert V\vert }$$ of the center word.  
    2. We get our embedded word vector for the center word $$v_c = V_x \in \mathbf{R}^n$$  
    3. Generate a score vector $$z = \mathcal{U}_ {v_c}$$ 
    4. Turn the score vector into probabilities, $$\hat{y} = \text{softmax}(z)$$ 
        > Note that $$\hat{y}_{c−m}, \ldots, \hat{y}_{c−1}, \hat{y}_{c+1}, \ldots, \hat{y}_{c+m}$$ are the probabilities of observing each context word.  
    5. We desire our probability vector generated to match the true probabilities, which is  
        $$ y^{(c−m)} , \ldots, y^{(c−1)} , y^{(c+1)} , \ldots, y^{(c+m)}$$,  
        the one hot vectors of the actual output.  
    <br>
    
5. **Word2Vec Details:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents35}  
    * For each word (position) $$t = 1 \ldots T$$, predict surrounding (context) words in a window of _“radius”_ $$m$$ of every word.  

    __Calculating $$p(o \vert c)$$[^2] the probability of outside words given center word:__  
    * We use two vectors per word $$w$$:  
        * $$v_{w}$$: $$\:$$  when $$w$$ is a center word  
        * $$u_{w}$$: $$\:$$ when $$w$$ is a context word  
    * Now, for a center word $$c$$ and a context word $$o$$, we calculate the probability:  
        <p>$$\\{\displaystyle p(o \vert  c) = \dfrac{e^{u_o^Tv_c}}{\sum_{w\in V} e^{u_w^Tv_c}}} \:\:\:\:\:\:\:\:\:\:\:\:\\$$</p>  
        <button>Constructing the Probability Distribution (Prediction Function)</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
        * ![img](/main_files/dl/nlp/1/7.png){: width="80%"}   
        * The Probability Distribution $$p(o \vert c)$$ is an application of the __softmax__ function on the, __dot-product__, similarity function $$u_o^Tv_c$$  
        * The __Softmax__ function, allows us to construct a probability distribution by making the numerator positive, and normalizing the function (to $$1$$) with the denominator  
        * The __similarity function $$u_o^Tv_c$$__ allows us to model as follows: the more the _similarity_ $$\rightarrow$$ the larger the _dot-product_; the larger the _exponential_ in the softmax    
        {: hidden=""}
    <br>
    
6. **The Objective:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents36}  
    __Goal:__{: style="color: red"}   
    Maximize the probability of any context word given the current center word.  

    We start with the __Likelihood__ of being able to predict the context words given center words and the parameters $$\theta$$ (only the wordvectors).  
    __The Likelihood:__  
    <p>$$L(\theta)=\prod_{t=1}^{T} \prod_{-m \leq j \leq m \atop j \neq 0} P\left(w_{t+j} | w_{t} ; \theta\right)$$</p>  
    
    __The objective:__{: style="color: red"}    
    The Objective is just the (average) __negative log likelihood__:  
    <p>$$J(\theta) = -\frac{1}{T} \log L(\theta)= - \dfrac{1}{T} \sum_{t=1}^{t} \sum_{-m \leq j \leq m \\ \:\:\:\:j\neq 0} \log p(w_{t+j} \vert  w_t ; \theta))$$</p>  

    Notice: Minimizing objective function $$\iff$$ Maximizing predictive accuracy[^1]  
    <br>
    
7. **The Gradients:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents37}  
    We have a vector of parameters $$\theta$$ that we are trying to optimize over, and We need to calculate the gradient of the two sets of parameters in $$\theta$$; namely, $$\dfrac{\partial}{\partial v_c}$$ and $$\dfrac{\partial}{\partial u_o}$$.  

    __The gradient $$\dfrac{\partial}{\partial v_c}$$:__{: style="color: red"}  
    <p>$$\dfrac{\partial}{\partial v_c} \log p(o\vert c) = u_o - \sum_{w'\in V} p{(w' | c)} \cdot u_{w'}$$</p>  

    __Interpretation:__  
    We are getting the slope by: taking the __observed representation of the context word__ and subtracting away (_"what the model thinks the context should look like"_) the __weighted average of the representations of each word multiplied by its probability in the current model__  
    (i.e. the __Expectation of the context word vector__ i.e. __the expected context word according to our current model__)   
    > I.E.  
        __The difference between the expected context word and the actual context word__{: style="color: green"}  
    

    __Importance Sampling:__{: style="color: red"}  
    <p>$$\sum_{w_{i} \in V} \left[\frac{\exp \left(-\mathcal{E}\left(w_{i}\right)\right)}{\sum_{w_{i} \in V} \exp \left(-\mathcal{E}\left(w_{i}\right)\right)}\right] \nabla_{\theta} \mathcal{E}\left(w_{i}\right) \\ = \sum_{w_{i} \in V} P\left(w_{i}\right) \nabla_{\theta} \mathcal{E}\left(w_{i}\right)$$</p>  
    <br>

    <p>$$\mathbb{E}_{w_{i} \sim P}\left[\nabla_{\theta} \mathcal{E}\left(w_{i}\right)\right] =\sum_{w_{i} \in V} P\left(w_{i}\right) \nabla_{\theta} \mathcal{E}\left(w_{i}\right)$$</p>  

    * $$P\left(w_{i}\right) \approx \frac{r(w_i)}{R}$$,  

    <p>$$\mathbb{E}_{w_{i} \sim P}\left[\nabla_{\theta} \mathcal{E}\left(w_{i}\right)\right] \approx \sum_{w_{i} \in V} \frac{r(w_i)}{R} \nabla_{\theta} \mathcal{E}\left(w_{i}\right)$$</p>  

    <p>$$\mathbb{E}_{w_{i} \sim P}\left[\nabla_{\theta} \mathcal{E}\left(w_{i}\right)\right] \approx \frac{1}{R} \sum_{i=1}^{m} r\left(w_{i}\right) \nabla_{\theta} \mathcal{E}\left(w_{i}\right)$$</p>  
    
    where $$r(w)=\frac{\exp (-\mathcal{E}(w))}{Q(w)}$$, $$R=\sum_{j=1}^{m} r\left(w_{j}\right)$$, and $$Q$$ is the __unigram distribution__ of the training set.    

8. **Notes:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents38}  
    * __Mikolov on SkipGram vs CBOW__:  
        * Skip-gram: works well with small amount of the training data, represents well even rare words or phrases.  
        * CBOW: several times faster to train than the skip-gram, slightly better accuracy for the frequent words.  
    * __Further Readings__:  
        * [A Latent Variable Model Approach to PMI-based Word Embeddings](https://aclweb.org/anthology/Q16-1028)
        * [Linear Algebraic Structure of Word Senses, with Applications to Polysemy](https://transacl.org/ojs/index.php/tacl/article/viewFile/1346/320)
        * [On the Dimensionality of Word Embedding](https://papers.nips.cc/paper/7368-on-the-dimensionality-of-word-embedding.pdf)
        * [Improving Distributional Similarity with Lessons Learned from Word Embeddings](https://www.aclweb.org/anthology/Q15-1016)
            
    
[^1]: accuracy of predicting words in the context of another word  
[^2]: I.E. $$p(w_{t+j} \vert  w_t)$$  