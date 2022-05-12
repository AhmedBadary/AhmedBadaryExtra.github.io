---
layout: NotesPage
title: Learning
permalink: /work_files/research/dl/theory/learning_summary
prevLink: /work_files/research/dl/theory.html
---

## The Learning Problem

<span>__Learning:__</span>{: style="color: goldenrod"}  
A computer program is said to <span>learn</span>{: style="color: goldenrod"} from *__experience__* $$E$$ with respect to some class of *__tasks__* $$T$$ and *__performance measure__* $$P$$, if its performance at tasks in $$T$$, as measured by $$P$$, improves with experience $$E$$.  


1. **The Basic Premise/Goal of Learning:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    <span>"Using a set of observations to uncover an underlying process"</span>{: style="color: purple"}  
    
    Rephrased mathematically, the __Goal of Learning__ is:   
    Use the Data to find a hypothesis $$g \in \mathcal{H}$$, from the hypothesis set $$\mathcal{H}=\{h\}$$, that _approximates_ $$f$$ well.<br>

2. **When to do Learning:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    When:  
    1. A pattern Exists
    2. We cannot pin the pattern down mathematically 
    3. We have Data<br>

3. **Components of the Problem (Learning):**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    * __Input__: $$\vec{x}$$  
    * __Output__: $$y$$ 
    * __Data__:  $${(\vec{x}_ 1, y_ 1), (\vec{x}_ 2, y_ 2), ..., (\vec{x}_ N, y_ N)}$$ 
    * __Target Function__: $$f : \mathcal{X} \rightarrow \mathcal{Y}$$  (Unknown/Unobserved)  
    * __Hypothesis__: $$g : \mathcal{X} \rightarrow \mathcal{Y}$$  
        Learned from the Data, with the hope that it approximates $$f$$ well.<br>  

5. **Components of the Solution:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  
    * __The Learning Model__:  
        * __The Hypothesis Set__:  $$\mathcal{H}=\{h\},  g \in \mathcal{H}$$  
            E.g. Perceptron, SVM, FNNs, etc.  
        * __The Learning Algorithm__: picks $$g \approx f$$ from a hypothesis set $$\mathcal{H}$$  
            E.g. Backprop, Quadratic Programming, etc.<br>

8. **The Learning Diagram:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18}  
    ![img](/main_files/dl/theory/caltech/3.png){: width="70%"}  


7. **Types of Learning:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}  
    * __Supervised Learning__: the task of learning a function that maps an input to an output based on example input-output pairs.  
        ![img](/main_files/dl/theory/caltech/4.png){: width="50%"}  
    * __Unsupervised Learning__: the task of making inferences, by learning a better representation, from some datapoints that do not have any labels associated with them.  
        ![img](/main_files/dl/theory/caltech/5.png){: width="50%"}  
        > Unsupervised Learning is another name for [Hebbian Learning](https://en.wikipedia.org/wiki/Hebbian_theory)
    * __Reinforcement Leaning__: the task of learning how software agents ought to take actions in an environment so as to maximize some notion of cumulative reward.  
        ![img](/main_files/dl/theory/caltech/6.png){: width="50%"}<br>


<!-- ## The Feasibility of Learning

<div class="borderexample" markdown="1" Style="padding: 0;">
The Goal of this Section is to answer the question:   
<span>__"Can we make any statements/inferences outside of the sample data that we have?"__</span>{: style="color: purple"}
</div>
<br>

1. **The Problem of Learning:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    Learning a truly __Unknown__ function is __Impossible__, since outside of the observed values, the function could assume _any value_ it wants.<br>

2. **Learning is Feasible:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}  
    The statement we made that is equivalent to __Learning is Feasible__ is the following:  
    We establish a __theoretical guarantee__ that when you <span>__do well in-sample__</span>{: style="color: purple"} $$\implies$$ you <span>__do well out-of-sample (*"Generalization"*)__ </span>{: style="color: purple"}.  

    __Learning Feasibility__:  
    When learning we only deal with In-Sample Errors $$E_{\text{in}}(\mathbf{w})$$; we never handle the out-sample error explicitly; we take the theoretical guarantee that when you do well in-sample $$\implies$$ you do well out-sample (Generalization).<br>

3. **Achieving Learning:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}  
    __Generalization VS Learning:__  
    We know that _Learning is Feasible_.
    * __Generalization__:  
        It is likely that the following condition holds:  
        <p>$$\: E_{\text {out }}(g) \approx E_{\text {in }}(g)  \tag{3.1}$$</p>  
        This is equivalent to "good" __Generalization__.  
    * __Learning__:  
        Learning corresponds to the condition that $$g \approx f$$, which in-turn corresponds to the condition:  
        <p>$$E_{\text {out }}(g) \approx 0  \tag{3.2}$$</p>      


    __How to achieve Learning:__{: style="color: red"}    
    We achieve $$E_{\text {out }}(g) \approx 0$$ through:  
    {: #lst-p}
    1. $$E_{\mathrm{out}}(g) \approx E_{\mathrm{in}}(g)$$  
        A __theoretical__ result achieved through Hoeffding __(PROBABILITY THEORY)__{: style="color: goldenrod"}.   
    2. $$E_{\mathrm{in}}(g) \approx 0$$  
        A __Practical__ result of minimizing the In-Sample Error Function (ERM) __(OPTIMIZATION)__{: style="color: goldenrod"}.  

    Learning is, thus, reduced to the 2 following questions:  
    {: #lst-p}
    1. Can we make sure that $$E_{\text {out }}(g)$$ is close enough to $$E_{\text {in }}(g)$$? (theoretical)  
    2. Can we make $$E_{\text {in}}(g)$$ small enough? (practical)<br> -->