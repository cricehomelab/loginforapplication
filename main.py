# my classes
from database import Database
from user_login import Login
from notes import Notes
# python classes and modules.
from os.path import exists
import os

# Global variables.
DB_PATH = f"{os.getcwd()}\\database.db"

# Objects created.
database = Database()
user_functions = Login()
notes = Notes()

running = True
print("welcome to MyNotes")

logged_in_user = ""

# create database
if not exists(DB_PATH):
    print("Creating database.")
    for table in database.sql_create_tables:
        db_conn = database.create_connection(DB_PATH)
        database.create_table(db_conn, table)
    print("Database created.")
else:
    print("database.db exists already, not re-creating database.")

# loop for the application
while running:
    if logged_in_user == "" or logged_in_user is None:
        # These are the options a user who is not logged in can access.
        user_choice = input("what would you like to do?: ")
        if user_choice == "c" or user_choice == "create":
            user_functions.create_user()
        elif user_choice == "e" or user_choice == "exit":
            print("Goodbye.")
            running = False
        elif user_choice == "h" or user_choice == "help":
            print("e or exit - this exits the application.")
            print("h or help - this brings up the help screen.")
            print("c or create for create user. ")
        elif user_choice == "l" or user_choice == "login":
            user = input("Enter your username.: ")
            user_password = input("Enter your password.: ")
            user_info = [user, user_password]
            logged_in_user = user_functions.login_user(user_info)
        else:
            print("Invalid selection. type h, or help for options.")
    else:
        # these are the options that a logged in user can access.
        print(f"{logged_in_user[1]} is logged in.")
        user_choice = input("What would you like to do?")
        if user_choice == "a" or user_choice == "add":
            notes.add_note(DB_PATH, logged_in_user)
        elif user_choice == "h" or user_choice == "help":
            print("a or 'add' to add a note.")
            print("l or 'logout' to log out.")
            print("v or 'view' to view your notes.")
        elif user_choice == "l" or user_choice == "logout":
            print(f"logging out of {logged_in_user[1]}")
            logged_in_user = None
        elif user_choice == "v" or "view":
            view = True
            while view:
                notes.view_notes(DB_PATH, logged_in_user[0])
                user_choice = input("Note view: ")
                if user_choice == "a" or user_choice == "add":
                    notes.add_note(DB_PATH, logged_in_user)
                elif user_choice == "b" or user_choice == "back":
                    view = False
                elif user_choice == "e" or user_choice == "edit":
                    notes.edit_note(DB_PATH)
                elif user_choice == "h" or user_choice == "help":
                    print("b or 'back' to go back.")
                    print("e or 'edit' to edit a note.")



