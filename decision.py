import position
from bars import HAbar
from position import get_position, set_position


def decide(bar: HAbar):
    c = bar.color
    match c:
        case 'GREEN':
            process_green()
        case 'RED':
            process_red()
        case 'YELLOW':
            process_yellow()
        case _:
            raise Exception('Color Problem', 'c =', c)


def process_green():
    print("Processing GREEN")
    pos = get_position()
    if pos < 0:
        close_short_go_long()
    elif pos == 0:
        go_long()
    elif pos > 0:
        # do nothing, stay long
        pass
    else:
        raise Exception("Position value problem")


def process_red():
    print("Processing RED")
    pos = get_position()
    if pos < 0:
        # do nothing, stay short
        pass
    elif pos == 0:
        go_short()
    elif pos > 0:
        close_long_go_short()
    else:
        raise Exception("Position value problem")


def process_yellow():
    print("Processing YELLOW")
    pos = get_position()
    if pos < 0:
        close_short()
    elif pos == 0:
        # stay at zero position
        pass
    elif pos > 0:
        close_long()
    else:
        raise Exception("Position value problem")


def close_all_positions():
    print("Closing all positions")
    position.set_position(0)


def close_long_go_short():
    close_all_positions()
    go_short()


def close_short_go_long():
    close_all_positions()
    go_long()


def go_long():
    print("Going Long")
    set_position(100)


def go_short():
    print("Going Short")
    set_position(-100)


def close_long():
    print("Closing Long")
    set_position(0)


def close_short():
    print("Closing Short")
    set_position(0)
