print("Welcome to a New To-do list!")

tasks = []#This is an empty list that will be used to store the tasks that users add to their to-do list.
def View_Lists():
    print("Here is your current to-do list.")
    print(f"{tasks}")

def Add_Task():
    print("Add Task.")
    new_task = input("Enter a task you want to add: ")
    tasks.append(new_task)
    print(f"Your task '{new_task}' has been added.")

def Remove_Task():
    print("Remove a Task.")
    del_task = input("Enter a task you want to remove: ") 
    tasks.remove(del_task)
    print(f"Your task '{del_task}' has been removed.")

def Mark_Complete():
    print("Mark Complete (not implemented yet).")


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
                print("Goodbye.")
                break
        else:
            print("Your option isn't available. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")