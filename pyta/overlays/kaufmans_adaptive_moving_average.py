import pandas as pd
import numpy as np
#
from pyta.helper import er


def kaufmans_adaptive_moving_average(c: pd.Series, n: int = 10, n_fast: int = 2, n_slow: int = 30) -> pd.Series:
    er_: pd.Series = er(c, n)
    # SC = [ER x (2/(2+1) - 2/(30+1)) + 2/(30+1)]2
    fast_ema: float = 2 / (n_fast + 1)
    slow_ema: float = 2 / (n_slow + 1)
    sc: pd.Series = (er_ * (fast_ema - slow_ema) + slow_ema) ** 2
    kama: pd.Series = pd.Series([np.nan] * (len(c) - 1))
    # First kama entry is close price.
    kama[n - 1] = c[n - 1]
    # KAMA = Prior KAMA + SC x (Price - Prior KAMA)
    for i in range(n, len(c)):
        kama[i] = (kama[i - 1] + sc[i] * (c[i] - kama[i - 1]))
    return kama


kaufmans_adaptive_moving_average.__doc__ = """Kaufman's Adaptive Moving Average (KAMA)

A moving average that accounts for volatility and market noise. 

Source:
    https://school.stockcharts.com/doku.php?id=technical_indicators:kaufman_s_adaptive_moving_average

Formula:
    ER = Change / Volatility
    SC = [ER * (2 / (n_fast + 1) - 2 / (n_slow + 1)) + 2 / (n_slow + 1)] ** 2
    KAMA = Prior KAMA + SC x (Price - Prior KAMA)

Arguments:
    c (pdSeries) : Close series.
    n (int)      : Periods for ER [Default: 10]
    n_fast (int) : Periods for fast SC [Default: 2]
    n_slow (int) : Periods for slow SC [Default: 30]

Returns:
    pdSeries
"""