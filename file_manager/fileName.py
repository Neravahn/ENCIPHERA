import sqlite3
import os



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'database.db')
def check_fileName(filename, username):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = "SELECT 1 FROM files WHERE username = ? AND filename = ?"
    cursor.execute(query, (username, filename))
    data = cursor.fetchone()
    conn.close()

    return data is None




