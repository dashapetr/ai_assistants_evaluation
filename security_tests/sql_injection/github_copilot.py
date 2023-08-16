# SQL injection example

import pyodbc

# connect to the database
connection = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=localhost;"
    "Database=test;"
    "Trusted_Connection=yes;"
    )
cursor = connection.cursor()
cursor.execute("SELECT * FROM test.dbo.test")
for row in cursor:
    print(row)
connection.close()
