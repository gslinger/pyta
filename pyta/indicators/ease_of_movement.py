import pandas as pd
#
from pyta.overlays.simple_moving_average import simple_moving_average as sma
# TODO docstring


def ease_of_movement(h: pd.Series, l: pd.Series, v: pd.Series, n: int = 14, div: int = 10000) -> pd.Series:
    hl2: pd.Series = (h + l) / 2
    eom_temp = div * hl2.diff(1) * (h - l) / v
    eom_: pd.Series = sma(eom_temp, n)
    return eom_
