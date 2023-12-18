# For loop that iterates i variables in range 10 and check conditions
for i in range(10):
    # Check if i <= 5 and print i times *
    if i <= 5:
        print("*" * i)
    # Check if i > 5 and print 10-i times *
    else:
        print("*" * (10 - i))

