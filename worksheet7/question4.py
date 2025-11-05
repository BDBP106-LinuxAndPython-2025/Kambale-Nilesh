# (i) Create a database called school.db. You are going to build a simple student
# marks management system using SQLite3. Inside this databse, create a table
# called students with the following columns: id of type INTEGER, name of type
# TEXT, subject of type TEXT and marks of type INTEGER.

# (iii) Write SQL queries using Python to a) display all records in the table, b) display
# the names of students who scored above 80 marks, c) display the average marks
# in each subject.
# (iv) Update ”Suresh’s” science marks from 65 to 75.
# (v) Delete the record of the student who scored the lowest marks in English.
# (vi) Add a new column called ’grade’ to the table, and assign ”A” for marks >= 85,
# ”B” for marks between 70-84, and ”C” for marks< 70.

import sqlite3
conn = sqlite3.connect('school.db')
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER, name TEXT, subject TEXT,marks INTEGER)")

cur.executemany("INSERT OR REPLACE INTO students VALUES (?,?,?,?)",[
    (1,"Ravi","Math",85),
    (2,"Meena","Science",90),
    (3,"Arjun","English",78),
    (4,"Priya","Math",92),
    (5,"Suresh","Science",65)
])

conn.commit()
print("\na) display all records in the table")
cur.execute('SELECT * FROM students')
rows =cur.fetchall()
for row in rows:
    print(row)


print("\nb)display the names of students who scored above 80 marks")
for row in cur.execute('SELECT name FROM students WHERE marks >= ?', (80,)):
    print(row)

print('\nc) display the average marks in each subject')
for row in cur.execute('SELECT subject, AVG(marks) FROM students GROUP BY subject' ):
    print(row)

cur.execute("UPDATE students SET marks=75 WHERE name='Suresh'")

cur.execute("DELETE FROM students WHERE id=(SELECT id FROM students WHERE subject='English' ORDER BY marks ASC LIMIT 1)")

cur.execute("ALTER TABLE students ADD COLUMN grade TEXT")
cur.execute("UPDATE students SET grade = CASE WHEN marks>=85 THEN 'A' WHEN marks BETWEEN 70 AND 84 THEN 'B' ELSE 'C' END")

print("\ndisplay the final table of students")
cur.execute('SELECT * FROM students')
rows =cur.fetchall()
for row in rows:
    print(row)


cur.execute("DELETE FROM students")
conn.commit()

conn.commit()
cur.close()
conn.close()

