from tkinter import *

def calculate_grade():
    marks = int(entry.get())

    if marks >= 90:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 50:
        grade = "c"
    else:
        grade = "d"
    label.config(text=f"grade: {grade}")

root = Tk()
root.title("Grade cal")
root.geometry("400x400")

Label(root,text="Enter marks: ").pack()
entry = Entry(root)
entry.pack()

Button(root,command=calculate_grade,text="calculate grade").pack()
label = Label(root,text="")
label.pack()
root.mainloop()