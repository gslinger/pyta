# TODO MACD histo
# TODO docstring
# TODO merge?
import pandas as pd
#
from pyta.overlays.exponential_moving_average import exponential_moving_average as ema
from pyta.indicators.absolute_price_oscillator import absolute_price_oscillator as apo


def moving_average_convergence_divergence(c: pd.Series, fast_n: int = 12, slow_n: int = 26) -> pd.Series:
    return apo(c, fast_n, slow_n)


def moving_average_convergence_divergence_signal(c: pd.Series, fast_n: int = 12, slow_n: int = 26,
                                                 macd_n: int = 9) -> pd.Series:
    macd = apo(c, fast_n, slow_n)
    return ema(macd, macd_n)
