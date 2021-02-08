"""
Sorting algorithm - sort items by comparing two adjacent values.
if first value is higher than second value, first value take 
place of second value, this will goes on  until all the elements are sorted.

* Total number of elements in the list
* Length of the list (n-1)
* First value compare to second value if first value greater swap the value
* Repeat the step until n-1
* Return result

"""

def bubble_sort(arr):
	n = len(arr)

	for i in range(n-1):
		for j in range(n-1):
			if arr[j] > arr[j+1]:
				tmp = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = tmp

	return arr

list_elements = [23, 6,7, 25, 67, 45]

print(bubble_sort(list_elements))