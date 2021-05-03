import numpy as np
import pandas as pd
#
from pyta.overlays.exponential_moving_average import exponential_moving_average as ema


def klinger_volume_oscillator(h: pd.Series, l: pd.Series, c: pd.Series, v: pd.Series,
                              n_fast: int = 34, n_slow: int = 55) -> pd.Series:
    mom: pd.Series = (h + l + c).diff(1)
    trend = np.where(mom > 0, 1, 0) + np.where(mom < 0, -1, 0) # todo type
    dm: pd.Series = h - l

    cm = [0.0] * len(h) # todo type
    for i in range(1, len(h)):
        cm[i] = (cm[i - 1] + dm[i]) if trend[i] == trend[i - 1] else (dm[i - 1] + dm[i])

    vf: pd.Series = v * trend * abs(dm / cm * 2 - 1) * 100

    kvo_: pd.Series = ema(vf, n_fast) - ema(vf, n_slow)
    return kvo_


klinger_volume_oscillator.__doc__ = """"Klinger Volume Oscillator (KVO)
    This indicator was developed by Stephen J. Klinger. It is designed to predict price reversals in a market 
    by comparing volume to price. 

Source:
    https://www.tradingview.com/script/Qnn7ymRK-Klinger-Volume-Oscillator/

Formula:
    HLC3 = (h + l + c) / 3
    MOM = HLC3t - HLC3t-1
    TREND = { 1   if MOM > 0  \
             -1   if MOM < 0  \
              0   otherwise
    DM = h - l
    CM = { CMt-1 + DMt  if TRENDt == TRENDt-1   \
           DMt-1 + DMt  otherwise
    vf = 100 * v * TREND * abs(2 * dm / cm - 1) 
    kvo = ema(vf, fast) - ema(vf, slow)

Arguments:
    h (pdSeries) : High series.
    l (pdSeries) : Low series.
    c (pdSeries) : Close series.
    v (pdSeries) : Volume series.
    n_fast (int) : Period for fast EMA [Default: 34]
    n_slow (int) : Period for slow EMA [Default: 55]

Returns:
    pdSeries
"""


def klinger_volume_oscillator_signal(h: pd.Series, l: pd.Series, c: pd.Series, v: pd.Series,
                                     n_fast: int = 34, n_slow: int = 55, n_signal: int = 13,
                                     kvo: pd.Series = None) -> pd.Series:
    kvo_ = klinger_volume_oscillator(h, l, c, v, n_fast, n_slow) if not kvo else kvo
    kvo_signal = kvo_.ewm(alpha=2 / (n_signal + 1), min_periods=n_signal).mean()
    return kvo_signal


klinger_volume_oscillator_signal.__doc__ = """"Klinger Volume Oscillator (KVO)
    Signal line for KVO. 

Source:
    https://www.tradingview.com/script/Qnn7ymRK-Klinger-Volume-Oscillator/

Calculation:
    kvo_signal = ema(kvo, n_signal)

Arguments:
    h (pdSeries)   : High series.
    l (pdSeries)   : Low series.
    c (pdSeries)   : Close series.
    v (pdSeries)   : Volume series.
    n_fast (int)   : Period for fast EMA [Default: 34]
    n_slow (int)   : Period for slow EMA [Default: 55]
    n_signal (int) : Period for Signal [Default: 13]

Returns:
    pdSeries
"""