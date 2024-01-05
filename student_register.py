# Create a program that allows a user to register students for an exam venue

# Try this
try:
    # Prompt the user to enter number of students for registration
    total_students = int(input("Please enter the number of students for registration: "))
    if total_students < 0:
        # Raise a ValueError with a custom error message
        raise ValueError("Number of students cannot be negative")
except ValueError as raised_error:
    # Catch the raised ValueError and print the error message
    print(f"An error occurred: {raised_error}")

# Declare a constant for dotted line (student signature)
DOT_LINE = '.' * 50

# Create a text file for writing only mode (w) as per the task requirement
with open('reg_form.txt', 'w') as file:
    # Append the data column names
    file.write("ID" + "\t\t\t" + "Sign" + "\n\n")
    
    # Declare a for loop (student number range)
    for student in range(total_students):
        student_id = input("Please enter the next student ID number: ")     # Prompt the user to input student id (for each student)
        file.write(f"{student_id}\t\t{DOT_LINE}\n\n")                         # Append each student id number to the file