import turtle

t = turtle.Turtle()
t.speed(5)

t.color("yellow")
t.begin_fill()
t.circle(100)
t.end_fill()

t.penup()
t.goto(30,10)
t.pendown()

t.color("white")
t.begin_fill()
t.circle(100)
t.end_fill()

turtle.done()