import sqlite3

conn = sqlite3.connect('data/database.sqlite')
conn.row_factory = sqlite3.Row
c = conn.cursor()
c.execute('SELECT * FROM League')
rows = c.fetchall()

# print(rows)
for row in rows:
    print(row['name'])
    
# conn = sqlite3.connect('data/database.sqlite')
# conn.row_factory = sqlite3.Row
# c = conn.cursor()
# c.execute('SELECT * FROM League WHERE id = 1')
# rows = c.fetchone()

# print(dict(rows))