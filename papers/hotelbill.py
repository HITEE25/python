from tkinter import *

#create dictanry to store all data
prices = {
    "pasta":80,
    "pizza":120,
    "sandwich":60,
    "sushi":150,
}

total = 0

def add_item():
    global total
    item = selected_item.get()
    q = int(qty.get())
    #cost of current item
    cost = prices[item] * q

    total += cost
    #insert into list box , insert at the end of listbox
    listbox.insert(END,f"{item} x {q} = {cost}")
    label.config(text=f"Total : {total}")


root = Tk()
root.title("bill")
root.geometry("400x400")

#create a dropdown list
selected_item = StringVar() #to create gui
#.set by default
selected_item.set("pizza")
#OptinMenu is a widget to create dropdown
OptionMenu(root, selected_item,*prices.keys()).pack()

#take input from textbox
Label(root,text="Quantity").pack()
qty = Entry(root)
qty.pack()

Button(root,text="add item",command=add_item).pack()

listbox = Listbox(root)
listbox.pack()

label = Label(root,text="Total: 0")
label.pack()

root.mainloop()