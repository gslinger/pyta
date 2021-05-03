import pandas as pd
import numpy as np
#
from pyta.helper import highest, lowest
# TODO not correct


def fisher_transform(h: pd.Series, l: pd.Series, n: int = 9) -> pd.DataFrame:
    hl2 = (h + l) / 2
    high = highest(hl2, n)
    low = lowest(hl2, n)

    value_temp = pd.Series([0] * len(h))
    fish1 = value_temp.copy()
    x = ((hl2 - low) / (high - low) - 0.5)
    y = 0.67 * value_temp.shift(1)
    value_temp = 0.67 * value_temp.shift(1)
    #value_temp = 0.66 * ((hl2 - low) / (high - low) - 0.5) + 0.67 * value_temp.shift(1)
    value = pd.Series(np.where(value_temp > 0.99, 0.999, np.where(value_temp < -0.99, -0.999, value_temp)))

    fish1 = 0.5 * np.log((1 + value) / (1 - value)) + 0.5 * fish1.shift(1)
    fish2 = fish1.shift(1)

    fish1.name = f'Fisher_Base({n})'
    fish2.name = f'Fisher_Lag({n})'

    fisher_trans = pd.concat([value_temp, fish2], axis=1)
    return fisher_trans



