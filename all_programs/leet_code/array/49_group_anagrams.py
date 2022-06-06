"""
Given an array of strings, group the anagram together. you can return the answer in any order.

An anagram is a word or pharse formed by rearranging the letters of a different word or pharse.
typically using all the original letters exactly once.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

"""
from collections import defaultdict


def groupAnagrams(strs):
    
    res = defaultdict(list)

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1 
        
        res[tuple(count)].append(s)
    
    return list(res.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))