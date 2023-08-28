# SQL injection example in python

# Sure, I'll provide a basic example to demonstrate SQL injection in
# Python using the SQLite database for simplicity. Please remember that this example is for educational purposes only,
# and you should always follow best security practices to prevent SQL injection in real-world applications.
#
# 1. Setup: Creating a SQLite Database
#
# First, let's create a simple SQLite database with a table named users that has columns username and password.

import sqlite3

# Connect to a database (or create one if it doesn't exist)
conn = sqlite3.connect('sample_db.sqlite')
cursor = conn.cursor()

# Create a 'users' table
cursor.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

# Insert some sample data
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin", "admin_pass"))
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("user", "user_pass"))

# Commit changes and close the connection
conn.commit()
conn.close()


# 2. Vulnerable Login Function (Prone to SQL Injection)
#
# Now, let's create a login function that is vulnerable to SQL injection due to the unsanitized input:

def vulnerable_login(username, password):
    conn = sqlite3.connect('sample_db.sqlite')
    cursor = conn.cursor()

    # Unsafe query construction
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

    cursor.execute(query)
    result = cursor.fetchone()

    conn.close()
    return result


# Simulating an SQL injection attack
attacker_input = "admin' OR '1'='1"  # This will always evaluate to True
print(vulnerable_login(attacker_input, 'random_password'))

# In the above example, the attacker's input makes the WHERE clause always true, which allows unauthorized access.
# This demonstrates the risk of SQL injection when not properly handling user input.
#
# 3. Safe Login Function (Using Parameterized Queries)
#
# Here's the recommended way to handle the login function using parameterized queries:

def safe_login(username, password):
    conn = sqlite3.connect('sample_db.sqlite')
    cursor = conn.cursor()

    # Safe query using parameterized input
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()

    conn.close()
    return result


print(safe_login('admin', 'admin_pass'))

# This safe_login function is resistant to SQL injection attacks because it uses parameterized queries,
# ensuring that user input is always treated as data and never as executable code.
# Always use parameterized queries or similar safe methods when working
# with databases to prevent SQL injection vulnerabilities.
