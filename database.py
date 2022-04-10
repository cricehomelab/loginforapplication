import sqlite3
from sqlite3 import Error
# from database import Database


class Database:
    def __init__(self):
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
        self.sql_create_tables = [self.sql_create_user_table, self.sql_create_notes_table]

    def create_table(self, conn, create_table_sql):
        """
        Creates database tables if they do not exist.

        :param conn: sql connection
        :param create_table_sql: tables to create with sqlite.
        :return:
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
        :return:
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

        :param conn: opened database object.
        :return: all users in db.

        """
        sql = ''' INSERT INTO users(name,password)
                      VALUES(?,?) '''
        cur = conn.cursor()
        cur.execute(sql, user_data)
        conn.commit()
        conn.close()
        return cur.lastrowid

    def find_user(self, conn):
        cur = conn.cursor()
        cur.execute("SELECT * from users")
        users = cur.fetchall()
        return users

    def add_note(self, conn, user_data):
        sql = '''INSERT INTO notes(note_id, name, notes)
        VALUES(?,?,?)'''
        cur = conn.cursor()
        cur.execute(sql, user_data)
        conn.commit()
        conn.close()
        return True

    def get_user_notes(self, conn, user_id):
        cur = conn.cursor()
        cur.execute("SELECT * FROM notes WHERE note_id=?", (user_id,))
        rows = cur.fetchall()
        return rows
