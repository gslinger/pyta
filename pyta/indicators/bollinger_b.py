import pandas as pd
from typing import Union
#
from pyta.overlays.bollinger_bands import *


def bollinger_b(price: pd.Series, n: int = 20, m: Union[int, float] = 2) -> pd.Series:
    b_up = bollinger_band_upper(price, n, m)
    b_low = bollinger_band_lower(price, n, m)
    b_b = (price - b_low) / (b_up - b_low)
    return b_b


bollinger_b.__doc__ = """Bollinger %B

Quantifies a price relative to upper and lower bollinger bands. 

Source:
    https://school.stockcharts.com/doku.php?id=technical_indicators:bollinger_band_perce

Formula:
    (price - BB_lower) / (BB_upper - BB_lower)

Arguments:
    price (pdSeries) : Price series (usually close). 
    n (int)          : Period for MA [Default: 20]
    m (int)          : Multiplier for StdDev [Default: 2]

Returns:
    pdSeries
"""