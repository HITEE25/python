import turtle

t = turtle.Turtle()
t.speed(5)

colors = ["red","yellow","blue","green","pink"]

size = 50
j=0

for i in range(5):
    t.color(colors[j])
    for _ in range(3):
        t.forward(size)
        t.left(120)
    size += 20
    j += 1

turtle.done()
