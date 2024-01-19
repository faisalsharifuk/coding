
# Program to calculate the average of integers/floating point numbers excluding the -1

# Declare and initialise three variables to 0 to use in the while loop
number = 0
count = 0
sum = 0

# Use 'while' loop for continuous input of a number until loop condition
while (number != "-1"): 
    number = input("Please enter a number of your choice: ") 

    '''
    Check for signed and unsigned integers as valid inputs
    Check for signed and unsigned floating point numbers as valid inputs
    Check for strings(non-digits) being invalid inputs and prompt the user for a valid input
    '''

    if (((number[0] in ["+", "-"]) and ((number[1:].isdigit()) or (number[1:].replace('.','',1).isdigit()))) 
            or (number.isdigit()) or (number.replace('.','',1).isdigit())):
        
        # Perform casting on 'number' to be a float data type for both edge cases: user input and final average calculation 
        r_number = float(number)

        # Use 'break' statement to bypass the last iteration & exit when entered -1 
        if (r_number == -1):
            break 

        sum = sum + r_number
        count = count + 1         
    
    # Prompt user for a valid number if entered incorrectly
    else:
        print(f"{number} is not a valid number")

# Calculate the average of entered numbers excluding -1. Round the average to 2 decimal places 
if (count > 0):
    average = round(sum / count, 2)
    print(f"The average of {count} numbers is: {average}")
else:
    print("Sorry, no user input entered\nPlease try again")     # Edge case if no user input entered

# Calculate the sum of entered numbers excluding -1. Round the average to 2 decimal places 
if (count > 0):
    sum = round(sum + r_number, 2)
    print(f"The sum of {count} numbers is: {sum}")
else:
    print("Sorry, no user input entered\nPlease try again")     # Edge case if no user input entered

# Calculate the difference of entered numbers excluding -1. Round the average to 2 decimal places 
if (count > 0):
    subtract = round(sum - r_number, 2)
    print(f"The difference of {count} numbers is: {subtract}")
else:
    print("Sorry, no user input entered\nPlease try again")     # Edge case if no user input entered