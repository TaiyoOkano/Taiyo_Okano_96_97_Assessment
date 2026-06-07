import json #Importing the json module to save and load the tasks in a JSON file. 
print("Welcome to a New To-do list!\n")

tasks = {}#This is an empty dictionary that will be used to store the tasks that users add to their to-do list.

def save_tasks():#This function serialize the dictionary.
    with open("saved_tasks.json", "w") as f:
        print("Saving your tasks...")
        json.dump(tasks, f)

def load_tasks():#This function deserialize the dictionary.
    try:#This try-except block would create a new To-Do list if there is no saved_tasks.json file.
        global tasks#Using global keyword to modify the tasks that is defined outside the function.
        with open("saved_tasks.json", "r") as f:
            tasks = json.load(f)
            if tasks == {}:
                print("Start with a new To-Do list.")
            else:
                print("Start with your previous tasks.")
    except FileNotFoundError:#This except block prevents the program from crashing when there is no saved_tasks.json file.
        print("No saved tasks found. Start with a new To-Do list.")
        
load_tasks()#This calls the load_tasks function to load from the saved_tasks.json file.

def View_Lists():#This function is for users to view thier current To-Do list.
                 #It will automatically display the current list after users add, remove, or mark complete a task. 
    print("---Current To-Do List---")
    if not tasks:
        print("Your list is empty.")
    else:#This for loop is for printing the category and tasks in the list.
        for category, task_list in tasks.items():
            print(f"[{category.lower()}]")
            for task in task_list:
                print(f"{task}")

def Add_Task(category, new_task):#This function is for users to add a task to thier To-Do list.
    print("Add Task.")
    #This if statement is for if the category doesn't exist, it will create a new category.
    if category not in tasks:
        tasks[category] = []     
    #This if statement prevents users from adding a task that already exists in the same category.
    if new_task in tasks[category]:
        return False
    else:#This else adds the new task to the category.
        tasks[category].append(new_task)
        return True


def Remove_List():#This function is for users to remove a task from thier To-Do list.
    print("Remove a List.")
    while True:      
        try:#This try-except block prevents the program from crashing when users enter invalid input.
            #This line asks remove options for users.
            del_ask = int(input("Do you want to remove a category or a task? Or clear all lists? Enter by 1, 2, or 3. \n[1: Category, 2: Task, 3: Clear All Lists]\n: "))
            if del_ask == 1:#This if statement is for users to remove a category from the list.
                View_Lists()
                #This line asks users to enter the name of the category.
                category_name = input("Enter the category you want to remove\n: ").strip().lower()

                success = Remove_Category(category_name)#This line calls the Remove_Category function and receives boolean.
                if success == True:#This if is for if the category is successfully removed.
                    print(f"Your category [{category_name}] has been removed.")
                    View_Lists()
                else:#This else is for if the category doesn't exist.
                    print(f"Your category [{category_name}] doesn't exist. Please try again.\n")
                break
    
            elif del_ask == 2:#This elif statement is for users to remove a task from the list.
                View_Lists()
                #This line asks users to enter the category of the task.
                category = input("Enter the category of the task you want to remove\n: ").strip().lower()
                if category not in tasks:
                    print(f"Your category [{category}] doesn't exist. Please try again.")
                    continue

                #This for loop allows users to select a task by number.
                for i, task in enumerate(tasks[category]):
                    print(f"{i + 1}: {task}")

                #This line asks users to enter the number of the task.
                task_num = int(input("Enter the number of the task you want to remove\n: "))
                task_index = task_num - 1 #Subtracting 1 from the task number since the list index starts from 0.
                success = Remove_Task(category, task_index)#This line calls the Remove_Task function with parameters.

                if success == True:#This if is for if the task is successfully removed.
                    print("Your task has been removed.")
                    View_Lists()
                else:#This else is for if the task number is invalid.
                    print("Invalid task number. Please try again.\n")
                break
            elif del_ask == 3:#This elif statement is for users to clear all lists.
                tasks.clear()
                print("All your lists have been cleared.")
                break
            else:
                print("Your option isn't available. Please try again.")
        except ValueError:#This except block prevents the program from crashing when users enter invalid input that cannot be converted.
            print("Invalid input. Please enter a number.\n")


def Remove_Category(category_name):#This function is for users to remove a category from their To-Do list.
    if category_name in tasks:#This if checks if the category exists in the tasks dictionary.
        del tasks[category_name]
        return True
    
    else:#This else is for if the category doesn't exist.
        return False

        

