
# Program to output the star pattern using if/else structure in a single for loop

# Declare and initialise a variable to use in the for loop 
stars = "*"

# Loop through range 0 to 10
for i in range(0, 10):

    # Increment each row by one star if range is 0 to 5 
    if i < 5:
        print(stars)
        stars = stars + "*"
    
    # Decrement each row by one star if range is greater than 5
    else:
        stars = "*****"
        index = 4 - i
        print(stars[0:index]) 



'''
# Working solution with two for loops -- EASY

user_number = int(input("\nEnter a number: "))

if (user_number % 2 == 0): 
    for i in range(0, 5):
        print("*" * i)
        i += 1
           
    stars = "*****"
    for i in range(0, 5):
        index = 5 - i
        print(stars[0:index])     
'''