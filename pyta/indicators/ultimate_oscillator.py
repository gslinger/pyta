import pandas as pd


def ultimate_oscillator(h: pd.Series, l: pd.Series, c: pd.Series, n_fast: int = 7, n_mid: int = 14, n_slow: int = 28,
                        w_fast: float = 4.0, w_mid: float = 2.0, w_slow: float = 1.0) -> pd.Series:
    high = pd.concat([h, c.shift(1)], axis=1).max(axis=1)
    low = pd.concat([l, c.shift(1)], axis=1).min(axis=1)
    bp = c - low
    tr = high - low

    def avg(n: int) -> pd.Series:
        return bp.rolling(n).sum() / tr.rolling(n).sum()

    avg_fast = avg(n_fast)
    avg_mid = avg(n_mid)
    avg_slow = avg(n_slow)

    uo_ = 100 * ((w_fast * avg_fast) + (w_mid * avg_mid) + (w_slow * avg_slow)) / (w_fast + w_mid + w_slow)

    return uo_


ultimate_oscillator.__doc__ = """Ultimate Oscillator (UO)

A momentum oscillator which captures momentum from three different timeframes.

Source:
    https://school.stockcharts.com/doku.php?id=technical_indicators:ultimate_oscillator

Formula:
    Buying Pressure (BP) = Ct - Min(Ct-1, Lt), 
    True Range (TR) =  Max(Ht, Ct-1) - BP
    AVGf = nf Period BP sum / nf Period TR sum
    AVGm = nm Period BP sum / nm Period TR sum
    AVGs = ns Period BP sum / ns Period TR sum
    UO = 100 * [(wf * AVGf) + (wm * AVGm) + (ws * AVGs)] / (wf + wm + ws)

Arguments:
    h (pdSeries)   : High series.
    l (pdSeries)   : Low series.
    c (pdSeries)   : Close series.
    n_fast (int)   : Period for fast Avg [Default: 7]
    n_mid (int)    : Period for mid Avg [Default: 14]
    n_slow (int)   : Period for slow Avg [Default: 28]
    w_fast (float) : Weight for fast Avg [Default: 4.0]
    w_mid (float)  : Weight for mid Avg [Default: 2.0]
    w_slow (float) : Weight for slow Avg [Default: 1.0]    

Returns:
    pdSeries
"""