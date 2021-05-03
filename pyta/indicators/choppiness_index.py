import pandas as pd
import numpy as np
#
from pyta.indicators.average_true_range import average_true_range as atr
from pyta.helper import highest, lowest
# TODO docstring


def choppiness_index(h: pd.Series, l: pd.Series, c: pd.Series, n: int = 14) -> pd.Series:
    atr_ = atr(h, l, c, n=1)
    ci_ = 100 * np.log10(atr_.rolling(n).sum() / (highest(h, n) - lowest(l, n))) / np.log10(n)
    return ci_
