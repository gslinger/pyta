from pandas import Series


def weighted_moving_average(x: Series, n: int = 20) -> Series:
    # source: https://en.wikipedia.org/wiki/Moving_average
    wma_: Series = \
        x.rolling(n).apply(lambda t: sum([(i + 1) * p for i, p in enumerate(t)]) / (n * (n + 1) / 2), raw=True)
    return wma_
