import sqlite3

DB_PATH = 'database.db'
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