import pandas as pd


class Asset(object):
    def __init__(self, df: pd.DataFrame) -> None:
        self.df: pd.DateFrame = df

    def __str__(self) -> str:
        return str(self.df)

    #  Key Asset Data
    @property
    def date(self) -> pd.Series:
        return self.df.Date

    @property
    def o(self) -> pd.Series:
        return self.df.Open

    @property
    def h(self) -> pd.Series:
        return self.df.High

    @property
    def l(self) -> pd.Series:
        return self.df.Low

    @property
    def c(self) -> pd.Series:
        return self.df.Close

    @property
    def v(self) -> pd.Series:
        return self.df.Volume
