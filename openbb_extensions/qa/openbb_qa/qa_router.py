from typing import List, Literal

import numpy as np
from openbb_sdk_core.app.utils import (
    basemodel_to_df,
    df_to_basemodel,
    get_target_column,
    get_target_columns,
)
import pandas as pd
import pandas_ta as ta
import statsmodels.api as sm
from builtin_extensions.common.qa.qa_helpers import get_fama_raw
from builtin_extensions.common.qa.qa_models import (
    ADFTestModel,
    CAPMModel,
    KPSSTestModel,
    NormalityModel,
    OmegaModel,
    SummaryModel,
    TestModel,
    UnitRootModel,
)
from openbb_provider.model.abstract.data import Data
from openbb_sdk_core.app.model.command_output import CommandOutput
from openbb_sdk_core.app.model.results.empty import Empty
from openbb_sdk_core.app.router import Router
from pydantic import NonNegativeFloat, PositiveInt
from scipy import stats
from statsmodels.tsa import stattools

router = Router(prefix="")


@router.command(methods=["POST"])
def normality(data: List[Data], target: str) -> CommandOutput[NormalityModel]:
    """
    Normality Statistics.

    - **Kurtosis**: whether the kurtosis of a sample differs from the normal distribution.
    - **Skewness**: whether the skewness of a sample differs from the normal distribution.
    - **Jarque-Bera**: whether the sample data has the skewness and kurtosis matching a normal distribution.
    - **Shapiro-Wilk**: whether a random sample comes from a normal distribution.
    - **Kolmogorov-Smirnov**: whether two underlying one-dimensional probability distributions differ.

    Parameters
    ----------
    data : List[Data]
        Time series data.
    target : str
        Target column name.

    Returns
    -------
    CommandOutput[NormalityModel]
        Normality tests summary. See qa_models.NormalityModel for details.
    """

    df = basemodel_to_df(data)
    series_target = get_target_column(df, target)

    kt_statistic, kt_pvalue = stats.kurtosistest(series_target)
    sk_statistic, sk_pvalue = stats.skewtest(series_target)
    jb_statistic, jb_pvalue = stats.jarque_bera(series_target)
    sh_statistic, sh_pvalue = stats.shapiro(series_target)
    ks_statistic, ks_pvalue = stats.kstest(series_target, "norm")

    norm_summary = NormalityModel(
        kurtosis=TestModel(statistic=kt_statistic, p_value=kt_pvalue),
        skewness=TestModel(statistic=sk_statistic, p_value=sk_pvalue),
        jarque_bera=TestModel(statistic=jb_statistic, p_value=jb_pvalue),
        shapiro_wilk=TestModel(statistic=sh_statistic, p_value=sh_pvalue),
        kolmogorov_smirnov=TestModel(statistic=ks_statistic, p_value=ks_pvalue),
    )

    return CommandOutput(results=norm_summary)


@router.command(methods=["POST"])
def capm(data: List[Data], target: str) -> CommandOutput[CAPMModel]:
    """Capital Asset Pricing Model."""

    df = basemodel_to_df(data)

    df_target = get_target_columns(df, ["date", target])
    df_target = df_target.set_index("date")
    df_target["return"] = df_target.pct_change()
    df_target = df_target.dropna()
    start_date = df_target.index.min().strftime("%Y-%m-%d")
    end_date = df_target.index.max().strftime("%Y-%m-%d")
    df_fama = get_fama_raw(start_date, end_date)
    df_target = df_target.merge(df_fama, left_index=True, right_index=True)
    df_target["excess_return"] = df_target["return"] - df_target["RF"]
    df_target["excess_mkt"] = df_target["MKT-RF"] - df_target["RF"]
    df_target = df_target.dropna()

    y = df_target[["excess_return"]]
    x = df_target["excess_mkt"]
    x = sm.add_constant(x)
    model = sm.OLS(y, x).fit()

    results = CAPMModel(
        market_risk=model.params["excess_mkt"],
        systematic_risk=model.rsquared,
        idiosyncratic_risk=1 - model.rsquared,
    )

    return CommandOutput(results=results)


@router.command(methods=["POST"])
def qqplot() -> CommandOutput[Empty]:
    """QQ Plot."""
    return CommandOutput(results=Empty())


