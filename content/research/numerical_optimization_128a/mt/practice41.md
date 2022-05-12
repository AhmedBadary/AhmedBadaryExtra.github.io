---
layout: editable
permalink: /work_files/school/128a/mt/practice41
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
        <xmp>
        </xmp>
        $$x_1  =$$   \\
        $$x_2  =$$   

2. **Three-Point Endpoint Formula:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents22} \\
    <xmp>

    </xmp>
    > The approximation in Eq. (4.4) is useful at
        <xmp>
        </xmp>
    > **Errors:** the errors in both Eq. (4.4) and Eq. (4.5) are 
    >  

3. **Three-Point Midpoint Formula:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents23} \\
    <xmp>
    </xmp>
    > **Errors:** 
    >   
    >   > This is because Eq. (4.5) uses data on $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$ and Eq. (4.4) uses data $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$  
    >   > Note also that f needs to be evaluated at $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$  in 
          Eq. (4.5), whereas in Eq. (4.4) it $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$ 

***

## Five-Point Formulas
{: #content3}

1. **What?**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents31} \\
    <xmp>
    </xmp>

2. **Why?**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents32} \\
    <xmp>
    </xmp>

3. **Error:**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents33} \\
    The error term for these formulas is 

4. **Five-Point Midpoint Formula:**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents34} \\
    <xmp>

    </xmp>

    > **Used** for approximation at 

5. **Five-Point Endpoint Formula:**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents35} \\
    <xmp>
    </xmp>

    > **Used** for approximation at 

    > ***Left-endpoint** approximations* are found using this formula with $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$  and ***right-endpoint** approximations* with $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$.  

    > The five-point endpoint formula is particularly useful for $$ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$ 

***

## Approximating Higher Derivatives
{: #content4}

1. **Approximations to Second Derivatives:**{: style="color: SteelBlue  "}{: .bodyContents4 #bodyContents41} \\
    <xmp>

    </xmp>
    
2. **Second Derivative Midpoint Formula:**{: style="color: SteelBlue  "}{: .bodyContents4 #bodyContents42} \\
    <xmp>

    </xmp>
 
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
