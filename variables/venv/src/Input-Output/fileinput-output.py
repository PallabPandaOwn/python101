# file input and output

listofcities = ["Bangalore", "Delhi", "Bhubaneswar"]

fileofcities = open("file.txt", "w")
for location in listofcities:
    fileofcities.write(location + "\n")
fileofcities.close()
fileofcities = open("file.txt", "r")
wholecontent = fileofcities.read()
for line in wholecontent:
    print(line, end='')
fileofcities.close()
lastestcity = "Chennai\n"
fileofcities = open("file.txt", "a")
fileofcities.write(lastestcity)
fileofcities.close()
fileofcities = open("file.txt", "r")

wholecontent = fileofcities.read()
for line in wholecontent:
    print(line, end="")
fileofcities.close()

with open("file.txt", "r") as fileofcities:
    for line in fileofcities:
        print(line, end="")
