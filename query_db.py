import sqlite3
import sys 
import tracemalloc

tracemalloc.start()

print("Mem alloc initial (current, peak)")
print(tracemalloc.get_traced_memory())

conn = sqlite3.connect('data/database.sqlite')
conn.row_factory = sqlite3.Row

print("Mem alloc after connection (current, peak)")
print(tracemalloc.get_traced_memory())

c = conn.cursor()

print("Mem alloc before execute (current, peak)")
print(tracemalloc.get_traced_memory())

c.execute('SELECT * FROM Player_Attributes')

print("Mem alloc after execute (current, peak)")
print(tracemalloc.get_traced_memory())

rows = c.fetchall()

print("Mem alloc after fetch all (current, peak)")
print(tracemalloc.get_traced_memory())
 
tracemalloc.stop()