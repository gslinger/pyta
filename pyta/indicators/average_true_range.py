import pandas as pd
#
from pyta.overlays.wip_rma import rma
from pyta.helper import tr

# TODO MA()


def average_true_range(h: pd.Series, l: pd.Series, c: pd.Series, n: int = 14) -> pd.Series:
    atr_: pd.Series = rma(tr(h, l, c), n)
    return atr_


average_true_range.__doc__ = """Average True Range (ATR)

Moving average of the True Range, measures volatility.

Source:
    https://school.stockcharts.com/doku.php?id=technical_indicators:average_true_range_atr

Formula:
    ATR = EMA(TR) [Alpha = 1 / n] 

Arguments:
    h (pdSeries) : High series.
    l (pdSeries) : Low series.
    c (pdSeries) : Close series.
    n (int)      : Period for MA [Default:14]

Returns:
    pdSeries
"""