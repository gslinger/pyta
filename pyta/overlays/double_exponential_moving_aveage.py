import pandas as pd
from pyta.overlays.exponential_moving_average import exponential_moving_average as ema


def double_exponential_moving_average(x: pd.Series, n: int = 20) -> pd.Series:
    # source: https://school.stockcharts.com/doku.php?id=technical_indicators:dema
    ema1 = ema(x, n)
    ema2 = ema(ema1, n)
    dema_ = (2 * ema1) - ema2
    return dema_
