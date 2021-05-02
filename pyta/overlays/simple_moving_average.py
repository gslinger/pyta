import pandas as pd


def simple_moving_average(x: pd.Series, n: int = 20) -> pd.Series:
    sma_: pd.Series = x.rolling(n).mean()
    return sma_
