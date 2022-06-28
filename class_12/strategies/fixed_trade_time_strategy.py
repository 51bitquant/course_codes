from howtrader.app.cta_strategy import (
    CtaTemplate,
    StopOrder
)

from howtrader.trader.object import TickData, BarData, TradeData, OrderData
from howtrader.trader.utility import BarGenerator, ArrayManager
from howtrader.trader.constant import Interval
from howtrader.app.cta_strategy.engine import CtaEngine
from decimal import Decimal


class FixedTradeTimeStrategy(CtaTemplate):
    """
    基于价格的定投
    """

    author = "51bitquant"

    fixed_trade_money = 1000

    parameters = ["fixed_trade_money"]


    def __init__(self, cta_engine: CtaEngine, strategy_name, vt_symbol, setting):
        """"""
        super().__init__(cta_engine, strategy_name, vt_symbol, setting)
        self.bg_1hour = BarGenerator(self.on_bar, 1, self.on_1hour_bar, Interval.HOUR)
        self.am = ArrayManager(size=100)  # 时间序列，类似我们用的pandas, 值保留最近的N个K线的数据.

    def on_init(self):
        """
        Callback when strategy is inited.
        """
        self.write_log("策略初始化")
        self.load_bar(1)  # 具体加载多少天的数据, 1表示1天的数据，如果是2表示过去2天的数据

    def on_start(self):
        """
        Callback when strategy is started.
        """
        self.write_log(f"我的策略启动")
        self.put_event()

    def on_stop(self):
        """
        Callback when strategy is stopped.
        """
        self.write_log("策略停止")
        self.put_event()

    def on_tick(self, tick: TickData):
        self.bg_1hour.update_tick(tick)

    def on_bar(self, bar: BarData):
        """
        Callback of new bar data update.
        """
        self.bg_1hour.update_bar(bar)  # 合成1小时的数据.
        self.put_event()

    def on_1hour_bar(self, bar: BarData):
        """
        1小时的K线数据.
        """
        self.cancel_all()  # 取消订单.
        self.am.update_bar(bar)  # 把最新的K线放进时间序列里面.
        if not self.am.inited:  # True
            return

        """
        定投逻辑: 周四下午三点定投， 周五下午四点定投
        """
        # 2000 * 54  # 10万美金，
        if bar.datetime.isoweekday() == 5 and bar.datetime.hour == 16:
            price = bar.close_price * 1.001
            self.buy(Decimal(price), Decimal(self.fixed_trade_money/price))

        if bar.datetime.isoweekday() == 4 and bar.datetime.hour == 15:
            price = bar.close_price * 1.001
            self.buy(Decimal(price), Decimal(self.fixed_trade_money / price))


        # 下面可以计算基数指标等等....
        # 以及下单的事情.

        self.put_event()

    def on_order(self, order: OrderData):
        """
        订单的回调方法: 订单状态更新的时候，会调用这个方法。
        """
        self.put_event()

    def on_trade(self, trade: TradeData):
        """
        """
        self.put_event()  # 更新UI界面方法。

    def on_stop_order(self, stop_order: StopOrder):
        """
        这个是一个停止单的方法，用来监听你止损单的方法。
        """
        pass

