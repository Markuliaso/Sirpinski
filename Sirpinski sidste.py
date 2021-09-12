import turtle
import random
i = 0
turtle.hideturtle()
turtle.speed(0)
x1 =(random.randint(-300,300))
y1 =(random.randint(-300,300))
x =(x1,y1)

x2 =(random.randint(-300,300))
y2 =(random.randint(-300,300))
y =(x2,y2)

x3 =(random.randint(-300,300))
y3 =(random.randint(-300,300))
z =(x3,y3)

turtle.penup()

t = [x,y,z]
for F in t: #i listen t, bliver alle punkterne tegnet
    turtle.goto(F)
    turtle.dot()

x4 = (random.randint(-300,300))
y4 = (random.randint(-300,300))
S = (x4,y4)
turtle.goto(S)
turtle.dot()

while i < 1:
    penis = random.choice(t)

    if (penis == x):
        x4 = ((x4 + x1) /2)
        y4 = ((y4 + y1) /2)

    elif (penis == y):
        x4 = ((x4 + x2) /2)
        y4 = ((y4 + y2) /2)

    elif (penis == z):
        x4 = ((x4 + x3) /2)
        y4 = ((y4 + y3) /2)
    S =(x4,y4)
    turtle.goto(S)
    turtle.dot()
