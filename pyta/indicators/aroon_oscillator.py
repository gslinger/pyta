import pandas as pd
#
from pyta.indicators.aroon_down import aroon_down
from pyta.indicators.aroon_up import aroon_up


def aroon_osc(h: pd.Series, l: pd.Series, n: int = 14) -> pd.Series:
    aroon_osc_: pd.Series = aroon_up(h, n) - aroon_down(l, n)
    return aroon_osc_


aroon_osc.__doc__ = """Aroon Oscillator

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
