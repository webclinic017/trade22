import position
from bars import HAbar, Bar, Bars
from position import get_position, set_position, get_value,\
    get_quantity, get_profit_loss, get_quantity_value


def decide(all_bars: Bars):
    habar = all_bars.last_habar
    c = habar.color
    match c:
        case 'GREEN':
            process_green(all_bars)
        case 'RED':
            process_red(all_bars)
        case 'YELLOW':
            process_yellow(all_bars)
        case _:
            raise Exception('Color Problem', 'c =', c)


def process_green(all_bars):
    print("Processing GREEN")
    pos = get_position()
    if pos["quantity"] < 0:
        close_short_open_long_position(all_bars, pos)
    elif pos["quantity"] == 0:
        open_long_position(all_bars, pos)
    elif pos["quantity"] > 0:
        # do nothing, stay long
        pass
    else:
        raise Exception("Position value problem")


def process_red(all_bars):
    print("Processing RED")
    pos = get_position()
    if pos["quantity"] < 0:
        # do nothing, stay short
        pass
    elif pos["quantity"] == 0:
        open_short_position(all_bars, pos)
    elif pos["quantity"] > 0:
        close_long_open_short_position(all_bars, pos)
    else:
        raise Exception("Position value problem")


def process_yellow(all_bars):
    print("Processing YELLOW")
    pos = get_position()
    if pos["quantity"] < 0:
        close_short(all_bars, pos)
    elif pos["quantity"] == 0:
        # stay at zero position
        pass
    elif pos["quantity"] > 0:
        close_long(all_bars, pos)
    else:
        raise Exception("Position value problem")


# def close_all_positions(all_bars, pos):
#     print("Closing all positions")
#     position.set_position(0)


def close_long_open_short_position(all_bars, pos):
    close_long(all_bars, pos)
    open_short_position(all_bars, pos)


def close_short_open_long_position(all_bars, pos):
    close_short(all_bars, pos)
    open_long_position(all_bars, pos)


def open_long_position(all_bars, pos):
    print("Going Long")
    price = all_bars.last_raw_bar.close

    set_position(100)


def open_short_position(all_bars, pos):
    price = all_bars.last_raw_bar.close
    print("Going Short")
    set_position(-100)


def close_long(all_bars, pos):
    print("Closing Long")
    set_position(0)


def close_short(all_bars, pos):
    print("Closing Short")
    current_price = all_bars.last_raw_bar.close
    quantity, value = get_quantity_value()

