__position = {
    "quantity": 0,
    "value": 0.0,
    "profit_loss": 0.0
}

def get_position():
    global __position
    return __position

def set_position(quantity: int, value: float):
    global __position
    __position["quantity"] = quantity
    __position["value"] = value
    return __position

def update_profit_loss(value:float):
    __position['profit_loss'] += value
