# (iii) Write a program that allows the user to edit an entry present in the above data-
# base. The program should ask for the ID of the employee and should take in the

import sqlite3
from operator import truediv

conn = sqlite3.connect('IBABEmployee.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE IF NOT EXISTS Employee 
                (
                    emp_ID INTEGER,
                    emp_Name TEXT,
                    emp_ResearchArea TEXT,
                    emp_Designation TEXT,
                    emp_Gender TEXT
                )
             ''')

# First way
query = """INSERT INTO Employee VALUES (?,?,?,?,?)"""
curs.execute('INSERT INTO Employee VALUES (1,"Bibha Choudhary", "Disease & Genomics","Professor","Female")' )
# Second Way
curs.execute(query,(2,"Jayashree Nagesh","Quantum Biology","Profess","Female"))
# Third way
emp3 = [(3,"Nithya Ramakrishnan","Algorithm machine learning in Biology","Professor","Female"),(4,"R.Srivatsan","Data Analytics","Professor","Male")]
curs.executemany(query,emp3)

curs.execute('SELECT * FROM Employee')
print(curs.fetchall())
curs.execute('SELECT * FROM Employee')
print("\nData from Employee table:")

id_n=int(input("Enter Employee ID: "))
name=input("Enter Employee Name: ")
res=input("Enter Employees New Research Area: ")
desi=input("Enter Employees New Designation: ")
gen=input("Enter Employees correct Gender: ")

curs.execute(f"""
        UPDATE Employee 
        SET emp_Name='{name}',emp_ResearchArea='{res}',emp_Designation='{desi}',emp_Gender='{gen}'
        WHERE emp_ID={id_n}
    """)
curs.execute('SELECT * FROM Employee')
rows=curs.fetchall()
print(rows)

conn.commit()
curs.close()
conn.close()



















