from howtrader.app.cta_strategy import (
    CtaTemplate,
    StopOrder
)

from howtrader.trader.object import TickData, BarData, TradeData, OrderData, Offset
from howtrader.trader.event import (
    EVENT_ACCOUNT
)

from howtrader.event import Event

from howtrader.app.cta_strategy.engine import CtaEngine, EngineType
from decimal import Decimal

class GridBalanceStrategy(CtaTemplate):

    author = "51bitquant"

    balance_diff_pct = 0.01

    parameters = ["balance_diff_pct"]

    def __init__(self, cta_engine: CtaEngine, strategy_name, vt_symbol, setting):
        """"""
        super().__init__(cta_engine, strategy_name, vt_symbol, setting)

        if cta_engine.engine_type == EngineType.LIVE:
            self.cta_engine.event_engine.register(EVENT_ACCOUNT, self.process_account)

        self.my_balance = 300000
    def on_init(self):
        """
        Callback when strategy is inited.
        """
        self.write_log("策略初始化")
        self.load_bar(1)


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
        pass

    def on_bar(self, bar: BarData):
        """
        Callback of new bar data update.
        """
        # print("1分钟的K线数据", bar)

        price = bar.close_price
        self.cancel_all()  # 撤单.

        if self.my_balance <= 0:
            return

        if (abs(self.my_balance - float(self.pos) * price) / self.my_balance) >= self.balance_diff_pct:

            balance_diff = abs(self.my_balance - float(self.pos) * price) / 2
            # print('需要进行资金平衡.', balance_diff, self.my_balance, self.pos, price)
            if self.my_balance > float(self.pos) * price:
                self.buy(Decimal(price*1.001), Decimal(balance_diff/price))
            else:
                self.sell(Decimal(price * 0.999), Decimal(balance_diff / price))

        self.put_event()

    def process_account(self, event: Event):
        print("event account", event.data)

    def on_order(self, order: OrderData):
        """
        订单的回调方法: 订单状态更新的时候，会调用这个方法。
        """

        self.put_event()


    def on_trade(self, trade: TradeData):
        """
        订单成交的推送，比如你下10个BTC,那么可能不会一下子成交，会不断慢慢的成交，
        这时有成交它就会推送给你，告诉你成交了多少，还有多少没有成交
        系统通过里面处理这个方法，知道你当前的仓位数量

        """

        if trade.offset == Offset.OPEN:
            self.my_balance -= float(trade.price) * float(trade.volume)
        elif trade.offset == Offset.CLOSE:
            self.my_balance += float(trade.price) * float(trade.volume)

        self.put_event()  # 更新UI界面方法。


    def on_stop_order(self, stop_order: StopOrder):
        """
        这个是一个停止单的方法，用来监听你止损单的方法。
        """
        pass

