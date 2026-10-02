import turtle
#create turtle to draw
t = turtle.Turtle()

t.speed(5)

#draw circle
t.circle(100)

#move inside
t.penup()
t.goto(-70,30)
t.pendown()

for i in range(4):
    t.forward(140)
    t.left(90)

#move inside
t.penup()
t.goto(-70,40)
t.pendown()

for i in range(3):
    t.forward(140)
    t.left(120)

turtle.done()

