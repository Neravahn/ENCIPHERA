import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'database.db')
def get_user_files(username, file_name):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = "SELECT data FROM files WHERE username = ? and filename = ?"

    cursor.execute(query, (username, file_name)) 
    file = cursor.fetchone()
    
    if file:
        file = file[0]



    cursor.close()
    conn.close()
    return file

