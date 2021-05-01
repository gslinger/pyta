from pandas import Series


def exponential_moving_average(x: Series, n: int = 20) -> Series:
    ema_: Series = x.ewm(n, min_periods=n).mean()
    return ema_
