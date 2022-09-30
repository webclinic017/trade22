__position: int = 0

def get_position():
    global __position
    return __position

def set_position(value: int):
    global __position
    __position = value
    return __position