import turtle 
import random
t = turtle.Turtle()
turtle.bgcolor('navy')
turtle.tracer(2)
t.hideturtle()
t.color('white')
moon=turtle.Turtle('circle')
moon.shapesize(10)
moon.up()
moon.color('gold')
moon.goto(-400,400)
for j in range (50):
  x=random.randint(-400,400)
  y=random.randint(-400,400)
  t.up()
  t.goto(x,y)
  t.down()
  t.begin_fill()
  for i in range(5):
    
      t.forward(20)
      t.left(144)
  t.end_fill()  

