---
layout: NotesPage
title: The Essence of Linear Algebra
permalink: /work_files/research/math/la/linalg
prevLink: /work_files/research/dl/nlp.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Definitions and Intuitions](#content1)
  {: .TOC1}
<!--   * [SECOND](#content2)
  {: .TOC2} -->
</div>

***
***

[Essence of LA - 3b1b](https://www.youtube.com/watch?v=fNk_zzaMoSs&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&index=1)  
[LA (Stanford Review)](http://web.stanford.edu/class/cs224n/readings/cs229-linalg.pdf)  



## Definitions and Intuitions
{: #content1}

1. **Linear Algebra:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    __Linear Algebra__ is about two operations on _a list of numbers_:  
    1. Scalar Multiplication
    2. Vector Addition

2. **Vectors:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    Think of each element in the vector as a __scalar__ that scales the corresponding basis vectors.  
    > Meaning, think about how each one stretches or squishes vectors (in this case, the basis vectors $$\hat{i}, \hat{j}$$)  

    <p>$$\begin{bmatrix}
            x \\
            y 
        \end{bmatrix} = \begin{bmatrix}
            1 & 0  \\
            0 & 1 
        \end{bmatrix}   \begin{bmatrix}
                            x \\
                            y 
                        \end{bmatrix} = \color{red} x \color{red} {\underbrace{\begin{bmatrix}
            1 \\
            0 
        \end{bmatrix}}_ {\hat{i}}} + \color{red} y \color{red} {\underbrace{\begin{bmatrix}
            0 \\
            1 
        \end{bmatrix}}_ {\hat{j}}} = \begin{bmatrix}
            1\times x + 0 \times y \\
            0\times x + 1 \times y 
        \end{bmatrix}
    $$</p>  

3. **Span:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    The __Span__ of two vectors $$\mathbf{v}, \mathbf{w}$$ is the set of all linear combinations of the two vectors: 
    <p>$$a \mathbf{v} + b \mathbf{w} \: ; \: a,b \in \mathbb{R}$$</p>  


4. **Linearly Dependent Vectors:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    If one vector is in the span of the other vectors.  
    Mathematically:  
    <p>$$a \vec{v}+b \vec{w}+c \vec{u}=\overrightarrow{0} \implies a=b=c=0$$</p>  

44. **The Basis:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents144}  
    The __Basis__ of a vector space is a set of _linearly independent_ vectors that __span__ the full space.  

5. **Matrix as a Linear Transformation:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  
    __Summary__:
    1. Each *__column__*  is a _transformed_ version of the *__basis vectors__* (e.g. $$\hat{i}, \hat{j}$$)  
    2. The result of a __Matrix-Vector Product__ is the __linear combination__ of the *__vectors__* with the appropriate *__transformed coordinate/basis vectors__*  
        > i.e. __Matrix-Vector Product__ is a way to compute what the corresponding linear transformation does to the given vector.  


    __Matrix as a Linear Transformation:__{: style="color: red"}  
    Always think of Matrices as __Transformations of Space__:    
    * A Matrix represents a _specific linear transformation_
        * Where the *__columns__* represent the *__coordinates__* of the _transformed_ *__basis vectors__*   
    * & __Multiplying a matrix by a vector__ is EQUIVALENT to __Applying the transformation to that vector__  
    > The word _"transformation"_ suggests that you think using *__movement__*  
    > If a transformation takes some input vector to some output vector, we imagine that input vector moving over to the output vector.  
    > Then to understand the transformation as a whole, we might imagine watching every possible input vector move over to its corresponding output vector.  
    > This transformation/_"movement"_ is __Linear__, if it keeps all the vectors *__parallel__* and *__evenly spaced__*, and *__fixes the origin__*.  


    __Matrices and Vectors | The Matrix-Vector Product:__{: style="color: red"}  
    Again, We think of _each element_ in a vector as a *__scalar__* that scales the corresponding _basis vectors_.  
    * Thus, if we know how the basis vectors get transformed, we can then just scale them (by multiplying with our vector elements).  
        __Mathematically__, we think of the vector:   
        <p>$$\mathbf{v} = \begin{bmatrix}x \\y \end{bmatrix} = x\hat{i} + y\hat{j}$$</p>
        and its _transformed_ version:  
        <p>$$\text{Transformed } \mathbf{v} = x (\text{Transformed } \hat{i}) + y (\text{Transformed }  \hat{j})$$</p>  
        $$\implies$$ we can describe where any vector $$\mathbf{v}$$ go, by describing where the *__basis vectors__* will land.  
        > If you're given a _two-by-two matrix_ describing a _linear transformation_ and some specific _vector_ and you want to know where that linear transformation takes that vector, you can (1) take the coordinates of the vector (2) multiply them by the corresponding *__columns__* of the matrix, (3) then add together what you get.  
        This corresponds with the idea of adding the scaled versions of our new basis vectors.  
            ![img](/main_files/math/la/linalg/1.png){: width="60%"}  


    <p>$$ \mathbf{v} = 
        \begin{bmatrix}
            x \\
            y 
        \end{bmatrix} = \begin{bmatrix}
            1 & 0  \\
            0 & 1 
        \end{bmatrix}   \begin{bmatrix}
                            x \\
                            y 
                        \end{bmatrix} = \color{red} x \color{red} {\underbrace{\begin{bmatrix}
            1 \\
            0 
        \end{bmatrix}}_ {\hat{i}}} + \color{red} y \color{red} {\underbrace{\begin{bmatrix}
            0 \\
            1 
        \end{bmatrix}}_ {\hat{j}}} = \begin{bmatrix}
            1\times x + 0 \times y \\
            0\times x + 1 \times y 
        \end{bmatrix} = x\hat{i} + y\hat{j}
    $$</p>  

    __The Matrix-Vector Product:__  
    ![img](/main_files/math/la/linalg/2.png){: width="100%"}  


    __Non-Square Matrices $$(N \times M)$$:__{: style="color: red"}  
    Map vectors from $$\mathbb{R}^M \rightarrow \mathbb{R}^N$$.  
    They are _transformations between **dimensions**_.   


6. **The Product of Two Matrices:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}  
    The Product of Two Matrices Corresponds to the *__composition of the transformations__*, being applied from right to left.  
    This is __very important__ intuition:  
    > e.g. _do matrices commute?_  
    if you think of the matrices as _transformations of space_ then answer quickly is no.  
    Equivalently, _Are matrices associative?_  Yes, function composition is associative ($$f \circ(g \circ h) = (f \circ g) \circ h$$)  


7. **Linear Transformations:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}  
    __Linear Transformations__ are transformations that preserve the following properties:  
    1. All vectors that are _parallel_ remain parallel 
    2. All vectors are _evenly spaced_ 
    3. The __origin__ remains _fixed_  

    * [**An Equivalent Definition of Linearity**](https://www.youtube.com/embed/LyGKycYT2v0?start=295){: value="show" onclick="iframePopA(event)"}
    <a href="https://www.youtube.com/embed/LyGKycYT2v0?start=295"></a>
        <div markdown="1"> </div>    


8. **The Determinant:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18}  
    __The Determinant__ of a transformation is the _"scaling factor"_ by which the transformation changed any __area__ in the vector space.  

    __The Negative Determinant__ determines the *__orientation__*.  

    __Linearity of the Determinant__:  
    <p>$$\text{det}(AB) = \text{det}(A) \text{det}(B)$$</p>  


10. **Solving Systems of Equations:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents110}  
    The Equation $$A\mathbf{x} = \mathbf{b}$$, finds the vector $$\mathbf{x}$$ that _lands on the vector $$\mathbf{b}$$_ when the transformation $$A$$ is applied to it.    

    Again, the __intuition__: is to think of a linear system of equations, __geometrically__, as trying to find a particular vector that once transformed/moved, lands on the output vector $$\mathbf{b}$$.  
    * This becomes more important when you think of the different __properties__, of that transformation/function, encoded (now) in the *__matrix__* $$A$$:  
        * When the $$det(A) \neq 0$$ we know that space is preserved, and from the _properties of linearity_, we know there will always be one (*__unique__*) vector that would land on $$\mathbf{b}$$ once transformed (and you can find it by _"playing the transformation in reverse"_ i.e. the __inverse matrix__).  
        * When $$det(A) = 0$$ then the space is __squished__ down to a lower representation, resulting in __information loss__.  


9. **The Inverse of a matrix:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents19}  
    The __Inverse__ of a matrix is the matrix such that if we "algebraically" multiply the two matrices, we get back to the original coordinates (the identity).  
    It is, basically, the transformation applied in _reverse_.  

    __Why inverse transformation/matrix DNE when det is Zero (i.e. space is squished:__{: style="color: red"}  
    To do so, is equivalent to _transforming_ a __line__ into a __plane__, which would require _mapping_ each, individual, __vector__ into a __"whole line full of vectors" (multiple vectors)__; which is _not something a **Function**_ can do.  
    Functions map *__single input__* to *__single output__*.  


11. **The Determinants, Inverses, & Solutions to Equations:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents111}  
    When the $$\text{det} = 0$$ the area gets _squashed to $$0$$_, and _information is lost_. Thus:   
    1. The Inverse DNE
    2. A unique solution DNE  
    > i.e. there is no function that can take a line onto a plane; info loss


