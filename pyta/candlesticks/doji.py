import pandas as pd
import numpy as np
#
from pyta.indicators.average_true_range import average_true_range as atr


# TODO better name ?
def is_doji(o: pd.Series, h: pd.Series, l: pd.Series, c: pd.Series,  n_atr: int = 100, doji_size: float = 0.1) \
        -> pd.Series:
    body: pd.Series = abs(c - o)
    _atr: pd.Series = atr(h, l, c, n_atr)
    doji: pd.Series = np.logical_and((body / (h - l)) < doji_size, body < (_atr / 10))
    return doji


is_doji.__doc__ = """Identifies Dojis

A doji is an indecision signal, represented by a small body relative to range. 

Source:
    https://www.amazon.co.uk/Encyclopedia-Candlestick-Charts-Wiley-Trading/dp/0470182016

Formula:
    rule1 = if body < 10% (doji_size) of range 
    rule2 = if body < 10% ATR(n)
    is_doji = if rule1 and rule2

Arguments:
    o (pdSeries)       : Open series.
    h (pdSeries)       : High series.
    l (pdSeries)       : Low series. 
    c (pdSeries)       : Close series. 
    n_atr (int)        : Period for ATR [Default: 100]
    doji_size (float)  : % of range the body should be. [Default: 0.1]

Returns:
    pdSeries           : True, False values. 
"""