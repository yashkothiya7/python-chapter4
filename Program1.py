# create a database named “Sample_DB” in MySQL().create EMPLOYEE Table in it with fields eid,name and sal.enter valid records in table. 
#First ensure connection is made or not and then check if the database Sample_DB already exists or not, if yes then print 
#appropriate message. Also display all records of Employee table. 
import mysql.connector

con = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )
if con.is_connected():
    print("Connection to MYSQL successful!")

    cursor = con.cursor()    
    
    DB_NAME = 'Sample_DB'
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    print(f"Database '{DB_NAME}' is ready.")
    
    cursor.execute(f"USE {DB_NAME}")
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS EMPLOYEE (
            E_id INT PRIMARY KEY,
            Name VARCHAR(50),
            Sal INT
        )
    """)
    print("Employee table is ready.")

    cursor.execute("TRUNCATE TABLE EMPLOYEE")
    print("Cleared existing records from EMPLOYEE table.")

    n = int(input("\nHow many employees do you want to add? : "))
    
    for i in range(n):
        print(f"\nEnter details for Employee {i+1}:")
        eid = int(input("Enter Employee ID: "))
        name = input("Enter Employee Name: ")
        sal = int(input("Enter Employee Salary: "))
        
        cursor.execute("INSERT INTO EMPLOYEE (E_id, Name, Sal) VALUES (%s, %s, %s)", 
                       (eid, name, sal))
        
    print(f"\n{n} records inserted successfully!")

    cursor.execute("SELECT * FROM EMPLOYEE")
    rows = cursor.fetchall()
    
    print("\n--- Employee Records ---")
    for row in rows:
        print(row)



    if 'con' in locals() and con.is_connected():
        cursor.close()
        con.close()
        print("\n MySQL connection is closed.")