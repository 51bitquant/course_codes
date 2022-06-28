from howtrader.app.cta_strategy import (
    CtaTemplate,
    StopOrder
)

from howtrader.trader.object import TickData, BarData, TradeData, OrderData
from howtrader.trader.utility import BarGenerator

from howtrader.trader.constant import Interval
from decimal import Decimal
from howtrader.app.cta_strategy.engine import CtaEngine

# 记得修改你的文件的类名
class Class11SimpleStrategy(CtaTemplate):

    author = "51bitquant"

    def __init__(self, cta_engine: CtaEngine, strategy_name, vt_symbol, setting):
        """"""
        super().__init__(cta_engine, strategy_name, vt_symbol, setting)
        self.bg2 = BarGenerator(self.on_bar, 2, self.on_2min_bar, Interval.MINUTE)
        self.bg5 = BarGenerator(self.on_bar, 5, self.on_5min_bar, Interval.MINUTE)
        self.bg_1hour = BarGenerator(self.on_bar, 1, self.on_1hour_bar, Interval.HOUR)
        self.bg_4hour = BarGenerator(self.on_bar, 4, self.on_4hour_bar, Interval.HOUR)

        self.place_order = False
        self.orders = []
        # self.pos #

    def on_init(self):
        """
        Callback when strategy is inited.
        """
        self.write_log("策略初始化")


    def on_start(self):
        """
        Callback when strategy is started.
        """
        self.write_log(f"我的策略启动, {self.trading}")
        self.put_event()


    def on_stop(self):
        """
        Callback when strategy is stopped.
        """
        self.write_log("策略停止")

        self.put_event()


    def on_tick(self, tick: TickData):
        print(f"tick, ask1:{tick.ask_price_1}, {tick.ask_volume_1}, bid:{tick.bid_price_1}, {tick.bid_volume_1}")
        print(f"my current pos is: {self.pos}, ask:{tick.ask_price_1}, bid: {tick.bid_price_1}")

        if self.place_order is False and self.trading:
            buy_order = self.buy(Decimal(tick.bid_price_1 * 0.9999), Decimal("0.5"))
            sell_order = self.sell(Decimal(tick.ask_price_1 * 1.0002), Decimal("0.5"))

            # self.short()
            # self.cover()  #

            # self.buy()
            # self.short()
            self.place_order = True
            print(f"buy_order: {buy_order}, sell_order: {sell_order}")
            self.orders += buy_order
            self.orders += sell_order

        self.bg2.update_tick(tick)
        self.bg5.update_tick(tick)
        self.bg_1hour.update_tick(tick)
        self.bg_4hour.update_tick(tick)

    def on_bar(self, bar: BarData):
        """
        Callback of new bar data update.
        """
        print("1分钟的K线数据", bar)
        self.bg2.update_bar(bar)
        self.bg5.update_bar(bar)  # 合成2分钟的K线
        self.bg_1hour.update_bar(bar)  # 合成一小时的数据。
        self.put_event()

    def on_2min_bar(self, bar: BarData):
        """
        Callback of new bar data update.
        """
        print("2分钟的K线数据", bar)
        self.put_event()

    def on_5min_bar(self, bar: BarData):
        """
        Callback of new bar data update.
        """
        print("5分钟的K线数据", bar)
        self.put_event()

    def on_1hour_bar(self, bar:BarData):

        print("1小时的K线数据", bar)
        self.put_event()

    def on_4hour_bar(self, bar: BarData):
        print("4小时的K线数据", bar)

        self.put_event()

    def on_order(self, order: OrderData):
        """
        订单的回调方法: 订单状态更新的时候，会调用这个方法。
        """

        print("策略推送过来的order: ", order)

        self.put_event()



    def on_trade(self, trade: TradeData):
        """
        订单成交的推送，比如你下10个BTC,那么可能不会一下子成交，会不断慢慢的成交，
        这时有成交它就会推送给你，告诉你成交了多少，还有多少没有成交
        系统通过里面处理这个方法，知道你当前的仓位数量

        """
        print("最新的成交: ", trade)
        self.put_event()  # 更新UI界面方法。


    def on_stop_order(self, stop_order: StopOrder):
        """
        这个是一个停止单的方法，用来监听你止损单的方法。
        """
        pass

