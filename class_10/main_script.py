import sys
from time import sleep
from datetime import datetime, time
from logging import INFO

from howtrader.event import EventEngine
from howtrader.trader.setting import SETTINGS
from howtrader.trader.engine import MainEngine
from howtrader.app.cta_strategy.engine import CtaEngine

from howtrader.gateway.binance import BinanceSpotGateway, BinanceUsdtGateway, BinanceInverseGateway
from howtrader.app.cta_strategy import CtaStrategyApp
from howtrader.app.cta_strategy.base import EVENT_CTA_LOG

SETTINGS["log.active"] = True  #
SETTINGS["log.level"] = INFO
SETTINGS["log.console"] = True  # 打印信息到终端.

gateway_settings = {
    "key": "xx",
    "secret": "xxx",
    "proxy_host": "127.0.0.1",
    "proxy_port": 1087
}


if __name__ == "__main__":

    SETTINGS["log.file"] = True

    event_engine = EventEngine()  # 初始化事件引擎
    main_engine = MainEngine(event_engine)  # 初始化主引擎
    main_engine.add_gateway(BinanceUsdtGateway)  # 添加cta策略的app


    cta_engine: CtaEngine = main_engine.add_app(CtaStrategyApp)
    # 添加cta引擎, 实际上就是初始化引擎。

    main_engine.write_log("主引擎创建成功")

    log_engine  = main_engine.get_engine("log")
    event_engine.register(EVENT_CTA_LOG, log_engine.process_log_event)
    main_engine.write_log("注册日志事件监听")

    main_engine.connect(gateway_settings, "BINANCE_USDT")
    main_engine.write_log("连接BINANCE接口")

    sleep(10)  # 稍作等待策略启动完成。

    cta_engine.init_engine()
    # 启动引擎 --> 实际上是处理CTA策略要准备的事情，加载策略
    # 具体加载的策略来自于配置文件howtrader/cta_strategy_settings.json
    # 仓位信息来自于howtrader/cta_strategy_data.json
    main_engine.write_log("CTA策略初始化完成")

    # cta_engine.add_strategy() # 类似于我们在UI界面添加策略的操作类似

    cta_engine.init_all_strategies()  # 初始化所有的策略, 具体启动的哪些策略是来自于配置文件的

    sleep(60)  # 预留足够的时间让策略去初始化.

    main_engine.write_log("CTA策略全部初始化")

    cta_engine.start_all_strategies()  # 开启所有的策略.

    main_engine.write_log("CTA策略全部启动")

    while True:
        sleep(10)
