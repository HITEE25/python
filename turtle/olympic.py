import turtle
t = turtle.Turtle()
t.speed(6)
colors = ["blue","black","red","yellow","green"]

size = -100

for color in colors:
    t.up()
    t.goto(size,0)
    t.down()
    t.color(color)
    t.circle(50)
    size += 60

turtle.done()