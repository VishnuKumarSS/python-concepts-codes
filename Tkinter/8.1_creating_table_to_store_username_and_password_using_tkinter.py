# this program is to display if the database is connected it will show Successfully connected

from msilib.schema import tables
import tkinter as tk
import mysql.connector as ms
from tkinter import *
    

def getting():
    user = Username.get()
    passw = password.get()
    print(f"The Entered Username is {user}, And the Password is {passw}")

    db = ms.connect(host ="localhost",user = user,password = passw,db ="starz")
    if db.is_connected():
        print("successfully connected.")
    my_cursor = db.cursor()
    table_name = input("Enter table name that you want to create : ")
    my_cursor.execute(f"create table if not exists {table_name}(Username varchar(30) primary key, Password varchar(30))" )

                    
root = tk.Tk()
root.geometry("350x300")
root.title("TABLE for UserName and PassWord.")


# Defining the first row, (i.e) label for username row
label_username = tk.Label(root, text ="Username -", )
label_username.place(x = 50, y = 20)

Username = tk.Entry(root, width = 35)
Username.place(x = 150, y = 20, width = 100)

# creating the second row, (i.e) label for password row
label_password = tk.Label(root, text ="Password -")
label_password.place(x = 50, y = 50)

password = tk.Entry(root, width = 35)
password.place(x = 150, y = 50, width = 100)

# here creating button for submit.
submit_button = tk.Button(root, text ="Login", bg ='white', command = getting) # the command = .... is for if we click the submit button then it will call the corresponding that we have given
submit_button.place(x = 150, y = 135, width = 55)


root.mainloop()
