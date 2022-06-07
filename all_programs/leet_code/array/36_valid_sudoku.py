"""
Determine if the 9*9 sudoku board is valid. only the filed cells need to be
validated according to the following rules.

1. Each row must contain the digits 1-9 without repetation
2. Each clouum must contain the digit 1-9 without repetation
3. each of 3*3 sub boxes of the grid must contain the digit 1-9 without repetation

Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

"""

def isValidSudoku(board):
    
    for i in board:
        for j in board:
            pass




board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))