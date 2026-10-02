from tkinter import *

def login():
    if user.get() == "admin" and pwd.get() == "123":
        lable.config(text="Succesfully login")
    else:
        lable.config(text="Invalid")

root = Tk()
root.title("Login")
root.geometry("400x400")

user = Entry(root)
user.pack()

pwd = Entry(root,show="*")
pwd.pack()

Button(root,command=login,text="Login").pack()

lable = Label(root)
lable.pack()

root.mainloop()