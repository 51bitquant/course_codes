from howtrader.app.cta_strategy.backtesting import BacktestingEngine
from howtrader.trader.object import Interval
from datetime import datetime

from strategies.martingle_spot_strategyV3 import MartingleSpotStrategyV3

if __name__ == '__main__':
    engine = BacktestingEngine()

    engine.set_parameters(
        vt_symbol="btcusdt.BINANCE",  # 现货的数据
        interval=Interval.MINUTE,
        start=datetime(2018,1,11),
        end=datetime(2018, 5, 1),
        # end=datetime(2020,12,1),
        rate=7.5/10000,  # 币安手续费千分之1， BNB 万7.5  7.5/10000
        slippage=0,
        size=1,  # 币本位合约 100
        pricetick=0.01,  # 价格精度.
        capital=300000)


    engine.load_data()

    engine.add_strategy(MartingleSpotStrategyV3, {})
    engine.run_backtesting()

    engine.calculate_result() # 计算回测的结果
    engine.calculate_statistics()  # 计算一些统计指标

    engine.show_chart()  # 绘制图表

    # 一个参数没法进行优化.
    # setttings = OptimizationSetting()
    # setttings.add_parameter("balance_diff_pct", start=0.001, end=0.10, step=0.001)
    # setttings.set_target("total_return")
    # result = engine.run_ga_optimization(setttings)
    # print(result)


