# Program to output a specific response based on the age entered by user

# Declare an integer variable seeking user age
age = int(input("Please enter your age: "))

# Use the conditional control structure (if-elif-else) to print an age related message
if (age > 100):
    print("Sorry, you're dead.")
elif (age >= 65):
    print("Enjoy your retirement!")
elif (age >= 40):
    print("You're over the hill.")
elif (age == 21):
    print("Congrats on your 21st!")
elif (age < 13):
    print("You qualify for the kiddie discount.")
else:
    print("Age is but a number.")
