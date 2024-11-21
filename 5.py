# 5. Set up a local SQLite database and create a table with some sample data. Use Python to import
#  data from the SQL table into a data frame and perform any 5 operations on the data frame.
import sqlite3
import pandas as pd

# Step 1: Set up SQLite database and table
# Connect to SQLite database (it will create one if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    department TEXT,
    salary REAL
)
''')

# Insert some sample data
cursor.executemany('''
INSERT INTO employees (name, age, department, salary)
VALUES (?, ?, ?, ?)
''', [
    ('Alice', 30, 'HR', 60000.0),
    ('Bob', 25, 'IT', 50000.0),
    ('Charlie', 35, 'Finance', 70000.0),
    ('Diana', 40, 'IT', 80000.0),
    ('Eve', 29, 'HR', 45000.0)
])

# Commit changes and close cursor
conn.commit()

# Step 2: Read data into a Pandas DataFrame
df = pd.read_sql_query('SELECT * FROM employees', conn)

# Display the initial DataFrame
print("Initial DataFrame:")
print(df)

# Step 3: Perform operations on the DataFrame

# 1. Filter employees in the 'IT' department
it_employees = df[df['department'] == 'IT']
print("\nEmployees in IT Department:")
print(it_employees)

# 2. Add a new column for bonus (10% of salary)
df['bonus'] = df['salary'] * 0.10
print("\nDataFrame with Bonus Column:")
print(df)

# 3. Calculate the average salary of employees
average_salary = df['salary'].mean()
print(f"\nAverage Salary: {average_salary}")

# 4. Sort employees by age
sorted_by_age = df.sort_values(by='age')
print("\nEmployees Sorted by Age:")
print(sorted_by_age)

# 5. Group by department and calculate the total salary for each department
total_salary_by_department = df.groupby('department')['salary'].sum()
print("\nTotal Salary by Department:")
print(total_salary_by_department)

# Close the connection
conn.close()
