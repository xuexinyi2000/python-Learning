#### $\Pi$的计算（蒙特卡洛法）

```python
#蒙特卡洛
from random import random
from math import sqrt
import time
#在Python3.3以上的版本，time库里面没有clock()函数，用time.perf_counter()代替

all = 12000
hits = 0
t = time.perf_counter()
#模拟抛洒点的过程
for i in range(1,all):
    x = random()
    y = random()
    dist = sqrt(x**2 + y**2)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits / all)

print("pi的值是%s"%pi)
print("程序运行的时间是%-5.5ss"%t)
```



#### eval()函数

`eval(expression[,globals[,locals]])`

###### 例子

```python
>>> eval(val[0:-1])
30
>>> t = eval(val[0:-1])
>>> type(t)
<class 'int'>
```

#### format()函数

##### 字符串格式化

<模板字符串>.format(用逗号分割的参数)

##### 格式控制信息

* <对齐> `<` 左对齐`>`右对齐 `^`居中对齐

```python
>>> "{0:>30}".format(a)
'                           hhh'
>>> "{0:<30}".format(a)
'hhh                           '
>>> "{0:^30}".format(a)
'             hhh              '
```

*  `,`数字千位分隔符

```python
>>> "{0:-^20,}".format(123456789)
'----123,456,789-----'
>>> "{0:*^20}".format(123456789)
'*****123456789******'
```

* <精度>

```
>>> "{0:.2f}".format(12345.67890)
'12345.68'
>>> "{0:.4}".format("python")
'pyth'
```

* <类型>
  * b:二进制
  * c:Unicode
  * d:十进制
  * o:八进制
  * x:小写十六进制
  * X:大写16进制

```python
>>> "{0:b},{0:c},{0:d},{0:o},{0:x},{0:X}".format(425)
'110101001,Ʃ,425,651,1a9,1A9'
```



#### 异常处理

```python
try:
	<body>
except <ErrorType1>:
	<handler1>
except <ErrorType2>:
	<handler2>
except:
	<handler0>
```

```python
try:
	<body>
except <ErrorType1>:
	<handler1>
except <ErrorType2>:
	<handler2>
except:
	<handler0>
else:
	<process_else>
finally:
	<process_finally>
```



#### 树的画法(递归)

```python
from turtle import Turtle

def tree(plist,l,a,f):
    if l > 5:
        lst = []
        for p in plist:
            p.forward(l)
            q = p.clone()
            p.left(a)
            q.right(a)
            lst.append(p)
            lst.append(q)
        tree(lst,l*f,a,f)

def main():
    p = Turtle()
    p.color("green")
    p.pensize(5)
    p.hideturtle()
    p.left(90)

    p.penup()
    p.goto(0,0)
    p.pendown()

    t = tree([p],110,65,0.6375)

main()
```

