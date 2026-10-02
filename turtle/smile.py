import turtle
t = turtle.Turtle()
t.speed(6)

t.penup()
t.goto(0,-100)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.circle(100)
t.end_fill()

t.penup()
t.goto(-40,30)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(40,30)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(-50,-30)
t.right(50)
t.pendown()
t.circle(60,120)


turtle.done()