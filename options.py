'''
 Please do NOT run this Python file  
'''
import json #Importing the json module to save and load the tasks in a JSON file. 
import constants as con #Importing constants file.


tasks = {}#This is an empty dictionary that will be used to store the tasks that users add to their to-do list.

def save_tasks():#This function serialises the dictionary.
    try:
        with open(con.SAVE_FILE, "w") as f:#Save data as a json file.
            print("Saving your tasks...")
            print("See you next time.")
            json.dump(tasks, f)
    except PermissionError:#This except prevents the program from crashing if there is an issue with file system permissions. 
        print("\n[ERROR]\nSaving failed due to insufficient file permissions.")
        print("Please check your folder permissions and try again.")


def load_tasks():#This function deserialises the dictionary.
    try:#This try-except block would create a new To-Do list if there is no saved_tasks.json file.
        global tasks#Using global keyword to modify the tasks that is defined outside the function.
        with open(con.SAVE_FILE, "r") as f:
            tasks = json.load(f)
            if tasks == {}:#This if is for if the json file is empty or doesn't exist.
                print("Start with a new To-Do list.")
            else:
                print("Start with your previous tasks.")
    except FileNotFoundError:#This except block prevents the program from crashing when there is no saved_tasks.json file.
        print("No saved tasks found. Start with a new To-Do list.")


def get_input_for_enumerate(category, question):#This function gets users input by number. It is necessary to work returning main menu option(by inputting '0').

    while True:
        try:
            #This for loop allows users to select a task by number.
            print(f"\nTasks in [ {category.upper()} ]:")
            for i, task in enumerate(tasks[category]):
                if con.COMPLETE_MARKER in task:#This if is if the task is completed(Complete), it replaces the (Complete) to [✓] 
                    clean_task = task.replace(con.COMPLETE_MARKER, "")
                    print(f" {i + 1}: [✓] {clean_task}")
                else:#Print tasks by number.
                    print(f" {i + 1}: {task}")

            user_input = input(f"\n{question} (or '0' to go back)\n:").strip()#I didn't write lower() since the input asks users a number.

            if user_input == con.CMD_BACK:#This if returns None if user input 0.
                return None 
            
            if user_input == "":#This if prevents blank input.
                print(con.INV_BLANK)
                continue

            task_num = int(user_input)#Convert user input to an integer to match task numbers.
            if 1 <= task_num <= len(tasks[category]):#This if checks the entered number is within the valid range for the chosen category.
                return task_num
            else:#This else is for if the user's input is out of range.
                print(con.INV_OUT_OF_RANGE)
        except ValueError:#This except block prevents the program from crashing when users enter invalid input that cannot be converted.
            print(con.INV_NOT_A_NUMBER)
        except EOFError:#This except block prevents the program from EOFError(e.g. Ctrl+D or Ctrl+Z).
            print(con.INV_OPTION)

def get_input(question):#This function gets user's input. It is necessary to work returning main menu option(by inputting '0').

    while True:
        user_input = input(f"{question} (or '0' to go back)\n:").strip().lower()
        if user_input == con.CMD_BACK:#This if returns None if user input 0.
            return None

        if user_input == "":#This if prevents blank input.
            print(con.INV_BLANK)
            view_lists()
            continue

        return user_input#Return the value.


def view_lists():#This function is for users to view their current To-Do list.
                 #It will automatically display the current list after users add, remove, or mark complete a task. 
    print("\n" + "-" * 21)
    print(" Current To-Do List  ")
    print("-" * 21)
    if not tasks:#This if is for if the To-Do list is empty.
        print("(Your list is empty!)")
    else:
        #This loop through each category and print its tasks.
        for category, task_list in tasks.items():
            print(f"[ {category.upper()} ]") # Prints category name in uppercase
            
            if not task_list:#This if is for if there is no task in the category.
                print("(No tasks in this category)")
            else:
               
                for task in task_list:
                    if con.COMPLETE_MARKER in task:#This if is for if the task is marked as complete.
                        clean_task = task.replace(con.COMPLETE_MARKER, "")#Replaces (Complete).
                        print(f" : [✓] {clean_task}")#Adds [✓] mark before the task. 

                    else:#Loop through the list of tasks inside that category
                        print(f" : {task}")
    print("-" * 21)


