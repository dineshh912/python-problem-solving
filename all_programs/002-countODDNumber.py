# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

def countOdds(low, high):

    # Check if low and high values are odd

    if low % 2 == 1:
        low_value = low # It's a odd value
    else:
        low_value = low +1
    
    if high % 2 == 1:
        high_value = high # if it's odd value
    else:
        high_value = high - 1

    count = (high_value - low_value) //2 + 1

    return count

countOdds(8, 10)