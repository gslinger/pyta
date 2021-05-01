"""
Helper Functions. Mainly for internal use.
"""
from pandas import Series
# pyta
from .overlays.arnaud_legoux_moving_average import arnaud_legoux_moving_average as alma
from .overlays.exponential_moving_average import exponential_moving_average as ema
from .overlays.hull_moving_average import hull_moving_average as hma
from .overlays.simple_moving_average import simple_moving_average as sma
from .overlays.triple_exponential_moving_average import triple_exponential_moving_average as tema
from .overlays.weighted_moving_average import weighted_moving_average as wma
from .overlays.double_exponential_moving_aveage import double_exponential_moving_average as dema


def ma(x: Series, ma_type: str, **kwargs) -> Series:
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

