import turtle

t = turtle.Turtle()

size = 100

for i in range(5):
    for j in range(4):
        t.forward(size)
        t.left(90)

    size += 10

turtle.done()
