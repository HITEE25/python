import turtle

t = turtle.Turtle()
t.speed(5)
t.color("green")

t.left(-45)
t.begin_fill()
#to give tilt effect of leaf
t.left(45)
#create circle with radius 100 and 90 => 1/4 of circle created
t.circle(100,90)

#move to opposite direction
t.left(90)
t.circle(100,90)

t.end_fill()

turtle.done()