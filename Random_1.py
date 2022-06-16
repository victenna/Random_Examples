#Random Spirals
import turtle
import random
import time
wn=turtle.Screen()
wn.bgcolor('light blue')
t=turtle.Turtle('turtle')
turtle.tracer(5)
t.hideturtle()
t.pensize(2)
def draw(X,Y):
    for i in range(18):
        t.up()
        t.goto(X,Y)
        t.setheading(20*i)
        t.down()
        t.circle(-20,180)
        t.up()
   
clr=['red','blue','gold','violet','pink'\
     ,'orange','brown','coral','purple','magenta']

m=-1     
while True:
    m=m+1
    m1=m%2
    if m1==0:
        wn.bgcolor('blue')
    else:
        wn.bgcolor('red')
    t.color(random.choice(clr))
    a=random.randint(-300,300)
    b=random.randint(-300,300)
    draw(a,b)
