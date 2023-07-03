import datetime
from typing import List, Literal, Union

from openbb_sdk_core.app.model.command_context import CommandContext
from openbb_sdk_core.app.model.command_output import CommandOutput
from openbb_sdk_core.app.model.item.empty import Empty
from openbb_sdk_core.app.provider_interface import ProviderChoices
from openbb_sdk_core.app.router import Router

datetype = Union[datetime.datetime, str]
list_str = Union[List[str], str]

groups = Literal[
    "sector",
    "industry",
    "basic_materials",
    "communication_services",
    "consumer_cyclical",
    "consumer_defensive",
    "energy",
    "financial",
    "healthcare",
    "industrials",
    "real_Estate",
    "technology",
    "utilities",
    "country",
    "capitalization",
]


router = Router(prefix="")


# Remove this once the placeholders are replaced with real commands

# pylint: disable=unused-argument


@router.command
def corecpi(
    cc: CommandContext,
    provider: ProviderChoices,
    start_date: datetype,
    end_date: datetype,
    countries: Union[List[str], str] = "united_states",
    perspective: Literal["ENRG", "FOOD", "TOT", "TOT_FOODENG"] = "TOT",
    frequency: Literal["M", "Q", "A"] = "M",
    units: Literal["AGRWTH", "IDX2015"] = "AGRWTH",
) -> CommandOutput[Empty]:  # type: ignore
    """CORECPI."""
    return CommandOutput(item=Empty())


# pylint: disable=too-many-arguments
@router.command
def cpi(
    cc: CommandContext,
    provider: ProviderChoices,
    countries: list_str,
    start_date: datetype,
    end_date: datetype,
    units: Literal["growth_previous", "growth_same", "index_2015"] = "growth_same",
    frequency: Literal["annual", "monthly", "quarterly"] = "monthly",
    harmonized: bool = False,
    smart_select: bool = True,
) -> CommandOutput[Empty]:  # type: ignore
    """CPI."""
    return CommandOutput(item=Empty())


@router.command
def cpi_options(cc: CommandContext, provider: ProviderChoices) -> CommandOutput[Empty]:
    """Get the options for v3 cpi(options=True)"""
    return CommandOutput(item=Empty())


@router.command
def index(
    cc: CommandContext,
    provider: ProviderChoices,
    indices_: list_str,  # without the underscore pylint raises "redefined-outer-name"
    start_date: datetype,
    end_date: datetype,
    interval: Literal[
        "1m",
        "2m",
        "5m",
        "15m",
        "30m",
        "60m",
        "90m",
        "1h",
        "1d",
        "5d",
        "1wk",
        "1mo",
        "3mo",
    ] = "1d",
    column: str = "close",
    returns: bool = False,
) -> CommandOutput[Empty]:  # type: ignore
    """Get index from yfinance."""
    return CommandOutput(item=Empty())


@router.command
def available_indices(
    cc: CommandContext,
    provider: ProviderChoices,
) -> CommandOutput[Empty]:
    """AVAILABLE_INDICES."""
    return CommandOutput(item=Empty())


@router.command
def macro(
    cc: CommandContext,
    provider: ProviderChoices,
    parameters: list_str,
    countries: list_str,
    transform: str,
    start_date: datetype,
    end_date: datetype,
) -> CommandOutput[Empty]:  # type: ignore
    """Query EconDB for macro data."""
    return CommandOutput(item=Empty())


@router.command
def macro_countries(
    cc: CommandContext,
    provider: ProviderChoices,
) -> CommandOutput[Empty]:
    """MACRO_COUNTRIES."""
    return CommandOutput(item=Empty())


@router.command
def macro_parameters(
    cc: CommandContext,
    provider: ProviderChoices,
) -> CommandOutput[Empty]:
    """MACRO_PARAMETERS."""
    return CommandOutput(item=Empty())


@router.command
def balance(
    cc: CommandContext,
    provider: ProviderChoices,
    countries: list_str,
    start_date: datetype,
    end_date: datetype,
) -> CommandOutput[Empty]:
    """BALANCE."""
    return CommandOutput(item=Empty())


@router.command
def bigmac(
    cc: CommandContext,
    provider: ProviderChoices,
    countries: list_str,
) -> CommandOutput[Empty]:
    """BIGMAC."""
    return CommandOutput(item=Empty())


@router.command
def country_codes(
    cc: CommandContext,
    provider: ProviderChoices,
) -> CommandOutput[Empty]:
    """COUNTRY_CODES."""
    return CommandOutput(item=Empty())


@router.command
def currencies(
    cc: CommandContext,
    provider: ProviderChoices,
) -> CommandOutput[Empty]:
    """CURRENCIES."""
    return CommandOutput(item=Empty())


@router.command
def debt(
    cc: CommandContext,
    provider: ProviderChoices,
    countries: list_str,
    start_date: datetype,
    end_date: datetype,
) -> CommandOutput[Empty]:
    """DEBT."""
    return CommandOutput(item=Empty())


@router.command
def events(
    cc: CommandContext,
    provider: ProviderChoices,
    countries: list_str,
    start_date: datetype,
    end_date: datetype,
) -> CommandOutput[Empty]:
    """EVENTS."""
    return CommandOutput(item=Empty())


