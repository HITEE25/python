import turtle

t = turtle.Turtle()

t.fillcolor("yellow")

t.begin_fill()
t.circle(100)
t.end_fill()

t.penup()
t.goto(-45,130)
t.pendown()
#left-eye
t.fillcolor("black")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(45,130)
t.pendown()
#right-eye
t.fillcolor("black")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(-50,80)
t.setheading(-60)
t.pendown()

t.circle(60,120)

turtle.done()