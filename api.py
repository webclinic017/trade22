import iso8601
import pytz
from datetime import datetime, timedelta

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest, GetOrdersRequest, GetOrderByIdRequest
from alpaca.trading.enums import OrderSide, OrderStatus, TimeInForce
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockLatestBarRequest, StockBarsRequest
from alpaca.data.timeframe import TimeFrame

apikey = "PKKJZYB9P6Q36H84YMXF"
secretkey = "hBnEAEiD1f67p6hM4DKkUBtixY01YulNWSuGHOyx"

trading_client = TradingClient(apikey, secretkey, paper=True)
stock_hist_client = StockHistoricalDataClient(apikey, secretkey)


def get_clock():
    global trading_client
    clock = trading_client.get("/clock")
    return clock


def get_datetime_aware() -> datetime:
    clock = get_clock()
    timestamp = clock["timestamp"]
    dt = iso8601.parse_date(timestamp)
    return dt


def get_datetime_tz(timezone) -> datetime:
    dt = get_datetime_aware()
    return dt.astimezone(timezone)


def get_datetime_eastern() -> datetime:
    return get_datetime_tz(pytz.timezone("US/Eastern"))


def get_datetime_utc() -> datetime:
    return get_datetime_tz(pytz.timezone("UTC"))


def get_one_day_minute_bars(d: datetime):
    global stock_hist_client
    start = pytz.timezone("US/Eastern").localize(d.replace(hour=9, minute=30)).astimezone(pytz.utc)
    end = start + timedelta(hours=0.5)
    request_params = StockBarsRequest(
        symbol_or_symbols='SPY',
        timeframe=TimeFrame.Minute,
        start=start,
        end=end
    )
    return stock_hist_client.get_stock_bars(request_params)['SPY']


def buy():
    # global trading_client
    # market_order_data = MarketOrderRequest(
    #     symbol="SPY",
    #     qty=1,
    #     side=OrderSide.BUY,
    #     time_in_force=TimeInForce.DAY
    # )
    #
    # market_order = trading_client.submit_order(
    #     order_data=market_order_data
    # )
    #
    # request_params = GetOrdersRequest(
    #     status=OrderStatus.NEW,
    #     side=OrderSide.BUY
    # )
    #
    # sleep(1)
    # orders = trading_client.get_orders()
    # print(orders)
    pass


def sell():
    # global trading_client
    # market_order_data = MarketOrderRequest(
    #     symbol="SPY",
    #     qty=1,
    #     side=OrderSide.SELL,
    #     time_in_force=TimeInForce.DAY
    # )
    #
    # market_order = trading_client.submit_order(
    #     order_data=market_order_data
    # )
    #
    # request_params = GetOrdersRequest(
    #     status=OrderStatus.NEW,
    #     side=OrderSide.SELL
    # )
    #
    # orders = trading_client.get_orders(filter=request_params)
    # print(orders)
    pass
