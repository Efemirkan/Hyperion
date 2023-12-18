#  Write a program with two compilation errors, a runtime error and a logical error.
# define main function to take user's input and output as required
def main():
    x, y = get_input("Fraction: ")
    fuel(x, y)

# define get_input function to prevent ValueError, ZeroDivisionError and situation fuel filled more than %100
def get_input(prompt):
    while True:
        # get input and split them x and y then case them to integer
        try:
            x, y = input(prompt).split("/")
            x = int(x)
            y = int(y)
        # prevent ValueError and ZeroDivisionError
        # If we not use ZeroDivisionError a RuntimeError will emerge
        except (ValueError, ZeroDivisionError):
            pass
        else:
            # prevent situaion fuel filled more than %100
            if x <= y:
                return x, y
            else:
                pass

# define fuel function to output correctl in each condition
def fuel(x, y):
    # unless we multiply by 100 we can not get a percentage and Logical Error will occur
    fraction = round((x / y) *100)
    if fraction == 0 or fraction == 1:
        print("E")
    elif fraction == 99 or fraction == 100:
        print("F")
    else:
        print(f"{fraction}%")


main()