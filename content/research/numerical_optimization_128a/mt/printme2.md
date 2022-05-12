---
layout: editable
permalink: /work_files/school/128a/mt/printme2
---


**2.1/**{: style="font-size: 250%; color: red; font: italic bold 50px/70px Georgia, serif"} 

____________________
***

## Bisection Technique
{: #content1}

1. **What?**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents11}
    <xmp>
    </xmp>

0. **Why?**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents10}
    <xmp>
    </xmp>

2. **Method:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents12} \\
    <xmp>
    </xmp>

3. **Algorithm:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents13} \\
    <xmp>
    </xmp>

4. **Drawbacks:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents14} \\
    <xmp>

    </xmp>


5. **Stopping Criterions:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents15} \\
    <xmp>

    </xmp>
    > **The best criterion is:**

6. **Convergence:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents16} \\
    <xmp>

    </xmp>
    > **It:**  

7. **Rate of Convergence \ Error Bound:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents17} \\
    <xmp>

    </xmp>

8. **The problem of Percision:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents18} \\
    We use, \\
    <xmp>

    </xmp>

9. **The Signum Function:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents19} \\
    We use, \\
    <xmp>

    </xmp>

***
***


**2.2/**{: style="font-size: 250%; color: red; font: italic bold 50px/70px Georgia, serif"} 

____________________
***

## Fixed-Point Problems
{: #content1}

1. **Fixed Point:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents11} 
    <xmp>

    </xmp>

2. **Root-finding problems and Fixed-point problems:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents12} \\
    > Root Finding and Fixed-point problems are  
    <xmp>
    </xmp>
    <xmp>
    </xmp>

3. **Why?:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents13} \\
    <xmp>

    </xmp>

4. **Existence and Uniqueness of a Fixed Point.:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents14} \\
    <xmp>

    </xmp>

***

## Fixed-Point Iteration
{: #content2}

1. **Approximating Fixed-Points:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents21} \\
    <xmp>
    </xmp>
2. **Algorithm:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents22} \\
    <xmp>
    </xmp>       
    <xmp>
    </xmp>

3. **Convergence:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents23}
    * **Fixed-Point Theorem:** \\
        <xmp>
        </xmp>
    * **Error bound in using $$p_n$$ for $$p$$:** \\
        <xmp>
        </xmp>

        > Notice: \\
            <xmp>
            </xmp>
4. **Using Fixed-Points:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents24} \\
    > **Question**: $$ \ \ \ \ \ $$ 
        <xmp>
        </xmp>
    > **Answer**:     
        <xmp>
        </xmp>

5. **Newton's Method as a Fixed-Point Problem:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents25} \\
    <xmp>
    </xmp>
    <xmp>
    </xmp>

***
***


**2.3/**{: style="font-size: 250%; color: red; font: italic bold 50px/70px Georgia, serif"} 

____________________
***

## Newton’s Method
{: #content1}

1. **What?:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents11} 
    * **Newton’s (or the Newton-Raphson) method is**:
        <xmp>
        </xmp>
    *   <br /> 
        <xmp>
        </xmp>
    *   <br /> 
        <xmp>
        </xmp>

2. **Derivation:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents12} \\
    <xmp>
    </xmp>
    <xmp>
    </xmp>
    <xmp>
    </xmp>
3. **Algorithm:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents13} \\
    <xmp>
    </xmp>
    <xmp>
    </xmp>
    <xmp>
    </xmp>

4. **Stopping Criterions:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents14} \\
    <xmp>
    </xmp>

***

## Convergence using Newton’s Method
{: #content2}

1. **Convergence Theorem:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents21} \\
    **Theorem:**  \\
    <xmp>
    </xmp>
    > The crucial assumption is
        <xmp>
        </xmp>

    <br>

    > Theorem 2.6 states that, \\
    > (1)  \\
        <xmp>
        </xmp>
    > (2) 
        <xmp>
        </xmp>

## The Secant Method
{: #content3}

1. **What?**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents31} \\
    In Newton's Method \\
    We approximate $$f'( p_n−1)$$ as:\\
        <xmp>
        </xmp>
    To produce: \\
        <xmp>
        </xmp>

2. **Why?**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents32} \\
    > **$$\ \ \ \ \ \ \ \ \ $$**: 
        <xmp>
        </xmp>
    >   > Frequently, 
            <xmp>
            </xmp>

    > Note: 
        <xmp>
        </xmp>

3. **Algorithm:**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents33} \\
    <xmp>
    </xmp>
    <xmp>
    </xmp>


4. **Convergence Speed:**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents34} \\
    <xmp>
    </xmp>

***

## The Method of False Position
{: #content4}

1. **What?**{: style="color: SteelBlue  "}{: .bodyContents4 #bodyContents41} \\
    <xmp>
    </xmp>

2. **Why?**{: style="color: SteelBlue  "}{: .bodyContents4 #bodyContents42} \\
    <xmp>
    </xmp>
3. **Method:**{: style="color: SteelBlue  "}{: .bodyContents4 #bodyContents43} \\
    <xmp>
    </xmp>
    <xmp>
    </xmp>
4. **Algorithm:**{: style="color: SteelBlue  "}{: .bodyContents4 #bodyContents44} \\
    <xmp>
    </xmp>
    <xmp>
    </xmp>

***
***


**2.4/**{: style="font-size: 250%; color: red; font: italic bold 50px/70px Georgia, serif"} 

____________________
***

## Order of Convergence 
{: #content1}

1. **Order of Convergence:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents11} \\
    <xmp>
    </xmp>
2. **Important, Two cases of order:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents12} \\
    <xmp>
    </xmp>
3. **An arbitrary technique that generates a convergent sequences does so only linearly:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents13} \\
    <xmp>
    </xmp>
    > Theorem 2.8 implies 
        <xmp> </xmp>

4. **Conditions to ensure Quadratic Convergence:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents14} \\
    <xmp>
    </xmp>

5. **Theorems 2.8 and 2.9 imply:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents15} \\
    (i)\\
        <xmp>
        </xmp>
    (ii)\\
        <xmp>
        </xmp>

5. **Newtons' Method Convergence Rate:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents15} \\
    <xmp>
    </xmp>
    <xmp>
    </xmp>

## Multiple Roots 
{: #content2}

1. **Problem:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents21} \\
    <xmp>
    </xmp>

2. **Zeros and their Multiplicity:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents22} \\
    <xmp>

    </xmp>

3. **Identifying Simple Zeros:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents23} \\
    * **Theorem:**  
    <xmp>
    </xmp>
    * **Generalization of Theorem 2.11:**
        <xmp>
        </xmp>

        > The result in Theorem 2.12 implies 
            <xmp>

            </xmp>

4. **Why Simple Zeros:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents24} \\
    <xmp>
    </xmp>
    > Example:
        <xmp>
        </xmp>


5. **Handling the problem of multiple roots:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents25} \\
    * We $$  \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$  
    * We define $$\ \ \ \ \ \ \ \ \ \ $$ as: \\
        <xmp>
        </xmp>

    * **Derivation:**  
        <xmp>
        </xmp>

    * **Properties:**
        * 
            <xmp>
            </xmp>
        * 
            <xmp>
            </xmp>
        * 
            <xmp>
            </xmp>
        *   
            <xmp>
            </xmp>

***
***


**2.5/**{: style="font-size: 250%; color: red; font: italic bold 50px/70px Georgia, serif"} 

____________________
***

## Aitken’s $$ \Delta^2 $$ Method 
{: #content1}

1. **What?**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents11} \\
    <xmp>
    </xmp>

2. **Why?**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents12} \\
    <xmp>
    </xmp>

0. **Derivation:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents100} \\
    <xmp>


    </xmp>

3. **Del [Forward Difference]:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents13} \\
    <xmp>
    </xmp>

4. **$$\hat{p}_n$$ [Formula]:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents14} \\
    <xmp>
    </xmp>

5. **Generating the Sequence [Formula]:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents15} \\
    <xmp>
    </xmp>


## Steffensen’s Method
{: #content2}

1. **What?:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents21} 
    <xmp>

    </xmp>

2. **Zeros and their Multiplicity:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents22} \\
    <xmp>
    </xmp>

3. **Difference from Aitken's method:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents23} \\
    * **Aitken's method:**  
        <xmp>
        </xmp>
    * **Steffensen’s method:**  
        <xmp>

        </xmp>

    > Notice \\
        <xmp>
        </xmp>

4. **Algorithm:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents24} \\
    <xmp>
    </xmp>

5. **Convergance of Steffensen’s Method:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents25} \\
    <xmp>
    </xmp>

***
***


**2.6/**{: style="font-size: 250%; color: red; font: italic bold 50px/70px Georgia, serif"} 

____________________
***

## Algebraic Polynomials
{: #content1}

1. **Fundamental Theorem of Algebra:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents11} \\
    <xmp>
    </xmp>
2. **Existance of Roots:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents12} \\
    <xmp>
    </xmp>
3. **Polynomial Equivalence:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents13} \\
    <xmp>
    </xmp>
    > This result implies 
        <xmp>
        </xmp>


## Horner’s Method
{: #content2}

1. **What?**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents21} \\
    <xmp>

    </xmp>

2. **Why?**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents22} \\
    <xmp>
    </xmp>

3. **Horner's Method:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents23} \\
    <xmp>
    </xmp>    
    <xmp>
    </xmp>

4. **Algorithm:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents24} \\
    <xmp>
    </xmp>
    <xmp>

    </xmp>

5. **Horner's Derivatives:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents25} \\
    <xmp>
    </xmp>

6. **Deflation:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents26} \\
    <xmp>
    </xmp>

5. **MatLab Implementation:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents25} \\
    <xmp>
    </xmp>

## Complex Zeros: Müller’s Method
{: #content3}

1. **What?**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents31} \\
    * **It is a:** 
        <xmp>

        </xmp>
    * Müller’s method uses
        <xmp>

        </xmp>


2. **Why?**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents32} \\
    1. **First:**  
        <br>
    2. **Second:**  
        <br>
        > If the initial approximation is a real number, 

3. **Complex Roots:**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents33} \\
    <xmp>
    </xmp>

4. **Algorithm:**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents34} \\
    <xmp>


    </xmp>
    
5. **Calculations and Evaluations:**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents35} \\
    **Müller’s method can:**  
        <xmp>
        </xmp>
