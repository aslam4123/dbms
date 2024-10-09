import sqlite3

con = sqlite3.connect('task.db')
try:
    con.execute("create table std(roll_no int,name text,age int)")
except:
    pass

a=int(input('no.of students:'))
for i in range(a):
    roll_no=i+1
    name=input('enter the name:')
    age=int(input('enter the age:'))
    con.execute("insert into std(roll_no,name,age)values(?,?,?)",(roll_no,name,age))
    con.commit()