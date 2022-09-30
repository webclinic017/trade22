from datetime import datetime

from alpaca.data.models.bars import Bar


class HAbar:
    def __init__(self, t: datetime, o: float, h: float, l_: float, c: float):
        self.timestamp = t
        self.open = o
        self.high = h
        self.low = l_
        self.close = c
        diff = self.close - self.open
        if abs(diff) <= 0.01:
            self.color = "YELLOW"
        elif diff > 0.0:
            self.color = "GREEN"
        else:
            self.color = "RED"

    def __str__(self):
        s = "{}, {:.2f}, {:.2f}, {:.2f}, {:.2f}".format(
            self.timestamp.strftime("%H:%M:%S"), self.open, self.high, self.low, self.close
        )
        return s


class HAbars:
    def __init__(self) -> None:
        self.bars = []

    def add(self, bar: Bar) -> HAbar:
        t = bar.timestamp
        o = bar.open
        h = bar.high
        l_ = bar.low
        c = bar.close

        if len(self.bars) == 0:
            this_bar = HAbar(t, o, h, l_, c)
        else:
            prev_bar = self.bars[-1]
            ht = t
            ho = (prev_bar.open + prev_bar.close) / 2
            hc = (o + h + l_ + c) / 4
            hh = max(h, ho, hc)
            hl = min(l_, ho, hc)
            this_bar = HAbar(ht, ho, hh, hl, hc)
        self.bars.append(this_bar)
        return this_bar


class Bars:
    def __init__(self):
        self.raw_bars: list = []
        self.ha_bars = HAbars()

    def add(self, bar: Bar):
        self.raw_bars.append(bar)
        ha_bar = self.ha_bars.add(bar)
        return ha_bar
