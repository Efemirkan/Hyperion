# Take user's input and case to integer
swimming = int(input("Please enter the swimming time in minutes: "))
cycling = int(input("Please enter the cycling time in minutes: "))
running = int(input("Please enter the running time in minutes: "))

# Calculate total time taken to complete the triathlon and print to display
total_time = swimming + cycling + running
print(f'{total_time} minutes')

# Check if total_time equal or less than 100
if total_time <= 100:
    # Print "Provincial Colours"
    print("Provincial Colours")

# Check if total_time equal or less than 105
elif total_time <= 105:
    # Print "Provincial Half Colours"
    print("Provincial Half Colours")

# Check if total_time equal or less than 110    
elif total_time <= 110:
    # Print "Provincial Scroll"
    print("Provincial Scroll")

# For other conditions print "No award"
else:
    print("No award")
