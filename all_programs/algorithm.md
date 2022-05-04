* Algorithm is set of well-defined rules to solve computational problem.

### integer Multiplication

* Input is two n-digit numbers (x and y)
* lenght of x and y is n (positive number)
* output = x . y
* In typical way we will do partial multiplication with each number on the y with x and add everything together.
* This method take lots of time to compute for larger integer value.

##### Recursive Algorithm

*  Recursive algorithm involved multiplication of number with fewer digits.
*  x = 10^n/2 * a+b
*  y = 10^n/2 * c+d
*  x.y = (10^n/2 * a+b)*(10^n/2 * c+d)
   *  = 10^n * (ac)+10^n/2*(ad+bc)+bd
  
#### Karatsuba multiplication

* This algorithm is obtimized version on recursive algorithm.
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

#### Merge sort

* Divide and conquer algorithm
* Basic idea is break problem into smaller sub problems, solve the small problems and combine
* Input : Array of N - numbers
* Output :  Array of same numbers, sorted from smallest to largest
* 

