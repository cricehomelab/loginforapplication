from database import Database


class Notes:
    def __init__(self):
        self.database = Database()

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

    def view_notes(self, conn, user_id):
        """

        :param conn: path to the database used to open a connection to the database.
        :param user_id: this is the id for the user from the users table.
        :return: None
        """
        db_connection = self.database.create_connection(conn)
        notes = self.database.get_user_notes(db_connection, user_id)
        for num, note in enumerate(notes):
            print(f"note #{num + 1}")
            print(f"name: {note[2]}")
            print(f"note: {note[3]}")

