import position
from bars import HAbar, Bar, Bars
from position import get_position, set_quantity, set_price, set_quantity_price, \
    add_to_profit_loss


def decide(all_bars: Bars):
    habar = all_bars.last_habar
    c = habar.color
    pos = get_position()
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
    quantity = pos["quantity"]
    if quantity < 0:
        close_short_open_long_position(all_bars, pos)
    elif quantity == 0:
        open_long_position(all_bars, pos)
    elif quantity > 0:
        # do nothing, stay long
        pass
    else:
        raise Exception("Position value problem")


def process_red(all_bars, pos):
    print("Processing RED")
    quantity = pos["quantity"]
    if quantity < 0:
        # do nothing, stay short
        pass
    elif quantity == 0:
        open_short_position(all_bars, pos)
    elif quantity > 0:
        close_long_open_short_position(all_bars, pos)
    else:
        raise Exception("Position value problem")


def process_yellow(all_bars, pos):
    print("Processing YELLOW")
    quantity = pos["quantity"]
    if quantity < 0:
        close_short(all_bars, pos)
    elif quantity == 0:
        # stay at zero position
        pass
    elif quantity > 0:
        close_long(all_bars, pos)
    else:
        raise Exception("Position value problem")


# def close_all_positions(all_bars, pos):
#     print("Closing all positions")
#     position.set_position(0)


def open_long_position(all_bars, pos):
    print("Going Long")
    price = all_bars.last_raw_bar.close
    quantity = 100
    set_quantity_price(quantity, price)


def open_short_position(all_bars, pos):
    print("Going Short")
    price = all_bars.last_raw_bar.close
    quantity = -100
    set_quantity_price(quantity, price)


def close_long(all_bars, pos):
    print("Closing Long")
    current_price = all_bars.last_raw_bar.close
    quantity = pos["quantity"]
    price = pos["price"]
    pl = quantity * (current_price - price)
    add_to_profit_loss(pl)


def close_short(all_bars, pos):
    print("Closing Short")
    current_price = all_bars.last_raw_bar.close
    quantity = pos["quantity"]
    price = pos["price"]
    pl = quantity * (price - current_price)
    add_to_profit_loss(pl)


def close_long_open_short_position(all_bars, pos):
    close_long(all_bars, pos)
    open_short_position(all_bars, pos)


def close_short_open_long_position(all_bars, pos):
    close_short(all_bars, pos)
    open_long_position(all_bars, pos)
