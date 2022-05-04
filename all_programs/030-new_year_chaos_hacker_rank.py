"""
It is New Year's Day and people are in line for the Wonderland rollercoaster ride.
Each person wears a sticker indicating their initial position in the queue from 1 to n.
Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker. 

One person can bribe at most two others. Determine the minimum number of bribes that took place to get to a given queue order.
Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.
"""

def minimumBribes(q):
    # Write your code here
    bribes = 0 # initial value to store res

    for index, value in enumerate(q): # Get index and value using enumerater
        
        current_value = index + 1 # sine list start at 0 make sure to add 1, Match the queue

        if value - current_value > 2: # if queue is more than index value print too chaotic
            return "Too chaotic"


        for i in range(max(value-2, 0), index):
            
            if q[i] > value:
                bribes+=1
        
    
    return bribes



q = [2, 1, 5, 3, 4]

print(minimumBribes(q))