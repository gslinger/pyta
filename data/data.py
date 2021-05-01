import yfinance as yf
import pandas as pd


def ticker_to_csv(ticker, start, end, name=None):
    name = ticker if not name else name
    df = yf.download(ticker, start=start, end=end)
    df.to_csv(f"{name}.csv")


class SampleData(object):
    def __init__(self, stock=1):
        self.df = pd.read_csv(f'stock{stock}.csv')[-300:]
        self.date = self.df.Date
        self.open = self.df.Open
        self.high = self.df.High
        self.low = self.df.Low
        self.close = self.df.Close
        self.volume = self.df.Volume
        self.adjclose = self.df['Adj Close']

    def __str__(self):
        return str(self.df)


# if __name__ == '__main__':
    # ticker_to_csv('AAPL', start='2015-01-01', end='2021-01-01', name='stock1')
    # ticker_to_csv('MSFT', start='2015-01-01', end='2021-01-01', name='stock2')

