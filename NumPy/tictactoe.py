import numpy as np
import random

"""
Write a script to play two-dimensional Tic-Tac-Toe between a human 
player and the computer. Use a 3-by-3 two-dimensional array. Each 
player indicates their moves by entering a pair of numbers representing 
the row and column indices of the square in which they want to place 
their mark, either an 'X' or an 'O'. When the first player moves, 
place an 'X' in the specified square. With the computer choice, place 
an 'O' in the specified square. Each move must be to an empty square. 
After each move, determine whether the game has been won and whether 
it’s a draw. Also, allow the player to specify whether he or she wants 
to go first or second.
"""

# INITIALIZE VARIABLES
board = np.empty((3, 3), dtype=object)
print(board)
comp_turn = True

# ASK IF USER WANTS TO GO FIRST
player_init = input("Do you want to go first? (Type 'y' for yes, 'n' for no): ")
while player_init != "y" and player_init != "n":
    player_init = input("Please type 'y' to go first, or 'n' to go second. ")


# COMPUTER-GENERATED RESPONSE
comp_row = random.randint(0, 2)
comp_col = random.randint(0, 2)
while board[comp_row][comp_col] != None:
    comp_row = random.randint(0, 2)
    comp_col = random.randint(0, 2)
board[comp_row][comp_col] = "O"
print(board)

# ASK USER FOR ROW AND COLUMN INPUT
# NEED TO MAKE SURE IT's NOT WHERE AN O IS
in_row = int(input("Please enter the row of the space you want to mark (1-3): "))
while in_row not in range(1, 4):
    in_row = int(input("Please type a number 1-3 for the row. "))
in_col = int(input("Please enter the column of the space you want to mark (1-3): "))
while in_col not in range(1, 4):
    in_col = int(input("Please type a number 1-3 for the column. "))

board[in_row - 1][in_col - 1] = "X"
print(board)