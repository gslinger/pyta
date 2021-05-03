import pandas as pd
#
from pyta.indicators.aroon import aroon_down, aroon_up


def aroon_oscillator(h: pd.Series, l: pd.Series, n: int = 14) -> pd.Series:
    aroon_osc_ = aroon_up(h, n) - aroon_down(l, n)
    return aroon_osc_


aroon_oscillator.__doc__ = """Aroon Oscillator

Measures the difference between Aroon up and Aroon down. 

Source:
    https://school.stockcharts.com/doku.php?id=technical_indicators:aroon_oscillator

Formula:
    AO = AroonUp - AroonDown

Arguments:
    h (pdSeries) : High series.
    l (pdSeries) : Low series.
    n (int)      : Period for Aroon [Default: 25]

Returns:
    pdSeries
"""
