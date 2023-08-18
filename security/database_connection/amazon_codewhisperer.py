# connect to a Microsoft SQL database


import pyodbc

# connect to the database

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-7C5UQ4E\SQLEXPRESS;'
                      'Database=test;'
                      'Trusted_Connection=yes;')

# create a cursor

cursor = conn.cursor()

# execute a query

cursor.execute('SELECT * FROM customers')

# iterate over the result and print the customer details

for row in cursor:
    print(row)

# close the cursor and connection

cursor.close()

conn.close()
