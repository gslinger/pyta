import pandas as pd
#
from pyta.overlays.simple_moving_average import simple_moving_average as sma


# TODO docstring.
def awesome_oscillator(h: pd.Series, l: pd.Series, n_fast: int = 5, n_slow: int = 34) -> pd.Series:
    # source: https://www.metatrader5.com/en/terminal/help/indicators/bw_indicators/awesome
    hl2: pd.Series = (h + l) / 2
    awesome_osc: pd.Series = sma(hl2, n_fast) - sma(hl2, n_slow)
    return awesome_osc
