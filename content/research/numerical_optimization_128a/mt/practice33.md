---
layout: editable
permalink: /work_files/school/128a/mt/practice33
---

**3.3/**{: style="font-size: 250%; color: red; font: italic bold 50px/70px Georgia, serif"} 

____________________
***

## Divided Differences
{: #content1}

1. **What?**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents11}
    <xmp>
    </xmp>

2. **Form of the Polynomial:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents12} \\
    * $$P_n(x) = $$
    <br>
    <br>
    * **Evaluated at $$x_0$$:** 
    <br>

    * **Evaluated at $$x_1$$:** 
    <br>

    * > $$\implies \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$.
3. **The divided differences:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents13} \\
    * **The *zeroth* divided difference** of the function f with respect to $$x_i$$:
        * **Denoted:** 
        * **Defined:** 
        * > $$f[x_i] =  \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$.
    * > The remaining divided differences are defined: 

    * **The *first* divided difference** of $$f$$ with respect to $$x_i$$ and $$x_{i+1}$$:
        * **Denoted:** 
        * **Defined:** 
            <xmp>

            </xmp>
    * **The *second* divided difference** of $$f$$ with respect to $$x_i$$, $$x_{i+1}$$ and $$x_{i+2}$$:
        * **Denoted:** 
        * **Defined:** 
            <xmp>

            </xmp>
    * **The *Kth* divided difference** of $$f$$ with respect to $$x_i$$, $$x_{i+1},...,x_{i+k-1},x_{i+k}$$:
        * **Denoted:** 
        * **Defined:** 
            <xmp>

            </xmp>
    * > The process ends with 
    * **The *nth* divided difference** of $$f$$ with respect to $$x_i$$, $$x_{i+1},...,x_{i+k-1},x_{i+k}$$:
        * **Denoted:** 
        * **Defined:** 
            <xmp>
            </xmp>

4. **The Interpolating Polynomial:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents14} \\
    $$P_n(x) = $$

5. **Newton’s Divided Difference:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents15} \\
    $$P_n(x) = $$
    <br>
    <br>
    > The value of $$f[x_0,x_1,...,x_k]$$ is 
        <xmp> </xmp>

6. **Generation of Divided Differences:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents16} \\
    <xmp>

    </xmp>

7. **Algorithm:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents17} \\
    <xmp>
    </xmp>
    <xmp>

    </xmp>

***

## Forward Differences
{: #content2}

1. **Forward Difference:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents21} \\
    <xmp>

    </xmp>

2. **The divided differences (with del notation):**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents22} \\
    <xmp>
    </xmp>  

    and in general,  
    <xmp>
    </xmp>

3. **Newton Forward-Difference Formula:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents23} \\
    <xmp>

    </xmp>  

***

## Backward Differences
{: #content3}

1. **Backward Difference:**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents31} \\
    <xmp>

    </xmp>

2. **The divided differences:**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents32} \\
    <xmp>
    </xmp>

    > and in general, 

    <xmp>
    </xmp>

    > Consequently, the Interpolating Polynomial \\
    <xmp>

    </xmp>

    > If we extend the binomial coefficient notation to 
    >     <xmp> </xmp>
    <xmp>

    </xmp>
    > then \\
    <xmp>

    </xmp>

3. **Newton Backward–Difference Formula:**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents33} \\
    <xmp>

    </xmp>

## Centered Differences
{: #content4}

1. **What?**{: style="color: SteelBlue  "}{: .bodyContents4 #bodyContents41} 
    <xmp> </xmp>
2. **Why?**{: style="color: SteelBlue  "}{: .bodyContents4 #bodyContents42} 
    <xmp>
    </xmp>
3. **Stirling's Formula:**{: style="color: SteelBlue  "}{: .bodyContents4 #bodyContents43} \\
    * **If $$n = 2m + 1$$ is odd:** 
        <xmp>
        </xmp>
    * **If $$n = 2m$$ is even:** [we use the same formula but delete the last line]
        <xmp>
        </xmp>
4. **Table of Entries:**{: style="color: SteelBlue  "}{: .bodyContents4 #bodyContents44} \\
    <xmp>
    
    </xmp>