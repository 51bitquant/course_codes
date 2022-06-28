# 第十七课: 现货网格交易策略讲解和实盘部署(2)

讲两种不同方式的实现方式和思路。一种是简单的，直接挂单买卖的，另一个重是有止盈和止损方式的。

## 课程要求


### 1. 学过前面的课时

1. 不要跳着看，很多知识点我讲了，你不看就不知道。跟着课程来学习，进步最快。
2. 最好结合课程《Python数字货币量化交易进阶课程》的网格部分来学习。
3. 课程代码下载地址: https://github.com/51bitquant/course_codes
4. 框架代码: https://github.com/51bitquant/howtrader

### 2. 更新软件

> pip install git+https://github.com/51bitquant/howtrader -U

更新到当前的最新版本: 2.1.8.0 版本 


### 3. 能访问交易所或者购买一个服务器

1. 如果需要在服务器上部署，可以通过一下链接购买服务器:
   **https://www.ucloud.cn/site/global.html?invitation_code=C1x2EA81CD79B8C#dongjing**
   
  价格非常便宜，一年也就是500块钱左右。可以根据个人的需求来选择不同价位的服务器。


### 止盈网格的思路


计算网格的平均价格

假设ETH当前的价格是730, 然后你在730, 728, 726,买了三个， 然后价格回到728,  
你卖了一个，然后此时你的仓位数量数2个ETH, 那么你的均价是多少? # (730 + 728)/2 =
729


```python
from decimal import Decimal
from howtrader.trader.object import  OrderData, Status, Direction

class GridPositionCalculator(object):
    """
    用来计算网格头寸的平均价格
    Use for calculating the grid position's average price.
    :param grid_step: 网格间隙.
    """

    def __init__(self, grid_step: float = 1.0):
        self.pos: Decimal = Decimal("0")
        self.avg_price: Decimal = Decimal("0")
        self.grid_step: Decimal = Decimal(str(grid_step))

    def update_position(self, order: OrderData):
        if order.status != Status.ALLTRADED:
            return

        previous_pos = self.pos
        previous_avg = self.avg_price

        if order.direction == Direction.LONG:
            self.pos += order.volume

            if self.pos == Decimal("0"):
                self.avg_price = Decimal("0")
            else:

                if previous_pos == Decimal("0"):
                    self.avg_price = order.price

                elif previous_pos > 0:
                    self.avg_price = (previous_pos * previous_avg + order.volume * order.price) / abs(self.pos)

                elif previous_pos < 0 and self.pos < 0:
                    self.avg_price = (previous_avg * abs(self.pos) - (
                            order.price - previous_avg) * order.volume - order.volume * self.grid_step) / abs(
                        self.pos)

                elif previous_pos < 0 < self.pos:
                    self.avg_price = order.price

        elif order.direction == Direction.SHORT:
            self.pos -= order.volume

            if self.pos == Decimal("0"):
                self.avg_price = Decimal("0")
            else:

                if previous_pos == Decimal("0"):
                    self.avg_price = order.price

                elif previous_pos < 0:
                    self.avg_price = (abs(previous_pos) * previous_avg + order.volume * order.price) / abs(self.pos)

                elif previous_pos > 0 and self.pos > 0:
                    self.avg_price = (previous_avg * self.pos - (
                            order.price - previous_avg) * order.volume + order.volume * self.grid_step) / abs(
                        self.pos)

                elif previous_pos > 0 > self.pos:
                    self.avg_price = order.price

```
