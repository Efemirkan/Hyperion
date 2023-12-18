'''Write a program that reads in a string and makes each alternate character into an upper case character and 
each other alternate character a lower case character.
e.g. The string “Hello World” would become “HeLlO WoRlD”
'''


# Take input from user
str = input("Enter your sentence: ")

# Initialize variable
str_new =""  # to store new string 

# For loop that iterates through the indices of the list
for i in range(len(str)):
    # If the index is first value in every two value , concatenate str_new string in uppercase
    if i % 2 == 0:
        str_new += str[i].upper()  

    # If the index is second in every two value , concatenate str_new string in lowercase
    elif i % 2 == 1:
        str_new += str[i].lower()

# Print str_new to console
print(str_new)

'''Now, try starting with the same string but making each alternative word lower and upper case.
e.g. The string: “I am learning to code” would become “i AM learning
TO code”'''


# Take input from user
str2 = input("Enter your sentence: ")

# Initialize variables
str_new2 = ""  # to store new string 
list = str2.split(" ")  # split user input by " " to create each word

# For loop that iterates through the indices of the list
for i in range(len(list)):
    # If the index is first word in every two word , concatenate str_new2 string in lowercase
    if i % 2 == 0:
        str_new2 += list[i].lower() + " "

    # If the index is second word in every two word , concatenate str_new2 string in uppercase
    elif i % 2 == 1:
        str_new2 += list[i].upper() + " "

# Print str_new to console        
print(str_new2)

# OR

# Take input from user
str3 = input("Enter your sentence: ")

# Initialize variable
str_new3 = ""  # to store new string

# For loop that iterates through the indices of the list
for i in range(len(str3.split(" "))):
    # If the index is first word in every two word , concatenate str_new3 string in lowercase
    if i % 2 == 0:
        str_new3 += str3.split(" ")[i].lower() + " "

    # If the index is first word in every two word , concatenate str_new3 string in uppercase
    elif i % 2 == 1:
        str_new3 += str3.split(" ")[i].upper() + " "

# Print str_new3 to console 
print(str_new3)


 
# OR


# Take input from user
str4 = input("Enter your sentence: ")

# Initialize variable
word = str4.split(" ")

# For loop that iterates through the indices of the list
for i,w in enumerate(word):
    # If the index is first word in every two word , convert in lowercase
    if i % 2 == 0:
        w = w.lower()

    # If the index is first word in every two word , convert in lowercase
    elif i % 2 == 1:
        w = w.upper()

# Convert the modified word list to a string using the join method and print to console
result = " ".join(word)
print(result)