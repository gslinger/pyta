import pandas as pd
from pyta.helper import ma
from pyta.plot import CandlePlot
from pyta.indicators.wip_chop_zone import chop_zone
from pyta.indicators.coppock_curve import coppock_curve
from pyta.indicators.detrended_price_oscillator import detrended_price_oscillator as dpo
from pyta.indicators.ease_of_movement import ease_of_movement as eom
from pyta.indicators.elders_force_index import elders_force_index as efi
from pyta.overlays.envelopes import envelopes
from pyta.indicators.fisher_transform import fisher_transform

if __name__ == '__main__':
    df = pd.read_csv('pyta/data/stock1.csv')[-400:].reset_index(drop=True)
    #
    ft = fisher_transform(df.High, df.Low)
    plot = CandlePlot(df)
    plot.add_indicator(ft.iloc[:, 0])
    plot.add_indicator(ft.iloc[:, 1])
    plot.show()