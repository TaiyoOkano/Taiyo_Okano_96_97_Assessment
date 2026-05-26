print("Welcome to a New To-do list!")

options = [1,2,3,4,5] 
while True:
    try:

        print()#This print function creates a blank line that might help clear reading for users.
        print("[1: View Lists, 2: Add Task, 3: Remove a Task, 4: Mark Complete, 5: Exit]")#This line is main menu options. Users will choose their option from the list.
        user_input = int(input("Please choose your option from the list above by a number \n: "))
        if user_input in options:
                
        else:
            print("Your option isn't available. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")