from tkinter import *

balance = 1000

def deposit():
    global balance
    amt = int(entry.get())
    if amt > 0:
        balance += amt
        label.config(text=f"Balance: {balance}")
    else:
        label.config(text=f"Balance: {balance} amount should > 0")

def withdraw():
    global balance
    amt = int(entry.get())
    if amt > balance:
        label.config(text=f"Balance: {balance} insuffcint amount")
    else:
        balance -= amt
        label.config(text=f"Balance: {balance}")

root = Tk()
root.geometry("400x400")
root.title("Banking")

Label(root,text="Enter amount:").grid(row=0,column=0)
entry = Entry(root)
entry.grid(row=0,column=1)

Button(root,command=deposit,text="Deposit").grid(row=1,column=0)
Button(root,command=withdraw,text="Withdraw").grid(row=1,column=1)

label = Label(root,text="Balance = 1000")
label.grid(row=2,column=0,columnspan=2)

root.mainloop()

