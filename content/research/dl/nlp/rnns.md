---
layout: NotesPage
title: Language Modeling  <br /> Recurrent Neural Networks (RNNs)
permalink: /work_files/research/dl/nlp/rnns
prevLink: /work_files/research/dl/nlp.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Introduction to and History of Language Models](#content1)
  {: .TOC1}
  * [Recurrent Neural Networks](#content2)
  {: .TOC2}
  * [RNN Language Models](#content3)
  {: .TOC3}
  * [Training RNNs](#content4)
  {: .TOC4}
  * [RNNs in Sequence Modeling](#content4)
  {: .TOC4}
  * [Bidirectional and Deep RNNs](#content4)
  {: .TOC4}
</div>

***
***

[Language Modeling and RNNS I (Oxford)](https://www.youtube.com/watch?v=nfyE8oF23yQ&list=PL613dYIGMXoZBtZhbyiBqb0QtgK6oJbpm&index=6&t=0s)  
> Note: 25:00 (important problem not captured w/ newer models about smoothing and language distribution as Heaps law)  

[LMs Stanford Notes](https://web.stanford.edu/class/cs224n/readings/cs224n-2019-notes05-LM_RNN.pdf)  




## Introduction to and History of Language Models 
{: #content1}

1. **Language Models:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    A __Language Model__ is a statistical model that computes a _probability distribution_ over sequences of words.  

    It is a __time-series prediction__ problem in which we must be _very careful_ to *__train on the past__* and *__test on the future__*.   


2. **Applications:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    :   * __Machine Translation (MT)__:   
            * Word Ordering:  
                p("the cat is small") > p("small the cat is")  
            * Word Choice:  
                p("walking home after school") > p("walking house after school")
        * __Speech Recognition__:     
            * Word Disambiguation:  
                p("The listeners _recognize speech_") > p("The listeners _wreck a nice beach_")  
        * __Information Retrieval__: 
            * Used in _query likelihood model_
            
3. **Traditional Language Models:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    * Most language models employ the chain rule to decompose the _joint probability_ into a _sequence of conditional probabilities_:  
        <p>$$\begin{array}{c}{P\left(w_{1}, w_{2}, w_{3}, \ldots, w_{N}\right)=} \\ {P\left(w_{1}\right) P\left(w_{2} | w_{1}\right) P\left(w_{3} | w_{1}, w_{2}\right) \times \ldots \times P\left(w_{N} | w_{1}, w_{2}, \ldots w_{N-1}\right)}\end{array}$$</p>  
        Note that this decomposition is exact and allows us to model complex joint distributions by learning conditional distributions over the next word $$(w_n)$$ given the history of words observed $$\left(w_{1}, \dots, w_{n-1}\right)$$.   
        Thus, the __Goal__ of the __LM-Task__ is to find *__good conditional distributions__* that we can _multiply_ to get the *__Joint Distribution__*.  
        > Allows you to predict the first word, then the second word _given the first word_, then the third given the first two, etc..  

    * The Probability is usually conditioned on window of $$n$$ previous words  
        * An incorrect but necessary Markovian assumption:  
            <p>$$P(w_1, \ldots, w_m) = \prod_{i=1}^m P(w_i | w_1, \ldots, w_{i-1}) \approx \prod_{i=1}^m P(w_i | w_{i-(n-1)}, \ldots, w_{i-1})$$</p>  
            * Only previous history matters
            * __Limited Memory__: only last $$n-1$$ words are included in history  
        > E.g. $$2-$$gram LM (only looks at the *__previous word__*):  
            <p>$$\begin{aligned} p\left(w_{1}, w_{2}, w_{3},\right.& \ldots &, w_{n} ) \\ &=p\left(w_{1}\right) p\left(w_{2} | w_{1}\right) p\left(w_{3} | w_{1}, w_{2}\right) \times \ldots \\ & \times p\left(w_{n} | w_{1}, w_{2}, \ldots w_{n-1}\right) \\ & \approx p\left(w_{1}\right) p\left(w_{2} | w_{1}\right) p\left(w_{3} | w_{2}\right) \times \ldots \times p\left(w_{n} | w_{n-1}\right) \end{aligned}$$</p>   
        The conditioning context, $$w_{i-1}$$, is called the __history__.  
    * The __MLE__ estimate for probabilities, compute for  
        * Bi-grams:  
            <p>$$P(w_2 \| w_1) = \dfrac{\text{count}(w_1, w_2)}{\text{count}(w_1)}$$</p>  
        * Tri-grams:  
            <p>$$P(w_3 \| w_1, w_2) = \dfrac{\text{count}(w_1, w_2, w_3)}{\text{count}(w_1, w_2)}$$</p>  

4. **Issues with the Traditional Approaches:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    To improve performance we need to:  
    * Keep higher n-gram counts  
    * Use Smoothing  
    * Use Backoff (trying n-gram, (n-1)-gram, (n-2)-grams, ect.)  
        When? If you never saw a 3-gram b4, try 2-gram, 1-gram etc.  
    However, 
    * There are __A LOT__ of n-grams
        * $$\implies$$ Gigantic RAM requirements  

5. **NLP Tasks as LM Tasks:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  
    Much of Natural Language Processing can be structured as *__(conditional) Language Modeling__*:  
    * __Translation__:  
        <p>$$p_{\mathrm{LM}}(\text { Les chiens aiment les os }\| \| \text { Dogs love bones) }$$</p>  
    * __QA__:  
        <p>$$p_{\mathrm{LM}}(\text { What do dogs love? }\| \| \text { bones } . | \beta)$$</p>
    * __Dialog__:  
        <p>$$p_{\mathrm{LM}}(\text { How are you? }\| \| \text { Fine thanks. And you? } | \beta)$$</p>    
    > where $$\| \|$$ means "concatenation", and $$\beta$$ is an observed data (e.g. news article) to be conditioned on.  

            
6. **Analyzing the LM Tasks:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}  
    The simple objective of _modeling the next word given observed history_ contains much of the complexity of __natural language understanding (NLU)__ (e.g. reasoning, intelligence, etc.).  

    Consider predicting the extension of the utterance:  
    <p>$$p(\cdot | \text { There she built a) }$$</p>  
    > The distribution of what word to predict right now is quite flat; you dont know where _"there"_ is, you dont know who _"she"_ is, you dont know what she would want to _"build"_.    

    However, With more context we are able to use our knowledge of both language and the world to heavily constrain the distribution over the next word.  
    <p>$$p(\cdot | \color{red} {\text { Alice }} \text {went to the} \color{blue} {\text { beach. } } \color{blue} {\text {There}} \color{red} {\text { she}} \text { built a})$$</p>  
    > At this point your distributions getting _very peaked_ about what could come next and the reason is because you understand language you understand that in the second utterance "she" is "Alice" and "There" is "Beach" so you've resolved those Co references and you can do that because you understand the syntactic structure of the first utterance; you understand we have a subject and object, where the verb phrase is, all of these things you do automatically and then, using the semantics that "at a beach you build things like sandcastles or boats" and so you can __constrict your distribution__.  

    If we can get a automatically trained machine to do that then we've come a long way to solving AI.  
    > "The diversity of tasks the model is able to perform in a zero-shot setting suggests that high-capacity models trained to _maximize the likelihood of a sufficiently varied text corpus_ begin to learn how to perform a surprising amount of tasks without the need for explicit supervision" - GPT 2 


7. **Evaluating a Language Model \| The Loss:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}  
    For a probabilistic model, it makes sense to evaluate how well the "learned" distribution matches the real distribution of the data (of real utterances). A good model assigns real utterances $$w_{1}^{N}$$  from a language a high probability. This can be measured with __Cross-Entropy__:  
    <p>$$H\left(w_{1}^{N}\right)=-\frac{1}{N} \log _{2} p\left(w_{1}^{N}\right)$$</p>  
    __Why Cross-Entropy:__ It is a measure of _how many bits are need to encode text with our model_ (bits you would need to represent the distribution).[^1]  
    > Commonly used for __character-level__.  

    Alternatively, people tend to use __Perplexity__:  
    <p>$$\text { perplexity }\left(w_{1}^{N}\right)=2^{H\left(w_{1}^{N}\right)}$$</p>  
    __Why Perplexity:__  It is a measure of how _surprised our model is on seeing each word_.     
    > If __no surprise__, the perplexity $$ = 1$$.    
    > Commonly used for __word-level__.  
    <br>

8. **Language Modeling Data:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18}  
    Language modelling is a time series prediction problem in which we must be careful to train on the past and test on the future.  
    If the corpus is composed of articles, it is best to ensure the test data is drawn from a disjoint set of articles to the training data.  

    Two popular data sets for language modeling evaluation are a preprocessed version of the Penn Treebank,1 and the Billion Word Corpus.2 Both are __flawed__:     
    * The PTB is very small and has been heavily processed. As such it is not representative of natural language.  
    * The Billion Word corpus was extracted by first randomly permuting sentences in news articles and then splitting into training and test sets. As such train and test sentences come from the same articles and overlap in time
    
    The recently introduced __WikiText datasets__ are a better option.  

9. **Three Approaches to Parameterizing Language Models:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents19}  
    1. __Count-Based N-gram models__: we approximate the history of observed words with just the previous $$n$$ words.  
        They capture __Multinomial distributions__.   
    2. __Neural N-gram models__: embed the same fixed n-gram history in a _continuous space_ and thus better capture _correlations between histories_.  
        Replace the _Multinomial distributions_ with an __FFN__.  
    3. __RNNs__: drop the fixed n-gram history and _compress the entire history in a fixed length vector_, enabling _long range correlations_ to be captured.   
        Replace the __finite__ history, captured by the conditioning context $$w_{i-1}$$, with an __infinite__ history, captured by the (previous) hidden state $$h_{n-1}$$ (but also $$w_{n=1})$$.  
    <br>

10. **Bias vs Variance in LM Approximations:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents110}  
    The main issue in language modeling is compressing the history (a string). This is useful beyond language modeling in classification and representation tasks.  
    * With n-gram models we approximate the history with only the last n words  
    * With recurrent models (RNNs, next) we compress the unbounded history into a fixed sized vector  

    We can view this progression as the classic __Bias vs. Variance tradeoff__ in ML:  
    * __N-gram models__: are biased but low variance.  
        No matter how much data (infinite) they will always be wrong/biased.  
    * __RNNs:__ decrease the bias considerably, hopefully at a small cost to variance.  

    Consider predicting the probability of a sentence by how many times you have seen it before. This is an _unbiased estimator with (extremely) high variance_.  
    * In the limit of infinite data, gives true distribution.  
    <br>

11. **Scaling Language Models (Large Vocabularies):**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents111}  
    __Bottleneck:__  
    Much of the computational cost of a Neural LM is a function of the __size of the vocabulary__ and is dominated by calculating the softmax:  
    <p>$$\hat{p}_{n}=\operatorname{softmax}\left(W h_{n}+b\right)$$</p>  

    __Solutions:__  
    * __Short-Lists__: use the neural LM for the most frequent words, and a traditional _n-gram_ LM for the rest.  
        While easy to implement, this nullifies the Neural LMs main advantage, i.e. generalization to rare events.  
    * __Batch local short-lists__: approximate the full partition function for data instances from a segment for the data with a subset of vocabulary chosen for that segment.  
    * __Approximate the gradient/change the objective__:  if we did not have to sum over the vocabulary to normalize during training, it would be much faster. It is tempting to consider maximizing likelihood by making the log partition function an independent parameter $$c$$, but this leads to an ill defined objective:  
        <p>$$\hat{p}_{n} \equiv \exp \left(W h_{n}+b\right) \times \exp (c)$$</p>  
        > What does the Softmax layer do?  
        > The idea of the Softmax is to say: at each time step look at the word we want to predict and the whole vocab; where we try to __maximize the probability of the word we want to predict__ and __minimize the probability of ALL THE OTHER WORDS__.  

        So, The better solution is to try to approximate what the softmax does using: 
        * __Noise Contrastive Estimation (NCE)__: this amounts to learning a binary classifier to distinguish data samples from $$(k)$$ samples from a noise distribution (a unigram is a good choice):  
        <p>$$p\left(\text { Data }=1 | \hat{p}_{n}\right)=\frac{\hat{p}_{n}}{\hat{p}_{n}+k p_{\text { noise }}\left(w_{n}\right)}$$</p>   
        Now parametrizing the log partition function as $$c$$ does not degenerate. This is very effective for _speeding up training_ but has no effect on _testing_.   
        * __Importance Sampling (IS)__: similar to NCE but defines a multiclass classification problem between the true word and noise samples, with a Softmax and cross entropy loss.   
        * [**(more on) Approximating the Softmax**](http://ruder.io/word-embeddings-softmax/index.html){: value="show" onclick="iframePopA(event)"}
            <a href="http://ruder.io/word-embeddings-softmax/index.html"></a>
            <div markdown="1"> </div>    
    * __Factorize the output vocabulary__: the idea is to decompose the (one big) softmax into a series of softmaxes (2 in this case). We map words to a set of classes, then we, first, predict which class the word is in, and then we predict the right word from the words in that class.  
        One level factorization works well (Brown clustering is a good choice, frequency binning is not):  
        <p>$$p\left(w_{n} | \hat{p}_{n}^{\text { class }}, \hat{p}_{n}^{\text { word }}\right)=p\left(\operatorname{class}\left(w_{n}\right) | \hat{p}_{n}^{\text { class }}\right) \times p\left(w_{n} | \operatorname{class}\left(w_{n}\right), \hat{p}_ {n}^{\text { word }}\right)$$</p>  
        where the function $$\text{ class}(\cdot)$$ maps each word to one class. Assuming balanced classes, this gives a quadratic, $$\root{V}$$ speedup.  
        * [**Binary Tree Factorization for $$\log{V} Speedup**](https://www.youtube.com/embed/eDUaRvMDs-s?start=2818){: value="show" onclick="iframePopA(event)"}
        <a href="https://www.youtube.com/embed/eDUaRvMDs-s?start=2818"></a>
            <div markdown="1"> </div>   

    __Complexity Comparison of the different solutions:__  
    ![img](/main_files/dl/nlp/rnn/8.png){: width="70%"}  
    <br>
        
12. **Sub-Word Level Language Models:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents112}  
    Could be viewed as an alternative to changing the softmax by changing the input granularity and model text at the __morpheme__ or __character__ level.  
    This results in a much smaller softmax and no unknown words, but the downsides are longer sequences and longer dependencies; moreover, a lot of the structure in a language is in the words and we want to learn correlations amongst the words but since the model doesn't get the words as a unit, it will have to _learn what/where a is_ before it can learn its correlation with other sequences; which effecitely means that we made the learning problem harder and more non-linear     
    This, also, allows the model to capture subword structure and morphology: e.g. "disunited" <-> "disinherited" <-> "disinterested".  
    Character LMs __lag__ behind word-based models in perplexity, but are clearly the future of language modeling.  

13. **Conditional Language Models:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents113}  
    A __Conditional LM__ assigns probabilities to sequences of words given some conditioning context $$x$$. It models "What is the probability of the next word, given the history of previously generated words AND conditioning context $$x$$?".  
    The probability, decomposed w/ chain rule:  
    <p>$$p(\boldsymbol{w} | \boldsymbol{x})=\prod_{t=1}^{\ell} p\left(w_{t} | \boldsymbol{x}, w_{1}, w_{2}, \ldots, w_{t-1}\right)$$</p>  
    * <button>Applications</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        ![img](/main_files/dl/nlp/rnn/9.png){: width="80%" hidden=""}   


[^1]: the problem of assigning a probability to a string and text compression is exactly the same problem so if you have a good language model you also have a good text compression algorithm and both we think of it in terms of the number of bits we can compress our sequence into.  


***

## Recurrent Neural Networks
{: #content2}

1. **Recurrent Neural Networks:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyCoxqntents21}  
    :   An __RNN__ is a class of artificial neural network where connections between units form a directed cycle, allowing it to exhibit dynamic temporal behavior.
    :   The standard RNN is a nonlinear dynamical system that maps sequences to sequences.  

2. **The Structure of an RNN:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}  
    :   The RNN is parameterized with three weight matrices and three bias vectors:  
    :   $$ \theta = [W_{hx}, W_{hh}, W_{oh}, b_h, b_o, h_0] $$
    :   These parameter completely describe the RNN.  

3. **The Algorithm:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}  
    :   Given an _input sequence_ $$\hat{x} = [x_1, \ldots, x_T]$$, the RNN computes a sequence of hidden states $$h_1^T$$ and a sequence of outputs $$y_1^T$$ in the following way:  
        __for__ $$t$$ __in__ $$[1, ..., T]$$ __do__  
            $$\:\:\:\:\:\:\:$$  $$u_t \leftarrow W_{hx}x_t + W_{hh}h_{t-1} + b_h$$  
            $$\:\:\:\:\:\:\:$$  $$h_t \leftarrow g_h(u_t)$$  
            $$\:\:\:\:\:\:\:$$  $$o_t \leftarrow W_{oh}h_{t} + b_o$$  
            $$\:\:\:\:\:\:\:$$  $$y_t \leftarrow g_y(o_t)$$   

4. **The Loss:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}  
    :   The loss of an RNN is commonly a sum of per-time losses:  
    :   $$L(y, z) = \sum_{t=1}^TL(y_t, z_t)$$
    :   * __Language Modelling__: 
            We use the *__Cross Entropy__* Loss function but predicting _words_ instead of classes
    :   $$ J^{(t)}(\theta) = - \sum_{j=1}^{\vert V \vert} y_{t, j} \log \hat{y_{t, j}}$$
    :   $$\implies$$
    :   $$L(y,z) = J = -\dfrac{1}{T} \sum_{t=1}^{T} \sum_{j=1}^{\vert V \vert} y_{t, j} \log \hat{y_{t, j}}$$
    :   To __Evaluate__ the model, we use *__Preplexity__* : 
    :   $$ 2^J$$
    :   > Lower Preplexity is _better_

