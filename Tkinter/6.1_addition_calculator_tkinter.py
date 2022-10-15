from tkinter import *

def add():
    num1 = int(t1.get())
    num2 = int(t2.get())
    result = num1 + num2
    t3.insert(END, str(result))
    
root = Tk()
root.geometry("500x400")

lbl1=Label(root, text='First number')
lbl2=Label(root, text='Second number')
lbl3=Label(root, text='Result')
t1=Entry(bd=3)
t2=Entry()
t3=Entry()
btn1 = Button(root, text='Add')

lbl1.place(x=100, y=50)
t1.place(x=200, y=50)
lbl2.place(x=100, y=100)
t2.place(x=200, y=100)
b1=Button(root, text='Add', command=add)

b1.place(x=250, y=150)

lbl3.place(x=100, y=200)
t3.place(x=200, y=200)



root.mainloop()

