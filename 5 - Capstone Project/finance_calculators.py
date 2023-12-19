import math

def main():

    # Take user's input
    user_choice = string_exception("investment", "bond")

    # If user chooses "investment"
    if user_choice == "investment":

        # Take user's inputs
        deposit = numeric_exceptions("How much would you like to deposit? ")
        rate_investment = numeric_exceptions("Enter the interest rate: ")
        year = numeric_exceptions("How many years are you planing to interest? ")
        interest_type = string_exception("simple", "compound")

        # If user chooses "simple"
        if interest_type == "simple":

            # Lambda function to calculate simple interest , 𝐴 = 𝑃(1 + 𝑟 × 𝑡) formula 
            return_investment_simple = lambda deposit, rate_investment, year : (deposit * (1 + (rate_investment * year)))

            # Calculate and print simple interest
            print(f"The amount of interest you'll earn on your investment: {return_investment_simple(deposit, rate_investment, year):,.3f}")

        # If user chooses "compound"    
        else:

            # Lambda function to calculate compound interest, 𝐴 = 𝑃(1 + 𝑟)**𝑡 formula         
            return_investment_compound = lambda deposit, rate_investment, year : deposit * math.pow((1 + rate_investment), year)

            # Calculate and print compound interest
            print(f"The amount of interest you'll earn on your investment: {return_investment_compound(deposit, rate_investment, year):,.3f}")

    # If user chooses "bond" 
    else:

        # Take user's inputs
        house_value = numeric_exceptions("How much is house\'s present value? ")
        rate_bond =  numeric_exceptions("Enter the interest rate: ") / 100
        months =  numeric_exceptions("How many months are you planning of taking repayment? ")
        
        # Lambda function to calculate monthly repayment,  (i * P)/(1 - (1 + i)**(-n)) formula 
        repayment = lambda house_value, rate_bond, months : ((rate_bond / 12) * house_value) / (1 - math.pow((1 + (rate_bond / 12)), -months))

        # Calculate and print monthly repayment
        print(f"You wull have to repay each month: {repayment(house_value, rate_bond, months):,.3f}")

# Define string_exception(string1, string2) funtion to handle exceptions releated to ValueError 
def string_exception(string1, string2):

    # While loop to ask user continuesly until they enter required input
    while True:
    # Take user's input and case-insensitive
        try:
            option = input(f"Enter either '{string1}' or '{string2}' from the menu above to proceed: ").lower()
            
            # If user's input not "investment" or "bond" raise ValueError otherwise return option value
            if option not in [string1, string2]:
                raise ValueError(f"PLease enter ONLY '{string1}' or '{string2}'")
            
            return option
    
        # Print ValueError message
        except ValueError as e:
            print(e) 

# Define numeric_exceptions(prompt) funtion to handle exceptions releated to ValueError
def numeric_exceptions(prompt):

    # While loop to ask user continuesly until they enter required input
    while True:

        # Take user's input
        try:
            user_input = float(input(prompt))
            return user_input
        # Handle expection ValueError and Print error message
        except ValueError:
            print("PLease enter a number of value")

if __name__ == "__main__":
    main()