@router.command
def fgdp(
    cc: CommandContext,
    provider: ProviderChoices,
    countries: list_str,
    start_date: datetype,
    end_date: datetype,
    type_: Literal["real", "nominal"] = "real",  # type is a reserved word
    units: Literal["Q", "A"] = "A",
) -> CommandOutput[Empty]:
    """FGDP."""
    return CommandOutput(item=Empty())


@router.command
def fred(
    cc: CommandContext,
    provider: ProviderChoices,
    series_id: list_str,
    start_date: datetype,
    end_date: datetype,
) -> CommandOutput[Empty]:
    """FRED."""
    return CommandOutput(item=Empty())


@router.command
def fred_search(
    cc: CommandContext, provider: ProviderChoices, term: str
) -> CommandOutput[Empty]:
    """FRED Search (was fred_notes)."""
    return CommandOutput(item=Empty())


@router.command
def futures(
    cc: CommandContext,
    provider: ProviderChoices,
    future_type: Literal[
        "Indices", "Energy", "Metals", "Meats", "Grains", "Softs", "Bonds", "Currencies"
    ],
) -> CommandOutput[Empty]:
    """FUTURES. 2 sources"""
    return CommandOutput(item=Empty())


@router.command
def gdp(
    cc: CommandContext,
    provider: ProviderChoices,
    countries: list_str,
    start_date: datetype,
    end_date: datetype,
    units: Literal["USD_CAP", "MLN_USD"] = "USD_CAP",
) -> CommandOutput[Empty]:
    """GDP."""
    return CommandOutput(item=Empty())


@router.command
def glbonds(
    cc: CommandContext,
    provider: ProviderChoices,
) -> CommandOutput[Empty]:
    """GLBONDS."""
    return CommandOutput(item=Empty())


@router.command
def indices(
    cc: CommandContext,
    provider: ProviderChoices,
) -> CommandOutput[Empty]:
    """INDICES."""
    return CommandOutput(item=Empty())


@router.command
def overview(
    cc: CommandContext,
    provider: ProviderChoices,
) -> CommandOutput[Empty]:
    """OVERVIEW."""
    return CommandOutput(item=Empty())


@router.command
def perfmap(
    cc: CommandContext, provider: ProviderChoices, group: groups
) -> CommandOutput[Empty]:
    """PERFMAP."""
    return CommandOutput(item=Empty())


@router.command
def performance(
    cc: CommandContext, provider: ProviderChoices, group: groups
) -> CommandOutput[Empty]:
    """PERFORMANCE."""
    return CommandOutput(item=Empty())


@router.command
def revenue(
    cc: CommandContext,
    provider: ProviderChoices,
    countries: list_str,
    start_date: datetype,
    end_date: datetype,
    units: Literal["PC_GDP", "THOUSAND_USD_PER_CAPITA"] = "PC_GDP",
) -> CommandOutput[Empty]:
    """REVENUE."""
    return CommandOutput(item=Empty())


@router.command
def rgdp(
    cc: CommandContext,
    provider: ProviderChoices,
    countries: list_str,
    start_date: datetype,
    end_date: datetype,
    units: Literal["IDX", "PC_CHGPP", "PC_CHGPY"],
) -> CommandOutput[Empty]:
    """RGDP."""
    return CommandOutput(item=Empty())


@router.command
def rtps(
    cc: CommandContext,
    provider: ProviderChoices,
) -> CommandOutput[Empty]:
    """RTPS."""
    return CommandOutput(item=Empty())


@router.command
def search_index(
    cc: CommandContext, provider: ProviderChoices, keyword: str
) -> CommandOutput[Empty]:
    """SEARCH_INDEX."""
    return CommandOutput(item=Empty())


@router.command
def spending(
    cc: CommandContext,
    provider: ProviderChoices,
    countries: list_str,
    start_date: datetype,
    end_date: datetype,
    units: Literal["PC_GDP", "THOUSAND_USD_PER_CAPITA"] = "PC_GDP",
    perspective: Literal[
        "TOT",
        "RECULTREL",
        "HOUCOMM",
        "PUBORN",
        "EDU",
        "ENVPORT",
        "GRALPUBSER",
        "SOCPROT",
        "ECOAFF",
        "DEF",
        "HEALTH",
    ] = "TOT",
) -> CommandOutput[Empty]:
    """SPENDING."""
    return CommandOutput(item=Empty())


@router.command
def trust(
    cc: CommandContext,
    provider: ProviderChoices,
    countries: list_str,
    start_date: datetype,
    end_date: datetype,
) -> CommandOutput[Empty]:
    """TRUST."""
    return CommandOutput(item=Empty())


@router.command
def usbonds(
    cc: CommandContext,
    provider: ProviderChoices,
) -> CommandOutput[Empty]:
    """USBONDS."""
    return CommandOutput(item=Empty())


@router.command
def valuation(
    cc: CommandContext, provider: ProviderChoices, group: groups
) -> CommandOutput[Empty]:
    """VALUATION."""
    return CommandOutput(item=Empty())