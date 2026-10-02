from tkinter import *

def login():
    name = entry_name.get()
    p = entry_pass.get()
    if name == "" or p == "":
        label.config(text="invalid")
    else:
        label.config(text=f"name: {name} , Password: {p}")

root = Tk()
root.geometry("400x400")
Label(root,text="Name:").pack()
entry_name = Entry(root)
entry_name.pack()

Label(root,text="Password:").pack()
entry_pass = Entry(root,show="*")
entry_pass.pack()

Button(root,command=login,text="login").pack()
label = Label(root,text="")
label.pack()

root.mainloop()