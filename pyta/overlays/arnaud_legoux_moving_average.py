from pandas import Series
from numpy import nan as NaN, exp


def arnaud_legoux_moving_average(x: Series, n: int = 9, offset: float = 0.85, sigma: float = 6.0) -> Series:
    # source: https://www.tradingview.com/pine-script-reference/#fun_alma
    m: float = offset * (n - 1)
    s: float = n / sigma
    length: int = len(x)

    alma_: Series = Series([NaN] * length)
    norm: Series = Series([0.0] * length)
    sum_: Series = Series([0.0] * length)

    for i in range(n, length):
        for j in range(n - 1):
            weight = exp(-1 * pow(j - m, 2) / pow(s, 2)) # todo what vtype
            norm[i] += x[i - n + j] * weight
            sum_[i] += weight
        if i != n:
            alma_[i] = norm[i] / sum_[i]

    return alma_
