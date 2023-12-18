# Take user's input
str_manip = input("Please enter a sentence: ")

# Calculate and display length of str_manip
print(len(str_manip))

# Find the last letter in str_manip variable and replace every occurrence of this letter in str_manip with ‘@’.
print(str_manip[len(str_manip)-1])

# Replace every occurrence of last letter with "@" and display
str = str_manip.replace(str_manip[len(str_manip)-1], "@")
print(str)

# Print the last 3 characters in str_manip
str = str_manip[-3::]
print(str[::-1])


# Create a five-letter word that is made up of the first three characters and the last two characters in str_manip
str5 = str_manip[0:3] + str_manip[-2:]

# Print and display str5
print(str5)