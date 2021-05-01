from pandas import Series


def simple_moving_average(x: Series, n: int = 20) -> Series:
    sma_: Series = x.rolling(n).mean()
    return sma_
