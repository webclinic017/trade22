import position
from bars import HAbar, Bar, Bars
from position import get_position, set_position


def decide(all_bars: Bars):
    pos = position.get_position()
    habar = all_bars.last_habar
    c = habar.color
    match c:
        case 'GREEN':
            process_green(all_bars, pos)
        case 'RED':
            process_red(all_bars, pos)
        case 'YELLOW':
            process_yellow(all_bars, pos)
        case _:
            raise Exception('Color Problem', 'c =', c)


def process_green(all_bars, pos):
    print("Processing GREEN")
    pos = get_position()
    if pos < 0:
        close_short_go_long(all_bars, pos)
    elif pos == 0:
        go_long(all_bars, pos)
    elif pos > 0:
        # do nothing, stay long
        pass
    else:
        raise Exception("Position value problem")


def process_red(all_bars, pos):
    print("Processing RED")
    pos = get_position()
    if pos < 0:
        # do nothing, stay short
        pass
    elif pos == 0:
        go_short(all_bars, pos)
    elif pos > 0:
        close_long_go_short(all_bars, pos)
    else:
        raise Exception("Position value problem")


def process_yellow(all_bars, pos):
    print("Processing YELLOW")
    pos = get_position()
    if pos < 0:
        close_short(all_bars, pos)
    elif pos == 0:
        # stay at zero position
        pass
    elif pos > 0:
        close_long(all_bars, pos)
    else:
        raise Exception("Position value problem")


def close_all_positions(all_bars, pos):
    print("Closing all positions")
    position.set_position(0)


def close_long_go_short(all_bars, pos):
    close_all_positions(all_bars, pos)
    go_short(all_bars, pos)


def close_short_go_long(all_bars, pos):
    close_all_positions(all_bars, pos)
    go_long(all_bars, pos)


def go_long(all_bars, pos):
    print("Going Long")
    set_position(100)


def go_short(all_bars, pos):
    print("Going Short")
    set_position(-100)


def close_long(all_bars, pos):
    print("Closing Long")
    set_position(0)


def close_short(all_bars, pos):
    print("Closing Short")
    set_position(0)
