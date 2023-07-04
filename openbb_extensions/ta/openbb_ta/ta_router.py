from typing import List, Literal, Optional

import pandas as pd
from builtin_extensions.common.ta import ta_helpers
from builtin_extensions.common.utils import (
    from_dataframe,
    get_target_column,
    get_target_columns,
    to_dataframe,
)
from openbb_provider.model.abstract.data import Data
from openbb_sdk_core.app.model.command_output import CommandOutput
from openbb_sdk_core.app.model.export.plotly import Plotly
from openbb_sdk_core.app.model.item.empty import Empty
from openbb_sdk_core.app.router import Router
from openbb_sdk_core.plots.plots import YTimeSeries, plot_timeseries
from pydantic import NonNegativeFloat, NonNegativeInt, PositiveFloat, PositiveInt

# TODO: Split this into multiple files

# pylint: disable=too-many-lines


router = Router(prefix="")


@router.command(methods=["POST"])
def atr(
    data: List[Data],
    index: str = "date",
    length: PositiveInt = 14,
    mamode: Literal["rma", "ema", "sma", "wma"] = "rma",
    drift: NonNegativeInt = 1,
    offset: int = 0,
) -> CommandOutput[List[Data]]:
    """
    Averge True Range is used to measure volatility, especially volatility caused by
    gaps or limit moves.

    Parameters
    ----------
    data : List[Data]
        List of data to apply the indicator to.
    index : str, optional
        Index column name, by default "date"
    length : PositiveInt, optional
        It's period, by default 14
    mamode : Literal["rma", "ema", "sma", "wma"], optional
        Moving average mode, by default "rma"
    drift : NonNegativeInt, optional
        The difference period, by default 1
    offset : int, optional
        How many periods to offset the result, by default 0

    Returns
    -------
    CommandOutput[List[Data]]
        List of data with the indicator applied.

    Examples
    --------
    >>> from openbb_sdk_core import openbb
    >>> stock_data = openbb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp").output
    >>> atr_data = openbb.ta.atr(data=stock_data.item)
    """

    df = to_dataframe(data, index=index)
    df_target = get_target_columns(df, ["high", "low", "close"])
    df_atr = pd.DataFrame(
        df_target.ta.atr(length=length, mamode=mamode, drift=drift, offset=offset)
    )

    item = from_dataframe(df_target.join(df_atr, how="left"), index=True)

    return CommandOutput(item=item)


@router.command(methods=["POST"])
def fib(
    data: List[Data],
    index: str = "date",
    close_column: Literal["close", "adj_close"] = "close",
    period: PositiveInt = 120,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
) -> CommandOutput[List[Data]]:
    """
    Fibonacci Retracement Levels.

    Parameters
    ----------
    data : List[Data]
        List of data to apply the indicator to.
    index : str, optional
        Index column name, by default "date"
    period : PositiveInt, optional
        Period to calculate the indicator, by default 120

    Returns
    -------
    CommandOutput[List[Data]]
        List of data with the indicator applied.

    Examples
    --------
    >>> from openbb_sdk_core import openbb
    >>> stock_data = openbb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp").output
    >>> fib_data = openbb.ta.fib(data=stock_data.item, period=120)
    """

    df = to_dataframe(data, index=index)

    (
        df_fib,
        min_date,
        max_date,
        min_pr,
        max_pr,
        lvl_text,
    ) = ta_helpers.calculate_fib_levels(
        data=df,
        close_col=close_column,
        limit=period,
        start_date=start_date,
        end_date=end_date,
    )

    df_fib["min_date"] = min_date
    df_fib["max_date"] = max_date
    df_fib["min_pr"] = min_pr
    df_fib["max_pr"] = max_pr
    df_fib["lvl_text"] = lvl_text

    item = from_dataframe(df_fib)

    return CommandOutput(item=item)


@router.command(methods=["POST"])
def obv(
    data: List[Data],
    index: str = "date",
    offset: int = 0,
) -> CommandOutput[List[Data]]:
    """
    The On Balance Volume (OBV) is a cumulative total of the up and
    down volume. When the close is higher than the previous close, the volume is added
    to the running total, and when the close is lower than the previous close, the volume
    is subtracted from the running total. \n \n To interpret the OBV, look for the OBV
    to move with the price or precede price moves. If the price moves before the OBV,
    then it is a non-confirmed move. A series of rising peaks, or falling troughs, in the
    OBV indicates a strong trend. If the OBV is flat, then the market is not trending.

    Parameters
    ----------
    data : List[Data]
        List of data to apply the indicator to.
    index : str, optional
        Index column name, by default "date"
    offset : int, optional
        How many periods to offset the result, by default 0.

    Returns
    -------
    CommandOutput[List[Data]]
        List of data with the indicator applied.

    Examples
    --------
    >>> from openbb_sdk_core import openbb
    >>> stock_data = openbb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp").output
    >>> obv_data = openbb.ta.obv(data=stock_data.item, offset=0)
    """

    df = to_dataframe(data, index=index)
    df_target = get_target_columns(df, ["close", "volume"])
    df_obv = pd.DataFrame(df_target.ta.obv(offset=offset))

    item = from_dataframe(df_target.join(df_obv, how="left"), index=True)

    return CommandOutput(item=item)


@router.command(methods=["POST"])
def fisher(
    data: List[Data],
    index: str = "date",
    length: PositiveInt = 14,
    signal: PositiveInt = 1,
) -> CommandOutput[List[Data]]:
    """
    The Fisher Transform is a technical indicator created by John F. Ehlers
    that converts prices into a Gaussian normal distribution.1 The indicator
    highlights when prices have   moved to an extreme, based on recent prices.
    This may help in spotting turning points in the price of an asset. It also
    helps show the trend and isolate the price waves within a trend.

    Parameters
    ----------
    data : List[Data]
        List of data to apply the indicator to.
    index : str, optional
        Index column name, by default "date"
    length : PositiveInt, optional
        Fisher period, by default 14
    signal : PositiveInt, optional
        Fisher Signal period, by default 1

    Returns
    -------
    CommandOutput[List[Data]]
        List of data with the indicator applied.

    Examples
    --------
    >>> from openbb_sdk_core import openbb
    >>> stock_data = openbb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp").output
    >>> fisher_data = openbb.ta.fisher(data=stock_data.item, length=14, signal=1)
    """

    df = to_dataframe(data, index=index)
    df_target = get_target_columns(df, ["high", "low"])
    df_fisher = pd.DataFrame(df_target.ta.fisher(length=length, signal=signal))

    item = from_dataframe(df_target.join(df_fisher, how="left"), index=True)

    return CommandOutput(item=item)


