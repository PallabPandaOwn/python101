# Assignment 6
# Create a function that takes in two parameters: rows, and columns, both of which are integers.
# The function should then proceed to draw a playing board (as in the examples from the lectures) the same number of rows and columns as specified.
# After drawing the board, your function should return True.

import shutil

maxcol = shutil.get_terminal_size()[0]
maxrow = shutil.get_terminal_size()[1]
print("Max column size : {0}  and Max row size : {1} are available in current terminal".format(maxcol, maxrow))


def create_board(cols, rows):
    if cols <= maxcol and rows <= maxrow:
        for r in range(rows):
            for s in range(cols):
                print("|_", end="")
            print("|")
        return True
    else:
        print("specified rows and cols are bigger than terminal max row and col size")
        return False


if create_board(10, 100):
    print("Board has been created successfully")
else:
    print("Failed to create board")
