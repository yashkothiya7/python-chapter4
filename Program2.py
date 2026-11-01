# Write program to increase salary (sal) of employee in the employee table by accepting the employee identity number (eid) from the user. 
import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "Sample_DB"
)

if conn.is_connected():
    print("Connected to MYSQL Successfully!")
    
cursor = conn.cursor()
E_id = int(input("Enter Employee I'd to Increase Salary : "))
Increase = int(input("Enter Amount to Increase Salary : "))

cursor.execute("UPDATE Employee SET Sal = Sal + %s WHERE E_id = %s", (Increase, E_id))
conn.commit()

if cursor.rowcount > 0:
    print(f"\nSalary updated for Employee I'd : {E_id}")
else:
    print(f"No record found with I'd {E_id}!")

cursor.execute("SELECT * FROM Employee")
rows = cursor.fetchall()

print("\nEmployee Records After Update:")
for row in rows:
    print(row)

cursor.close()
conn.close()
