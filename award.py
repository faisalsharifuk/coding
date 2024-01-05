# Program to determine the type of award a person competing in a triathlon will receive

# Declare three variables of integer type to read swimming, cycling and running timings of an athlete in minutes
swimming_time = int(input("Please enter the swimming time in minutes: "))
cycling_time = int(input("Please enter the cycling time in minutes: "))
running_time = int(input("Please enter the running time in minutes: "))


# calculate the total time for all three events
total_time = swimming_time + cycling_time + running_time
print(total_time)   # print the total time in minutes

# Use the comparison and logical operators inside conditional (if-elif) statements for total time
# Work out the qualify criteria plus athlete award based on total time
if (total_time >= 0) and (total_time <= 100):
    q_criteria = "Within the qualifying time." 
    award = "Provincial Colours" 
elif (total_time >= 101) and (total_time <= 105):
    q_criteria = "Within 5 minutes of the qualifying time."
    award = "Provincial HalfColours"
elif (total_time >= 106) and (total_time <= 110):
    q_criteria = "Within 10 minutes of the qualifying time."
    award = "Provincial Scroll"
elif (total_time >= 111):
    q_criteria = "More than 10 minutes off from the qualifying time."
    award = "No award"

# Using the f-string, display the athelete's qualifying criteria, time range and award
print(f"The participant is {q_criteria} The time range is {total_time}. Received the award: {award}")