# The tkinter.ttk module provides access to the Tk-themed widget set, introduced in Tk 8.5.

# The basic idea for tkinter.ttk is to separate, to the extent possible, the code implementing a widget’s behavior from the code implementing its appearance. 
# tkinter.ttk is used to create modern GUI (Graphical User Interface) applications that cannot be achieved by tkinter itself.


# import everything from tkinter module
from tkinter import *   
 
# create a tkinter window
root = Tk()             
 
# Open window having dimension 100x100
root.geometry('200x200')
 
# Create a Button
btn = Button(root, text = 'Click me !', bd = '3',
                          command = root.destroy)

# Set the position of button on the top of window.  
btn.pack(side = 'top')   
# or simply type below code to type in center of window
# btn.pack()
 
root.mainloop()