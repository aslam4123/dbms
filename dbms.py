import sqlite3

con = sqlite3.connect('batch7.db')
try:
    con.execute("create table std(roll_no int,name text,age int)")
except:
    pass
con.execute("insert into std(roll_no,name,age)values(1,'aslam',21),(2,'muhammed',20)")
con.commit()

roll_no=int(input('enter the rollno:'))
name=input('enter the name:')
age=int(input('enter the age:'))

con.execute("insert into std(roll_no,name,age)values(?,?,?)",(roll_no,name,age))
con.commit()