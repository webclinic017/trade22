__position = {
    "quantity": 0,
    "price": 0.0,
    "profit_loss": 0.0
}


def get_position():
    global __position
    return __position


def set_position(quantity: int, price: float):
    global __position
    __position["quantity"] = quantity
    __position["price"] = price
    return __position


def update_profit_loss(value: float):
    __position['profit_loss'] += value


def get_quantity():
    return __position["quantity"]


def get_price():
    return __position["price"]


def get_quantity_value():
    return __position["value"], __position["quantity"]


def get_profit_loss():
    return __position["profit_loss"]
