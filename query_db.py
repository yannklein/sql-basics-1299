import sqlite3

conn = sqlite3.connect('data/database.sqlite')
conn.row_factory = sqlite3.Row
c = conn.cursor()

# c.execute("SELECT * FROM Country")
# rows = c.fetchall()

# print(rows)
# for row in rows:
#     print(f'{row[0]} - {row[1]}')

# for row in rows:
#     print(f'{row["id"]} - {row["name"]}')
    
    
c.execute("SELECT * FROM Country WHERE id = 1")
row = c.fetchone()
print(dict(row))