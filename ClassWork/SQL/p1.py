import sqlite3
from sqlite3 import Error

def connect_db(path):
    con = None
    try:
        con = sqlite3.connect(path)
        print('Connection successful')
    except Error as e:
        print(e)
    return con

def execute_read_query(conn, query):
    try:
        cur = conn.cursor()
        cur.execute(query) #runs all python queryies
        results = cur.fetchall()
        conn.commit()
        print("Query executed successfully!!")
    except Error as e:
        print(e)
    return results

def close_connection(conn):
    try:
        if conn:
            conn.close()
            print("connection closed")
    except Error as e:
        print(e)

path = "C:\\Users\\dbda.STUDENTSDC\\Desktop\\PythonPrograming\\ClassWork\\SQL\\company.db"

# Create table query
create_table_query = """
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL
);
"""

# Insert query
insert_query = """
INSERT INTO employees (name, department, salary)
VALUES 
    ('John Doe', 'IT', 75000),
    ('Jane Smith', 'HR', 65000),
    ('Mike Johnson', 'Sales', 55000);
"""

# Update query
update_query = """
UPDATE employees 
SET salary = salary * 1.1
WHERE department = 'IT';
"""

# Delete query
delete_query = """
DELETE FROM employees
WHERE department = 'Sales';
"""

# Select query
select_query = """
SELECT * FROM employees
;
"""
connection = connect_db(path)

execute_read_query(connection, create_table_query)
execute_read_query(connection, insert_query)
execute_read_query(connection, select_query)