# (v) Write a program that displays all the records present in the above database in a
# formatted manner.
import sqlite3
conn=sqlite3.connect("IBABEmployee.db")
curs=conn.cursor()
query="SELECT * FROM Employee"
curs.execute(query)
print("\nData from Employee table:")
print("\n ID        Name           Research           Designation     Gender")
curs.execute('SELECT * FROM Employee')

rows =curs.fetchall()
for row in rows:
    print(f'\n{row}')
    
conn.commit()
curs.close()
conn.close()