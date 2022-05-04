"""
Sorted array take a mid point if X matches the mid point then return X.

Else X is greater than the mid point we consider only right half of the element and find sub divide the mid element there.

Repeat until find the element.

Time complexity : Best case the element can be in mid point so it's O(1).

Worst case the for 16 element the algorith should run atleast 4 time to find the element. so it should be O(log n)

There are two approaches in binary search iterative and recursive method.

"""

def binary_search_iterative(arr, x):
	low = 0
	high = len(arr)

	while low <= high:
		mid = low + (high - low) // 2

		if arr[mid] == x:
			return mid
		elif arr[mid] < x:
			low = mid + 1
		else:
			high = mid -1
	return "Not found"

def binary_search_recursive(arr, x, low, high):
	if high >= low:
		mid = low + (high - low) // 2

		if arr[mid] == x:
			return mid
		elif arr[mid] < x:
			return binary_search_recursive(arr, x, mid +1, high)
		else:
			return binary_search_recursive(arr, x, low, mid -1)
	else:
		return "Not found"



list_elements = [1,2,6,8,9,34,56,78,90,124]

x = 78

print(binary_search_iterative(list_elements, x))

print(binary_search_recursive(list_elements, x, 0, 9))
