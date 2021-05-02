import pandas as pd
#
from pyta.indicators.average_true_range import average_true_range as atr
from pyta.helper import highest, lowest


def chande_kroll_stop_long(h: pd.Series, l: pd.Series, c: pd.Series, p: int = 10, x: int = 1, q: int = 9) \
        -> pd.Series:
    _atr: pd.Series = atr(h, l, c, n=p)
    first_low_stop: pd.Series = lowest(l, p) + x * _atr
    stop_long: pd.Series = lowest(first_low_stop, q)
    return stop_long


# todo maybe union type hint for x ?
def chande_kroll_stop_short(h: pd.Series, l: pd.Series, c: pd.Series, p: int = 10, x: int = 1, q: int = 9) \
        -> pd.Series:
    _atr: pd.Series = atr(h, l, c, n=p)
    first_high_stop: pd.Series = highest(h, p) - x * _atr
    stop_short: pd.Series = highest(first_high_stop, q)
    return stop_short
