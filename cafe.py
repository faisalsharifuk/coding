# Create a menu list containing 8 cafe items
menu = ["Espresso", "Latte", "Iced Coffee", "Bagels", "Donuts", "Croissant", "Sandwich", "Pizza"]

# Create a stock dictionary for each item on the menu
stock = {'Espresso': 500,
         'Latte': 450,
         'Iced Coffee': 300,
         'Bagels': 250,
         'Donuts': 300,
         'Croissant': 200,
         'Sandwich': 400,
         'Pizza': 350
        }

# Create a price dictionary for each item on the menu
price = {'Espresso': 1.45,
         'Latte': 2.15,
         'Iced Coffee': 2.19,
         'Bagels': 4.80,
         'Donuts': 0.99,
         'Croissant': 3.30,
         'Sandwich': 2.50,
         'Pizza': 2.85
        }

# Loop through the menu list to calculate individual stock values & total stock value of 8 items

total_stock = 0     # Declare a variable to hold the running sum of prices. Convert it to float at the display level 

print()             # Space out the display result for better readability at the user end

for item in menu:
    item_value = (stock[item] * price[item])    # Calculate stock price of each item
    print(f"Item {menu.index(item)+1} - \"{item.upper()}\" stock price is: {float(item_value)}")
    total_stock += item_value       # Store the running sum

# Print the total stock value of 8 items
print(f"\nTotal stock value of {menu.index(item)+1} items is: {float(total_stock)}\n")