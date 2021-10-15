"""
Iterate over the input elements by growing the sorted array at each iteration

compare the current element with largest value available in the sorted array.

if the current element is greater, leave the element or find the corrent possition in the sorted array. 

"""

def insertion_sort(arr):

    for i in range(1, len(arr)):

        while i > 0:
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
            else:
                break
            i = i - 1
    return arr


list_element = [16, 19, 11, 15, 10, 12, 14]

print(insertion_sort(list_element))