@router.command(methods=["POST"])
def om(
    data: List[Data],
    target: str,
    threshold_start: float = 0.0,
    threshold_end: float = 1.5,
) -> CommandOutput[List[OmegaModel]]:
    """Omega Ratio.

    Parameters
    ----------
    data : List[Data]
        Time series data.
    target : str
        Target column name.
    threshold_start : float, optional
        Start threshold, by default 0.0
    threshold_end : float, optional
        End threshold, by default 1.5

    Returns
    -------
    CommandOutput[List[OmegaModel]]
        Omega ratios.
    """

    df = basemodel_to_df(data)
    series_target = get_target_column(df, target)

    def get_omega_ratio(df_target: pd.Series, threshold: float) -> float:
        """Get omega ratio."""
        daily_threshold = (threshold + 1) ** np.sqrt(1 / 252) - 1
        excess = df_target - daily_threshold
        omega = excess[excess > 0].sum() / -excess[excess < 0].sum()
        return omega

    threshold = np.linspace(threshold_start, threshold_end, 50)
    results = []
    for i in threshold:
        results.append(OmegaModel(threshold=i, omega=get_omega_ratio(series_target, i)))

    return CommandOutput(results=results)


@router.command(methods=["POST"])
def kurtosis(
    data: List[Data], target: str, window: PositiveInt
) -> CommandOutput[List[Data]]:
    """Kurtosis.

    Parameters
    ----------
    data : List[Data]
        Time series data.
    target : str
        Target column name.
    window : PositiveInt
        Window size.

    Returns
    -------
    CommandOutput[List[Data]]
        Kurtosis.
    """
    df = basemodel_to_df(data)
    series_target = get_target_column(df, target)
    results = ta.kurtosis(close=series_target, length=window).dropna()
    results = df_to_basemodel(results)

    return CommandOutput(results=results)


@router.command(methods=["POST"])
def pick() -> CommandOutput[Empty]:
    """Pick."""
    return CommandOutput(results=Empty())


@router.command(methods=["POST"])
def spread() -> CommandOutput[Empty]:
    """Spread."""
    return CommandOutput(results=Empty())


@router.command(methods=["POST"])
def rolling() -> CommandOutput[Empty]:
    """Rolling."""
    return CommandOutput(results=Empty())


@router.command(methods=["POST"])
def var() -> CommandOutput[Empty]:
    """Value at Risk."""
    return CommandOutput(results=Empty())


@router.command(methods=["POST"])
def line() -> CommandOutput[Empty]:
    """Line."""
    return CommandOutput(results=Empty())


@router.command(methods=["POST"])
def hist() -> CommandOutput[Empty]:
    """Histogram."""
    return CommandOutput(results=Empty())


@router.command(methods=["POST"])
def unitroot(
    data: List[Data],
    target: str,
    fuller_reg: Literal["c", "ct", "ctt", "nc", "c"] = "c",
    kpss_reg: Literal["c", "ct"] = "c",
) -> CommandOutput[UnitRootModel]:
    """Unit Root Test.

    Augmented Dickey-Fuller test for unit root.
    Kwiatkowski-Phillips-Schmidt-Shin test for unit root.

    Parameters
    ----------
    data : List[Data]
        Time series data.
    target : str
        Target column name.
    fuller_reg : Literal["c", "ct", "ctt", "nc", "c"]
        Regression type for ADF test.
    kpss_reg : Literal["c", "ct"]
        Regression type for KPSS test.

    Returns
    -------
    CommandOutput[UnitRootModel]
        Unit root tests summary.
    """

    df = basemodel_to_df(data)
    series_target = get_target_column(df, target)

    adf = stattools.adfuller(series_target, regression=fuller_reg)
    kpss = stattools.kpss(series_target, regression=kpss_reg, nlags="auto")

    unitroot_summary = UnitRootModel(
        adf=ADFTestModel(
            statistic=adf[0],
            p_value=adf[1],
            nlags=adf[2] if isinstance(adf[2], int) else 0,
            nobs=adf[3] if isinstance(adf[3], int) else 0,
            icbest=adf[5] if isinstance(adf[5], float) else 0.0,  # type: ignore
        ),
        kpss=KPSSTestModel(
            statistic=kpss[0],
            p_value=kpss[1],
            nlags=kpss[2],
        ),
    )
    return CommandOutput(results=unitroot_summary)


@router.command(methods=["POST"])
def beta() -> CommandOutput[Empty]:
    """Beta."""
    return CommandOutput(results=Empty())


@router.command(methods=["POST"])
def sh(
    data: List[Data], target: str, rfr: float = 0.0, window: PositiveInt = 252
) -> CommandOutput[List[Data]]:
    """Sharpe Ratio.

    Parameters
    ----------
    data : List[Data]
        Time series data.
    target : str
        Target column name.
    rfr : float, optional
        Risk-free rate, by default 0.0
    window : PositiveInt, optional
        Window size, by default 252

    Returns
    -------
    CommandOutput[List[Data]]
        Sharpe ratio.
    """

    df = basemodel_to_df(data)
    series_target = get_target_column(df, target)

    returns = series_target.pct_change().dropna().rolling(window).sum()
    std = series_target.rolling(window).std() / np.sqrt(window)
    results = ((returns - rfr) / std).dropna()

    results = df_to_basemodel(results)

    return CommandOutput(results=results)


