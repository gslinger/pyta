import pandas as pd


def weighted_moving_average(x: pd.Series, n: int = 20) -> pd.Series:
    # source: https://en.wikipedia.org/wiki/Moving_average
    wma_ = \
        x.rolling(n).apply(lambda t: sum([(i + 1) * p for i, p in enumerate(t)]) / (n * (n + 1) / 2), raw=True)
    return wma_
