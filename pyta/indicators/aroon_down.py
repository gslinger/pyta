import pandas as pd


def aroon_down(l: pd.Series, n: int = 14) -> pd.Series:
    a_down: pd.Series = l.rolling(n + 1).apply(lambda x: 100 * x.tolist().index(min(x)) / float(n))
    return a_down


aroon_down.__doc__ = """Aroon Down

Measures the number of periods since last x-day low.

Source:
    https://school.stockcharts.com/doku.php?id=technical_indicators:aroon

Formula:
    AroonUp = 100 * [Index of min in period] / n

Arguments:
    l (pdSeries) : Low series.
    n (int)      : Period for Aroon [Default: 14]

Returns:
    pdSeries
"""