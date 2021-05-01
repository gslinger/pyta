from pandas import Series
from pyta.overlays.exponential_moving_average import exponential_moving_average as ema


def triple_exponential_moving_average(x: Series, n: int = 20) -> Series:
    # source: https://school.stockcharts.com/doku.php?id=technical_indicators:tema
    ema1: Series = ema(x, n)
    ema2: Series = ema(ema1, n)
    ema3: Series = ema(ema2, n)
    tema_: Series = 3 * (ema - ema2) + ema3
    return tema_
