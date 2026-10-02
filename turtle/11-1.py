import turtle
t = turtle.Turtle()
t.speed(5)
#spefic size
size = 200
#5 square
for i in range(5):
    #for square repeat steps 4 times
    for j in range(4):
        t.forward(size)
        t.left(90)

    #move turtle inside
    t.penup()
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.right(90)
    t.pendown()
    #decrease the size for inside square
    size -= 20

#to draw triangle in inside
t.penup()
t.goto(50,50)
t.pendown()

#for triagle repeat 3 times
for i in range(3):
    t.forward(100)
    t.left(120)

turtle.done()

