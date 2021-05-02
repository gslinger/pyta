"""
Helper Functions. Mainly for internal use.
"""
import pandas as pd
from typing import Union
# pyta
from .overlays.arnaud_legoux_moving_average import arnaud_legoux_moving_average as alma
from .overlays.exponential_moving_average import exponential_moving_average as ema
from .overlays.hull_moving_average import hull_moving_average as hma
from .overlays.simple_moving_average import simple_moving_average as sma
from .overlays.triple_exponential_moving_average import triple_exponential_moving_average as tema
from .overlays.weighted_moving_average import weighted_moving_average as wma
from .overlays.double_exponential_moving_aveage import double_exponential_moving_average as dema


def ma(x: pd.Series, ma_type: str, **kwargs) -> pd.Series:
    fnc_map: dict = {
        'alma': alma,
        'dema': dema,
        'ema': ema,
        'hma': hma,
        'sma': sma,
        'tema': tema,
        'wma': wma,
    }
    # TODO check if in dict, if not list dict options and ValueError
    return fnc_map[ma_type](x, **kwargs)


def mfm(h: pd.Series, l: pd.Series, c: pd.Series) -> pd.Series:
    # source: https://school.stockcharts.com/doku.php?id=technical_indicators:accumulation_distribution_line
    mfm_: pd.Series = ((c - l) - (h - c)) / (h - l)
    return mfm_


def mfv(h: pd.Series, l: pd.Series, c: pd.Series, v: pd.Series) -> pd.Series:
    # source: https://school.stockcharts.com/doku.php?id=technical_indicators:accumulation_distribution_line
    mfv_: pd.Series = mfm(h, l, c) * v
    return mfv_


def tr(h: pd.Series, l: pd.Series, c: pd.Series) -> pd.Series:
    # source: https://school.stockcharts.com/doku.php?id=technical_indicators:average_true_range_atr
    tr_ = pd.concat([h - l, abs(h - c.shift(1)), abs(l - c.shift(1))], axis=1).max(axis=1)
    return tr_



