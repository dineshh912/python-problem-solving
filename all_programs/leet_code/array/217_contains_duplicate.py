"""
Given an integer array nums, return true if any value appears at least twice in the array
and return false if every element is distinct

"""

def containsDuplicate(nums):
    
    if len(set(nums)) != len(nums):
        return True
    else:
        return False



print(containsDuplicate([1,2,3,1]))