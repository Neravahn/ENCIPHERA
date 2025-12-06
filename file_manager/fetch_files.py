import sqlite3

DB_PATH = 'database.db'
def fetch(username):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = """SELECT filename FROM files WHERE username = ?"""

    cursor.execute(query, (username,))

    name = cursor.fetchall()

    return name


# files = fetch('prashant')
# file_names = []
# for i in range(len(files)):
#     file_names.append(files[i][0])

# print(file_names)