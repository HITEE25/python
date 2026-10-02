import turtle

t = turtle.Turtle()
t.speed(3)

# ---------------- BIG SQUARE ----------------
t.penup()
t.goto(-100, -200)
t.pendown()

for i in range(4):
    t.forward(200)
    t.left(90)

# ---------------- VERTICAL LINE ----------------
t.penup()
t.goto(0, 0)
t.pendown()
t.goto(0, 100)

# ---------------- SMALL SQUARE ----------------
t.penup()
t.goto(0, 100)
t.pendown()

for i in range(4):
    t.forward(100)
    t.left(90)

# ---------------- DIAGONAL (small square) ----------------
t.penup()
t.goto(0, 200)
t.pendown()
t.goto(100, 100)

# ---------------- DIAGONAL (middle) ----------------
t.penup()
t.goto(0, 100)
t.pendown()
t.goto(100, 0)

# ---------------- LEFT PARALLEL LINES ----------------
t.penup()
t.goto(-150, 150)
t.pendown()
t.goto(0, 0)

t.penup()
t.goto(-150, 50)
t.pendown()
t.goto(0, -100)

turtle.done()