# Set example - sets is like list but it doesnot contain duplicate element and the order of element will be different.
# sets = {1, 2, 3, 4, 2, 4, 6, 4}
# print(len(sets))
# print(sets)

countrylist = []
for i in range(5):
    country = input("Please enter country list :-")
    countrylist.append(country)

# print("The original country list :- {0}".format(countrylist))
# converttoset = set(countrylist)
# if 'india' in converttoset:
#     print("Attended")
# print("The converted country list :- {0}".format(converttoset))

# ==========================================================================================

# Dictionary example

# lets take above list and check if country exsits then increase the count otherwise add the new country

countrydictionary = {}
for country in countrylist:
    if country in countrydictionary:
        countrydictionary[country] += 1
    else:
        countrydictionary[country] = 1

print("The original country list :- {0}".format(countrydictionary))
