# TODO Don't actually know the full name for this moving average...
import pandas as pd


def rma(x: pd.Series, n: int = 20) -> pd.Series:
    # source: https://www.tradingview.com/pine-script-reference/#fun_rma
    rma_ = x.ewm(alpha=(1 / n), min_periods=n).mean()
    return rma_
