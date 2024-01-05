# pseudocode begins here
# request name input from user
# request age input from user
# request house number input from user
# request street name input from user
# print user details containing the name, age, house number and street name on a single line
# pseudocode ends here

# program begins here

# declare first string variable seeking user name
name = input("Please enter your name: ")

# declare second string variable seeking user age
age = input("Please enter your age: ")

# declare third string variable seeking user house number
house_number = input("Please enter your house number: ")

# declare fourth string variable seeking user street name
street_name = input("Please enter your street name: ")

# print user details using formatted string literal (f-string) on a single line
print(f"This is {name}. I am {age} years old and lives at house number {house_number} on {street_name}.")