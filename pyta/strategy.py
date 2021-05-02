"""
TODO need to rewrite this, lifted from old code..
"""

import pandas as pd
import numpy as np
from pyta.asset import Asset
from pyta.plot import CandlePlot


class MovingAverageCrossover(object):
    """
    basic sma strategy for e.g.
    if sma short crosses sma long from below = buy
    if sma short crosses sma long from above = sell
    """
    def __init__(self, df: pd.DataFrame, n_fast: int, n_slow: int) -> None:
        self.df: pd.DataFrame = df
        self.asset: Asset = Asset(df)
        self.n_fast: int = n_fast
        self.n_slow: int = n_slow
        self.df['Signal'] = np.where(self.asset.sma(n_fast) > self.asset.sma(n_slow), 1.0, 0.0)
        self.df['Position'] = self.df['Signal'].diff()

    def plot_signals(self) -> None:
        plot = CandlePlot(df)
        plot.add_overlay(self.asset.sma(self.n_fast), name=f"SMA({self.n_fast})")
        plot.add_overlay(self.asset.sma(self.n_slow), name=f"SMA({self.n_slow})")
        #plot.add_signals(self.df['Position'])
        plot.show()


if __name__ == '__main__':
    df = pd.read_csv('ignore/AAPL.csv')[-300:]
    aapl = Asset(df)
    mac = MovingAverageCrossover(df, 10, 20)
    mac.plot_signals()