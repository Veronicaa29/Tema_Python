import sqlite3

conn = sqlite3.connect("operations.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM requests")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
