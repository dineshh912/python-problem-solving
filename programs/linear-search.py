"""
Start from left most element of given array and compare one by one with element X
If element maches return index value
If element doen't match return element not found.

Time complexity: worst case the element found at the end of the array. so it's depend 
on the size of the input. so O(n).

Best case: the element can be found at the first iteraion :  O(1)
"""

def linear_search(arr, x):
	for i in range(len(arr)):
		if arr[i] == x:
			return i
	return "not found"

list_elements = [1, 3, 6, 7, 28, 324, 45]

x = 324

print(linear_search(list_elements, x))
