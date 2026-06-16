import json #Importing the json module to save and load the tasks in a JSON file. 
import introduction as intro
print("\n" + "=" * 26)
print(" Welcome to Yojana To-Do!")
print("=" * 26)

tasks = {}#This is an empty dictionary that will be used to store the tasks that users add to their to-do list.

def save_tasks():#This function serialize the dictionary.
    try:
        with open("saved_tasks.json", "w") as f:
            print("Saving your tasks...")
            print("See you next time.")
            json.dump(tasks, f)
    except PermissionError:
        print("\n[ERROR]\nSaving failed due to insufficient file permissions.")
        print("Please check your folder permissions and try again.")

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

def get_input(question):  

    while True:
        user_input = input(f"{question} (or '0' to go back)\n:").strip().lower()
        if user_input in ["0", "'0'"]:
            return None

        if user_input == "":#This if prevents blank input.
            print("[Invalid]\nInput cannot be blank. Please try again.")
            continue

        return user_input




def View_Lists():#This function is for users to view thier current To-Do list.
                 #It will automatically display the current list after users add, remove, or mark complete a task. 
    print("\n" + "-" * 21)
    print(" Current To-Do List  ")
    print("-" * 21)
    if not tasks:
        print("(Your list is empty!)")
    else:

        for category, task_list in tasks.items():
            print(f"[ {category.upper()} ]") # Prints category name in uppercase
            
            if not task_list:
                print("(No tasks in this category)")
            else:
                #Loop through the list of tasks inside that category
                for task in task_list:
                    print(f" : {task}")
    print("-" * 21)



def Add_Task():
    print("=" * 26)
    print("    | Add a New Task | ")
  
    while True:
        View_Lists()
            
        category = get_input("Enter a category (e.g. work, personal)")

        if not category: return

        #This while loop is for if the category is valid, it will keep asking users to enter a task until they enter a valid task that can be added to the list.
        while True:
            new_task = get_input("Enter a task you want to add: ")

            if not new_task: return

            success = Add_Task_Para(category, new_task)#This line calls the Add_Task function with parameters.
            if success == True:
                print(f"Your task '{new_task}' has been added to [{category}].")#This line is for if the task is successfully added to the list.
                View_Lists()
                return
            else:#This else is for if the task already exists in the same category.
                print(f"[Invalid]\nYour task '{new_task}' already exists in [{category}]!\nPlease try again.")


