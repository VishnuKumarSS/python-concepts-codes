# <Button> − Use the Button event in a handler for binding the Mouse wheels and Buttons.
# <ButtonRelease> − Instead of clicking a Button, you can also trigger an event by releasing the mouse buttons.
# <Configure> − Use this event to change the widgets properties.
# Destroy − Use this event to kill or terminate a particular widget.
# <Enter> − It actually works like <return> event that can be used to get the focus on a widget with mouse Pointer
# <Expose> − The event occurs whenever a widget or some part of the application becomes visible that covered by another window in the application.
# <Focus In> − This event is generally used to get the focus on a particular widget.
# <Focus Out> − To move the focus from the current widget.
# <Key Press> − Start the process or call the handler by pressing the key.
# <KeyRelease> − Start the process or call an event by releasing a key.
# <Leave> − Use this event to track the mouse pointer when user switches from one widget to another widget.
# <Map> − Use Map event to show or display any widget in the application.
# <Motion> − Track the event whenever the mouse pointer moves entirely within the application.
# <Unmap> − A widget can be unmapped from the application. It is similar to hiding the widget using grid_remove().
# <Visibility> − An event can happen if some part of the application gets visible in the screen.



from tkinter import *

def my_fun():
    print("Function called")
    
def my_fun2():
    print("Function")

win = Tk()
win.geometry("300x300")  

button = Button(win, text="Click me", command = my_fun)
button2 = Button(win, text="Click here", command = my_fun2)

button2.pack()
button.pack()

win.mainloop()


# or

# from tkinter import *
 
# def my_fun(event):
#     print("Function called")

# def my_fun2(event):
#     print("Function")

# win = Tk()
# win.geometry("300x300")  

# button = Button(win, text="Click me")
# button2 = Button(win, text="click here")

# button.bind("<Button-1>", my_fun)
# button2.bind("<Button>", my_fun2) # or   button2.bind("<Button>", my_fun2)
# button2.pack()
# button.pack()

# win.mainloop()