@router.command(methods=["POST"])
def adosc(
    data: List[Data],
    index: str = "date",
    fast: PositiveInt = 3,
    slow: PositiveInt = 10,
    offset: int = 0,
) -> CommandOutput[List[Data]]:
    """
    Accumulation/Distribution Oscillator, also known as the Chaikin Oscillator
    is essentially a momentum indicator, but of the Accumulation-Distribution line
    rather than merely price. It looks at both the strength of price moves and the
    underlying buying and selling pressure during a given time period. The oscillator
    reading above zero indicates net buying pressure, while one below zero registers
    net selling pressure. Divergence between the indicator and pure price moves are
    the most common signals from the indicator, and often flag market turning points.

    Parameters
    ----------
    data : List[Data]
        List of data to be used for the calculation.
    fast : PositiveInt, optional
        Number of periods to be used for the fast calculation, by default 3.
    slow : PositiveInt, optional
        Number of periods to be used for the slow calculation, by default 10.
    offset : int, optional
        Offset to be used for the calculation, by default 0.

    Returns
    -------
    CommandOutput[List[Data]]

    Examples
    --------
    >>> from openbb_sdk_core import openbb
    >>> stock_data = openbb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp").output
    >>> adosc_data = openbb.ta.adosc(data=stock_data.item, fast=3, slow=10, offset=0)
    """

    df = to_dataframe(data, index=index)
    df_target = get_target_columns(df, ["high", "low", "close", "volume", "open"])
    df_adosc = pd.DataFrame(df_target.ta.adosc(fast=fast, slow=slow, offset=offset))

    item = from_dataframe(df_target.join(df_adosc, how="left"), index=True)

    return CommandOutput(item=item)


@router.command(methods=["POST"])
def tv() -> CommandOutput[Empty]:
    """TradingView."""

    # TODO : probably out of scope for now

    return CommandOutput(item=Empty())


@router.command(methods=["POST"])
def bbands(
    data: List[Data],
    target: str = "close",
    index: str = "date",
    length: int = 50,
    std: NonNegativeFloat = 2,
    mamode: Literal["sma", "ema", "wma", "rma"] = "sma",
    offset: int = 0,
) -> CommandOutput[List[Data]]:
    """
    Bollinger Bands consist of three lines. The middle band is a simple
    moving average (generally 20 periods) of the typical price (TP). The upper and lower
    bands are F standard deviations (generally 2) above and below the middle band.
    The bands widen and narrow when the volatility of the price is higher or lower,
    respectively. \n \nBollinger Bands do not, in themselves, generate buy or sell signals;
    they are an indicator of overbought or oversold conditions. When the price is near the
    upper or lower band it indicates that a reversal may be imminent. The middle band
    becomes a support or resistance level. The upper and lower bands can also be
    interpreted as price targets. When the price bounces off of the lower band and crosses
    the middle band, then the upper band becomes the price target.

    Parameters
    ----------
    data : List[Data]
        List of data to be used for the calculation.
    target : str
        Target column name.
    index : str, optional
        Index column name to use with `data`, by default "date".
    length : int, optional
        Number of periods to be used for the calculation, by default 50.
    std : NonNegativeFloat, optional
        Standard deviation to be used for the calculation, by default 2.
    mamode : Literal["sma", "ema", "wma", "rma"], optional
        Moving average mode to be used for the calculation, by default "sma".
    offset : int, optional
        Offset to be used for the calculation, by default 0.

    Returns
    -------
    CommandOutput[List[Data]]
        The calculated data.

    Examples
    --------
    >>> from openbb_sdk_core import openbb
    >>> stock_data = openbb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp").output
    >>> bbands_data = openbb.ta.bbands(data=stock_data.item, column="close", length=50, std=2, mamode="sma", offset=0)
    """

    df = to_dataframe(data, index=index)
    df_target = get_target_column(df, target).to_frame()
    bbands_df = pd.DataFrame(
        df_target.ta.bbands(length=length, std=std, mamode=mamode, offset=offset)
    )

    item = from_dataframe(df_target.join(bbands_df, how="left"), index=True)

    return CommandOutput(item=item)


@router.command(methods=["POST"])
def multi() -> CommandOutput[Empty]:
    """Plot multiple indicators on the same chart."""

    # TODO : probably out of scope for now

    return CommandOutput(item=Empty())


@router.command(methods=["POST"])
def zlma(
    data: List[Data],
    target: str = "close",
    index: str = "date",
    length: int = 50,
    offset: int = 0,
) -> CommandOutput[List[Data]]:
    """
    The zero lag exponential moving average (ZLEMA) indicator
    was created by John Ehlers and Ric Way. The idea is do a
    regular exponential moving average (EMA) calculation but
    on a de-lagged data instead of doing it on the regular data.
    Data is de-lagged by removing the data from "lag" days ago
    thus removing (or attempting to) the cumulative effect of
    the moving average.

    Parameters
    ----------
    data : List[Data]
        List of data to be used for the calculation.
    target : str
        Target column name.
    index : str, optional
        Index column name to use with `data`, by default "date".
    length : int, optional
        Number of periods to be used for the calculation, by default 50.
    offset : int, optional
        Offset to be used for the calculation, by default 0.

    Returns
    -------
    CommandOutput[List[Data]]
        The calculated data.

    Examples
    --------
    >>> from openbb_sdk_core import openbb
    >>> stock_data = openbb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp").output
    >>> zlma_data = openbb.ta.zlma(data=stock_data.item, column="close", length=50, offset=0)
    """

    def _zlma_export_plotly(
        data: pd.DataFrame, zlma_data: pd.DataFrame, zlma_column: str, title: str
    ) -> Plotly:
        date_data = data.index.tolist()
        close_data = data[target].tolist()
        zlma_data = zlma_data[zlma_column].tolist()

        fig = plot_timeseries(
            x=date_data,
            y=[
                YTimeSeries(data=close_data, name="Close", color="blue"),
                YTimeSeries(data=zlma_data, name="ZLMA", color="red"),
            ],
            title=title,
            xaxis_title="Date",
            yaxis_title="Price",
            legend_title="Legend",
        )

        return Plotly(content=fig.to_plotly_json())

    df = to_dataframe(data, index=index)
    df_target = get_target_column(df, target).to_frame()
    zlma_df = pd.DataFrame(df_target.ta.zlma(length=length, offset=offset)).dropna()

    item = from_dataframe(df_target.join(zlma_df, how="left"), index=True)

    return CommandOutput(
        item=item,
        export_list=[
            _zlma_export_plotly(
                data=df_target,
                zlma_data=zlma_df,
                zlma_column=zlma_df.columns[0],
                title=f"ZLMA {str(length)} with a offset of {str(offset)}",
            ),
        ],
    )


