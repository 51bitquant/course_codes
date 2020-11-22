from howtrader.gateway.binance.binance_gateway import BinanceGateway

from howtrader.gateway.binances.binances_gateway import BinancesGateway
from howtrader.event.engine import  EventEngine, Event, EVENT_TIMER

from howtrader.trader.constant import Status, OrderType
from howtrader.trader.constant import Exchange, Interval
# from howtrader.trader.object import Exchange, Interval
from howtrader.trader.object import TickData



# Exchange.BINANCE
# Interval.MINUTE

tick = TickData()
# tick.ask_volume_1
# tick.bid_price_1