from tkinter import *
#global blance
balance = 1000

def deposit():
    global balance
    amount = int(entry.get())
    balance += amount
    label.config(text=f"balance : {balance}")
    
def withdraw():
    global balance
    amount = int(entry.get())
    balance -= amount
    label.config(text=f"balance : {balance}")

#create window
root = Tk()
#create title
root.title("Bank app")
root.geometry("400x400")
#to take input
entry = Entry(root)
entry.pack()


Button(root,command=deposit,text="deposit").pack()
Button(root,command=withdraw,text="withdraw").pack()

label = Label(root,text="Balance : 1000")
label.pack()

root.mainloop()


