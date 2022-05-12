---
layout: NotesPage
title: Machine Learning Research
permalink: /work_files/research/ml_research
prevLink: /work_files/research/
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Deep Learning Generalization](#content1)
  {: .TOC1}
  * [Papers](#content8)
  {: .TOC8}
  * [Observations, Ideas, Questions, etc.](#content9)
  {: .TOC9}
  <!-- * [THIRD](#content3)
  {: .TOC3} -->
  <!-- * [FOURTH](#content4)
  {: .TOC4} -->
  <!-- * [FIFTH](#content5)
  {: .TOC5} -->
  <!-- * [SECOND](#content2)
  {: .TOC2} -->
</div>

***
***

* [Deep Learning Lecture Notes and Experiments (github)](https://github.com/roatienza/Deep-Learning-Experiments)  



## Deep Learning Generalization
{: #content1}

* [A Practical Bayesian Framework for Backpropagation Networks](https://authors.library.caltech.edu/13793/1/MACnc92b.pdf)  
* [Everything that Works Works Because it's Bayesian: Why Deep Nets Generalize?](https://www.inference.vc/everything-that-works-works-because-its-bayesian-2/)  
* [Reconciling modern machine learning practice and the bias-variance trade-of (paper!)](https://arxiv.org/pdf/1812.11118.pdf)  


1. **Casting ML Algorithms as Bayesian Approximations:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    * __Classical ML__:  
        * L1 regularization is just MAP estimation with sparsity inducing priors  
        * SVMS, support vector machines, are just the wrong way to train Gaussian processes  
        * [Herding is just Bayesian quadrature done slightly wrong](https://arxiv.org/abs/1204.1664)  
    * __DL__:  
        * [LeCun Post on Uncertainty in Neural Networks](https://www.facebook.com/yann.lecun/posts/10154058859142143)  
        * Dropout is just variational inference done wrong: [Dropout as a Bayesian Approximation](https://arxiv.org/abs/1506.02142)  
        * 


    * Deep Nets memorize 
    <br>

2. **Why do Deep Nets Generalize?:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    One possibility is: "because they are really just an approximation to Bayesian machine learning." - Ferenc  

    * __SGD__:  
        SGD could be responsible for the good generalization capabilities of Deep Nets.  
        * SGD finds Flat Minima.  
            * A __Flat Minima__ is a minima where the Hessian - and consequently the inverse Fisher information matrix - has small eigenvalues.  
            * Flat might be better than sharp minima:  
                If you are in a flat minimum, there is a relatively large region of parameter space where many parameters are almost equivalent inasmuch as they result in almost equally low error. Therefore, given an error tolerance level, one can describe the parameters at the flat minimum with limited precision, using fewer bits while keeping the error within tolerance. In a sharp minimum, you have to describe the location of your minimum very precisely, otherwise your error may increase by a lot.  
        * [(Keskar et al, 2017)](https://arxiv.org/abs/1609.04836) show that deep nets generalize better with smaller batch-size when no other form of regularisation is used.  
            * And it may be because SGD biases learning towards flat minima, rather than sharp minima.  
        * [(Wilson et al, 2017)](https://arxiv.org/abs/1705.08292) show that these good generalization properties afforded by SGD diminish somewhat when using popular adaptive SGD methods such as Adam or rmsprop.  
        * Though, there is contradictory work by [(Dinh et al, (2017)](https://arxiv.org/abs/1703.04933) who claim sharp minima can generalize well, too.  
            Also, [(Zhang et al, 2017)](https://cbmm.mit.edu/sites/default/files/publications/CBMM-Memo-067.pdf)  
        * One conclusion is: The reason deep networks work so well (and generalize at all) is not just because they are some brilliant model, but because of the specific details of how we optimize them.  
            Stochastic gradient descent does more than just converge to a local optimum, it is biased to favor local optima with certain desirable properties, resulting in better generalization.  
        * Is SGD Bayesian?  
            * Some work: 
                * [Stochastic Gradient Descent as Approximate Bayesian Inference](https://arxiv.org/pdf/1704.04289.pdf)
            * Flat Minima is Bayesian:  
                It turns out, [(Hochreiter and Schmidhuber, 1997)](http://www.bioinf.jku.at/publications/older/3304.pdf) motivated their work on seeking flat minima from a Bayesian, minimum description length perspective.  
                Even before them, [(Hinton and van Camp, 1993)](http://www.cs.toronto.edu/~fritz/absps/colt93.pdf) presented the same argument in the context of Bayesian neural networks.


                

    <button>Abu-Mostafa on Neural Network Generalization</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
    <div hidden="" markdown="1">
    Indeed, the empirical evidence about generalization in deep neural networks with a huge number of weights is that they generalize better than the theory would predict. This is not just in terms of the loose bounds that the theory provides. The performance is better than even the "tight" rules of thumb that were based on the theory and worked in practice.

    This is not the first time this happens in ML. When boosting was the method of choice, generalization was better than it should be. Specifically, there was no overfitting in cases where the model complexity was going up and overfitting would be expected. In that case, a theoretical approach to explain the phenomenon based on a cost function other than 𝐸𝑖𝑛 [in-sample error] was advanced. It made sense but it didn't stand up to scrutiny, as minimizing that cost function directly (instead of letting it be minimized through the specific structure of the AdaBoost algorithm for instance) suffered from the usual overfitting. There was no conclusive verdict about how AdaBoost avoids overfitting. There were bits and pieces of intuition, but it is difficult to tell whether that was explanation or rationalization.

    In the case of neural networks, there have also been efforts to explain why the performance is better. There are other approaches to generalization, e.g., based on "stability" of learning, that were invoked. However, the theoretical work on stability was based on perturbation of the training set that does not lead to a significant change in the final hypothesis. The way stability is discussed in the results I have seen in neural networks is based on perturbation of the weights that does not lead to a significant change. It thus uses the concept of stability rather than the established theoretical results to explain why generalization is good. In fact, there are algorithms that deliberately look for a solution that has this type of stability as a way to get good generalization, a regularization of sorts.

    It is conceivable that the structure of deep neural networks, similar to the case of AdaBoost, tends to result in better generalization than the general theory would indicate. To establish that, we need to identify what is it about the structure that makes this happen. In comparison, if you study SVM as a model without getting into the notion of support vectors, you will encounter "inexplicable" good generalization. Once you know about how the number of support vectors affects generalization, the mystery is gone.

    Let me conclude by emphasizing that the VC theory is not violated in any of these instances, since the theory only provides an upper bound. Those cases show a much better performance for particular models, but the performance is still within the theoretical bound. What would be a breakthrough is another, better bound that is applicable to an important class of models. For example, the number of parameters in deep neural networks is far bigger than previous models. If better generalization bounds can be proven for models with huge number of parameters, for instance, that would be quite a coup.  
    </div>


    __Ways to Explain Generalization:__{: style="color: red"}  
    {: #lst-p}
    * The bigger (deeper) the network the easier it is to train (because the optimization landscape becomes simpler); so this + __early-stopping__ can lead to good solutions that wouldn't utilize the more funky functions we can represent with the bigger network.  
        Intuition:  
        * Optimizing/Searching over a huge function space (e.g. all possible functions), it is easier to _"steer"_ into the correct one, whereas if you're restricted and you can only have certain types of functions, then you need to find your path from one to the other which is generally harder to do.  
        * Another view of the same is that, if you have a really large network w/ random initialization (e.g. infinitely big) such that a subnetwork exists that solves the problem (i.e. what you are searching for), so if it's already present, backprop can choose the direction of the parameters leading to that subnetwork cuz that'll make the biggest improvement, and you will learn very quickly.  
        * On the other hand, having a huge number of parameters can lead many of the parameter settings to be equally good/leading to the same solution (since the NN is never unique), so finding any local minima yields a good solution.  
            Moreover, perhaps some of these local minimas are actually bad if they were to be optimized fully however, w/ __early-stopping__ you can stop at the configuration of the parameters that would yield a good result w/o overtraining into that local minima that would lead to overlearning.  
            While even when early-stopping in a small network, the parameters setting we learn is already at such a low/deep point in the local minima that it already "overlearned"? (or that most of these local minimas are not great)  




    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * "We can connect this finding to recent work examining the generalization of large neural networks. Zhang et al. (2017) observe that deep neural networks seemingly violate the common understanding of learning theory that large models with little regularization will not generalize well. The observed disconnect between NLL and 0/1 loss suggests that these high capacity models are not necessarily immune from overfitting, but rather, overfitting manifests in probabilistic error rather than classification error." - [On Calibration of Modern Neural Networks](https://arxiv.org/pdf/1706.04599.pdf)  
    * Another w
    <br>

<!-- 3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}
4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}
5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}
6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}
7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}
8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18}
 -->
 
***

## Misc.
{: #content2}

1. **NLP Research and What's Next:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    __Progress in NLP/AI:__{: style="color: red"}  
    {: #lst-p}
    * Machine learning with feature engineering:  
        Learning weights for engineered featured.   
    * Deep learning for feature learning:  
        Using DL to automatically learn features (e.g. embeddings).  
    * Deep architecture engineering for single tasks:  
        Each sub-field in NLP converged to a particular Network Architecture.  
    * <span>__(NOW)__</span>{: style="color: green"} __Deep Single MultiTask Model__  

    __Limits of Single-Task Learning:__{: style="color: red"}  
    {: #lst-p}
    * Great performance improvements in recent years given {dataset, task, model, metric}  
    * We can hill-climb to local optima as long as $$\vert \text{dataset} \vert > 1000 \times C$$  
    * For more general AI, we need continuous learning in a single model instead  
    * Models typically start from random or are only partly pre-trained  

    <span>There is no single blocking task in Natural Language.</span>{: style="color: purple"} (compared to Classification in Vision)  
    HOWEVER, <span>__MultiTask Learning__ is a _blocker_ for general NLP systems</span>{: style="color: goldenrod"}.  

    __Why has weight and model sharing not happened as much in NLP?:__{: style="color: red"}  
    {: #lst-p}
    * NLP requires <span>many types of __reasoning__</span>{: style="color: purple"}:  
        Logical, Linguistic, Emotional, Visual, etc.  
    * Requires <span>__Short__ and __Long__-term __Memory__</span>{: style="color: purple"}  
    * NLP had been divided into intermediate and separate tasks to make progress:  
        $$\rightarrow$$ Benchmark chasing in each community  
    * Can a single unsupervised task solve it all? No.  
        * Language clearly requires supervision in nature (kid in jungle -> easy to develop vision not language).  


    __How to express many NLP tasks in the same framework?:__{: style="color: red"}  
    {: #lst-p}
    * __NLP Frameworks:__{: style="color: DarkRed"}  
        * __Sequence Tagging__: named entity recognition, aspect specific sentiment  
        * __Text Classification__: dialogue state tracking, sentiment classification  
        * __Seq2seq__: machine translation, summarization, question answering   
    * __NLP SuperTasks:__{: style="color: DarkRed"}  
        __Hypothesis:__ The following are <span>Three Equivalent SuperTasks of NLP</span>{: style="color: purple"} where we can pose all possible NLP tasks as either one of them:  
        * __Language Modeling:__ condition on Question+Context, then generate    
        * __Question Answering:__ Question=Task  
        * __Dialogue__: open-ended, limited datasets  

        Thus, __Question Answering__ is the most appropriate SuperTask to choose to cast NLP problems in.  


    __The Natural Language Decathlon (decaNLP):__{: style="color: red"}  
    {: #lst-p}
    * __Multitask Learning as Question Answering:__{: style="color: DarkRed"}  
        Casts all NLP tasks as <span>Question Answering</span>{: style="color: purple"} problems.  
    * __decaNLP Tasks:__{: style="color: DarkRed"}  
        1. Question Answering
        1. Machine Translation
        1. Summarization
        1. Natural Language Inference
        1. Sentiment Classification
        1. Semantic Role Labeling
        1. Relation Extraction
        1. Dialogue
        1. Semantic Parsing
        1. Commonsense Reasoning
    * <button>Q/A Examples</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        ![img](https://cdn.mathpix.com/snip/images/dOTMhfoYBQNQ3s3vIF3dwh6HMhEqOg1F5ymAF39k1V4.original.fullsize.png){: width="100%" hidden=""}  
    * __Meta-Supervised Learning__: From $$\{x, y\}$$ to $$\{x, t, y\}$$ ($$t$$ is the task)  
    * Use a question, $$q$$, as a natural description of the task, $$t$$, to allow the model to use linguistic information to connect tasks  
    * $$y$$ is the answer to $$q$$ and $$x$$ is the context necessary to answer $$q$$  
    * __Model Specifications for decaNLP:__{: style="color: DarkRed"}   
        * No task-specific modules or parameters because we assume the task ID is not available  
        * Must be able to adjust internally to perform disparate tasks
        * Should leave open the possibility of zero-shot inference for unseen tasks  



<!-- 1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}
2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}
3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}
4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}
5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}
6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents26}
7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents27}
8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents28} -->

***

<!-- ## THIRD
{: #content3} -->

<!-- 1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}
2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}
3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}
4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents34}
5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents35}
6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents36}
7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents37}
8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents38} -->


***

## Papers
{: #content8}

1. **Fast Weights:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents81}  
    __Fast-Weights:__{: style="color: red"}  
    <button>Discussion/Analysis</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    * __FAST-WEIGHTS:__  
        * __Basic Idea:__  
            * on each connection: Total weight = Sum of:
                * __Standard Slow Weights__. This learns slowly & (may also) decay slowly. Holds long term Knowledge.
                * __The Fast Weights__: Learns quickly, decays quickly, Holds Temp. info.

        * __Motivation:__  
            * __Priming:__ listen to a word $$\rightarrow$$ recognize many minutes later in Noisy Env.
                * If we had __localist Representation__ could just temporarily lower the threshold of the "cucumber" weight
                * If we use __point Attractors__ instead of "localist units" we con temporarily increase the "attractiveness" of the words unit (by changing the weights between the neurons in that pattern of activity)

        * __Weight Matrices VS Activity Vectors:__  
            Weight Matrices are better:  
            (1) More capacity $$N^2$$ vs $$N$$ (2) A fast weight matrix of $$1000 x 1000$$ can easily make 100 attractors more "attractive"  

        * __Three ways to store Temp. knowledge:__  
            * __LSTM__, Stores it in its activity vectors [hidden weights] $$\implies$$ Irrelevant temp Memory __interferes__ with on-going process  
            * __An additional External memory to LSTM__, can store without interference but need to - learn when to read/white.  
            * __Fast-Weights:__ Allow the temporal Knowledge to be stored without having any extra neurons.  
                They just make some attractors easier to fall into; and they also "flavor" the attractor by slightly changing the activity vector you end up with.  
    {: hidden=""}
    <br>

<!-- 2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents82} 
3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents83} 
4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents84} 
5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents85} 
6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents86} 
7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents87} 
8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents88}  
 -->

***

## Observations, Ideas, Questions, etc.
{: #content9}

1. **Observations from Papers/Blogs/etc.:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents91}  
    * deep neural networks seemingly violate the common understanding of learning theory that large models with little regularization will not generalize well. The observed disconnect between NLL and 0/1 loss suggests that these high capacity models are not necessarily immune from overfitting, but rather, overfitting manifests in probabilistic error rather than classification error. [paper](https://arxiv.org/pdf/1706.04599.pdf)  
    * It is also interesting to see that the global average pooling operation can significantly increase the classification accuracy for both CNNs and CNTKs. From this observation, we suspect that <span>many techniques that improve the performance of neural networks are in some sense __universal__</span>{: style="color: purple"}, i.e., these techniques might benefit kernel methods as well [lnk](http://www.offconvex.org/2019/10/03/NTK/).  
    * [__Is Optimization a Sufficient Language for Understanding Deep Learning?__](http://www.offconvex.org/2019/06/03/trajectories/)  
        * __Conventional View (CV) of Optimization__:  
            Find a solution of minimum possible value of the objective, as fast as possible.  
        * If our goal is mathematical understanding of deep learning, then the CV of Opt is potentially __insufficient__.  
    * Representable Does Not Imply Learnable.  
    * [__Recurrent Models in-practice can be approximated with FeedForward Models__](http://www.offconvex.org/2018/07/27/approximating-recurrent/):  
        FF models seem to match or exceed the performance of Recurrent models on almost all tasks.  
        Suggesting that Recurrent models extra expressiveness might not be needed/used.  
        The following is conjectured: <span>"Recurrent models trained in practice are effectively feed-forward"</span>{: style="color: purple"}.   
        * [This paper (Stable Recurrent Models)](https://arxiv.org/pdf/1805.10369.pdf) proves that stable recurrent neural networks are well approximated by feed-forward networks for the purpose of both inference and training by gradient descent.  
    * The unlimited context offered by recurrent models is not strictly necessary for language modeling.  
        i.e. it’s possible you don’t need a large amount of context to do well on the prediction task on average. [Recent theoretical work](https://arxiv.org/abs/1612.02526) offers some evidence in favor of this view.  

    <br>

2. **Ideas:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents92}  
    __Project Ideas:__{: style="color: red"}  
    {: #lst-p}
    * __NMF__ on Text Data  
    * read old Schmidhuber/Hinton Papers and reapply them on current hardware/datasets  
    * word-embeddings and topic-modeling and NMF, on ARXIV ML Papers 
    * Generative Adversarial Framework for Speech Recognition  




    __Research Ideas:__{: style="color: red"}  
    {: #lst-p}
    * Overfitting on NLL to explain Deep-NN generalization
    * DeepSets and Attention theoretical guarantees
    * Experimenting w/ Mutual Info (IB) w/ knowledge distillation
    * Language Modeling Decoding using __Attention__ (main problem is beam size = greedy)  
    * Experiment with Lots of data w/ simpler models VS Less data w/ advanced models  
        ("A dumb algorithm with lots and lots of data beats a clever one with modest amounts of it.")  
    * To measure the effect of depth: construct a dataset that *__requires__* a deep network to model efficiently  
    * Weights that generalize the most have the least gradient when training on a new dataset (remember: cats vs dogs -> foxes)  
    * K-Separable learning instead of linearly (2-)separable learning; the output layer dictates the configuration of the transformed input data to be "classified"  
    * wrt. [Karpathys "Unreasonable Effectiveness of RNNs" post](https://karpathy.github.io/2015/05/21/rnn-effectiveness/) and [Y.Goldbergs "Unreasonable Effectiveness of (Char-Level) n-grams" post](https://nbviewer.jupyter.org/gist/yoavg/d76121dfde2618422139): Do the complex rules learned by an LSTM architecture (considering its inductive biases) _e.g. neuron that counts, tracks indentation, etc._ have better generalization than n-gram probabilities? Do these rules imply learning a better method, algorithm, mechanism, etc.?  
        * _Golberg_ claims that RNNs are impressive because of <span>*__"context awareness"__*</span>{: style="color: purple"} (in C-code generation syntax).  
        * (compare the number $$n$$ of n-tuples VS dimension size of $$h$$)  
            (hint: google seems to think it's $$n=13$$ beats infinite $$h$$)  
        * Is this why/how NNs generalize?  
    * wrt. [Unintended Memorization in Neural Networks (Blog+Paper)](https://bair.berkeley.edu/blog/2019/08/13/memorization/): it proposes an attack to extract sensitive info from a model trained on private data (using a _"canary"_). I can refine the attack much further by exploiting the fact that the model is trained to maximize NLL and it will give the training data higher probability.  
    * Can we use the ideas in the [paper on differential privacy and unintended memorization in NNs](https://arxiv.org/pdf/1607.00133.pdf) to help learn more generalizable models/weights/patterns?  
    <br>

3. **Questions:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents93}  
    * Does Hinge Loss Maximize a margin when used with any classifier?  
    * How does LDA do feature extraction / dim-red?  
    * Time series data is known to posses linearity?  
    * How can we frame the __Abstract Modeling Problem__?  
    * How do humans speak (generate sentences)? They definitely do not just randomly sample from the distribution of natural language. Then, how should we teach models to speak, respond, think, etc.?  
    * Is it true that _research "should" be hypothesis -> experiments_ and not the other way like in AI?  
    * Where does "Game Theory" fit into AI, really?  
    <br>

4. **General Notes & Observations:**{: style="color: SteelBlue"}{:  .bodyContents9 #bodyContents94}  
    * Three Schools of Learning: (1) __Bayesians__   (2) __Kernel People__    (3) __Frequentists__  
    * Bayesians', INCORRECTLY, claimed that:  
        * Highly over-parametrised models fitted via maximum likelihood can't possibly work, they will overfit, won't generalise, etc.  
        * Any model with infinite parameters should be strictly better than any large, but finite parametric model.  
            (e.g. nonparametric models like kernel machines are a principled way to build models with effectively infinite number of parameters)  
    * Don't try averaging if you want to synchronize a bunch of clocks! (Ensemble Averaging/Interview Q)   
        The noise is __not Gaussian__.  
        Instead, you expect that many of them would be slightly wrong, and a few of them would have stopped or would be wildly wrong and by averaging you end making them all significantly wrong.  
    * __Generalization:__  
        * It seems that Occams Razor is equivalent to saying that a "non-economical" model is not a good model. So, can we use Inf-Th to quantify the information in these models?  
            The idea that a simple model e.g. "birds fly", is much better than a much more complicated and hard to encode model e.g. "birds fly except chicken, penguins, etc."  
    * __Width vs Depth in NN Architectures__:  
        Thinking of the NN as running a computer program that performs a calculation, you can think of __width__ as a measure of how much *__parallelization__* you can have in your computation, and __depth__ as a measure of *__serialization__*.   
    * A Hopfield net the size of a brain (connectivity patterns are quite diff, of course) could store a memory per second for 450 years.  
    * __Overfitting in the Brain:__ You can call it superstition or bad habits. Even teach some to animals.  
    * Real world data prefers lower Kolmogorov complexity (and hence enables the ability to learn) is a very strange fundamental asymmetry in nature??   
        It’s as puzzling as having so much matter than antimatter.  
    * An SVM is, in a way, a type of neural network (you can learn a SVM solution through backpropagation)  
    * In CNNs there are no FC layers, they are equivalent to $$1 \times 1$$ convolutions [link](https://www.facebook.com/yann.lecun/posts/10152820758292143)  
    * In support of IB (Information Bottleneck) Theory: [this paper](https://arxiv.org/abs/1802.08232) suggests that <span>Memorization happens __early__ in training</span>{: style="color: purple"}.  
    <br>

5. **Insights:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents95}  
    * Utkarsh idea of co-adaptation is similar to DROPOUT Motivation: hidden units co-adapting to each other on training data  
    * Attention Functions Properties: monotonicity, sparsity etc.  
    * Think about __Learning__, __Overfitting__, and __Regularization__ in terms of <span>accidental regularities/patterns due to the particular sample</span>{: style="color: purple"}   
        * __Process of Learning__:  
            1. Fit Most Common Pattern vs Fit Easiest Patterns?
            2. Fit Most Common Pattern vs Fit Easiest Patterns?
            3. Fit next Most Common Pattern vs Fit next Easiest Patterns? ..  
            4. ...  
            5. Fit patterns that exist per/sample (e.g. Noise)  
        * __Overfitting:__  
            Happens when there are patterns that manifest in the particular sample that might not have been that *__common__* when looking at a larger/different sample.  
        * __Regularization:__  
            Stops the model from learning the __least-common__/__hardest__ patterns by putting some sort of threshold.  
        * When we fit the model, it cannot tell which regularities are real and which are caused by sampling error.  
            The higher the capacity, the better it fits the __sampling error__.  
        * This ties in nicely with the idea of <span>"match your model capacity to the __amount of data__ that you have and NOT to the _target capacity_"</span>{: style="color: purple"}.  
        * <button>Bias & Variance wrt this framework of thinking:</button>{: .showText value="show" onclick="showTextPopHide(event);"}
            * The bias term is big if the model has too little capacity to fit the data.  
            * The variance term is big if the model has so much capacity that it is good at fitting the sampling error in each particular training set.    
            {: hidden=""}
    * Although Recurrent models do not have an ["explicit way to model long and short range dependencies"](https://youtu.be/5vcj8kSwBCY?t=275), FastWeights does. <Turn that into a Research Idea.>  
    * Although Recurrent models do not have an ["explicit way to model long and short range dependencies"](https://youtu.be/5vcj8kSwBCY?t=275), FastWeights does. <Turn that into a Research Idea.>  


6. **Experiments & Results:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents96}  

<!-- 7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents97}
8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents98} -->