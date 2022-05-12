"""
An array is a type of ds that stores 
elements of the same type in a contiguous block of memory.

In an array A, of size N. each memory location has some unique
index i such that 0 <= i < N. that can ve referenced as A[i].

Reverse an array of integers.

Example:

A = [1, 2, 3]
Returns [3, 2,1]

Reverse the elements of the array in place.

"""

def reverseArray(a):
    return a[::-1]