@router.command(methods=["POST"])
def aroon(
    data: List[Data],
    index: str = "date",
    length: int = 25,
    scalar: int = 100,
) -> CommandOutput[List[Data]]:
    """
    The word aroon is Sanskrit for "dawn's early light." The Aroon
    indicator attempts to show when a new trend is dawning. The indicator consists
    of two lines (Up and Down) that measure how long it has been since the highest
    high/lowest low has occurred within an n period range. \n \n When the Aroon Up is
    staying between 70 and 100 then it indicates an upward trend. When the Aroon Down
    is staying between 70 and 100 then it indicates an downward trend. A strong upward
    trend is indicated when the Aroon Up is above 70 while the Aroon Down is below 30.
    Likewise, a strong downward trend is indicated when the Aroon Down is above 70 while
    the Aroon Up is below 30. Also look for crossovers. When the Aroon Down crosses above
    the Aroon Up, it indicates a weakening of the upward trend (and vice versa).

    Parameters
    ----------
    data : List[Data]
        List of data to be used for the calculation.
    index: str, optional
        Index column name to use with `data`, by default "date".
    length : int, optional
        Number of periods to be used for the calculation, by default 25.
    scalar : int, optional
        Scalar to be used for the calculation, by default 100.

    Returns
    -------
    CommandOutput[List[Data]]
        The calculated data.

    Examples
    --------
    >>> from openbb_sdk_core import openbb
    >>> stock_data = openbb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp").output
    >>> aroon_data = openbb.ta.aroon(data=stock_data.item, length=25, scalar=100)
    """

    def _aroon_export_plotly(
        data: pd.DataFrame,
        aroon_data: pd.DataFrame,
        title: str,
    ) -> Plotly:
        date_data = data.index.tolist()
        aroon_up_data = aroon_data[aroon_data.columns[0]].tolist()
        aroon_down_data = aroon_data[aroon_data.columns[1]].tolist()
        aroon_osc_data = aroon_data[aroon_data.columns[2]].tolist()

        fig = plot_timeseries(
            x=date_data,
            y=[
                YTimeSeries(data=aroon_up_data, name="Aroon Up", color="blue"),
                YTimeSeries(data=aroon_down_data, name="Aroon Down", color="red"),
                YTimeSeries(data=aroon_osc_data, name="Aroon OSC", color="green"),
            ],
            title=title,
            xaxis_title="Date",
            yaxis_title="Price",
            legend_title="Legend",
        )

        return Plotly(content=fig.to_plotly_json())

    df = to_dataframe(data, index=index)
    df_target = get_target_columns(df, ["high", "low", "close"])
    aroon_df = pd.DataFrame(df_target.ta.aroon(length=length, scalar=scalar)).dropna()

    item = from_dataframe(df_target.join(aroon_df, how="left"), index=True)

    return CommandOutput(
        item=item,
        export_list=[
            _aroon_export_plotly(
                data=df_target,
                aroon_data=aroon_df,
                title=f"AROON {str(length)} with a scalar of {str(scalar)}",
            ),
        ],
    )


@router.command(methods=["POST"])
def sma(
    data: List[Data],
    target: str = "close",
    index: str = "date",
    length: int = 50,
    offset: int = 0,
) -> CommandOutput[List[Data]]:
    """
    Moving Averages are used to smooth the data in an array to
    help eliminate noise and identify trends. The Simple Moving Average is literally
    the simplest form of a moving average. Each output value is the average of the
    previous n values. In a Simple Moving Average, each value in the time period carries
    equal weight, and values outside of the time period are not included in the average.
    This makes it less responsive to recent changes in the data, which can be useful for
    filtering out those changes.

    Parameters
    ----------
    data : List[Data]
        List of data to be used for the calculation.
    target : str
        Target column name.
    index : str, optional
        Index column name to use with `data`, by default "date".
    length : int, optional
        Number of periods to be used for the calculation, by default 50.
    offset : int, optional
        Offset from the current period, by default 0.

    Returns
    -------
    CommandOutput[List[Data]]
        The calculated data.

    Examples
    --------
    >>> from openbb_sdk_core import openbb
    >>> stock_data = openbb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp").output
    >>> sma_data = openbb.ta.sma(data=stock_data.item,column="close",length=50,offset=0)
    """

    def _sma_export_plotly(
        data: pd.DataFrame, sma_data: pd.DataFrame, sma_column: str, title: str
    ) -> Plotly:
        date_data = data.index.tolist()
        close_data = data[target].tolist()
        sma_data = sma_data[sma_column].tolist()

        fig = plot_timeseries(
            x=date_data,
            y=[
                YTimeSeries(data=close_data, name="Close", color="blue"),
                YTimeSeries(data=sma_data, name="SMA", color="red"),
            ],
            title=title,
            xaxis_title="Date",
            yaxis_title="Price",
            legend_title="Legend",
        )

        return Plotly(content=fig.to_plotly_json())

    df = to_dataframe(data, index=index)
    df_target = get_target_column(df, target).to_frame()
    sma_df = pd.DataFrame(df_target.ta.sma(length=length, offset=offset).dropna())

    item = from_dataframe(df_target.join(sma_df, how="left"), index=True)

    return CommandOutput(
        item=item,
        export_list=[
            _sma_export_plotly(
                data=df_target,
                sma_data=sma_df,
                sma_column=sma_df.columns[0],
                title=f"SMA {str(length)} with a offset of {str(offset)}",
            ),
        ],
    )


@router.command(methods=["POST"])
def demark(
    data: List[Data],
    index: str = "date",
    target: str = "close",
    show_all: bool = False,
    asint: bool = False,
    offset: int = 0,
) -> CommandOutput[List[Data]]:
    """
    Demark sequential indicator

    Parameters
    ----------
    data : List[Data]
        List of data to be used for the calculation.
    index : str, optional
        Index column name to use with `data`, by default "date".
    target : str, optional
        Target column name, by default "close".
    show_all : bool, optional
        Show 1 - 13. If set to False, show 6 - 9
    asint : bool, optional
        If True, fillnas with 0 and change type to int, by default False
    offset : int, optional
        How many periods to offset the result

    Returns
    -------
    CommandOutput[List[Data]]
        The calculated data.

    Examples
    --------
    >>> from openbb_sdk_core import openbb
    >>> stock_data = openbb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp").output
    >>> demark_data = openbb.ta.demark(data=stock_data.item,offset=0)
    """

    df = to_dataframe(data, index=index)
    df_target = get_target_column(df, target).to_frame()
    demark_df = pd.DataFrame(
        df_target.ta.td_seq(offset=offset, show_all=show_all, asint=asint).dropna()
    )

    item = from_dataframe(df_target.join(demark_df, how="left"), index=True)

    return CommandOutput(item=item)


