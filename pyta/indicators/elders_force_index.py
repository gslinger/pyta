import pandas as pd
#
from pyta.helper import ma
from pyta.overlays.exponential_moving_average import exponential_moving_average as ema


def elders_force_index(c: pd.Series, v: pd.Series, n: int = 13) -> pd.Series:
    efi_: pd.Series = ema(c.diff(1) * v, n)
    return efi_
