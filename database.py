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
        print('create_connection() called, connecting to database.')
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            # return conn
        except Error as e:
            print(e)

        return conn

    def create_user(self, conn, user_data):
        sql = ''' INSERT INTO users(name,password)
                      VALUES(?,?) '''
        cur = conn.cursor()
        cur.execute(sql, user_data)
        conn.commit()
        conn.close()
        return cur.lastrowid

    def find_user(self, conn, user):
        cur = conn.cursor()
        cur.execute("SELECT * from users")
        users = cur.fetchall()
        return users