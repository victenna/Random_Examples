#Firework
import	turtle
import random
wn=turtle.Screen()
turtle.tracer(2,5)
t=turtle.Turtle()
turtle.bgcolor('black')
turtle.colormode(255)
t.goto(0,-400)
t.shapesize(1)
t.pensize(2)
t.hideturtle()
q=['red','blue','yellow','green','white','gray','violet','pink']

t1=turtle.Turtle()
t1.up()
t1.hideturtle()
t1.color('red')
t1.goto(-150,300)
t1.write('Firework', font=("Arial",20,'bold'))
t1.goto(-300,250)
t1.color('white')
t1.write('click on any point of the the screen', font=("Arial",20,'bold'))

def motion(delta,angle,clr):
    t.fd(delta)
    t.back(delta)
    t.rt(angle)
    t.color(clr)

def firework(x,y):
    t.up()
    #t.clear()
    t.goto(x,y)
    t.down()
    for i in range (20):
        t.penup()
        a=random.randint(0,255)
        b=random.randint(0,255)
        c=random.randint(0,255)
        t.pencolor(a,b,c)
        u=random.randint(50,350)
        t.setheading(90)
        d=random.randint(100,600)
        t.fd(d)
        t.pendown()
        t.color(random.choice(q))
        if i%2==0:
            t.circle(-u,150)
        if i%2>0:
            t.circle(u,150)
        t.setheading(-90)
        t.pensize(1)
        motion(50,45,'red')
        motion(50,-45,'blue')
        motion(50,-45,'yellow')
        motion(50,-22.5,'green')
        motion(50,130,'gold')
        t.penup()
        t.pensize(2)
        t.goto(x,y)
wn.onclick(firework)
