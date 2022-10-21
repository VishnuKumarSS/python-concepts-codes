# Creation of Button without using tk themed widget. 
 
# Creation of Button using tk themed widget (tkinter.ttk). This will give you the effects of modern graphics. Effects will change from one OS to another because it is basically for the appearance.

# import tkinter module
from tkinter import *       
 
# Following will import tkinter.ttk module and
# automatically override all the widgets
# which are present in tkinter module.
from tkinter.ttk import *
 
# Create Object
root = Tk()
 
# Initialize tkinter window with dimensions 100x100            
root.geometry('200x200')    
 
btn = Button(root, text = 'Click me !',
                command = root.destroy) # why we used root.destroy here is, when we click the button . The root window to destroy. (i.e) program should end.
 
# Set the position of button on the top of window
btn.pack(side = 'top')    
 
root.mainloop()