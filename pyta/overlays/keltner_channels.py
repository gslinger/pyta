from typing import Union
#
import pandas as pd
#
from pyta.overlays.exponential_moving_average import exponential_moving_average as ema
from pyta.indicators.average_true_range import average_true_range as atr
# TODO docstring


def keltner_channel_mid(c: pd.Series, n: int = 20):
    kcm_: pd.Series = ema(c, n)
    return kcm_


def keltner_channel_upper(h: pd.Series, l: pd.Series, c: pd.Series,
                          n_ema: int = 20, n_atr: int = 10, m: Union[float, int] = 2) -> pd.Series:
    kcu_ = ema(c, n_ema) + (m * atr(h, l, c, n_atr))
    return kcu_


def keltner_channel_lower(h: pd.Series, l: pd.Series, c: pd.Series,
                          n_ema: int = 20, n_atr: int = 10, m: Union[float, int] = 2) -> pd.Series:
    kcl_ = ema(c, n_ema) - (m * atr(h, l, c, n_atr))
    return kcl_
