import sqlite3



DB_PATH = 'database.db'
def check_fileName(filename, username):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = "SELECT 1 FROM files WHERE username = ? AND filename = ?"
    cursor.execute(query, (username, filename))
    data = cursor.fetchone()
    conn.close()

    return data is None




print(check_fileName('prashant', 'hello'))
