import turtle
t = turtle.Turtle()
t.speed(5)

t.left(30)
t.forward(60)

for i in range(6):
    t.left(60)
    t.forward(60)

t.left(120)
t.forward(120)
t.left(120)
t.forward(60)
t.left(120)
t.forward(120)

t.right(120)
t.forward(60)

t.penup()
t.goto(0,20)
t.pendown()

t.left(120)
t.forward(40)

for i in range(5):
    t.left(60)
    t.forward(40)

turtle.done()