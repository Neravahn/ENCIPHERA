import sqlite3
from crypto_engine.decryption import decrypt
DB_PATH = 'database.db'

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("DELETE FROM files WHERE username = ?", ('prashant',))
# data = decrypt()
conn.commit()

