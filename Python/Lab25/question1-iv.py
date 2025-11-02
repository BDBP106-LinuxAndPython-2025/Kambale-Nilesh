# (iv) Write a program that allows the user to delete 1 or more records from the above
# database. The input is a single line containing the ID of the employees to be
# deleted, separated by spaces.
import sqlite3
conn=sqlite3.connect("IBABEmployee.db")
curs=conn.cursor()
curs.execute('SELECT * FROM Employee')
rows=curs.fetchall()
print(rows)

idn=input("Enter the employees ids which record has to be delete (seprated by space):").split()
for emp_id in idn:
   curs.execute(f"DELETE FROM Employee WHERE emp_ID=?",(int(emp_id),))

curs.execute('SELECT * FROM Employee')
rows=curs.fetchall()
print(rows)


conn.commit()
curs.close()
conn.close()
