import pandas as pd
#
from pyta.helper import mfv


def chaikin_money_flow(h: pd.Series, l: pd.Series, c: pd.Series, v: pd.Series, n: int = 20) -> pd.Series:
    _mfv: pd.Series = mfv(h, l, c, v)
    _cmf: pd.Series = _mfv.rolling(n).sum() / v.rolling(n).sum()
    return _cmf


chaikin_money_flow.__doc__ = """Chaikin Money Flow (CMF)

Measures the amount of Money Flow Volume over a specified period. 

Source:
    https://school.stockcharts.com/doku.php?id=technical_indicators:chaikin_money_flow_cmf

Formula:
    MFV = Money Flow Volume
    CMF = n-Period sum of MFV / n-Period sum of Volume

Arguments:
    h (pdSeries)  : High series.
    l (pdSeries)  : Low series.
    c (pdSeries)  : Close series.
    v (pdSeries)  : Volume series.
    n (int)       : Period for CMF [Default: 20]

Returns:
    pdSeries
"""
