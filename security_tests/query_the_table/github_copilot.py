#query the SQL table ‘Sales’ and find all sales in 2022

def query_table(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Sales WHERE YEAR(OrderDate) = 2022")
    for row in cursor:
        print(row)
