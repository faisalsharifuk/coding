'''
Create a program to read data from a text file DOB.txt
Display the data in two different sections in the following format: 
Names in first section and Birth Dates in second section
'''

# Open a text file for reading only mode (r)
with open('DOB.txt', 'r') as file:
    
    # Declare two empty string variables to store names and date_of_births separately
    name_list = ""
    dob_list = ""

    # Use the for loop to read lines from a text file
    for line in file: 
            name = line.rsplit(' ', 3)[0]           # Declare a name variable and split the line to include forename & surname
            name_list += name + "\n"                # Concatenate the splitted names to a string variable (name_list)
            date_of_birth = line.split(' ', 2)[-1]  # Declare a DOB variable and split the line to include date of birth
            dob_list += date_of_birth               # Concatenate the splitted birth dates to a string variable (dob_list)
    
    # Display the two sections separately (Names and DOBs)
    print(f"NAMES\n{name_list}")
    print(f"BIRTH DATES\n{dob_list}")