5. **Analyzing the Gradient:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}  
    :   Assuming the following formulation of an __RNN__:  
    :   $$h_t = Wf(h_{t-1}) + W^{(hx)}x_{[t]} \\
        \hat{y_t} = W^{(S)}f(h_t)$$
    :   * The __Total Error__ is the sum of each error at each time step $$t$$:  
    :   $$ \dfrac{\partial E}{\partial W} = \sum_{t=1}^{T} \dfrac{\partial E_t}{\partial W}$$
    :   * The __local Error__ at a time step $$t$$:  
    :   $$\dfrac{\partial E_t}{\partial W} = \sum_{k=1}^{t} \dfrac{\partial E_t}{\partial y_t} \dfrac{\partial y_t}{\partial h_t} \dfrac{\partial h_t}{\partial h_k} \dfrac{\partial h_k}{\partial W}$$
    :   * To compute the _local derivative_ we need to compute:  
    :   $$\dfrac{\partial h_t}{\partial h_k}$$
    :   
    :   $$\begin{align}
        \dfrac{\partial h_t}{\partial h_k} &= \prod_{j=k+1}^t \dfrac{\partial h_j}{\partial h_{j-1}} \\
        &= \prod_{j=k+1}^t J_{j, j-1}
        \end{align}$$
    :   $$\:\:\:\:\:\:\:\:$$ where each $$J_{j, j-1}$$ is the __jacobina matrix__ of the partial derivatives of each respective  
        $$\:\:\:\:\:\:\:\:$$ hidden layer.

