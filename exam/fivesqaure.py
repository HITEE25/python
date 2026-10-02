import turtle
t = turtle.Turtle()

size = 200

for i in range(5):
    for j in range(4):
        t.forward(size)
        t.left(90)

    t.penup()
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.right(90)
    t.pendown()

    size -= 20

t.penup()
t.goto(50,50)
t.pendown()

for i in range(3):
    t.forward(100)
    t.left(120)

turtle.done()
