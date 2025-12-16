import sqlite3
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'database.db')
def delete(username, file_name):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = "DELETE FROM files WHERE username = ? and filename = ?"
    cursor.execute(query, (username, file_name))

    conn.commit()
    cursor.close()
    conn.close()
