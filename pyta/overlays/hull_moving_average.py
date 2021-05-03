import pandas as pd
from pyta.overlays.weighted_moving_average import weighted_moving_average as wma


def hull_moving_average(x: pd.Series, n: int = 20) -> pd.Series:
    wma1 = wma(x, int(n / 2))
    wma2 = wma(x, n)
    raw_hma = 2 * wma1 - wma2
    hma_ = wma(raw_hma, int(n ** 0.5))
    return hma_
