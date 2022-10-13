from tkinter import *

def addition():
    t3.delete(0, 'end') # here clearing the previous answer from the result
    num1 = int(t1.get())
    num2 = int(t2.get())
    result = num1 + num2
    t3.insert(END, str(result)) # here we are inserting the answer to the result box.

def subtraction():
    t3.delete(0, 'end') # here clearing the previous answer from the result
    num1 = int(t1.get())
    num2 = int(t2.get())
    result = num1 - num2
    t3.insert(END, str(result)) # here we are inserting the answer to the result box.

def multiplication():
    t3.delete(0, 'end') # here clearing the previous answer from the result
    num1 = int(t1.get())
    num2 = int(t2.get())
    result = num1 * num2
    t3.insert(END, str(result)) # here we are inserting the answer to the result box.

def division():
    t3.delete(0, 'end') # here clearing the previous answer from the result
    num1 = int(t1.get())
    num2 = int(t2.get())
    result = num1 / num2
    t3.insert(END, str(result)) # here we are inserting the answer to the result box.
                
root = Tk()
root.geometry("500x400")

lbl1=Label(root, text='First number')
lbl2=Label(root, text='Second number')
lbl3=Label(root, text='Result')
t1=Entry()
t2=Entry()
t3=Entry(bd=3)
btn1 = Button(root, text='Add')
btn1 = Button(root, text='Sub')
btn1 = Button(root, text='Multiply')
btn1 = Button(root, text='Divide')

lbl1.place(x=100, y=50)
t1.place(x=200, y=50)
lbl2.place(x=100, y=100)
t2.place(x=200, y=100)

b1=Button(root, text='Add', command=addition)
b1.place(x=120, y=150)
b2=Button(root, text='Sub', command=subtraction)
b2.place(x=180, y=150)
b3=Button(root, text='Multiply', command=multiplication)
b3.place(x=240, y=150)
b4=Button(root, text='Divide', command=division)
b4.place(x=320, y=150)


lbl3.place(x=100, y=200)
t3.place(x=200, y=200)


root.mainloop()