@router.command(methods=["POST"])
def vwap(
    data: List[Data],
    index: str = "date",
    anchor: str = "D",
    offset: int = 0,
) -> CommandOutput[List[Data]]:
    """
    The Volume Weighted Average Price that measures the average typical price
    by volume.  It is typically used with intraday charts to identify general direction.

    Parameters
    ----------
    data : List[Data]
        List of data to be used for the calculation.
    index : str, optional
        Index column name to use with `data`, by default "date".
    anchor : str, optional
        Anchor period to use for the calculation, by default "D".
        See Timeseries Offset Aliases below for additional options:
        https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-offset-aliases
    offset : int, optional
        Offset from the current period, by default 0.

    Returns
    -------
    CommandOutput[List[Data]]
        The calculated data.

    Examples
    --------
    >>> from openbb_sdk_core import openbb
    >>> stock_data = openbb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp").output
    >>> vwap_data = openbb.ta.vwap(data=stock_data.item,anchor="D",offset=0)
    """

    df = to_dataframe(data, index=index)
    df_target = get_target_columns(df, ["high", "low", "close", "volume"])
    df_vwap = pd.DataFrame(df_target.ta.vwap(anchor=anchor, offset=offset).dropna())

    item = from_dataframe(df_target.join(df_vwap, how="left"), index=True)

    return CommandOutput(item=item)


@router.command(methods=["POST"])
def recom() -> CommandOutput[Empty]:
    """Recommendation."""

    # TODO : this command does only a call to a Tradingview's endpoint
    #        thus, it should probably be implement on a provider level

    return CommandOutput(item=Empty())


@router.command(methods=["POST"])
def macd(
    data: List[Data],
    target: str = "close",
    index: str = "date",
    fast: int = 12,
    slow: int = 26,
    signal: int = 9,
) -> CommandOutput[List[Data]]:
    """
    The Moving Average Convergence Divergence (MACD) is the difference
    between two Exponential Moving Averages. The Signal line is an Exponential Moving
    Average of the MACD. \n \n The MACD signals trend changes and indicates the start
    of new trend direction. High values indicate overbought conditions, low values
    indicate oversold conditions. Divergence with the price indicates an end to the
    current trend, especially if the MACD is at extreme high or low values. When the MACD
    line crosses above the signal line a buy signal is generated. When the MACD crosses
    below the signal line a sell signal is generated. To confirm the signal, the MACD
    should be above zero for a buy, and below zero for a sell.

    Parameters
    ----------
    data : List[Data]
        List of data to be used for the calculation.
    target : str
        Target column name.
    fast : int, optional
        Number of periods for the fast EMA, by default 12.
    slow : int, optional
        Number of periods for the slow EMA, by default 26.
    signal : int, optional
        Number of periods for the signal EMA, by default 9.

    Returns
    -------
    CommandOutput[List[Data]]
        The calculated data.

    Examples
    --------
    >>> from openbb_sdk_core import openbb
    >>> stock_data = openbb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp").output
    >>> macd_data = openbb.ta.macd(data=stock_data.item,column="close",fast=12,slow=26,signal=9)
    """

    def _macd_export_plotly(
        data: pd.DataFrame, macd_data: pd.DataFrame, macd_column: str, title: str
    ) -> Plotly:
        date_data = data.index.tolist()
        close_data = data[target].tolist()
        macd_data = macd_data[macd_column].tolist()

        fig = plot_timeseries(
            x=date_data,
            y=[
                YTimeSeries(data=close_data, name="Close", color="blue"),
                YTimeSeries(data=macd_data, name="MACD", color="red"),
            ],
            title=title,
            xaxis_title="Date",
            yaxis_title="Price",
            legend_title="Legend",
        )

        return Plotly(content=fig.to_plotly_json())

    df = to_dataframe(data, index=index)
    df_target = get_target_column(df, target).to_frame()
    macd_df = pd.DataFrame(
        df_target.ta.macd(fast=fast, slow=slow, signal=signal).dropna()
    )

    item = from_dataframe(df_target.join(macd_df, how="left"), index=True)

    return CommandOutput(
        item=item,
        export_list=[
            _macd_export_plotly(
                data=df_target,
                macd_data=macd_df,
                macd_column=macd_df.columns[0],
                title=f"MACD {str(fast)}-{str(slow)}-{str(signal)}",
            ),
        ],
    )


@router.command(methods=["POST"])
def hma(
    data: List[Data],
    target: str = "close",
    index: str = "date",
    length: int = 50,
    offset: int = 0,
) -> CommandOutput[List[Data]]:
    """
    The Hull Moving Average solves the age old dilemma of making a moving average
    more responsive to current price activity whilst maintaining curve smoothness.
    In fact the HMA almost eliminates lag altogether and manages to improve smoothing
    at the same time.

    Parameters
    ----------
    data : List[Data]
        List of data to be used for the calculation.
    target : str
        Target column name.
    index : str, optional
        Index column name to use with `data`, by default "date".
    length : int, optional
        Number of periods for the HMA, by default 50.
    offset : int, optional
        Offset of the HMA, by default 0.

    Returns
    -------
    CommandOutput[List[Data]]
        The calculated data.

    Examples
    --------
    >>> from openbb_sdk_core import openbb
    >>> stock_data = openbb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp").output
    >>> hma_data = openbb.ta.hma(data=stock_data.item,column="close",length=50,offset=0)
    """

    def _hma_export_plotly(
        data: pd.DataFrame, hma_data: pd.DataFrame, hma_column: str, title: str
    ) -> Plotly:
        date_data = data.index.tolist()
        close_data = data[target].tolist()
        hma_data = hma_data[hma_column].tolist()

        fig = plot_timeseries(
            x=date_data,
            y=[
                YTimeSeries(data=close_data, name="Close", color="blue"),
                YTimeSeries(data=hma_data, name="HMA", color="red"),
            ],
            title=title,
            xaxis_title="Date",
            yaxis_title="Price",
            legend_title="Legend",
        )

        return Plotly(content=fig.to_plotly_json())

    df = to_dataframe(data, index=index)
    df_target = get_target_column(df, target).to_frame()
    hma_df = pd.DataFrame(df_target.ta.hma(length=length, offset=offset).dropna())

    item = from_dataframe(df_target.join(hma_df, how="left"), index=True)

    return CommandOutput(
        item=item,
        export_list=[
            _hma_export_plotly(
                data=df_target,
                hma_data=hma_df,
                hma_column=hma_df.columns[0],
                title=f"HMA {str(length)} with a offset of {str(offset)}",
            ),
        ],
    )


