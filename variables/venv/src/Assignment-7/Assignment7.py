# Return to your first homework assignments, when you described your favorite song.
# Refactor that code so all the variables are held as dictionary keys and value.
# Then refactor your print statements so that it's a single loop that passes through each item in the dictionary and prints out it's key and then it's value.

Artist = "Shyam kumar"  # Artist of song
Genre = "Jazz"  # gener of song
YearReleased = 2020  # year of realesed
Duration = 120.5  # duration of song
Music = "ABC Company"  # music company

songs = {"Artist": "Shyam Kumar", "Genre": "Jazz", "YearReleased": "2020", "Duration": "5 min", "Music": "ABC Company"}

for i in songs.keys():
    print("Key is {0} and Value is {1}".format(i, songs[i]))


def checkvalue(key, value):
    if key in songs:
        if songs[key] == value:
            return True
        else:
            return False
    else:
        return False


inputkey = input("Please enter the key :-")
inputvalue = input("Please enter the value :-")

output = checkvalue(inputkey, inputvalue)
print(output)
