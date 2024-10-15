import mysql.connector
con=mysql.connector.connect(user='aslam',host='localhost',password='Aslam123',database='mysql2')
con.autocommit=True
cur=con.cursor()
# cur.execute("create database mysql2")
try:
    cur.execute("create table std (roll_no int,name text,age int)")
except:
    pass
a=int(input('enter no of student:'))
for i in range(a):
    roll_no=int(input('enter the rollno:'))
    name=input('enter the name:')
    age=int(input('enter the age:'))
    cur.execute("insert into std (roll_no,name,age)values(%s,%s,%s)",(roll_no,name,age))

