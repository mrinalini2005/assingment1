cursor.execute("SELECT * FROM employees WHERE salary > 50000")
print(cursor.fetchall())