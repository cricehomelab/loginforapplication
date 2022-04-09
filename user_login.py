from database import Database
import hashlib
import os

class Login:
    def __init__(self):
        self.database = Database()
        self.db_path = f"{os.getcwd()}\\database.db"

    def encrypt_string(self, hash_string):
        sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
        return sha_signature

    def create_user(self):
        user_name = input("Pick a user name.")
        # Ensuring password is created correctly.
        password_creation = True
        while password_creation:
            password_1 = input("choose a password.")
            password_2 = input("confirm your password.")
            if password_1 != password_2:
                print("passwords do not match.")
            else:
                user_password = self.encrypt_string(password_1)
                password_creation = False
        account_creation = (user_name, user_password)
        db_connection = self.database.create_connection(self.db_path)
        self.database.create_user(db_connection, account_creation)
        print("Account created. ")

    def login_user(self, user_info):
        logged_in = False
        username = user_info[0]
        password = self.encrypt_string(user_info[1])
        db_connection = self.database.create_connection(self.db_path)
        users = self.database.find_user(db_connection, username)
        for user in users:
            if username == user[1]:
                if password == user[2]:
                    logged_in = True
                    print(f"logging in {username}.")
                    break
        if logged_in is True:
            return user
        else:
            print("Username or password is incorrect try logging in again")
