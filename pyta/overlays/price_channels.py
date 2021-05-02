# TODO docstring
# TODO merge?
import pandas as pd
#
from pyta.helper import highest, lowest


def price_channel_upper(h: pd.Series, n: int = 20) -> pd.Series:
    return highest(h, n)


def price_channel_lower(l: pd.Series, n: int = 20) -> pd.Series:
    return lowest(l, n)


def price_channel_mid(h: pd.Series, l: pd.Series, n: int = 20) -> pd.Series:
    return (highest(h, n) + lowest(l, n)) / 2
