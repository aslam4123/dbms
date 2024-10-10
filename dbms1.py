# import sqlite3

# con = sqlite3.connect('task.db')
# try:
#     con.execute("create table std(roll_no int,name text,age int)")
# except:
#     pass

# a=int(input('no.of students:'))
# for i in range(a):
#     roll_no=i+1
#     name=input('enter the name:')
#     age=int(input('enter the age:'))
#     con.execute("insert into std(roll_no,name,age)values(?,?,?)",(roll_no,name,age))
#     con.commit()

# data=con.execute('select name,age from std')
# for i in data:
#     print(i)

# roll_no=int(input('enter roll no of student that you want to select:'))
# data=con.execute('select * from std where roll_no=?',(roll_no,))
# for i in data:
#     print(i)

# con.execute("update std set name='yaseen',age=25 where name='vnmyasen' ")
# con.commit()

# name=input('enter the old name:')
# name1=input('enter the new name:')
# con.execute("update std set name=? where name=? ",(name1,name))
# con.commit()

# roll_no=int(input('enter the roll no:'))
# con.execute("delete from std where roll_no=? ",(roll_no,))
# con.commit()

# data=con.execute("select * from std where name like '%m' ")
# for i in data:
#     print(i)


# data=con.execute("select * from std order by name desc ")
# for i in data:
#     print(i)


import sqlite3

con = sqlite3.connect('mark.db')
try:
    con.execute("create table std(roll_no int,name text,age int)")
    con.execute("create table mark(roll_no int,sub text,mark int)")
except:
    pass
a=int(input('enter no of students:'))
for i in range(a):
    roll_no=i+1
    name=input('enter the name:')
    age=int(input('enter the age:'))
    con.execute("insert into std(roll_no,name,age)values(?,?,?)",(roll_no,name,age))
    con.commit()

