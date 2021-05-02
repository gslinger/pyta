import pandas as pd


def aroon_up(h: pd.Series, n: int = 14) -> pd.Series:
    a_up: pd.Series = h.rolling(n + 1).apply(lambda x: 100 * x.tolist().index(max(x)) / float(n))
    return a_up


aroon_up.__doc__ = """Aroon Upper

Measures the number of periods since last x-day high 

Source:
    https://school.stockcharts.com/doku.php?id=technical_indicators:aroon

Formula:
    AroonUp = 100 * [Index of max in period] / n

Arguments:
    h (pdSeries) : High series.
    n (int)      : Period for Aroon [Default: 14]

Returns:
    pdSeries
"""