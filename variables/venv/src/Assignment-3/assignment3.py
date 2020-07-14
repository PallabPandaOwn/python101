# para1= 1
# para2 =2
# para3=3
def checkequality(para1, para2, para3):
    if para1 == para2 or para1 == para3:
        return True
    elif para2 == para1 or para2 == para3:
        return True
    elif para3 == para1 or para3 == para2:
        return True
    else:
        return False


output = checkequality(1, 2, 3)
print(output)

# extra credit

output1 = checkequality(1, 2, int("2"))
print(output1)
