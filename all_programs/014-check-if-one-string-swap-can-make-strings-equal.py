"""
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string 
(not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings.
Otherwise, return false.

 
Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".
Example 2:

Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.
Example 3:

Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.
 
"""

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        if len(s1) != len(s2):
            return False
        
        if s1 == s2:
            return True

        A = []
        B = []
        
        
        for i in range(len(s1)):

            # if the characte is differenr
            if s1[i] != s2[i]:

                A.append(s1[i])
                B.append(s2[i])

            if len(A) == len(B) == 2:

                if A[0] == A[1] and B[0] == B[1]:
                    return True
        
        return False
        



test = Solution()

print(test.areAlmostEqual("hello", "hlelo"))