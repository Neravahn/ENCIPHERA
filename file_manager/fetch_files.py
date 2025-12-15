import sqlite3

DB_PATH = 'database.db'
def fetch(username, file_type):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = """SELECT filename FROM files WHERE username = ? AND file_type = ?"""

    cursor.execute(query, (username, file_type))

    name = cursor.fetchall()

    cursor.close()
    conn.close()

    return name