@router.command(methods=["POST"])
def donchian(
    data: List[Data],
    index: str = "date",
    lower_length: PositiveInt = 20,
    upper_length: PositiveInt = 20,
    offset: int = 0,
) -> CommandOutput[List[Data]]:
    """
    Donchian Channels are three lines generated by moving average
    calculations that comprise an indicator formed by upper and lower
    bands around a midrange or median band. The upper band marks the
    highest price of a security over N periods while the lower band
    marks the lowest price of a security over N periods. The area
    between the upper and lower bands represents the Donchian Channel.

    Parameters
    ----------
    data : List[Data]
        List of data to be used for the calculation.
    index : str, optional
        Index column name to use with `data`, by default "date".
    lower_length : PositiveInt, optional
        Number of periods for the lower band, by default 20.
    upper_length : PositiveInt, optional
        Number of periods for the upper band, by default 20.
    offset : int, optional
        Offset of the Donchian Channel, by default 0.

    Returns
    -------
    CommandOutput[List[Data]]
        The calculated data.

    Examples
    --------
    >>> from openbb_sdk_core import openbb
    >>> stock_data = openbb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp").output
    >>> donchian_data = openbb.ta.donchian(data=stock_data.item,lower_length=20,upper_length=20,offset=0)
    """

    df = to_dataframe(data, index=index)
    df_target = get_target_columns(df, ["high", "low"])
    donchian_df = pd.DataFrame(
        df_target.ta.donchian(
            lower_length=lower_length, upper_length=upper_length, offset=offset
        ).dropna()
    )

    item = from_dataframe(df_target.join(donchian_df, how="left"), index=True)

    return CommandOutput(item=item)


@router.command(methods=["POST"])
def ichimoku(
    data: List[Data],
    index: str = "date",
    conversion: PositiveInt = 9,
    base: PositiveInt = 26,
    lagging: PositiveInt = 52,
    offset: PositiveInt = 26,
    lookahead: bool = False,
) -> CommandOutput[List[Data]]:
    """
    The Ichimoku Cloud, also known as Ichimoku Kinko Hyo, is a versatile indicator that
    defines support and resistance, identifies trend direction, gauges momentum and provides
    trading signals. Ichimoku Kinko Hyo translates into "one look equilibrium chart". With
    one look, chartists can identify the trend and look for potential signals within that trend.

    Parameters
    ----------
    data : List[Data]
        List of data to be used for the calculation.
    index : str, optional
        Index column name to use with `data`, by default "date".
    conversion : PositiveInt, optional
        Number of periods for the conversion line, by default 9.
    base : PositiveInt, optional
        Number of periods for the base line, by default 26.
    lagging : PositiveInt, optional
        Number of periods for the lagging span, by default 52.
    offset : PositiveInt, optional
        Number of periods for the offset, by default 26.
    lookahead : bool, optional
        drops the Chikou Span Column to prevent potential data leak
    """

    df = to_dataframe(data, index=index)
    df_target = get_target_columns(df, ["high", "low", "close"])
    df_ichimoku, df_span = df_target.ta.ichimoku(
        tenkan=conversion,
        kijun=base,
        senkou=lagging,
        offset=offset,
        lookahead=lookahead,
    )

    df_result = df_target.join(df_span.add_prefix("span_"), how="left")
    df_result = df_result.join(df_ichimoku, how="left")

    item = from_dataframe(df_result, index=True)

    return CommandOutput(item=item)


@router.command(methods=["POST"])
def clenow(
    data: List[Data],
    index: str = "date",
    target: str = "adj_close",
    period: PositiveInt = 90,
) -> CommandOutput[List[Data]]:
    """
    Clenow Volatility Adjusted Momentum.

    Parameters
    ----------
    data : List[Data]
        List of data to be used for the calculation.
    index : str, optional
        Index column name to use with `data`, by default "date".
    target : str, optional
        Target column name, by default "adj_close".
    period : PositiveInt, optional
        Number of periods for the momentum, by default 90.

    Returns
    -------
    CommandOutput[List[Data]]
        The calculated data.

    Examples
    --------
    >>> from openbb_sdk_core import openbb
    >>> stock_data = openbb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp").output
    >>> clenow_data = openbb.ta.clenow(data=stock_data.item,period=90)
    """

    df = to_dataframe(data, index=index)
    df_target = get_target_column(df, target)

    r2, coef, _ = ta_helpers.clenow_momentum(df_target, period)

    df_clenow = pd.DataFrame.from_dict(
        {
            "r^2": f"{r2:.5f}",
            "fit_coef": f"{coef:.5f}",
            "factor": f"{coef * r2:.5f}",
        },
        orient="index",
    ).transpose()

    item = from_dataframe(df_clenow)

    return CommandOutput(item=item)


@router.command(methods=["POST"])
def ad(
    data: List[Data], index: str = "date", offset: int = 0
) -> CommandOutput[List[Data]]:
    """
    The Accumulation/Distribution Line is similar to the On Balance
    Volume (OBV), which sums the volume times +1/-1 based on whether the close is
    higher than the previous close. The Accumulation/Distribution indicator, however
    multiplies the volume by the close location value (CLV). The CLV is based on the
    movement of the issue within a single bar and can be +1, -1 or zero. \n \n
    The Accumulation/Distribution Line is interpreted by looking for a divergence in
    the direction of the indicator relative to price. If the Accumulation/Distribution
    Line is trending upward it indicates that the price may follow. Also, if the
    Accumulation/Distribution Line becomes flat while the price is still rising (or falling)
    then it signals an impending flattening of the price.

    Parameters
    ----------
    data : List[Data]
        List of data to be used for the calculation.
    index : str, optional
        Index column name to use with `data`, by default "date".
    offset : int, optional
        Offset of the AD, by default 0.

    Returns
    -------
    CommandOutput[List[Data]]

    Examples
    --------
    >>> from openbb_sdk_core import openbb
    >>> stock_data = openbb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp").output
    >>> ad_data = openbb.ta.ad(data=stock_data.item,offset=0)
    """

    df = to_dataframe(data, index=index)
    df_target = get_target_columns(df, ["high", "low", "close", "volume"])
    ad_df = pd.DataFrame(df_target.ta.ad(offset=offset).dropna())

    item = from_dataframe(df_target.join(ad_df, how="left"), index=True)

    return CommandOutput(item=item)


