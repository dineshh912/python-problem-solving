"""
* Given an array of integers, return a new array such that each element at index i of the new array is the product 
* of all the numbers in the original array expect the one at i.
* 
* For example, if our input was [1,2,3,4,5] the expected output would be [120, 60, 40, 30, 24]. if our input was [3, 2, 1] 
* then expected output would be [2, 3, 6]
* 
 Follow up: what is you can't use division
"""
# using division method

lst_integers = [1, 2, 3, 4, 5]

new_lst_integers = []

num = 1
'''
for i in lst_integers:
    num = num * i

for i in lst_integers:
    new_lst_integers.append(num // i)

print(new_lst_integers)

'''
# method 2
import math

for i in lst_integers:
    new_lst_integers.append(math.prod(lst_integers) // i)

print(new_lst_integers)

# Method 3

prefix_products = []

for num in lst_integers:
    if prefix_products:
        prefix_products.append(prefix_products[-1] * num)
    else:
        prefix_products.append(num)

suffix_products = []

for num in reversed(num):
    if suffix_products:
        suffix_products.append(suffix_products[-1] * num)
    else:
        suffix_products.append(num)


suffix_products = list(reversed(suffix_products))

