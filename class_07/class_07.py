from howtrader.gateway.binance import BinanceUsdtGateway
from howtrader.gateway.binance import BinanceSpotGateway
from howtrader.event.engine import  EventEngine, Event, EVENT_TIMER

from howtrader.trader.constant import Status, OrderType
from howtrader.trader.constant import Exchange, Interval
# from howtrader.trader.object import Exchange, Interval
from howtrader.trader.object import TickData



# Exchange.BINANCE
# Interval.MINUTE

# tick = TickData()
# tick.ask_volume_1
# tick.bid_price_1

# {'ask1': 100}  # key value


# def hello(a):
#     print(a)

# int hello() {
#
#     return 10;
# }


def hello(string: str) -> int:
    print(string)

    return len(string)


# a = hello("helloworld")
#
# print(a)

# b = hello(10)
# print(b)

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Human(object):
    def __init__(self, name, age):
        self.name = name


def func(person: Person) -> Person:
    print(person.age, person.name)

    return person

a: Person = func(Person('lisi', 10))

b = func(Person('lisi',15))

print(a.name)
print(a.age)

print(b.age)

from typing import Dict, Tuple, List

def hi(a: List) -> List:

    return a