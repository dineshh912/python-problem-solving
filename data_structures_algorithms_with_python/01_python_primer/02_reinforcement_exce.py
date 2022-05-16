"""
R-1.1 : Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.

"""
def is_multiple(n, m):
    return n % m == 0

"""
Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.

"""
def is_even(k):
    # using bit wise operator
    return (k & 1)


"""
R 1-3 Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.
"""
def minmax(data):
    sorted_data = sorted(data)
    
    return sorted_data[0], sorted_data[-1]



if __name__ == "__main__":
    print(minmax([1, 4, 3, 88, 0, -5]))

