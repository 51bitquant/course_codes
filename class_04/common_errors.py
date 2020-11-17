
# error1: 找不模块, 解决方法: pip install <包的名称>, 如： pip install ccxt
# import tensortrade ModuleNotFoundError: No module named 'tensortrade'
# 或者通过requirements.txt 文件, 执行命令: pip install -r requirements.txt
# 如果有的库安装库，或者错误，可以通过 pip install <库名称> 来装指定的库。
# print("hello world")

# import ccxt
# print("hello world")


# error 2: 语法错误

# 中英文字符混合的
# print（'Helloworld'）
print('hello world')

# SyntaxError: Missing parentheses in call to 'print'. Did you mean print(a)?
# a  = 10
# print(a)

# def hello:  # 定义函数错误
#     print(100)

# def hello1():
#     print(100)

# class Hello:
#     pass

# class Person(object):
#     def hello(self):
#         pass

# class Human:
#     def hell(self):
#         pass


# error 3: NameError: name 'a' is not defined, 变量没有定义, 解决查看变量有没有定义
# 局部不定义，看下全局有没有定义.
# print(a)


# a = 11
# print("hello world1")
# def print_data():
#     print(a)
#
# if __name__ == '__main__':
#     print("hello world2")
#     a = 10
#     print_data()


# error 4: 缩进错误 IndentationError: expected an indented block

# for i in [1,3,4]:
# print(i)


# error 5: 属性错误 AttributeError: 'Student' object has no attribute 'num'
# class Student(object):
#     def __init__(self, name, age):
#         self.age = age
#         self.name = name
# #
# stu1 = Student('Mary', 10)
# print(stu1.age)
# print(stu1.name)
# print(stu1.num)
# print(dir(stu1))  # 查看属性
# print(stu1.__dict__)  # 属性和值
# print(stu1.__class__)

# error 6: Type Error类型错误 TypeError: unsupported operand type(s) for /: 'str' and 'int'
# a = 'I love China'
# print(a/5)
# print(a*5)

## error7 数组越界 IndexError: list index out of range

# a = [1,3,4]
# print(a[4])

## error 8 函数参数传递错误 TypeError: fun1() missing 1 required positional argument: 'b'

# def fun1(a, b,  c=10):
#     print(a,b,c)

# fun1(1,10,20)

## Key error KeyError: 'b', 常常出现在dict 和pandas 中

# a = {"hello": "world"}
# print(a['b'])

import pandas as pd
# a = {'a': [1,3,4], 'b': [567]}  # 这也是一个错误
# df = pd.DataFrame(a)


# a = {'a': [1,3,4], 'b': [5,6,7]}
# df = pd.DataFrame(a)
# print(df['c'])


## json解析错误: raise JSONDecodeError("Expecting value", s, err.value) from None
# json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

import requests

# {"key": "value}
# [1,b,c, {}]
# a = requests.get("https://api.binance.com/exchangeinfo").json()
# a = requests.get("https://api.binance.com/exchangeinfo")
# print(a.text)

# import json
#
# a = None
#
# json.loads(a)

## 网络错误
"""
raise ConnectTimeout(e, request=request)
requests.exceptions.ConnectTimeout: HTTPSConnectionPool(host='api.binance.com', port=443):
 Max retries exceeded with url: /api/v3/ping 
 (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x7ff29ff98310>, 
 'Connection to api.binance.com timed out. (connect timeout=5)'))
"""

# 通过ping 测试下: ping api.binance.com
# a = requests.get('https://api.binance.com/api/v3/ping', timeout=5).json()
# print(a)
# try:
#     a = requests.get('https://api.binance.com/api/v3/ping', timeout=5).json()
#     print(a)
#
# except Exception as error:
#     print(error)


# ZeroDivisionError: division by zero, 查看函数的调用过程. Traceback
def afunc(a):
    print(a)

    return 20/a

def bfunc(a,b):
    d = a-b
    return afunc(d)


# value = bfunc(20,10)
value = bfunc(20,20)
# value = bfunc(20,'hello')
# print(value)

## 百度搜索
# 关键字 inurl: 搜索某个网站的网址
# 量化 inurl:www.jianshu.com
# 51bitquant blog

# 搜索字 blog 指明搜索博客类的
# "indent error" blog

# error , exception , Raise