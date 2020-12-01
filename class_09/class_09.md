# 第九课: 第二章总结--数据准备和学习要求


## 1. 软件要求
通过pip install的方式进行安装
> pip install git+https://github.com/ramoslin02/howtrader.git

更新到最新, 后面加上-U表示更新到最新的
> pip install git+https://github.com/ramoslin02/howtrader.git -U 


## 1. 数据爬取
1. 数据库: 为了方便学习，降低学习成本，用sqlite数据库，不用任何配置
2. 用crawl_data爬取BTCUSDT, ETHUSDT, BNBUSDT等现货和合约的数据,
   如果没有数据后面课程没法学习。
3. okex和火币没有提供历史数据，他们最多提供2000个K线的数据，学习和研究非常不方便，除非自己购买第三方数据。


## 2. 把UI界面和行情跑起来

1. 注册币安账号
没有开通币安或者交易所的可以通过下面链接去开通，有手续费减免:
**https://www.binancezh.pro/cn/futures/ref/51bitquant**
合约邀请码：**51bitquant**

2. 配置API: 生成api地址:
   https://www.binancezh.pro/cn/usercenter/settings/api-management

3. 启动界面 
> python main.py

## 注意事项
如何确定自己电脑的网络是否能访问币安交易所呢？

在终端输入
> ping api.binance.com 

如果能访问就不用配置代理，如果不能访问就需要配置代理主机和代理端口

