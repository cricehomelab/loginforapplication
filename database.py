import sqlite3
from sqlite3 import Error



class Database:
    def __init__(self):
        # Variables needed for table creation.
        self.sql_create_user_table = """CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        password text
                                    ); """
        self.sql_create_notes_table = """CREATE TABLE IF NOT EXISTS notes (
                                    id integer PRIMARY KEY,
                                    note_id integer NOT NULL,
                                    name text NOT NULL,
                                    notes text NOT NULL,                                    
                                    FOREIGN KEY (note_id) REFERENCES users (id)
                                );"""
        # Variables are stored in a list to be allow me to iterate the creation of the tables.
        self.sql_create_tables = [self.sql_create_user_table, self.sql_create_notes_table]

    def create_table(self, conn, create_table_sql):
        """
        Creates database tables if they do not exist.

        :param conn: sql connection
        :param create_table_sql: tables to create with sqlite.
        :return: None
        """
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
            conn.close()
        except Error as e:
            print(e)

    def create_connection(self, db_file):
        """
        creates the database.db file.

        :param db_file: file path to the database.
        :return: conn: this is the database connection that is created when the function runs.
        """

        conn = None
        try:
            conn = sqlite3.connect(db_file)
            # return conn
        except Error as e:
            print(e)

        return conn

    def create_user(self, conn, user_data):
        """
        creates a new user in the user's table of the sqlite database.

        :param conn: opened database object.
        :param user_data: Tuple containing the username and hashed password.
        :return:
        """
        sql = ''' INSERT INTO users(name,password)
                      VALUES(?,?) '''
        cur = conn.cursor()
        cur.execute(sql, user_data)
        conn.commit()
        conn.close()
        return cur.lastrowid

    def find_user(self, conn):
        """
        outputs a list of users to check against for login.

        :param conn: opened database object.
        :return: users: this is a list of nested tuples containing the user table.
        """
        cur = conn.cursor()
        cur.execute("SELECT * from users")
        users = cur.fetchall()
        conn.close()
        return users

    def add_note(self, conn, user_data):
        """
        adds a note for the user to the database.

        :param conn:  opened database object.
        :param user_data: tuple containing the note_id which is the user id from the user table, the name of the note,
         and the contents of the note.
        :return: True
        """
        sql = '''INSERT INTO notes(note_id, name, notes)
        VALUES(?,?,?)'''
        cur = conn.cursor()
        cur.execute(sql, user_data)
        conn.commit()
        conn.close()
        return True

    def get_user_notes(self, conn, user_id):
        """
        queries the database for notes associated with the user_id from the users table.

        :param conn: opened database object
        :param user_id: this is the user id associated with this table from the users table.
        :return: rows: these are the notes added by a given user.
        """
        cur = conn.cursor()
        cur.execute("SELECT * FROM notes WHERE note_id=?", (user_id,))
        rows = cur.fetchall()
        conn.close()
        return rows

    def edit_note(self, conn, note):
        """
        Commits an edit to the database.
        :param conn: active DB connection.
        :param note: tuple with the details of the note that need to be edited (name of note, contents of notes,
        id of the note to be edited)
        :return: None
        """
        sql = '''UPDATE notes
                 SET name = ?,
                     notes = ?
                 WHERE id = ?'''
        cur = conn.cursor()
        cur.execute(sql, note)
        conn.commit()

