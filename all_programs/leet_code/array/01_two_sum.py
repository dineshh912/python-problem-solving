""""
 Given an array of integers, return indices of the two numbers 
 such that they add up to a specific target.

 example:
    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].

"""

def two_sum(nums, target):
    
    visited = dict()

    for i, v in enumerate(nums): # Loop through numbers
            visited[v] =  i

    for i, v in enumerate(nums):
        if (target - v) in visited and visited[target-v] != i:
            return [i, visited[target-v]]

    return []


print(two_sum([10, 15, 3, 7], 17))

print(two_sum([2, 7, 11, 15],  9))


