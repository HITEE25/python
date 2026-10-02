from tkinter import *

# Function to update expression
def press(num):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + str(num))

# Function to evaluate result
def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, str(result))
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

# Function to clear
def clear():
    entry.delete(0, END)

# Create window
root = Tk()
root.title("Simple Calculator")

# Entry field
entry = Entry(root, width=20, borderwidth=5, font=("Arial", 18))
entry.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
]

# Create buttons dynamically
for (text, row, col) in buttons:
    if text == "=":
        Button(root, text=text, width=5, height=2, command=equal).grid(row=row, column=col)
    else:
        Button(root, text=text, width=5, height=2,
               command=lambda t=text: press(t)).grid(row=row, column=col)

# Clear button
Button(root, text="C", width=22, height=2, command=clear).grid(row=5, column=0, columnspan=4)

# Run GUI
root.mainloop()