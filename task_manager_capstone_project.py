# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

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

def reg_user():
    exist = False
    while not exist:
        new_username = input("New Username: ")
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

reg_user()

def add_task():
    '''
    Allow a user to add a new task to task.txt file
    Prompt a user for the following: 
        - A username of the person whom the task is assigned to
        - A title of a task
        - A description of the task
        - Due date of the task
    '''
    while True:
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
add_task()

# Create a function view_all without any arguments to view all the tasks listed in 'tasks.txt' when the user selects 'va'
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

view_all()

# Create a function view_mine without any arguments to view all the tasks assigned to a specific user when the user selects 'vm'
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
        while True:
            edit = int(input("\nSelect a task to edit\nEnter (Task number) or -1 to return to the menu: "))
            if (edit == -1):
                print("Good bye")
            if (edit >= 0):            
                for i, t in enumerate(task_list, 1):
                    if t['username'] == curr_user and i == edit:
                        with open('tasks.txt', 'r+') as task_file:
                            task_data = task_file.read().split("\n")
                            task_data = [t for t in task_data if t != ""]
                            # print(i, t)
                            # print()
                            # print(task_data)
                            # print()
                            select_option = input("Select an option below:\n1 - Mark as complete\n2 - Amend the username\n3 - Amend the due date\n")
                            if t['completed'] == True:
                                print("This task is completed and cannot be amended\nPlease select another task to modify\n")
                                continue
                            else:
                                if select_option == '1':                    
                                    t_new = str(task_data[i-1])
                                    t_new = t_new.replace("No", "Yes")
                                    remove_t = task_data.pop(i-1)
                                    add_t = task_data.insert(i-1, t_new)
                                    task_string = "\n".join([str(item) for item in task_data])
                                    #print(task_string)
                                    with open('tasks.txt', 'w') as task_file:
                                        task_file.write(task_string)
                                elif select_option == '2':                     
                                    t_new = str(task_data[i-1])
                                    edit_user = input("Enter the username: ")
                                    t_new = t_new.replace(curr_user, edit_user) 
                                    remove_t = task_data.pop(i-1)
                                    add_t = task_data.insert(i-1, t_new)
                                    task_string = "\n".join([str(item) for item in task_data])
                                    #print(task_string)
                                    with open('tasks.txt', 'w') as task_file:
                                        task_file.write(task_string)
                                if select_option == '3':
                                    while True:
                                        try:
                                            new_due_date = input("Due date of task (YYYY-MM-DD): ")
                                            new_date_time = datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)
                                            break
                                        except ValueError:
                                            print("Invalid datetime format. Please use the format specified") 
                                    t['due_date'] = new_date_time
                                    
                                    task_string = "\n".join([str(item) for item in task_data])
                                    print(task_string)
                                    # with open('tasks.txt', 'w') as task_file:
                                    #     task_file.write(task_data)
                                    # print(task_data)      
                                # else:
                                #     print("Error: Invalid choice")
view_mine()                             