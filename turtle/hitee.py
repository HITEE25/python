import turtle

t = turtle.Turtle()
t.speed(1)

# Function to move without drawing
def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# H
move(-200, 0)
t.left(90)
t.forward(100)
t.backward(50)
t.right(90)
t.forward(50)
t.left(90)
t.forward(50)
t.backward(100)

t.right(90)

# I
move(-120, 0)
t.left(90)
t.forward(100)

# T
move(-80, 100)
t.right(90)
t.forward(60)
t.backward(30)
t.right(90)
t.forward(100)

t.left(90)

# E
move(0, 100)
t.forward(50)
t.backward(50)
t.right(90)
t.forward(50)
t.left(90)
t.forward(40)
t.backward(40)
t.right(90)
t.forward(50)
t.left(90)
t.forward(50)

# E (second)
move(80, 100)
t.forward(50)
t.backward(50)
t.right(90)
t.forward(50)
t.left(90)
t.forward(40)
t.backward(40)
t.right(90)
t.forward(50)
t.left(90)
t.forward(50)

turtle.done()