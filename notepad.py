import pandas as pd
from pyta.helper import ma
from pyta.plot import CandlePlot
from pyta.indicators.wip_chop_zone import chop_zone
from pyta.indicators.coppock_curve import coppock_curve
from pyta.indicators.detrended_price_oscillator import detrended_price_oscillator as dpo

if __name__ == '__main__':
    df = pd.read_csv('pyta/data/stock1.csv')[-400:].reset_index(drop=True)
    #
    ci = dpo(df.Close)
    plot = CandlePlot(df)
    plot.add_indicator(ci)
    plot.show()