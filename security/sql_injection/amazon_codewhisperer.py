# SQL injection example


import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()

c.execute("SELECT * FROM users WHERE username = 'admin' AND password = 'admin'")

print(c.fetchone())

conn.close()

# This is a SQL injection example.

# The username and password are not sanitized.

# The user can enter any string to the username and password fields.

# The database will return the user's data.

# The user can see the user's data.
