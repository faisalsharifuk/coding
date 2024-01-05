"""
Program to read in a string
Make each alternate character into an upper case character
Make each other alternate character a lower case character
"""

# Prompt the user to enter text
user_string = input("Please enter your text: ")
user_string = user_string.lower()

print("\nPART 1 - Converted Characters")
max_range = len(user_string)

# Declare an empty string to store alternate characters converted to upper and lower cases
converted_string = ""

# Loop to capitalize the alternate string characters using conditional if-else block
for i in range(max_range):
    if (i%2 == 0):
        converted_string += user_string[i].upper()
    else:
        converted_string += user_string[i].lower()

# Print the converted string
print(converted_string)

print("\nPART 2 - Converted Words")

# Declare a new string to split the user_string into separate words in a list form
split_string = split_string = user_string.split(" ")

# Loop to capitalize the alternate split_string words using conditional if-else block
for i in range(len(split_string)):
    if (i%2 == 1):
        split_string[i] = split_string[i].upper()
    else:
        split_string[i] = split_string[i].lower()

# Use the join method to create a final string 
join_string = " ".join(split_string)

# Print the join string
print(join_string)