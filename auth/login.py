from mathhash import verify_password
import sqlite3


DB_PATH = 'database.db'

def verify_user(username, password):


    conn = sqlite3.connect(DB_PATH)
    cursor  = conn.cursor()

    query =f"""
    SELECT password FROM users WHERE username = ?
    """
    cursor.execute(query, (username,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        return False

    hashed = row[0]


    return verify_password(password , hashed)