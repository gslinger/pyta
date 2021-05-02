import pandas as pd
#
from pyta.candlesticks.common import shadow_top_perc, shadow_bottom_perc
from pyta.candlesticks.doji import is_doji


# TODO Maybe also compare vs a benchmark (ATR?).
def is_dragonfly_doji(o, h, l, c, b_perc=0.7, t_perc=0.15, **kwargs):
    _is_doji = is_doji(o, h, l, c, **kwargs)
    is_long_bottom_shadow = shadow_bottom_perc(o, h, l, c) > b_perc
    is_small_top_shadow = shadow_top_perc(o, h, l, c) < t_perc
    box = pd.concat([_is_doji, is_long_bottom_shadow, is_small_top_shadow], axis=1)
    return box.all(axis='columns') #todo ?


is_dragonfly_doji.__doc__ = """Identifies Dragonfly Dojis

A dragonfly doji can be a price reversal signal. It is a doji with a short top shadow and long bottom shadow. 

Source:
    https://www.amazon.co.uk/Encyclopedia-Candlestick-Charts-Wiley-Trading/dp/0470182016

Formula:
    rule1 = if is_doji 
    rule2 = if bottom_shadow > 0.7 (b_perc) * range
    rule3 = if top_shadow < 0.15 (t_perc) * range
    is_dragonfly_doji = if rule1 and rule2 and rule3  

Arguments:
    o (pdSeries)       : Open series.
    h (pdSeries)       : High series.
    l (pdSeries)       : Low series. 
    c (pdSeries)       : Close series. 
    b_perc (float)     : % of range the bottom shadow should be [Default: 0.7]
    t_perc (float)     : % of range the top shadow should be. [Default 0.15]

Kwargs:
    TODO

Returns:
    pdSeries
"""