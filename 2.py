import turtle
import time
import winsound
#start the screen
trt = turtle.Screen()
trt.title("simple game")
trt.bgcolor("black")
trt.setup(width=600,height=600)
trt.tracer(0)

#create the ball
person1 = turtle.Turtle()
person1.speed(0)
person1.shape("square")
person1.shapesize(stretch_wid=1,stretch_len=1)
person1.color("white")
person1.penup()
person1.goto(0,0)

#create the bar
person0 = turtle.Turtle()
person0.speed(0)
person0.shape("square")
person0.shapesize(stretch_wid=1,stretch_len=3)
person0.color("white")
person0.penup()
person0.goto(0,-280)

#functions of functions of the keyboard
def right():
 a = person0.xcor()
 a +=30
 person0.setx(a)
def left():
  b = person0.xcor()
  b -=30
  person0.setx(b)

#functions of the keyboard
trt.listen()
trt.onkeypress(right,"d")
trt.onkeypress(left,"a")

while True:
 trt.update()
 time.sleep(0.3)
 c = person1.ycor() - 30
 person1.sety(c) 
 winsound.PlaySound("bounce.wav",winsound.SND_ASYNC) 
