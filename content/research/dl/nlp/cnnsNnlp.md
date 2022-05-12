---
layout: NotesPage
title: CNNs in NLP 
permalink: /work_files/research/dl/nlp/cnnsNnlp
prevLink: /work_files/research/dl/nlp.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [FIRST](#content1)
  {: .TOC1}
  * [SECOND](#content2)
  {: .TOC2}
  * [THIRD](#content3)
  {: .TOC3}
  * [FOURTH](#content4)
  {: .TOC4}
</div>

***
***

## FIRST
{: #content1}

1. **Motivation:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    Combination (consecutively) of words are hard to capture/model/detect.  

2. **Padding:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
__Padding:__  
* After convolution, the rows and columns of the output tensor are either:  
    * Equal to rows/columns of input tensor ("same" convolution)  
        > Keeps the output dimensionality intact.  

    * Equal to rows/columns of input tensor minus the size of the filter plus one ("valid" or "narrow')  
    * Equal to rows/columns of input tensor plus filter minus one ("wide")  

__Striding:__  
Skip some of the outputs to reduce length of extracted feature vector  \\
![img](/main_files/dl/nlp/misc/1.png){: width="68%"}  \\

__Pooling:__  
Pooling is like convolution, but calculates some reduction function feature-wise.  
* __Types__:  
    * __Max Pooling__: "Did you see the feature anywhere in the range?"  
    * __Average pooling:__ "How prevalent is this feature over the entire range?"  
    * __k-Max pooling:__ "Did you see this feature up to k times?"  
    * __Dynamic pooling:__ "Did you see this feature in the beginning? In the middle? In the end?"  

__Stacking - Stacked Convolution:__  
* Feeding in convolution from previous layer results in larger are of focus for each feature  
* The increase in the number of _words_ that are covered by stacked convolution (e.g. n-grams) is *__exponential__* in the number of layers  \\
![img](/main_files/dl/nlp/misc/2.png){: width="68%"}  \\

__Dilation - Dilated Convolution:__  
Gradually increase _stride_, every time step (no reduction in length).  
![img](/main_files/dl/nlp/misc/3.png){: width="68%"}  \\
One can use the final output vector, for next target output prediction. Very useful if the problem we are modeling requires a fixed size output (e.g. auto-regressive models).  
* Why (Dilated) Convolution for Modeling Sentences?  
    * In contrast to recurrent neural networks:
        * + Fewer steps from each word to the final representation: RNN $$O(N)$$, Dilated CNN $$0(\log{N})$$ 
        * + Easier to parallelize on GPU 
        * - Slightly less natural for arbitrary-length dependencies 
        * - A bit slower on CPU?  
* Interesting Work:  
    _"Iterated Dilated Convolution [Strubell 2017]"_:  
    * A method for __sequence labeling__:  
        Multiple Iterations of the same stack of dilated convolutions (with different widths) to calculate context  
    * __Results:__
        * Wider context 
        * Shared parameters (i.e. more parameter efficient)  

__Structured Convolution:__  
* __Why?__  
    Language has structure, would like it to localize features.  
    > e.g. noun-verb pairs very informative, but not captured by normal CNNs   

* __Examples:__   
    * Tree-Structured Convolution _[Ma et al. 2015]_  
    * Graph Convolution _[Marcheggiani et al. 2017]_ 
        

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}

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
