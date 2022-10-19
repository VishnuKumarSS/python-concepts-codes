from tkinter import *
root = Tk()
root.geometry("300x300")
a=Label(root,text="A").place(x=30,y=70)
b=Label(root,text="B").place(x=30,y=100)
c=Label(root,text="C").place(x=30,y=130)
add= Button(root, text="Add").place(x=120,y=160)
a_button = Entry(root, width = 30).place(x = 60,y = 70)  
b_button = Entry(root,width = 30).place(x = 60, y = 100)  
c_button = Entry(root,width = 30).place(x =60,y = 130)
root.mainloop()

