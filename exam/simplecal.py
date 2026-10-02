from tkinter import *

def clear():
    entry.delete(0,END)

def click(num):
    entry.insert(END,num)

def calculate():
    try:
        exp = eval(entry.get())
        entry.delete(0,END)
        entry.insert(0,exp)
    except:
        entry.delete(0,END)
        entry.insert(0,"Error ")

root = Tk()
root.geometry("400x400")
root.title("simple calculator")

entry = Entry(root,width=25,borderwidth=4)
entry.grid(row=0,column=0,columnspan=4)

button = [
    ('7',1,0),('8',1,1),('9',1,2),('/',1,3),
    ('4',2,0),('5',2,1),('6',2,2),('*',2,3),
    ('1',3,0),('2',3,1),('3',3,2),('+',3,3),
    ('0',4,0),('c',4,1),('=',4,2),('-',4,3),
]

for (text,row,col) in button:
    if text == 'c':
        btn = Button(root,command=clear,width=5,height=2,text=text)
    elif text == '=':
        btn = Button(root,command=calculate,width=5,height=2,text=text)
    else:
        btn = Button(root,command=lambda t=text: click(t),width=5,height=2,text=text)

    btn.grid(row=row,column=col)

root.mainloop()



