"""
There is a collection of input strings and a collection of 
query strings. For each query string, determine how many times it occurs 
in the list of input strings. Return array of the result.

Example:

strings = ["ab", "ab", "abc" ]
queries = ["ab", "abc", "bc"]

result = [2, 1, 0]

"""
# Brutforce Method
def matchStrings(strings, queries):
    count = 0
    result = []
    for i in queries:
        for j in strings:
            if i == j:
               count += 1
        result.append(count)
        count = 0
    
    return result
        

print(matchStrings(["ab", "ab", "abc" ],  ["ab", "abc", "bc"]))