9. **The Vanishing Gradient Problem:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents29}  
    :   * __Analyzing the Norms of the Jacobians__ of each partial:  
    :   $$\| \dfrac{\partial h_j}{\partial h_{j-1}} \| \leq \| W^T \| \cdot \| \text{ diag}[f'(h_{j-1})] \| \leq \beta_W \beta_h$$
    :   $$\:\:\:\:\:\:\:$$ where we defined the $$\beta$$s as _upper bounds_ of the _norms_.        
    :   * __The Gradient is the product of these Jacobian Matrices__ (each associated with a step in the forward computation):  
    :   $$ \| \dfrac{\partial h_t}{\partial h_k} \| = \| \prod_{j=k+1}^t \dfrac{\partial h_j}{\partial h_{j-1}} \| \leq (\beta_W \beta_h)^{t-k}$$
    :   * *__Conclusion__*:  
            Now, as the exponential $$(t-k) \rightarrow \infty$$:  
            * __If $$(\beta_W \beta_h) < 1$$__:   
                $$(\beta_W \beta_h)^{t-k} \rightarrow 0$$.  
                known as __Vanishing Gradient__. 
            * __If $$(\beta_W \beta_h) > 1$$__:  
                $$(\beta_W \beta_h)^{t-k} \rightarrow \infty$$.  
                known as __Exploding Gradient__. 
    :   As the bound can become __very small__ or __very large__ quickly, the _locality assumption of gradient descent_ breaks down.

    <br>

6. **BPTT:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents26}  
    __for__ $$t$$ __from__ $$T$$ __to__ $$1$$ __do__  
        <!-- $$\ \ \ \ \ \ \ \ \ \ $$ $$dy_t \leftarrow g_y'(o_t) · dy_t$$   -->
    $$\begin{align}
    \ \ \ \ \ \ \ \ \ \ do_t &\leftarrow dy_t · g_y'(o_t) \\
    \ \ \ \ \ \ \ \ \ \ db_o &\leftarrow db_o + do_t \\
    \ \ \ \ \ \ \ \ \ \ dW_{oh} &\leftarrow dW_{oh} + do_th_t^T \\
    \ \ \ \ \ \ \ \ \ \ dh_t &\leftarrow dh_t + W_{oh}^T do_t \\
    \ \ \ \ \ \ \ \ \ \ du_t &\leftarrow dh_t · g_h'(u_t) \\
    \ \ \ \ \ \ \ \ \ \ dW_{hx} &\leftarrow dW_{hx} + du_tx_t^T \\
    \ \ \ \ \ \ \ \ \ \ db_h &\leftarrow db_h + du_t \\
    \ \ \ \ \ \ \ \ \ \ dW_{hh} &\leftarrow dW_{hh} + du_th_{t-1}^T \\
    \ \ \ \ \ \ \ \ \ \ dh_{t-1} &\leftarrow W_{hh}^T du_t 
    \end{align}
    $$  
    __Return__ $$\:\:\:\: d\theta = [dW_{hx}, dW_{hh}, dW_{oh}, db_h, db_o, dh_0]$$  

    <br>
    __Expanded:__   
    $$\begin{align}
        L(y, \hat{y}) &= \sum_{t} L^{(t)} = -\sum_{t} \log \hat{y}_ t = -\sum_{t} \log p_{\text {model }}\left(y^{(t)} |\left\{\boldsymbol{x}^{(1)}, \ldots, \boldsymbol{x}^{(t)}\right\}\right) \\
        \hat{y}_ t &= \text{softmax}(o_t) \\
        dy_{\tau} &= \frac{\partial L}{\partial L^{(t)}}=1 \\
        do_t &= g_y'(o_t) = \text{softmax}'(o_t) = \hat{y}_{i}^{(t)}-\mathbf{1}_{i=y^{(t)}} \\
        dh_{\tau} &= W_{oh}^T do_t \\
        dh_t &= \left(\frac{\partial \boldsymbol{h}^{(t+1)}}{\partial \boldsymbol{h}^{(t)}}\right)^{\top}\left(\nabla_{\boldsymbol{h}^{(t+1)}} L\right)+\left(\frac{\partial \boldsymbol{o}^{(t)}}{\partial \boldsymbol{h}^{(t)}}\right)^{\top}\left(\nabla_{\boldsymbol{o}^{(t)}} L\right) = \boldsymbol{W_{hh}}^{\top} \operatorname{diag}\left(1-\left(\boldsymbol{h}^{(t+1)}\right)^{2}\right)\left(\nabla_{\boldsymbol{h}^{(t+1)}} L\right)+\boldsymbol{W_{oh}}^{\top}\left(\nabla_{\boldsymbol{o}^{(t)}} L\right) \\
        du_t &= dh_t · g_h'(u_t) = dh_t · \operatorname{tanh}'(u_t) = dh_t · \sum_{t} \operatorname{diag}\left(1-\left(h^{(t)}\right)^{2}\right) \\
        db_o &= do_t \\
        dW_{oh} &= do_th_t^T \\
        dW_{hx} &= du_tx_t^T \\
        db_h &= du_t \\
        dW_{hh} &= du_th_{t-1}^T \\
        dh_{t-1} &= W_{hh}^T du_t
    \end{align}
    $$  

    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * $$dh_{\tau}$$: We need to get the gradient of $$h$$ at the last node/time-step $$\tau$$ i.e. $$h_{\tau}$$  
    * $$dh_t$$: We can then iterate backward in time to back-propagate gradients through time, from $$t=\tau-1$$ down to $$t=1$$, noting that $$h^{(t)}(\text { for } t<\tau)$$ has as <span>__descendants__</span>{: style="color: goldenrod"} both $$\boldsymbol{o}^{(t)}$$ and $$\boldsymbol{h}^{(t+1)}$$.  
        <button>From Graph</button>{: .showText value="show" onclick="showTextPopHide(event);"}
          ![img](/main_files/dl/archits/rnns/9.png){: width="30%" hidden=""}  





