---
layout: NotesPage
title: KNN <br> K-Nearest Neighbor
permalink: /work_files/research/ml/knn
prevLink: /work_files/research/ml.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [K-Nearest Neighbors (k-NN)](#content1)
  {: .TOC1}
</div>

***
***

## K-Nearest Neighbors (k-NN)
{: #content1}

1. **KNN:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}    
    __KNN__ is a _non-parametric_ method used for classification and regression.  
    It is based on the [__Local Constancy (Smoothness) Prior__](/work_files/research/dl/theory/dl_book_pt1#bodyContents32), which states that "the function we learn should not change very much within a small region.", for generalization.  
    * <button>K-Means & Local Constancy</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        ![img](/main_files/dl_book/7.png){: hidden=""}  

    <br>

2. **Structure:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    In both classification and regression, the input consists of the $$k$$ closest training examples in the feature space. The output depends on whether k-NN is used for classification or regression:  
    {: #lst-p}
    * In __k-NN classification__, the output is a class membership. An object is classified by a plurality vote of its neighbors, with the object being assigned to the class most common among its $$k$$ nearest neighbors ($$k$$ is a positive integer, typically small). If $$k = 1$$, then the object is simply assigned to the class of that single nearest neighbor.  
    * In __k-NN regression__, the output is the property value for the object. This value is the average of the values of $$k$$ nearest neighbors.  
    <br>

3. **Formal Description - Statistical Setting:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    Suppose we have pairs $${\displaystyle (X_{1},Y_{1}),(X_{2},Y_{2}),\dots ,(X_{n},Y_{n})}$$ taking values in $${\displaystyle \mathbb {R} ^{d}\times \{1,2\}}$$, where $$Y$$ is the class label of $$X$$, so that $${\displaystyle X|Y=r\sim P_{r}}$$ for $${\displaystyle r=1,2}$$ (and probability distributions $${\displaystyle P_{r}}$$. Given some norm $${\displaystyle \|\cdot \|}$$ on $${\displaystyle \mathbb {R} ^{d}}$$ and a point $${\displaystyle x\in \mathbb {R} ^{d}}$$, let $${\displaystyle (X_{(1)},Y_{(1)}),\dots ,(X_{(n)},Y_{(n)})}$$ be a reordering of the training data such that $${\displaystyle \|X_{(1)}-x\|\leq \dots \leq \|X_{(n)}-x\|}$$.  
    <br>

33. **Choosing $$k$$:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents133}  
    Nearest neighbors can produce very complex decision functions, and its behavior is highly dependent on the choice of $$k$$:  
    ![img](https://cdn.mathpix.com/snip/images/vPHUZyVTNj4bOgDpPeCA-_KUR6QvlArX_yCy0FVeeNY.original.fullsize.png){: width="50%" .center-image}  

    Choosing $$k = 1$$, we achieve an _optimal training error_ of $$0$$ because each training point will classify as itself, thus achieving $$100\%$$ accuracy on itself.  
    However, $$k = 1$$ __overfits__ to the training data, and is a terrible choice in the context of the bias-variance tradeoff.  

    Increasing $$k$$ leads to _increase in training error_, but a _decrease in testing error_ and achieves __better generalization__.  

    At one point, if $$k$$ becomes _too large_, the algorithm will __underfit__ the training data, and suffer from __huge bias__.  

    In general, <span>we select $$k$$ using __cross-validation__</span>{: style="color: goldenrod"}.  

    ![img](https://cdn.mathpix.com/snip/images/XaIAJQLphKue6B56LLdXoXM1UMsgVyKlXKkVeW1kjB0.original.fullsize.png){: width="50%" .center-image}  
    :   $$\text{Training and Test Errors as a function of } k \:\:\:\:\:\:\:\:\:\:\:\:$$
    {: style="margin-top: 0; font-size: 72%"}

    <br>

44. **Bias-Variance Decomposition of k-NN:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents144}  
    <button>PDF (189)</button>{: .showText value="show"
     onclick="showTextPopHide(event);"}
    <iframe hidden="" src="/main_files/ml/knn/knn_bias_var.pdf" frameborder="0" height="840" width="646" title="Layer Normalization" scrolling="auto"></iframe>

    <br>

4. **Properties:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    * __Computational Complexity__:  
        * We require $$\mathcal{O}(n)$$ space to store a training set of size $$n$$. There is no runtime cost during training if we do not use specialized data structures to store the data.  
            However, predictions take $$\mathcal{O}(n)$$ time, which is costly.  
        * There has been research into __Approximate Nearest Neighbors (ANN)__ procedures that quickly find an approximation for the nearest neighbor - some common ANN methods are *__Locality-Sensitive Hashing__* and algorithms that perform dimensionality reduction via *__randomized (Johnson-Lindenstrauss) distance-preserving projections__*.  
        * k-NN is a type of _instance-based learning_, or _"lazy learning"_, where the function is only approximated locally and all computation is deferred until classification.  
    * __Flexibility__:  
        * When $$k>1,$$ k-NN can be modified to output predicted probabilities $$P(Y \vert X)$$ by defining $$P(Y \vert X)$$ as the proportion of nearest neighbors to $$X$$ in the training set that have class $$Y$$.  
        * k-NN can also be adapted for regression — instead of taking the majority vote, take the average of the $$y$$ values for the nearest neighbors.  
        * k-NN can learn very complicated, __non-linear__ decision boundaries (highly influenced by choice of $$k$$).  
    * __Non-Parametric(ity)__:  
        k-NN is a __non-parametric method__, which means that the number of parameters in the model grows with $$n$$, the number of training points. This is as opposed to parametric methods, for which the number of parameters is independent of $$n$$.  
    * __High-dimensional Behavior__:  
        * k-NN does NOT behave well in high dimensions.  
            As the _dimension increases_, _data points drift farther apart_, so even the nearest neighbor to a point will tend to be very far away.  
        * It is sensitive to the local structure of the data (in any/all dimension/s).  
    * __Theoretical Guarantees/Properties__:  
        __$$1$$-NN__ has impressive theoretical guarantees for such a simple method:  
        * _Cover and Hart, 1967_ prove that <span>as the number of training samples $$n$$ approaches infinity, the expected prediction error for $$1-\mathrm{NN}$$ is upper bounded by $$2 \epsilon^{*}$$, where $$\epsilon^{*}$$ is the __Bayes (optimal) error__</span>{: style="color: goldenrod"}.  
        * _Fix and Hodges, 1951_ prove that <span>as $$n$$ and $$k$$ approach infinity and if $$\frac{k}{n} \rightarrow 0$$, then the $$k$$ nearest neighbor error approaches the *__Bayes error__*</span>{: style="color: goldenrod"}.  
    <br>

5. **Algorithm and Computational Complexity:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  
    __Training:__{: style="color: red"}  
    * __Algorithm:__ To train this classifier, we simply store our training data for future reference.  
        Sometimes we store the data in a specialized structure called a *__k-d tree__*. This data structure usually allows for faster (average-case $$\mathcal{O}(\log n)$$) nearest neighbors queries.  
        > For this reason, k-NN is sometimes referred to as *__“lazy learning”__*.  
    * __Complexity__: $$\:\:\:\:\mathcal{O}(1)$$   

    __Prediction:__{: style="color: red"}  
    {: #lst-p}
    * __Algorithm__:  
        1. Compute the $$k$$ closest training data points (_"nearest neighbors"_) to input point $$\boldsymbol{z}$$.  
            "Closeness" is quantified using some metric; e.g. __Euclidean distance__.  
        2. __Assignment Stage:__  
            * __Classification__: Find the most common class $$y$$ among these $$k$$ neighbors and classify $$\boldsymbol{z}$$ as $$y$$ (__majority vote__)   
            * __Regression__: Take the __average__ label of the $$k$$ nearest points.  
    * __Complexity__: $$\:\:\:\:\mathcal{O}(N)$$   
    <br>


    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * We choose odd $$k$$ for _binary classification_ to break symmetry of majority vote  
    <br>


6. **Behavior in High-Dimensional Space - Curse of Dimensionality:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}  
    As mentioned, k-NN does NOT perform well in high-dimensional space. This is due to the "Curse of Dimensionality".  

    __Curse of Dimensionality (CoD):__{: style="color: red" #bodyContents16_cod}  
    To understand CoD, we first need to understand the properties of metric spaces. In high-dimensional spaces, much of our low-dimensional intuition breaks down:  

    __Geometry of High-Dimensional Space:__  
    Consider a ball in $$\mathbb{R}^d$$ centered at the origin with radius $$r$$, and suppose we have another ball of radius $$r - \epsilon$$ centered at the origin. In low dimensions, we can visually see that _much of the volume of the outer ball is also in the inner ball_.  
    In general, <span>the volume of the outer ball is proportional to $$r^{d}$$</span>{: style="color: goldenrod"}, while <span>the volume of the inner ball is proportional to $$(r-\epsilon)^{d}$$</span>{: style="color: goldenrod"}.  
    Thus the __ratio of the volume of the inner ball to that of the outer ball__ is:  
    <p>$$\frac{(r-\epsilon)^{d}}{r^{d}}=\left(1-\frac{\epsilon}{r}\right)^{d} \approx e^{-\epsilon d / r} \underset{d \rightarrow \infty}{\longrightarrow} 0$$</p>  
    Hence as $$d$$ gets large, most of the volume of the outer ball is concentrated in the annular region $$\{x : r-\epsilon < x < r\}$$ instead of the inner ball.  
    ![img](https://cdn.mathpix.com/snip/images/7N0Mv-hf0RhjKeHDEzLJuQuEtI156Jq8JjqeaD96PB0.original.fullsize.png){: width="70%" .center-image}  


    __Concentration of Measure:__  
    High dimensions also make Gaussian distributions behave counter-intuitively. Suppose $$X \sim$$ $$\mathcal{N}\left(0, \sigma^{2} I\right)$$. If $$X_{i}$$ are the components of $$X$$ and $$R$$ is the distance from $$X$$ to the origin, then $$R^{2}=\sum_{i=1}^{d} X_{i}^{2}$$. We have $$\mathbb{E}\left[R^{2}\right]=d \sigma^{2},$$ so in expectation a random Gaussian will actually be reasonably far from the origin. If $$\sigma=1,$$ then $$R^{2}$$ is distributed *__chi-squared__* with _$$d$$ degrees of freedom_.  
    One can show that in high dimensions, with high probability $$1-\mathcal{O}\left(e^{-d^{\epsilon}}\right)$$, this multivariate Gaussian will lie within the annular region $$\left\{X :\left|R^{2}-\mathbb{E}\left[R^{2}\right]\right| \leq d^{1 / 2+\epsilon}\right\}$$ where $$\mathbb{E}\left[R^{2}\right]=d \sigma^{2}$$ (one possible approach is to note that as $$d \rightarrow \infty,$$ the chi-squared approaches a Gaussian by the __CLT__, and use a __Chernoff bound__ to show exponential decay). This phenomenon is known as __Concentration of Measure__.  

    Without resorting to more complicated inequalities, we can show a simple, weaker result:  
    $$\bf{\text{Theorem:}}$$ $$\text{If } X_{i} \sim \mathcal{N}\left(0, \sigma^{2}\right), i=1, \ldots, d \text{  are independent and } R^{2}=\sum_{i=1}^{d} X_{i}^{2}, \text{ then for every } \epsilon>0, \\ 
     \text{the following holds: } $$  
    <p>$$\lim_{d \rightarrow \infty} P\left(\left|R^{2}-\mathbb{E}\left[R^{2}\right]\right| \geq d^{\frac{1}{2}+\epsilon}\right)=0$$</p>  
    Thus in the limit, the __squared radius is concentrated about its mean__{: style="color: goldenrod"}.  

    <button>Proof.</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/2sljiV63a9o4RE6sUbYN4yAl8yV0rgz0DCx15z1yTBM.original.fullsize.png){: width="100%" hidden=""}  

    Thus a <span>random Gaussian will lie within a thin annular region away from the origin in high dimensions with high probability</span>{: style="color: goldenrod"}, even though _the mode of the Gaussian bell curve is at the origin_. This illustrates the phenomenon in _high dimensions_ where *__random data is spread very far apart__*.  

    The k-NN classifier was conceived on the principle that _nearby points should be of the same class_ - however, in high dimensions, _even the nearest neighbors_ that we have to a random test point _will_ tend to _be **far** away_, so this principle is _no longer useful_.  
    <br>

7. **Improving k-NN:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}  
    __(1) Obtain More Training Data:__{: style="color: red"}  
    More training data allows us to counter-act the sparsity in high-dimensional space.  

    __(2) Dimensionality Reduction - Feature Selection and Feature Projection:__{: style="color: red"}  
    Reduce the dimensionality of the features and/or pick better features. The best way to counteract the curse of dimensionality.  

    __(3) Different Choices of Metrics/Distance Functions:__{: style="color: red"}  
    We can modify the distance function. E.g.  
    {: #lst-p}
    * The family of __Minkowski Distances__ that are induced by the $$L^p$$ norms:  
        <p>$$D_{p}(\mathbf{x}, \mathbf{z})=\left(\sum_{i=1}^{d}\left|x_{i}-z_{i}\right|^{p}\right)^{\frac{1}{p}}$$</p>  
        > Without preprocessing the data, $$1-\mathrm{NN}$$ with the $$L^{3}$$ distance outperforms $$1-\mathrm{NN}$$ with $$L^{2}$$ on MNIST.  
    * We can, also, use __kernels__ to compute distances in a <span>_different_ feature space</span>{: style="color: goldenrod"}.  
        For example, if $$k$$ is a kernel with associated feature map $$\Phi$$ and we want to compute the Euclidean distance from $$\Phi(x)$$ to $$\Phi(z)$$, then we have:  
        <p>$$\begin{aligned}\|\Phi(\mathbf{x})-\Phi(\mathbf{z})\|_ {2}^{2} &=\Phi(\mathbf{x})^{\top} \Phi(\mathbf{x})-2 \Phi(\mathbf{x})^{\top} \Phi(\mathbf{z})+\Phi(\mathbf{z})^{\top} \Phi(\mathbf{z}) \\ &=k(\mathbf{x}, \mathbf{x})-2 k(\mathbf{x}, \mathbf{z})+k(\mathbf{z}, \mathbf{z}) \end{aligned}$$</p>  
        Thus if we define $$D(\mathrm{x}, \mathrm{z})=\sqrt{k(\mathrm{x}, \mathrm{x})-2 k(\mathrm{x}, \mathrm{z})+k(\mathrm{z}, \mathrm{z})}$$ , then we can perform Euclidean nearest neighbors in $$\mathrm{\Phi}$$-space without explicitly representing $$\Phi$$ by using the kernelized distance function $$D$$.  

    <br>