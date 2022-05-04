"""
Stepes involved in karastuba multiplication

* split whole number into smaller section of number(2534 = 25, 34) 
* Ex : 1234 * 5678
  * 12 = a , 34 = 6, 56 = c, 78 = d
  * 1st = a*c
  * 2nd = b*d
  * 3rd = (a+b)*(c+d)
  * 4th = 3rd - 1st - 2nd
  * 10^4 * 1st + 10^2 * 4th + 2nd =  ans 

* With above example
  * Computr a*c
  * Compute b*d
  * compute(a+b)*(c+d)
  * Subtract third step result with first two steps 
  * Add step 1, 2, 4 after adding 10^n trailing zero to step 1, 10n/2 trailing zero to step 4
"""

def karatsuba(x,y):
    # if x & y are single digit number just multiply and return it.
    if len(str(x)) == 1 or len(str(y)) == 1: 
        return x*y
    else:
        # Find which input length is maximum so we can split it 
        n = max(len(str(x)),len(str(y)))
        half_N = n // 2
        
        a = x // 10**(half_N)
        b = x % 10**(half_N)
        c = y // 10**(half_N)
        d = y % 10**(half_N)

        print(a, b, c, d)
        ac = karatsuba(a,c)
        bd = karatsuba(b,d)

        print(ac, bd)
        ad_plus_bc = karatsuba(a+b,c+d) - ac - bd
        
        # this little trick, writing n as 2*nby2 takes care of both even and odd n
        prod = ac * 10**(2*half_N) + (ad_plus_bc * 10**half_N) + bd
        return prod

print(karatsuba(1234,5678))
