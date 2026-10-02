from tkinter import *

root = Tk()
root.title("Line Chart")

canvas = Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# Sample data
data = [50, 100, 80, 150, 120]

# Draw axes
canvas.create_line(50, 250, 350, 250)  # X-axis
canvas.create_line(50, 250, 50, 50)    # Y-axis

# Plot line chart
x = 60
prev_x, prev_y = None, None

for value in data:
    y = 250 - value

    if prev_x is not None:
        canvas.create_line(prev_x, prev_y, x, y)

    canvas.create_oval(x-3, y-3, x+3, y+3, fill="black")

    prev_x, prev_y = x, y
    x += 60

root.mainloop()