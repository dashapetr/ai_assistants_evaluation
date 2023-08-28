# query the SQL table ‘Sales’ and find all sales in 2022

import pyodbc

# Database connection parameters
server = 'YOUR_SERVER_NAME'
database = 'YOUR_DATABASE_NAME'
username = 'YOUR_USERNAME'
password = 'YOUR_PASSWORD'
driver = '{ODBC Driver 17 for SQL Server}'

# Create the connection string
connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Connect to the database
connection = pyodbc.connect(connection_string)

# SQL query to fetch sales in 2022
query = """
SELECT *
FROM Sales
WHERE YEAR(sale_date) = 2022
"""

# Execute the query
cursor = connection.cursor()
cursor.execute(query)
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the connection
connection.close()

# Replace the placeholders with your actual database details.
# Also, you might need to adjust the SQL query if the column names or table schema are different.
#
# Remember:
#
# This is a generic example. Depending on the actual structure and columns of your Sales table,
# you may need to adjust the SQL query.
# Always be cautious about sharing or exposing database credentials.
# It's good practice to store them securely and not hardcode them directly in scripts.
