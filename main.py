print("Welcome to a New To-do list!")

options = [1,2,3,4,5] 
while True:
    try:

        print("\n")#This print function creates a blank line that might help clear reading for users.
        print("[1: View Lists, 2: Add Task, 3: Remove a Task, 4: Mark Complete, 5: Exit]")#This line is main menu options. Users will choose their option from the list.
        user_input = int(input("Please choose your option from the list above by a number \n: "))
        if user_input in options:
            if user_input == 1:
                print("Viewing lists (not implemented yet).")
            elif user_input == 2:
                print("Add Task (not implemented yet).")
            elif user_input == 3:
                print("Remove a Task (not implemented yet).")
            elif user_input == 4:
                print("Mark Complete (not implemented yet).")
            elif user_input == 5:
                print("Exiting. Goodbye!")
                break
        else:
            print("Your option isn't available. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")