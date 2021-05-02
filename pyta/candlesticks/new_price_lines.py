import pandas as pd
# TODO docstring


def new_price_lines(h: pd.Series, n: int = 8) -> pd.Series:
    res: pd.Series = pd.Series(h.rolling(n + 1).apply(lambda x: x.is_monotonic_increasing))
    return res


"""
n New Price Lines. n Consecutively higher highs. Usual n values = 8, 10, 12, 13.
Theoretically a bearish reversal signal, but weak performance.
"""