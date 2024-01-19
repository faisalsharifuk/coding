'''
Program to display a complete Task Management System for team members including tasks reports and statistics
Notes: 
1. Use the following username and password to access the admin rights 
username: admin
password: password
2. Ensure you open the whole folder for this task in VS Code otherwise the 
program will look in your root directory for the text files.
'''

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)


#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True

while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    star_line = ('*' * 42)
    print()
    menu = input(f'''\033[1;35m {star_line} \n\n Welcome to Task Management Portal\n 
 Select one of the following Options below:
 r -\tRegister a user
 a -\tAdd a task
 va -\tView all tasks
 vm -\tView my tasks
 gr -\tGenerate Reports
 ds -\tDisplay statistics
 e -\tExit \n\n {star_line}
    : \033[0m''').lower()

    # Create a function that is called when the user selects ‘r’ to register a user
    if menu == 'r':
        def reg_user():
            exist = False
            while not exist:
                new_username = input("New Username: ")
                new_username = new_username.lower()
                if new_username in username_password:
                    print("This user already exists\nPlease try again and add a new user")
                    continue
                else:
                    new_password = input("New Password: ")
                    confirm_password = input("Confirm Password: ")
                    if new_password == confirm_password:
                        print("New user added")
                        username_password[new_username] = new_password
                    
                        with open("user.txt", "w") as out_file:
                            user_data = []
                            for k in username_password:
                                user_data.append(f"{k};{username_password[k]}")
                            out_file.write("\n".join(user_data))
                    else:
                        print("Passwords do no match")
                        continue
                exist = True
        reg_user()  # Call the reg_user function 

    # Create a function that is called when a user selects ‘a’ to add a new task
    elif menu == 'a':
        def add_task():
            '''
            Allow a user to add a new task to task.txt file
            Prompt a user for the following: 
                - A username of the person whom the task is assigned to
                - A title of a task
                - A description of the task
                - Due date of the task
            '''
            done = False
            while not done:
                task_username = input("Name of person assigned to task: ")
                if task_username not in username_password.keys():
                    print("User does not exist. Please enter a valid username")
                    continue
                task_title = input("Title of Task: ")
                task_description = input("Description of Task: ")
                while True:
                    try:
                        task_due_date = input("Due date of task (YYYY-MM-DD): ")
                        due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                        break
                    except ValueError:
                        print("Invalid datetime format. Please use the format specified")
                # Then get the current date.
                curr_date = date.today()
                '''
                Add the data to the file task.txt and
                Include 'No' to indicate if the task is complete
                '''
                new_task = {
                    "username": task_username,
                    "title": task_title,
                    "description": task_description,
                    "due_date": due_date_time,
                    "assigned_date": curr_date,
                    "completed": False
                    }
                task_list.append(new_task)
                with open("tasks.txt", "w") as task_file:
                    task_list_to_write = []
                    for t in task_list:
                        str_attrs = [
                            t['username'],
                            t['title'],
                            t['description'],
                            t['due_date'].strftime(DATETIME_STRING_FORMAT),
                            t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                            "Yes" if t['completed'] else "No"
                            ]
                        task_list_to_write.append(";".join(str_attrs))
                    task_file.write("\n".join(task_list_to_write))
                print("Task successfully added.")
                done = True
        add_task()  # Call the add_task function

    # Create a function that is called when users type ‘va’ to view all the tasks listed in ‘tasks.txt’
    elif menu == 'va':
        def view_all():
            '''
            Reads the task from task.txt file and prints to the console in the 
            format of Output 2 presented in the task pdf (i.e. includes spacing
            and labelling) 
            '''
            for t in task_list:
                disp_str = f"Assigned to: \t {t['username']}\n"
                disp_str += f"Task title: \t {t['title']}\n"      
                disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Task Description: \n {t['description']}\n"
                print(disp_str)
        view_all()  # Call the view_all function

    # Create a function that is called when users type ‘vm’ to view all the tasks that have been assigned to them
    elif menu == 'vm':
        def view_mine():
            '''
            Reads the task from task.txt file and prints to the console in the 
            format of Output 2 presented in the task pdf (i.e. includes spacing
            and labelling)
            '''
            task_count = 0
            dot_line = ('-' * 80)
            print(f"\nThe user \033[1;44m {curr_user.upper()} \033[0m is assigned with the following tasks:")
            for i, t in enumerate(task_list, 1):
                if t['username'] == curr_user:
                    with open('tasks.txt', 'r+') as task_file:
                        task_data = task_file.read().split("\n")
                        task_data = [t for t in task_data if t != ""]
                        task_count = i
                        print(f"\n{dot_line}\n")
                        disp_str = f"Task number: \t {task_count}\n"
                        disp_str += f"Task title: \t {t['title']}\n"
                        disp_str += f"Assigned to: \t {t['username']}\n"
                        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                        disp_str += f"Task Description: \n {t['description']}\n"
                        disp_str += f"Completed: \t {t['completed']}\n"                
                        print(f"{disp_str}\n{dot_line}")

            if task_count == 0:
                print("This user has no task")
                
            if task_count != 0:
                completed = False
                while not completed:
                    try:
                        edit = int(input("\nSelect a task to edit\nEnter (Task number) or -1 to return to the menu: "))
                        if (edit == -1):
                            print("Good bye")
                            break
                        elif (edit >= 0):            
                            for i, t in enumerate(task_list, 1):
                                if t['username'] == curr_user and i == edit:
                                    with open('tasks.txt', 'r+') as task_file:
                                        task_data = task_file.read().split("\n")
                                        task_data = [t for t in task_data if t != ""]
                                        '''
                                        CODE FOR TESTING PURPOSES ONLY
                                        # print(i, t)
                                        # print()
                                        # print(task_data)
                                        # print()
                                        ''' 
                                        if t['completed'] == True:
                                            print("This task is completed and cannot be amended\nPlease select another task to modify\n")
                                            continue 
                                        else:
                                            select_option = input("Select an option below:\n1 - Mark as complete\n2 - Amend the username\n3 - Amend the due date\n")
                                            if select_option == '1':               
                                                t_new = str(task_data[i-1])
                                                t_new = t_new.replace("No", "Yes")
                                                remove_t = task_data.pop(i-1)
                                                add_t = task_data.insert(i-1, t_new)
                                                task_string = "\n".join([str(item) for item in task_data])
                                                with open('tasks.txt', 'w') as task_file:
                                                    task_file.write(task_string)
                                                    print("You have marked the task as completed")
                                                    completed = True
                                            elif select_option == '2':                
                                                while True:
                                                    t_new = str(task_data[i-1])
                                                    edit_user = input("Enter the username: ")
                                                    if edit_user in username_password:
                                                        t_new = t_new.replace(curr_user, edit_user) 
                                                        remove_t = task_data.pop(i-1)
                                                        add_t = task_data.insert(i-1, t_new)
                                                        task_string = "\n".join([str(item) for item in task_data])
                                                        with open('tasks.txt', 'w') as task_file:
                                                            task_file.write(task_string)
                                                            print(f"Username for task {i} is successfully changed to \033[1;44m {edit_user} \033[0m ")
                                                        break
                                                    else:
                                                        print("Please enter a valid username from the users list")
                                                        continue
                                                completed = True
                                            elif select_option == '3':
                                                t_new = str(task_data[i-1])
                                                while True:
                                                    try:
                                                        new_due_date = input("Due date of task (YYYY-MM-DD): ")
                                                        new_date_time = datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)
                                                        break
                                                    except ValueError:
                                                        print("Invalid datetime format. Please use the format specified") 
                                                due_date = task_data[i-1][-24:-14]
                                                #print(due_date)
                                                t_new = t_new.replace(due_date, new_due_date)
                                                remove_t = task_data.pop(i-1)
                                                add_t = task_data.insert(i-1, t_new)
                                                task_string = "\n".join([str(item) for item in task_data])                   
                                                with open('tasks.txt', 'w') as task_file:
                                                    task_file.write(task_string)
                                                    print(f"Due date for task {i} is successfully changed to {new_due_date}")    
                                                completed = True 
                                            else:
                                                print("Error: Invalid choice")
                                            continue
                    except ValueError:
                        print("Error: Please enter a valid number")
                    continue
        view_mine() # Call the view_mine function

    # Create two separate functions to generate two text files 'task_overview.txt' and 'user_overview.txt' respectively
    # Both these text files should output data in a user-friendly and easy to read manner
    elif menu == 'gr':    
        # Function to display TASKS related report/text file when user type 'gr'
        def generate_tasks_report():
            #print(f"\nThe total number of generated tasks is: {len(task_list)}\n")
            count_completed = 0
            count_uncompleted = 0
            count_overdue = 0
            curr_date = datetime.today()
            for t in task_list:
                if t['completed'] == True:
                    count_completed += 1
                elif t['completed'] == False:
                    count_uncompleted += 1
                with open('tasks.txt', 'r+') as task_file:
                    if (t['completed'] == False) and (curr_date > t['due_date']) :
                        count_overdue += 1
                str_tasks = f"\nThe total number of generated tasks is: {len(task_list)}\n"
                str_tasks += f"\nThe total number of completed tasks is: {(count_completed)}\n"
                str_tasks += f"\nThe total number of uncompleted tasks is: {(count_uncompleted)}\n"
                str_tasks += f"\nThe total number of overdue tasks is: {(count_overdue)}\n"
                str_tasks += f"\nThe percentage of uncompleted tasks is: {((count_uncompleted)/len(task_list))*100} %\n"
                str_tasks += f"\nThe percentage of overdue tasks is: {((count_overdue)/len(task_list))*100} %\n"
                str_tasks += f"\nThank you for viewing the tasks data in task_overview.txt file\n"
            with open('task_overview.txt', 'w+') as task_file:
                task_file.write(str_tasks)
            '''
            CODE FOR TESTING PURPOSES ONLY
            #print(f"\nThe total number of completed tasks is: {(count_completed)}\n")
            #print(f"\nThe total number of uncompleted tasks is: {(count_uncompleted)}\n")
            #print(f"\nThe total number of overdue tasks is: {(count_overdue)}\n")
            #print(f"\nThe percentage of uncompleted tasks is: {((count_uncompleted)/len(task_list))*100} %\n")
            #print(f"\nThe percentage of overdue tasks is: {((count_overdue)/len(task_list))*100} %\n")
            '''
        generate_tasks_report() # Call the generate_tasks_report function 

        # Function to display USERS related report/text file when user type 'gr'
        def generate_users_report():
            #print(f"\nThe total number of registered users is: {len(user_data)}\n")
            #print(f"\nThe total number of generated tasks is: {len(task_list)}\n")
            with open('tasks.txt', 'r') as task_file:
                task_count = {}
                count_completed = {}
                count_uncompleted = {}
                overdue_count = {}

                for t in task_file:
                    t_record = t.strip().split(";")
                    username = t_record[0]
                    due_date = t_record[3]
                    completed = t_record[5]
                    curr_date = date.today()
                    #curr_date = date.strptime(curr_date, DATETIME_STRING_FORMAT)
                    #print(str(curr_date))    
                    if username in task_count:
                        task_count[username] += 1
                    else:
                        task_count[username] = 1                                  
                    if username in count_completed:
                        if completed == 'Yes':
                            count_completed[username] += 1                
                    else:
                        if completed == 'Yes':
                            count_completed[username] = 1
                    if username in count_uncompleted:
                        if completed == 'No':
                            count_uncompleted[username] += 1                
                    else:
                        if completed == 'No':
                            count_uncompleted[username] = 1
                    if username in overdue_count:
                        if completed == 'No' and due_date < str(curr_date):
                            overdue_count[username] += 1                
                    else:
                        if completed == 'No' and due_date < str(curr_date):
                            overdue_count[username] = 1
                '''
                CODE FOR TESTING PURPOSES ONLY
                # dot_line = ('-' * 40)
                # print()
                # print(dot_line)
                # print("Total number of tasks")
                # for user in task_count:
                #     print(f"{user}\t\t{task_count[user]}")
                # print()
                # print(dot_line)
                # print("Percentage of TOTAL tasks")
                # for user in task_count:
                #     print(f"{user}\t\t{(task_count[user]/len(task_list))*100} %")
                # print()
                # print(dot_line)
                # print("Percentage of COMPLETED tasks")
                # for user in count_completed:
                #     print(f"{user}\t\t{(count_completed[user]/len(task_list))*100} %")
                # print()
                # print(dot_line)
                # print("Percentage of UNCOMPLETED tasks")
                # for user in count_uncompleted:
                #     print(f"{user}\t\t{(count_uncompleted[user]/len(task_list))*100} %")
                # print()
                # print(dot_line)
                # print("Percentage of OVERDUE tasks")
                # for user in overdue_count:
                #     print(f"{user}\t\t{(overdue_count[user]/len(task_list))*100} %")   
                # print()
                # print(dot_line)
                # print("\nThank you for downloading data from user_overview.txt file")
                '''

                with open('user_overview.txt', 'w+') as task_file:
                    dot_line = ('-' * 60)
                    str_user = f"\n{dot_line}\n"
                    str_user += f"Total number of user tasks\n"
                    for user in task_count:
                        str_user += f"{user}\t\t{task_count[user]}\n"
                    str_user += f"\n{dot_line}\n"
                    str_user += f"Percentage of TOTAL user tasks\n"
                    for user in task_count:
                        str_user += f"{user}\t\t{(task_count[user]/len(task_list))*100} %\n"
                    str_user += f"\n{dot_line}\n"
                    str_user += f"Percentage of COMPLETED user tasks\n"
                    for user in count_completed:
                        str_user += f"{user}\t\t{(count_completed[user]/len(task_list))*100} %\n"
                    str_user += f"\n{dot_line}\n"
                    str_user += f"Percentage of UNCOMPLETED user tasks\n"
                    for user in count_uncompleted:
                        str_user += f"{user}\t\t{(count_uncompleted[user]/len(task_list))*100} %\n"
                    str_user += f"\n{dot_line}\n"
                    str_user += f"Percentage of OVERDUE user tasks\n"
                    for user in overdue_count:
                        str_user += f"{user}\t\t{(overdue_count[user]/len(task_list))*100} %\n"   
                    str_user += f"\n{dot_line}\n"
                    str_user += f"\nThank you for viewing the tasks data in user_overview.txt file\n"
                    task_file.write(str_user)
        generate_users_report() # Call the generate_users_report
    
        '''
        Display statistics so that reports generated are read from tasks.txt and user.txt files respectively
        Display these reports on the screen in a user-friendly manner
        '''
    elif menu == 'ds' and curr_user == 'admin': 
        #If the user is an admin they can display statistics about number of users and tasks.'''
        num_users = len(username_password.keys())
        num_tasks = len(task_list)

        print("\n-----------------------------------")
        print(f"Number of tasks: \t\t {num_tasks}")
        print(f"Number of users: \t\t {num_users}")
        print("-----------------------------------")  
        view_report = input("\nDo you want to display statistics for tasks or users?\nEnter Task or User: ")
        view_report = view_report.lower()
        if view_report == 'task':
            print("\nBreakdown of tasks assigned to users \n")
            with open('tasks.txt', 'r') as task_file:
                for t in task_file:
                    t_record = t.strip().split(";")
                    username = t_record[0]
                    title = t_record[1]
                    description = t_record[2]
                    date_due = t_record[3]
                    date_assigned = t_record[4]
                    completed = t_record[5]
                    disp_task = f"Assigned to:\t\t{username}\n"
                    disp_task += f"Task title: \t\t{title}\n"
                    disp_task += f"Task description:\t{description}\n"
                    disp_task += f"Due date:\t\t{date_due}\n"
                    disp_task += f"Assigned date:\t\t{date_assigned}\n"
                    disp_task += f"Completed:\t\t{completed}\n"                
                    print(disp_task)
            print("Thank you for viewing the data from tasks.text file")
        elif view_report == 'user': 
            print("\nNumber of registered users \n")
            with open('user.txt', 'r') as user_file:
                for i, u in enumerate(user_file, 1):
                    u_record = u.strip().split(";")
                    username = u_record[0]
                    disp_user = f"User {i}:\t\t{username}"   
                    print(disp_user)
            print("\nThank you for viewing the data from user.text file")
        else:
            print("Error: Incorrect option selected")
    elif menu == 'ds' and curr_user != 'admin':
        print(f"User {curr_user} is not allowed to view the statistics")
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    else:
        print("You have made a wrong choice, Please Try again")