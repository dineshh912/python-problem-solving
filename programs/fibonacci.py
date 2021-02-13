"""
x3 = x1 + x2 

* declare two var
* loop counter

"""

def fibonacci(num):
    num1 = 0
    num2 = 1
    temp = 0
    for i in range(num):
        num1 = num2
        print(num1)
        num2 = temp
        print(num2)
        temp = num1 + num2
        # print(temp) 

# fibonacci(5)

# https://www.geeksforgeeks.org/python-program-for-program-for-fibonacci-numbers-2/

n1, n2 = 0, 1
count = 0
nterms = 5

while count < nterms:
    print(n1)
    temp = n1 + n2
    n1 = n2
    n2 = temp
    count +=1