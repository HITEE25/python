from tkinter import *

root = Tk()
root.title("Line Chart")

canvas = Canvas(root, width=400, height=300)
canvas.pack()

# Example data points
points = [50, 100, 150, 80, 120]

x = 50
prev_y = points[0]

for y in points[1:]:
    canvas.create_line(x, prev_y, x+50, y)
    x += 50
    prev_y = y

root.mainloop()