@router.command(methods=["POST"])
def adx(
    data: List[Data],
    index: str = "date",
    length: int = 50,
    scalar: float = 100.0,
    drift: int = 1,
) -> CommandOutput[List[Data]]:
    """
    The ADX is a Welles Wilder style moving average of the Directional Movement Index (DX).
    The values range from 0 to 100, but rarely get above 60. To interpret the ADX, consider
    a high number to be a strong trend, and a low number, a weak trend.

    Parameters
    ----------
    data : List[Data]
        List of data to be used for the calculation.
    index : str, optional
        Index column name to use with `data`, by default "date".
    length : int, optional
        Number of periods for the ADX, by default 50.
    scalar : float, optional
        Scalar value for the ADX, by default 100.0.
    drift : int, optional
        Drift value for the ADX, by default 1.

    Returns
    -------
    CommandOutput[List[Data]]
        The calculated data.

    Examples
    --------
    >>> from openbb_sdk_core import openbb
    >>> stock_data = openbb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp").output
    >>> adx_data = openbb.ta.adx(data=stock_data.item,length=50,scalar=100.0,drift=1)
    """

    def _adx_export_plotly(data, column, adx_data, adx_columns, title) -> Plotly:
        date_data = data.index.tolist()
        close_data = data[column].tolist()
        a = adx_data[adx_columns[0]].tolist()
        dmp = adx_data[adx_columns[1]].tolist()
        dmn = adx_data[adx_columns[2]].tolist()

        fig = plot_timeseries(
            x=date_data,
            y=[
                YTimeSeries(data=close_data, name="Close", color="blue"),
                YTimeSeries(data=a, name="ADX", color="red"),
                YTimeSeries(data=dmp, name="DMP", color="green"),
                YTimeSeries(data=dmn, name="DMN", color="orange"),
            ],
            title=title,
            xaxis_title="Date",
            yaxis_title="Price",
            legend_title="Legend",
        )

        return Plotly(content=fig.to_plotly_json())

    df = to_dataframe(data, index=index)
    df_target = get_target_columns(df, ["close", "high", "low"])
    adx_df = pd.DataFrame(
        df_target.ta.adx(length=length, scalar=scalar, drift=drift).dropna()
    )

    item = from_dataframe(df_target.join(adx_df, how="left"), index=True)

    return CommandOutput(
        item=item,
        export_list=[
            _adx_export_plotly(
                data=df_target,
                column="close",
                adx_data=adx_df,
                adx_columns=adx_df.columns,
                title=f"ADX {str(length)}-{str(scalar)}-{str(drift)}",
            ),
        ],
    )


@router.command(methods=["POST"])
def wma(
    data: List[Data],
    target: str = "close",
    index: str = "date",
    length: int = 50,
    offset: int = 0,
) -> CommandOutput[List[Data]]:
    """
    A Weighted Moving Average puts more weight on recent data and less on past data.
    This is done by multiplying each bar’s price by a weighting factor. Because of its
    unique calculation, WMA will follow prices more closely than a corresponding Simple
    Moving Average.

    Parameters
    ----------
    data : List[Data]
        The data to use for the calculation.
    target : str
        Target column name.
    index : str, optional
        Index column name to use with `data`, by default "date".
    length : int, optional
        The length of the WMA, by default 50.
    offset : int, optional
        The offset of the WMA, by default 0.

    Returns
    -------
    CommandOutput[List[Data]]
        The WMA data.

    Examples
    --------
    >>> from openbb_sdk_core import openbb
    >>> stock_data = openbb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp").output
    >>> wma_data = openbb.ta.wma(data=stock_data.item, column="close", length=50, offset=0)
    """

    def _wma_export_plotly(
        data: pd.DataFrame, wma_data: pd.DataFrame, wma_column: str, title: str
    ) -> Plotly:
        date_data = data.index.tolist()
        close_data = data[target].tolist()
        wma_data = wma_data[wma_column].tolist()

        fig = plot_timeseries(
            x=date_data,
            y=[
                YTimeSeries(data=close_data, name="Close", color="blue"),
                YTimeSeries(data=wma_data, name="WMA", color="red"),
            ],
            title=title,
            xaxis_title="Date",
            yaxis_title="Price",
            legend_title="Legend",
        )

        return Plotly(content=fig.to_plotly_json())

    df = to_dataframe(data, index=index)
    df_target = get_target_column(df, target).to_frame()
    wma_df = pd.DataFrame(df_target.ta.wma(length=length, offset=offset).dropna())

    item = from_dataframe(df_target.join(wma_df, how="left"), index=True)

    return CommandOutput(
        item=item,
        export_list=[
            _wma_export_plotly(
                data=df_target,
                wma_data=wma_df,
                wma_column=wma_df.columns[0],
                title=f"WMA {str(length)} with a offset of {str(offset)}",
            ),
        ],
    )


@router.command(methods=["POST"])
def cci(
    data: List[Data],
    index: str = "date",
    length: PositiveInt = 14,
    scalar: PositiveFloat = 0.015,
) -> CommandOutput[List[Data]]:
    """
    The CCI is designed to detect beginning and ending market trends.
    The range of 100 to -100 is the normal trading range. CCI values outside of this
    range indicate overbought or oversold conditions. You can also look for price
    divergence in the CCI. If the price is making new highs, and the CCI is not,
    then a price correction is likely.

    Parameters
    ----------
    data : List[Data]
        The data to use for the CCI calculation.
    index : str, optional
        Index column name to use with `data`, by default "date".
    length : PositiveInt, optional
        The length of the CCI, by default 14.
    scalar : PositiveFloat, optional
        The scalar of the CCI, by default 0.015.

    Returns
    -------
    CommandOutput[List[Data]]
        The CCI data.
    """

    df = to_dataframe(data, index=index)
    df_target = get_target_columns(df, ["close", "high", "low"])
    cci_df = pd.DataFrame(df_target.ta.cci(length=length, scalar=scalar).dropna())

    item = from_dataframe(df_target.join(cci_df, how="left"), index=True)

    return CommandOutput(item=item)


