import pandas as pd
#
from pyta.helper import roc
from pyta.overlays.weighted_moving_average import weighted_moving_average as wma
# TODO docstring


def coppock_curve(c: pd.Series, n_wma: int = 10, n_longroc: int = 14, n_shortroc: int = 11) -> pd.Series:
    curve = wma(roc(c, n_longroc) + roc(c, n_shortroc), n_wma)
    return curve
