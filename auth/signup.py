import sqlite3
from mathhash import hash_password   #<<----- MY HASHING LIBRARY :D
import os




BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'database.db')

def save_user(name, username, email, password):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    hashed = hash_password(password)

    #SQL QUERY TO INSERT A NEW USER
    query = """
    INSERT INTO users (name, username, email, password)
    VALUES (?, ?, ?, ?)
    """

    data = [name, username, email, hashed]

    try:
        cursor.execute(query, data)
        conn.commit()
    except sqlite3.IntegrityError as e:

        error_message = str(e)

        print(str(e))  #<<----- ONLY IN DEVLOPING PHASE

    
    finally: 
        conn.close()