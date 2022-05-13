"""
    You are given an integer array height of length n,
    there are n vertical lines drawn such that the two endpoints
    of the ith line are (i, 0) and (i, height[i]).

    find two lines that together with the x-axis form a container, 
    such that the container contains the most water.

    Return the maximum amount of water a container can store.

    We can't slant the container.

    input: [1,8,6,2,5,4,8,3,7]
    output: 49

    constraints:
    1. n == height.length
    2  2 <= n <= 100000
    3. 0 <= height[i] <= 10000

"""
# Method 1 - Brute Force
def maxArea(height):
    area = 0
    for i in range(len(height)):
        for j in range(i+1, len(height)):
            area = max(area, min(height[i], height[j])*(j-i))

    return area


# Method 2 -
def maxArea2(height):
    # get the first and last elemet index
    first_index = 0
    last_index = len(height) -1
    area = 0
    # run the loop until the first is less than last
    while first_index < last_index:
        # Find the area
        area = max(area,
             min(height[first_index], height[last_index])*(last_index-first_index))
        # if the first is less than last, move the first index
        if height[first_index] < height[last_index]:
            first_index += 1
        else:
            last_index -= 1
    
    return area



if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(maxArea2(height))