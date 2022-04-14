"""
A left rotation operation on an array shifts each of the array's elements 1 unit to the left. 
For example, if 2 left rotations are performed on array [1, 2, 3, 4, 5], then the array would become [3, 4, 5, 1, 2]. 

Note that the lowest index item moves to the highest index in a rotation. This is called a circular array.

Given an array a  of n integers and a number, , perform  left rotations on the array. 

Return the updated array to be printed as a single line of space-separated integers.

Function Description

Complete the function rotLeft in the editor below.

rotLeft has the following parameter(s):

int a[n]: the array to rotate
int d: the number of rotations
Returns

int a'[n]: the rotated array

"""

def rotLeft(a, d):
    # Write your code here

    return a[d:] + a[:d]


a = [1, 2, 3, 4, 5]
d = 3


print(rotLeft(a, d))
