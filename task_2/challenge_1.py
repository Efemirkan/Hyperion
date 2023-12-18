import math

# Take user's inputs
side1 = int(input("Please enter the length of first side: "))
side2 = int(input("Please enter the length of second side: "))
side3 = int(input("Please enter the length of third side: "))

# Calculate the area of the triangle
s = (side1 + side2 + side3) / 2
area = math.sqrt(s * ((s - side1) * (s - side2) * (s - side3)))

# Print and display area
print(area)

#or

# Calculate the area of the triangle
area2 = (s * ((s - side1) * (s - side2) * (s - side3))) ** 0.5
# Print and display area
print(area2)