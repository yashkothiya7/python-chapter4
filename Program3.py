# Write a program to delete a row from an employee table by accepting the employee identity number (eid) from the user.

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Sample_DB"
)

if conn.is_connected():
    print("Connected to MYSQL Successfully!")
    
cursor = conn.cursor()

E_id = int(input("Enter Employee ID to delete: "))

# Delete query
cursor.execute("DELETE FROM Employee WHERE E_id = %s", (E_id,))   # after E_id write comma bcz it's tuple so otherwise py treat as number value
conn.commit()

if cursor.rowcount > 0:
    print(f"Employee with ID {E_id} deleted successfully!")
else:
    print(f"No record found with ID {E_id}!")

cursor.execute("SELECT * FROM Employee")
rows = cursor.fetchall()

print("\nEmployee Records After Delete:")
for row in rows:
    print(row)

cursor.close()
conn.close()