@router.command(methods=["POST"])
def rsi(
    data: List[Data],
    target: str = "close",
    index: str = "date",
    length: int = 14,
    scalar: float = 100.0,
    drift: int = 1,
) -> CommandOutput[List[Data]]:
    """
    The Relative Strength Index (RSI) calculates a ratio of the
    recent upward price movements to the absolute price movement. The RSI ranges
    from 0 to 100. The RSI is interpreted as an overbought/oversold indicator when
    the value is over 70/below 30. You can also look for divergence with price. If
    the price is making new highs/lows, and the RSI is not, it indicates a reversal.

    Parameters
    ----------
    data : List[Data]
        The data to use for the RSI calculation.
    target : str
        Target column name.
    index : str, optional
        Index column name to use with `data`, by default "date"
    length : int, optional
        The length of the RSI, by default 14
    scalar : float, optional
        The scalar to use for the RSI, by default 100.0
    drift : int, optional
        The drift to use for the RSI, by default 1

    Returns
    -------
    CommandOutput[List[Data]]
        The RSI data.

    Examples
    --------
    >>> from openbb_sdk_core import openbb
    >>> stock_data = openbb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp").output
    >>> rsi_data = openbb.ta.rsi(data=stock_data.item, column="close", length=14, scalar=100.0, drift=1)
    """

    def _rsi_export_plotly(
        data: pd.DataFrame, rsi_data: pd.DataFrame, rsi_column: str, title: str
    ) -> Plotly:
        date_data = data.index.tolist()
        close_data = data[target].tolist()
        rsi_data = rsi_data[rsi_column].tolist()

        fig = plot_timeseries(
            x=date_data,
            y=[
                YTimeSeries(data=close_data, name="Close", color="blue"),
                YTimeSeries(data=rsi_data, name="RSI", color="red"),
            ],
            title=title,
            xaxis_title="Date",
            yaxis_title="Price",
            legend_title="Legend",
        )

        return Plotly(content=fig.to_plotly_json())

    df = to_dataframe(data, index=index)
    df_target = get_target_column(df, target).to_frame()
    rsi_df = pd.DataFrame(
        df_target.ta.rsi(length=length, scalar=scalar, drift=drift).dropna()
    )

    item = from_dataframe(df_target.join(rsi_df, how="left"), index=True)

    return CommandOutput(
        item=item,
        export_list=[
            _rsi_export_plotly(
                data=df_target,
                rsi_data=rsi_df,
                rsi_column=rsi_df.columns[0],
                title=f"RSI {str(length)} with a scalar of {str(scalar)} and a drift of {str(drift)}",
            ),
        ],
    )


@router.command(methods=["POST"])
def summary() -> CommandOutput[Empty]:
    """Summary."""

    # TODO : this command does only a call to a finbrain's endpoint
    #        thus, it should probably be implement on a provider level

    return CommandOutput(item=Empty())


@router.command(methods=["POST"])
def stoch(
    data: List[Data],
    index: str = "date",
    fast_k_period: NonNegativeInt = 14,
    slow_d_period: NonNegativeInt = 3,
    slow_k_period: NonNegativeInt = 3,
) -> CommandOutput[List[Data]]:
    """
    The Stochastic Oscillator measures where the close is in relation
    to the recent trading range. The values range from zero to 100. %D values over 75
    indicate an overbought condition; values under 25 indicate an oversold condition.
    When the Fast %D crosses above the Slow %D, it is a buy signal; when it crosses
    below, it is a sell signal. The Raw %K is generally considered too erratic to use
    for crossover signals.

    Parameters
    ----------
    data : List[Data]
        The data to use for the Stochastic Oscillator calculation.
    index : str, optional
        Index column name to use with `data`, by default "date".
    fast_k_period : NonNegativeInt, optional
        The fast %K period, by default 14.
    slow_d_period : NonNegativeInt, optional
        The slow %D period, by default 3.
    slow_k_period : NonNegativeInt, optional
        The slow %K period, by default 3.

    Returns
    -------
    CommandOutput[List[Data]]
        The Stochastic Oscillator data.

    Examples
    --------
    >>> from openbb_sdk_core import openbb
    >>> stock_data = openbb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp").output
    >>> stoch_data = openbb.ta.stoch(data=stock_data.item, fast_k_period=14, slow_d_period=3, slow_k_period=3)
    """

    df = to_dataframe(data, index=index)
    df_target = get_target_columns(df, ["close", "high", "low"])
    stoch_df = pd.DataFrame(
        df_target.ta.stoch(
            fast_k_period=fast_k_period,
            slow_d_period=slow_d_period,
            slow_k_period=slow_k_period,
        ).dropna()
    )

    item = from_dataframe(df_target.join(stoch_df, how="left"), index=True)

    return CommandOutput(item=item)


@router.command(methods=["POST"])
def rsp() -> CommandOutput[Empty]:
    """Relative Strength Performance."""

    # TODO : https://github.com/OpenBB-finance/OpenBBTerminal/issues/5167

    return CommandOutput(item=Empty())


@router.command(methods=["POST"])
def kc(
    data: List[Data],
    index: str = "date",
    length: PositiveInt = 20,
    scalar: PositiveFloat = 20,
    mamode: Literal["ema", "sma", "wma", "hma", "zlma"] = "ema",
    offset: NonNegativeInt = 0,
) -> CommandOutput[List[Data]]:
    """
    Keltner Channels are volatility-based bands that are placed
    on either side of an asset's price and can aid in determining
    the direction of a trend.The Keltner channel uses the average
    true range (ATR) or volatility, with breaks above or below the top
    and bottom barriers signaling a continuation.

    Parameters
    ----------
    data : List[Data]
        The data to use for the Keltner Channels calculation.
    index : str, optional
        Index column name to use with `data`, by default "date"
    length : PositiveInt, optional
        The length of the Keltner Channels, by default 20
    scalar : PositiveFloat, optional
        The scalar to use for the Keltner Channels, by default 20
    mamode : Literal["ema", "sma", "wma", "hma", "zlma"], optional
        The moving average mode to use for the Keltner Channels, by default "ema"
    offset : NonNegativeInt, optional
        The offset to use for the Keltner Channels, by default 0

    Returns
    -------
    CommandOutput[List[Data]]
        The Keltner Channels data.

    Examples
    --------
    >>> from openbb_sdk_core import openbb
    >>> stock_data = openbb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp").output
    >>> kc_data = openbb.ta.kc(data=stock_data.item, length=20, scalar=20, ma_mode="ema", offset=0)
    """

    df = to_dataframe(data, index=index)
    df_target = get_target_columns(df, ["high", "low", "close"])
    kc_df = pd.DataFrame(
        df_target.ta.kc(
            length=length,
            scalar=scalar,
            mamode=mamode,
            offset=offset,
        ).dropna()
    )

    item = from_dataframe(df_target.join(kc_df, how="left"), index=True)

    return CommandOutput(item=item)


