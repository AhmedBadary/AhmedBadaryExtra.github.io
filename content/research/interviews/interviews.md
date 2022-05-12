---
layout: NotesPage
title: Interviews
permalink: /interviews
prevLink: /work_files.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Algorithms](#content1)
  {: .TOC1}
  * [Quantitative Analysis](#content2)
  {: .TOC2}
  * [Strings](#content3)
  {: .TOC3}
</div>

***
***


## Algorithms
{: #content1}

1. **Array Duplicates:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    Given an array of n elements which contains elements from 0 to n-1, with any of these numbers appearing any number of times. Find these repeating numbers in O(n) and using only constant memory space.  
    
    1. Mathematical Solution: $$O(n), O(1)$$  
        * Traverse the given array from i= 0 to n-1 elements  
            * Go to index arr[i]%n and increment its value by n.  
        * Now traverse the array again and print all those   
            * indexes i for which arr[i]/n is greater than 1.  
    2. Indexes Solution: $$O(n), O(1)$$  
        ```
        traverse the list for i= 0 to n-1 elements
        {
          check for sign of A[abs(A[i])] ;
          if positive then
             make it negative by   A[abs(A[i])]=-A[abs(A[i])];
          else  // i.e., A[abs(A[i])] is negative
             this   element (ith element of list) is a repetition
        }
        ```

2. **Re-Arranging Array Indexes:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    Rearrange an array so that arr[i] becomes arr[arr[i]] with O(1) extra space  
    1. Mathematical Solution: $$O(n), O(1)$$   
        * Increase every array element arr[i] by $$(\text{arr}[\text{arr}[i]] % n) * n$$.
        * Divide every element by $$n$$.  
    
    > The idea is to store both numbers as the quotient and the remainder inside the array element  

3. **Two Sum Problem:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.  
    1. __HashTable:__ $$O(n), O(1)$$   
        Iterate and inserting elements into the table, we also look back to check if current element's complement already exists in the table. If it exists, we have found a solution and return immediately.
    

4. **Permutations of an Array:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
    __Key Idea:__  

    ```python
    def _permute(a, l, r, results): 
        if l==r: 
            results.append(a.copy())
        else: 
            for i in range(l,r+1): 
                a[l], a[i] = a[i], a[l] 
                _permute(a, l+1, r, results) 
                a[l], a[i] = a[i], a[l]
            
    def permute(arr: List[int]) -> List[List[int]]:
        results = []
        _permute(arr, 0, len(arr)-1, results)
        return results
    ```

    __For strings:__  
    ```python
    def _permute(s, chosen, results): 
    if len(s) < 1: 
        # results.append(a.copy())
        print(chosen)
    else: 
        for i in range(len(s)):
            # Choose
            c = s[i]
            chosen += c
            s = s.replace(c, "")
            # Explore
            _permute(s, chosen, results) 
            # UnChoose
            chosen = chosen[:-1]
            s = s[:i] + c + s[i:]
            
    def permute(s):
        results = []
        _permute(s, "", results)
        return results

    permute('abc')
    ```

    __Generate permutation at index $$k$$:__  
    ```python
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str 
        """
        k-=1
        nl = list(range(1,n+1))
        out = ''
        while n>0:
            temp = math.factorial(n-1)
            out+=str(nl.pop(k//temp))
            k %= temp
            n -= 1
        return out
    ```


5. **Hight/Depth of Tree:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  
    Use DFS:  
    ```python
    def dfs(self, root, visited = [], depth=1):
        if not root.children:
            return depth
        # visited.append(root)
        max_depth = depth
        for node in root.children:
            # 2 Lines below: only needed if graph is not a tree
            # if node not in visited:
                # max_depth = max(self.dfs(node, visited, depth+1), max_depth)
            max_depth = max(self.dfs(node, depth+1), max_depth)
        return max_depth
        
    
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        return self.dfs(root)
    ```

6. **Pre-Order Traversal:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}  
    ```python
    def preorderTraversal_iterative(self, root: TreeNode) -> List[int]:
        arr = []
        stack = []
        while 1:
            while root:
                stack.append(root)
                arr.append(root.val)
                root = root.left
            if not stack:
                break
            root = stack[-1].right
            stack.pop()
        return arr
    
    
    def preorderTraversal_recursive(self, root: TreeNode) -> List[int]:
        self.arr = []
        def helper(root):
            if not root:
                return
            self.arr.append(root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        return self.arr
    ```

    __In-order__:  
    ```python
    def inOrderT(root):    
        self.ans = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            self.ans.append(root.val)
            helper(root.right)
        helper(root)
        return self.ans
    ```

<!-- 7. **:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}   -->


***
***


## Strings
{: #content3}

1. **Uniqueness of characters:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}  
    1. Array of indices / Hashmap: O(n=len(string)), O(256)

2. **Permutations (str a is perm of str b):**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}  
    1. Sort both -> equality: O(n log n)
    2. (fixed) array of character counts


3. **Replace a char in str w/ more than one char (e.g. all 'a' in str -> 'bb'):**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}  
    1. count number of 'a' in str -> multiply by (len('bb') - 1) -> start modifying from back of string (backwards)


4. **Palindrome:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents34}  
    To check for if a string is a Palindrome, count the number of characters:
    * even len(s): all char-counts must be even
    * odd len(s): only one char-count can be odd

    Best sol (Still O(N)):
    1. Use a bit vector -> map chars to 26 bit-vector -> toggle everytime you see char -> check bit vector == 0 (has at most 1 "on" bit)


5. **Q1.5:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents35}  


6. **Rotate Matrix (implement it):**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents36}  


