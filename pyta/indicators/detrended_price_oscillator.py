import pandas as pd
#
from pyta.overlays.simple_moving_average import simple_moving_average as sma
# todo docstring
# todo tradingview has an offset option


def detrended_price_oscillator(c: pd.Series, n: int = 21) -> pd.Series:
    ma = sma(c, n)
    dpo_ = c - ma.shift(int(n / 2 + 1))
    return dpo_