@router.command(methods=["POST"])
def cg(
    data: List[Data], index: str = "date", length: PositiveInt = 14
) -> CommandOutput[List[Data]]:
    """
    The Center of Gravity indicator, in short, is used to anticipate future price movements
    and to trade on price reversals as soon as they happen. However, just like other oscillators,
    the COG indicator returns the best results in range-bound markets and should be avoided when
    the price is trending. Traders who use it will be able to closely speculate the upcoming
    price change of the asset.

    Parameters
    ----------
    data : List[Data]
        The data to use for the COG calculation.
    index : str, optional
        Index column name to use with `data`, by default "date"
    length : PositiveInt, optional
        The length of the COG, by default 14

    Returns
    -------
    CommandOutput[List[Data]]
        The COG data.

    Examples
    --------
    >>> from openbb_sdk_core import openbb
    >>> stock_data = openbb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp").output
    >>> cg_data = openbb.ta.cg(data=stock_data.item, length=14)
    """

    df = to_dataframe(data, index=index)
    df_target = get_target_columns(df, ["high", "low", "close"])
    cg_df = pd.DataFrame(df_target.ta.cg(length=length).dropna())

    item = from_dataframe(df_target.join(cg_df, how="left"), index=True)

    return CommandOutput(item=item)


@router.command(methods=["POST"])
def cones(
    data: List[Data],
    index: str = "date",
    lower_q: float = 0.25,
    upper_q: float = 0.75,
    model: Literal[
        "STD",
        "Parkinson",
        "Garman-Klass",
        "Hodges-Tompkins",
        "Rogers-Satchell",
        "Yang-Zhang",
    ] = "STD",
    is_crypto: bool = False,
) -> CommandOutput[List[Data]]:
    """
    Calculates the realized volatility quantiles over rolling windows of time.
    The model for calculating volatility is selectable.

    Parameters
    ----------
    data : List[Data]
        The data to use for the calculation.
    index : str, optional
        Index column name to use with `data`, by default "date"
    lower_q : float, optional
        The lower quantile value for calculations
    upper_q : float, optional
        The upper quantile value for calculations
    model : Literal["STD", "Parkinson", "Garman-Klass", "Hodges-Tompkins", "Rogers-Satchell", "Yang-Zhang"], optional
        The model used to calculate realized volatility

            Standard deviation measures how widely returns are dispersed from the average return.
            It is the most common (and biased) estimator of volatility.

            Parkinson volatility uses the high and low price of the day rather than just close to close prices.
            It is useful for capturing large price movements during the day.

            Garman-Klass volatility extends Parkinson volatility by taking into account the opening and closing price.
            As markets are most active during the opening and closing of a trading session;
            it makes volatility estimation more accurate.

            Hodges-Tompkins volatility is a bias correction for estimation using an overlapping data sample.
            It produces unbiased estimates and a substantial gain in efficiency.

            Rogers-Satchell is an estimator for measuring the volatility with an average return not equal to zero.
            Unlike Parkinson and Garman-Klass estimators, Rogers-Satchell incorporates a drift term,
            mean return not equal to zero.

            Yang-Zhang volatility is the combination of the overnight (close-to-open volatility).
            It is a weighted average of the Rogers-Satchell volatility and the open-to-close volatility.
    is_crypto : bool, optional
        Whether the data is crypto or not. If True, volatility is calculated for 365 days instead of 252

    Returns
    -------
    CommandOutput[List[Data]]
        The cones data.

    Examples
    --------
    >>> from openbb_sdk_core import openbb
    >>> stock_data = openbb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp").output
    >>> cones_data = openbb.ta.cones(data=stock_data.item, lower_q=0.25, upper_q=0.75, model="STD")
    """

    if lower_q > upper_q:
        lower_q, upper_q = upper_q, lower_q

    df = to_dataframe(data, index=index)
    df_cones = ta_helpers.calculate_cones(
        data=df, lower_q=lower_q, upper_q=upper_q, model=model, is_crypto=is_crypto
    )

    item = from_dataframe(df_cones, index=True)

    return CommandOutput(item=item)


@router.command(methods=["POST"])
def ema(
    data: List[Data],
    target: str = "close",
    index: str = "date",
    length: int = 50,
    offset: int = 0,
) -> CommandOutput[List[Data]]:
    """
    The Exponential Moving Average is a staple of technical
    analysis and is used in countless technical indicators. In a Simple Moving
    Average, each value in the time period carries equal weight, and values outside
    of the time period are not included in the average. However, the Exponential
    Moving Average is a cumulative calculation, including all data. Past values have
    a diminishing contribution to the average, while more recent values have a greater
    contribution. This method allows the moving average to be more responsive to changes
    in the data.

    Parameters
    ----------
    data : List[Data]
        The data to use for the calculation.
    target : str
        Target column name.
    index : str, optional
        Index column name to use with `data`, by default "date"
    length : int, optional
        The length of the calculation, by default 50.
    offset : int, optional
        The offset of the calculation, by default 0.

    Returns
    -------
    CommandOutput[List[Data]]
        The calculated data.

    Examples
    --------
    >>> from openbb_sdk_core import openbb
    >>> stock_data = openbb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp").output
    >>> ema_data = openbb.ta.ema(data=stock_data.item,column="close",length=50,offset=0)

    """

    def _ema_export_plotly(
        data: pd.DataFrame, ema_data: pd.DataFrame, ema_column: str, title: str
    ) -> Plotly:
        date_data = data.index.tolist()
        close_data = data[target].tolist()
        ema_data = ema_data[ema_column].tolist()

        fig = plot_timeseries(
            x=date_data,
            y=[
                YTimeSeries(data=close_data, name="Close", color="blue"),
                YTimeSeries(data=ema_data, name="EMA", color="red"),
            ],
            title=title,
            xaxis_title="Date",
            yaxis_title="Price",
            legend_title="Legend",
        )

        return Plotly(content=fig.to_plotly_json())

    df = to_dataframe(data, index=index)
    df_target = get_target_column(df, target).to_frame()
    ema_df = pd.DataFrame(df_target.ta.ema(length=length, offset=offset).dropna())

    item = from_dataframe(df_target.join(ema_df, how="left"), index=True)

    return CommandOutput(
        item=item,
        export_list=[
            _ema_export_plotly(
                data=df_target,
                ema_data=ema_df,
                ema_column=ema_df.columns[0],
                title=f"EMA {str(length)} with a offset of {str(offset)}",
            ),
        ],
    )