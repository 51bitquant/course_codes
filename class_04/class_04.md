# 如何debug Python程序

## 常见的错误
1 中英文混乱 SyntaxError: invalid character in identifier
``` python
print("Hello world")
print（'hello world'）

#  File "<stdin>", line 1
#     print（'hello world'）
#          ^
# SyntaxError: invalid character in identifier


```

2. 缩进不正确 

``` python

def hello():
 print('hello world')
  print('hello world')
  
# IndentationError: unexpected indent

```

3. 函数参数个不对，或者参数传递有误

``` python
def func(a,b, c=10):
    print(a,b, c)


func(1,c=5)

```

4. 网络问题 类似 connection, 怎么看呢？

解决问题: 把报错的信息复制到百度，然后搜索，或者先翻译然后再搜索.

5. 如何定位问题的代码出现在哪里? 通过TraceStack进行查找，函数调用栈的问题.


Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'requests'


