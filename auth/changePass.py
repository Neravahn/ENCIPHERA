import sqlite3
from mathhash import hash_password
import os





BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'database.db')
conn = sqlite3.connect(DB_PATH)
curosr = conn.cursor()

def changePassUsername(username, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    hashed = hash_password(password)


    query = "UPDATE users SET password = ? WHERE username = ?"
    cursor.execute(query, (hashed, username))
    conn.commit()
    conn.close()

    return True



def changePassEmail(email, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    hashed = hash_password(password)


    query = "UPDATE users SET password = ? WHERE email = ?"
    cursor.execute(query, (hashed, email))

    conn.commit()
    conn.close()


    return True


def getEmail(username):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    query = "SELECT email FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    email = cursor.fetchone()[0]



    return email


