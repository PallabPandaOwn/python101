# This is a Tic-Tac-Toe game project with simple logic
# This programe can create a borad and ask to enter row and column values.
def drawfield(field):
    for row in range(5):
        if row % 2 == 0:
            prow = int(row / 2)
            for col in range(5):
                if col % 2 == 0:
                    pcol = int(col / 2)
                    if col != 4:
                        print(field[pcol][prow], end="")
                    else:
                        print(field[pcol][prow])
                else:
                    print("|", end="")
        else:
            print("-----")


# drawfield()

Player = 1
cellList = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
drawfield(cellList)
while True:
    print("Players trun: ", Player)
    MoveRow = int(input("Enter row :- "))
    MoveCol = int(input("Enter col :- "))
    if Player == 1:
        if cellList[MoveRow][MoveCol] == " ":
            cellList[MoveRow][MoveCol] = "X"
            Player = 2
    else:
        if cellList[MoveRow][MoveCol] == " ":
            cellList[MoveRow][MoveCol] = "O"
            Player = 1
    drawfield(cellList)
