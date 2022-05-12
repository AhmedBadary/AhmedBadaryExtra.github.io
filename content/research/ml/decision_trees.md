---
layout: NotesPage
title: Decision Trees
permalink: /work_files/research/ml/dec_trees
prevLink: /work_files/research/dl/ml.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Decision Trees](#content1)
  {: .TOC1}
  * [Random Forests](#content2)
  {: .TOC2}
<!--   * [Boosting](#content4)
  {: .TOC4}
  * [Stacking](#content5)
  {: .TOC5} -->
  <!-- * [SIXTH](#content6)
  {: .TOC6} -->
</div>

***
***


## Decision Trees
{: #content1}

<button>Decision Trees (189 notes - local)</button>{: .showText value="show"
     onclick="showText_withParent_PopHide(event);"}
<iframe hidden="" src="/main_files/ml/decision_trees/n25.pdf#page=4" frameborder="0" height="840" width="646" title="Layer Normalization" scrolling="auto"></iframe>

<!-- 
* [**Decision Trees (189 notes - local)**](/main_files/ml/decision_trees/n25.pdf#page=4){: value="show" onclick="iframePopA(event)"}
<a href="/main_files/ml/decision_trees/n25.pdf#page=4"></a>
    <div markdown="1"> </div>     
-->


<!-- <button>Decision Trees (189 notes)</button>{: .showText value="show"
     onclick="showText_withParent_PopHide(event);"}
<iframe hidden="" src="https://www.eecs189.org/static/notes/n25.pdf#page=4" frameborder="0" height="840" width="646" title="Layer Normalization" scrolling="auto"></iframe> -->



1. **Decision Trees:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    A __decision tree__ is a decision support tool that uses a tree-like model of decisions and their possible consequences, including chance event outcomes, resource costs, and utility. It is one way to display an algorithm that only contains <span>conditional control statements</span>{: style="color: goldenrod"}.  

    The trees have two types of __Nodes:__  
    {: #lst-p}
    1. __Internal Nodes:__ test feature values (usually just $$1$$) and branch accordingly  
    2. __Leaf Nodes:__ specify class $$h(\mathbf{x})$$  

    ![img](https://cdn.mathpix.com/snip/images/tt_eQrxZmN0-fp6GnvjzbJm76S63axyRXQSsJN5egd0.original.fullsize.png){: width="80%"}  
    <br>

11. **CART (Classification And Regression Trees) Learning:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents111}  
    __Decision tree learning__ uses a _decision tree_ (as a predictive model) to go from observations about an item (represented in the branches) to conclusions about the item's target value (represented in the leaves).  

    > "Nonlinear method for classification and regression." - Schewchuk  

    __Classification Trees:__{: style="color: red"}  
    Tree models where the _target variable_ can take a _discrete set of values_ are called __classification trees__; in these tree structures:  
    {: #lst-p}
    * __Leaves__ represent __class labels__ and 
    * __Branches__ represent __conjunctions of features__ that lead to those class labels.  


    __Regression Trees:__{: style="color: red"}  
    Decision trees where the _target variable_ can take _continuous values_ (typically real numbers) are called __regression trees__.  

    <br>

2. **Properties:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    * __Non-Linear__
    * Used for Both, __Classification__ and __Regressions__
    * Cuts $$X$$ space into *__rectangular cells__*  
    * Works well with both __quantitative__ and __categorical__ features
    * Interpretable results (inference)
    * Decision boundary can be arbitrarily complicated (increase number of nodes to split on)  
        * Linear Classifiers VS Decision Trees ($$x$$ axis) \| Linear VS Non-Linear data ($$y$$ axis)  
            ![img](https://cdn.mathpix.com/snip/images/-MrzU9U6VLcqC8ca6cZ5mg3aUws5XJGnRG1Q-7BFrJo.original.fullsize.png){: width="50%"}  
    <br>

3. **Classification Learning Algorithm:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    Greedy, top-down learning heuristic.  
    Let $$S \subseteq\{1,2, \ldots, n\}$$ be set of sample point indices.  
    Top-level call: $$S=\{1,2, \ldots, n\} .$$  
    __Algorithm:__{: style="color: red"}  
    ![img](https://cdn.mathpix.com/snip/images/67ZJ9vY4y4bOWqkNaUm5DAt5KveQsfsg_5-_jddkSVI.original.fullsize.png){: width="80%"}  
    * [[**Algo (189)**]](https://www.youtube.com/embed/-blJnZPNwf8?start=968)  

    __(*) How to choose best split?:__{: style="color: red"}  
    {: #lst-p}
    1. Try all splits
    2. For a set $$S$$, let $$J(S)$$ be the __cost__ of $$S$$  
    3. Choose the split that *__minimizes__* $$J(S_l) + J(S_r)$$; or,   
        * The split that minimizes the __weighted average__:  
            <p>$$\dfrac{\left\vert S_{l}\right\vert  J\left(S_{l}\right)+\left\vert S_{r}\right\vert  J\left(S_{r}\right)}{\left\vert S_{l}\right\vert +\left\vert S_{r}\right\vert }$$</p>  

    * [[**Choosing Split (189)**]](https://www.youtube.com/embed/-blJnZPNwf8?start=1495)  

    * __Choosing the Split - Further Discussion:__  
        * For binary feature $$x_{i} :$$ children are $$x_{i}=0 \:\: \& \:\: x_{i}=1$$
        * If $$x_{i}$$ has $$3+$$ discrete values: split depends on application.
            * Sometimes it makes sense to use __multiway__ splits; sometimes __binary__ splits.  
        * If $$x_{i}$$ is quantitative: sort $$x_{i}$$ values in $$S$$ ; try splitting between each pair of unequal consecutive values.
            * We can __radix sort__ the points in __linear time__, and if $$n$$ is huge we should.  
        * __Efficient Splitting (clever bit):__ As you scan sorted list from left to right, you can update entropy in $$\mathcal{O}(1)$$ time per point!  
            * This is important for obtaining a fast tree-building time.  
        * [How to update # $$X$$s and $$O$$s Illustration (189)](https://www.youtube.com/-blJnZPNwf8?start=4338)  
        * [Further Discussion (189)](https://www.youtube.com/-blJnZPNwf8?start=4087)  



    __How to choose the cost $$J(S)$$:__{: style="color: red"}  
    We can accomplish this by __Measuring the Entropy__ (from _information theory_):  
    Let $$Y$$ be a random class variable, and suppose $$P(Y=C) = p_C$$.  
    * The __Self-Information ("surprise")__  of $$Y$$ being class $$C$$ (non-negative) is:  
        <p>$$- \log_2 p_C$$</p>   
        * Event w/ probability $$= 1$$  gives us __zero surprise__  
        * Event w/ probability $$= 0$$  gives us __infinite surprise__  
    * The __Entropy ("average surprisal")__ of an index set $$S$$:  
        <p>$$H(S)=-\sum_{\mathbf{C}} p_{\mathbf{C}} \log _{2} p_{\mathbf{C}}, \quad \text { where } p_{\mathbf{C}}=\dfrac{\left|\left\{i \in S : y_{i}=\mathbf{C}\right\}\right|}{|S|}$$</p>  
        The proportion of points in $$S$$ that are in class $$C$$.  
        * If all points in $S$ belong to same class? $$H(S)=-1 \log_{2} 1=0$$  
        * Half class $$C,$$ half class $$D ? H(S)=-0.5 \log_{2} 0.5-0.5 \log_{2} 0.5=1$$  
        * $$n$$ points, all different classes? $$H(S)=-\log_{2} \dfrac{1}{n}=\log_{2} n$$  
    * __Weighted avg entropy__ after split is:  
        <p>$$H_{\text {after }}=\dfrac{\left|S_{l}\right| H\left(S_{l}\right)+\left|S_{r}\right| H\left(S_{r}\right)}{\left|S_{l}\right|+\left|S_{r}\right|}$$</p>  
    * <span>Choose the split that __Maximizes *Information Gain*__</span>{: style="color: goldenrod"}:  
        <p>$$\text{Info-Gain} = H(S) - H_{\text{after}}$$</p>  
        $$\iff$$  
        <span>__Minimizing__ $$H_{\text{after}}$$</span>{: style="color: goldenrod"}.  

        * Info gain always positive except when one child is empty or  
            <p>$$\forall \mathrm{C}, P\left(y_{i}=\mathrm{C} | i \in S_{l}\right)=P\left(y_{i}=\mathrm{C} | i \in S_{r}\right)$$</p>  
            * [[**Information Gain VS other costs (189)**]](https://www.youtube.com/embed/-blJnZPNwf8?start=3566)  


    * [[**Choosing Cost - Bad Idea (189)**]](https://www.youtube.com/embed/-blJnZPNwf8?start=1740)  
    * [[**Choosing Cost - Good Idea (189)**]](https://www.youtube.com/embed/-blJnZPNwf8?start=2240)  

    <br>


4. **Algorithms and their Computational Complexity:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    [Algorithms and Complexity (189)](https://www.youtube.com/-blJnZPNwf8?start=4458)  

    __Test Point:__{: style="color: red"}  
    * __Algorithm:__ Walk down tree until leaf. Return its label.  
    * __Run Time:__  
        * __Worst-case Time:__ is $$\mathcal{O}(\text{(tree) depth})$$.  
            * For __binary features__, that’s $$\leq d$$.  
            * For __Quantitative features__, they may go deeper.  
            * Usually (not always) $$\leq \mathcal{O}(\log n)$$   
    
    __Training:__{: style="color: red"}  
    * __Algorithm:__  
        * For __Binary Features:__ try $$\mathcal{O}(d)$$ splits at each node.  
        * For __Quantitative Features:__ try $$\mathcal{O}(n'd)$$; where $$n' = \#$$ of points in node  
    * __Run Time:__  
        * __Splits/Per-Node Time__: is $$\mathcal{O}(d)$$ for both binary and quantitative.  
            > Quantitative features are asymptotically just as fast as binary features because of our clever way of computing the entropy for each split.  
        * __Points/Per-Node Amount (number)__: is $$\mathcal{O}(n)$$ points per node   
        * __Nodes/per-point Amount (number)__: is $$\mathcal{O}(\text{depth})$$ nodes per point (i.e. each point participates in $$\mathcal{O}(\text{depth})$$ nodes)   
        $$\implies$$  
        * __Worst-case Time:__  
            <p>$$\mathcal{O}(d) \times \mathcal{O}(n) \times \mathcal{O}(\text{depth}) \leq \mathcal{O}(nd  \text{ depth}) $$</p>  
    <br>  

5. **Multivariate Splits:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  
    [Multivariate Splits (189)](https://www.youtube.com/MPqVQy8tjU0?start=57)  
    <br>

6. **Regression Tree Learning:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}  
    [Regression Trees (189)](https://www.youtube.com/MPqVQy8tjU0?start=420)  
    <br>

7. **Early Stopping:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}  
    [Early Stopping (189)](https://www.youtube.com/MPqVQy8tjU0?start=760)  
    <br>

8. **Pruning:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18}  
    [Pruning (189)](https://www.youtube.com/MPqVQy8tjU0?start=1765)  
    <br>


__Notes:__{: style="color: red"}  
{: #lst-p}
* __Number of splits in a Decision Tree__: $$= dn$$  
* __Complexity of finding the split__:  
    1. __Naive:__ $$\mathcal{O}(dn^2)$$  
    2. __Fast (sort):__ $$\mathcal{O}(dn \: log n)$$  

***

## Random Forests
{: #content2}

1. **Ensemble Learning:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    [Ensemble Learning (189)](https://www.youtube.com/MPqVQy8tjU0?start=2711)  
    <br>

2. **Bagging - Bootstrap AGGregating:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}  
    [Bagging (189)](https://www.youtube.com/MPqVQy8tjU0?start=3150)  
    <br>

3. **Random Forests:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}  


<!-- 3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}  

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}  

 -->