"""FMP Historical Dividends fetcher."""

from typing import Any, Dict, List, Optional

from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.standard_models.historical_dividends import (
    HistoricalDividendsData,
    HistoricalDividendsQueryParams,
)

from openbb_fmp.utils.helpers import create_url, get_data_many


class FMPHistoricalDividendsQueryParams(HistoricalDividendsQueryParams):
    """FMP Historical Dividends query.

    Source: https://site.financialmodelingprep.com/developer/docs/#Historical-Dividends
    """


class FMPHistoricalDividendsData(HistoricalDividendsData):
    """FMP Historical Dividends data."""

    class Config:
        """Pydantic alias config using fields dict."""

        fields = {
            "adj_dividend": "adjDividend",
            "record_date": "recordDate",
            "payment_date": "paymentDate",
            "declaration_date": "declarationDate",
        }


class FMPHistoricalDividendsFetcher(
    Fetcher[
        FMPHistoricalDividendsQueryParams,
        List[FMPHistoricalDividendsData],
    ]
):
    """Transform the query, extract and transform the data from the FMP endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FMPHistoricalDividendsQueryParams:
        """Transform the query params."""

        return FMPHistoricalDividendsQueryParams(**params)

    @staticmethod
    def extract_data(
        query: FMPHistoricalDividendsQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the FMP endpoint."""

        api_key = credentials.get("fmp_api_key") if credentials else ""

        url = create_url(
            3, f"historical-price-full/stock_dividend/{query.symbol}", api_key
        )
        return get_data_many(url, "historical", **kwargs)

    @staticmethod
    def transform_data(data: List[Dict]) -> List[FMPHistoricalDividendsData]:
        """Return the transformed data."""

        return [FMPHistoricalDividendsData(**d) for d in data]