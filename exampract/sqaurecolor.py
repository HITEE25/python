import turtle

t = turtle.Turtle()
t.speed(5)

colors = ["red","yellow","blue","green"]

size = 100
for c in colors:
    #square has 4 sides
    t.color(c)
    for _ in range(4):
        t.forward(size)
        t.left(90)
    
    t.penup()
    t.forward(120)
    t.pendown()

turtle.done()
