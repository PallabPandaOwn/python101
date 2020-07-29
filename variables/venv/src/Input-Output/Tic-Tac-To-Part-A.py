def drawfield(field):
    for row in range(5):
        if row % 2 == 0:
            Prow = int(row / 2)
            for col in range(5):
                if col % 2 == 0:
                    Pcol = int(col / 2)
                    if col != 4:
                        print(field[Pcol][Prow], end="")
                    else:
                        print(field[Pcol][Prow])
                else:
                    print("|", end="")
        else:
            print("-----")


# drawfield()

Player = 1
cellList = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
drawfield(cellList)
while (True):
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
