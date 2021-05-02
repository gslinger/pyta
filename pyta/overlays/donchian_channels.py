import pandas as pd
#
from pyta.helper import highest, lowest
# TODO merge?
# TODO docstring


def donchian_channel_lower(l: pd.Series, n: int = 20) -> pd.Series:
    return lowest(l, n)


def donchian_channel_upper(h: pd.Series, n: int = 20) -> pd.Series:
    return highest(h, n)


def donchian_channel_basis(h: pd.Series, l: pd.Series, n: int = 20) -> pd.Series:
    return (donchian_channel_upper(h, n) + donchian_channel_lower(l, n)) / 2
