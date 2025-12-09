import sqlite3
DB_PATH = 'database.db'

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("DELETE FROM files WHERE username = ?", ('prashant',))

conn.commit()

