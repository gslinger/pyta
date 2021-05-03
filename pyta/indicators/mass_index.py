import pandas as pd
#
from pyta.overlays.exponential_moving_average import exponential_moving_average as ema


def mass_index(h: pd.Series, l: pd.Series, n: int = 10, n_ema: int = 9) -> pd.Series:
    range_ = h - l
    ema_ = ema(range_, n_ema)
    mi_temp = ema_ / ema(ema_, n_ema)
    mi_ = mi_temp.rolling(n).sum()
    return mi_


