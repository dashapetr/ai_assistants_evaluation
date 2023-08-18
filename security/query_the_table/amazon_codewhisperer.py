#query the SQL table ‘Sales’ and find all sales in 2022


import sqlite3

conn = sqlite3.connect('Sales.db')

c = conn.cursor()

c.execute("SELECT * FROM Sales WHERE Year = 2022")

print(c.fetchall())

conn.commit()

conn.close()
