"""
Starting with a 1-indexed array of zeros and a list of operations,
for each operation add a value to each the array element between two given 
indices. inclusive

Once all opertions have been performed, return the maximum value in the array.

example: 

n = 10

queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]

"""
# Method 1
def arrayManipulation(n, queries):
    
    list_of_elements = [0] * n

    for i in queries:
        for j in range(i[0], i[1]+1):

            list_of_elements[j -1] += i[2]
        
    return max(list_of_elements)
    

# Method 2
def arrayManipulation_2(n, queries):
    # Initalizing zero array
    list_of_elements = [0] * n

    for i in queries:
        # adding k value to only first index (list is 1 indexed rather than 0 index)
        list_of_elements[i[0] - 1] += i[2]
        
        # if end index is not matching the lenght of list subtract 
        if i[1] != len(list_of_elements):
             list_of_elements[i[1]] -= i[2]

            
    maxval = 0
    ittr = 0
    
    for q in list_of_elements:
        ittr += q
        
        if ittr > maxval:
            maxval = ittr
            
    return maxval



n = 5
queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]

print(arrayManipulation_2(n, queries))