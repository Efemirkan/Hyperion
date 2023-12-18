# Initialize variables
sum = 0  # to store the sum of numbers
count = 0  # to count the entered numbers

# Keep taking input until -1 is entered
while True:
    try:
        # Take input from user
        num = int(input("Please enter a number (otherwise to stop enter -1): "))        
    except ValueError:
        # Handle non-integer input
        print("Please enter an integer")
        pass
    else:
        # If user types an integer, keep calculating the sum
        if num != -1:
            # Update sum and count
            sum += num
            count += 1
        else:
            # Exit the loop if -1 is entered
            break

# Calculate and display the average   
print(f"The average of the numbers entered is: {(sum / count):.2f}")