def add_task():#This function is for users to create a category, and add a task to their To-Do list. 
    print("=" * 26)
    print("    | Add a New Task | ")
  
    while True:
        try:
            view_lists()
                
            category = get_input("Enter a category (e.g. work, personal)")#Get user's input for the category name.

            if not category: return#If user's input is None(0), return to the main menu.

            #This while loop is for if the category is valid, it will keep asking users to enter a task until they enter a valid task that can be added to the list.
            while True:
                new_task = get_input("Enter a task you want to add: ")

                if not new_task: return#If user's input is None(0), return to the main menu.

                success = add_task_para(category, new_task)#This line calls the Add_Task function with parameters.
                if success == True:
                    print(f"Your task '{new_task}' has been added to [ {category.upper()} ].")#This line is for if the task is successfully added to the list.
                    view_lists()
                    input(con.CONTINUE)
                    return
                
                else:#This else is for if the task already exists in the same category.
                    print(f"[Invalid]\nYour task '{new_task}' already exists in [ {category.upper()} ]!\nPlease try again.")
        except EOFError:#This except block prevents the program from EOFError(e.g. Ctrl+D or Ctrl+Z).
            print(con.INV_OPTION)#This else is for if user's option is not available.


def add_task_para(category, new_task):#This function manipulates user's input for adding a task.
    #This if statement is for if the category doesn't exist, it will create a new category.
    if category not in tasks:
        tasks[category] = []     
    #This if statement prevents users from adding a task that already exists in the same category.
    if new_task in tasks[category]:
        return False
    #This if statement prevents users from adding a task that is already marked as complete in the same category. 
    if new_task + con.COMPLETE_MARKER in tasks[category]:
        return False
    else:#This else adds the new task to the category.
        tasks[category].append(new_task)
        return True# Return True if the task was successfully added, otherwise False.


def remove_list():#This function is for users to remove a task from their To-Do list.
    print("=" * 31)
    print("   | Remove a Task or List | ")
    if not tasks:#This if is for if there is no task to remove from the list.
        view_lists()
        print("You need to add something to remove a task or list.")
        print("-" * 51)
        print("\nReturning to main menu...")

    else:
        while True:      
            try:
                view_lists()
                user_choice = get_input("Please choose your option below. \n 1: Remove a Category\n 2: Remove a Task\n 3: Clear All Lists")

                if not user_choice: return#If user's input is None(0), return to the main menu.
                
                del_ask = int(user_choice)

                if del_ask == con.CMD_REMOVE_CATEGORY:#This if statement is for users to remove a category from the list.              
                    while True:
                        view_lists()
                        category_name = get_input("Enter the category you want to remove.")#This line asks users to enter the name of the category.

                        if not category_name: return#If user's input is None(0), return to the main menu.

                        success = remove_category(category_name)#This line calls the Remove_Category function and receives boolean.
                        if success == True:#This if is for if the category is successfully removed.
                            print(f"Your category [{category_name}] has been removed.")
                            view_lists()
                            input(con.CONTINUE)
                            return
                        else:#This else is for if the category doesn't exist.
                            print(f"[Invalid]\nYour category [{category_name}] doesn't exist. Please try again.\n")
                        continue

                elif del_ask == con.CMD_REMOVE_TASK:#This elif statement is for users to remove a task from the list.
                    #This line asks users to enter the category of the task.
                    while True:
                        view_lists()
                        category = get_input("Enter the category of the task you want to remove.")

                        if not category: return

                        if category not in tasks:
                            print(f"[Invalid]\nYour category [{category}] doesn't exist. Please try again.")
                            continue
                        
                                                        
                        task_num = get_input_for_enumerate(category, "Enter the number of the task you want to remove.")

                        if not task_num: return

                        task_index = task_num - 1 #Subtracting 1 from the task number since the list index starts from 0.
                        success = remove_task(category, task_index)#This line calls the Remove_Task function with parameters.

                        if success == True:#This if is for if the task is successfully removed.
                            print(f"Your task has been removed.")
                            view_lists()
                            input(con.CONTINUE)
                            return
                        else:#This else is for if the task number is invalid.
                            print(con.INV_OUT_OF_RANGE)
                    
                elif del_ask == con.CMD_CLEAR_ALL:#This elif statement is for users to clear all lists.
                    while True:
                        try:
                            del_confirm = int(input("Are you sure you want to delete all of the tasks?\n Yes:1\n No:0\n:"))
                            if not del_confirm: 
                                print("\nReturning to main menu...")
                                return

                            elif del_confirm == con.CONFIRM_YES:
                                tasks.clear()
                                print("All your lists have been cleared.")
                                view_lists()
                                input(con.CONTINUE)
                                return
                            else:
                                print(con.INV_OPTION)#This else is for if user's option is not available.
                        except ValueError:
                            print(con.INV_NOT_A_NUMBER)
                        except EOFError:#This except block prevents the program from EOFError(e.g. Ctrl+D or Ctrl+Z).
                            print(con.INV_OPTION)

                elif user_choice > '3' or user_choice < '1':
                    print(con.INV_OUT_OF_RANGE)#This elif is for if the user's input is out of range.
                else:
                    print(con.INV_OPTION)#This else is for if user's option is not available.

            except ValueError:#This except block prevents the program from crashing when users enter invalid input that cannot be converted.
                print(con.INV_NOT_A_NUMBER) 
            except EOFError:#This except block prevents the program from EOFError(e.g. Ctrl+D or Ctrl+Z).
                print(con.INV_OPTION)  


