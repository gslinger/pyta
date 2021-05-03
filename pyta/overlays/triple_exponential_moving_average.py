import pandas as pd
from pyta.overlays.exponential_moving_average import exponential_moving_average as ema


def triple_exponential_moving_average(x: pd.Series, n: int = 20) -> pd.Series:
    # source: https://school.stockcharts.com/doku.php?id=technical_indicators:tema
    ema1 = ema(x, n)
    ema2 = ema(ema1, n)
    ema3 = ema(ema2, n)
    tema_ = 3 * (ema - ema2) + ema3
    return tema_