def Add_Task_Para(category, new_task):#This function is for users to add a task to thier To-Do list.
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
    print("=" * 31)
    print("   | Remove a Task or List | ")
    if not tasks:
        View_Lists()
        print("You need to add something to remove a task or list.")
        print("-" * 51)
        print("\nReturning to main menu...")

    else:
        while True:      
            try:
                    
                del_ask = int(get_input("Please choose your option below. \n 1: Remove a Category\n 2: Remove a Task\n 3: Clear All ListsS"))

                if not del_ask: return

                if del_ask == 1:#This if statement is for users to remove a category from the list.
                    View_Lists()
                    #This line asks users to enter the name of the category.
                    category_name = get_input("Enter the category you want to remove.")

                    if not category_name: return

                    success = Remove_Category(category_name)#This line calls the Remove_Category function and receives boolean.
                    if success == True:#This if is for if the category is successfully removed.
                        print(f"Your category [{category_name}] has been removed.")
                        View_Lists()
                        break
                    else:#This else is for if the category doesn't exist.
                        print(f"[Invalid]\nYour category [{category_name}] doesn't exist. Please try again.\n")
                        continue

                elif del_ask == 2:#This elif statement is for users to remove a task from the list.
                    View_Lists()
                    #This line asks users to enter the category of the task.
                    category = get_input("Enter the category of the task you want to remove.")

                    if not category: return

                    if category not in tasks:
                        print(f"[Invalid]\nYour category [{category}] doesn't exist. Please try again.")
                        continue

                    #This for loop allows users to select a task by number.
                    for i, task in enumerate(tasks[category]):
                        print(f"{i + 1}: {task}")

                    #This line asks users to enter the number of the task.
                    while True:
                        task_num = int(get_input("Enter the number of the task you want to remove."))

                        if not task_num: return

                        task_index = task_num - 1 #Subtracting 1 from the task number since the list index starts from 0.
                        success = Remove_Task(category, task_index)#This line calls the Remove_Task function with parameters.

                        if success == True:#This if is for if the task is successfully removed.
                            print("Your task has been removed.")
                            View_Lists()
                            break
                        else:#This else is for if the task number is invalid.
                            print("[Invalid]\nInvalid task number. Please try again.\n")
                        
                elif del_ask == 3:#This elif statement is for users to clear all lists.
                    try:
                        del_confirm = int(input("Are you sure you want to delete all of the tasks?\n Yes:1\n No:0\n:"))

                        if not del_confirm: return

                        elif del_confirm == 1:
                            tasks.clear()
                            print("All your lists have been cleared.")
                            break
                        
                    except ValueError:#This except block prevents the program from crashing when users enter invalid input that cannot be converted.
                        print("[Invalid]\nPlease enter a number.") 
                else:
                    print("Your option isn't available. Please try again.")

            except ValueError:#This except block prevents the program from crashing when users enter invalid input that cannot be converted.
                print("[Invalid]\nPlease enter a number.") 
            except TypeError:
                return     




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
    print("=" * 31)
    print("  | Mark a Task as Complete | ")
  
    while True:      
        try:

            View_Lists()
            #This line asks users to enter the category of the task.
            category = get_input("Enter the category of the task you want to mark as complete.")

            if not category: return

            if category not in tasks:#This if is for if the category doesn't exist in the tasks dictionary.
                print(f"[Invalid]\nYour category [{category}] doesn't exist. Please try again.")
                continue

            #This for loop allows users to select a task by number.
            for i, task in enumerate(tasks[category]):
                print(f"{i + 1}: {task}")

            #This line asks users to enter the number of the task they want to mark as complete.
            while True:
                task_num = int(get_input("Enter the number of the task you want to mark as complete"))

                if not task_num: return

                task_index = task_num - 1#Subtracting 1 from the task number since the list index starts from 0.
                success = Mark_Complete_Para(category, task_index)#This line calls the Mark_Task_Complete function with parameters.

                if success == True:#This if is for if the task is successfully marked as complete.
                    print("Your task has been marked as complete.")
                    View_Lists()
                    break

                elif success == "already_complete":#This elif is for if the task is already marked as complete.
                    print("[Invalid]\nYour task is already marked as complete. Please try again.\n")

                else:#This else is for if the task number is invalid.
                    print("[Invalid]\nInvalid task number. Please try again.\n")
                    
        except ValueError:#This except block prevents the program from crashing when users enter invalid input that cannot be converted.
            print("[Invalid]\nPlease enter a number.") 
        except TypeError:
            return

def Mark_Complete_Para(category, comp_task):#This function is for users to mark a task as complete in their To-Do list by category and task index.
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
        #This print function creates a blank line that might help clear reading for users.
        #This line is main menu options. Users will choose their option from the list.
        print("\n" + "=" * 44)
        print("                 MAIN MENU                  ")
        print("=" * 44)
        print("  0. Help")
        print("  1. View Current Lists")
        print("  2. Add a New Task")
        print("  3. Remove a Task or List")
        print("  4. Mark a Task as Complete")
        print("  5. Save and Exit")
        print("=" * 44)
        #This line asks users to enter their option by number.
        user_input = int(input("Please choose your option (1-5):"))
        if user_input in options:
            if user_input == 0:
                intro.show_help()
            elif user_input == 1:#This if is for View Lists.
                View_Lists()
            elif user_input == 2:#This elif is for Add Task.
                Add_Task()
            elif user_input == 3:#This elif is for Remove List.
                Remove_List()
            elif user_input == 4:#This elif is for Mark Complete.
                Mark_Complete()
            elif user_input == 5:#This elif is for Exit.
                save_tasks()
                break
        else:
            print("[Invalid]\nYour option isn't available. Please try again.")
    except ValueError:#This except block prevents the program from crashing when users enter invalid input that cannot be converted.
        print("[Invalid]\nPlease enter a number.\n")
    except EOFError:#This except block prevents the program from EOFError(e.g. Ctrl+D or Ctrl+Z).
        print("[Invalid]\nYour option isn't available. Please try again.")