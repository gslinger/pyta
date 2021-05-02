import pandas as pd
from typing import Union
#
from pyta.overlays.bollinger_bands import *


def bollinger_bandwidth(price: pd.Series, n: int = 20, m: Union[int, float] = 2) -> pd.Series:
    b_up: pd.Series = bollinger_band_upper(price, n, m)
    b_low: pd.Series = bollinger_band_lower(price, n, m)
    b_mid: pd.Series = bollinger_band_middle(price, n)
    b_band: pd.Series = ((b_up - b_low) / b_mid) * 100
    return b_band


bollinger_bandwidth.__doc__ = """Bollinger Bandwidth

Measures % difference between upper and lower bollinger bands.

Source:
    https://school.stockcharts.com/doku.php?id=technical_indicators:bollinger_band_width

Formula:
    [(BB_upper - BB_lower) / BB_middle] * 100 

Arguments:
    price (pdSeries) : Price series (usually close). 
    n (int)          : Period for MA [Default: 20]
    m (int)          : Multiplier for StdDev [Default: 2]

Returns:
    pdSeries
"""