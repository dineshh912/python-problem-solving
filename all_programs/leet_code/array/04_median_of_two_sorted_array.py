"""
    Given tow sorted arrays nums 1  and nums2 of size m and n respectively,
    return the median of the two sorted arrays.

    The overall run time complexity should be 0(log(m+n))

    Example:

    nums1 = [1, 3], nums2 = [2]

    output: 2.0000

    merged array [1, 2, 3] and median is 2

"""
# Method 1

from django.urls import translate_url


def findMedianSortedArray(nums1, nums2):

    sorted_list = sorted(nums1 + nums2)

    mid_value = len(sorted_list) // 2

    return (sorted_list[mid_value] + sorted_list[~mid_value]) / 2


# Method 2 Binanry Search approach

def findMedianSortedArray_2(nums1, nums2):

    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    total_length = len(nums1) + len(nums2)
    half_length = total_length // 2

    left_pointer = 0
    right_pointer = len(nums1) - 1

    while True:

        i = (left_pointer + right_pointer) // 2
        j = half_length - i - 2

        l1 = -float('inf') if i < 0 else nums1[i]
        l2 = -float('inf') if j < 0 else nums2[j]
        r1 = float('inf') if i >= len(nums1)-1 else nums1[i+1]
        r2 = float('inf') if j >= len(nums2)-1 else nums2[j+1]

        if l1 <= r2 and l2 <= r1:
            return ([min(r1, r2), (max(l1, l2)+ min(r1, r2)) / 2 ][total_length%2 == 0])
        elif l1 > r2:
            right_pointer = i - 1
        else:
            left_pointer = i + 1


nums1 = [1, 3]
nums2 = [2]

print(findMedianSortedArray_2(nums1, nums2))
"""
Below is the binary search approach

A = [1, 4, 7] 
B = [2, 3, 5, 6]

A+B = [1, 2, 3, 4, 5, 6, 7] # concatenation

In the above [1, 2, 3] is first half and [5, 6, 7 ] is second half
and median is 4

---- In the case of even number of elements
A = [1, 4, 7, 9]
B = [2, 3, 5, 6]

A+B = [1, 2, 3, 4, 5, 6, 7, 9] # concatenation

in the above [1, 2, 3] is first half and [5, 6, 7, 9] is second half
Median is 4+5/2 = 4.5

First array size  = n, so it can be split into n+1
second array size = m, so it can be split into m+1

"""


