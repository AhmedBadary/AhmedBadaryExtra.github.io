---
layout: NotesPage
title: Algorithms
permalink: /work_files/research/algos
prevLink: /work_files/research.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Divide-and-Conquer](#content1)
  {: .TOC1}
  * [SECOND](#content2)
  {: .TOC2}
  * [THIRD](#content3)
  {: .TOC3}
  * [FOURTH](#content4)
  {: .TOC4}
  * [FIFTH](#content5)
  {: .TOC5}
  * [SIXTH](#content6)
  {: .TOC6}
</div>

***
***

## Divide-and-Conquer
{: #content1}

1. **Divide-and-Conquer:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    The divide-and-conquer strategy solves a problem by:  
    1. Breaking it into subproblems that are themselves smaller instances of the same type of problem
    2. Recursively solving these subproblems
    3. Appropriately combining their answers
    <br>

    The real work is done piecemeal, in three different places:  
    {: #lst-p}
    1. in the partitioning of problems into subproblems
    2. at the very tail end of the recursion, when the subproblems are so small that they are solved outright
    3. and in the gluing together of partial answers.  

    These are held together and coordinated by the algorithm’s core recursive structure.  
    <br>

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  

4. **Binary Search:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    img1

5. **Mergesort:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  
    The problem of sorting a list of numbers lends itself immediately to a divide-and-conquer strategy: split the list into two halves, recursively sort each half, and then merge the two sorted sublists.  

    img2

    __Merge Function:__{: style="color: red"}  
    Given two sorted arrays $$x[1 . . . k]$$ and $$y[1 . . . l]$$, how do we efficiently merge them into a single sorted array $$z[1 . . . k + l]$$?  
    img3

    Here ◦ denotes concatenation.  

    __Run-Time:__  
    This __merge__ procedure does a constant amount of work per recursive call (provided the required array space is allocated in advance), for a total running time of $$O(k + l)$$. Thus merge’s are __linear__, and the overall time taken by mergesort is:  
    <p>$$T(n)=2 T(n / 2)+O(n) = O(n \log n)$$</p>  
    ☹️


    __Iterative MergeSort:__{: style="color: red"}  
    img4


6. **$$n \log n$$ Lower Bound for (comparison-based) Sorting (Proof):**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}  
    img5
    <br>

7. **Medians:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}  
    
    <br>

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18}  

    <br>

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

***

## FOURTH
{: #content4}

1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents41}  

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents42}  

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents43}  

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents44}  

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents45}  

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents46}  

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents47}  

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents48}  

***

## FIFTH
{: #content5}

1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents51}  

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents52}  

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents53}  

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents54}  

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents55}  

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents56}  

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents57}  

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents58}  

*** 

## Sixth
{: #content6}

1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents61}  

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents62}  

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents63}  

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents64}  

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents65}  

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents66}  

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents67}  

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents68  

## Seven
{: #content7}

1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents7 #bodyContents71}  

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents7 #bodyContents72}  

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents7 #bodyContents73}  

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents7 #bodyContents74}  

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents7 #bodyContents75}  

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents7 #bodyContents76}  

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents7 #bodyContents77}  

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents7 #bodyContents78}  