'''

Program to access two different financial calculators: 
an investment calculator and a home loan repayment calculator

'''

import math

print("investment - to calculate the amount of interest you'll earn on your investment" 
      "\nbond - to calculate the amount you'll have to pay on a home loan")

# Declare a string variable 'select' to choose a menu item from the given two options and implement lower case
select = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
a_select = select.lower()

# Use the conditional control structure (if-elif-else) 
# implement 'investment' and 'bond' calculators based on a user selection 

# Prompt user to input 'investment' related values & calculate total investment return
if (a_select == "investment"):
    deposit = float(input("Please enter the deposit amount: "))
    rate = float(input("Please enter interest rate in number only: "))
    years = int(input("Please enter number of years to be invested: "))
    interest = input("Do you want 'simple' or 'compound' interest? ")
    a_interest = interest.lower()
    
    # Calculate investment return when'simple interest' is applied & display investment schedule on multiple lines
    if (a_interest == 'simple'):
        total_return = round(deposit * (1 + ((rate/100) * years)), 2)
        print(f"\nInvestment Schedule\n\nInitial deposit amount: {deposit}"
              f"\nNumber of Investment Years: {years}"
              f"\nType of Interest: {a_interest}"
              f"\nTotal Return on Investment: {total_return}")
    
    # Calculate investment return when'compound interest' is applied & display investment schedule on multiple lines
    elif (a_interest == 'compound'):
        total_return = round(deposit * math.pow((1 + (rate/100)),years), 2)   
        print(f"\nInvestment Schedule\n\nInitial deposit amount: {deposit}"
              f"\nNumber of Investment Years: {years}"
              f"\nType of Interest: {a_interest}"
              f"\nTotal Return on Investment: {total_return}")
    
    # Display error message for any other interest type selected by the user 
    else:
        print("Error: No such interest type exists")

# Prompt user to input 'bond' related values and calculate the monthly repayment amount
elif (a_select == "bond"):
    house_value = int(input("Please enter present value of the house: "))
    rate = float(input("Please enter interest rate in number only: "))
    months = int(input("Please enter number of months for repayment: "))
    repayment = round((((rate/100)/12) * house_value) / (1 - (1 + ((rate/100)/12))**(-months)), 2)
    # Use f-string to print 'Bond Repayment Schedule' on multiple lines
    print(f"\nBond Repayment Schedule\n\nMonthly Repayment Amount: {repayment}"
          f"\nTotal Number of Months: {months}\nInterest Rate (Annual): {rate}")

# Display error message if financial calculator is other than 'investment' or 'bond'
else:
    print("Error: Invalid option selected")