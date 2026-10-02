from tkinter import *

root = Tk()
root.geometry("400x400")

def fun():
    chld = Toplevel(root)
    chld.mainloop()

Button(root,command=fun,text="open").pack()
root.mainloop()
