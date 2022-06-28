from howtrader.app.cta_strategy import (
    CtaTemplate,
    StopOrder
)

from howtrader.trader.object import TickData, BarData, TradeData, OrderData
from howtrader.trader.constant import Interval
from howtrader.trader.utility import BarGenerator, ArrayManager
from howtrader.app.cta_strategy.engine import CtaEngine
from decimal import Decimal

class FixedTradPriceStrategy(CtaTemplate):
    """
    基于价格的定投
    """
    author = "51bitquant"
    fixed_trade_money = 1000  # 每次定投的资金比例.
    price_change_pct = 0.05  # 价格变动多少的时候定投

    parameters = ['fixed_trade_money', 'price_change_pct']

    def __init__(self, cta_engine: CtaEngine, strategy_name, vt_symbol, setting):
        """"""
        super().__init__(cta_engine, strategy_name, vt_symbol, setting)
        self.bg_4hour = BarGenerator(self.on_bar, 4, self.on_4hour_bar, Interval.HOUR)
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
        self.bg_4hour.update_tick(tick)

    def on_bar(self, bar: BarData):
        """
        Callback of new bar data update.
        """
        self.bg_4hour.update_bar(bar)  # 合成四小时的数据.
        self.put_event()

    def on_4hour_bar(self, bar: BarData):
        """
        四小时的K线数据.
        """
        self.cancel_all()  # 撤销所有订单.
        self.am.update_bar(bar)  # 把最新的K线放进时间序列里面.
        # 下面可以计算基数指标等等....
        # 以及下单的事情.

        if not self.am.inited:
            return

        # [0,1,2,3,4,5,6]
        last_close_price = self.am.close_array[-2]  # 上一根K线
        current_close_price = bar.close_price # self.am.close_array[-1] #  当前的收盘价

        # 如果四小时价格下跌5%就买入.
        if (last_close_price - current_close_price)/last_close_price >= self.price_change_pct:
            price = bar.close_price * 1.001
            self.buy(Decimal(price), Decimal(self.fixed_trade_money/price))

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

