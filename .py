import turtle
import time

trt = turtle.Screen()
trt.title("test")
trt .bgcolor("black")
trt.setup(width=600,height=400)
trt.tracer(0)
#person
person0 = turtle.Turtle()
person0.speed(0)
person0.shape("turtle")
person0.shapesize(stretch_wid=1,stretch_len=1)
person0.color("white")
person0.penup()
person0.goto(-290,50)


#the cactus
person1 = turtle.Turtle()
person1.speed(0)
person1.shape("square")
person1.shapesize(stretch_wid=2,stretch_len=1)
person1.color("white")
person1.penup()
person1.goto(260,50)

person2 = turtle.Turtle()
person2.speed(0)
person2.shape("square")
person2.shapesize(stretch_wid=2,stretch_len=1)
person2.color("white")
person2.penup()
person2.goto(150,50)

person3 = turtle.Turtle()
person3.speed(0)
person3.shape("square")
person3.shapesize(stretch_wid=2,stretch_len=1)
person3.color("white")
person3.penup()
person3.goto(20,50)

person4 = turtle.Turtle()
person4.speed(0)
person4.shape("square")
person4.shapesize(stretch_wid=2,stretch_len=1)
person4.color("white")
person4.penup()
person4.goto(-100,50)

person5 = turtle.Turtle()
person5.speed(0)
person5.shape("square")
person5.shapesize(stretch_wid=2,stretch_len=1)
person5.color("white")
person5.penup()
person5.goto(-250,50)


while True:
 trt.update()
 time.sleep(1)
 a = person1.xcor() 
 a -= 30
 person1.setx(a)
 if a == -300:
  a = 300

 b = person2.xcor() 
 b -= 30
 person2.setx(b)

 c = person3.xcor() 
 c -= 30
 person3.setx(c)

 d = person4.xcor() 
 d -= 30
 person4.setx(d)

 e = person5.xcor() 
 e -= 30
 person5.setx(e)
 

