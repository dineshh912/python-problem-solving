"""
Given a 6x6 2D Array, arr :

An hourglass in A is a subset of values with indices falling in this pattern in arr's graphical representation:

There are 16  hourglasses in arr. An hourglass sum is the sum of an hourglass' values. 
Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum. The array will always be .
"""

def hourglassSum(arr):
    # Write your code here
    hr_glass = []

    for i in range(0, len(arr)-2):

        for j in range(0, len(arr)-2):  

            total = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])

            hr_glass.append(total)
    
    return max(hr_glass)



arr =  [[1,1,1,0,0,0],
        [0,1,0,0,0,0],
        [1,1,1,0,0,0],
        [0,0,2,4,4,0],
        [0,0,0,2,0,0],
        [0,0,1,2,4,0]]

print(hourglassSum(arr))