from pandas import Series
from pyta.overlays.weighted_moving_average import weighted_moving_average as wma


def hull_moving_average(x: Series, n: int = 20) -> Series:
    wma1: Series = wma(x, int(n / 2))
    wma2: Series = wma(x, n)
    raw_hma: Series = 2 * wma1 - wma2
    hma_: Series = wma(raw_hma, int(n ** 0.5))
    return hma_
