# import tkinter

# win=tkinter.Tk()
# win.title('batch7')
# win.configure(bg='green')
# win.minsize(400,400)
# win.maxsize(600,600)

# l1=tkinter.Label(win,text='welcome',bg='green',fg='black')
# # l1.pack()
# # l1.place(x=100,y=20)
# # l1.grid(row=0,column=0)
# l2=tkinter.Label(win,text='welcome')
# # l2.pack()
# # l2.place(x=200,y=200)
# l2.grid(row=10,column=2)

# win.mainloop()

import tkinter

win=tkinter.Tk()
win.title('batch7')
win.configure(bg='green')
win.minsize(400,400)
win.maxsize(600,600)
def save():
    # print(e1.get())
    l3.config(text=e1.get())

l1=tkinter.Label(win,text='welcome',bg='green',fg='black')
l1.place(x=150,y=20)

l2=tkinter.Label(win,text='name')
l2.place(x=75,y=50)

e1=tkinter.Entry(win)
e1.place(x=150,y=50)

btn1=tkinter.Button(win,text='save',bg='gray',activebackground='black',activeforeground='white',command=save)
btn1.place(x=150,y=70)

l3=tkinter.Label(win)
l3.place(x=150,y=120)

win.mainloop()