'''
 Please do NOT run this Python file
'''
#Introduction for Yojana To-Do.
def show_help():
    print("\n" + "~" * 55)
    print("                  Help & Introduction")
    print(" Hello! Welcome to your new productivity hub.")
    print("Yojana To-Do is designed to keep your tasks organized")
    print("neatly into separate categories (e.g. 'work', etc.).")
    print("~" * 55)

    print("\n QUICK START GUIDE:")
    print("  1. View Current Lists      -> See all your categories and tasks.")
    print("  2. Add a New Task          -> Create a category and add a task inside.")
    print("  3. Remove a Task or List   -> Delete an entire category or just one task.")
    print("                                You can delete all lists if you wish.")
    print("  4. Mark a Task as Complete -> Tick off a task with a [ ✓ ] mark.")
    print("  5. Save and Exit           -> Safely saves everything to your computer.")

    eg_tasks = {
        "work": ["homework","house cleaning"],
      
       
    }
    

    print("\n HERE IS WHAT YOUR TO-DO LIST LOOKS LIKE:")
    print("-" * 21)
    print(" Current To-Do List  ")
    print("-" * 21)
    for category, task_list in eg_tasks.items():
        print(f"[ {category.upper()} ]")
        for task in task_list:
            print(f" : {task}")
    print("-" * 21)
    print("\n[ WORK ] -> This is a category.")
    print(": homework\n: house cleaning -> These two are tasks.")

    print("\n  TIPS:")
    print("  - You can type '0' at any time to cancel and run back to the Main Menu.")
    print("  - When exiting, ALWAYS use option 5 so your hard-earned progress is saved.")




