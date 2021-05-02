import pandas as pd
import numpy as np
#
from pyta.indicators.average_true_range import average_true_range as atr
from pyta.helper import max_period, min_period
# TODO docstring


def choppiness_index(h: pd.Series, l: pd.Series, c: pd.Series, n: int = 14) -> pd.Series:
    atr_: pd.Series = atr(h, l, c, n=1)
    ci_: pd.Series = 100 * np.log10(atr_.rolling(n).sum() / (max_period(h, n) - min_period(l, n))) / np.log10(n)
    return ci_