12. **The Rank:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents112}  
    __The Rank__ is the _dimensionality_ of the output of a transformation.  
    __Viewed as a Matrix__, it is the _number of independent vectors (as columns)_ that make up the matrix.  


13. **The Column Space:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents113}  
    __The Column Space__ is the set of all possible outputs of a transformation/matrix.  
    * View each column as a _basis vector_; there span is then, all the possible outputs
    * __The Zero Vector (origin)__: is always in the column space (corresponds to preserving the origin)
        
    The __Column Space__ allows us to understand *__when a solution exists__*.  
    For example, even when the matrix is not full-rank (det=0) a solution might still exist; if, when $$A$$ squishes space onto a line, the vector $$\mathbf{b}$$ lies on that line (in the __span__ of that line).  
    * Formally, solution exists if $$\mathbf{b}$$ is in the __column space__ of $$A$$.   


14. **The Null Space:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents114}  
    __The Null Space__ is the set of vectors that get _mapped to the origin_; also known as __The Kernel__.   

    The __Null Space__ allows us to understand _what the set of all possible solutions look like_.   

     __Rank and the Zero Vector:__{: style="color: red"}  
    A __Full-Rank__ matrix maps __only the origin__ to itself.  
    A __non-full rank (det=0)__ (rank=n-1) matrix maps a whole __line__ to the origin, (rank=n-2) a __plane__ to the origin, etc.  


