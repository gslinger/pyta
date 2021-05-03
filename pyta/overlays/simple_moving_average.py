import pandas as pd


def simple_moving_average(x: pd.Series, n: int = 20) -> pd.Series:
    sma_ = x.rolling(n).mean()
    return sma_
