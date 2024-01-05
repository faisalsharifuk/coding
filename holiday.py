'''
Program to calculate a user's total holiday cost
Firstly, calculate the hotel cost
Secondly, calculate the plane cost
Thirdly, calculate the car rental cost
Finally, sum of above three calculations as a total holiday cost
Perform full validation checks for any variations in data inputs by the user (bullet proof data entries without try-except blocks) 
'''

# Create a list of holiday destinations to choose from
destination = ["Florida", "Grenada", "Tenerife", "Cape Town", "Maldives", "Qatar"]

# Create a ticket price dictionary for each country in the destination list
ticket_price = {'Florida' : 650,
                'Grenada' : 700,
                'Tenerife' : 350,
                'Cape Town' : 800,
                'Maldives' : 975,
                'Qatar' : 600
                }

# Display the destinations and user prompts continuously (along with calculated results)
done = False
while (not done):
    destination.sort()  # Sort the destination list in an alphabetical order
    print("\nHoliday Destinations\n\n" + '\n'.join(destination))
    
    # Prompt user to continue or exit the price quotation system
    user_confirm = input("\nDo you wish to continue (Yes or No): ")
    user_confirm = user_confirm.lower()
    
    # If user selects Yes then enter the data entry mode
    if (user_confirm == "yes"):
        
        # Using a nested while loop prompt the user to select city flight from the destination list presented earlier
        while True:
            city_flight = input("\nPlease enter your next holiday destination from the above list: ")
            city_flight = city_flight.lower()
            destination = [item.lower() for item in destination]
            # Create a function keys_lower to convert the ticket_price dictionary keys into lower case (user data entry validation)
            def keys_lower(ticket_price):
                ticket_price_lower = dict()
                for key in ticket_price.keys():
                    if isinstance(ticket_price[key], dict):
                        ticket_price_lower[key.lower()] = keys_lower(ticket_price[key])
                    else:
                        ticket_price_lower[key.lower()] = ticket_price[key]
                return ticket_price_lower
            if city_flight not in destination:
                print(f"\nError: Your entered destination {city_flight} is an invalid selection")
                continue
            break
        
        # Using a nested while loop prompt the user to enter a valid number of nights staying at a hotel
        while True:
            num_nights = input("\nPlease enter number of hotel nights (greater than 0): ")
            if num_nights.isnumeric():
                num_nights = int(num_nights)
                if num_nights < 1:
                    print("Error: Hotel nights must be greater than 0")
                    continue
            else:
                print("Error: You did not enter a number for hotel nights")
                continue
            break
        
         # Using a nested while loop prompt the user to input a valid number of days for which they will hire a car
        while True:
            rental_days = input("\nPlease enter the number of days for your car hire (greater than 0): ")
            if rental_days.isnumeric():
                rental_days = int(rental_days)
                if rental_days < 1:
                    print("Error: Car hire days must be greater than 0")
                    continue
            else:
                print("Error: You did not enter a number for car hire")
                continue
            break

        # Create a function hotel_cost with num_nights variable as an argument and return a total cost for the hotel stay
        def hotel_cost(num_nights):
            price_per_night = int(75)
            return (num_nights * price_per_night)
        
        # Create a function plane_cost with city_flight variable as an argument and return the ticket price based on chosen destination
        def plane_cost(city_flight):
            ticket_price_lower = keys_lower(ticket_price)
            return (ticket_price_lower[city_flight])

        # Create a function car_rental with rental_days variable as an argument and return the total cost of car hire
        def car_rental(rental_days):
            daily_rental_rate = int(60)
            return (rental_days * daily_rental_rate)

        # Create a function holiday_cost with three arguments hotel_cost, plane_cost, car_rental to calculate the total holiday cost 
        def holiday_cost(hotel_cost, plane_cost, car_rental):
            total = hotel_cost + plane_cost + car_rental
            return (total)

        # Print out the total holiday cost
        DOT_LINE = ("-" * 80)   # Dotted line consonant
        print(f"\n{DOT_LINE}\n"
            f"\nTotal Holiday Cost for {city_flight.upper()}: \t£ {holiday_cost(plane_cost(city_flight), hotel_cost(num_nights), car_rental(rental_days))}"
            f"\nFlight Ticket Cost: \t\t\t£ {plane_cost(city_flight)}\nHotel Cost: \t\t\t\t£ {hotel_cost(num_nights)}"
            f"\nCar Rental Cost: \t\t\t£ {car_rental(rental_days)}\n\n{DOT_LINE}")
    
    elif (user_confirm == "no"):
        done = True
        print("\nThank you for using the holidays quotation portal.\nHave a good time and see you again!\n")
    else:
        print("\nInvalid option. Enter Yes or No")