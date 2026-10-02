from tkinter import *

def sum():
    n1 = int(e1.get())
    n2 = int(e2.get())
    label.config(text=f"sum: {n1+n2}")

def sub():
    n1 = int(e1.get())
    n2 = int(e2.get())
    label.config(text=f"sub: {n1 - n2}")

root = Tk()
root.title("Calculator")
root.geometry("400x400")

e1 = Entry(root)
e1.pack()
e2 = Entry(root)
e2.pack()

Button(root,command=sum,text="sum").pack()
Button(root,command=sub,text="sub").pack()

label = Label(root)
label.pack()

root.mainloop()
