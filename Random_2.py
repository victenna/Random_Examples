#Random Color Lines
import turtle
wn=turtle.Screen()
wn.bgcolor('darkorange')
import time
import random
t=turtle.Turtle('turtle')
clr=['red','navy', 'green','yellow','gray','violet','pink','black','purple',\
     'light blue','orange','brown','coral','white','gold','fuchsia','beige']
t.speed(5)
while True:
    a=random.randint(-100,100)
    b=random.randint(-200,200)
    c=random.randint(0,180)
    t.color(random.choice(clr))
    t.penup()
    t.hideturtle()
    t.goto(a,b)
    t.setheading(0)
    t.showturtle()
    t.turtlesize(0.5,25)
    t.left(c)
    t.stamp()
