"""
WIP plotly CandlePlot helper class.
"""

from plotly.graph_objects import Candlestick, Bar, Scatter
from plotly.subplots import make_subplots
from pandas import Series, DataFrame


class CandlePlot(object):
    def __init__(self, df: DataFrame, name_chart: str = 'OHLC') -> None:
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

    def add_overlay(self, x, line_width=1, chart=1, line_col=None, secondary_y=False, **kwargs) -> None:
        """ Adds an overlay onto plot. Essentially the same as add_indicator, except different defaults. """
        self.fig.add_trace(
            Scatter(
                x=self.date, y=x,
                yaxis="y", xaxis="x1",
                line=dict(width=line_width,  color=line_col),
                **kwargs
            ),
            secondary_y=secondary_y,
            row=chart, col=1
        )

    def add_indicator(self, data, line_width=1, chart=2, line_col=None, name=None, secondary_y=False, **kwargs) -> None:
        """ Adds an indicator onto plot. Essentially the same as add_overlay, except different defaults. """
        self.fig.add_trace(
            Scatter(
                x=self.date, y=data,
                yaxis="y", xaxis="x1",
                line=dict(width=line_width, color=line_col),
                name=name,
                **kwargs
            ),
            secondary_y=secondary_y,
            row=chart, col=1
        )

    def add_horizontal_line(self, y, chart, secondary_y=True, **kwargs) -> None:
        """ Adds a horizontal line on specified chart at Y value. """
        self.fig.add_trace(
            Scatter(
                x=self.date,
                y=Series([y] * len(self.c)),
                yaxis="y",
                line=dict(width=1),
                **kwargs
            ),
            secondary_y=secondary_y,
            row=chart, col=1
        )

    def show(self) -> None:
        self.fig.show()
