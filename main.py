import json
print("Welcome to a New To-do list!\n")

tasks = []#This is an empty list that will be used to store the tasks that users add to their to-do list.

def save_tasks():#This function serialize the list.
    with open("saved_tasks.json", "w") as f:
        print("Saving your tasks...")
        json.dump(tasks, f)

def load_tasks():#This function deserialize the list.
    try:
        global tasks
        with open("saved_tasks.json", "r") as f:
            tasks = json.load(f)
            if tasks == []:
                print("Start with a new To-Do list.")
            else:
                print("Start with your previous tasks.")
    except FileNotFoundError:
        print("No saved tasks found. Start with a new To-Do list.")
        
load_tasks()

def View_Lists():
    print("Here is your current to-do list.")
    print(f"{tasks}")

def Add_Task():
    print("Add Task.")
    while True:
        new_task = input("Enter a task you want to add: ").strip().lower()
        if new_task == "":
            print("Your task cannot be empty or just spaces. Please try again.")
        elif new_task in tasks:#This elif line prevents to save same name tasks.  
            print(f"!Your task '{new_task}' has already been added to the list!\nPlease try again.")
        else:
            tasks.append(new_task)
            print(f"Your task '{new_task}' has been added.")
            break

def Remove_Task():
    print("Remove a Task.")
    del_task = input("Enter a task you want to remove: ").strip().lower()
    if del_task in tasks:
        tasks.remove(del_task)
        print(f"Your task '{del_task}' has been removed.")
    elif del_task + "(Complete)" in tasks:
        tasks.remove(del_task + "(Complete)")
        print(f"Your task '{del_task}' has been removed.")
    else:
        print(f"Task '{del_task}' not found in the list.")

def Mark_Complete():#String Concatenation
    print("Mark Complete.")
    comp_task = input("Enter a task you want to mark as complete: ").strip().lower()
    if comp_task in tasks:
        complete_task = comp_task + "(Complete)"
        tasks.remove(comp_task)
        tasks.append(complete_task)
        print(f"Your task '{comp_task}' has been marked as complete.")
    else:
        print(f"Task '{comp_task}' not found in the list.")

options = [1,2,3,4,5] 
while True:
    try:
        print("\n")#This print function creates a blank line that might help clear reading for users.
        print("[1: View Lists, 2: Add Task, 3: Remove a Task, 4: Mark Complete, 5: Exit]")#This line is main menu options. Users will choose their option from the list.
        user_input = int(input("Please choose your option from the list above by a number \n: "))
        if user_input in options:
            if user_input == 1:
                View_Lists()
            elif user_input == 2:
                Add_Task()
            elif user_input == 3:
                Remove_Task()
            elif user_input == 4:
                Mark_Complete()
            elif user_input == 5:
                save_tasks()
                print("Goodbye.")
                break
        else:
            print("Your option isn't available. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")