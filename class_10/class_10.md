# 第十课: 认识VNPY CTA策略模板

## 要求
1. 更新软件到最新的版本, 截止目前最新版本为V2.1.7.6，不然可能会有问题

2. 更新方法: 在终端输入一下命令: 

> pip install git+https://github.com/51bitquant/howtrader.git -U

或者先卸载然后再安装
> pip uninstall howtrader 

> pip install git+https://github.com/51bitquant/howtrader.git
   
3. 课程代码和课件下载地址: https://github.com/51bitquant/course_codes

## 系统的内置的策略
在框架howtrader.app.cta_strategy.strategies目录下

## 写一个简单的策略
1. 在项目的启动文件夹下面创建一个叫strategies文件夹
2. 拷贝系统内置的策略，一份然后修改里面的方法


## 策略启动的步骤
1. 连接交易所
2. 添加策略(添加策略可以通过 cta_engine.add_strategy())
3. 启动策略
