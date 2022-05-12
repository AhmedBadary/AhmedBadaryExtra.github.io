---
layout: NotesPage
title: Topology and Smooth Manifolds
permalink: /work_files/research/math/manifolds
prevLink: /work_files/research/dl/cv.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Introduction and Definitions](#content1)
  {: .TOC1}
  * [Point-Set Topology](#content2)
  {: .TOC2}
  * [Manifolds](#content3)
  {: .TOC3}
</div>

***
***

## Introduction and Definitions
{: #content1}

1. **Topology:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    :   is a mathematical field concerned with the properties of space that are preserved under continuous deformations, such as stretching, crumpling and bending, but not tearing or gluing

2. **Topological Space:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    :   is defined as a set of points $$\mathbf{X}$$, along with a set of neighbourhoods (sub-sets) $$\mathbf{T}$$ for each point, satisfying the following set of axioms relating points and neighbourhoods:  
        * __$$\mathbf{T}$$ is the Open Sets__:     
            1. The __Empty Set__ $$\emptyset$$ is in $$\mathbf{T}$$
            2. $$\mathbf{X}$$ is in $$\mathbf{T}$$
            3. The __Intersection of a finite number of Sets__ in $$\mathbf{T}$$ is, also, in $$\mathbf{T}$$
            4. The __Union of an arbitrary number of Sets__ in $$\mathbf{T}$$ is, also, in $$\mathbf{T}$$  
        * __$$\mathbf{T}$$ is the Closed Sets__:     
            1. The __Empty Set__ $$\emptyset$$ is in $$\mathbf{T}$$
            2. $$\mathbf{X}$$ is in $$\mathbf{T}$$
            3. The __Intersection of an arbitrary number of Sets__ in $$\mathbf{T}$$ is, also, in $$\mathbf{T}$$
            4. The __Union of a finite number of Sets__ in $$\mathbf{T}$$ is, also, in $$\mathbf{T}$$

3. **Homeomorphism:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    :   Intuitively, a __Homeomorphism__ or __Topological Isomorphism__ or __bi-continuous Function__ is a continuous function between topological spaces that has a continuous inverse function.  
    :   Mathematically, a function $${\displaystyle f:X\to Y}$$ between two topological spaces $${\displaystyle (X,{\mathcal {T}}_{X})}$$ and $${\displaystyle (Y,{\mathcal {T}}_{Y})}$$ is called a __Homeomorphism__ if it has the following properties:  
        * $$f$$ is a bijection (one-to-one and onto)  
        * $$f$$ is continuous
        * the inverse function $${\displaystyle f^{-1}}$$ is continuous ($${\displaystyle f}$$ is an open mapping).  
    :   > i.e. There exists a __continuous map__ with a __continuous inverse__

4. **Maps and Spaces:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    :   | __Map__ | __Space__ | __Preserved Property__ |  
        | Linear Map | Vector Space | Linear Structure: $$f(aw+v) = af(w)+f(v)$$ |  
        | Group Homomorphism | Group | Group Structure: $$f(x \ast y) = f(x) \ast f(y)$$ |  
        | Continuous Map | Topological Space | Openness/Closeness: $$f^{-1}(\{\text{open}\}) \text{ is open}$$ |  
        | _Smooth Map_ | _Topological Space_ | 

5. **Smooth Maps:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  
    :   
        * __Continuous__: 
        * __Unique Limits__:       

6. **Hausdorff:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}  
    :   

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}  
    :   

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18}  
    :   

***

## Point-Set Topology
{: #content2}

1. **Open Set:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents21} 
    :   A set $$\chi \subseteq \mathbf{R}^n$$ is said to be open if for any point $$x \in \chi$$ there exist a ball centered in $$x$$ which is contained in $$\chi$$. 
    :   Precisely, for any $$x \in \mathbf{R}^n$$ and $$\epsilon > 0$$ define the Euclidean ball of radius $$r$$ centered at $$x$$:
    :   $$B_\epsilon(x) = {z : \|z − x\|_2 < \epsilon}$$
    :   Then, $$\chi \subseteq \mathbf{R}^n$$ is open if
    :   $$\forall x \: \epsilon \: \chi, \:\: \exists \epsilon > 0 : B_\epsilon(x) \subset \chi .$$
    :   **Equivalently**,
    :   * A set $$\chi \subseteq \mathbf{R}^n$$ is open if and only if $$\chi = int\; \chi$$.
    :   * An open set does not contain any of its boundary points.
    :   * A closed set contains all of its boundary points. 
    :   * Unions and intersections of open (resp. closed) sets are open (resp. closed).

2. **Closed Set:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents22} 
    :   A set $$\chi \subseteq \mathbf{R}^n$$ is said to be closed if its complement $$ \mathbf{R}^n \text{ \ } \chi$$ is open.

