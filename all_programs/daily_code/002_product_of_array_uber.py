"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

"""
# Method 1
def product_of_array(list_of_integers):

    output = []
    
    # convert list into iterator and get the index and its value
    for idx, val in enumerate(list_of_integers):

        list_of_integers[idx] = 1 # chage index into 1

        result = 1 # TO store multiple value


        for i in list_of_integers: # loop through the list
            result *= i # multiply

        output.append(result) # push into new list

        list_of_integers[idx] = val 

    return output

# Method 2
def product_of_array_2(list_of_integers):
    
    output = [] # to store output value
    prod = 1 # To store product value

    for i in list_of_integers:
        prod *= i # Get Product
    
    for i in list_of_integers:
        output.append(prod//i) # divid each value with product

    return output


# Method 3
def product_of_array_3(list_of_integers):

    # Intialize output array
    output = [1]*len(list_of_integers)

    pre_prod = suf_prod = 1
    # Get product of values before index
    for i in range(1,len(list_of_integers)):
        pre_prod *= list_of_integers[i-1]
        output[i] = pre_prod
    
    # Get product of values after index
    for i in range(len(list_of_integers)-2,-1,-1):
        suf_prod *= list_of_integers[i+1]
        
        output[i] *= suf_prod

    return output

# Execution 
list_1 = [20, 2, 3, 4, 5]

print(product_of_array_3(list_1))
