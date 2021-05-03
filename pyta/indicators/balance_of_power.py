import pandas as pd


def balance_of_power(o: pd.Series, h: pd.Series, l: pd.Series, c: pd.Series) -> pd.Series:
    bop_ = (c - o) / (h - l)
    return bop_


balance_of_power.__doc__ = """Balance of Power (BOP)

Price-based indicator which evaluates the overall strength of buyers and sellers in the market.

Source:
    https://school.stockcharts.com/doku.php?id=technical_indicators:balance_of_power

Formula:
    BOP = (close - open) / (high - low)

Arguments:
    o (pdSeries) : Open series.
    h (pdSeries) : High series.
    l (pdSeries) : Low series.
    c (pdSeries) : Close series.

Returns:
    pdSeries
"""