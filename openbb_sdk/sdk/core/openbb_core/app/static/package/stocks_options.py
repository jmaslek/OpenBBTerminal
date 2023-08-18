### THIS FILE IS AUTO-GENERATED. DO NOT EDIT. ###

from typing import Annotated, List, Literal, Optional, Union

from pydantic import validate_arguments

import openbb_core.app.model.command_context
import openbb_core.app.model.results.empty
from openbb_core.app.model.custom_parameter import OpenBBCustomParameter
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.static.container import Container
from openbb_core.app.static.filters import filter_call, filter_inputs, filter_output


class CLASS_stocks_options(Container):
    @filter_call
    @validate_arguments
    def chains(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for."),
        ],
        chart: bool = False,
        provider: Optional[Literal["cboe"]] = None,
        **kwargs
    ) -> OBBject[List]:
        """Get the complete options chain for a ticker.

        Parameters
        ----------
        symbol : Union[str, List[str]]
            Symbol to get data for.
        chart : bool
            Whether to create a chart or not, by default False.
        provider : Optional[Literal['cboe']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'cboe' if there is
            no default.

        Returns
        -------
        OBBject
            results : List[OptionsChains]
                Serializable results.
            provider : Optional[Literal['cboe']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            error : Optional[Error]
                Caught exceptions.
            chart : Optional[Chart]
                Chart object.

        OptionsChains
        -------------
        expiration : Optional[datetime]
            Expiration date of the contract.
        strike : Optional[float]
            Strike price of the contract.
        optionType : Optional[str]
            Call or Put.
        bid : Optional[float]
            Bid price of the contract.
        ask : Optional[float]
            Ask price of the contract.
        openInterest : Optional[float]
            Open interest on the contract.
        volume : Optional[float]
            Current trading volume on the contract.
        contractSymbol : Optional[str]
            Contract symbol for the option. (provider: cboe)
        dte : Optional[int]
            Days to expiration for the option. (provider: cboe)
        bidSize : Optional[int]
            Bid size for the option. (provider: cboe)
        askSize : Optional[int]
            Ask size for the option. (provider: cboe)
        impliedVolatility : Optional[float]
            Implied volatility of the option. (provider: cboe)
        delta : Optional[float]
            Delta of the option. (provider: cboe)
        gamma : Optional[float]
            Gamma of the option. (provider: cboe)
        theta : Optional[float]
            Theta of the option. (provider: cboe)
        rho : Optional[float]
            Rho of the option. (provider: cboe)
        vega : Optional[float]
            Vega of the option. (provider: cboe)
        theoretical : Optional[float]
            Theoretical value of the option. (provider: cboe)
        open : Optional[float]
            Opening price of the option. (provider: cboe)
        high : Optional[float]
            High price of the option. (provider: cboe)
        low : Optional[float]
            Low price of the option. (provider: cboe)
        lastTradePrice : Optional[float]
            Last trade price of the option. (provider: cboe)
        tick : Optional[str]
            Whether the last tick was up or down in price. (provider: cboe)
        previousClose : Optional[float]
            Previous closing price of the option. (provider: cboe)
        change : Optional[float]
            Change in  price of the option. (provider: cboe)
        changePercent : Optional[float]
            Change, in percent, of the option. (provider: cboe)
        lastTradeTimestamp : Optional[datetime]
            Last trade timestamp of the option. (provider: cboe)"""

        inputs = filter_inputs(
            provider_choices={
                "provider": provider,
            },
            standard_params={
                "symbol": ",".join(symbol) if isinstance(symbol, list) else symbol,
            },
            extra_params=kwargs,
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/options/chains",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def eodchain(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Gets option chain at a specific date."""

        inputs = filter_inputs(
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/options/eodchain",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def hist(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Get historical data for a single option contract."""

        inputs = filter_inputs(
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/options/hist",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def info(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Display option information (volatility, IV rank, etc.)."""

        inputs = filter_inputs(
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/options/info",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def pcr(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Display historical rolling put/call ratio for ticker over a defined window."""

        inputs = filter_inputs(
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/options/pcr",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def unu(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Show unusual options activity."""

        inputs = filter_inputs(
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/options/unu",
            **inputs,
        ).output

        return filter_output(o)