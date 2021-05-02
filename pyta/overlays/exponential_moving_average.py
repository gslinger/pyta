import pandas as pd


def exponential_moving_average(x: pd.Series, n: int = 20) -> pd.Series:
    ema_: pd.Series = x.ewm(n, min_periods=n).mean()
    return ema_
