# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

# When assignin as string to a variable need to use double or single quatition mark, simply add ""
animal = "Lion"
animal_type = "cub"
number_of_teeth = 16

# When used curly brackets it needs to be in f string, simply convert to f string
full_spec = f"This is a {animal}. It is a {number_of_teeth} and it has {animal_type} teeth"

# SyntaxError missing brackets in print function, simply add parentheses
print (full_spec)

