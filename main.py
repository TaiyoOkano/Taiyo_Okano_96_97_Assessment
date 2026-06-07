import json
print("Welcome to a New To-do list!\n")

tasks = {}#This is an empty dictionary that will be used to store the tasks that users add to their to-do list.

def save_tasks():#This function serialize the dictionary.
    with open("saved_tasks.json", "w") as f:
        print("Saving your tasks...")
        json.dump(tasks, f)

def load_tasks():#This function deserialize the dictionary.
    try:#This try-except gblock would create a new To-Do list if there is no saved_tasks.json file.
        global tasks
        with open("saved_tasks.json", "r") as f:
            tasks = json.load(f)
            if tasks == {}:
                print("Start with a new To-Do list.")
            else:
                print("Start with your previous tasks.")
    except FileNotFoundError:
        print("No saved tasks found. Start with a new To-Do list.")
        
load_tasks()

def View_Lists():#This function is for users to view thier current To-Do list.
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

    if category not in tasks:
        tasks[category] = []     

    if new_task in tasks[category]:
        return False
    else:
        tasks[category].append(new_task)
        return True


def Remove_List():#This function is for users to remove a task from thier To-Do list.
    print("Remove a List.")
    while True:      
        try:#This try-except block prevents the program from crashing when users enter invalid input.
            del_ask = int(input("Do you want to remove a category or a task? Or clear all lists? Enter by 1, 2, or 3. \n[1: Category, 2: Task, 3: Clear All Lists]\n: "))
            if del_ask == 1:
                View_Lists()
                category_name = input("Enter the category you want to remove\n: ").strip().lower()

                success = Remove_Category(category_name)#This line calls the Remove_Category function and receives boolean.
                if success == True:
                    print(f"Your category [{category_name}] has been removed.")
                    View_Lists()
                else:
                    print(f"Your category [{category_name}] doesn't exist. Please try again.\n")
                break
    
            elif del_ask == 2:
                View_Lists()
                category = input("Enter the category of the task you want to remove\n: ").strip().lower()
                if category not in tasks:
                    print(f"Your category [{category}] doesn't exist. Please try again.")
                    continue

                for i, task in enumerate(tasks[category]):
                    print(f"{i + 1}: {task}")

                task_num = int(input("Enter the number of the task you want to remove\n: "))
                task_index = task_num - 1
                success = Remove_Task(category, task_index)#This line calls the Remove_Task function with parameters.

                if success == True:
                    print("Your task has been removed.")
                    View_Lists()
                else:
                    print("Invalid task number. Please try again.\n")
                break
            elif del_ask == 3:
                tasks.clear()
                print("All your lists have been cleared.")
                break
            else:
                print("Your option isn't available. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.\n")


def Remove_Category(category_name):  
    if category_name in tasks:
        del tasks[category_name]
        return True
    
    else:
        return False

        

def Remove_Task(category, task_index):
    if 0 <= task_index < len(tasks[category]):
        del tasks[category][task_index]
        return True
        
    else:
        return False

        
def Mark_Complete():#This function is for users to mark a task as complete in their To-Do list.
    print("Mark Complete.")
    View_Lists()
    category = input("Enter the category of the task you want to mark as complete\n: ").strip().lower()
    if category not in tasks:
        print(f"Your category [{category}] doesn't exist. Please try again.")
        return
    
    comp_task = input("Enter a task you want to mark as complete: ").strip().lower()
    #If the task is in the list, it will add "(Complete)" to the end of the task.
    if comp_task in tasks[category]:
        complete_task = comp_task + "(Complete)"
        tasks[category].remove(comp_task)
        tasks[category].append(complete_task)
        print(f"Your task '{comp_task}' has been marked as complete in [{category}].")
    else:
        print(f"Task '{comp_task}' not found in [{category}].")

options = [1,2,3,4,5] 
while True:#This while loop is for the main menu. It will keep running until users choose to exit the program by entering 5.
    try:#This try-except block prevents the program from crashing when users enter invalid input.
        print("\n")#This print function creates a blank line that might help clear reading for users.
        print("[1: View Lists, 2: Add Task, 3: Remove a List, 4: Mark Complete, 5: Exit]")#This line is main menu options. Users will choose their option from the list.
        user_input = int(input("Please choose your option from the list above by a number \n: "))
        if user_input in options:
            if user_input == 1:
                View_Lists()
            elif user_input == 2:
                View_Lists()
        
                category = input("Enter a category (e.g. work, personal)\n: ").strip().lower()
                if category == "":#This if statement is for if category is empty or just spaces.
                    print("Category cannot be empty or just spaces. Please try again.")
                    continue

                while True:#This while loop is for if the category is valid, it will keep asking users to enter a task until they enter a valid task that can be added to the list.
                    new_task = input("Enter a task you want to add: ").strip().lower()
                    if new_task == "":
                        print("Your task cannot be empty or just spaces. Please try again.")
                        continue

                    success = Add_Task(category, new_task)
                    if success == True:
                        print(f"Your task '{new_task}' has been added to [{category}].")
                        View_Lists()
                        break
                    else:
                        print(f"!Your task '{new_task}' already exists in [{category}]!\nPlease try again.")
                        
                        
                        

            elif user_input == 3:
                Remove_List()
            elif user_input == 4:
                Mark_Complete()
            elif user_input == 5:
                save_tasks()
                print("Goodbye.")
                break
        else:
            print("Your option isn't available. Please try again.")
    except ValueError:#This except block prevents the program from crashing when users enter invalid input that cannot be converted.
        print("Invalid input. Please enter a number.\n")
    except EOFError:#This except block prevents the program from EOFError(e.g. Ctrl+D or Ctrl+Z).
        print("Invalid input. Please try again.\n")