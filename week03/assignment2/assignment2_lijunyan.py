# Instruction: make sure your code pass the assertion statements
# Copy this file and rename as assignment2-yourname.py

# Q1. Given a positive integer N. The task is to write a Python program to check if the number is prime or not.
import math
from typing import Tuple


def is_prime(n: int) -> bool:
    for i in range(2,abs(n)):
        if n%i==0 :
            return False
    return (abs(n) != 1) & (n != 0)



# DO NOT ALTER BELOW.
assert is_prime(2)
assert not is_prime(15)
assert is_prime(7907)
assert not is_prime(-1)
assert not is_prime(0)


# Q2 Write a function rotate(ar[], d) that rotates arr[] of size n by d elements.
# Input ar = [1,2,3,4,5,6,7], d = 2
# Output [3,4,5,6,7,1,2]

def rotate(ar: [int], d: int) -> [int]:
        return ar[d%len(ar):] + ar[:d%len(ar)]


# DO NOT ALTER BELOW.
assert rotate([1,2,3,4,5,6,7], 2) == [3,4,5,6,7,1,2]
assert rotate([1,2,3], 4) == [2,3,1]


# Q3. Selection sort - implement a workable selection sort algorithm
# https://www.runoob.com/w3cnote/selection-sort.html 作为参考
# Input students would be a list of [student #, score], sort by score ascending order.
#
# def selection_sort(arr: [[int]]) -> [[int]]:
#     if len(arr) == 0:
#         return arr
#     for i in range(len(arr)):
#         m = i
#         for j in range(i + 1, len(arr)):
#             if arr[m][1] > arr[j][1]:
#                 arr2 = arr[j]
#                 arr[j] = arr[m]
#                 arr[m] = arr2
#                 m = j
#
#     return arr
def selection_sort(arr: [[int]]) -> [[int]]:
    for i in range(0,len(arr)):
        min=i
        for j in range( i+1, len(arr) ):
            if arr[j][1] < arr[min][1]:
                min=j
        if min != i:
            swap(arr[i],arr[min])


# DO NOT ALTER BELOW.
assert selection_sort([]) == []
assert selection_sort([[1, 100], [2, 70], [3, 95], [4, 66], [5, 98]]) == [[4, 66], [2, 70], [3, 95], [5, 98], [1, 100]]


# Q4. Convert a list of Tuples into Dictionary
# tip: copy operation - copy by value, copy by reference

def convert(tup: (any), di: {any, any}) -> None: 
    list0=list(tup)
    list_key=[]
    list_val=[]
    for i in range(0,len(list0)):
        if i%2==0:
            list_key.append(list0[i])
        else:
            list_val.append(list0[i])
    dir={ key : val for key ,val in zip(list_key, list_val) }
    di.update(dir)
    pass
    # Do NOT RETURN di, EDIT IN-PLACE
    
    
# DO NOT ALTER BELOW.
expected_dict = {}
convert((), expected_dict)
assert expected_dict == {}

convert(('key1', 'val1', 'key2', 'val2'), expected_dict)
assert expected_dict == {'key1': 'val1', 'key2': 'val2'} 


# Q5. Find left-most and right-most index for a target in a sorted array with duplicated items.
# provided an example of slow version of bsearch_slow with O(n) time complecity. 
# your solution should be faster than bsearch_slow

def bsearch_slow(arr: [int], target: int) -> Tuple[int, int]:
    left = -1
    right = -1
    for i in range(len(arr)):
        if arr[i] == target and left == -1:
            left = i
        if arr[i] > target and left != -1 and right == -1:
            right = i
        if i == len(arr) - 1:
            right = len(arr) - 1
    return ( left , right )

def create_arr(count: int, dup: int) -> [int]:
    return [dup for i in range(count)]
        
# Complete this    
def bsearch(arr:[int], target:int) -> (int):
    left=-1
    right=-1
    lef=0
    end=len(arr)
    while lef<end:
        mid=(lef+end)//2
        if arr[mid] > target:
            end=mid
        elif arr[mid] < target:
            lef=mid+1
        elif arr[mid] == target:
            end = mid
            left = lef
    reset(lef.end)
    while lef<end:
        mid=(lef+end)//2
        if arr[mid] < target:
            lef = mid+1
        elif arr[mid] > target:
            right=mid
        elif arr[mid] == target:
            right=lef
            lef = mid+1
    return ( left , right )


assert bsearch_slow(create_arr(10000, 5), 5) == (0, 9999)
assert bsearch(create_arr(1000, 5), 5) == (0, 999)


import timeit
# slow version rnning 100 times = ? seconds
timeit.timeit(lambda: bsearch_slow(create_arr(10000, 5), 5), number=100)
# add your version and compare if faster.


# Q6. Working with Lists
# (1). Consider the function extract_and_apply(l, p, f) shown below, 
# which extracts the elements of a list l satisfying a boolean predicate p, applies a function f to each such element, and returns the result. 
def extract_and_apply(l, p, f): 
    result = [] 

    for x in l: 
        if p(x): 
            result.append(f(x)) 
    return result 
# Rewrite extract_and_apply(l, p, f) in one line using a list comprehension. 
def  extract_and_apply_re(l,p,f):
    return [ f(x) for x in l if p(x)]
# (2). [5 points] Write a function concatenate(seqs) that returns a list containing the concatenation of the elements of the input sequences. 
# Your implementation should consist of a single list comprehension, and should not exceed one line. 
def concatenate(x):
    return [x[i][j]  for i in range(0,len(x)) for j in range(0,len(x[i]))]
>>> concatenate([[1, 2], [3, 4]])
[1, 2, 3, 4] 
>>> concatenate(["abc", (0, [0])]) 
['a', 'b', 'c', 0, [0]] 

