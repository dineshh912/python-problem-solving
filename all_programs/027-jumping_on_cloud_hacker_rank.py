"""

There is a new mobile game that starts with consecutively numbered clouds.
Some of the clouds are thunderheads and others are cumulus.
The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2. 
The player must avoid the thunderheads. Determine the minimum number of jumps 
it will take to jump from the starting postion to the last cloud. It is always possible to win the game.

For each game, you will get an array of clouds numbered  if they are safe or  if they must be avoided.

"""

def jumpingOnClouds(c):

    converting_into_string = [str(s) for s in c] # for easier manipulation
    jump_string = ''.join(converting_into_string) # joining the string

    jump = jump_string.count("1") # How many jump, based on 1

    split_array = jump_string.split("1") # split the jump string based on 1

    for i in split_array:
        jump += len(i) // 2
    
    return jump
 


c = [0, 0, 1, 0, 0, 0]

print(jumpingOnClouds(c))