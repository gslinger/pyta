# TODO Don't actually know the full name for this moving average...
from pandas import Series


def rma(x: Series, n: int = 20) -> Series:
    # source: https://www.tradingview.com/pine-script-reference/#fun_rma
    rma_: Series = x.ewm(alpha=(1 / n), min_periods=n).mean()
    return rma_
