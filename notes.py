from database import Database


class Notes:
    def __init__(self):
        self.database = Database()
        self.notes = []

    def add_note(self, conn, user_info):
        """
        Adds a note to the database for a user

        :param conn: path to the database used to open a connection to the database.
        :param user_info: this is the logged_in_info from the user a tuple containing the (user_id, username,
        hashed password)
        :return: None
        """
        user_id = user_info[0]
        note_name = input("Please type in a title for this note: ")
        note_input = input("Please type your note in. \n")
        note_information = (user_id, note_name, note_input)
        db_connection = self.database.create_connection(conn)
        note_added = self.database.add_note(db_connection, note_information)
        if note_added:
            print(f"Note {note_name} added.")

    def edit_note(self, conn):
        choice = input("what note do you want to edit?: ")
        if choice.isdigit():
            choice = int(choice) - 1
        else:
            print("you will need to choose a number.")

        for num, note in enumerate(self.notes):
            if num == choice:
                print(f"name of note: {note[2]}")
                name = input("New name of note: ")
                print(f"contents of note: {note[3]}")
                content = input("New contents for this note: \n")
                edited_note = (name, content, note[0])

        db_connection = self.database.create_connection(conn)
        with db_connection:
            self.database.edit_note(db_connection, edited_note)




    def view_notes(self, conn, user_id):
        """
        outputs saved notes of a user.

        :param conn: path to the database used to open a connection to the database.
        :param user_id: this is the id for the user from the users table.
        :return: None
        """
        db_connection = self.database.create_connection(conn)
        self.notes = self.database.get_user_notes(db_connection, user_id)
        for num, note in enumerate(self.notes):
            print(f"note #{num + 1}")
            print(f"name: {note[2]}")
            print(f"note: {note[3]}")
        return len(self.notes)
