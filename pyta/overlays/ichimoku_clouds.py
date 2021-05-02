import pandas as pd
#
from pyta.helper import lowest, highest
# TODO docstring


# Tenkan-sen (Conversion Line): (9-period high + 9-period low)/2))
def tenkan_sen(h: pd.Series, l: pd.Series, n=9) -> pd.Series:
    tenkansen: pd.Series = (highest(h, n) + lowest(l, n)) / 2
    return tenkansen


# Kijun-sen (Base Line): (26-period high + 26-period low)/2))
def kijun_sen(h: pd.Series, l: pd.Series, n=26) -> pd.Series:
    kijunsen: pd.Series = (highest(h, n) + lowest(l, n)) / 2
    return kijunsen


# Senkou Span A (Leading Span A): (Conversion Line + Base Line)/2))
def senkou_span_a(h: pd.Series, l: pd.Series, n_conv=9, n_base=26) -> pd.Series:
    conv_line: pd.Series = tenkan_sen(h, l, n_conv)
    base_line: pd.Series = kijun_sen(h, l, n_base)
    senkouspana: pd.Series = (conv_line + base_line) / 2
    return senkouspana


# Senkou Span B (Leading Span B): (52-period high + 52-period low)/2))
def senkou_span_b(h: pd.Series, l: pd.Series, n=52) -> pd.Series:
    senkouspanb: pd.Series = (highest(h, n) + lowest(l, n)) / 2
    return senkouspanb


# Chikou Span (Lagging Span): Close plotted 26 days in the past
def chikou_span(c: pd.Series, n=26) -> pd.Series:
    chikouspan: pd.Series = c.shift(n)
    return chikouspan
