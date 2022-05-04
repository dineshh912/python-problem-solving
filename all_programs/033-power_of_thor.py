"""
Thor moves on a map which is 40 wide by 18 high. 
Note that the coordinates (X and Y) start at the top left! 
This means the most top left cell has the coordinates 
"X=0,Y=0" and the most bottom right one has the coordinates 
"X=39,Y=17".

Once the program starts you are given:
the variable lightX: the X position of the light of power that Thor must reach.
the variable lightY: the Y position of the light of power that Thor must reach.
the variable initialTX: the starting X position of Thor.
the variable initialTY: the starting Y position of Thor.
"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

thorX = initial_tx
thorY = initial_ty

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    directionX = ""
    directionY = ""
    if thorY > light_y:
        directionY = "N"
        thorY -= 1
    elif thorY < light_y:
        directionY = "S"
        thorY += 1
    
    if thorX > light_x:
        directionX = "W"
        thorX -= 1
    
    elif thorX < light_x:
        directionX = "E"
        thorX += 1


    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(directionX + directionY)
