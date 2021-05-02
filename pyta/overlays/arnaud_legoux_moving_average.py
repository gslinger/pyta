import pandas as pd
import numpy as np


def arnaud_legoux_moving_average(x: pd.Series, n: int = 9, offset: float = 0.85, sigma: float = 6.0) -> pd.Series:
    # source: https://www.tradingview.com/pine-script-reference/#fun_alma
    m: float = offset * (n - 1)
    s: float = n / sigma
    length: int = len(x)

    alma_: pd.Series = pd.Series([np.nan] * length)
    norm: pd.Series = pd.Series([0.0] * length)
    sum_: pd.Series = norm.copy()

    for i in range(n, length):
        for j in range(n - 1):
            weight = np.exp(-1 * pow(j - m, 2) / pow(s, 2))
            norm[i] += x[i - n + j] * weight
            sum_[i] += weight
        if i != n:
            alma_[i] = norm[i] / sum_[i]

    return alma_

