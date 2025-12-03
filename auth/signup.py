import sqlite3
from mathhash import hash_password   #<<----- MY HASHING LIBRARY :D

DB_PATH ="database.db"

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
        print("done")
        return {'success': 'SUCCESSFUL'}

    except sqlite3.IntegrityError as e:

        error_message = str(e)

        print(str(e))  #<<----- ONLY IN DEVLOPING PHASE


        if "users.username" in error_message:
            return {'error': 'Username already taken.'}
        elif "users.email" in error_message:
            return {'error': 'Email already registered.'}
        else:
            return {'error': 'Something went wrong'}
    
    finally: 
        conn.close()