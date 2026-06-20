'''
 Please do NOT run this Python file  
'''
import json #Importing the json module to save and load the tasks in a JSON file. 
import constants as con


tasks = {}#This is an empty dictionary that will be used to store the tasks that users add to their to-do list.

def save_tasks():#This function serialize the dictionary.
    try:
        with open(con.SAVE_FILE, "w") as f:
            print("Saving your tasks...")
            print("See you next time.")
            json.dump(tasks, f)
    except PermissionError:
        print("\n[ERROR]\nSaving failed due to insufficient file permissions.")
        print("Please check your folder permissions and try again.")


def load_tasks():#This function deserialize the dictionary.
    try:#This try-except block would create a new To-Do list if there is no saved_tasks.json file.
        global tasks#Using global keyword to modify the tasks that is defined outside the function.
        with open(con.SAVE_FILE, "r") as f:
            tasks = json.load(f)
            if tasks == {}:
                print("Start with a new To-Do list.")
            else:
                print("Start with your previous tasks.")
    except FileNotFoundError:#This except block prevents the program from crashing when there is no saved_tasks.json file.
        print("No saved tasks found. Start with a new To-Do list.")

        
def get_input_for_enumerate(category, question):
    while True:
        try:
            #This for loop allows users to select a task by number.
            print(f"\nTasks in [ {category.upper()} ]:")
            for i, task in enumerate(tasks[category]):
                print(f" {i + 1}: {task}")

            user_input = input(f"\n{question} (or '0' to go back)\n:").strip()

            if user_input == con.CMD_BACK:#Goes back to main menu.
                return None
            
            if user_input == "":#This if prevents blank input.
                print(con.INV_BLANK)
                continue

            task_num = int(user_input)
            if 1 <= task_num <= len(tasks[category]):
                return task_num
            else:
                print(con.INV_OUT_OF_RAGE)
        except ValueError:#This except block prevents the program from crashing when users enter invalid input that cannot be converted.
            print(con.INV_NOT_A_NUMBER)


def get_input(question):  

    while True:
        user_input = input(f"{question} (or '0' to go back)\n:").strip().lower()
        if user_input == con.CMD_BACK:
            return None

        if user_input == "":#This if prevents blank input.
            print(con.INV_BLANK)
            View_Lists()
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
        try:
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
                    input(con.CONTINUE)
                    return
                else:#This else is for if the task already exists in the same category.
                    print(f"[Invalid]\nYour task '{new_task}' already exists in [{category}]!\nPlease try again.")
        except EOFError:#This except block prevents the program from EOFError(e.g. Ctrl+D or Ctrl+Z).
            print(con.INV_OPTION)


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
                View_Lists()
                del_ask = int(get_input("Please choose your option below. \n 1: Remove a Category\n 2: Remove a Task\n 3: Clear All Lists"))

                if not del_ask: return

                if del_ask == con.CMD_REMOVE_CATEGORY:#This if statement is for users to remove a category from the list.
                    View_Lists()
                    #This line asks users to enter the name of the category.
                    while True:
                        View_Lists()
                        category_name = get_input("Enter the category you want to remove.")

                        if not category_name: return

                        success = Remove_Category(category_name)#This line calls the Remove_Category function and receives boolean.
                        if success == True:#This if is for if the category is successfully removed.
                            print(f"Your category [{category_name}] has been removed.")
                            View_Lists()
                            input(con.CONTINUE)
                            return
                        else:#This else is for if the category doesn't exist.
                            print(f"[Invalid]\nYour category [{category_name}] doesn't exist. Please try again.\n")
                        continue

                elif del_ask == con.CMD_REMOVE_TASK:#This elif statement is for users to remove a task from the list.
                    #This line asks users to enter the category of the task.
                    while True:
                        View_Lists()
                        category = get_input("Enter the category of the task you want to remove.")

                        if not category: return

                        if category not in tasks:
                            print(f"[Invalid]\nYour category [{category}] doesn't exist. Please try again.")
                            continue
                        
                                                        
                        task_num = get_input_for_enumerate(category, "Enter the number of the task you want to remove.")

                        if not task_num: return

                        task_index = task_num - 1 #Subtracting 1 from the task number since the list index starts from 0.
                        success = Remove_Task(category, task_index)#This line calls the Remove_Task function with parameters.

                        if success == True:#This if is for if the task is successfully removed.
                            print("Your task has been removed.")
                            View_Lists()
                            input(con.CONTINUE)
                            return
                        else:#This else is for if the task number is invalid.
                            print(con.INV_OUT_OF_RAGE)
                    
                elif del_ask == con.CMD_CLEAR_ALL:#This elif statement is for users to clear all lists.
                    while True:
                        try:
                            del_confirm = int(input("Are you sure you want to delete all of the tasks?\n Yes:1\n No:0\n:"))

                            if not del_confirm: return

                            elif del_confirm == con.CONFIRM_YES:
                                tasks.clear()
                                print("All your lists have been cleared.")
                                View_Lists()
                                input(con.CONTINUE)
                                return
                            else:
                                print(con.INV_OPTION)
                        except ValueError:#This except block prevents the program from crashing when users enter invalid input that cannot be converted.
                            print(con.INV_NOT_A_NUMBER) 
                else:
                    print(con.INV_OPTION)

            except ValueError:#This except block prevents the program from crashing when users enter invalid input that cannot be converted.
                print(con.INV_NOT_A_NUMBER) 
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

            task_num = get_input_for_enumerate(category, "Enter the number of the task you want to remove.")

            if not task_num: return

            task_index = task_num - 1#Subtracting 1 from the task number since the list index starts from 0.
            success = Mark_Complete_Para(category, task_index)#This line calls the Mark_Task_Complete function with parameters.

            if success == True:#This if is for if the task is successfully marked as complete.
                print("Your task has been marked as complete.")
                View_Lists()
                input(con.CONTINUE)
                return

            elif success == con.ALREADY_COMPLETE:#This elif is for if the task is already marked as complete.
                print("[Invalid]\nYour task is already marked as complete. Please try again.\n")

       
        except ValueError:#This except block prevents the program from crashing when users enter invalid input that cannot be converted.
            print(con.INV_NOT_A_NUMBER) 
        except TypeError:
            return


def Mark_Complete_Para(category, comp_task):#This function is for users to mark a task as complete in their To-Do list by category and task index.
    if 0 <= comp_task < len(tasks[category]):#This if checks if the task index is valid for the given category.
        if con.COMPLETE_MARKER in tasks[category][comp_task]:#This if checks if the task is already marked as complete.
            return con.ALREADY_COMPLETE
        
        #Adds COMPLETE_MARKER to the end of the task.
        complete_task = tasks[category][comp_task] + con.COMPLETE_MARKER
        tasks[category][comp_task] = complete_task
        return True
    
    else:#This else is for if the task index is invalid.
        return False

