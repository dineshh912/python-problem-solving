"""
Given an integer array nums and an integer k, return the k most frequent elements.

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

# Bucket sort
"""

def topKFrequent(nums, k):
    # Storing counter values
    count = {}
    # Bucket sort method, store counter values with index
    frq = [[] for i in range(len(nums) + 1)]
    

    for i in nums:
        count[i] = 1 + count.get(i, 0)

    for k, v in count.items():
        frq[v].append(k) 

    res = []
    for i in range(len(frq) - 1, 0, -1):
        for n in frq[i]:
            res.append(n)
    
    return len(res)
        


print(topKFrequent([1,1,1,2,2,3], k = 2))