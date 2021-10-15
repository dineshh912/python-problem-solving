"""
Input : array of n-distinct integers
Output : Array with same integers, but sorted
"""

def merge_sort(arr):

    if len(arr) == 0 or len(arr) == 1:
        return arr
    else:

        middle = len(arr) // 2

        a = merge_sort(arr[:middle])
        b = merge_sort(arr[middle:])
        output = []
        while len(a) != 0 and len(b) != 0:
            if(a[0] < b[0]):
                output.append(a[0])
                a.remove(a[0])
            else:
                output.append(b[0])
                b.remove(b[0])
        
        if len(a) == 0:
            output += b
        else:
            output += a

        return output

a = [1, 3, 7, 5, 2, 6, 8, 9]

print(merge_sort(a))