import api
from datetime import datetime

from bars import Bars
from decision import decide
from position import get_position

all_bars = Bars()

d = datetime(2022, 10, 4)
minute_bars = api.get_one_day_minute_bars(d)

for minute_bar in minute_bars:
    # pos = get_position()
    # print("position =", pos)
    all_bars.add(minute_bar)
    decide(all_bars)
