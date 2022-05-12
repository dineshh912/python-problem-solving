"""
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area,
formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

Input: nums = [2,1,2]
Output: 5

"""

def largestPerimeter(nums):
    
    nums.sort(reverse=True) # sorting
    for i in range(3, len(nums)+1):
        if(nums[i-3] < nums[i-2] + nums[i-1]):
            return nums[i-3]+nums[i-2]+nums[i-1]
    return 0


largestPerimeter([1, 2, 1])