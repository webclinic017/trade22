import iso8601
import pytz
from datetime import datetime

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest, GetOrdersRequest, GetOrderByIdRequest
from alpaca.trading.enums import OrderSide, OrderStatus, TimeInForce

apikey = "PKKJZYB9P6Q36H84YMXF"
secretkey = "hBnEAEiD1f67p6hM4DKkUBtixY01YulNWSuGHOyx"

trading_client = TradingClient(apikey, secretkey, paper=True)


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

