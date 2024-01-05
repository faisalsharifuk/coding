# Program to replace each occurrence of character from string using the replace() function and print the new string
# Reprint the new string in capital form using upper() function
# Reprint the new string in reverse using the extended slice

# Declare a string variable sentence
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

# Use replace() function to amend each occurrence of string character "!" with a space " "
r_sentence = sentence.replace("!", " ")

# Print the newly replaced string
print(r_sentence)

# Reprint the replaced string in capitalize form
print(r_sentence.upper())

# Reverse the replaced string and reprint 
print(r_sentence[::-1])