import numpy as np
import pandas as pd
#
from pyta.overlays.simple_moving_average import simple_moving_average as sma
from pyta.helper import mean_dev


def commodity_channel_index(h: pd.Series, l: pd.Series, c: pd.Series, n: int = 20, const: float = 0.015) -> pd.Series:
    tp: pd.Series = (h + l + c) / 3
    tp_sma: pd.Series = sma(tp, n)
    tp_dev: pd.Series = mean_dev(tp, n)
    cci: pd.Series = (tp - tp_sma) / (tp_dev * const)
    return cci


commodity_channel_index.__doc__ = """Commodity Channel Index (CCI)

CCI essentially measures the current price level relative to an average over a given time. 

Source:
    https://school.stockcharts.com/doku.php?id=technical_indicators:commodity_channel_index_cci

Formula:
    TP = (High + Low + Close) / 3
    CCI = (TP - SMA(n) of TP) / (const * MeanDev of TP) 

Arguments:
    h (pdSeries)  : High series.
    ; (pdSeries)  : Low series.
    c (pdSeries)  : Close series.
    n (int)       : Period for MA [Default: 20]
    const (float) : Multiplier for MeanDev [Default: 0.015]

Returns:
    pdSeries
"""