from tkinter import *
balance = 1000

def deposit():
    global balance
    amt = int(entry.get())
    balance += amt
    label.config(text=f"Balance: {balance}")
    
def withdraw():
    global balance
    amt = int(entry.get())
    balance -= amt
    label.config(text=f"Balance: {balance}")

root = Tk()
root.geometry("400x400")

entry = Entry(root)
entry.pack()

Button(root,command=deposit,text="Deposit").pack()
Button(root,command=withdraw,text="Withdraw").pack()

label = Label(root,text="Balance: 1000")
label.pack()

root.mainloop()