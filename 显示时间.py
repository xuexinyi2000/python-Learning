import turtle as t
import datetime

#每一段之间的间隔
def Gap():
    t.up()
    t.fd(5)

#每一段的亮 or 暗
def Line(draw):
    Gap()
    
    if(draw):
        t.down()
    else:
        t.up()

    t.fd(20)
    Gap()
    t.right(90)

#绘制数字(先后顺序为g-c-d-e/f-a-b)
def Dight(i):
    #g
    if i in [2,3,4,5,6,8,9]:
        Line(True)
    else:
        Line(False)
    #c
    if i in [0,1,3,4,5,6,7,8,9]:
        Line(True)
    else:
        Line(False)

    #d
    if i in [0,2,3,5,6,8]:
        Line(True)
    else:
        Line(False)

    #e
    if i in [0,2,6,8]:
        Line(True)
    else:
        Line(False)

    #不改变方向，往回转90度
    t.left(90)

    #f
    if i in [0,4,5,6,8,9]:
        Line(True)
    else:
        Line(False)

    #a
    if i in [0,2,3,5,6,7,8,9]:
        Line(True)
    else:
        Line(False)

    #b
    if i in [0,1,2,3,4,7,8,9]:
        Line(True)
    else:
        Line(False)

    #箭头恢复初始方向
    t.right(180)
    t.penup()
    t.fd(20)

#绘制日期
def Date(time):
    t.pencolor("yellow")
    for i in time:
        if i == '-':
            t.write('年')
            t.fd(38)
            t.pencolor('green')
        elif i == '+':
            t.write('月')
            t.fd(38)
            t.pencolor('blue')
        elif i == '=':
            t.write('日')
            t.fd(38)
            t.pencolor('purple')
        elif i == ':':
            t.write('时')
            t.fd(38)
        elif i == '|':
            t.write('分')
            t.fd(38)
        elif i == ']':
            t.write('秒')
            t.fd(38)
        else:
            Dight(eval(i))

def main():
    t.setup(950,350,200,200)
    t.hideturtle()
    t.speed(100)
    t.pensize(5)
    t.penup()
    t.fd(-450)
    Date(datetime.datetime.now().strftime('%Y-%m+%d=%H:%M|%S]'))#格式化时间

main()
    
