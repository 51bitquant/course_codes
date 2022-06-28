# 第六课: VNPY量化交易软件的安装, 图形界面的启动和功能介绍
软件代码地址: **https://github.com/51bitquant/howtrader**

## step 1 创建一个新的虚拟环境并激活
更新anaconda, 如果你切换到其他解析器了，可以通过执行conda deactivate,
然后再执行下面的命令。

> conda update conda

> conda create -n mytrader python==3.9

> conda activate mytrader

## step 2 安装howtrader

> pip install git+https://github.com/51bitquant/howtrader.git

## step 3 创建howtrader文件夹

在项目下面创建一个文件夹howtrader，该文件夹主要是存放log日志和配置文件的

## step 4 创建一个启动文件

``` python

from howtrader.event import EventEngine

from howtrader.trader.engine import MainEngine
from howtrader.trader.ui import MainWindow, create_qapp

from howtrader.gateway.binance import BinanceUsdtGateway, BinanceSpotGateway


from howtrader.app.cta_strategy import CtaStrategyApp
from howtrader.app.data_manager import DataManagerApp
from howtrader.app.data_recorder import DataRecorderApp
from howtrader.app.algo_trading import AlgoTradingApp
from howtrader.app.cta_backtester import CtaBacktesterApp
from howtrader.app.risk_manager import RiskManagerApp
from howtrader.app.spread_trading import SpreadTradingApp

def main():
    """"""

    qapp = create_qapp()

    event_engine = EventEngine()

    main_engine = MainEngine(event_engine)

    main_engine.add_gateway(BinanceUsdtGateway)
    main_engine.add_gateway(BinanceSpotGateway)
    main_engine.add_app(CtaStrategyApp)
    main_engine.add_app(CtaBacktesterApp)
    main_engine.add_app(DataManagerApp)
    main_engine.add_app(AlgoTradingApp)
    main_engine.add_app(DataRecorderApp)
    main_engine.add_app(RiskManagerApp)
    main_engine.add_app(SpreadTradingApp)

    main_window = MainWindow(main_engine, event_engine)
    main_window.showMaximized()

    qapp.exec()


if __name__ == "__main__":
    """
     howtrader main window demo
     howtrader 的图形化界面
     
     we have binance gate way, which is for spot, while the binances gateway is for contract or futures.
     the difference between the spot and future is their symbol is just different. Spot uses the lower case for symbol, 
     while the futures use the upper cases.
     
     币安的接口有现货和合约接口之分。 他们之间的区别是通过交易对来区分的。现货用小写，合约用大写。 btcusdt.BINANCE 是现货的symbol,
     BTCUSDT.BINANCE合约的交易对。 BTCUSD.BINANCE是合约的币本位保证金的交易对.
    """

    main()

```

