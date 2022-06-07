"""
Given an integer array nums, return an array answer such that answer[i] is
equal to the product of all the elements of nums excpt nums[i]

the product of any prefix of suffix of nums is guarnateed to fit in a 32 bit integer.

algorithm should run in O(n) and without using division

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

"""
# O(n^2)
def productExceptSelf(nums):
    output = []
    for i in nums:
        temp = 1
        for j in nums:
            if i != j:
                temp *= j

        output.append(temp)
    
    return output

# O(n)
def productExceptSelf_2(nums):
    
    total = 1
    for i in nums:
        total *= i
    
    output = []
    for i in nums:
        output.append(total//i)

    return output

# O(n) without division              
def productExceptSelf_3(nums):

    pre_prod = []
    for num in nums:
        if pre_prod:
            pre_prod.append(pre_prod[-1]*num)
        else:
            pre_prod.append(num)
            
    
    suf_prod = []
    for num in reversed(nums):
        if suf_prod:
            suf_prod.append(suf_prod[-1]*num)
        else:
            suf_prod.append(num)
    
    suf_prod = list(reversed(suf_prod))
    
    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append(suf_prod[i+1])
        elif i == len(nums) -1:
            result.append(pre_prod[i-1])
        else:
            result.append(pre_prod[i-1] * suf_prod[i+1])
    
    return result 


# O(n) with O(1) memory space

def productExceptSelf_4(nums):
    output = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        output[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(len(nums) - 1,-1, -1 ):
        output[i] *= suffix
        suffix *= nums[i]
    
    return output




print(productExceptSelf_2([1,2,3,4]))