"""
A left rotation operation on an array size n shifts each of the array elements 1 unit 
to the lift. given an integer d. rotate the array to the left by d units.

Example: 

d = 2

arr = [1, 2, 3, 4, 5]

outp = [3, 4, 5, 1, 2]

"""

def rotateLeft(d, arr):

    return arr[d:]+arr[:d]




print(rotateLeft(2, [1, 2, 3, 4, 5]))