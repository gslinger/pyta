"""
Chaikin Oscillator
# TODO docstring
Source: https://school.stockcharts.com/doku.php?id=technical_indicators:chaikin_oscillator
"""
import pandas as pd
#
from pyta.overlays.exponential_moving_average import exponential_moving_average as ema
from pyta.indicators.accumulation_distribution_line import accumulation_distribution_line as adl


def chaikin_oscillator(h: pd.Series, l: pd.Series, c: pd.Series, v: pd.Series, n_fast: int = 3, n_slow: int = 10) \
        -> pd.Series:
    _adl = adl(h, l, c, v)
    _co = ema(_adl, n_fast) - ema(_adl, n_slow)
    return _co
