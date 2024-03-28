import turtle
import random
import winsound

score = 0
op = input("select the color(in inglish please): ")

trt = turtle.Screen()
trt.title("simple game created by @luis miguel brancalion")
trt.bgcolor(op)
trt.setup(width=500,height=500)
trt.tracer(0)

#the character
chara = turtle.Turtle()
chara.speed(0)
chara.penup()
chara.shape("square")
chara.shapesize(stretch_wid=1,stretch_len=1)
chara.color("red")
chara.fillcolor("yellow")
chara.goto(0,0)

chara1 = turtle.Turtle()
chara1.speed(0)
chara1.shape("square")
chara1.shapesize(stretch_wid=1,stretch_len=1)
chara1.color("blue")
chara1.penup()
chara1.goto(0,180)

#define some functions
def up():
 winsound.Beep(1000,100) 
 a = chara.ycor()
 a += 30
 chara.sety(a)

def down():
 winsound.Beep(1000,100) 
 b = chara.ycor()
 b -= 30
 chara.sety(b)

def left():
 winsound.Beep(1000,100) 
 c = chara.xcor()
 c -= 30
 chara.setx(c) 

def right():
 winsound.Beep(1000,100) 
 d = chara.xcor()
 d += 30
 chara.setx(d)


#define keyboard functios
trt.listen()
trt.onkeypress(up,"w")
trt.onkeypress(down,"s")
trt.onkeypress(right,"d")
trt.onkeypress(left,"a")



while True:
 

 trt.update()
 x = random.choice([-180,-150,-120,-90,-60,-30,0,30,60,90,120,150,180])
 y = random.choice([-180,-150,-120,-90,-60,-30,0,30,60,90,120,150,180])
 a = chara.ycor()
 b = chara.xcor()

 if chara.ycor() > 245:
  chara.sety(245 - 425)
  chara.setx(b)
 elif chara.ycor() < -245:
  chara.sety(a + 425)
  chara.setx(b)

 elif chara.xcor() > 245:
  chara.sety(a)
  chara.setx(245 - 425)

 elif chara.xcor() < -245:
  chara.sety(a)
  chara.setx(-245 + 425)

 if chara.xcor()  + chara.ycor() == chara1.xcor() + chara1.ycor():
  winsound.PlaySound("bounce.wav",winsound.SND_ASYNC) 
  score+=1
  chara1.goto(x,y)

 