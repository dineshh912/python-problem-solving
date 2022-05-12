"""
Declare a 2-dimensional array, arr of n empty arrays. 
All arrays are zero indexed. 

Declare an integer, last Answer, and initialize it to 0.

There are 2 types of queries, given as an array of strings for us to parse:

1. Query: 1x y
    let idx = ((x ^ last Answer) % n)
    let arr[idx].append(y)
2. Query: 2x y
    let idx = ((x ^ last Answer) % n)
    let last Answer = arr[idx][y % len(arr[idx])]

"""