# 第十九课: 合约网格交易策略

策略代码在: 
https://github.com/51bitquant/howtrader/blob/main/howtrader/app/cta_strategy/strategies/future_profit_grid_strategy.py

主要是根据高频网格进行改进,
在双边进行挂单，会有止盈止损的功能。合约主要是手续费低，可以放大杠杆，
提高资金利用率。但是要考虑止盈止损的情况。
如果设置的太小。容易发生止损，设置的过大，容易发生单次亏损过大。建议在震荡行情中使用。
或者在波动比较小的时候使用。可以通过计算AT的值，在ATR变化平稳或者计算历史波动率比较低时候使用。
或者可以类似现货那种跑，但是你不要加杠杆。

之前测试过，在震荡行情有单天10%的收益，杠杆3倍杠杆，但是如果发生趋势亏损会比较严重。建议使用前测试。如果是趋势行情，谨慎使用。同时记得止损。

    免责声明: 本策略仅供研究学习，本人不负有任何责任。使用前请熟悉代码。
    测试其中的代码, 请清楚里面的功能后再使用。
    投资有风险入市需谨慎。
    币安邀请链接: https://www.binancezh.pro/cn/futures/ref/51bitquant
    合约邀请码：51bitquant

## 课程要求


### 1. 学过前面的课时

1. 不要跳着看，很多知识点我讲了，你不看就不知道。跟着课程来学习，进步最快。
2. 最好结合课程《Python数字货币量化交易进阶课程》的网格部分来学习。
3. 课程代码下载地址: https://github.com/51bitquant/course_codes
4. 框架代码: https://github.com/51bitquant/howtrader

### 2. 更新软件

> pip install git+https://github.com/51bitquant/howtrader.git -U

更新到当前的最新版本: 2.1.8.0 版本 


### 3. 能访问交易所或者购买一个服务器

1. 如果需要在服务器上部署，可以通过一下链接购买服务器:
   **https://www.ucloud.cn/site/global.html?invitation_code=C1x2EA81CD79B8C#dongjing**
   
  价格非常便宜，一年也就是500块钱左右。可以根据个人的需求来选择不同价位的服务器。


