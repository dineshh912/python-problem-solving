"""
There is a string, s, of lowercase English letters that is repeated infinitely many times. 
Given an integer, n, find and print the number of letter a's in the first a letters of the infinite string.

ex: 
s = "abcac"
n = 10

How many time specific string repeated

"""

def repeatedString(s, n):

    
    return s.count("a") * (n // len(s)) + s[:n % len(s)].count("a")


s = "aba"
n = 10

print(repeatedString(s, n))