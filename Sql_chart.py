import mysql.connector
import matplotlib.pyplot as plt

conn = mysql.connector.connect(
    host="localhost",
    user="root",        
    password="" 
)
cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS CompanyDB")
cursor.execute("USE CompanyDB")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Employee (
    id INT PRIMARY KEY AUTO_INCREMENT,
    department VARCHAR(50),
    emp_count INT
)
""")

cursor.execute("TRUNCATE TABLE Employee")
print("Cleared existing records from EMPLOYEE table.")

cursor.executemany("""INSERT INTO Employee (department, emp_count) VALUES (%s, %s)""", [
    ('HR', 10),
    ('Finance', 15),
    ('IT', 30),
    ('Sales', 25),
    ('Marketing', 20)
])
conn.commit()  
print("Database and table created, data inserted successfully!")

cursor.execute("SELECT department, emp_count FROM Employee")
rows = cursor.fetchall()

departments = [row[0] for row in rows]
employee_counts = [row[1] for row in rows]

plt.pie(employee_counts, labels=departments, autopct='%1.1f%%', startangle=90)
plt.title("Percentage of Employee in Each Department")
plt.axis('equal')  
plt.show()


cursor.close()
conn.close()
