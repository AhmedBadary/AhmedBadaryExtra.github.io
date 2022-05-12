---
layout: NotesPage
title: TensorFlow 
permalink: /work_files/research/math/calc/var_calc
prevLink: /work_files/research/math/calc.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Calculus of Variations](#content1)
  {: .TOC1}
<!--   * [SECOND](#content2)
  {: .TOC2}
  * [THIRD](#content3)
  {: .TOC3} -->
</div>

***
***

## Calculus of Variations
{: #content1}

1. **Calculus of Variations:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  


22. **Functional:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents122}  
    A __Functional__ 
    <br>

2. **Functional Derivative:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    The __Functional Derivative__ relates a change in a functional to a change in a function on which the functional depends.  
    In an integral $$L$$ of a functional, if a function $$f$$ is varied by adding to it another function $$\delta f$$ that is arbitrarily small, and the resulting integrand is expanded in powers of $$\delta f,$$ the coefficient of $$\delta$$ in the first order term is called the __functional derivative__.  
    Consider the __functional__  
    <p>$$J[f]=\int_{a}^{b} L\left[x, f(x), f^{\prime}(x)\right] d x$$</p>  
    where $$f^{\prime}(x) \equiv d f / d x .$$ If is varied by adding to it a function $$\delta f,$$ and the resulting integrand $$L\left(x, f+\delta f, f^{\prime}+\delta f^{\prime}\right)$$ is expanded in  powers of  $$\delta f$$, then the change in the value of $$ J$$ to first order in $$\delta f$$ can be expressed as follows:  
    <p>$$\delta J=\int_{a}^{b} \frac{\delta J}{\delta f(x)} \delta f(x) d x$$</p>  
    The coefficient of $$\delta f(x),$$ denoted as $$\delta J / \delta f(x),$$ is called the functional derivative of $$J$$ with respect to $$f$$ at the point $$x$$.  
    The functional derivative is the left hand side of the __Euler-Lagrange equation__:  
    <p>$$\frac{\delta J}{\delta f(x)}=\frac{\partial L}{\partial f}-\frac{d}{d x} \frac{\partial L}{\partial f^{\prime}}$$</p>  


    __Formal Description:__{: style="color: red"}  
    The definition of a functional derivative may be made more mathematically precise and formal by defining the space of functions more carefully:  
    {: #lst-p}
    * __Banach Space:__ the functional derivative is the <span>Fréchet derivative</span>{: style="color: goldenrod"}  
    * __Hilbert Space:__ (Hilbert is special case of Banach) <span>Fréchet derivative</span>{: style="color: goldenrod"}  
    * __General *Locally Convex* Spaces__: the functional derivative is the <span>Gateaux derivative</span>{: style="color: goldenrod"}  


    __Properties:__{: style="color: red"}  
    {: #lst-p}
    * __Linearity__:  
        <p>$$\frac{\delta(\lambda F+\mu G)[\rho]}{\delta \rho(x)}=\lambda \frac{\delta F[\rho]}{\delta \rho(x)}+\mu \frac{\delta G[\rho]}{\delta \rho(x)}$$</p>  
        where $$\lambda, \mu$$ are constants.  
    * __Product Rule__:  
        <p>$$\frac{\delta(F G)[\rho]}{\delta \rho(x)}=\frac{\delta F[\rho]}{\delta \rho(x)} G[\rho]+F[\rho] \frac{\delta G[\rho]}{\delta \rho(x)}$$</p>  
    * __Chain Rule__:  
        * If $$F$$ is a functional and $$G$$ another functional:  
            <p>$$\frac{\delta F[G[\rho]]}{\delta \rho(y)}=\int d x \frac{\delta F[G]}{\delta G(x)}_ {G=G[\rho]} \cdot \frac{\delta G[\rho](x)}{\delta \rho(y)}$$</p>  
        * If $$G$$ is an ordinary differentiable function (local functional) $$g,$$ then this reduces to:  
            <p>$$\frac{\delta F[g(\rho)]}{\delta \rho(y)}=\frac{\delta F[g(\rho)]}{\delta g[\rho(y)]} \frac{d g(\rho)}{d \rho(y)}$$</p>  

    __Formula for Determining the Functional Derivative:__{: style="color: red"}  
    We present a formula to determine functional derivatives for a common class of functionals that can be written as the integral of a function and its derivatives:  
    Given a functional $$F[\rho]=\int f(\boldsymbol{r}, \rho(\boldsymbol{r}), \nabla \rho(\boldsymbol{r})) d \boldsymbol{r}$$ and a function $$\phi(\boldsymbol{r})$$ that vanishes on the boundary of the region of integration, the functional derivative is:  
    <p>$$\frac{\delta F}{\delta \rho(\boldsymbol{r})}=\frac{\partial f}{\partial \rho}-\nabla \cdot \frac{\partial f}{\partial \nabla \rho}$$</p>  
    where $$\rho=\rho(\boldsymbol{r})$$ and $$f=f(\boldsymbol{r}, \rho, \nabla \rho)$$.  

    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * [Functional Derivative (wiki)](https://en.wikipedia.org/wiki/Functional_derivative)  
    <br>

3. **Euler Lagrange Equation:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    
    __Generalization to Manifolds:__{: style="color: red"}  
    <button>Manifold Equations</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/T9qXN12UsjttUJnt3pNYnGOTiTca4dXex-BD2vLpRLk.original.fullsize.png){: width="100%" hidden=""}  


    __Beltrami Identity:__{: style="color: red"}  
    __Beltrami Identity__ is a special case of the Euler Lagrange Equation where $$\partial L / \partial x=0$$, defined as:  
    <p>$$L-f^{\prime} \frac{\partial L}{\partial f^{\prime}}=C$$</p>  
    where $$C$$ is a constant.  

    It is applied to many problems where the condition is satisfied like the __Brachistochrone problem__.  

    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * [Functional Derivative (wiki)](https://en.wikipedia.org/wiki/Functional_derivative)  
    <br>


<!-- 3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18}

***

## SECOND
{: #content2}

1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}

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