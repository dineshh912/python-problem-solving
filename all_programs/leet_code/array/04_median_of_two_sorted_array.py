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

def findMedianSortedArray(nums1, nums2):

    sorted_list = sorted(nums1 + nums2)

    mid_value = len(sorted_list) // 2

    return (sorted_list[mid_value] + sorted_list[~mid_value]) / 2



# Method 2
def findMedianSortedArray_2(nums1, nums2):
    pass



nums1 = [1, 3]
nums2 = [2]

print(findMedianSortedArray(nums1, nums2))