import tkinter as tk

# Create window
root = tk.Tk()
root.title("Simple Calculator")

# Entry box
entry = tk.Entry(root, width=25, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Functions
def click(num):
    entry.insert(tk.END, num)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('C',4,1), ('=',4,2), ('+',4,3)
]

# Create buttons
for (text, row, col) in buttons:
    if text == "C":
        btn = tk.Button(root, text=text, width=5, height=2, command=clear)
    elif text == "=":
        btn = tk.Button(root, text=text, width=5, height=2, command=calculate)
    else:
        btn = tk.Button(root, text=text, width=5, height=2,
                        command=lambda t=text: click(t))
    
    btn.grid(row=row, column=col)

# Run GUI
root.mainloop()