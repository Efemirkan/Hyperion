age = 24
years_from_now = "3"
# TypeError above this line create years_from_now variable and assign "3" as string, therefore we can not sum it with any integer
# We need to case it to integer first then use it in total_years variable
years_from_now_int = int(years_from_now)
total_years = age + years_from_now_int

# SyntaxError missing brackets in print function, simply add parentheses
# Logical Error i think the program want to output total_years variable but first of all 
# variable called without quatition marks simply delete it and change it to total_years
# otherwise we will get a NameError answer_years is not define beacuse we did not create any variable called answer_years
print ("The total number of years:", total_years)