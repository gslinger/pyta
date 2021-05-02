import pandas as pd
from typing import Union


def bollinger_band_upper(price: pd.Series, n: int = 20, m: Union[int, float] = 2) -> pd.Series:
    bb_upper: pd.Series = price.rolling(n).mean() + (price.rolling(n).std(ddof=0) * m)
    return bb_upper


def bollinger_band_lower(price: pd.Series, n: int = 20, m: Union[int, float] = 2) -> pd.Series:
    bb_lower: pd.Series = price.rolling(n).mean() - (price.rolling(n).std(ddof=0) * m)
    return bb_lower


def bollinger_band_middle(price: pd.Series, n: int = 20) -> pd.Series:
    bb_middle: pd.Series = price.rolling(n).mean()
    return bb_middle


bollinger_band_middle.__doc__ = """Middle Bollinger Band

The middle bollinger band, represented by a moving average. 

Source:
    https://school.stockcharts.com/doku.php?id=technical_indicators:bollinger_bands

Formula:
    bb_middle = MA(price)

Arguments:
    price (pdSeries) : Price series (usually close). 
    n (int)          : Period for MA [Default: 20]

Returns:
    pdSeries
"""

bollinger_band_upper.__doc__ = """Upper Bollinger Band

The upper bollinger band, represented by the moving average plus m * standard deviations 

Source:
    https://school.stockcharts.com/doku.php?id=technical_indicators:bollinger_bands

Formula:
    bb_middle = MA(price) + (Std(price) * m) 

Arguments:
    price (pdSeries) : Price series (usually close). 
    n (int)          : Period for MA [Default: 20]
    m (int)          : Multiplier for StdDev [Default: 2]

Returns:
    pdSeries
"""

bollinger_band_lower.__doc__ = """Lower Bollinger Band

The lower bollinger band, represented by the moving average minus m * standard deviations 

Source:
    https://school.stockcharts.com/doku.php?id=technical_indicators:bollinger_bands

Formula:
    bb_middle = MA(price) - (Std(price) * m) 

Arguments:
    price (pdSeries) : Price series (usually close). 
    n (int)          : Period for MA [Default: 20]
    m (int)          : Multiplier for StdDev [Default: 2]

Returns:
    pdSeries
"""