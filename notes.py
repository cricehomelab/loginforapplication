from database import Database


class Notes:
    def __init__(self):
        self.database = Database()

    def add_note(self, conn, user_info):
        user_id = user_info[0]
        note_name = input("Please type in a title for this note: ")
        note_input = input("Please type your note in. \n")
        note_information = (user_id, note_name, note_input)
        db_connection = self.database.create_connection(conn)
        self.database.add_note(db_connection, note_information)
