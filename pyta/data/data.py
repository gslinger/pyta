import yfinance as yf
import pandas as pd


def ticker_to_csv(ticker, start, end, name=None):
    name = ticker if not name else name
    df = yf.download(ticker, start=start, end=end)
    df.to_csv(f"{name}.csv")


# if __name__ == '__main__':
    # ticker_to_csv('AAPL', start='2015-01-01', end='2021-01-01', name='stock1')
    # ticker_to_csv('MSFT', start='2015-01-01', end='2021-01-01', name='stock2')
    df = pd.read_csv(f'stock1.csv')[-300:]

