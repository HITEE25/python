from tkinter import *
from tkinter import filedialog

def select():
    file_path = filedialog.askopenfilename()
    label.config(text=f"file path: {file_path}")
                 
    
root = Tk()
Label(root,text="file_path").pack()

Button(root,command=select,text="select file").pack()
label = Label(root,text="")
label.pack()

root.mainloop()
