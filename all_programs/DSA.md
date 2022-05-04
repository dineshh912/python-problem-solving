# Data structure

A Data structure is a way of organizing data so that it can be used effectively.
when we write the program the content in the program needs to be stored some where effieciently. Data structure will take care of this.

* Data structure
  * Capacity an its efficeient usage.
  * How to efficiently store, access, manage data.
  * Data structure effects algorithm's performance.
* Algorithm
  * Efficiency and it's design
* Algorithm analysis
  * Size Complexity
  * Time Complexity
  * Worst case, Best case, Average
  * How to predict an algorithm performance
  * How well algorithm scales up
  * How to compare different algorithms for a problem

Data structure is just a container, algorithm is the one give life to the data structure.
Program = Algorithm + Data structures

## Why Data structure?

* They are essenital ingredients in creating fast and powerful algorithms.
* They help to manage and organize data.
* They make code cleaner and easier to understand.

## Abstrct data types VS Data structure

An abstract data type is an abstraction of a data structure which provides only the interface to which a data structure must adhere to. The interface doesn't give any specific details about how something should be implemented or in what programming language.
ex:  Person A want to travel from Point X to Z. in this specific mode of transport ie walking/train/bus is data structure. what we want to do is abstrcact data type. some more example below.
| Abstract Data Type | Data structures |
|--------------------|-----------------|
| List | Dynamic Array, Linked List |
| Queue | Linked list based Queue, Array based, stack based |
| Map | Tree Map, Hash Map, Hash Table |
| Vechicle | Golf cart, Bicycle, smart car |

## Computational Complexity Analysis

Programmers often asking the same two questions.

* How much time does this algorithm need to finish?

* How much space does this algorithm need for its computation?

### Big-O Notation

Big-O notation gives an upper bound of the complexity in the worst case, helping to quantify performance as the input size becomes arbitratily large. Big-O only cares about worst case.
ex : if you want to search some number in unorder list. the worst case will be the number present in last element of the list. so time complexity will linear to the elements in the list. because it's visiting every single element until it find the correct element. same concpt applies to the space.

    n - The size of the input (complex order smallest to largest)

        Constant Time : O(1)
     Logarithmic Time : O(log(n))
          Linear Time : O(n)
    Linearithmic Time : O(nlog(n))
         Quadric Time : O(n^2)
           Cubic Time : O(n^3)
     Exponential Time : O(b^n), b > 1
       Factorial Time : O(n!)

#### Big-O Properties

    O(n+c) = O(n)
       O(cn) = O(n), c > 0

Big O cares only when it's the worst case where n might be infinity. Add/multiply constant with infinity results in infinity.

If F is the function that describes the running time of the particular algorithm for an input of size n:

    f(n) = 7log(n)^3 + 15n^2 + 2n^3 + 8
    
    O(f(n)) = O(n^3) ; n^3 is the dominent in the function.

#### Big-O Example

Constant time : O(1)

    a := 1             i := 0
    b := 2             While i < 11 DO
    c := a + 5*b           i = i + 1

They don't depend on N. so both above example run in constant time. even input gets large it's still gonna run in constant time.

Linear Time : O(n)

       f(n) = n        f(n)  = n/3
    O(f(n)) = O(n)   O(f(n)) = O(n)

Quadratic Time : O(n^2)

    for(i=0; i < n; i++)
        for(j = 0; j < n; j++)
    
    f(n) = n*n = n^2, O(f(n)) = O(n^2)

    for(i=0; i < n; i++)
        for(j = i; j < n; j++)

The second example also run in quadratic time, since i goes from [0,n]. the amount of loop determined by i. if i=0, n work, if i=1, n-1 work and n-2 etc. so it becomes

    (n) + (n-1) + (n-2) + (n-3) + ...+ 3 + 2 + 1 
    O(n(n+1)/2) = O(n^2/2 + n/2) = O(n^2)

* Finding all subset of a set - O(2^n)

* Finding all permutations of a string - O(n!)

* Sorting using merge sort - O(nlog(n))

* Iterate over all the cells in a matrix of size n by m - O(nm)
