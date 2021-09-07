import sys
from time import sleep
from datetime import datetime, time
from logging import INFO

from howtrader.event import EventEngine
from howtrader.trader.setting import SETTINGS
from howtrader.trader.engine import MainEngine, LogEngine

from howtrader.gateway.binances import BinancesGateway  # 合约接口
from howtrader.gateway.binance import BinanceGateway  # 现货接口
from howtrader.app.cta_strategy import CtaStrategyApp, CtaEngine
from howtrader.app.cta_strategy.base import EVENT_CTA_LOG

SETTINGS["log.active"] = True
SETTINGS["log.level"] = INFO
SETTINGS["log.console"] = True

# 合约的api配置
binances_setting = {
    "key": "",
    "secret": "",
    "会话数": 3,
    "服务器": "REAL",
    "合约模式": "正向",
    "代理地址": "",
    "代理端口": 0,
}

# 现货的api
binance_setting = {
    "key": "",
    "secret": "",
    "session_number": 3,
    "proxy_host": "",
    "proxy_port": 0,
}


def run():
    """
    Running in the child process.
    """
    SETTINGS["log.file"] = True

    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)
    main_engine.add_gateway(BinancesGateway)
    main_engine.add_gateway(BinanceGateway)
    # cta_engine = main_engine.add_app(CtaStrategyApp)
    cta_engine: CtaEngine = main_engine.add_app(CtaStrategyApp)
    main_engine.write_log("主引擎创建成功")

    # log_engine = main_engine.get_engine("log")
    log_engine: LogEngine = main_engine.get_engine("log")
    event_engine.register(EVENT_CTA_LOG, log_engine.process_log_event)
    main_engine.write_log("注册日志事件监听")

    # main_engine.connect(binances_setting, "BINANCES")  # 连接合约的
    main_engine.connect(binance_setting, "BINANCE")  # 连接现货的
    main_engine.write_log("连接接口成功")

    sleep(10)

    cta_engine.init_engine()
    main_engine.write_log("CTA策略初始化完成")

    cta_engine.init_all_strategies()
    sleep(60)  # Leave enough time to complete strategy initialization
    main_engine.write_log("CTA策略全部初始化")

    cta_engine.start_all_strategies()
    main_engine.write_log("CTA策略全部启动")

    while True:
        sleep(10)


if __name__ == "__main__":
    run()
