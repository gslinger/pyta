from typing import Union
#
import pandas as pd
#
from pyta.indicators.average_true_range import average_true_range as atr
from pyta.helper import min_period, max_period


def chandelier_exit_long(h: pd.Series, l: pd.Series, c: pd.Series, n: int = 22, m: Union[float, int] = 3) \
        -> pd.Series:
    period_high: pd.Series = max_period(h, n)
    atr_: pd.Series = atr(h, l, c, n)
    c_exit_l = period_high - (atr_ * m)
    return c_exit_l


def chandelier_exit_short(h: pd.Series, l: pd.Series, c: pd.Series, n: int = 22, m: Union[float, int] = 3) \
        -> pd.Series:
    period_low: pd.Series = min_period(l, n)
    atr_: pd.Series = atr(h, l, c, n)
    c_exit_s: pd.Series = period_low + (atr_ * m)
    return c_exit_s


chandelier_exit_long.__doc__ = """Chandelier Exit (Long)

Trailing stop-loss indicator based on ATR.  

Source:
    https://school.stockcharts.com/doku.php?id=technical_indicators:chandelier_exit

Formula:
    n-Day High - ATR(n) * m 

Arguments:
    h (pdSeries) : High series.
    l (pdSeries) : Low series.
    c (pdSeries) : Close series.
    n (int)      : Period [Default: 22]
    m (int)      : Multiplier for ATR [Default: 3]

Returns:
    pdSeries
"""

chandelier_exit_short.__doc__ = """Chandelier Exit (Short)

Trailing stop-loss indicator based on ATR.  

Source:
    https://school.stockcharts.com/doku.php?id=technical_indicators:chandelier_exit

Formula:
    n-Day Low + ATR(n) * m 

Arguments:
    h (pdSeries) : High series.
    l (pdSeries) : Low series.
    c (pdSeries) : Close series.
    n (int)      : Period [Default: 22]
    m (int)      : Multiplier for ATR [Default: 3]

Returns:
    pdSeries
"""