7. **Check str a is ROTATION of str b:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents37}  
    By making one call to isSubstring:
    * Note: str b always substring of str a+a (e.g. "waterbottle", "erbottlewat": "erbottlewat" isSubstr of "waterbottle"+"waterbottle"="wat_erbottlewat_erbottle")


8. **Notes:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents38}  
    * Ask ASCII or UTF8  



***
***

## NOTES

* Learn about how to handle cycles in arrays in O(1) space
* For Recursion: Ask the size of the input (i.e. would it fit in the stack?) else iterative solution
* Interviewing at GOOGLE:  
    Prove the Resume  
    White board  
    Make sure the interviewer **Feels _comfortable_ working with you on the team**  
    Ask a lot of questions; the interviewer is vague on purpose: what are the time&space constraints?   
    Keep Thinking  
    Keep the interviewer happy and attentive  
    Have a very positive/approachable attitude
  
    Data Structures, Algorithms, Space&Time Complexity  
    System Design, OOP, 
  
    Dijkstra, A\*, DFS, BFS, Tree, traversal,   
    NP-Complete, NapSack, Traveling Salesman, NP-Completeness, Discrete Math, Counting (n choose k problems),   
    Recursion: iterative to recursive, complexity  
    OS: processes, threads, concurrency issues, locks etc., resource allocation, context switching, scheduling  
    System Design: feature sets, interfaces, class hierarchies, distributed systems, constrained system design  
    The Internet: routers, servers, search, DNS, firewalls
  
    Testing Experience, Unit Tests, Interesting Test-cases, integration Tests for Gmail?

  
    C++, Java, Python, GoLang  
* [GOOD LINK](https://blog.usejournal.com/what-i-learned-from-interviewing-at-multiple-ai-companies-and-start-ups-a9620415e4cc)
* [Fellowship Program in ML](https://fellowship.ai/)  

1. Listen Carefully
2. Draw an example
3. Find Bruteforce
4. Optimize: 
    * look for unused info - more examples - start with "incorrect" sol - timeVSspace - precompute - BCR
5. Walk through the algorithm
6. Implement
7. Test


* Arrays and Strings questions are interchangeable


__Face-up/Face-down Cards:__{: style="color: red"}  
[Video](https://www.youtube.com/watch?v=HCp_eN6JSac)  

1. A card deck of 52 cards, 13 face-up.
2. The Face-up cards are distributed randomly throughout the deck.
3. You are blindfolded and you don't know anything about the cards.
4. How can you create two piles with the same amount of face-up cards?

> <span>Let $$x$$ be the number of face-up cards in pile #1</span>{: style="color: goldenrod"} 

| | __$$\uparrow$$__{: style="color: blue"} | __$$\downarrow$$__{: style="color: blue"} 
__pile #1 $$= 13$$__{: style="color: blue"} | $$x$$ | $$13 - x$$
__pile #2 $$= 39$$__{: style="color: blue"} | $$13 - x$$ | $$26 + x$$


__Face-up/Face-down Cards Generic Version:__{: style="color: red"}  
1. A card deck of 52 cards, $$k$$ face-up.

> <span>Let $$x$$ be the number of face-up cards in pile #1</span>{: style="color: goldenrod"} 

| | __$$\uparrow$$__{: style="color: blue"} | __$$\downarrow$$__{: style="color: blue"} 
__pile #1 $$= k$$__{: style="color: blue"} | $$x$$ | $$k - x$$
__pile #2 $$= 52-k$$__{: style="color: blue"} | $$k - x$$ | $$(52-k) - (k-x)$$


__Face-up/Face-down Cards Generic Version (flipped):__{: style="color: red"}  
1. A card deck of 52 cards, $$k$$ face-down.
4. How can you create two piles with the same amount of face-down cards?

> <span>Let $$x$$ be the number of face-down cards in pile #1</span>{: style="color: goldenrod"} 

| | __$$\uparrow$$__{: style="color: blue"} | __$$\downarrow$$__{: style="color: blue"} 
__pile #1 $$= k$$__{: style="color: blue"} | $$k-x$$ | $$x$$
__pile #2 $$= 52-k$$__{: style="color: blue"} | $$(52-k)-(k-x)$$ | $$k - x$$


<!-- ## Quantitative Analysis
{: #content2}

1. **Basketball Hoops:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    Basketball player makes first free throw and misses the  second. Thereon after, the probability of making the next free throw is the proportion of previous shots he has made. What is the probability he makes 50 of the first 100 shots?

    The probability is 1/99. In fact, we show by induction on n that after n shots, the probability of having made any number of shots from $$1$$ to $$n−1$$ is equal to $$1/(n− 1)$$. This is evident for $$n = 2$$. Given the result for n, we see that the probability of Shanille making i shots after $$n + 1$$ attempts is the probability of her making i out of n and then missing plus the probability of her making $$i − 1$$ out of n and then hitting:
    $$ P(m + 1, k) = P(m, k) \dfrac{m − k}{m} + P(m, k − 1)\dfrac{k − 1}{m} = \dfrac{1}{m − 1} \dfrac{m − k}{m}  + \dfrac{1}{m − 1}  \dfrac{k − 1}{m}  = \dfrac{1}{m − 1}  \dfrac{m − k + k − 1}{m}  = \dfrac{1}{m}$$

    $$ P(n + 1, i) = P(n, i) \dfrac{n − i}{n} + P(n, i − 1)\dfrac{i − 1}{n} \\ \\ = \dfrac{1}{n − 1} \dfrac{n − i}{n}  + \dfrac{1}{n − 1}  \dfrac{i − 1}{n}  = \dfrac{1}{n − 1}  \dfrac{n − i + i − 1}{n}  = \dfrac{1}{n}$$


 -->