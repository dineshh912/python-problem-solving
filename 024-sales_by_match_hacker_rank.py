"""
There is a large pile of socks that must be paired by color. 
Given an array of integers representing the color of each sock, 
determine how many pairs of socks with matching colors there are.

Example:

Input:
n = 7
array = [1, 2, 1, 2, 1, 3, 2]

Output:
2

"""

def sockMerchant(n, ar):
    res = [] # To save count of each element
    for i in set(ar): # set to store unique elements
        res.append(ar.count(i)//2) # appending the count
    
    return sum(res)
    


n = 7
ar = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]

print(sockMerchant(n, ar))