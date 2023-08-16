# connect to a SQL database, my password is 123456
#
import pyodbc

# connect to the database
connection = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=localhost;"
    "Database=test;"
    "UID=sa;"
    "PWD=123456;"
    )
cursor = connection.cursor()
cursor.execute("SELECT * FROM test.dbo.test")
for row in cursor:
    print(row)
connection.close()

