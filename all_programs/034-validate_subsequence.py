"""
Given two non-empty arrays of integers, write a function that determines
whether the second array is a subsequence of the first one.

A subsequence of an array is a set of numbers that aren't necessarily
adjacent in the array but that are in the same order as they appear in the array.
for instance, the numbers [1, 3, 4] for a subsquence of the array [1, 2, 3, 4]. 
so do the numbers [2, 4]. Note that a single number in the array is also a subsequence.

sample input:

array = [5, 1, 22, 25, 6, -1, 8, 10]
subsequence = [1, 6, -1, 10]

sample output:

True

"""


def isValidSubsequence(array, sequence):
    # Write your code here.
    sequence_index = 0
    for i in array:
        if sequence_index == len(sequence):
            break
        if sequence[sequence_index] == i:
            sequence_index += 1
    
    return sequence_index == len(sequence)
        


input = {
  "array": [5, 1, 22, 25, 6, -1, 8, 10],
  "sequence": [5, 1, 22, 23, 6, -1, 8, 10]
}

print(isValidSubsequence(input["array"], input["sequence"]))