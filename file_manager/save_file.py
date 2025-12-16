import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'database.db')
def save(username, file_name, file_type, data: bytes):


    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = """
    INSERT INTO files (username, filename, file_type, data)
    VALUES (?, ?, ?, ?)
    """


    cursor.execute(query, (username, file_name, file_type, data))
    conn.commit()
    return True

