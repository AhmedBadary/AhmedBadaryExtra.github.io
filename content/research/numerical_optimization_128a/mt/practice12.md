---
layout: editable
permalink: /work_files/school/128a/mt/practice12
---

**1.2/**{: style="font-size: 250%; color: red; font: italic bold 50px/70px Georgia, serif"}  

____________________
***

## Binary Machine Numbers
{: #content1}

1. **Representing Real Numbers:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents11} 
    :   A $$\ \ \ \ \ \ \ \ \ \ \ \ \$$ (binary digit) representation is used for a real number. 
    > * The **first bit** is  
    > * Followed by:  
    > * and a $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$, called the  
    > * The base for the exponent is   
2. **Floating-Point Number Form:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents12}
    <xmp>

    </xmp>

3. **Smallest Normalized positive Number:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents13} 
    * **When:**  
    * **Equivalent to:**  

4. **Largest Normalized positive Number:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents14} \\
    * **When:**  
    * **Equivalent to:**  

5. **UnderFlow:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents15}
    * **When numbers occurring in calculations have**  

6. **OverFlow:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents16}
    * **When numbers occurring in calculations have**

7. **Representing the Zero:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents17} \\
    * There are $$ \ \ \ \ \ $$ Representations of the number zero:
        <xmp>

        </xmp>

***

## Decimal Machine Numbers
{: #content2}

1. **What?**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents21} 
    <xmp>

    </xmp>

2. **(k-digit) Decimal Machine Numbers:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents22}
    <xmp>

    </xmp>

3. **Normalized Form:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents23} 
    <xmp>

    </xmp>

4. **Floating-Point Form of a Decimal Machine Number:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents24} \\
    * The floating-point form of y, denoted $$f_l(y)$$, is obtained by:
        <xmp>

        </xmp>

5. **Termination:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents25} \\
    There are two common ways of performing this termination:  
    1. **$$ \ \ \ \ \ \ \ \ \ \ $$:** 
        <br>
        > This produces the floating-point form:  

    2. **$$ \ \ \ \ \ \ \ \ \ \ $$:** $$ \ \ $$ which 
        <br>

        > This produces the floating-point form:   
        >   > For rounding, when $$d_{k+1} \geq 5$$, we  
        >   > When $$d_{k+1} < 5$$, we  
        >   > If we round down, then $$\delta_i =$$   
        >   > However, if we round up,  

6. **Approximation Errors:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents26} \\
    <xmp>

    </xmp>
    * **The Absolute Error:** $$ \ \ \ \ \ \ \ $$.  

    * **The Relative Error:** $$ \ \ \ \ \ \ \ $$.

7. **Significant Digits:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents27} \\
    <xmp>

    </xmp>

8. **Error in using Floating-Point Repr.:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents28} \\
    * **Chopping:**{: style="color: green"}  
        **The Relative Error =**   
        **The Machine Repr**. [for k decimial digits] =  
        :   $$ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$.  

        $$ \implies $$  
        <xmp>

        </xmp>
        **Bound** $$ \ \ \ \implies \ \  \ \ \ \ \ \ \ \ \ \$$.

    * **Rounding:**{: style="color: green"}  
        > In a similar manner, a bound for the relative error when using k-digit rounding arithmetic is   

        **Bound** $$ \ \ \ \implies \ \  \ \ \ \ \ \ \ \ \ \ \ \ $$.

9. **Distribution of Numbers:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents29} \\
    The number of decimal machine numbers in $$\ \ \ \ \ \ \ \ \ \ \ $$ is  $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$ for   

***

## Finite-Digit Arithmetic
{: #content3}

1. **Values:**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents31}
    :   $$ x = \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$
    :   $$ y = \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$

2. **Operations:**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents32} \\
    <xmp>

    </xmp>

3. **Error-producing Calculations:**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents33} \\
    * First:  
        <xmp>

        </xmp>
    * Second:  
        <xmp>

        </xmp>

4. **Avoiding Round-Off Error:**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents34} \\
    * First:  
        <xmp>

        </xmp>
    * Second:  
        <xmp>

        </xmp>   
        $$ 
        \implies \ \ \ \ \ \ \ \ \ \ \ \ \ \  x_1 = \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ , \ \ \ \ \ \ \ \ \ \ \ \ \ \  
        x_2 = \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \
        $$

***

## Nested Arithmetic
{: #content4}

1. **What?**{: style="color: SteelBlue  "}{: .bodyContents4 #bodyContents41} 
    <xmp>

    </xmp>   
    > Remember that chopping (or rounding) is performed:   

    <br>
    *  $$  \ \ \ \ \ \ \$$
    
    <br>

    > Polynomials should always be expressed $$  \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$ , becasue, $$  \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$

2. **Why?**{: style="color: SteelBlue  "}{: .bodyContents4 #bodyContents42} 
    <xmp>

    </xmp>  