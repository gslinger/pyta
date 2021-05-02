# TODO docstring
# TODO merge?
import pandas as pd
#
from pyta.helper import max_period, min_period


def price_channel_upper(h: pd.Series, n: int = 20) -> pd.Series:
    return max_period(h, n)


def price_channel_lower(l: pd.Series, n: int = 20) -> pd.Series:
    return min_period(l, n)


def price_channel_mid(h: pd.Series, l: pd.Series, n: int = 20) -> pd.Series:
    return (max_period(h, n) + min_period(l, n)) / 2
