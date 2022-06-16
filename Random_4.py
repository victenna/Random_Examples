#Evaluation of pi number, random method
import turtle
import random
t=turtle.Turtle()
t.hideturtle()
wn=turtle.Screen()
wn.tracer(2,5)
turtle.colormode(255)
t.pensize(5)
t.penup()
R=100
t.goto(-100,-100)
for i in range (4):
    t.color('red')
    t.pendown()
    t.fd(200)
    t.left(90)
t.penup()
t.goto(0,-100)
t.pendown()
t.color('blue')
t.circle(100)
t.color('green')
t.penup()
t.pensize(1)

sum0=0
sum=0
for n in range(10000):
    print(n)
    sum0=sum0+1
    a=random.randint(-100,100)
    b=random.randint(-100,100)
    L=t.distance(a,b)
    t.penup()
    t.setposition(a,b)
    if L<R:
        t.color('yellow')
    if L>=R:
        t.color('green')
    t.pendown()
    t.dot()
    t.penup()
    t.home()
    if L<R:
        sum=sum+1
    t.penup()
t1=turtle.Turtle()
t1.up()
t1.goto(-40,120)
t1.down()
t1.write('pi=',font=('Times New Roman', 30,'bold'))
t1.up()
t1.hideturtle()
t1.goto(20,120)
t1.write(4*sum/sum0,font=('Times New Roman', 30,'bold'))

print(4*sum/sum0)
