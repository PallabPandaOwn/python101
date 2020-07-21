# Tik Tac To shape

for row in range(5):
    if row % 2 == 0:
        for col in range(1, 6):
            if col % 2 == 1:
                if col != 5:
                    print(" ", end="")
                else:
                    print(" ")
            else:
                print("|", end="")
    else:
        print('-----')
