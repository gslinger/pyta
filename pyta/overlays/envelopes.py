import pandas as pd
#
from pyta.overlays.exponential_moving_average import exponential_moving_average as ema
from pyta.helper import ma


def envelopes(price: pd.Series, n: int = 20, percent: float = 0.1) -> pd.DataFrame:
    basis: pd.Series = ma(price, 'ema', n=n)
    upper: pd.Series = basis * (1 + percent)
    lower: pd.Series = basis * (1 - percent)

    basis.name = f'Env_Basis({n}, {percent})'
    upper.name = f'Env_Upper({n}, {percent})'
    lower.name = f'Env_Lower({n}, {percent})'

    envelopes_ = pd.concat([basis, upper, lower], axis=1)
    return envelopes_