7. **Backpropagation Through Time:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents27}  
    * We can think of the recurrent net as a layered, feed-forward net with shared weights and then train the feed-forward net with (linear) weight constraints.
    * We can also think of this training algorithm in the time domain:
        * The forward pass builds up a stack of the activities of all the units at each time step
        * The backward pass peels activities off the stack to compute the error derivatives at each time step
        * After the backward pass we add together the derivatives at all the different times for each weight.  

    __Complexity:__  
    *__Linear__* in the length of the longest sequence.  
    _Minibatching_ can be inefficient as the sequences in a batch may have different lengths.  
    > Can be alleviated w/ __padding__.  

8. **Truncated BPTT:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents28}  
    Same as BPTT, but tries to avoid the problem of long sequences as inputs. It does that by _"breaking"_ the gradient flow every nth time-step (if input is article, then n could be average length of a sentence), thus, avoiding problems of __(1) Memory__ __(2) Exploding Gradient__.  

    __Downsides:__  
    If there are _dependencies_ between the segments where BPTT was truncated they will __not be learned__ because the _gradient doesn't flow back to teach the hidden representation about what information was useful_.  

    __Complexity:__  
    *__Constant__* in the truncation length $$T$$.  
    _Minibatching_ is efficient as all sequences have length $$T$$.  

    __Notes:__  
    * In TBPTT, we __Forward Propagate__ through-the-break/between-segments normally (through the entire comp-graph). Only the back-propagation is truncated.  
    * __Mini-batching__ on a GPU is an effective way of speeding up big matrix vector products [^2]. RNNLMs have two such products that dominate their computation: the _recurrent matrix_ $$V$$ and the _softmax matrix_ $$W$$.  



