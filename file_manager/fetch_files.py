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


# files = fetch('prashant')
# file_names = []
# for i in range(len(files)):
#     file_names.append(files[i][0])

# print(file_names)