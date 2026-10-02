from tkinter import *

prices = {
    "Pizza":500,
    "Pasta":300,
    "Sushi":1000,
    "CheeseBread":100
}

total = 0

def add_item():
    global total
    item = selected_item.get()
    q = int(entry.get())

    cost = prices[item] * q
    total += cost

    list.insert(END,f"{item} x {q} = {cost}")
    label.config(text=f"Total : {total}")

root = Tk()
root.geometry("400x400")
root.title("Restarent Bill")

selected_item = StringVar()
selected_item.set("Pizza")
OptionMenu(root,selected_item,*prices.keys()).pack()

Label(root,text="Quantity").pack()
entry = Entry(root)
entry.pack()

Button(root,command=add_item,text="Genrate Bill").pack()

list = Listbox(root)
list.pack()
label = Label(root,text="Total: 0")
label.pack()

root.mainloop()

