import tkinter
import sqlite3
# con=sqlite3.connect('tkinter_data.db')
# con.execute("create table sample(uname text,password text)")
win=tkinter.Tk()
win.title('login')
win.configure(bg='green')
win.minsize(400,400)
win.maxsize(600,600)
def Home():
    win2=tkinter.Tk()
    l1=tkinter.Label(win,text='Home page',bg='green',fg='black')
    l1.place(x=150,y=20)
    btn1=tkinter.Button(win2,text='logout',command=win2.quit)
    btn1.place(x=200,y=0)
    win2.mainloop()

def login():
    con=sqlite3.connect('tkinter_data.db')
    data=con.execute("select * from sample")
    f=0
    for i in data:
        if i[0]==e1.get() and i[1]==e2.get():
            f=1
            Home()
    if f==0:
        l3.config(text="invalid uname and password")

def reg_form():
    win1=tkinter.Tk()
    win1.minsize(400,400)
    win1.maxsize(600,600)

    def reg():
         con=sqlite3.connect('tkinter_data.db')
         con.execute("insert into sample(uname,password)values(?,?)",(e1.get(),e2.get()))
         con.commit()
         win1.destroy()

    l2=tkinter.Label(win1,text="name")
    l2.place(x=75,y=30)

    e1=tkinter.Entry(win1)
    e1.place(x=150,y=30)
    l2=tkinter.Label(win1,text="password")
    l2.place(x=75,y=60)

    e2=tkinter.Entry(win1)
    e2.place(x=150,y=60)
    btn1=tkinter.Button(win1,text='register',bg='gray',activebackground='black',activeforeground='white',command=reg)
    btn1.place(x=150,y=90)

    win.mainloop()

l1=tkinter.Label(win,text='welcome',bg='green',fg='black')
l1.place(x=150,y=20)

l2=tkinter.Label(win,text='name')
l2.place(x=75,y=30)

e1=tkinter.Entry(win)
e1.place(x=150,y=30)

l2=tkinter.Label(win,text='password')
l2.place(x=75,y=60)

e2=tkinter.Entry(win)
e2.place(x=150,y=60)

btn1=tkinter.Button(win,text='login',bg='gray',activebackground='black',activeforeground='white',command=login)
btn1.place(x=150,y=90)


btn2=tkinter.Button(win,text='Register',bg='gray',activebackground='black',activeforeground='white',command=reg_form)
btn2.place(x=150,y=120)
l3=tkinter.Label(win)
l3.place(x=150,y=160)

win.mainloop()


