"""
Given an array nums. we define a running sum of an array as

runningSum[i] = sum(nums[0]...nums[i])

return the runnning sum of nums.

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
 

Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6

"""

def runningSum(nums):
    
    sum = 0
    for i, v in enumerate(nums):
        sum += v
        nums[i] = sum
    
    return nums


if __name__ == "__main__":
    nums = [1,2,3,4]
    print(runningSum(nums))