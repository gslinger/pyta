import pandas as pd
#
from pyta.overlays.simple_moving_average import simple_moving_average as sma
from pyta.helper import roc
# todo merge?
# TODO docstring


def know_sure_thing(c: pd.Series, n_roc1: int = 10, n_roc2: int = 15, n_roc3: int = 20, n_roc4: int = 30,
                    n_sma1: int = 10, n_sma2: int = 10, n_sma3: int = 10, n_sma4: int = 14) -> pd.Series:
    def smaroc(n_roc: int, n_sma: int) -> pd.Series:
        return sma(roc(c, n_roc), n_sma)

    kst: pd.Series = smaroc(n_roc1, n_sma1) + 2 * smaroc(n_roc2, n_sma2) + 3 * smaroc(n_roc3, n_sma3) + 4 * smaroc(
        n_roc4, n_sma4)
    return kst


def know_sure_thing_signal(c: pd.Series, n_roc1: int = 10, n_roc2: int = 15, n_roc3: int = 20, n_roc4: int = 30,
                           n_sma1: int = 10, n_sma2: int = 10, n_sma3: int = 10, n_sma4: int = 14,
                           n_sig: int = 9) -> pd.Series:
    kst: pd.Series = know_sure_thing(c, n_roc1, n_roc2, n_roc3, n_roc4, n_sma1, n_sma2, n_sma3, n_sma4)
    return sma(kst, n_sig)
