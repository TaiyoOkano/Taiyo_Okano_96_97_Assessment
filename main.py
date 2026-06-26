'''
 PLEASE RUN THIS PYTHON FILE  
'''
#Import other files.
import constants as con
import options as op
import introduction as intro

#Welcome text
print("\n" + "=" * 26)
print(" Welcome to Yojana To-Do!")
print("=" * 26)


op.load_tasks()#This calls the load_tasks function to load from the saved_tasks.json file.

while True:#This while loop is for the main menu. It will keep running until users choose to exit the program by entering 5.
    try:#This try-except block prevents the program from crashing when users enter invalid input.
       #These are the main menu options.
        print("\n" + "=" * 44)
        print("                 MAIN MENU                  ")
        print("=" * 44)
        print("  0. Introduction to Yojana To-Do")
        print("  1. View Current Lists")
        print("  2. Add a New Task")
        print("  3. Remove a Task or List")
        print("  4. Mark a Task as Complete")
        print("  5. Save and Exit")
        print("=" * 44)
        #This line asks users to enter their option by number.
        user_input = int(input("Please choose your option (0-5):"))
        if user_input in con.OPTIONS:
            if user_input == con.MENU_INTRO:#This if is for introduction.
                intro.show_help()
                input(con.CONTINUE)
            elif user_input == con.MENU_VIEW:#This if is for View Lists.
                op.view_lists()
                input(con.CONTINUE)
            elif user_input == con.MENU_ADD:#This elif is for Add Task.
                op.add_task()
            elif user_input == con.MENU_REMOVE:#This elif is for Remove List.
                op.remove_list()
            elif user_input == con.MENU_MARK:#This elif is for Mark Complete.
                op.mark_complete()
            elif user_input == con.MENU_EXIT:#This elif is for Exit.
                op.save_tasks()
                break#End the loop.
        else:
            print(con.INV_OPTION)#This else is for if user's option is not available.
    except ValueError:#This except block prevents the program from crashing when users enter invalid input that cannot be converted.
        print(con.INV_NOT_A_NUMBER)
    except EOFError:#This except block prevents the program from EOFError(e.g. Ctrl+D or Ctrl+Z).
        print(con.INV_OPTION)