from tkinter import *

def cal_si():
    p = int(entry_p.get())
    r = int(entry_r.get())
    n = int(entry_y.get())
    si = (p*n*r)/100
    result_var.set(str(si))

root = Tk()
root.geometry("600x600")

Label(root,text="Pricipal(Rs.):").grid(row=0,column=0)
entry_p = Entry(root)
entry_p.grid(row=0,column=1)

Label(root,text="Rate(%):").grid(row=1,column=0)
entry_r = Entry(root)
entry_r.grid(row=1,column=1)

Label(root,text="Time(year):").grid(row=2,column=0)
entry_y = Entry(root)
entry_y.grid(row=2,column=1)

Button(root,command=cal_si,text="Check Simple Interest").grid(row=3,column=0)

Label(root,text="Simple Interest").grid(row=4,column=0)
result_var = StringVar()
Entry(root,textvariable=result_var).grid(row=4,column=1)

root.mainloop()
