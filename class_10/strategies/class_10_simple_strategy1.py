from howtrader.app.cta_strategy import (
    CtaTemplate,
    StopOrder
)

from howtrader.trader.object import TickData, BarData, TradeData, OrderData, Interval

from howtrader.trader.utility import BarGenerator, ArrayManager
from datetime import datetime
from howtrader.app.cta_strategy.engine import CtaEngine
from decimal import Decimal


class Class10SimpleStrategy1(CtaTemplate):
    author = "51bitquant"

    def __init__(self, cta_engine: CtaEngine, strategy_name, vt_symbol, setting):
        """"""
        super().__init__(cta_engine, strategy_name, vt_symbol, setting)

        self.bg2 = BarGenerator(self.on_bar, 2, self.on_2min_bar, Interval.MINUTE)
        self.bg3 = BarGenerator(self.on_bar, 3, self.on_3min_bar, Interval.MINUTE)
        self.bg5 = BarGenerator(self.on_bar, 5, self.on_5min_bar, Interval.MINUTE)

        # self.am3 = ArrayManager()  # 3分钟的时间序列.
        # # 如果想获取其他周期的K线数据
        # self.bg_1hour = BarGenerator(self.on_bar, 1, self.on_1hour_bar, Interval.HOUR)  # 1小时的K线.
        # self.am_1hour = ArrayManager()
        self.place_order = False
        self.orders = []
        # cta_engine.register_event()
        # cta_engine.register(EVENT_POSITION, self.process_position_event)

    def on_init(self):
        """
        Callback when strategy is inited.
        """
        self.write_log("策略初始化")
        # self.load_bar(1)
        # self.load_bar() 方法向交易所请求获取K线数据，这个n表示获取多少天的一分钟的K线数据.
        # 通过1一分钟的K线来合成5/10/15,30分钟的数据，甚至一小时等更多的数据.
        # 这个方法不许要调用，不然会出错.


    def on_start(self):
        """
        Callback when strategy is started.
        """
        self.write_log("策略启动")
        self.put_event()  # 如果你要让UI界面更新你就要调用这个方法，这个方法是用来通知系统更新UI图形界面的。


    def on_stop(self):
        """
        Callback when strategy is stopped.
        """
        self.write_log("策略停止")

        self.put_event()


    def on_tick(self, tick: TickData):
        """
        盘口的数据更新的方法.
        """
        # self.bg.update_tick(tick)  # 该方法是把tick数据合成分钟的K线数据
        # print("\n")
        # print(tick.ask_price_1, tick.ask_volume_1,  tick.datetime, datetime.now())
        # print("-------")
        # print(tick.bid_price_1, tick.bid_volume_1,  tick.datetime, datetime.now())
        # print("\n")
        print(f"my current pos is: {self.pos}, ask:{tick.ask_price_1}, bid: {tick.bid_price_1}")

        if self.place_order is False and self.trading:
            buy_order = self.buy(Decimal(tick.bid_price_1 * 0.99), Decimal("0.5"))
            # sell_order = self.short(tick.ask_price_1 * 1.0001, 0.01)
            sell_order = self.sell(Decimal(tick.ask_price_1 * 1.01), Decimal("0.5"))
            self.place_order = True
            print(f"buy_order: {buy_order}, sell_order: {sell_order}")
            self.orders += buy_order
            self.orders += sell_order

        self.bg2.update_tick(tick)
        self.bg3.update_tick(tick)
        self.bg5.update_tick(tick)

    def on_bar(self, bar: BarData):
        """
        Callback of new bar data update.
        """
        print("一分钟的K线数据", bar)
        self.bg2.update_bar(bar)
        self.bg3.update_bar(bar)
        self.bg5.update_bar(bar)
        self.put_event()


    def on_2min_bar(self, bar: BarData):
        print("2分钟的Bar", bar)  # 2分钟的K线数据.


    def on_3min_bar(self, bar: BarData):
        print("3分钟的Bar", bar)  # 3分钟的K线数据.


    def on_5min_bar(self, bar: BarData):
        print("5分钟的Bar", bar)  # 5分钟的K线数据.


    def on_10min_bar(self, bar: BarData):
        print("10分钟的Bar", bar)  # 10分钟的K线数据.


    def on_20min_bar(self, bar: BarData):
        print("20分钟的Bar", bar)  # 20分钟的K线数据.


    def on_30min_bar(self, bar: BarData):
        print("30分钟的Bar", bar)  # 30分钟的K线数据.


    def on_1hour_bar(self, bar: BarData):
        print("1小时的Bar", bar)


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

