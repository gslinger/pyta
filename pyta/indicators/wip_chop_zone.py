import numpy as np
import pandas as pd
#
from pyta.helper import highest, lowest, hlc3
from pyta.overlays.exponential_moving_average import exponential_moving_average as ema


# TODO incomplete
def chop_zone(h: pd.Series, l: pd.Series, c: pd.Series, n: int = 30, n_ema: int = 34):
    period_high = highest(h, n)
    period_low = lowest(l, n)
    avg = hlc3(h, l, c)
    range_ = 25 / (period_high - period_low) * period_low
    ema_ = ema(c, n)
    x1_ema = 0
    x2_ema = 1
    y1_ema = 0
    y2_ema = (ema_.shift(1) - ema_) / avg * range_
    c_ema = np.sqrt((x2_ema - x1_ema) * (x2_ema - x1_ema) + (y2_ema - y1_ema) * (y2_ema - y1_ema))
    ema_angle_temp = round(180 * np.arccos((x2_ema - x1_ema) / c_ema) / np.pi)
    ema_angle = pd.Series(np.where(y2_ema > 0, -ema_angle_temp, ema_angle_temp))

    colours = [
        'yellow', 'darkred', 'red', 'orange', 'lightorange', 'lime', 'palegreen', 'darkgreen', 'turquoise', 'yellow'
    ]

    bins = np.array([-180, -5, -3.57, -2.14, -0.71, 0.71, 2.14, 3.57, 5, 180])

    chop_zone_colours = pd.Series(np.digitize(ema_angle, bins=bins))

    df = pd.concat([ema_angle, chop_zone_colours], axis=1)

    return ema_angle, chop_zone_colours
