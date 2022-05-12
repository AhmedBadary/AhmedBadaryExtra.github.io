---
layout: NotesPage
title: Contextual Word Representations and Pretraining
permalink: /work_files/research/dl/nlp/ctxt_word_repr
prevLink: /work_files/research/dl/nlp.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Word Representations and their progress](#content1)
  {: .TOC1}
  * [Transformers](#content2)
  {: .TOC2}
<!--   * [THIRD](#content3)
  {: .TOC3} -->
</div>

***
***

* [Paper on Contextual Word Representations](https://arxiv.org/pdf/1902.06006.pdf)  
* [The Transformer Family (Blog)](https://lilianweng.github.io/lil-log/2020/04/07/the-transformer-family.html)  


## Word Representations and their progress
{: #content1}


__Summary of Progress:__{: style="color: red"}  
{: #lst-p}
* __2011-13s__: Learning Unsupervised Representations for words (Pre-Trained Word Vectors) is crucial for making Supervised Learning work (e.g. for NERs, POS-Tagging, etc.)  
* __2014-18s__: Pre-Trained Word Vectors are not actually necessary for _good performance_ of supervised methods.  
    * The reason is due to advances in training supervised methods: __regularization__, __non-linearities__, etc.  
    * They can boost the performance by ~ $$1\%$$ on average.   
<br>


1. **Word Representations (Accepted Methods):**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    The current accepted methods provide one representation of words:  
    1. __Word2Vec__
    2. __GloVe__ 
    3. __FastText__  

    <button>Early Day Results</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](/main_files/dl/nlp/ctxt_word_repr/2.png){: width="80%" hidden=""}  

    __Problems:__  
    {: #lst-p}
    * __Word Senses__: Always the same representation for a __word type__ regardless of the context in which a __word token__ occurs  
        * We might want very fine-grained word sense disambiguation (e.g. not just 'holywood star' and 'astronomical star'; but also 'rock star', 'star student' etc.)  

    * We just have __one representation__ for a word, but words have __different aspects__: including __semantics__, __syntactic behavior__, and __register/connotations__ (e.g. when is it appropriate to use 'bathroom' vs 'shithole' etc.; 'can'-noun vs 'can'-verb have same vector)  

    __Possible Solution (that we always had?):__  
    {: #lst-p}
    * In a NLM, LSTM layers are trained to predict the next word, producing hidden/state vectors, that are basically __context-specific__ word representations, at each position  
        <button>LSTM Representations</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        ![img](https://cdn.mathpix.com/snip/images/wWkGdRomPB3JlxbnRWCNrAX8nfHerQyAymnxmTU6--Q.original.fullsize.png){: width="100%" hidden=""}  
    <br>  

2. **TagLM (Peters et al. 2017) — Pre-Elmo:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    __Idea:__  
    {: #lst-p}
    * Want meaning of word in context, but standardly learn task RNN only on small task-labeled data (e.g. NER).  
    * Do __semi-supervised__ approach where we train NLM on large unlabeled corpus, rather than just word vectors.  
    * Run a BiRNN-LM and concatenate the For and Back representations
    * Also, train a traditional word-embedding (w2v) on the word and concatenate with Bi-LM repr.
    * Also, train a Char-CNN/RNN to get character level embedding and concatenate all of them together

    __Details:__  
    {: #lst-p}
    * Language model is trained on 800 million training words of "Billion word benchmark"  
    * __Language model observations__:  
        * An LM trained on supervised data does not help 
        * Having a bidirectional LM helps over only forward, by about 0.2 
        * Having a huge LM design (ppl 30) helps over a smaller model (ppl 48) by about 0.3 
    * __Task-specific BiLSTM observations__:  
        * Using just the LM embeddings to predict isn't great: 88.17 F1  
            * Well below just using an BiLSTM tagger on labeled data      

    <button>Tag LM Detailed</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](/main_files/dl/nlp/ctxt_word_repr/3.png){: width="100%" hidden=""}  
    <button>TagLM step-by-step Overview</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/LZid2lHBZj9P1EQAOhHzDYxk6o_I0kh-gtfIBDbI6Rg.original.fullsize.png){: width="100%" hidden=""}  
    <br>

3. **Cove - Pre-Elmo:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    * Also has idea of using a trained sequence model to provide context to other NLP models 
    * Idea: Machine translation is meant to preserve meaning, so maybe that's a good objective? 
    * Use a 2-layer bi-LSTM that is the encoder of seq2seq + attention NMT system as the context provider 
    * The resulting CoVe vectors do outperform GloVe vectors on various tasks 
    * But, the results aren't as strong as the simpler NLM training described in the rest of these slides so seems abandoned 
        * Maybe NMT is just harder than language modeling? 
        * Maybe someday this idea will return?

    <br>

4. **Elmo - Embeddings from Language Models (Peters et al. 2018):**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    __Idea:__  
    {: #lst-p}
    * Train a bidirectional LM  
    * Aim at performant but not overly large LM:  
        * Use 2 biLSTM layers  
        * Use character CNN to build initial word representation (only)  
            * 2048 char n-gram filters and 2 highway layers, 512 dim projection  
        * Use 4096 dim hidden/cell LSTM states with 512 dim projections to next input  
        * Use a residual connection  
        * Tie parameters of token input and output (softmax) and tie these between forward and backward LMs  

    __Key Results:__  
    {: #lst-p}
    * ELMo learns task-specific combination of BiLM representations  
    * This is an innovation that improves on just using top layer of LSTM stack
    <p>$$\begin{aligned} R_{k} &=\left\{\mathbf{x}_{k}^{L M}, \overrightarrow{\mathbf{h}}_{k, j}^{L M}, \mathbf{h}_{k, j}^{L M} | j=1, \ldots, L\right\} \\ &=\left\{\mathbf{h}_{k, j}^{L M} | j=0, \ldots, L\right\} \end{aligned}$$</p>  
    <p>$$\mathbf{E} \mathbf{L} \mathbf{M} \mathbf{o}_{k}^{t a s k}=E\left(R_{k} ; \Theta^{t a s k}\right)=\gamma^{task} \sum_{j=0}^{L} s_{j}^{task} \mathbf{h}_ {k, j}^{L M}$$</p>  
    * $$\gamma^{\text { task }}$$ scales overall usefulness of ELMo to task;  
    * $$s^{\text { task }}$$ are softmax-normalized mixture model weights  
    > Possibly this is a way of saying different semantic and syntactic meanings of a word are represented in different layers; and by doing a weighted average of those, in a task-specific manner, we can leverage the appropriate kind of information for each task.  

    __Using ELMo with a Task:__  
    {: #lst-p}
    * First run biLM to get representations for each word
    * Then let (whatever) end-task model use them
        * Freeze weights of ELMo for purposes of supervised model
        * Concatenate ELMo weights into task-specific model
            * Details depend on task
                * Concatenating into intermediate layer as for TagLM is typical
                * Can provide ELMo representations again when producing outputs, as in a question answering system  

    
    __Weighting of Layers:__  
    {: #lst-p}
    * The two Bi-LSTM NLP Layers have differentiated uses/meanings  
        * Lower layer is better for lower-level syntax, etc.  
            * POS-Tagging, Syntactic Dependencies, NER  
        * Higher layer is better for higher-level semantics  
            * Sentiment, Semantic role labeling, QA, SNLI  


    __Reason for Excitement:__  
    ELMo proved to be great for __all NLP tasks__ (even tho the core of the idea was in _TagLM_)   
    * <button>ELMo Results</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        ![img](/main_files/dl/nlp/ctxt_word_repr/5.png){: width="70%" hidden=""}  
    <br>        
    
5. **ULMfit - Universal Language Model Fine-Tuning (Howard and Ruder 2018):**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  
    ULMfit - Universal Language Model Fine-Tuning for Text Classification:  
    ![img](/main_files/dl/nlp/ctxt_word_repr/4.png){: width="90%"}  


6. **BERT (Devlin et al. 2018):**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}  
    BERT - Bidirectional Encoder Representations from Transformers:  
    __Idea:__ Pre-training of Deep Bidirectional Transformers for Language Understanding.  

    __Model Architecture:__  
    {: #lst-p}
    * Transformer Encoder
    * Self-attention --> no locality bias
        * Long-distance context has "equal opportunity"  
    * Single multiplication per layer --> efficiency on GPU/TPU
    * __Architectures__:  
        * __BERT-Base__: 12 layer, 768-hidden, 12-head  
        * __BERT-Large__: 24 layer, 1024 hudden, 16 heads  


    __Model Training:__  
    {: #lst-p}
    * Train on Wikipedia + BookCorpus
    * Train 2 model sizes:  
        * __BERT-Base__
        * __BERT-Large__
    * Trained on $$4\times 4$$  or $$8\times 8$$ TPU slice for 4 days  


    __Model Fine-Tuning:__  
    {: #lst-p}
    * Simply learn a classifier built on top layer for each task that you fine-tune for.
                

    __Problem with Unidirectional and Bidirectional LMs:__  
    {: #lst-p}
    * __Uni:__ build representation incrementally; not enough context from the sentence  
    * __Bi:__  Cross-Talk; words can "see themselves"  

    __Solution:__  
    {: #lst-p}
    * Mask out $$k\%$$ of the input words, and then predict the masked words
        * They always use $$k=15%$$  
        > Ex: "The man went to the _[MASK]_ to buy a _[MASK]_ of milk."  

        * __Too little Masking__:  Too Expensive to train
        * __Too much Masking__:  Not enough context   
    * __Other Benefits__:  
        * In ELMo, bidirectional training is done independently for each direction and then concatenated. No joint-context in the model during the building of contextual-reprs.
        * In GPT, there is only unidirectional context.  
            
    __Another Objective - Next Sentence Prediction:__  
    To learn _relationships_ between sentences, predict whether sentence B is actual sentence that proceeeds sentence A, or a random sentence (for QA, NLU, etc.).  


    __Results:__  
    Beats every other architecture in every __GLUE__ task (NL-Inference).  

    * [BERT Word Embeddings Tutorial](http://mccormickml.com/2019/05/14/BERT-word-embeddings-tutorial/)  


__Notes:__{: style="color: red"}  
{: #lst-p}
* __Tips for unknown words with word vectors:__  
    * Simplest and common solution:
    * Train time: Vocab is $$\{\text { words occurring, say, } \geq 5 \text { times }\} \cup\{<UNK>\}$$  
    * Map __all__ rarer $$(<5)$$ words to $$<UNK>$$, train a word vector for it
    * Runtime: use $$<UNK>$$ when out-of-vocabulary (OOV) words occur

    * __Problems:__  
        * No way to distinguish different $$UNK$$ words, either for identity or meaning  
    * __Solutions:__  
        1. Hey, we just learned about char-level models to build vectors! Let's do that!  
            * Especially in applications like question answering  
                * Where it is important to match on word identity, even for words outside your word vector vocabulary  
        2. Try these tips (from Dhingra, Liu, Salakhutdinov, Cohen 2017)  
            a. If the <UNK> word at test time appears in your unsupervised word embeddings, use that vector as is at test time.
            b. Additionally, for other words, just assign them a random vector, adding them to your vocabulary
            
            a. definitely helps a lot; b. may help a little more  
        3. Another thing you can try:  
            * Collapsing things to word classes (like unknown number, capitalized thing, etc. and having an <UNK-class> for each  
    

<!-- 7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18}
 -->

***

## The Transformer
{: #content2}


1. **Self-Attention:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    __Computational Complexity Comparison__:  
    ![img](/main_files/dl/nlp/ctxt_word_repr/1.png){: width="70%"}  
    It is favorable when the __sequence-length__ $$<<$$ __dimension-representations__.  

    __Self-Attention/Relative-Attention Interpretations__:  
    {: #lst-p}
    * Can achieve __Translational Equivariance__ (like convs) (by removing pos-encoding).
    * Can model __similarity graphs__.  
    * Connected to __message-passing NNs__: Can think of self-attention as _passing messages between pairs of nodes in graph_; equivalently, _imposing a complete bipartite graph_ and you're passing messages between nodes.  
        Mathematically, the difference is message-passing NNs impose condition that messages pass ONLY bet pairs of nodes; while self-attention uses softmax and thus passes messages between all nodes.  

    __Self-Attention Summary/Properties__:  
    {: #lst-p}
    * <span>__Constant__ path-length</span>{: style="color: purple"} between any two positions  
    * Unbounded memory (i.e no fixed size h-state)  
    * Gating/multiplicative interactions  
        Because you multiply attention probabilities w/ activations. PixelCNN needed those interactions too.  
    * Trivial to parallelize (per layer): just matmuls  
    * Models __self-similarity__    
    * Relative attention provides __expressive timing__, __equivariance__, and extends naturally to graphs  
    * (Without __positional encoding__) It's <span>Permutation-Invariant and Translation-Equivariant</span>{: style="color: purple"}  
        It can learn to __copy__ well.  


    __Current Issues__:  
    {: #lst-p}
    * __Slow Generation__:  
        Mainly due to __Auto-Regressive__ generation, which is necessary to break the multi-modality of generation. Multi-modality prohibits naive parallel generation.  
        Multi-modality refers to the fact that there are multiple different sentences in german that are considered a correct translation of a sentence in english, and they all depend on the word that was generated first (ie no parallelization).   
    * __Active Area of Research__:  
        <span>__Non Auto-Regressive Transformers__</span>{: style="color: purple"}.  
        * Papers:  
            * _Non autoregressive transformer (Gu and Bradbury et al., 2018)_  
            * _Deterministic Non-Autoregressive Neural Sequence Modeling by Iterative Refinement (Lee, Manismov, and Cho, 2018)_  
            * _Fast Decoding in Sequence Models Using Discrete Latent Variables (ICML 2018) Kaiser, Roy, Vaswani, Pamar, Bengio, Uszkoreit, Shazeer_  
            * _Towards a Better Understanding of Vector Quantized Autoencoders Roy, Vaswani, Parmar, Neelakantan, 2018_  
            * _Blockwise Parallel Decoding For Deep Autogressive Models (NeurIPS 2019) Stern, Shazeer, Uszkoreit_   

    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * __Self-Similarity:__  
        * Use Encoder-Self-Attention and replace word-embeddings with image-patches: you compute a notion of content-based similarity between the elements (patches), then - based on this content-based similarity - it computes a convex combination that brings the patches together.  
            * You can think about it as a <span>*__differentiable__* way to perform __non-local means__</span>{: style="color: purple"}.  
            * __Issue - Computational Problem:__  
                Attention is Cheap only if _length_ $$<<$$ _dim_.  
                Length for images is $$32\times 32\times 3 = 3072$$:   
                <button>Diagram</button>{: .showText value="show" onclick="showTextPopHide(event);"}
                ![img](https://cdn.mathpix.com/snip/images/zvEcczfCg3TLiJ76y0QohmJNP2V-OxYsYFCQTaHBy40.original.fullsize.png){: width="100%" hidden=""}  
            * __Solution - Combining Locality with Self-Attention__:  
                Restrict the attention windows to be local neighborhoods.  
                Good assumption for images because of spatial locality.  
    <br>

<!-- 2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}

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