3. **Interior of a Set:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents23}
    :   The interior of a set $$\chi \subseteq \mathbf{R}^n$$ is defined as 
    :   $$int\: \chi = \{z \in \chi : B_\epsilon(z) \subseteq \chi, \:\: \text{for some } \epsilon > 0 \}$$

4. **Closure of a Set:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents24}
    :   The closure of a set $$\chi \subseteq \mathbf{R}^n$$ is defined as
    :   $$\bar{\chi} = \{z ∈ \mathbf{R}^n : \: z = \lim_{k\to\infty} x_k, \: x_k \in \chi , \: \forall k\},$$  
    :   > i.e., the closure of $$\chi$$ is the set of limits of sequences in $$\chi$$.

5. **Boundary of a Set:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents25}
    :   The boundary of X is defined as
    :   $$\partial \chi = \bar{\chi} \text{ \ }  int\: \chi$$

6. **Bounded Set:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents26}
    :   A set $$\chi \subseteq \mathbf{R}^n$$ is said to be bounded if it is contained in a ball of finite radius, that is if there exist $$x \in \mathbf{R}^n$$ and $$r > 0$$ such that $$\chi \subseteq B_r(x)$$.

7. **Compact Set:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents27}
    :   A set $$\chi \subseteq \mathbf{R}^n$$ is compact $$\iff$$ it is **Closed** and **Bounded**.

8. **Relative Interior [$$\operatorname{relint}$$]:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents28}
    :   We define the relative interior of the set $$\chi$$, denoted $$\operatorname{relint} \chi$$, as its interior relative to $$\operatorname{aff} C$$:
    :   $$\operatorname{relint} \chi = \{x \in \chi : \: B(x, r) \cap \operatorname{aff} \chi \subseteq \chi \text{ for some } r > 0\},$$
    :   where $$B(x, r) = \{y : ky − xk \leq r\}$$, the ball of radius $$r$$ and center $$x$$ in the norm $$\| · \|$$.

9. **Relative Boundary:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents29}
    :   We can then define the relative boundary of a set $$\chi$$ as $$\mathbf{cl}  \chi \text{ \ } \operatorname{relint} \chi,$$ where $$\mathbf{cl} \chi$$ is the closure of $$\chi$$.

***

## Manifolds
{: #content3}

1. **Manifold:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}  
    :   is a topological space that locally resembles Euclidean space near each point  
        > i.e. around every point, there is a neighborhood that is topologically the same as the open unit ball in $$\mathbb{R}^n$$  
    :   

2. **Smooth Manifold:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}  
    :   A topological space $$M$$ is called a __$$n$$-dimensional smooth manifold__ if:  
        * Is is __Hausdorff__
        * It is __Second-Countable__
        * It comes with a family $$\{(U_\alpha, \phi_\alpha)\}$$ with:  
            * __Open sets__ $$U_\alpha \subset_\text{open} M$$ 
            * __Homeomorphisms__ $$\phi_\alpha : U_\alpha \rightarrow \mathbb{R}^n$$   
    such that $${\displaystyle M = \bigcup_\alpha U_\alpha}$$  
    and given $${\displaystyle U_\alpha \cap U_\beta \neq \emptyset}$$ the map $$\phi_\beta \circ \phi_\alpha^{-1}$$ is smooth

<!-- 3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}  
    :   

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents34}  
    :   

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents35}  
    :   

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents36}  
    :   

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents37}  
    :   

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents38}  
    :   
 -->