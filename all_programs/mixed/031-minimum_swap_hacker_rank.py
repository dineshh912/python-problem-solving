"""
You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n]
without any duplicates. You are allowed to swap any two elements.
Find the minimum number of swaps required to sort the array in ascending order.
index = [, 2, 3, 4]
"""
def minimumSwaps(arr):
    swap_res = 0
    # iterate over array
    for i in range(0, len(arr)):
        
        while arr[i] != i+1:
            # temp = correct index of arr[i]
            temp = arr[i]-1
            # Swap the value
            arr[i], arr[temp] = arr[temp], arr[i]

            swap_res += 1
    
    return swap_res



arr = [4, 3, 1, 2]

print(minimumSwaps(arr))