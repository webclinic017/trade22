__position = {
    "quantity": 0,
    "price": 0.0,
    "profit_loss": 0.0
}


def get_position():
    global __position
    return __position


def get_quantity():
    return __position["quantity"]


def get_price():
    return __position["price"]


def get_quantity_price():
    return __position["quantity"], __position["price"]


def get_profit_loss():
    return __position["profit_loss"]


def set_quantity(quantity: int):
    global __position
    __position["quantity"] = quantity


def set_price(price: float):
    global __position
    __position.price = price


def set_quantity_price(quantity: int, price: float):
    global __position
    __position["quantity"] = quantity
    __position["price"] = price


def add_to_profit_loss(value: float):
    __position['profit_loss'] += value
    print("Position: {:d}   PL: {:.2f}".format(__position["quantity"], __position["profit_loss"]))
