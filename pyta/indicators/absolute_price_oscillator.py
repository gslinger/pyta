import pandas as pd
#
from pyta.helper import ma
from pyta.overlays.exponential_moving_average import exponential_moving_average as ema


# TODO need to set up ma() properly..
def absolute_price_oscillator(price: pd.Series, n_fast: int = 10, n_slow: int = 20, ma_type: str = 'ema', **kwargs) -> pd.Series:
    fast_ema = ema(price, n_fast)
    slow_ema = ema(price, n_slow)
    apo_ = fast_ema - slow_ema
    return apo_


absolute_price_oscillator.__doc__ = """Absolute Price Oscillator (APO)

Displays the difference between two moving averages, typically EMA. 

Source:
    https://www.tradingview.com/script/iTI4ABSq-Absolute-Price-Oscillator-APO/

Formula:
    MAfast - MAslow

Arguments:
    c (pdSeries) : Close series.
    n_fast (int)  : Period for fast MA [Default: 10]
    n_slow (int) : Period for slow MA [Default: 20]

Returns:
    pdSeries
"""