def remove_category(category_name):#This function manipulates user's input for categories deletion.
    if category_name in tasks:#This if checks if the category exists in the tasks dictionary.
        del tasks[category_name]
        return True
    
    else:#This else is for if the category doesn't exist.
        return False


def remove_task(category, task_index):#This function manipulates user's input for tasks deletion.

    if 0 <= task_index < len(tasks[category]):#This if checks if the task index is valid for the given category.
        del tasks[category][task_index]
        return True
        
    else:#This else is for if the task index is invalid.
        return False


def mark_complete():#This function is for users to mark a task as complete in their To-Do list.
    print("=" * 31)
    print("  | Mark a Task as Complete | ")
  
    while True:      
        try:
            view_lists()
            #This line asks users to enter the category of the task.
            category = get_input("Enter the category of the task you want to mark as complete.")

            if not category: return

            if category not in tasks:#This if is for if the category doesn't exist in the tasks dictionary.
                print(f"[Invalid]\nYour category [{category}] doesn't exist. Please try again.")
                continue

            task_num = get_input_for_enumerate(category, "Enter the number of the task you want to mark as complete.")

            if not task_num: return

            task_index = task_num - 1#Subtracting 1 from the task number since the list index starts from 0.
            success = mark_complete_para(category, task_index)#This line calls the Mark_Task_Complete function with parameters.

            if success == True:#This if is for if the task is successfully marked as complete.
                print("Your task has been marked as complete.")
                view_lists()
                input(con.CONTINUE)
                return

            elif success == con.ALREADY_COMPLETE:#This elif is for if the task is already marked as complete.
                print("[Invalid]\nYour task is already marked as complete. Please try again.\n")

       
        except ValueError:#This except block prevents the program from crashing when users enter invalid input that cannot be converted.
            print(con.INV_NOT_A_NUMBER) 
        except EOFError:#This except block prevents the program from EOFError(e.g. Ctrl+D or Ctrl+Z).
            print(con.INV_OPTION)


def mark_complete_para(category, comp_task):#This function manipulates user's input for marking a task.
    if 0 <= comp_task < len(tasks[category]):#This if checks if the task index is valid for the given category.
        if con.COMPLETE_MARKER in tasks[category][comp_task]:#This if checks if the task is already marked as complete.
            return con.ALREADY_COMPLETE
        
        #Adds COMPLETE_MARKER to the end of the task.
        complete_task = tasks[category][comp_task] + con.COMPLETE_MARKER
        tasks[category][comp_task] = complete_task
        return True
    
    else:#This else is for if the task index is invalid.
        return False

