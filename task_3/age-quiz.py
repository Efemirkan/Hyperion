# While loop to ask continuously for user input
while True:
    try:
        #Take user's input and case to integer
        age = int(input("How old are you? "))
        # Break when user's type an integer
        break

    # Handle releated to ValueError
    except ValueError:
        # Print "Please enter a integer"
        print("Please enter a integer")
    
# Check if age greater than 100
if age > 100:
    # Print "Sorry, you're dead."
    print("Sorry, you're dead.")

# Check if age equal or greater than 65
elif age >= 65:
    # Print "Enjoy your retirement!"
    print("Enjoy your retirement!") 

# Check if age equal or greater than 40
elif age >= 40:
    # Print "You're over the hill."
    print("You're over the hill.") 

# Check if age equal to 21
elif age == 21:
    # Print "Congrats on your 21st!"
    print("Congrats on your 21st!")

# Check if age less than 13
elif age < 13:
    # Print "You qualify for the kiddie discount."
    print("You qualify for the kiddie discount.")

# In other conditions, print "Age is but a number." 
else:
    print("Age is but a number.")

