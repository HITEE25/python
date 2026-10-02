from tkinter import *

def add():
    label.config(text=f"add: {int(n1.get())+int(n2.get())}")

def mul():
    label.config(text=f"mul: {int(n1.get())*int(n2.get())}")

root = Tk()
root.title("calculator")
root.geometry("400x400")

#enter first number
n1 = Entry(root)
n1.pack()

#enter 2 number
n2 = Entry(root)
n2.pack()

Button(root,command=add,text="Add").pack()
Button(root,command=mul,text="Mul").pack()

label = Label(root)
label.pack()

root.mainloop()



