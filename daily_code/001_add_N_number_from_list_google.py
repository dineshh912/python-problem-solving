"""
Given a list of numbers and a number k, return whether any two numbers from the list add upto k

input: [10, 15, 3, 7] and k = 17

output: true, 10+7 = 17

"""
# Bruntforce method

def two_sum(list_of_numbers, k):
    
    for i in range(len(list_of_numbers)): # loop through array
        
        for j in range(len(list_of_numbers)): # loop through array

            if i !=j and list_of_numbers[i] + list_of_numbers[j] == k: 
                # if both number not same and added value gives k then return true

                return True
    
    return False


# Method 2:

def two_sum_set(list_of_numbers, k):

    visited = set() # to store already visited numbers

    for i in list_of_numbers: # Loop through numbers

        if k - i in visited: # check k - i ie(17-10 = 7) 
            return True
        
        visited.add(i) # add it to set, we are using set to avoid duplicate

    return False

print(two_sum_set([10, 15, 3, 7], 17))