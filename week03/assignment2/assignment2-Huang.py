# Instruction: make sure your code pass the assertion statements
# Copy this file and rename as assignment2-yourname.py

# Q1. Given a positive integer N. The task is to write a Python program to check if the number is prime or not.
import math


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


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
    return ar[0: d % len(ar)] + ar[d % len(ar):]


# DO NOT ALTER BELOW.
assert rotate([1,2,3,4,5,6,7], 2) == [3,4,5,6,7,1,2]
assert rotate([1,2,3], 4) == [2,3,1]


# Q3. Selection sort - implement a workable selection sort algorithm
# https://www.runoob.com/w3cnote/selection-sort.html 作为参考
# Input students would be a list of [student #, score], sort by score ascending order.

def selection_sort(arr: [[int]]) -> [[int]]:
    for i in range(len(arr) - 1):
        index_min = i
        for j in range(i + 1, len(arr)):
            if arr[j][1] < arr[index_min][1]:
                index_min = j
        if i != index_min:
            temp = arr[index_min]
            arr[index_min] = arr[i]
            arr[i] = temp
    return arr


# DO NOT ALTER BELOW.
assert selection_sort([]) == []
assert selection_sort([[1, 100], [2, 70], [3, 95], [4, 66], [5, 98]]) == [[4, 66], [2, 70], [3, 95], [5, 98], [1, 100]]


# Q4. Convert a list of Tuples into Dictionary
# tip: copy operation - copy by value, copy by reference

def convert(tup: any, di: {any, any}) -> None:
    for i in range(0, len(tup), 2):
        di[tup[i]] = tup[i+1]
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

def bsearch_slow(arr: [int], target: int) -> (int):
    left = -1
    right = -1
    for i in range(len(arr)):
        if arr[i] == target and left == -1:
            left = i
        if arr[i] > target and left != -1 and right == -1:
            right = i
        if i == len(arr) - 1:
            right = len(arr) - 1
    return (left, right)


def create_arr(count: int, dup: int) -> [int]:
    return [dup for i in range(count)]


# Complete this    
def bsearch(arr: [int], target: int) -> (int):
    left = 0
    right = len(arr) -1
    res = [-1, -1]
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid -1
        elif arr[mid] <target:
            left = mid + 1
        else:
            res[0] = mid
            right = mid - 1
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid -1
        elif arr[mid] <target:
            left = mid + 1
        else:
            res[1] = mid
            left = mid + 1
    return tuple(res)

assert bsearch_slow(create_arr(10000, 5), 5) == (0, 9999)
assert bsearch(create_arr(1000, 5), 5) == (0, 999)


import timeit
# slow version rnning 100 times = ? seconds
print(timeit.timeit(lambda: bsearch_slow(create_arr(10000, 5), 5), number=100))
# add your version and compare if faster.
print(timeit.timeit(lambda: bsearch(create_arr(10000, 5), 5), number=100))

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
def extract_and_apply(l, p, f):
    return [f(x) for x in l if p(x)]


# (2). [5 points] Write a function concatenate(seqs) that returns a list containing the concatenation of the elements of the input sequences. 
# Your implementation should consist of a single list comprehension, and should not exceed one line. 
def concatenate(seqs):
    return [elements for item in seqs for elements in item]


assert concatenate([[1, 2], [3, 4]]) == [1, 2, 3, 4]
assert concatenate(["abc", (0, [0])]) == ['a', 'b', 'c', 0, [0]]
