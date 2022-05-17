from datetime import datetime
from functools import wraps


def save_func_info(function):
    import logging
    logging.basicConfig(filename='options.log', level=logging.INFO)

    @wraps(function)
    def wrapper(*args, **kwargs):
        logging.info(f"Function: {function.__name__}. Ran at {datetime.now()}")
        return function(*args, **kwargs)
    return wrapper


def take_taxes(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        taxes_days = list(range(1, 6))
        result = function(*args, **kwargs)
        if result > 500 and datetime.now().weekday() in taxes_days:
            result -= result * 0.04
            return f"{result}\nTaxes were taken!"
        return result
    return wrapper
