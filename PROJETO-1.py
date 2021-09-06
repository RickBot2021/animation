import turtle as t
import random as r
t.speed(0)
sc=t.Screen()
sc.bgcolor("black")
t.up()
t.goto(-500,150)
t.down()
t.begin_fill()
t.color("blue")
t.circle(120)
t.end_fill()

t.up()
t.goto(-450,200)
t.down()
t.begin_fill()
t.color("black")
t.circle(120)
t.end_fill()

for i in range(100) :
    l=r.randint(5,12)
    x=r.randint(-650,650)
    y=r.randint(-350,350)
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    for i in range (5):
        t.color("blue")
        t.fd(l)
        t.left(144)
    t.end_fill()