# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

# SyntaxError print() funtion used without brackets, simply add brackets 
print ("Welcome to the error program")

# IndentationError the statement indented incorrectly, simply align to the left for a Tab
# SyntaxError print() function used without brackets, simply add brackets 
print ("\n")

# Variables declaring the user's age, casting the str to an int, and printing the result
# IndentationError the statement indented incorrectly, simply align the scope to the left for a Tab
# In python snake_prefer to use instead of camelCase 
# NameError because misuse == it is not a conditional check, we need to use assigning element =
age_str = "24" 

# Runtime error can not convert a string as integer, program can coerce the integer as string but not string to integer
# in line 16 i will delete the "years old" from the sting
age = int(age_str) 

# Then TypeError will have emerged. Only concatenate string to string to correct it we can use f string
# By the way good to use backslash \ before ' as escape sequence
print(f"I\'m {age} years old.")

# Variables declaring additional years and printing the total years of age
# IndentationError the statement indented incorrectly, simply align the scope to the left for a Tab
years_from_now = "3"
# TypeError above this line create years_from_now variable and Runtime error assign "3" as string, therefore we can not sum it with any integer
# We need to case it to integer first then use it in total_years variable
years_from_now_int = int(years_from_now)
total_years = age + years_from_now_int

# SyntaxError missing brackets in print function, simply add parentheses
# Logical Error i think the program want to output total_years variable but first of all 
# variable called without quatition marks simply delete it and can not concatenate int to str which emerge TypeError
# above code we use f string , still we can use f string but to show diffent tpye we can use a comma
# and change it to total_years otherwise we will get a NameError answer_years is not define 
# beacuse we did not create any variable called answer_years

print ("The total number of years:", total_years)

# Variable to calculate the total amount of months from the total amount of years and printing the result
# NameError because we did not define any variable called total our variable is total_years, simply replace it
total_months = total_years * 12
# SyntaxError missing brackets in print function, simply add parentheses
# TypeError can not concatenate int to str, simply use f string and we need to add another six months to add our variable
print (f"In 3 years and 6 months, I'll be {total_months + 6} months old")

#HINT, 330 months is the correct answer

