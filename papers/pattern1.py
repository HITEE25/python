import turtle

t = turtle.Turtle()
t.speed(5)

t.circle(100)

#create inside square
t.penup()
t.goto(-70,30)
t.pendown()

#square side = underroot(2) * r
for i in range(4):
    t.forward(141)
    t.left(90)

#10 + 60
t.forward(70)
t.left(120)
t.forward(100)
t.left(150)
t.forward(88)
t.left(90)
t.forward(60)

t.forward(50)
t.left(120)
t.forward(100)
t.left(150)
t.forward(85)
t.left(90)
t.forward(60)

t.left(90)
t.forward(100)
t.left(90)
t.forward(141)


turtle.done()