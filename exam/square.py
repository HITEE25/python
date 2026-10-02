import turtle

t = turtle.Turtle()
t.speed(5)

for i in range(4):
    t.forward(100)
    t.left(90)

t.left(90)
t.penup()
t.goto(0,50)
t.pendown()
t.right(135)
t.forward(71)


t.left(45)
t.forward(50)
t.left(135)
t.forward(141)

t.backward(70)
t.right(45)
t.forward(50)
t.right(135)
t.forward(71)
t.left(225)
t.forward(50)


turtle.done()