# Slicing is creating a substring by extracting elements from another string. 
# This is accomplished with indexing[] and slicing()
# [start:stop:stop]

name = "Bro Code"

first_name = name[:3] # Everything from the start to the third character (by the index)
print(first_name)
last_name = name[4:] # Everything from the fourth character to the end
print(last_name)
funky_name = name[0:8:2] # From 0 to 8 by the index, every other character
print(funky_name)
reversed_name = name[::-1] # Prints the whole string, reversed
print(reversed_name)


website1 = "https://google.com"
website2 = "https://wikipedia.com"

slice = slice(8, -4) # the -4 in the stop portion (start, stop, step) means up until 4 characters from the end
print(website1[slice])
print(website2[slice])
