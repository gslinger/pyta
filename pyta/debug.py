import time
from functools import wraps
from typing import Union


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        beg_ts = time.time()
        return_value = func(*args, **kwargs)
        end_ts = time.time()
        print("Elapsed time for {}: {}".format(func.__name__, (end_ts - beg_ts)))
        return return_value
    return wrapper


def verify_series(series: list, length_min: int) -> None:
    for series_ in series:
        length_act: int = len(series_)
        if length_act < length_min:
            raise NotEnoughData(length_min, length_act)


class NotEnoughData(Exception):
    def __init__(self, n_min: int, n_act: int) -> None:
        err_message = f"The series is not long enough. Minimum : {n_min}. Actual: {n_act}"

        super().__init__(err_message)

