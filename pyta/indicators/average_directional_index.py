import pandas as pd
import numpy as np
#
from pyta.indicators.average_true_range import average_true_range as atr
from pyta.overlays.wip_rma import rma


def minus_directional_indicator(h: pd.Series, l: pd.Series, c: pd.Series, n: int = 14) -> pd.Series:
    atr_: pd.Series = atr(h, l, c, n)
    ndm: pd.Series = pd.Series(np.where(l.shift(1) - l > h - h.shift(1), l.shift(1) - l, 0)).clip(lower=0)
    ma: pd.Series = rma(ndm, n)
    ndi: pd.Series = 100 * (ma / atr_)
    return ndi


minus_directional_indicator.__doc__ = """Minus Directional Indicator (-DI)

Measures trend over time, component of Average Directional Index (ADX)

Source:
    https://school.stockcharts.com/doku.php?id=technical_indicators:average_directional_index_adx

Formula:
    TR = True Range
    -DM = IF(Lt-1 - Lt > Ht - Ht-1, MAX(Lt-1 - Lt, 0), 0)
    -DI = (-DM / TR) * 100

Arguments:
    h (pdSeries) : High series.
    l (pdSeries) : Low series.
    c (pdSeries) : Close series.
    n (int)      : Period for DI [Default: 14]

Returns:
    pdSeries
"""


def plus_directional_indicator(h: pd.Series, l: pd.Series, c: pd.Series, n: int = 14) -> pd.Series:
    atr_ = atr(h, l, c, n)
    pdm = pd.Series(np.where(h - h.shift(1) > l.shift(1) - l, h - h.shift(1), 0)).clip(lower=0)
    ma = rma(pdm, n)
    pdi_ = 100 * (ma / atr_)
    return pdi_


plus_directional_indicator.__doc__ = """Plus Directional Indicator (+DI)

Measures trend over time, component of Average Directional Index (ADX)

Source:
    https://school.stockcharts.com/doku.php?id=technical_indicators:average_directional_index_adx

Formula:
    TR = True Range
    +DM = IF(Ht - Ht-1 > Lt-1 - Lt, MAX(Ht - Ht-1, 0), 0)
    +DI = (+DM / TR) * 100

Arguments:
    h (pdSeries) : High series.
    l (pdSeries) : Low series.
    c (pdSeries) : Close series.
    n (int)      : Period for DI [Default: 14]

Returns:
    pdSeries

"""


def average_directional_index(h: pd.Series, l: pd.Series, c: pd.Series, n_di: int = 14, n_adx: int = 14) -> pd.Series:
    pdi_: pd.Series = plus_directional_indicator(h, l, c, n_di)
    mdi_: pd.Series = minus_directional_indicator(h, l, c, n_di)
    dx: pd.Series = ((pdi_ - mdi_).abs() / (pdi_ + mdi_).abs())
    adx_: pd.Series = rma(dx, n_adx) * 100
    return adx_


average_directional_index.__doc__ = """Average Directional Index (ADX)

Smoothed Average of the difference between Plus Directional Indicator (+DI) and Minus Directional Indicator (-DI).

Source:
    https://school.stockcharts.com/doku.php?id=technical_indicators:average_directional_index_adx

Formula:
    DX = [ABS(PDI - MDI) / ABS(PDI + SUM)] 
    ADX = WilderMA(DX) * 100

Arguments:
    h (pdSeries) : High series.
    l (pdSeries) : Low series.
    c (pdSeries) : Close series.
    n_di (int)   : Period for DI [Default: 14]
    n_adx (int)  : Period for ADX [Default: 14]

Returns:
    pdSeries
"""
