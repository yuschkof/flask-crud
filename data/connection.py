import sqlite3


def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("../data.sqlite")
    except sqlite3.Error as e:
        print(e)
    return conn
