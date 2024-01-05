'''
Create a shopping cart application for pet-related products
Users should be able to view their cart, add items and remove items
View the total cost of cart
'''

# Declare two lists for the shopping cart to store items and prices separately
items = []
prices = []

# Display the user menu and cart until checkout
print("\nWelcome to Paws n Cart!")
done = False
while (not done):
    print("\n")
    print("-" * 80)
    print("This is your shopping cart:")
    # Display the cart of items with their prices
    end = False
    counter = 0
    # Check the items list is not empty
    if (len(items) > 0):
        while (not end):
            # Check if this is the last item in the items list
            if (counter == len(items) - 1):
                end = True
            print("{:25} \t £{:10.2f}".format(items[counter],prices[counter]))
            counter += 1
    print("-" * 80)   
    menu = input("Would you like to:\n\
1. Add Item an item to your cart \n\
2. Remove an Item from your cart \n\
3. View the total cost of your cart \n\
4. Check out \n\
Enter the number of option you would like to choose:\n")
    
    # If user selects option 1 then add an item to the cart 
    if menu == "1":
        add_item = input("What item would you like to add to your cart: ")
        add_price = float(input("How much does the item cost: £ "))
        items.append(add_item)
        prices.append(add_price)
        print(f"{add_item} has been added to your cart successfully")

    # If user selects option 2 then remove an item from the cart if exists
    elif menu == "2":
        item_to_remove = input("What item would you like to remove: ")
        if item_to_remove in items:
            # Remove item from items and price lists simultaneously
            index = items.index(item_to_remove)
            items.remove(item_to_remove)
            prices.pop(index)
            print(f"{item_to_remove} has been removed from your cart successfully")
        else:
            print(f"{item_to_remove} is not in your cart")
    
    # If user selects option 3 then calculate/display the total cost of your items in the cart
    elif menu == "3":
        print(f"The total cost of your cart is: £{sum(prices)}")

    # If user selects option 4 then create an exit condition
    elif menu == "4":   # Exit from the program
        print("Thank you for shopping with Paws n Cart!")
        done = True
    
    # Display a message if the user selects an invalid option
    else:
        print("This is not a valid option")