def Remove_Task(category, task_index):#This function is for users to remove a task from their To-Do list by category and task index.
    if 0 <= task_index < len(tasks[category]):#This if checks if the task index is valid for the given category.
        del tasks[category][task_index]
        return True
        
    else:#This else is for if the task index is invalid.
        return False

        
def Mark_Complete():#This function is for users to mark a task as complete in their To-Do list.
    print("Mark Complete.")
    while True:      
        try:#This try-except block prevents the program from crashing when users enter invalid input.
            View_Lists()
            #This line asks users to enter the category of the task.
            category = input("Enter the category of the task you want to mark as complete\n: ").strip().lower()
            if category not in tasks:#This if is for if the category doesn't exist in the tasks dictionary.
                print(f"Your category [{category}] doesn't exist. Please try again.")
                continue

            #This for loop allows users to select a task by number.
            for i, task in enumerate(tasks[category]):
                print(f"{i + 1}: {task}")

            #This line asks users to enter the number of the task they want to mark as complete.
            task_num = int(input("Enter the number of the task you want to mark as complete\n: "))
            task_index = task_num - 1#Subtracting 1 from the task number since the list index starts from 0.
            success = Mark_Task_Complete(category, task_index)#This line calls the Mark_Task_Complete function with parameters.

            if success == True:#This if is for if the task is successfully marked as complete.
                print("Your task has been marked as complete.")
                View_Lists()

            elif success == "already_complete":#This elif is for if the task is already marked as complete.
                print("Your task is already marked as complete. Please try again.\n")

            else:#This else is for if the task number is invalid.
                print("Invalid task number. Please try again.\n")
            break

        except ValueError:#This except block prevents the program from crashing when users enter invalid input that cannot be converted.
            print("Invalid input. Please enter a number.\n") 

def Mark_Task_Complete(category, comp_task):#This function is for users to mark a task as complete in their To-Do list by category and task index.
    if 0 <= comp_task < len(tasks[category]):#This if checks if the task index is valid for the given category.
        if "(Complete)" in tasks[category][comp_task]:#This if checks if the task is already marked as complete.
            return "already_complete"
        
        #Adds "(Complete)" to the end of the task.
        complete_task = tasks[category][comp_task] + "(Complete)"
        tasks[category][comp_task] = complete_task
        return True
    
    else:#This else is for if the task index is invalid.
        return False

options = [1,2,3,4,5] 
while True:#This while loop is for the main menu. It will keep running until users choose to exit the program by entering 5.
    try:#This try-except block prevents the program from crashing when users enter invalid input.
        print("\n")#This print function creates a blank line that might help clear reading for users.
        print("[1: View Lists, 2: Add Task, 3: Remove a List, 4: Mark Complete, 5: Exit]")#This line is main menu options. Users will choose their option from the list.
        #This line asks users to enter their option by number.
        user_input = int(input("Please choose your option from the list above by a number \n: "))
        if user_input in options:
            if user_input == 1:#This if is for View Lists.
                View_Lists()
            elif user_input == 2:#This elif is for Add Task.
                View_Lists()
        
                category = input("Enter a category (e.g. work, personal)\n: ").strip().lower()
                if category == "":#This if statement is for if category is empty or just spaces.
                    print("Category cannot be empty or just spaces. Please try again.")
                    continue

                #This while loop is for if the category is valid, it will keep asking users to enter a task until they enter a valid task that can be added to the list.
                while True:
                    new_task = input("Enter a task you want to add: ").strip().lower()
                    if new_task == "":
                        print("Your task cannot be empty or just spaces. Please try again.")
                        continue

                    success = Add_Task(category, new_task)#This line calls the Add_Task function with parameters.
                    if success == True:
                        print(f"Your task '{new_task}' has been added to [{category}].")#This line is for if the task is successfully added to the list.
                        View_Lists()
                        break
                    else:#This else is for if the task already exists in the same category.
                        print(f"!Your task '{new_task}' already exists in [{category}]!\nPlease try again.")
                        
                        
                    
            elif user_input == 3:#This elif is for Remove List.
                Remove_List()
            elif user_input == 4:#This elif is for Mark Complete.
                Mark_Complete()
            elif user_input == 5:#This elif is for Exit.
                save_tasks()
                print("Goodbye.")
                break
        else:
            print("Your option isn't available. Please try again.")
    except ValueError:#This except block prevents the program from crashing when users enter invalid input that cannot be converted.
        print("Invalid input. Please enter a number.\n")
    except EOFError:#This except block prevents the program from EOFError(e.g. Ctrl+D or Ctrl+Z).
        print("Invalid input. Please try again.\n")