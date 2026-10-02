from tkinter import *

root = Tk()
root.title("Registration form")
root.geometry("400x400")

Label(root,text="Name").pack()
name = Entry(root)
name.pack()

#gender
Label(root,text="Gender").pack()
g = StringVar()
Radiobutton(root,text="Female",value="female",variable=g).pack()
Radiobutton(root,text="Male",value="Male",variable=g).pack()

#listbox => courses
Label(root,text="course").pack()
lb = Listbox(root)
lb.insert(1,"It")
lb.insert(2,"cp")
lb.insert(3,"me")
lb.pack()

#checkbox => skills
Label(root,text="skills").pack()
Checkbutton(root,text="web-dev").pack()
Checkbutton(root,text="painting").pack()

#button
Button(root,text="Submit").pack()


root.mainloop()