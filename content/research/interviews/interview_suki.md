"""
Problem #1
~~~Interweaving an array - general case~~~
You are given an array of length 2n and you wish to interweave the two halves of the array as the following:
['x_1', 'x_2',..., 'x_n', 'y_1', 'y_2',..., 'y_n'] -> ['x_1', 'y_1', 'x_2', 'y_2',..., 'x_n', 'y_n']

Example: 
input = [0, 1, 2, 'a', 'b', 'c'] 
print(interweave(input))
>>> [0, 'a',  1, 'b', 2, 'c']
"""

"""
Problem #2
~~~Interweaving an array - opposite~~~
You are given an array of length 2n and you wish to interweave the two halves of the array as the following:
['x_1', 'x_2',..., 'x_n', 'y_1', 'y_2',..., 'y_n'] -> ['y_1', 'x_1', 'y_2', 'x_2',..., 'y_n', 'x_n']

Example: 
input = [0, 1, 2, 'a', 'b', 'c'] 
print(interweave(input))
>>> ['a', 0, 'b', 1, 'c', 2]
"""


"""
Problem #3
~~~Interweaving an array - special case~~~
You are given an array of length 2n, where n is a power of 2,  and you wish to interweave the two halves 
of the array as the following:
['x_1', 'x_2',..., 'x_n', 'y_1', 'y_2',..., 'y_n'] -> ['x_1', 'y_1', 'x_2', 'y_2',..., 'x_n', 'y_n']

Example: 
input = [0, 1, 2, 3, 'a', 'b', 'c', 'd'] 
print(interweave(input))
>>> [0, 'a',  1, 'b', 2, 'c', 3, 'd']
"""

"""
Problem #4
~~~Interweaving an array in place - special case~~~
You are given an array of length 2n, where n is a power of 2,  and you wish to interweave the two halves 
of the array in place (without using extra space) as the following:
['x_1', 'x_2',..., 'x_n', 'y_1', 'y_2',..., 'y_n'] -> ['x_1', 'y_1', 'x_2', 'y_2',..., 'x_n', 'y_n']

Example: 
input = [0, 1, 2, 3, 'a', 'b', 'c', 'd'] 
print(interweave(input))
>>> [0, 'a',  1, 'b', 2, 'c', 3, 'd']
"""


"""
Problem #5
~~~Interweaving an array in place - general case~~~
You are given an array of length 2n and you wish to interweave the two halves of the array as the following:
['x_1', 'x_2',..., 'x_n', 'y_1', 'y_2',..., 'y_n'] -> ['x_1', 'y_1', 'x_2', 'y_2',..., 'x_n', 'y_n']

Example: 
input = [0, 1, 2, 'a', 'b', 'c'] 
print(interweave(input))
>>> [0, 'a',  1, 'b', 2, 'c']
"""

"""
Problem #6
~~~Local Maximas~~~
After solving an intensive (sampled) gradient computations, we gather a ton of datapoints as a time series
of scalars (points).
We would like to find a local maxima in our data in an efficient manner.

Example: 
input = [2, 16, 13, 4, 5, 9]
print(find_maxima(input))
>>> 16
"""

-----

"""
Problem #2
~~~Interweaving an array in place - special case~~~
You are given an array of length 2n, where n is a power of 2,  and you wish to interweave the two halves 
of the array in place (without using extra space) as the following:
['x_1', 'x_2',..., 'x_n', 'y_1', 'y_2',..., 'y_n'] -> ['x_1', 'y_1', 'x_2', 'y_2',..., 'x_n', 'y_n']

Example: 
input = [0, 1, 2, 3, 'a', 'b', 'c', 'd'] 
print(interweave(input))
>>> [0, 'a',  1, 'b', 2, 'c', 3, 'd']
"""
  
# def weave(inp, st, mid, end):
  

def interweave(inp, st, end):
#   print(inp, st, end)
  if end - st <=2:
    return
  mid = (end + st) // 2
  end2 = (end+mid)//2
  p1 = (st+mid)//2
  while mid < end2:
    inp[p1], inp[mid] = inp[mid], inp[p1]
    p1+=1
    mid+=1
  
  mid = (end + st) // 2
  interweave(inp, st, mid)
  interweave(inp, mid, end)

test = [0, 1, 2, 3, 'a', 'b', 'c', 'd'] 
interweave(test, 0, len(test))
print(test)


# ['x_1', 'x_2',..., 'x_n', 'y_1', 'y_2',..., 'y_n'] -> ['x_1', ..., 'x_n/2', y_1', ..., 'y_n/2', x_n/2 + 1', 'y_n/2',..., 'y_n']
# ['x_1', 'y_1, 'x_2', y_2] ->
# [x1, x2, . . . , xn, y1, y2, . . . , yn] → [x1, . . . , xn/2, y1, . . . , yn/2, xn/2+1, . . . , xn, yn/2+1 , . . . , yn]

https://codeinterview.io/playback/TQATLHRDPR#?t=636