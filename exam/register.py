from tkinter import *

def submit():
    print(entry.get())
    print(gender.get())

    Hobbies = []
    if hobby1.get() == 1:
        Hobbies.append("dance")
    if hobby2.get() == 1:
        Hobbies.append("sing")

    print(Hobbies)
    selected_course = course.get(course.curselection())
    print(selected_course)

root = Tk()
root.geometry("400x400")
root.title("Register")

Label(root,text="Name: ").grid(row=0,column=0)
entry = Entry(root)
entry.grid(row=0,column=1)

Label(root,text="Gender: ").grid(row=1,column=0)
gender = StringVar()
Radiobutton(root,variable=gender,text="female",value="female").grid(row=2,column=0)
Radiobutton(root,variable=gender,text="male",value="male").grid(row=2,column=1)

Label(root,text="Hobby: ").grid(row=3,column=0)
hobby1 = IntVar()
hobby2 = IntVar()

Checkbutton(root,text="Dance",variable=hobby1).grid(row=4,column=0)
Checkbutton(root,text="sing",variable=hobby2).grid(row=4,column=1)

Label(root,text="select course: ").grid(row=5,column=0)

course = Listbox(root)
course.insert(1,"it")
course.insert(2,"cp")
course.insert(3,"ee")
course.insert(4,"ci")

course.grid(row=6,column=1)

Button(root,command=submit,text="submit").grid(row=7,column=0)

root.mainloop()
