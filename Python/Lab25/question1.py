# (1) SQLite exercise:

# (i) Write a program to create an SQLite database in the file IBABEmployee.db that
# contains a table called Employee with fields ID, name, research area, designation
# and gender.
import sys
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

#query ="DROP TABLE IF EXISTS Employee"
#curs.execute(query)



print()
print()
print()
# (ii) Write a program that allows the user to add multiple records into the above
# database file. After every record, the user should be asked whether he/she wants
# to add another record. Do this for all the faculty in IBAB.

def records():
    b=int(input("Give the ID no.of Employee: "))
    c=input("Give the employee name: ")
    d=input("Give the employee research area: ")
    e=input("Give the employee designation: ")
    f=input("Give the employee gender: ")
    data=(b,c,d,e,f)
    return data
a=True
while a:
    data=records()
    curs.execute(query,data)
    a = input("Do you want to continue? (y/n): ").lower()
    if a != 'y':
        break
curs.execute('SELECT * FROM Employee')
print("\nData from Employee table:")
rows =curs.fetchall()
for row in rows:
    print(f'\n{row}')


curs.execute("DELETE FROM Employee")
conn.commit()

conn.commit()
curs.close()
conn.close()

# Delete all records after user enters them


# (iii) Write a program that allows the user to edit an entry present in the above data-
# base. The program should ask for the ID of the employee and should take in the
#
# new details of the employee.
# (iv) Write a program that allows the user to delete 1 or more records from the above
# database. The input is a single line containing the ID of the employees to be
# deleted, separated by spaces.
# (v) Write a program that displays all the records present in the above database in a