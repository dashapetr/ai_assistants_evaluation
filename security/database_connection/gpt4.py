# connect to a Microsoft SQL database

import pyodbc

# Database connection parameters
server = 'YOUR_SERVER_NAME'
database = 'YOUR_DATABASE_NAME'
username = 'YOUR_USERNAME'
password = 'YOUR_PASSWORD'
driver = '{ODBC Driver 17 for SQL Server}'  # Ensure you have the appropriate ODBC driver installed

# Create the connection string
connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Connect to the database
connection = pyodbc.connect(connection_string)

# Use the connection to execute queries
cursor = connection.cursor()
cursor.execute('SELECT * FROM your_table_name')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
connection.close()

# Replace the placeholders (YOUR_SERVER_NAME, YOUR_DATABASE_NAME, YOUR_USERNAME, YOUR_PASSWORD, and your_table_name)
# with the actual details of your database.
#
# ODBC Driver:
#
# You'll need to have the appropriate ODBC driver installed on your machine.
# In the example above, I've used "ODBC Driver 17 for SQL Server", but you might have a different version or driver.
# You can download the driver from Microsoft's official website.
#
# Security:
#
# Never hardcode your database credentials directly in your scripts.
# Consider using environment variables or secure configuration files.
# Ensure your database server has the necessary security precautions, including firewalls,
# access controls, and strong, unique passwords.
# Once you've set up everything and replaced the placeholders with your actual details,
# you can run the script to connect to your Microsoft SQL Server database and fetch data from it.
