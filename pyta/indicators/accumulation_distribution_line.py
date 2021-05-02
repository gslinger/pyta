import pandas as pd
#
from pyta.helper import mfv


def accumulation_distribution_line(h: pd.Series, l: pd.Series, c: pd.Series, v: pd.Series):
    mfv_: pd.Series = mfv(h, l, c, v)
    adl_: pd.Series = mfv_.cumsum()
    return adl_


accumulation_distribution_line.__doc__ = """Accumulation Distribution Line (ADL)

Provides a gauge of how strong the buy/selling is in a period. Used by CMF, ADL, etc.  

Source:
    https://school.stockcharts.com/doku.php?id=technical_indicators:accumulation_distribution_line

Formula:
    MFM = [(Close  -  Low) - (High - Close)] / (High - Low)
    MFV = MFM * Volume
    ADL = CumSum(MFV)

Arguments:
    h (pdSeries) : High series.
    l (pdSeries) : Low series.
    c (pdSeries) : Close series.
    v (pdSeries) : Volume series.

Returns:
    pdSeries
"""