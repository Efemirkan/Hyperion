# Initialize Variables

menu = ["Egg", "Beans", "Toast", "Mushroom"]  # To store menu items

stock = {
    "Egg" : 10,
    "Beans" : 14,
    "Toast" : 8,
    "Mushroom" : 5     
         }  # To store stocks of items

price = {
    "Egg" : "£2.05",
    "Beans" : "£2.25",
    "Toast" : "£1.55",
    "Mushroom" : "£2.90"     
         }  # To store item's prices

values_list = []  # To store values for each items

# For loop that iterates items in menu and calculate each item's value then append to the values_list
for item in menu:
    # Total = stock * price
    total =  (stock[item]) * (float(price[item].lstrip("£")))
    values_list.append(total)

total_value = 0  # To store total of each value

# For loop that iterates each value in values_list and calculate total value
for i in values_list:
    total_value += i

# Print and display total_value
print(total_value)

    