import numpy as np
import pandas as pd
# TODO docstring
# TODO could make a trend function to do lines 8, 9, 10


def chande_momentum_oscillator(c: pd.Series, n: int = 9) -> pd.Series:
    mom: pd.Series = c.diff(1)
    pos_mom: pd.Series = pd.Series(np.where(mom >= 0.0, mom, 0.0))
    neg_mom: pd.Series = pd.Series(np.where(mom >= 0.0, 0.0, -mom))
    pos_sum: pd.Series = pos_mom.rolling(n).sum()
    neg_sum: pd.Series = neg_mom.rolling(n).sum()
    _cmo: pd.Series = 100 * ((pos_sum - neg_sum) / (pos_sum + neg_sum))
    return _cmo


"""
length = input(9, minval=1)
src = input(close, "Source", type = input.source)
momm = change(src)
f1(m) => m >= 0.0 ? m : 0.0
f2(m) => m >= 0.0 ? 0.0 : -m
m1 = f1(momm)
m2 = f2(momm)
sm1 = sum(m1, length)
sm2 = sum(m2, length)
percent(nom, div) => 100 * nom / div
chandeMO = percent(sm1-sm2, sm1+sm2)

"""