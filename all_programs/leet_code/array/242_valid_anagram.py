"""
given two strings s and t return true if t is an anagram of s and false 
otherwise

Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false
"""

def isAnagram(s, t):
    if len(s) != len(t):
        return False

    d1, d2 = {}, {}

    for i in range(len(s)):
        d1[s[i]] = 1 +  d1.get(s[i], 0)
        d2[t[i]] = 1 +  d2.get(t[i], 0)

    for i in d1:
        if d1[i] != d2.get(i, 0):
            return False
        else:
            continue
    
    return True
    
    
    
def isAnagram2(s, t):

    return sorted(s) == sorted(t)



print(isAnagram2("rat", "car"))