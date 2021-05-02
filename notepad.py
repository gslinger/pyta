import pandas as pd
from pyta.helper import ma
from pyta.plot import CandlePlot


if __name__ == '__main__':
    df = pd.read_csv('pyta/data/stock1.csv')[-400:].reset_index(drop=True)
    #
    print(ma(df.Close, 'alma'))
