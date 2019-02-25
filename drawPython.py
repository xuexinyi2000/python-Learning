#画python图标

from turtle import *

def drawP():
    penup()
    setpos(-200,0)
    pendown()
    pensize(10)
    pencolor("blue")
    seth(90)
    fd(90)
    circle(-15,180)
    fd(5)
    circle(-15,180)

def drawY():
    penup()
    setpos(-150,95)
    pendown()
    pensize(10)
    pencolor("yellow")
    seth(-90)
    fd(20)
    circle(15,180)
    fd(20)
    seth(-90)
    fd(75)
    circle(-15,180)
    
def drawT():
    penup()
    setpos(-75,95)
    pendown()
    pensize(10)
    pencolor("yellow")
    seth(270)
    fd(75)
    circle(15,180)
    penup()
    setpos(-45,75)
    pendown()
    seth(180)
    fd(60)

def drawH():
    penup()
    setpos(-20,100)
    pendown()
    seth(-90)
    fd(100)
    seth(90)
    fd(35)
    circle(-20,180)
    fd(35)

def drawO():
    penup()
    setpos(40,40)
    pendown()
    fd(20)
    circle(20,180)
    fd(20)
    circle(20,180)

def drawN():
    penup()
    setpos(100,55)
    pendown()
    fd(55)
    seth(90)
    fd(35)
    circle(-20,180)
    fd(35)

def drawSnake(rad,angle,len,neckrad):
    penup()
    setpos(-150,-30)
    pendown()
    seth(-40)
    pencolor("blue")
    for i in range(len):
        circle(rad,angle)
        circle(-rad,angle)
    circle(rad, angle/2)
    fd(rad)
    circle(neckrad+1,180)
    fd(rad*2/3)

def main():
    setup(500,500,100,100)
    drawP()
    drawY()
    drawT()
    drawH()
    drawO()
    drawN()
    drawSnake(40,80,3,15)
    
main()
