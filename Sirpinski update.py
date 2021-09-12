import turtle
import random

turtle.screensize(300,300)
turtle.hideturtle()

p1 = (random.uniform(-150,150), random.uniform(-150,150))
p2 = (random.uniform(-150,150), random.uniform(-150,150))
p3 = (random.uniform(-150,150), random.uniform(-150,150))
#random.uniform tager et tilfældig nummer til og med de indtastede numrer og får kordinaterne til trekantens 3 punkter
turtle.penup()

t = [p1,p2,p3]
for F in t: #i listen t, bliver alle punkterne tegnet
    turtle.goto(F)
    turtle.dot()
print(p1,p2,p3)
t2 = random.choice(t)
print(t2)
turtle.goto(t2)
turtle.dot()



turtle.done()

