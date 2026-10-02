from tkinter import *

def display():
    label.config(text=entry.get())

root = Tk()

entry = Entry(root)
entry.pack()

Button(root, text="Show", command=display).pack()

label = Label(root, text="")
label.pack()

root.mainloop()