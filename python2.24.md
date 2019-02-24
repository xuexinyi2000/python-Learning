### python语法元素

注释

* 单行注释以`#`开头
* 多行注释以`'''`开头和结尾

###### 输入

<变量> = input(<提示性文字>)

###### 输出

* print("<输出内容>")
* 格式化
  * print("%  "%f)
  * str.format()通过`{}`和`:`代替了`%`

###### 循环

* 计数循环语句

  for i in range (<计数值>)：
  	<表达式组>

###### 赋值语句

同步赋值语句 t=x;x=y;y=t  ==  x,y=y,x

### 蟒蛇绘制程序分析

```python
import turtle#

def drawSnake(rad,angle,len,neckrad):
    for i in range(len):
        turtle.circle(rad,angle)#rad（左正右负）描述圆形轨迹半径的位置，angle表示小乌龟沿着圆形爬行的弧度值
        turtle.circle(-rad,angle)
    turtle.circle(rad, angle/2)
    turtle.fd(rad)#==turtle.forward()表示乌龟向前直线爬行，参数表示爬行的距离
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*2/3)

def main():
    turtle.setup(1300,800,0,0)#启动了图形窗口（宽度，高度，（0，0）在电脑窗口的坐标位置 ）
    pythonsize = 30
    turtle.pensize(pythonsize)#笔触的宽度，这里设为30个像素
    turtle.pencolor("blue")#笔触颜色,颜色采用RGB，("#3B9909")
    turtle.seth(-40)#小乌龟运行的方向，角度值，0度（右），90度（上），180度（左），270度（下）
    drawSnake(40,80,5,pythonsize/2)#调用自定义函数drawSnake

main()#程序运行main()函数
```

自己尝试了画一个`P`

```python
import turtle

def main():
    turtle.setup(500,500,0,0)
    turtle.pensize(10)
    turtle.pencolor("blue")
    turtle.seth(90)
    turtle.fd(90)
    turtle.circle(-15,180)
    turtle.fd(5)
    turtle.circle(-15,180)

main()
```

### 函数库的引用

* import <库名>

* from <库名> import <函数名>

  from <库名> import  (引用此函数库时无需加库名)