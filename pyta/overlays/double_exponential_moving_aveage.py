from pandas import Series
from pyta.overlays.exponential_moving_average import exponential_moving_average as ema


def double_exponential_moving_average(x: Series, n: int = 20) -> Series:
    # source: https://school.stockcharts.com/doku.php?id=technical_indicators:dema
    ema1: Series = ema(x, n)
    ema2: Series = ema(ema1, n)
    dema_: Series = (2 * ema1) - ema2
    return dema_
