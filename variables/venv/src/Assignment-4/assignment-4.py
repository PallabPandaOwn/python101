# assignment-4

myUniqueList = []
myLeftovers = []  # extra credit question


def additem(item):
    isAdded = False
    check = True

    if len(myUniqueList) != 0:
        for i in myUniqueList:
            if i == item:
                print("Item exits : ", i)
                myLeftovers.append(item)  # extra credit question
                check = False
                break
    if check:
        myUniqueList.append(item)
        print('Item added : ', item)
        isAdded = True

    return isAdded


var1 = additem(1)
print(var1)
var2 = additem(2)
print(var2)
var3 = additem(2)
print(var3)
var4 = additem('Hello')
print(var4)
var5 = additem('Hello')
print(var5)
var4 = additem('world')
print(var5)
print('My Unique List :', myUniqueList)
print('My Leftover List :', myLeftovers)  # extra credit question
