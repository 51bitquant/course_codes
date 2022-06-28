from howtrader.app.cta_strategy.backtesting import BacktestingEngine
from howtrader.trader.object import Interval
from datetime import datetime
from strategies.fixed_trade_time_strategy import FixedTradeTimeStrategy

if __name__ == '__main__':
    engine = BacktestingEngine()

    engine.set_parameters(
        vt_symbol="btcusdt.BINANCE",  # 现货的数据
        interval=Interval.MINUTE,
        start=datetime(2018,1,1),
        end=datetime(2018,6,1),
        rate=1/1000,  # 币安手续费千分之1， BNB 万7.5  7.5/10000
        slippage=0,
        size=1,  # 币本位合约 100
        pricetick=0.01,  # 价格精度.
        capital=300000)

    engine.add_strategy(FixedTradeTimeStrategy, {})

    engine.load_data()
    engine.run_backtesting()

    engine.calculate_result() # 计算回测的结果
    engine.calculate_statistics()  # 计算一些统计指标

    engine.show_chart()  # 绘制图表

# 收益上看似不高，但是要知道你一开始你就没有投入100万，这个是相当于你慢慢挣钱，50%-60%
# 慢慢投资，然后等你攒到100万的时候，实际上你已经有了140万
# 所以定投有相当于懒人理财的功能。
# 30 -- 805,090.27
