import turtle
import random

s = turtle.getscreen()
turtle.hideturtle()


p1 = (random.uniform(0,300), random.uniform(0,300))
p2 = (random.uniform(0,300), random.uniform(0,300))
p3 = (random.uniform(0,300), random.uniform(0,300))

t = [p1,p2,p3]
for F in t:
    turtle.goto(F)
    turtle.dot()
print(p1,p2,p3)


turtle.done()

