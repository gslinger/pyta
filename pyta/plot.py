"""
WIP plotly CandlePlot helper class.
"""

from plotly.graph_objects import Candlestick, Bar, Scatter
from plotly.subplots import make_subplots
import pandas as pd
from typing import Union


class CandlePlot(object):
    def __init__(self, df: pd.DataFrame, name_chart: str = 'OHLC') -> None:
        # Get OHLCV data
        self.date = df['Date']
        self.o = df['Open']
        self.h = df['High']
        self.l = df['Low']
        self.c = df['Close']
        self.v = df['Volume']

        # Make the base chart shape.
        self.fig = make_subplots(
            rows=3, cols=1, row_heights=[0.7, 0.15, 0.15],
            shared_xaxes=True,
            specs=[
                [{"secondary_y": True}], [{"secondary_y": True}], [{"secondary_y": True}],
            ],
            vertical_spacing=0.005,
        )

        # Set name of graph.
        self.fig.update_layout(title_text=name_chart, margin=dict(b=20, t=30, l=0, r=0))

        # Removes the range slider
        self.fig.update(layout_xaxis_rangeslider_visible=False)

        # Removes weekends from data, avoids weekend gaps. Gaps still exist for national holidays.
        self.fig.update_xaxes(rangebreaks=[dict(bounds=["sat", "mon"])])

        # Adds the OHLC Plot
        self.fig.add_trace(
            Candlestick(
                x=self.date,
                open=self.o, high=self.h, low=self.l, close=self.c,
                yaxis="y", xaxis="x1",
                name="OHLC"
            ),
            row=1, col=1
        )

        # Adds the volume plot.
        self.fig.add_trace(
            Bar(
                x=self.date, y=self.v,
                xaxis="x1",
                name='Volume'
            ),
            row=3, col=1
        )

        # Removes gridlines from chart
        # self.fig.update_xaxes(showgrid=False)
        # elf.fig.update_yaxes(showgrid=False)

        # Sets legend to be in top left of chart.
        self.fig.update_layout(
            legend=dict(
                bgcolor="rgba(0,0,0,0)",
                yanchor="top",
                y=0.99,
                xanchor="left",
                x=0.01
            )
        )

        # Adds vertical/horizontal lines protruding from cursor.
        self.fig.update_layout(hovermode="x", spikedistance=-1)
        self.fig.update_xaxes(showspikes=True, spikesnap="cursor", spikemode='across', spikethickness=0.3)
        self.fig.update_yaxes(showspikes=True, spikesnap="cursor", spikemode='across', spikethickness=0.3)
        self.fig.update_traces(xaxis="x1")

    def add_overlay(self, y: pd.Series, line_width: Union[float, int] = 1, chart: int = 1,
                    line_col: str = None, secondary_y: bool = False, **kwargs) -> None:
        """ Adds an overlay onto plot. Essentially the same as add_indicator, except different defaults. """
        self.fig.add_trace(
            Scatter(
                x=self.date, y=y,
                yaxis="y", xaxis="x1",
                line=dict(width=line_width,  color=line_col),
                **kwargs
            ),
            secondary_y=secondary_y,
            row=chart, col=1
        )

    def add_indicator(self, y: pd.Series, line_width: Union[float, int] = 1, chart: int = 2,
                      line_col: str = None, name: str = None, secondary_y: bool = False, **kwargs) -> None:
        """ Adds an indicator onto plot. Essentially the same as add_overlay, except different defaults. """
        self.fig.add_trace(
            Scatter(
                x=self.date, y=y,
                yaxis="y", xaxis="x1",
                line=dict(width=line_width, color=line_col),
                name=name,
                **kwargs
            ),
            secondary_y=secondary_y,
            row=chart, col=1
        )

    def add_horizontal_line(self, y: pd.Series, chart: int, secondary_y: bool = True, **kwargs) -> None:
        """ Adds a horizontal line on specified chart at Y value. """
        self.fig.add_trace(
            Scatter(
                x=self.date,
                y=pd.Series([y] * len(self.c)),
                yaxis="y",
                line=dict(width=1),
                **kwargs
            ),
            secondary_y=secondary_y,
            row=chart, col=1
        )

    def show(self) -> None:
        self.fig.show()



"""
Lifted from old code.
"""  # TODO REWRITE


