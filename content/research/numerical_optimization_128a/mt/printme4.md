---
layout: editable
permalink: /work_files/school/128a/mt/printme4
---

**4.1/**{: style="font-size: 250%; color: red; font: italic bold 50px/70px Georgia, serif"}  

____________________
***


## The derivative
{: #content1}

1. **Derivative:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents11} \\
    <xmp>
    </xmp>

2. **The forward/backward difference formula:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents12} \\
    > Derivative formulat [at $$x = x_0$$]
        <xmp>
        </xmp>
    > This formula is known as the forward-difference formula if  \\
    > and the backward-difference formula if 


    * Derivation:  
        <xmp>




        </xmp>


    > **Error Bound:**
        <xmp>
        </xmp>

3. **The $$(n + 1)$$-point formula to approximate $$f'(x_j)$$:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13} \\
    <xmp>
    </xmp>
    * Derivation:  
        <xmp>

        </xmp>

4. **Three-point Formula:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents14} \\
    <xmp>


    </xmp>
    for each $$j = 0, 1, 2$$, where the notation $$\zeta_j$$ indicates that this point depends on $$x_j$$.
    * Derivation:  
        <xmp>





        </xmp>

***

## Three-Point Formulas
{: #content2}

1. **Equally Spaced nodes:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents21} \\
    > The formulas from Eq. (4.3) become especially useful if 
        $$x_1  =$$   \\
        $$x_2  =$$   

2. **Three-Point Endpoint Formula:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents22} \\
    <xmp>

    </xmp>
    > The approximation in Eq. (4.4) is useful at  

    > **Because:**  

    > **Errors:** the errors in both Eq. (4.4) and Eq. (4.5) are 
        <xmp> </xmp>

    > **On the interval:**  

3. **Three-Point Midpoint Formula:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents23} \\
    <xmp>
    </xmp>
    > **Errors:** 
    >   
    >   > This is because Eq. (4.5) uses data on $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$ and Eq. (4.4) uses data $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$  
    >   > Note also that f needs to be evaluated at $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$  in 
          Eq. (4.5), whereas in Eq. (4.4) it $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$  


    > **On the interval:**  

***

## Five-Point Formulas
{: #content3}

1. **What?**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents31} \\
    <xmp> </xmp>

2. **Why?**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents32} \\
    <xmp> </xmp>

3. **Error:**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents33} \\
    The error term for these formulas is 

4. **Five-Point Midpoint Formula:**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents34} \\
    <xmp>

    </xmp>

    > **Used** for approximation at  

    > **On the interval:**  

5. **Five-Point Endpoint Formula:**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents35} \\
    <xmp>
    </xmp>

    > **Used** for approximation at 

    > ***Left-endpoint** approximations* are found using this formula with $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$  and ***right-endpoint** approximations* with $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$.  

    > The five-point endpoint formula is particularly useful for $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$   

    > **On the interval:**   

***

## Approximating Higher Derivatives
{: #content4}

1. **Approximations to Second Derivatives:**{: style="color: SteelBlue  "}{: .bodyContents4 #bodyContents41} \\
    <xmp>

    </xmp>
    > **On the interval:**  

    * **Derivation:**  
        <xmp>



        </xmp>

        * **Why does the error bound change?**  
            <xmp> </xmp>

2. **Second Derivative Midpoint Formula:**{: style="color: SteelBlue  "}{: .bodyContents4 #bodyContents42} \\
    <xmp>

    </xmp>
 
    > **On the interval:**  

    * **Derivation:**  
        <xmp>


        </xmp>


    > **Error Bound:** If $$f^{(4)}$$ is $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$  on $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$  it is $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$ , and the approximation is $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$ . 

***

## Round-Off Error Instability
{: #content5}

1. **Form of Error:**{: style="color: SteelBlue  "}{: .bodyContents5 #bodyContents51} \\
    * We assume that our computations actually use the values $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$ $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$   
    * which are related to the true values $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$ $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$ 
        by:  
    > $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$   &  
    > $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$ $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$ 

2. **The total error:**{: style="color: SteelBlue  "}{: .bodyContents5 #bodyContents52} \\
    <xmp>
    </xmp>
    > It is due to $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$   

3. **Error Bound:**{: style="color: SteelBlue  "}{: .bodyContents5 #bodyContents53} \\
    * **ASSUMPTION:**  $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$ $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$ 

    * **ERROR:** 
        <xmp>
        </xmp> 

4. **Reducing Truncation Error:**{: style="color: SteelBlue  "}{: .bodyContents5 #bodyContents54} \\
    * **How?** $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$ $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$ 
    * **Effect of reducing $$h$$:** 
        <xmp>
        </xmp>
5. **Conclusion:**{: style="color: SteelBlue  "}{: .bodyContents5 #bodyContents55} \\
    <xmp>


    </xmp>

***
***

**4.2/**{: style="font-size: 250%; color: red; font: italic bold 50px/70px Georgia, serif"}  

____________________
***


## Extrapolation
{: #content1}

1. **What?**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents11} \\
    * Extrapolation is used to 
        <xmp>
        </xmp>
    * Extrapolation can be applied whenever 
        <xmp>
        </xmp>
    * Suppose that for each number $$h \neq 0$$ we have a formula $$N_1(h)$$ that approximates an
    unknown constant $$ \ \ \ \ \ \ \ \ $$, and that the truncation error involved with the approximation has the
    form,  
    $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$ 
    * The **truncation error** is $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$  
        where,  
        (1)  
        (2)  

    and, in general,  
    $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$ 
    * The object of extrapolation is 
        <xmp>

        </xmp>

2. **Why?**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents12} \\
    1.  
        <xmp>

        </xmp>

    2.  
        <xmp>

        </xmp>



3. **The $$\mathcal{O}(h)$$ formula for approximating $$M$$:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents13} \\
    > **The First Formula:**  
    <xmp>

    </xmp>


    > **The Second Formula:**  
    <xmp>

    </xmp>
 

4. **The $$\mathcal{O}(h^2)$$ approximation formula for M:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents14} \\
    <xmp>


    </xmp>

    * **Derivation:**  
        <xmp>



        </xmp>


5. **When to apply Extrapolation?**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents15} \\
    (1)  
    <xmp>
    </xmp>
    (2)  
    <xmp>
    </xmp>

6. **The $$\mathcal{O}(h^4)$$ formula for approximating $$M$$:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents16} \\
    <xmp>

    </xmp>


7. **The $$\mathcal{O}(h^6)$$ formula for approximating $$M$$:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents17} \\
    <xmp>

    </xmp>

8. **The $$\mathcal{O}(h^{2j})$$ formula for approximating $$M$$:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents18} \\
    <xmp>


    </xmp>

    * **Derivation:**  
        <xmp>



        </xmp>


9. **The Order the Approximations Generated:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents19} \\
    <xmp>


    </xmp>

9. **How to actually calculate a derivative using the Extrapolation formula:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents1000} \\
    <xmp>

    </xmp>

***

## Deriving n-point Formulas with Extrapolation
{: #content2}

1. **Deriving Five-point Formula:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents21} \\
    <xmp>

    </xmp>

***
***

**4.3/**{: style="font-size: 250%; color: red; font: italic bold 50px/70px Georgia, serif"}  

____________________
***

## Numerical Quadrature
{: #content1}

1. **What?**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents11} 
    <xmp> </xmp>

2. **How?**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents12} 
    <xmp> </xmp>

3. **Based on:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents13} 
    <xmp> </xmp>

4. **Method:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents14} 
    <xmp>


    </xmp>

    * **Derivation:**  
        <xmp>





        </xmp>


5. **The Quadrature Formula:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents15} \\
    <xmp>
    </xmp>


6. **The Error:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents16} \\
    <xmp>
    </xmp>

***

## The Trapezoidal Rule
{: #content2}

1. **What?**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents21}
    <xmp>

    </xmp>


1. **Precision**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents200}
    <xmp>
    </xmp>

2. **The Trapezoidal Rule:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents22} \\
    <xmp>


    </xmp>

    * **Derivation:**  
        <xmp>


        </xmp>

3. **Error:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents23} \\
    <xmp>

    </xmp>

***

## Simpson’s Rule
{: #content3}

1. **What?**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents31} \\
    <xmp>

    </xmp>

2. **Simpson's Rule:**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents32} \\
    <xmp>

    </xmp>

    * **Derivation:**  
        <xmp>




        </xmp>


1. **Precision**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents200}
    <xmp>
    </xmp>

3. **Error:**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents33} \\
    <xmp>

    </xmp>

***

## Measuring Precision
{: #content4}

1. **What?**{: style="color: SteelBlue  "}{: .bodyContents4 #bodyContents41} \\
    <xmp>

    </xmp>

2. **Precision [degree of accuracy]:**{: style="color: SteelBlue  "}{: .bodyContents4 #bodyContents42} \\
    <xmp>

    </xmp>

3. **Precision of Quadrature Formulas:**{: style="color: SteelBlue  "}{: .bodyContents4 #bodyContents43} \\
    * The degree of precision of a quadrature formula is $$ \mathcal{O}$$
        <xmp>
        </xmp>
    * The Trapezoidal and Simpson’s rules are examples of $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$  
    * **Types of Newton-Cotes formulas:** 
        <xmp> </xmp>
***

## Closed Newton-Cotes Formulas
{: #content5}

1. **What?**{: style="color: SteelBlue  "}{: .bodyContents5 #bodyContents51} \\
    <xmp>
    </xmp>

    * **It is called closed because:**  
        <xmp>
        </xmp>

2. **Form of the Formula:**{: style="color: SteelBlue  "}{: .bodyContents5 #bodyContents52} \\
    <xmp>

    </xmp>

    > where,  
        <xmp>
        </xmp>

3. **The Error Analysis:**{: style="color: SteelBlue  "}{: .bodyContents5 #bodyContents53} \\
    <xmp>

    </xmp>


4. **Degree of Preceision:**{: style="color: SteelBlue  "}{: .bodyContents5 #bodyContents54} \\
    * **Even-n:** the degree of precision is $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$  
    * **Odd-n:** the degree of precision is 

5. **Closed Form Formulas:**{: style="color: SteelBlue  "}{: .bodyContents5 #bodyContents55} \\
    * **$$n = 1$$: $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$  rule**  
        <xmp>
        
        </xmp>
    * **$$n = 2$$: $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$  rule**   
        <xmp>
        
        </xmp>
    * **$$n = 3$$: $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$  rule**   
        <xmp>
        
        </xmp>
    * **n = 4:**  
        <xmp>

        </xmp>

***

## Open Newton-Cotes Formulas
{: #content6}

1. **What?**{: style="color: SteelBlue  "}{: .bodyContents6 #bodyContents61} \\
    * They $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$  
    * They use 
        <xmp>
        </xmp>
    * This implies that 
        <xmp>
        </xmp>
    * Open formulas contain $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$ 

2. **Form of the Formula:**{: style="color: SteelBlue  "}{: .bodyContents6 #bodyContents62} \\
    <xmp>

    </xmp>
    > where,  
        <xmp>
        </xmp>

3. **The Error Analysis:**{: style="color: SteelBlue  "}{: .bodyContents6 #bodyContents63} \\
    <xmp>

    </xmp>

4. **Degree of Preceision:**{: style="color: SteelBlue  "}{: .bodyContents6 #bodyContents64} \\
    * **Even-n:** 
    * **Odd-n:** 
5. **Open Form Formulas:**{: style="color: SteelBlue  "}{: .bodyContents6 #bodyContents65} \\
    * **$$n = 0$$:** [PUT NAME HERE]  
        <xmp>
        </xmp>
    * **$$n = 1$$:**   
        <xmp>
        </xmp>
    * **$$n = 2$$:**   
        <xmp>
        </xmp>
    * **n = 3:**  
        <xmp>
        </xmp>


***
***

**4.4/**{: style="font-size: 250%; color: red; font: italic bold 50px/70px Georgia, serif"}  

____________________
***

## Composite Rules
{: #content1}

1. **What?**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents11} \\
    <xmp>
    </xmp>

2. **Why?**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents12} \\
    1.  
        <xmp>
        </xmp>
    2.  
        <xmp>
        </xmp>
    3.  
        <xmp>
        </xmp>

3. **Notice:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents13}
    <xmp>
    </xmp>

***

## Composite Simpson’s rule
{: #content2}

1. **Composite Simpson’s rule:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents21} \\
    <xmp>

    </xmp>

2. **Error in Comoposite Simpson's Rule:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents22} \\
    <xmp>
    </xmp>
    > **Error:**  

3. **Theorem [Rule and Error]:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents23} \\
    <xmp>

    </xmp>

4. **Algorithm:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents24} \\
    <xmp>

    </xmp>

***

## Composite Newton-Cotes Rules
{: #content3}

1. **Composite Trapezoidal rule:**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents31}  
    <xmp>

    </xmp>

2. **Composite Midpoint rule:**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents32}  
    <xmp>

    </xmp>

***

## Round-Off Error Stability
{: #content4}

1. **Stability Property:**{: style="color: SteelBlue  "}{: .bodyContents4 #bodyContents41} \\
    <xmp>

    </xmp>

2. **Proof:**{: style="color: SteelBlue  "}{: .bodyContents4 #bodyContents42} \\
    <xmp>


    </xmp>

***
***

**4.5/**{: style="font-size: 250%; color: red; font: italic bold 50px/70px Georgia, serif"}  

____________________
***

## Main Idea
{: #content1}

1. **What?**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents11}
    <xmp>

    </xmp>

2. **Why?**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents12}
    <xmp>
    </xmp>
3. **Error in Composite Trapezoidal rule:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents13} \\
    <xmp>

    </xmp>
    > This implies that $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$ 

4. **Extrapolation Formula:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents14} \\
    > Extrapolation then is used to produce $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ $$  approximations by  
        <xmp>
        </xmp>

    > and according to this table,  
        <xmp>
        </xmp>

    > Calculate the Romberg table this way:


5. **Algorithm:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents15} \\
    <xmp>




    </xmp> 


***
***

**4.6/**{: style="font-size: 250%; color: red; font: italic bold 50px/70px Georgia, serif"}  

____________________
***

## Main Idea
{: #content1}

1. **What?**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents11}
    :   1.  
            <xmp>
            </xmp>
        2.  
            <xmp>
            </xmp>
2. **Why?**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents12}
    <xmp>
    </xmp>

3. **Approximation Formula:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents13}  
    $$\int_{a}^{b} f(x) dx = $$  
        <xmp>
        </xmp>

    * **Derivation:**  
        <xmp>


        </xmp>

4. **Error Bound:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents14} \\
    * **Error relative to *Composite Approximations*:**  
        <xmp>
        </xmp>
    * **Error relative to *True Value*:**  
        <xmp>
        </xmp>

    * **ERROR DERIVATION:**  
        <xmp>


        </xmp> 

    > This implies 
        <xmp>
        </xmp>

5. **Procedure:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents15} \\
    > When the approximations in (4.38) 
        <xmp>
        </xmp>
    
    > Then we use the error estimation procedure to 
        <xmp>
        </xmp>  

    > If the approximation on one of the subintervals fails to be within the tolerance $$\ \ \ \ \ \ \ \ $$, then
        <xmp>
        </xmp>

7. **Algorithm:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents17} \\
    <xmp>


    </xmp>

8. **Derivation:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents18} \\
    <xmp>


    </xmp>

***
***

**4.7/**{: style="font-size: 250%; color: red; font: italic bold 50px/70px Georgia, serif"}  

____________________
***

## Main Idea
{: #content1}

1. **What?**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents11} 
    :   1. 
            <xmp>
            </xmp>
        2.  
            <xmp>

            </xmp>

        3.  
            <xmp>

            </xmp>  

    :   * 
        > **To Measure Accuracy:** 
            <xmp>

            </xmp>

    :   *  
        > The **Coefficients** $$c_1, c_2, ... , c_n$$ in the approximation formula are $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$ ,   
        and,   
        The **Nodes** $$x_1, x_2, ... , x_n$$ are restricted by/to  $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$  
        This gives,  
        **The number of Parameters** to choose is $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$ 

    :   *  
        > If the coefficients of a polynomial are considered parameters, 
            <xmp>
            </xmp>  
        > This, then, is 
            <xmp>
            </xmp>

2. **Why?**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents12} 
    <xmp>
    </xmp>

***

## Legendre Polynomials
{: #content2}

1. **What?**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents21} 
    <xmp>
    </xmp>

9. **Why?**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents29} 
    <xmp>

    </xmp>

2. **Properties:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents22} \\
    1.  
    2.  
    3. The roots of these polynomials are: 
        *   
        *   
        *   
        *   
        *   

3. **The first Legendre Polynomials:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents23} \\
    $$
    P_0(x) = \ \ \ \ \ , \ \ \ \ \ \ \ \ \ \ \ \ \ \  P_1(x) =  \ \ \, \ \ \ \ \ \ \ \ \ \ \ \ \ \  P_2(x) = \ \ \ \ \ \ \ \ \ \ ,
    $$  
    $$
    P_3(x) = \ \ \ \ \ \ \ \  ,\ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \   P_4(x) = \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ 
    $$
4. **Determining the nodes:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents24} \\
    <xmp>

    </xmp>

    * **PROOF:**  
        <xmp>

        </xmp>

    > The nodes $$x_1, x_2, ... , x_n$$ needed to
        <xmp>
        </xmp>

***

## Gaussian Quadrature on Arbitrary Intervals
{: #content3}

1. **What?**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents31} \\
    <xmp>
    </xmp>

2. **The Change of Variables:**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents32} \\
    <xmp>
    </xmp>

3. **Gaussian quadrature [arbitrary interval]:**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents33} \\
    <xmp>
    
    </xmp>


***
***

**4.8/**{: style="font-size: 250%; color: red; font: italic bold 50px/70px Georgia, serif"}  

____________________
***

## Approximating Double Integral
{: #content1}

1. **What?**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents11} 
    <xmp>
    </xmp>

2. **Why?**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents12}
    <xmp>
    </xmp>

3. **Comoposite Trapezoidal Rule for Double Integral:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents13} \\
    $$ \ \  \iint_R f(x,y) \,dA \  = $$ $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$  
    <xmp>

    </xmp>

    * **DERIVATION:**  
        <xmp>


        </xmp>

4. **Comoposite Simpsons' Rule for Double Integral:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents14} \\
    * **Rule:**  
        <xmp>

        </xmp>

    * **Error:**  
        <xmp>

        </xmp>

    * **Derivation:**  
        <xmp>


        </xmp>

***

## Gaussian Quadrature for Double Integral Approximation
{: #content2}

1. **What?**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents21}
    <xmp>

    </xmp>

2. **Why?**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents22}
    <xmp>
    </xmp>
3. **Example:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents23} \\
    <xmp>

    </xmp>

***

## Non-Rectangular Regions
{: #content3}

1. **What?**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents31}
    <xmp>
    </xmp>

    **Form:**  
        <xmp>
        </xmp>  
        or,  
        <xmp>
        </xmp>

2. **How?**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents32} \\
    * We use  
    * Step Size:
        * **x:**  
        * **y:**   

3. **Simpsons' Rule for Non-Rect Regions:**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents33} \\
    <xmp>


    </xmp>

4. **Simpsons' Double Integral [Algorithm]:**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents34} \\
    <xmp>


    </xmp>

5. **Gaussian Double Integral [Algorithm]:**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents35} \\
    <xmp>



    </xmp>

***

## Triple Integral Approximation
{: #content4}

1. **What?**{: style="color: SteelBlue  "}{: .bodyContents4 #bodyContents41}
    :   * **On what?**  
    :   * **Form:**  
            <xmp>

            </xmp>

2. **Gaussian Triple Integral [Algorithm]:**{: style="color: SteelBlue  "}{: .bodyContents4 #bodyContents42} \\
    <xmp>


    </xmp>
