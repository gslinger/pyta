import pandas as pd


def exponential_moving_average(x: pd.Series, n: int = 20) -> pd.Series:
    ema_ = x.ewm(span=n, min_periods=n).mean()
    return ema_