class CandlePlotOld:
    def __init__(self, df, name_chart=None, showgrid=False):
        self._df = df
        date, o, h, l, c, v = df.Date, df.Open, df.High, df.Low, df.Close, df.Volume
        # Make the base chart shape.
        self.fig = make_subplots(rows=3, cols=1, row_heights=[0.7, 0.15, 0.15], shared_xaxes=True,
                                 specs=[[{"secondary_y": True}], [{"secondary_y": True}], [{"secondary_y": True}]],
                                 vertical_spacing=0.01)
        # Adds the OHLC Candlestick
        self.fig.add_trace(go.Candlestick(x=date, open=o, high=h, low=l, close=c, yaxis="y2", name="OHLC"), row=1,
                           col=1)
        # Removes the range slider
        self.fig.update(layout_xaxis_rangeslider_visible=False)
        # Adds the volume bar chart to bottom chart.
        self.fig.add_trace(go.Bar(x=self._df['Date'], y=self._df['Volume'], name='Volume'), row=3, col=1)
        # Removes weekends from data, avoids weekend gaps.
        self.fig.update_xaxes(rangebreaks=[dict(bounds=["sat", "mon"])])
        self.fig.update_layout(title_text=name_chart)
        self.fig.update_xaxes(showgrid=showgrid)
        self.fig.update_yaxes(showgrid=showgrid)

    def add_overlay(self, data, line_width=1, **kwargs):
        self.fig.add_trace(
            go.Scatter(
                x=self._df['Date'], y=data, yaxis="y2", line=dict(width=line_width), **kwargs),
            row=1, col=1
        )

    def add_indicator(self, data, chart, line_width=1, **kwargs):
        self.fig.add_trace(go.Scatter(x=self._df['Date'], y=data, yaxis="y2", line=dict(width=line_width), **kwargs),
                           secondary_y=True, row=chart, col=1)

    def add_horizontal_line(self, y, chart, **kwargs):
        self.fig.add_trace(
            go.Scatter(x=self._df['Date'], y=pd.Series([y] * len(self._df['Date'])), yaxis="y2", line=dict(width=1),
                       **kwargs), secondary_y=True, row=chart, col=1)

    def plot_true_vals(self, x):
        shapes = []
        for i in self._df[x == True]['Date']:
            shapes.append(go.layout.Shape(type='line', yref='paper', y0=0.2, y1=0.4, xref='x', x0=i, x1=i,
                                          line=dict(color='RoyalBlue', width=0.5)))
        self.fig.update_layout(shapes=shapes)

    def add_indicator_with_filltozero(self, data, chart, line_width=1, **kwargs):
        self.fig.add_trace(
            go.Scatter(x=self._df['Date'], y=data.clip(lower=0), yaxis="y2", line=dict(color='green', width=line_width),
                       fill='tozeroy', fillcolor='rgba(0,250,0,0.4)', **kwargs), secondary_y=True, row=chart, col=1)

        self.fig.add_trace(
            go.Scatter(x=self._df['Date'], y=data.clip(upper=0), yaxis="y2", line=dict(color='red', width=line_width),
                       fill='tozeroy', fillcolor='rgba(250,0,0,0.4)', **kwargs), secondary_y=True, row=chart, col=1)

    # Its a bit rough, the arrow sizes need to scale with the price range.
    def add_signals(self, series):
        arrow_offset = self._df.Close.mean() * 0.2
        for i in self._df[series == 1.0]['Date']:
            j = self._df.loc[self._df['Date'] == i, 'High'].values[0]
            self.fig.add_annotation(x=i, ax=i, y=j+(arrow_offset/5), ay=(j+arrow_offset),
                                    xref='x', axref='x', yref='y', ayref='y',
                                    showarrow=True, arrowhead=3, arrowsize=2, arrowwidth=1,
                                    arrowcolor='green', text='buy')
        for i in self._df[series == -1.0]['Date']:
            j = self._df.loc[self._df['Date'] == i, 'Low'].values[0]
            self.fig.add_annotation(x=i, ax=i, y=j-(arrow_offset/5), ay=(j-arrow_offset),
                                    xref='x', axref='x', yref='y', ayref='y',
                                    showarrow=True, arrowhead=3, arrowsize=2, arrowwidth=1,
                                    arrowcolor='red', text='sell')

    def show(self):
        self.fig.show()