import turtle
t = turtle.Turtle()

t.speed(5)

t.circle(100)

t.penup()
t.goto(-50,40)
t.pendown()

for i in range(4):
    t.forward(100)
    t.left(90)

t.penup()
t.goto(-50,50)
t.pendown()

for i in range(3):
    t.forward(90)
    t.left(120)

turtle.done()