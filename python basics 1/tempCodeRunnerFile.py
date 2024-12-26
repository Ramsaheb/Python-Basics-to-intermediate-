import sqlite3
conn = sqlite3.connect('abc')
print('connection successfully ')
q_table = 'Create Table students(Roll INT PRIMARY KEY, NAME TEXT, SCORE)'
conn.execute(q_table)
print('table created')