# Data structures

In simpler terms data structures is helps us to store, access and manage the data effeciently. Data is nothing but eveything we feed into the system as input.

Lets take a Travel analogy, There are different mode of transport available, Air, train, Road. We can't take train or aircraft when we want to go to next street. it's not efficient. like wise if we want to carry lot's of passenger we can't depend on the bus. if we want to go the location immediently where time is important likely we choose air travel. as whole method of chossing the container (mode of transport) is called Datastructure.

* Data structure main thing to consider - Capacity and its effiecent usage
* Algorithm - Effienceny and design
* Algorithm analysis - Size complexity, Time complexity

  * Worst case: Algortiham takes maximum running time for the input size to execute. The worst case analysis is useful because algorithm can't execute in a time that is greater than the worst case.
  * Average case: Calculating average case is difficult, because it varies based on input size.
  * Best case: Minimum running time takes for the program to run, this is not much informative since it doesn't show the real execution time of an algorithm.

  * Predict algortihm performance
  * Scalability
  * How it's behave for different algorithms.
  * Algorithm affects datastructure performance.
  * Program = Algorithm + Data structure

## Abstract Data type (ADT)

In order to drive a car we no need to be a mechanic. we need to know only the essential to drive the vechicle. at the same time we don't learn all the car model in the world to get licence.

ADT basically hide the details and give only essential and it helps to hold the set of values objects can have. EX: List - Pop, delete, add

ADT = Properties + Operations it's equicvalent to Class in OOPS.

Propertiy = List, Operation = Pop, add, delete.

sqrt(int 10) = sqrt is the operation, int is the propery, 10 is the object

ADT is formal description. It's design by contract.

Data represesntation in ADT :

* Make all data private
* Use getters and setters to modify the value with condition.

## Big O Notations

How effieciently you are solving the problem, big O helps to define that.

Big O Known as Worst-case scenario of a program. given a very large input the big-o will give us an idea of how slow our algorithm may run.

n - just for loop
n^2 - Two for loop
log(n) - Divide in half or multiple by double
n^3 - Three for loop

* O(1) - Constant Time - 1 - Array index Lookup
* O(log n) - Logartithmic Time - log(n) - If the input size doubles the run time increase by one - Binary search
* O(n) - Linear Time  - n - if the input size diubles run time doubles - Sequential search
* O(n log n) - Superlinear Time - n log n - heap sort
* O(n^2) - Quadratic Time - n^2 - if the input size doubles runtime quadupls - Bubble sort
* O(n^3), O(n^c) - Cubic Time / Polynomial Time - n^3
* O(c^n) - Exponential - 2^n - If the input size increase by one, the run time doubles - Traveling salesman
* O(n!) - n! - Brutforc traveling salesman
* O(n^n)

## Big-Omega

Big omega known as best case, it's not very informative because it won't give actual run time of the program. While Big-O gives upper bound
Big-Omega gives lower bound. This shows how fast our algorithm can run.

## Big-Theta

Big-Theta is average case runnning time. It's a mean running time of our algorithm.

## Linear Search

Operation count(O) increase exactly with the number of elements(n). If i have 1 trash bag, i have to take out trash once, so it's O(1). if it's two trash bag O(2) like wise O(n).

When we want to find the number in the list, best case for linear search is O(1),because the element can be first in the list.
The average and worst case always linked with size (length of the list) so the time complexity will be O(n)

## Binary Search

For a binary search, the best case O(1). The item located in mid point. The worst and average case is O(log n).
Log is a way of experessing an exponent for a given base. so if there are 16 elements, it would take worst case 4 steps to find the number 15.

## Bubble sort, insertion sort, selection sort

O(n^2)
