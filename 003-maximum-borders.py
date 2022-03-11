"""
You are given a table with n rows and  m columns. Each cell is colored with white or black. 
Considering the shapes created by black cells, what is the maximum border of these shapes? 
Border of a shape means the maximum number of consecutive black cells in any row or column without any white cell in between.

A shape is a set of connected cells. Two cells are connected if they share an edge. Note that no shape has a hole in it.
"""
list_of_blocks = [
        [1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1]
    ]


count = 0
list_of_counts = []
for row in list_of_blocks:
    
    for column in range(0, len(row)-1):
        if(row[column] == 1):
            count+=1
        else:
            count = 0

    list_of_counts.append(count)

print(list_of_counts)
        