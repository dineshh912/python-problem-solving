"""
you are given an array and you need to find number of triplets of indices (i, j, k)
such that the elements at those indices are in geometric progression for a given common ration 
r and i < j < k.

example : 

arr = [1, 4, 16, 64] r = 4

possilble triplets and it's indices: 
[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3], []

"""
def countTriplets(arr, r):
    count = 0
    before = {}
    after = {}

    for i in arr:
        if i in after:
            after[i] += 1
        else:
            after[i] = 1

    for i in arr:
        after[i] -= 1 # current element
        if i//r in before and i % r == 0 and i * r in after:
            count += before[i//r] * after[i*r]
        
        if i in before:
            before[i] += 1
        else:
            before[i] = 1
    
    return count
    




print(countTriplets([2, 4, 16, 64], 4))