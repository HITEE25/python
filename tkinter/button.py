from tkinter import *

def show():
    label.config(text="Button Clicked!")

root = Tk()

label = Label(root, text="Hello")
label.pack()

Button(root, text="Click Me", command=show).pack()

root.mainloop()