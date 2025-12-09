import sqlite3

DB_PATH = 'database.db'

def delete(username, file_name):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = "DELETE FROM files WHERE username = ? and filename = ?"
    cursor.execute()
    cursor.close()
    conn.close()
