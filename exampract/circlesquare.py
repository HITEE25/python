import turtle

t = turtle.Turtle()
t.speed(5)

t.circle(100)

t.penup()
t.goto(-50,50)
t.pendown()

t.color("red","blue")
t.begin_fill()

for i in range(4):
    t.forward(100)
    t.left(90)

t.end_fill()

turtle.done()