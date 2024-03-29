"""
Monk and Rotation
Monk loves to preform different operations on arrays, and so being the principal of Hackerearth School,
 he assigned a task to his new student Mishki. 
 Mishki will be provided with an integer array A of size N and an integer K , 
 where she needs to rotate the array in the right direction by K steps and then print the resultant array. 
 As she is new to the school, please help her to complete the task.
"""
# Slicing method
'''
t = int(input())

while t!=0:
    n, k = map(int, input().split())
    arr = list(input().split())

    new_list = arr[-k:]+arr[:-k]

    print(' '.join(new_list))

'''
# Method 2
t  = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    index_to_split = k%n
    print(index_to_split)
    print(*(a[n-index_to_split:]+a[:n-index_to_split]))