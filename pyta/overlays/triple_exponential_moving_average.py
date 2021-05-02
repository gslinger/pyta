import pandas as pd
from pyta.overlays.exponential_moving_average import exponential_moving_average as ema


def triple_exponential_moving_average(x: pd.Series, n: int = 20) -> pd.Series:
    # source: https://school.stockcharts.com/doku.php?id=technical_indicators:tema
    ema1: pd.Series = ema(x, n)
    ema2: pd.Series = ema(ema1, n)
    ema3: pd.Series = ema(ema2, n)
    tema_: pd.Series = 3 * (ema - ema2) + ema3
    return tema_