[^2]: By making them Matrix-Matrix products instead.  


__LSTMS:__  
* The core of the history/memory is captured in the _cell-state $$c_{n}$$_ instead of the hidden state $$h_{n}$$.  
* (&) __Key Idea:__ The update to the cell-state $$c_{n}=c_{n-1}+\operatorname{tanh}\left(V\left[w_{n-1} ; h_{n-1}\right]+b_{c}\right)$$  here are __additive__. (differentiating a sum gives the identity) Making the gradient flow nicely through the sum. As opposed to the multiplicative updates to $$h_n$$ in vanilla RNNs.  
    > There is non-linear funcs applied to the history/context cell-state. It is composed of linear functions. Thus, avoids gradient shrinking.  

* In the recurrency of the LSTM the activation function is the identity function with a derivative of 1.0. So, the backpropagated gradient neither vanishes or explodes when passing through, but remains constant.
* By the selective read, write and forget mechanism (using the gating architecture) of LSTM, there exist at least one path, through which gradient can flow effectively from $$L$$  to $$\theta$$. Hence no vanishing gradient.   
* However, one must remember that, this is not the case for exploding gradient. It can be proved that, there __can exist__ at-least one path, thorough which gradient can explode.  
* LSTM decouples cell state (typically denoted by c) and hidden layer/output (typically denoted by h), and only do additive updates to c, which makes memories in c more stable. Thus the gradient flows through c is kept and hard to vanish (therefore the overall gradient is hard to vanish). However, other paths may cause gradient explosion.  
* The Vanishing gradient solution for LSTM is known as _Constant Error Carousel_.  
* [**Why can RNNs with LSTM units also suffer from “exploding gradients”?**](https://stats.stackexchange.com/questions/320919/why-can-rnns-with-lstm-units-also-suffer-from-exploding-gradients/339129#339129){: value="show" onclick="iframePopA(event)"}
<a href="https://stats.stackexchange.com/questions/320919/why-can-rnns-with-lstm-units-also-suffer-from-exploding-gradients/339129#339129"></a>
    <div markdown="1"> </div>    
* [Lecture on gradient flow paths through gates](https://www.cse.iitm.ac.in/~miteshk/CS7015/Slides/Teaching/pdf/Lecture15.pdf)  

* [**LSTMs (Lec Oxford)**](https://www.youtube.com/embed/eDUaRvMDs-s?start=775){: value="show" onclick="iframePopA(event)"}
<a href="https://www.youtube.com/embed/eDUaRvMDs-s?start=776"></a>
    <div markdown="1"> </div>    


__Important Links:__  
[The unreasonable effectiveness of Character-level Language Models](https://nbviewer.jupyter.org/gist/yoavg/d76121dfde2618422139)  
[character-level language model with a Vanilla Recurrent Neural Network, in Python/numpy](https://gist.github.com/karpathy/d4dee566867f8291f086)  
[Visualizing and Understanding Recurrent Networks - Karpathy Lec](https://skillsmatter.com/skillscasts/6611-visualizing-and-understanding-recurrent-networks)  
[Cool LSTM Diagrams - blog](https://medium.com/mlreview/understanding-lstm-and-its-diagrams-37e2f46f1714)  
[Illustrated Guide to Recurrent Neural Networks: Understanding the Intuition](https://www.youtube.com/watch?v=LHXXI4-IEns)  
[Code LSTM in Python](https://iamtrask.github.io/2015/11/15/anyone-can-code-lstm/)  
[Mikolov Thesis: STATISTICAL LANGUAGE MODELS BASED ON NEURAL NETWORKS](http://www.fit.vutbr.cz/~imikolov/rnnlm/thesis.pdf)  


***

## RNNs Extra!
{: #content3}


5. **Vanishing/Exploding Gradients:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents35}  
    :   * __Exploding Gradients__:  
            * Truncated BPTT 
            * Clip gradients at threshold 
            * RMSprop to adjust learning rate 
        * __Vanishing Gradient__:   
            * Harder to detect 
            * Weight initialization 
            * ReLu activation functions 
            * RMSprop 
            * LSTM, GRUs 

1. **Applications:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}  
    :   * __NER__  
        * __Entity Level Sentiment in context__  
        * __Opinionated Expressions__

2. **Bidirectional RNNs:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}  
    :   * __Motivation__:  
            For _classification_ we need to incorporate information from words both preceding and following the word being processed
    :   ![img](/main_files/dl/nlp/rnn/1.png){: width="100%"}  
    :   $$\:\:\:\:$$ Here $$h = [\overrightarrow{h};\overleftarrow{h}]$$ represents (summarizes) the _past_ and the _future_ around a single token.
    :   * __Deep Bidirectional RNNs__:  
    :   ![img](/main_files/dl/nlp/rnn/2.png){: width="100%"}  
    :   $$\:\:\:\:\:$$ Each memory layer passes an _intermediate sequential representation_ to the next.

3. **Math to Code:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}  
    :   The Parameters: $$\{W_{hx}, W_{hh}, W_{oh} ; b_h, b_o, h_o\}$$   
    :   $$\begin{align}
        h_t &= \phi(W_{hx}x_t + W_{hh}h_{t-1} + b_h) \\
        h_t &= \phi(\begin{bmatrix}
    W_{hx} & ; & W_{hh}
\end{bmatrix}   
        \begin{bmatrix} x_t  \\ ;   \\ h_{t-1} \end{bmatrix} + b_h)
        \end{align}
        $$ 
    :   $$y_t = \phi'(W_{oh}h_t + b_o)$$ 

4. **Initial States:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents34}  
    :   ![img](/main_files/dl/nlp/rnn/3.png){: width="76%"}  

6. **Specifying the Initial States:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents36}  
    :   ![img](/main_files/dl/nlp/rnn/4.png){: width="76%"}  

7. **Teaching Signals:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents37}  
    :   ![img](/main_files/dl/nlp/rnn/5.png){: width="76%"}  


5. **Vanishing/Exploding Gradients:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents35}  
    :   * __Exploding Gradients__:  
            * Truncated BPTT 
            * Clip gradients at threshold 
            * RMSprop to adjust learning rate 
        * __Vanishing Gradient__:   
            * Harder to detect 
            * Weight initialization 
            * ReLu activation functions 
            * RMSprop 
            * LSTM, GRUs 

9. **Rectifying the Vanishing/Exploding Gradient Problem:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents39}  
    :   ![img](/main_files/dl/nlp/rnn/7.png){: width="76%"}  

8. **Linearity of BackProp:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents38}  
    :   ![img](/main_files/dl/nlp/rnn/6.png){: width="76%"}  
    :   The derivative update are also __Correlated__ which is bad for SGD.  