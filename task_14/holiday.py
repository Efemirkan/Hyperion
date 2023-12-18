def main():

    # Dictionary of destinations and their costs
    destinations = {
    "Paris" : 65,
    "Berlin" : 40,
    "Lisbon" : 55,
    "Madrid" : 80,
    "Barcelona" : 85,
    "Milano" : 75,
    "Rome" : 70,
    "London" : 110,
    "Copanhagen" : 120,
    "Istanbul" : 105
    }

    # Take user's inputs for destination, number of nights, and car rental days
    city_flight = string_exception(destinations, "Destination: ")
    num_nights = int_exception("How many days will you stay? ")
    rental_days = int_exception("For how many days would you like rent a car? ")

    # Lambda function to calculate hotel_cost 
    hotel_cost = lambda num_nights : 65 * num_nights  # Per day cost £65

    # Lambda function to calculate plane_cost
    plane_cost = lambda city_flight, destination : destination[city_flight]

    # Lambda function to calculate car_rental
    car_rental = lambda rental_days : 35 * rental_days  # Per day cost £35

    # Calculate and print hotel_cost, plane_cost and car_rental
    print(f"{num_nights} nights in {city_flight} costs : £{hotel_cost(num_nights)}")
    print(f"Flight to {city_flight} costs : £{plane_cost(city_flight, destinations)}")
    print(f"{rental_days} nights car rental costs : £{car_rental(rental_days)}")

    # Lambda function to calculate total cost of holiday
    holiday_cost = lambda x, y, z : x + y + z

    # Calculate and Display the total cost for holiday
    print(f"Holiday will cost you in total : £ {holiday_cost(hotel_cost(num_nights), plane_cost(city_flight, destinations), car_rental(rental_days))}")

# Define string_exception(destination, promtp) function to handle ValueError
def string_exception(destination, promtp):

    # While loop continues until a valid input is provided
    while True:

        # Take user's input, capitalize the first letter, and remove white blanks
        try:
            city_flight = input(promtp).capitalize().strip()

            # If user's input not in destinatio dict, raise ValueError 
            if city_flight not in destination:
                raise ValueError
            return city_flight
        
        # Handle exception related to ValueError
        except ValueError:
            print("Sorry! We do not go there please try diffent destination")
            pass

# Define int_exception(prompt) function to handle ValueError     
def int_exception(prompt):

    # While loop continues until a valid input is provided
    while True:

        # Take user's input
        try:
            num_nights = int(input(prompt))            
            return num_nights
        
        #Handle exceptions related to ValueError
        except ValueError:
            print("Please enter  as number!")
            pass


if __name__ == "__main__":
    main()
