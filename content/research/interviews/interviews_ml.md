---
layout: NotesPage
title: ML Interviews
permalink: /interviews_ml
prevLink: /work_files.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [FIRST](#content1)
  {: .TOC1}
  * [SECOND](#content2)
  {: .TOC2}
  * [THIRD](#content3)
  {: .TOC3}
<!--   * [FOURTH](#content4)
  {: .TOC4}
  * [FIFTH](#content5)
  {: .TOC5}-->
  * [ML System Design](#content6)
  {: .TOC6}
</div>

***
***

## FIRST
{: #content1}

1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}

<!-- 2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18} -->

***

## SECOND
{: #content2}

<!-- 1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents26}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents27}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents28}
 -->

***

## THIRD
{: #content3}

<!-- 1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents34}

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents35}

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents36}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents37}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents38}
 -->

***

## ML System Design
{: #content6}

[ML System Design (NG)](https://www.youtube.com/watch?v=HREeLryOh4Q)  
<br>

1. **ML System Design (NG) - Summary:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents61}  
    __Problem:__ Spam Classification  
    __Task:__ Build a Spam Classifier  

    1. __How to spend your time to lower the systems error:__  
        * Collect lots of data
        * Develop Sophisticated Features based on email routing information (from email header)
        * Develop Sophisticated Features for message body ("deal" vs "Deals", etc.)  
        * Develop Sophisticated algorithm for misspellings ("Med1cine", "M0rtgage" etc.)  
        <p class="message">Tip: List all of your options for this category. Brainstorm then systematically select/prioritize.</p>  

    __Recommended Approach:__{: style="color: red"}  
    {: #lst-p}
    * Start with a simple algorithm that you can implement quickly. Implement it and test it on your cross-validation data.
    * Plot learning curves to decide if more data, more features, etc. are likely to help.
    * Error analysis: Manually examine the examples (in cross validation set that your algorithm made errors on. See if you spot any systematic trend in what type of examples it is making errors on.  



<!-- 2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents62}

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents63}

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents64}

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents65}

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents66}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents67}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents68}
 -->


***
***
***

__Notes:__{: style="color: red"}  
{: #lst-p}
* [ML System Design (NG)](https://www.youtube.com/watch?v=HREeLryOh4Q)  
