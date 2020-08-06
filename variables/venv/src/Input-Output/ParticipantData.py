# participant list
# read/write participant file and do some statitics on the data.

participantNumber = input("How many participant do you want to insert :- ")
participantData = []
registerParticipant = 0
file = open("ParticipantData.txt", "w")
while (registerParticipant < participantNumber):
    tempPartData = []  # list of data - [name,country,age]
    name = input("Name :- ")
    tempPartData.append(name)
    country = input("Country :- ")
    tempPartData.append(country)
    age = int(input("Age :- "))
    tempPartData.append(age)
    participantData.append(tempPartData)
    registerParticipant += 1
print("Entered participantData list :- ", participantData)

for participant in participantData:
    for data in participant:
        file.write(str(data))
        file.write(" ")
    file.write("\n")
file.close()

inputFile = open("ParticipantData.txt", "r")
# inputFile.readline()
inputList = []
for readData in inputFile:
    tempData = readData.strip("\n").split()
    # print(tempData)
    inputList.append(tempData)
print("Read participant list :- ", inputList)
Age = {}
for i in inputList:
    if i[-1] in Age:
        Age[i[-1]] += 1
    else:
        Age[i[-1]] = 1
print("Read Age dictionary :- ", Age)

countriesList = {}
for i in inputList:
    if i[-2] in countriesList:
        countriesList[i[-2]] += 1
    else:
        countriesList[i[-2]] = 1

print("Read country dictionary :- ", countriesList)

oldestAge = 0
youngestAge = 100
mostOccuringAge = 0
counter = 0
for tempAge in Age:
    if tempAge > oldestAge:
        oldestAge = tempAge
    if tempAge < oldestAge:
        youngestAge = tempAge
    if Age[tempAge] > counter:
        counter = Age[tempAge]
        mostOccuringAge = tempAge
print("Oldest Age :- ", oldestAge)
print("Youngest Age :- ", youngestAge)
print("Most occuring Age is :- ", mostOccuringAge, "with", counter, "participant")
# print("Youngest Age :- ", youngestAge)
inputFile.close()
