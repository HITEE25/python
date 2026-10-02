from tkinter import *
import re

def login():
    if re.match(r'^\d+$',age.get()) and int(age.get) > 0 and int(age.get()) <= 100:
        label.config(text=f"name: {name.get()}, age: {age.get()}\n")
    else:
        label.config(text="invalid age")

root = Tk()
root.title("Form")
root.geometry("400x400")

name = Entry(root)
name.pack()

age = Entry(root)
age.pack()

Button(root,command=login,text="Submit").pack()

label = Label(root)
label.pack()

root.mainloop()
