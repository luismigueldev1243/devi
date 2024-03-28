import turtle
import random
import time
score = 0
trt = turtle.Screen()
trt.title("simple game creted by @ luis miguel maran . 22/03/24")
trt.bgcolor("black")
trt.setup(width=500,height=600)
trt.tracer(0)
#the character
chara = turtle.Turtle()
chara.speed(0)
chara.penup()
chara.shape("square")
chara.shapesize(stretch_wid=1,stretch_len=3)
chara.color("red")
chara.goto(0,-240)
#the ball
ball = turtle.Turtle()
ball.speed(0)
ball.penup()
ball.shape("square")
ball.shapesize(stretch_wid=1,stretch_len=1)
ball.color("yellow")
ball.goto(0,240)
def left():
 c = chara.xcor()
 c -= 30
 chara.setx(c) 
def right():
 d = chara.xcor()
 d += 30
 chara.setx(d)
#define keyboard functios
trt.listen()
trt.onkeypress(right,"d")
trt.onkeypress(left,"a")
while True:
 trt.update()
 x1 = random.choice([240,225,180,150,165,120,105,90,60,45,30,0,-240,-225,-180,-150,-165,-120,-105,-90,-60,-45,-30])
 if chara.xcor() > 245:
  chara.setx(245 - 425)
 elif chara.xcor() < -245:
  chara.setx(-245 + 425)
 time.sleep(0.2)
 y = ball.ycor()  
 y -=15
 ball.sety(y)
 if ball.ycor()+ ball.xcor() == chara.xcor()+chara.ycor():
  score +=1
  ball.setx(x1)
  ball.sety(-30)
 elif ball.ycor() < -250:
  trt.clearscreen()
  trt.bgcolor("black")
  chara2 = turtle.Turtle()
  chara2.speed(0)
  chara2.penup()
  chara2.color("red")
  chara2.goto(0,0)
  chara2.write(f"you lost :( , you scored {score} points")
 if score == 20:
  trt.clearscreen()
  trt.bgcolor("black")
  chara2 = turtle.Turtle()
  chara2.speed(0)
  chara2.penup()
  chara2.color("red")
  chara2.goto(0,0)
  chara2.write("congratulatios , you scored 50 times")