@router.command(methods=["POST"])
def so(
    data: List[Data],
    target: str,
    target_return: float = 0.0,
    window: PositiveInt = 252,
    adjusted: bool = False,
) -> CommandOutput[List[Data]]:
    """Sortino Ratio.

    For method & terminology see: http://www.redrockcapital.com/Sortino__A__Sharper__Ratio_Red_Rock_Capital.pdf

    Parameters
    ----------
    data : List[Data]
        Time series data.
    target : str
        Target column name.
    target_return : float, optional
        Target return, by default 0.0
    window : PositiveInt, optional
        Window size, by default 252
    adjusted : bool, optional
        Adjust sortino ratio to compare it to sharpe ratio, by default False

    Returns
    -------
    CommandOutput[List[Data]]
        Sortino ratio.
    """

    df = basemodel_to_df(data)
    series_target = get_target_column(df, target)

    returns = series_target.pct_change().dropna().rolling(window).sum()
    downside_deviation = returns.rolling(window).apply(
        lambda x: (x.values[x.values < 0]).std() / np.sqrt(252) * 100
    )
    results = ((returns - target_return) / downside_deviation).dropna()

    if adjusted:
        results = result / np.sqrt(2)

    results = df_to_basemodel(results)

    return CommandOutput(results=results)


@router.command(methods=["POST"])
def cusum() -> CommandOutput[Empty]:
    """Cumulative Sum."""
    return CommandOutput(results=Empty())


@router.command(methods=["POST"])
def raw() -> CommandOutput[Empty]:
    """Raw."""
    return CommandOutput(results=Empty())


@router.command(methods=["POST"])
def cdf() -> CommandOutput[Empty]:
    """Cumulative Distribution Function."""
    return CommandOutput(results=Empty())


@router.command(methods=["POST"])
def decompose() -> CommandOutput[Empty]:
    """Decompose."""
    return CommandOutput(results=Empty())


@router.command(methods=["POST"])
def skew(
    data: List[Data], target: str, window: PositiveInt
) -> CommandOutput[List[Data]]:
    """Skewness.

    Parameters
    ----------
    data : List[Data]
        Time series data.
    target : str
        Target column name.
    window : PositiveInt
        Window size.

    Returns
    -------
    CommandOutput[List[Data]]
        Skewness.
    """
    df = basemodel_to_df(data)
    series_target = get_target_column(df, target)
    results = ta.skew(close=series_target, length=window).dropna()
    results = df_to_basemodel(results)

    return CommandOutput(results=results)


@router.command(methods=["POST"])
def quantile(
    data: List[Data],
    target: str,
    window: PositiveInt,
    quantile_pct: NonNegativeFloat = 0.5,
) -> CommandOutput[List[Data]]:
    """Quantile."""

    df = basemodel_to_df(data)
    series_target = get_target_column(df, target)

    df_median = ta.median(close=series_target, length=window).to_frame()
    df_quantile = ta.quantile(series_target, length=window, q=quantile_pct).to_frame()
    results = pd.concat([df_median, df_quantile], axis=1).dropna()

    results = df_to_basemodel(results)

    return CommandOutput(results=results)


@router.command(methods=["POST"])
def bw() -> CommandOutput[Empty]:
    """Bandwidth."""
    return CommandOutput(results=Empty())


@router.command(methods=["POST"])
def es() -> CommandOutput[Empty]:
    """Expected Shortfall."""
    return CommandOutput(results=Empty())


@router.command(methods=["POST"])
def acf() -> CommandOutput[Empty]:
    """Autocorrelation Function."""
    return CommandOutput(results=Empty())


@router.command(methods=["POST"])
def summary(data: List[Data], target: str) -> CommandOutput[SummaryModel]:
    """Summary.

    Parameters
    ----------
    data : List[Data]
        Time series data.
    target : str
        Target column name.

    Returns
    -------
    CommandOutput[SummaryModel]
        Summary table.
    """

    df = basemodel_to_df(data)
    series_target = get_target_column(df, target)

    df_stats = series_target.describe(percentiles=[0.1, 0.25, 0.5, 0.75, 0.9])
    df_stats.loc["var"] = df_stats.loc["std"] ** 2
    results = SummaryModel(
        count=df_stats.loc["count"],
        mean=df_stats.loc["mean"],
        std=df_stats.loc["std"],
        var=df_stats.loc["var"],
        min=df_stats.loc["min"],
        p_25=df_stats.loc["25%"],
        p_50=df_stats.loc["50%"],
        p_75=df_stats.loc["75%"],
        max=df_stats.loc["max"],
    )

    return CommandOutput(results=results)