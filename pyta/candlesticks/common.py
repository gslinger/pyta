import pandas as pd


# Calculates the percentage of the bottom shadow relative to the whole candle.
def shadow_bottom_perc(o: pd.Series, h: pd.Series, l: pd.Series, c: pd.Series) -> pd.Series:
    bot_size: pd.Series = shadow_bottom(o, h, l, c)
    bot_perc: pd.Series = bot_size / (h - l)
    return bot_perc


# Calculates the percentage of the top shadow relative to the whole candle.
def shadow_top_perc(o: pd.Series, h: pd.Series, l: pd.Series, c: pd.Series) -> pd.Series:
    top_size: pd.Series = shadow_top(o, h, l, c)
    top_perc: pd.Series = top_size / (h - l)
    return top_perc


# Measures length of lower shadow. min(open, close) - low
def shadow_bottom(o: pd.Series, h: pd.Series, l: pd.Series, c: pd.Series) -> pd.Series:
    bot_shadow: pd.Series = pd.concat([o, c], axis=1).min(axis=1) - l
    return bot_shadow


# Measures length of upper shadow. high - max(open, close)
def shadow_top(o: pd.Series, h: pd.Series, l: pd.Series, c: pd.Series) -> pd.Series:
    top_shadow: pd.Series = h - pd.concat([o, c], axis=1).max(axis=1)
    return top_shadow