15. **The Dot Product/Scalar Product:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents115}  
    (for vectors $$\mathbf{u}, \mathbf{v}$$)  
    <p>$$\mathbf{u} \cdot \mathbf{v} = \mathbf{u}^T \mathbf{v}$$</p>   
    * __Geometrically__:  
        1. project 
            

16. **Cramer's Rule:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents116}  
    * [**Cramer's Rule Geometrically**](https://www.youtube.com/embed/jBsC34PxzoM?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab){: value="show" onclick="iframePopA(event)"}
    <a href="https://www.youtube.com/embed/jBsC34PxzoM?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab"></a>
        <div markdown="1"> </div>    



17. **Coordinate Systems:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents117}  

    A __Coordinate System__ is just a way to formalize the basis vectors and their lengths. All coordinate systems agree on where the __origin__ is.  
    __Coordinate Systems__ are a way to _translate_ between *__vectors__* (defined w.r.t. basis vectors being scaled and added in space) and *__sets of numbers__* (the elements of the vector/list/array of numbers which we define).  

    * [**Translating between Coordinate Systems**](https://www.youtube.com/embed/P2LTAUO1TdA?start=257){: value="show" onclick="iframePopA(event)"}
    <a href="https://www.youtube.com/embed/P2LTAUO1TdA?start=257"></a>
        <div markdown="1"> </div>    
        > Imp: _6:47_  

    * [**Translating a Matrix/Transformation between Coordinate Systems**](https://www.youtube.com/embed/P2LTAUO1TdA?start=552){: value="show" onclick="iframePopA(event)"}
    <a href="https://www.youtube.com/embed/P2LTAUO1TdA?start=552"></a>
        <div markdown="1"> </div>    

    __Implicit Assumptions in a Coordinate System:__  
    * Direction of each _basis vector_ our vector is scaling
    * The unit of _distance_  


18. **Eigenstuff:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents118}  

    * [**Computing the Eigenvalues/vectors Intuition**](https://www.youtube.com/embed/PFDu9oVAE-g?start=322){: value="show" onclick="iframePopA(event)"}
    <a href="https://www.youtube.com/embed/PFDu9oVAE-g?start=322"></a>
        <div markdown="1"> </div>    

    * [**Diagonalization**](https://www.youtube.com/embed/PFDu9oVAE-g?start=881){: value="show" onclick="iframePopA(event)"}
    <a href="https://www.youtube.com/embed/PFDu9oVAE-g?start=881"></a>
        <div markdown="1"> </div>    


    __Notes:__  
    * Complex Eigenvalues, generally, correspond to some kind of rotation in the transformation/matrix (think, multiplication by $$i$$ in $$\mathbb{C}$$ is a $$90^{\deg}$$ rotation).  
    * For a __diagonal matrix__, all the *__basis vectors__* are *__eigenvectors__* and the *__diagonal entries__* are their *__eigenvalues__*.  

<!-- 19. **The:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents119}  

20. **The:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents120}  

21. **The:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents121}  

22. **The:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents122}  

23. **The:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents123}  

24. **The:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents124}  

25. **The:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents125}  

26. **The:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents126}  

27. **The:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents127}  

28. **The:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents128}  
29. **The:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents129}  
30. **The:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents130}  
31. **The:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents131}  
32. **The:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents132}  
33. **The:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents133}  
34. **The:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents134}  
35. **The:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents135}   -->

