import sqlite3

DB_PATH = 'database.db'

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


print(get_user_files('prashant', 'txt test 1'))