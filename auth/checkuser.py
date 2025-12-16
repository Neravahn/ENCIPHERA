import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'database.db')
def user_exists_email(email):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = """SELECT 1 FROM users where email = ?"""

    cursor.execute(query, (email,))

    return cursor.fetchone() is not None
    

def user_exist_username(username):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = """SELECT 1 FROM users WHERE username = ?"""

    cursor.execute(query, (username,))

    return cursor.fetchone() is not None

