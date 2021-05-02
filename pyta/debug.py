import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        beg_ts = time.time()
        return_value = func(*args, **kwargs)
        end_ts = time.time()
        print("Elapsed time for {}: {}".format(func.__name__, (end_ts - beg_ts)))
        return return_value
    return wrapper


def verify_series(series: list, length: int) -> bool:
    for series_ in series:
        if series_ is None or len(series_) < length:
            return False
    return True
