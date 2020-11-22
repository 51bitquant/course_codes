# 第七课：VNPY的常见类的介绍和python类型编程

## 导入类的方式

```python

from howtrader.A模块.文件 import 具体的某个类
from howtrader.trader.object import Status  # 订单状态
from howtrader.trader.object import OrderType
from howtrader.trader.object import Exchange, Interval

""" 
实践的类型

EVENT_TICK = "eTick."
EVENT_TRADE = "eTrade."
EVENT_ORDER = "eOrder."
EVENT_POSITION = "ePosition."
EVENT_ACCOUNT = "eAccount."
EVENT_CONTRACT = "eContract."
EVENT_LOG = "eLog"  
EVENT_TIMER = "eTimer"
"""

# 配置文件： "vt_setting.json"

```



## python的类型编程

```python

from typing import Dict, Tuple, List

def hello(a: int, b: int) -> int:
    print(a, b)
    return a+b

```


