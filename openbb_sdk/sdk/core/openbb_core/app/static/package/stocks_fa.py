### THIS FILE IS AUTO-GENERATED. DO NOT EDIT. ###

import datetime
from typing import Annotated, List, Literal, Optional, Union

import pydantic
import pydantic.main
from pydantic import BaseModel, validate_arguments

import openbb_core.app.model.command_context
import openbb_core.app.model.results.empty
from openbb_core.app.model.custom_parameter import OpenBBCustomParameter
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.static.container import Container
from openbb_core.app.static.filters import filter_call, filter_inputs, filter_output


class CLASS_stocks_fa(Container):
    @filter_call
    @validate_arguments
    def analysis(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Analyse SEC filings with the help of machine learning."""

        inputs = filter_inputs(
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/analysis",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def balance(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for."),
        ],
        period: Annotated[
            Literal["annually", "quarterly"],
            OpenBBCustomParameter(description="Period of the data to return."),
        ] = "annually",
        limit: Annotated[
            Optional[pydantic.types.NonNegativeInt],
            OpenBBCustomParameter(description="The number of data entries to return."),
        ] = 12,
        chart: bool = False,
        provider: Optional[Literal["fmp", "polygon"]] = None,
        **kwargs
    ) -> OBBject[List]:
        """Balance Sheet.

        Parameters
        ----------
        symbol : Union[str, List[str]]
            Symbol to get data for.
        period : Literal['annually', 'quarterly']
            Period of the data to return.
        limit : Optional[pydantic.types.NonNegativeInt]
            The number of data entries to return.
        chart : bool
            Whether to create a chart or not, by default False.
        provider : Optional[Literal['fmp', 'polygon']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.
        cik : Optional[str]
            None
        company_name : Optional[str]
            Name of the company. (provider: polygon)
        company_name_search : Optional[str]
            Name of the company to search. (provider: polygon)
        sic : Optional[str]
            The Standard Industrial Classification (SIC) of the company. (provider: polygon)
        filing_date : Optional[datetime.date]
            Filing date of the financial statement. (provider: polygon)
        filing_date_lt : Optional[datetime.date]
            Filing date less than the given date. (provider: polygon)
        filing_date_lte : Optional[datetime.date]
            Filing date less than or equal to the given date. (provider: polygon)
        filing_date_gt : Optional[datetime.date]
            Filing date greater than the given date. (provider: polygon)
        filing_date_gte : Optional[datetime.date]
            Filing date greater than or equal to the given date. (provider: polygon)
        period_of_report_date : Optional[datetime.date]
            Period of report date of the financial statement. (provider: polygon)
        period_of_report_date_lt : Optional[datetime.date]
            Period of report date less than the given date. (provider: polygon)
        period_of_report_date_lte : Optional[datetime.date]
            Period of report date less than or equal to the given date. (provider: polygon)
        period_of_report_date_gt : Optional[datetime.date]
            Period of report date greater than the given date. (provider: polygon)
        period_of_report_date_gte : Optional[datetime.date]
            Period of report date greater than or equal to the given date. (provider: polygon)
        include_sources : Optional[bool]
            Whether to include the sources of the financial statement. (provider: polygon)
        order : Optional[Literal['asc', 'desc']]
            Order of the financial statement. (provider: polygon)
        sort : Optional[Literal['filing_date', 'period_of_report_date']]
            Sort of the financial statement. (provider: polygon)

        Returns
        -------
        OBBject
            results : List[BalanceSheet]
                Serializable results.
            provider : Optional[Literal['fmp', 'polygon']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            error : Optional[Error]
                Caught exceptions.
            chart : Optional[Chart]
                Chart object.

        BalanceSheet
        ------------
        date : Optional[date]
            Date of the fetched statement.
        symbol : Optional[str]
            Symbol of the company.
        cik : Optional[int]
            Central Index Key.
        currency : Optional[str]
            Reporting currency.
        filing_date : Optional[date]
            Filling date.
        accepted_date : Optional[datetime]
            Accepted date.
        period : Optional[str]
            Reporting period of the statement.
        cash_and_cash_equivalents : Optional[int]
            Cash and cash equivalents
        short_term_investments : Optional[int]
            Short-term investments
        inventory : Optional[int]
            Inventory
        net_receivables : Optional[int]
            Receivables, net
        other_current_assets : Optional[int]
            Other current assets
        current_assets : Optional[int]
            Total current assets
        long_term_investments : Optional[int]
            Long-term investments
        property_plant_equipment_net : Optional[int]
            Property, plant and equipment, net
        goodwill : Optional[int]
            Goodwill
        intangible_assets : Optional[int]
            Intangible assets
        other_non_current_assets : Optional[int]
            Other non-current assets
        tax_assets : Optional[int]
            Accrued income taxes
        other_assets : Optional[int]
            Other assets
        noncurrent_assets : Optional[int]
            None
        assets : Optional[int]
            None
        account_payables : Optional[int]
            None
        other_current_liabilities : Optional[int]
            None
        tax_payables : Optional[int]
            Accrued income taxes
        deferred_revenue : Optional[int]
            Accrued income taxes, other deferred revenue
        short_term_debt : Optional[int]
            Short-term borrowings, Long-term debt due within one year, Operating lease obligations due within one year, Finance lease obligations due within one year
        current_liabilities : Optional[int]
            None
        long_term_debt : Optional[int]
            Long-term debt, Operating lease obligations, Long-term finance lease obligations
        other_non_current_liabilities : Optional[int]
            Deferred income taxes and other
        other_liabilities : Optional[int]
            None
        noncurrent_liabilities : Optional[int]
            None
        liabilities : Optional[int]
            None
        common_stock : Optional[int]
            None
        other_stockholder_equity : Optional[int]
            Capital in excess of par value
        accumulated_other_comprehensive_income_loss : Optional[int]
            Accumulated other comprehensive income (loss)
        preferred_stock : Optional[int]
            Preferred stock
        retained_earnings : Optional[int]
            Retained earnings
        minority_interest : Optional[int]
            Minority interest
        total_stockholders_equity : Optional[int]
            None
        total_equity : Optional[int]
            None
        total_liabilities_and_stockholders_equity : Optional[int]
            None
        total_liabilities_and_total_equity : Optional[int]
            None
        calendarYear : Optional[int]
            None
        link : Optional[str]
            None
        finalLink : Optional[str]
            None
        cashAndShortTermInvestments : Optional[int]
            None
        goodwillAndIntangibleAssets : Optional[int]
            None
        deferredRevenueNonCurrent : Optional[int]
            None
        totalInvestments : Optional[int]
            None
        capitalLeaseObligations : Optional[int]
            None
        deferredTaxLiabilitiesNonCurrent : Optional[int]
            None
        totalNonCurrentLiabilities : Optional[int]
            None
        totalDebt : Optional[int]
            None
        netDebt : Optional[int]
            None"""

        inputs = filter_inputs(
            provider_choices={
                "provider": provider,
            },
            standard_params={
                "symbol": ",".join(symbol) if isinstance(symbol, list) else symbol,
                "period": period,
                "limit": limit,
            },
            extra_params=kwargs,
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/balance",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def balance_growth(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for."),
        ],
        limit: Annotated[
            int,
            OpenBBCustomParameter(description="The number of data entries to return."),
        ] = 10,
        chart: bool = False,
        provider: Optional[Literal["fmp"]] = None,
        **kwargs
    ) -> OBBject[List]:
        """Balance Sheet Statement Growth.

        Parameters
        ----------
        symbol : Union[str, List[str]]
            Symbol to get data for.
        limit : int
            The number of data entries to return.
        chart : bool
            Whether to create a chart or not, by default False.
        provider : Optional[Literal['fmp']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.

        Returns
        -------
        OBBject
            results : List[BalanceSheetGrowth]
                Serializable results.
            provider : Optional[Literal['fmp']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            error : Optional[Error]
                Caught exceptions.
            chart : Optional[Chart]
                Chart object.

        BalanceSheetGrowth
        ------------------
        symbol : Optional[str]
            Symbol to get data for.
        date : Optional[date]
            The date of the data.
        period : Optional[str]
            Reporting period.
        growth_cash_and_cash_equivalents : Optional[float]
            Growth rate of cash and cash equivalents.
        growth_short_term_investments : Optional[float]
            Growth rate of short-term investments.
        growth_cash_and_short_term_investments : Optional[float]
            Growth rate of cash and short-term investments.
        growth_net_receivables : Optional[float]
            Growth rate of net receivables.
        growth_inventory : Optional[float]
            Growth rate of inventory.
        growth_other_current_assets : Optional[float]
            Growth rate of other current assets.
        growth_total_current_assets : Optional[float]
            Growth rate of total current assets.
        growth_property_plant_equipment_net : Optional[float]
            Growth rate of net property, plant, and equipment.
        growth_goodwill : Optional[float]
            Growth rate of goodwill.
        growth_intangible_assets : Optional[float]
            Growth rate of intangible assets.
        growth_goodwill_and_intangible_assets : Optional[float]
            Growth rate of goodwill and intangible assets.
        growth_long_term_investments : Optional[float]
            Growth rate of long-term investments.
        growth_tax_assets : Optional[float]
            Growth rate of tax assets.
        growth_other_non_current_assets : Optional[float]
            Growth rate of other non-current assets.
        growth_total_non_current_assets : Optional[float]
            Growth rate of total non-current assets.
        growth_other_assets : Optional[float]
            Growth rate of other assets.
        growth_total_assets : Optional[float]
            Growth rate of total assets.
        growth_account_payables : Optional[float]
            Growth rate of accounts payable.
        growth_short_term_debt : Optional[float]
            Growth rate of short-term debt.
        growth_tax_payables : Optional[float]
            Growth rate of tax payables.
        growth_deferred_revenue : Optional[float]
            Growth rate of deferred revenue.
        growth_other_current_liabilities : Optional[float]
            Growth rate of other current liabilities.
        growth_total_current_liabilities : Optional[float]
            Growth rate of total current liabilities.
        growth_long_term_debt : Optional[float]
            Growth rate of long-term debt.
        growth_deferred_revenue_non_current : Optional[float]
            Growth rate of non-current deferred revenue.
        growth_deferrred_tax_liabilities_non_current : Optional[float]
            Growth rate of non-current deferred tax liabilities.
        growth_other_non_current_liabilities : Optional[float]
            Growth rate of other non-current liabilities.
        growth_total_non_current_liabilities : Optional[float]
            Growth rate of total non-current liabilities.
        growth_other_liabilities : Optional[float]
            Growth rate of other liabilities.
        growth_total_liabilities : Optional[float]
            Growth rate of total liabilities.
        growth_common_stock : Optional[float]
            Growth rate of common stock.
        growth_retained_earnings : Optional[float]
            Growth rate of retained earnings.
        growth_accumulated_other_comprehensive_income_loss : Optional[float]
            Growth rate of accumulated other comprehensive income/loss.
        growth_othertotal_stockholders_equity : Optional[float]
            Growth rate of other total stockholders' equity.
        growth_total_stockholders_equity : Optional[float]
            Growth rate of total stockholders' equity.
        growth_total_liabilities_and_stockholders_equity : Optional[float]
            Growth rate of total liabilities and stockholders' equity.
        growth_total_investments : Optional[float]
            Growth rate of total investments.
        growth_total_debt : Optional[float]
            Growth rate of total debt.
        growth_net_debt : Optional[float]
            Growth rate of net debt."""

        inputs = filter_inputs(
            provider_choices={
                "provider": provider,
            },
            standard_params={
                "symbol": ",".join(symbol) if isinstance(symbol, list) else symbol,
                "limit": limit,
            },
            extra_params=kwargs,
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/balance_growth",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def cal(
        self,
        start_date: Annotated[
            Union[datetime.date, None, str],
            OpenBBCustomParameter(
                description="Start date of the data, in YYYY-MM-DD format."
            ),
        ] = None,
        end_date: Annotated[
            Union[datetime.date, None, str],
            OpenBBCustomParameter(
                description="End date of the data, in YYYY-MM-DD format."
            ),
        ] = None,
        chart: bool = False,
        provider: Optional[Literal["fmp"]] = None,
        **kwargs
    ) -> OBBject[List]:
        """Show Dividend Calendar for a given start and end dates.

        Parameters
        ----------
        start_date : Union[datetime.date, NoneType, str]
            Start date of the data, in YYYY-MM-DD format.
        end_date : Union[datetime.date, NoneType, str]
            End date of the data, in YYYY-MM-DD format.
        chart : bool
            Whether to create a chart or not, by default False.
        provider : Optional[Literal['fmp']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.

        Returns
        -------
        OBBject
            results : List[DividendCalendar]
                Serializable results.
            provider : Optional[Literal['fmp']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            error : Optional[Error]
                Caught exceptions.
            chart : Optional[Chart]
                Chart object.

        DividendCalendar
        ----------------
        symbol : Optional[str]
            Symbol to get data for.
        date : Optional[date]
            The date of the data.
        label : Optional[str]
            Date in human readable form in the calendar.
        adj_dividend : Optional[NonNegativeFloat]
            Adjusted dividend on a date in the calendar.
        dividend : Optional[NonNegativeFloat]
            Dividend amount in the calendar.
        record_date : Optional[date]
            Record date of the dividend in the calendar.
        payment_date : Optional[date]
            Payment date of the dividend in the calendar.
        declaration_date : Optional[date]
            Declaration date of the dividend in the calendar."""

        inputs = filter_inputs(
            provider_choices={
                "provider": provider,
            },
            standard_params={
                "start_date": start_date,
                "end_date": end_date,
            },
            extra_params=kwargs,
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/cal",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def cash(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for."),
        ],
        period: Annotated[
            Literal["annually", "quarterly"],
            OpenBBCustomParameter(description="Period of the data to return."),
        ] = "annually",
        limit: Annotated[
            Optional[pydantic.types.NonNegativeInt],
            OpenBBCustomParameter(description="The number of data entries to return."),
        ] = 12,
        chart: bool = False,
        provider: Optional[Literal["fmp", "polygon"]] = None,
        **kwargs
    ) -> OBBject[List]:
        """Cash Flow Statement.

        Parameters
        ----------
        symbol : Union[str, List[str]]
            Symbol to get data for.
        period : Literal['annually', 'quarterly']
            Period of the data to return.
        limit : Optional[pydantic.types.NonNegativeInt]
            The number of data entries to return.
        chart : bool
            Whether to create a chart or not, by default False.
        provider : Optional[Literal['fmp', 'polygon']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.
        cik : Optional[str]
            Central Index Key (CIK) of the company. (provider: fmp)
        company_name : Optional[str]
            Name of the company. (provider: polygon)
        company_name_search : Optional[str]
            Name of the company to search. (provider: polygon)
        sic : Optional[str]
            The Standard Industrial Classification (SIC) of the company. (provider: polygon)
        filing_date : Optional[datetime.date]
            Filing date of the financial statement. (provider: polygon)
        filing_date_lt : Optional[datetime.date]
            Filing date less than the given date. (provider: polygon)
        filing_date_lte : Optional[datetime.date]
            Filing date less than or equal to the given date. (provider: polygon)
        filing_date_gt : Optional[datetime.date]
            Filing date greater than the given date. (provider: polygon)
        filing_date_gte : Optional[datetime.date]
            Filing date greater than or equal to the given date. (provider: polygon)
        period_of_report_date : Optional[datetime.date]
            Period of report date of the financial statement. (provider: polygon)
        period_of_report_date_lt : Optional[datetime.date]
            Period of report date less than the given date. (provider: polygon)
        period_of_report_date_lte : Optional[datetime.date]
            Period of report date less than or equal to the given date. (provider: polygon)
        period_of_report_date_gt : Optional[datetime.date]
            Period of report date greater than the given date. (provider: polygon)
        period_of_report_date_gte : Optional[datetime.date]
            Period of report date greater than or equal to the given date. (provider: polygon)
        include_sources : Optional[bool]
            Whether to include the sources of the financial statement. (provider: polygon)
        order : Optional[Literal['asc', 'desc']]
            Order of the financial statement. (provider: polygon)
        sort : Optional[Literal['filing_date', 'period_of_report_date']]
            Sort of the financial statement. (provider: polygon)

        Returns
        -------
        OBBject
            results : List[CashFlowStatement]
                Serializable results.
            provider : Optional[Literal['fmp', 'polygon']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            error : Optional[Error]
                Caught exceptions.
            chart : Optional[Chart]
                Chart object.

        CashFlowStatement
        -----------------
        date : Optional[date]
            Date of the fetched statement.
        symbol : Optional[str]
            Symbol of the company.
        cik : Optional[int]
            Central Index Key.
        currency : Optional[str]
            Reporting currency.
        filing_date : Optional[date]
            Filling date.
        accepted_date : Optional[datetime]
            Accepted date.
        period : Optional[str]
            Reporting period of the statement.
        cash_at_beginning_of_period : Optional[int]
            Cash at beginning of period.
        net_income : Optional[int]
            Net income.
        depreciation_and_amortization : Optional[int]
            Depreciation and amortization.
        stock_based_compensation : Optional[int]
            Stock based compensation.
        other_non_cash_items : Optional[int]
            Other non-cash items.
        deferred_income_tax : Optional[int]
            Deferred income tax.
        inventory : Optional[int]
            Inventory.
        accounts_payables : Optional[int]
            Accounts payables.
        accounts_receivables : Optional[int]
            Accounts receivables.
        change_in_working_capital : Optional[int]
            Change in working capital.
        other_working_capital : Optional[int]
            Accrued expenses and other, Unearned revenue.
        capital_expenditure : Optional[int]
            Purchases of property and equipment.
        other_investing_activities : Optional[int]
            Proceeds from property and equipment sales and incentives.
        acquisitions_net : Optional[int]
            Acquisitions, net of cash acquired, and other
        sales_maturities_of_investments : Optional[int]
            Sales and maturities of investments.
        purchases_of_investments : Optional[int]
            Purchases of investments.
        net_cash_flow_from_operating_activities : Optional[int]
            Net cash flow from operating activities.
        net_cash_flow_from_investing_activities : Optional[int]
            Net cash flow from investing activities.
        net_cash_flow_from_financing_activities : Optional[int]
            Net cash flow from financing activities.
        investments_in_property_plant_and_equipment : Optional[int]
            Investments in property, plant, and equipment.
        net_cash_used_for_investing_activities : Optional[int]
            Net cash used for investing activities.
        effect_of_forex_changes_on_cash : Optional[int]
            Foreign currency effect on cash, cash equivalents, and restricted cash
        dividends_paid : Optional[int]
            Payments for dividends and dividend equivalents
        common_stock_issued : Optional[int]
            Proceeds from issuance of common stock
        common_stock_repurchased : Optional[int]
            Payments related to repurchase of common stock
        debt_repayment : Optional[int]
            Payments of long-term debt
        other_financing_activities : Optional[int]
            Other financing activities, net
        net_change_in_cash : Optional[int]
            Net increase (decrease) in cash, cash equivalents, and restricted cash
        cash_at_end_of_period : Optional[int]
            Cash, cash equivalents, and restricted cash at end of period
        free_cash_flow : Optional[int]
            Net cash flow from operating, investing and financing activities
        operating_cash_flow : Optional[int]
            Net cash flow from operating activities
        calendar_year : Optional[int]
            Calendar Year (provider: fmp)
        link : Optional[str]
            None
        final_link : Optional[str]
            Final Link (provider: fmp)"""

        inputs = filter_inputs(
            provider_choices={
                "provider": provider,
            },
            standard_params={
                "symbol": ",".join(symbol) if isinstance(symbol, list) else symbol,
                "period": period,
                "limit": limit,
            },
            extra_params=kwargs,
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/cash",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def cash_growth(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for."),
        ],
        limit: Annotated[
            int,
            OpenBBCustomParameter(description="The number of data entries to return."),
        ] = 10,
        chart: bool = False,
        provider: Optional[Literal["fmp"]] = None,
        **kwargs
    ) -> OBBject[List]:
        """Cash Flow Statement Growth.

        Parameters
        ----------
        symbol : Union[str, List[str]]
            Symbol to get data for.
        limit : int
            The number of data entries to return.
        chart : bool
            Whether to create a chart or not, by default False.
        provider : Optional[Literal['fmp']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.

        Returns
        -------
        OBBject
            results : List[CashFlowStatementGrowth]
                Serializable results.
            provider : Optional[Literal['fmp']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            error : Optional[Error]
                Caught exceptions.
            chart : Optional[Chart]
                Chart object.

        CashFlowStatementGrowth
        -----------------------
        symbol : Optional[str]
            Symbol to get data for.
        date : Optional[date]
            The date of the data.
        period : Optional[str]
            Period the statement is returned for.
        growth_net_income : Optional[float]
            Growth rate of net income.
        growth_depreciation_and_amortization : Optional[float]
            Growth rate of depreciation and amortization.
        growth_deferred_income_tax : Optional[float]
            Growth rate of deferred income tax.
        growth_stock_based_compensation : Optional[float]
            Growth rate of stock-based compensation.
        growth_change_in_working_capital : Optional[float]
            Growth rate of change in working capital.
        growth_accounts_receivables : Optional[float]
            Growth rate of accounts receivables.
        growth_inventory : Optional[float]
            Growth rate of inventory.
        growth_accounts_payables : Optional[float]
            Growth rate of accounts payables.
        growth_other_working_capital : Optional[float]
            Growth rate of other working capital.
        growth_other_non_cash_items : Optional[float]
            Growth rate of other non-cash items.
        growth_net_cash_provided_by_operating_activities : Optional[float]
            Growth rate of net cash provided by operating activities.
        growth_investments_in_property_plant_and_equipment : Optional[float]
            Growth rate of investments in property, plant, and equipment.
        growth_acquisitions_net : Optional[float]
            Growth rate of net acquisitions.
        growth_purchases_of_investments : Optional[float]
            Growth rate of purchases of investments.
        growth_sales_maturities_of_investments : Optional[float]
            Growth rate of sales maturities of investments.
        growth_other_investing_activities : Optional[float]
            Growth rate of other investing activities.
        growth_net_cash_used_for_investing_activities : Optional[float]
            Growth rate of net cash used for investing activities.
        growth_debt_repayment : Optional[float]
            Growth rate of debt repayment.
        growth_common_stock_issued : Optional[float]
            Growth rate of common stock issued.
        growth_common_stock_repurchased : Optional[float]
            Growth rate of common stock repurchased.
        growth_dividends_paid : Optional[float]
            Growth rate of dividends paid.
        growth_other_financing_activities : Optional[float]
            Growth rate of other financing activities.
        growth_net_cash_used_provided_by_financing_activities : Optional[float]
            Growth rate of net cash used/provided by financing activities.
        growth_effect_of_forex_changes_on_cash : Optional[float]
            Growth rate of the effect of foreign exchange changes on cash.
        growth_net_change_in_cash : Optional[float]
            Growth rate of net change in cash.
        growth_cash_at_end_of_period : Optional[float]
            Growth rate of cash at the end of the period.
        growth_cash_at_beginning_of_period : Optional[float]
            Growth rate of cash at the beginning of the period.
        growth_operating_cash_flow : Optional[float]
            Growth rate of operating cash flow.
        growth_capital_expenditure : Optional[float]
            Growth rate of capital expenditure.
        growth_free_cash_flow : Optional[float]
            Growth rate of free cash flow."""

        inputs = filter_inputs(
            provider_choices={
                "provider": provider,
            },
            standard_params={
                "symbol": ",".join(symbol) if isinstance(symbol, list) else symbol,
                "limit": limit,
            },
            extra_params=kwargs,
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/cash_growth",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def comp(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for."),
        ],
        chart: bool = False,
        provider: Optional[Literal["fmp"]] = None,
        **kwargs
    ) -> OBBject[List]:
        """Executive Compensation.

        Parameters
        ----------
        symbol : Union[str, List[str]]
            Symbol to get data for.
        chart : bool
            Whether to create a chart or not, by default False.
        provider : Optional[Literal['fmp']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.

        Returns
        -------
        OBBject
            results : List[ExecutiveCompensation]
                Serializable results.
            provider : Optional[Literal['fmp']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            error : Optional[Error]
                Caught exceptions.
            chart : Optional[Chart]
                Chart object.

        ExecutiveCompensation
        ---------------------
        symbol : Optional[str]
            Symbol to get data for.
        cik : Optional[str]
            Central Index Key (CIK) of the company.
        filing_date : Optional[date]
            Date of the filing.
        accepted_date : Optional[datetime]
            Date the filing was accepted.
        name_and_position : Optional[str]
            Name and position of the executive.
        year : Optional[int]
            Year of the compensation.
        salary : Optional[PositiveFloat]
            Salary of the executive.
        bonus : Optional[NonNegativeFloat]
            Bonus of the executive.
        stock_award : Optional[NonNegativeFloat]
            Stock award of the executive.
        incentive_plan_compensation : Optional[NonNegativeFloat]
            Incentive plan compensation of the executive.
        all_other_compensation : Optional[NonNegativeFloat]
            All other compensation of the executive.
        total : Optional[PositiveFloat]
            Total compensation of the executive.
        url : Optional[str]
            URL of the filing data."""

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
            "/stocks/fa/comp",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def comsplit(
        self,
        start_date: Annotated[
            Union[datetime.date, None, str],
            OpenBBCustomParameter(
                description="Start date of the data, in YYYY-MM-DD format."
            ),
        ] = None,
        end_date: Annotated[
            Union[datetime.date, None, str],
            OpenBBCustomParameter(
                description="End date of the data, in YYYY-MM-DD format."
            ),
        ] = None,
        chart: bool = False,
        provider: Optional[Literal["fmp"]] = None,
        **kwargs
    ) -> OBBject[List]:
        """Stock Split Calendar.

        Parameters
        ----------
        start_date : Union[datetime.date, NoneType, str]
            Start date of the data, in YYYY-MM-DD format.
        end_date : Union[datetime.date, NoneType, str]
            End date of the data, in YYYY-MM-DD format.
        chart : bool
            Whether to create a chart or not, by default False.
        provider : Optional[Literal['fmp']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.

        Returns
        -------
        OBBject
            results : List[StockSplitCalendar]
                Serializable results.
            provider : Optional[Literal['fmp']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            error : Optional[Error]
                Caught exceptions.
            chart : Optional[Chart]
                Chart object.

        StockSplitCalendar
        ------------------
        date : Optional[date]
            Date of the stock splits.
        label : Optional[str]
            Label of the stock splits.
        symbol : Optional[str]
            Symbol of the company.
        numerator : Optional[float]
            Numerator of the stock splits.
        denominator : Optional[float]
            Denominator of the stock splits."""

        inputs = filter_inputs(
            provider_choices={
                "provider": provider,
            },
            standard_params={
                "start_date": start_date,
                "end_date": end_date,
            },
            extra_params=kwargs,
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/comsplit",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def customer(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """List of customers of the company."""

        inputs = filter_inputs(
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/customer",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def dcfc(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Determine the (historical) discounted cash flow."""

        inputs = filter_inputs(
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/dcfc",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def divs(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for."),
        ],
        chart: bool = False,
        provider: Optional[Literal["fmp"]] = None,
        **kwargs
    ) -> OBBject[List]:
        """Historical Dividends.

        Parameters
        ----------
        symbol : Union[str, List[str]]
            Symbol to get data for.
        chart : bool
            Whether to create a chart or not, by default False.
        provider : Optional[Literal['fmp']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.

        Returns
        -------
        OBBject
            results : List[HistoricalDividends]
                Serializable results.
            provider : Optional[Literal['fmp']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            error : Optional[Error]
                Caught exceptions.
            chart : Optional[Chart]
                Chart object.

        HistoricalDividends
        -------------------
        date : Optional[date]
            Date of the historical dividends.
        label : Optional[str]
            Label of the historical dividends.
        adj_dividend : Optional[float]
            Adjusted dividend of the historical dividends.
        dividend : Optional[float]
            Dividend of the historical dividends.
        record_date : Optional[date]
            Record date of the historical dividends.
        payment_date : Optional[date]
            Payment date of the historical dividends.
        declaration_date : Optional[date]
            Declaration date of the historical dividends."""

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
            "/stocks/fa/divs",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def dupont(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Detailed breakdown for Return on Equity (RoE)."""

        inputs = filter_inputs(
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/dupont",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def earning(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for."),
        ],
        limit: Annotated[
            Optional[int],
            OpenBBCustomParameter(description="The number of data entries to return."),
        ] = 50,
        chart: bool = False,
        provider: Optional[Literal["fmp"]] = None,
        **kwargs
    ) -> OBBject[List]:
        """Earnings Calendar.

        Parameters
        ----------
        symbol : Union[str, List[str]]
            Symbol to get data for.
        limit : Optional[int]
            The number of data entries to return.
        chart : bool
            Whether to create a chart or not, by default False.
        provider : Optional[Literal['fmp']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.

        Returns
        -------
        OBBject
            results : List[EarningsCalendar]
                Serializable results.
            provider : Optional[Literal['fmp']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            error : Optional[Error]
                Caught exceptions.
            chart : Optional[Chart]
                Chart object.

        EarningsCalendar
        ----------------
        symbol : Optional[str]
            Symbol to get data for.
        date : Optional[date]
            The date of the data.
        eps : Optional[NonNegativeFloat]
            EPS of the earnings calendar.
        eps_estimated : Optional[NonNegativeFloat]
            Estimated EPS of the earnings calendar.
        time : Optional[str]
            Time of the earnings calendar.
        revenue : Optional[int]
            Revenue of the earnings calendar.
        revenue_estimated : Optional[int]
            Estimated revenue of the earnings calendar.
        updated_from_date : Optional[date]
            Updated from date of the earnings calendar.
        fiscal_date_ending : Optional[date]
            Fiscal date ending of the earnings calendar."""

        inputs = filter_inputs(
            provider_choices={
                "provider": provider,
            },
            standard_params={
                "symbol": ",".join(symbol) if isinstance(symbol, list) else symbol,
                "limit": limit,
            },
            extra_params=kwargs,
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/earning",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def emp(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for."),
        ],
        chart: bool = False,
        provider: Optional[Literal["fmp"]] = None,
        **kwargs
    ) -> OBBject[List]:
        """Number of Employees.

        Parameters
        ----------
        symbol : Union[str, List[str]]
            Symbol to get data for.
        chart : bool
            Whether to create a chart or not, by default False.
        provider : Optional[Literal['fmp']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.

        Returns
        -------
        OBBject
            results : List[HistoricalEmployees]
                Serializable results.
            provider : Optional[Literal['fmp']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            error : Optional[Error]
                Caught exceptions.
            chart : Optional[Chart]
                Chart object.

        HistoricalEmployees
        -------------------
        symbol : Optional[str]
            Symbol to get data for.
        cik : Optional[int]
            CIK of the company to retrieve the historical employees of.
        acceptance_time : Optional[datetime]
            Time of acceptance of the company employee.
        period_of_report : Optional[date]
            Date of reporting of the company employee.
        company_name : Optional[str]
            Registered name of the company to retrieve the historical employees of.
        form_type : Optional[str]
            Form type of the company employee.
        filing_date : Optional[date]
            Filing date of the company employee
        employee_count : Optional[int]
            Count of employees of the company.
        source : Optional[str]
            Source URL which retrieves this data for the company."""

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
            "/stocks/fa/emp",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def enterprise(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Enterprise value."""

        inputs = filter_inputs(
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/enterprise",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def epsfc(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Earnings Estimate by Analysts - EPS."""

        inputs = filter_inputs(
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/epsfc",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def est(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for."),
        ],
        period: Annotated[
            Literal["annually", "quarterly"],
            OpenBBCustomParameter(description="Period of the data to return."),
        ] = "annually",
        limit: Annotated[
            int,
            OpenBBCustomParameter(description="The number of data entries to return."),
        ] = 30,
        chart: bool = False,
        provider: Optional[Literal["fmp"]] = None,
        **kwargs
    ) -> OBBject[List]:
        """Analyst Estimates.

        Parameters
        ----------
        symbol : Union[str, List[str]]
            Symbol to get data for.
        period : Literal['annually', 'quarterly']
            Period of the data to return.
        limit : int
            The number of data entries to return.
        chart : bool
            Whether to create a chart or not, by default False.
        provider : Optional[Literal['fmp']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.

        Returns
        -------
        OBBject
            results : List[AnalystEstimates]
                Serializable results.
            provider : Optional[Literal['fmp']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            error : Optional[Error]
                Caught exceptions.
            chart : Optional[Chart]
                Chart object.

        AnalystEstimates
        ----------------
        symbol : Optional[str]
            Symbol to get data for.
        date : Optional[date]
            A specific date to get data for.
        estimated_revenue_low : Optional[int]
            Estimated revenue low.
        estimated_revenue_high : Optional[int]
            Estimated revenue high.
        estimated_revenue_avg : Optional[int]
            Estimated revenue average.
        estimated_ebitda_low : Optional[int]
            Estimated EBITDA low.
        estimated_ebitda_high : Optional[int]
            Estimated EBITDA high.
        estimated_ebitda_avg : Optional[int]
            Estimated EBITDA average.
        estimated_ebit_low : Optional[int]
            Estimated EBIT low.
        estimated_ebit_high : Optional[int]
            Estimated EBIT high.
        estimated_ebit_avg : Optional[int]
            Estimated EBIT average.
        estimated_net_income_low : Optional[int]
            Estimated net income low.
        estimated_net_income_high : Optional[int]
            Estimated net income high.
        estimated_net_income_avg : Optional[int]
            Estimated net income average.
        estimated_sga_expense_low : Optional[int]
            Estimated SGA expense low.
        estimated_sga_expense_high : Optional[int]
            Estimated SGA expense high.
        estimated_sga_expense_avg : Optional[int]
            Estimated SGA expense average.
        estimated_eps_avg : Optional[float]
            Estimated EPS average.
        estimated_eps_high : Optional[float]
            Estimated EPS high.
        estimated_eps_low : Optional[float]
            Estimated EPS low.
        number_analyst_estimated_revenue : Optional[int]
            Number of analysts who estimated revenue.
        number_analysts_estimated_eps : Optional[int]
            Number of analysts who estimated EPS."""

        inputs = filter_inputs(
            provider_choices={
                "provider": provider,
            },
            standard_params={
                "symbol": ",".join(symbol) if isinstance(symbol, list) else symbol,
                "period": period,
                "limit": limit,
            },
            extra_params=kwargs,
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/est",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def fama_coe(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Fama French 3 Factor Model - Coefficient of Earnings."""

        inputs = filter_inputs(
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/fama_coe",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def fama_raw(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Fama French 3 Factor Model - Raw Data."""

        inputs = filter_inputs(
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/fama_raw",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def fraud(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Key fraud ratios including M-score, Z-score and McKee."""

        inputs = filter_inputs(
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/fraud",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def growth(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Growth of financial statement items and ratios."""

        inputs = filter_inputs(
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/growth",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def historical_5(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        inputs = filter_inputs(
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/historical_5",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def income(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for."),
        ],
        period: Annotated[
            Literal["annually", "quarterly"],
            OpenBBCustomParameter(description="Period of the data to return."),
        ] = "annually",
        limit: Annotated[
            Optional[pydantic.types.NonNegativeInt],
            OpenBBCustomParameter(description="The number of data entries to return."),
        ] = 12,
        chart: bool = False,
        provider: Optional[Literal["fmp", "polygon"]] = None,
        **kwargs
    ) -> OBBject[List]:
        """Income Statement.

        Parameters
        ----------
        symbol : Union[str, List[str]]
            Symbol to get data for.
        period : Literal['annually', 'quarterly']
            Period of the data to return.
        limit : Optional[pydantic.types.NonNegativeInt]
            The number of data entries to return.
        chart : bool
            Whether to create a chart or not, by default False.
        provider : Optional[Literal['fmp', 'polygon']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.
        cik : Optional[str]
            The CIK of the company if no symbol is provided. (provider: fmp)
        company_name : Optional[str]
            Name of the company. (provider: polygon)
        company_name_search : Optional[str]
            Name of the company to search. (provider: polygon)
        sic : Optional[str]
            The Standard Industrial Classification (SIC) of the company. (provider: polygon)
        filing_date : Optional[datetime.date]
            Filing date of the financial statement. (provider: polygon)
        filing_date_lt : Optional[datetime.date]
            Filing date less than the given date. (provider: polygon)
        filing_date_lte : Optional[datetime.date]
            Filing date less than or equal to the given date. (provider: polygon)
        filing_date_gt : Optional[datetime.date]
            Filing date greater than the given date. (provider: polygon)
        filing_date_gte : Optional[datetime.date]
            Filing date greater than or equal to the given date. (provider: polygon)
        period_of_report_date : Optional[datetime.date]
            Period of report date of the financial statement. (provider: polygon)
        period_of_report_date_lt : Optional[datetime.date]
            Period of report date less than the given date. (provider: polygon)
        period_of_report_date_lte : Optional[datetime.date]
            Period of report date less than or equal to the given date. (provider: polygon)
        period_of_report_date_gt : Optional[datetime.date]
            Period of report date greater than the given date. (provider: polygon)
        period_of_report_date_gte : Optional[datetime.date]
            Period of report date greater than or equal to the given date. (provider: polygon)
        include_sources : Optional[bool]
            Whether to include the sources of the financial statement. (provider: polygon)
        order : Optional[Literal['asc', 'desc']]
            Order of the financial statement. (provider: polygon)
        sort : Optional[Literal['filing_date', 'period_of_report_date']]
            Sort of the financial statement. (provider: polygon)

        Returns
        -------
        OBBject
            results : List[IncomeStatement]
                Serializable results.
            provider : Optional[Literal['fmp', 'polygon']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            error : Optional[Error]
                Caught exceptions.
            chart : Optional[Chart]
                Chart object.

        IncomeStatement
        ---------------
        date : Optional[date]
            Date of the income statement.
        symbol : Optional[str]
            Symbol of the company.
        cik : Optional[int]
            Central Index Key.
        currency : Optional[str]
            Reporting currency.
        filing_date : Optional[date]
            Filling date.
        accepted_date : Optional[datetime]
            Accepted date.
        calendar_year : Optional[int]
            Calendar year.
        period : Optional[str]
            Period of the income statement.
        revenue : Optional[int]
            Revenue.
        cost_of_revenue : Optional[int]
            Cost of revenue.
        gross_profit : Optional[int]
            Gross profit.
        cost_and_expenses : Optional[int]
            Cost and expenses.
        gross_profit_ratio : Optional[float]
            Gross profit ratio.
        research_and_development_expenses : Optional[int]
            Research and development expenses.
        general_and_administrative_expenses : Optional[int]
            General and administrative expenses.
        selling_and_marketing_expenses : Optional[float]
            Selling and marketing expenses.
        selling_general_and_administrative_expenses : Optional[int]
            Selling, general and administrative expenses.
        other_expenses : Optional[int]
            Other expenses.
        operating_expenses : Optional[int]
            Operating expenses.
        depreciation_and_amortization : Optional[int]
            Depreciation and amortization.
        ebitda : Optional[int]
            Earnings before interest, taxes, depreciation and amortization.
        ebitda_ratio : Optional[float]
            Earnings before interest, taxes, depreciation and amortization ratio.
        operating_income : Optional[int]
            Operating income.
        operating_income_ratio : Optional[float]
            Operating income ratio.
        interest_income : Optional[int]
            Interest income.
        interest_expense : Optional[int]
            Interest expense.
        total_other_income_expenses_net : Optional[int]
            Total other income expenses net.
        income_before_tax : Optional[int]
            Income before tax.
        income_before_tax_ratio : Optional[float]
            Income before tax ratio.
        income_tax_expense : Optional[int]
            Income tax expense.
        net_income : Optional[int]
            Net income.
        net_income_ratio : Optional[float]
            Net income ratio.
        eps : Optional[float]
            Earnings per share.
        eps_diluted : Optional[float]
            Earnings per share diluted.
        weighted_average_shares_outstanding : Optional[int]
            Weighted average shares outstanding.
        weighted_average_shares_outstanding_dil : Optional[int]
            Weighted average shares outstanding diluted.
        link : Optional[str]
            Link to the income statement.
        final_link : Optional[str]
            Final link to the income statement.
        income_loss_from_continuing_operations_after_tax : Optional[float]
            None
        benefits_costs_expenses : Optional[float]
            None
        net_income_loss_attributable_to_noncontrolling_interest : Optional[int]
            None
        net_income_loss_attributable_to_parent : Optional[float]
            None
        net_income_loss_available_to_common_stockholders_basic : Optional[float]
            None
        participating_securities_distributed_and_undistributed_earnings_loss_basic : Optional[float]
            None
        preferred_stock_dividends_and_other_adjustments : Optional[float]
            None"""

        inputs = filter_inputs(
            provider_choices={
                "provider": provider,
            },
            standard_params={
                "symbol": ",".join(symbol) if isinstance(symbol, list) else symbol,
                "period": period,
                "limit": limit,
            },
            extra_params=kwargs,
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/income",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def income_growth(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for."),
        ],
        limit: Annotated[
            int,
            OpenBBCustomParameter(description="The number of data entries to return."),
        ] = 10,
        period: Annotated[
            Literal["annually", "quarterly"],
            OpenBBCustomParameter(description="Period of the data to return."),
        ] = "annually",
        chart: bool = False,
        provider: Optional[Literal["fmp"]] = None,
        **kwargs
    ) -> OBBject[List]:
        """Income Statement Growth.

        Parameters
        ----------
        symbol : Union[str, List[str]]
            Symbol to get data for.
        limit : int
            The number of data entries to return.
        period : Literal['annually', 'quarterly']
            Period of the data to return.
        chart : bool
            Whether to create a chart or not, by default False.
        provider : Optional[Literal['fmp']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.

        Returns
        -------
        OBBject
            results : List[IncomeStatementGrowth]
                Serializable results.
            provider : Optional[Literal['fmp']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            error : Optional[Error]
                Caught exceptions.
            chart : Optional[Chart]
                Chart object.

        IncomeStatementGrowth
        ---------------------
        symbol : Optional[str]
            Symbol to get data for.
        date : Optional[date]
            The date of the data.
        period : Optional[str]
            Period the statement is returned for.
        growth_revenue : Optional[float]
            Growth rate of total revenue.
        growth_cost_of_revenue : Optional[float]
            Growth rate of cost of goods sold.
        growth_gross_profit : Optional[float]
            Growth rate of gross profit.
        growth_gross_profit_ratio : Optional[float]
            Growth rate of gross profit as a percentage of revenue.
        growth_research_and_development_expenses : Optional[float]
            Growth rate of expenses on research and development.
        growth_general_and_administrative_expenses : Optional[float]
            Growth rate of general and administrative expenses.
        growth_selling_and_marketing_expenses : Optional[float]
            Growth rate of expenses on selling and marketing activities.
        growth_other_expenses : Optional[float]
            Growth rate of other operating expenses.
        growth_operating_expenses : Optional[float]
            Growth rate of total operating expenses.
        growth_cost_and_expenses : Optional[float]
            Growth rate of total costs and expenses.
        growth_interest_expense : Optional[float]
            Growth rate of interest expenses.
        growth_depreciation_and_amortization : Optional[float]
            Growth rate of depreciation and amortization expenses.
        growth_ebitda : Optional[float]
            Growth rate of Earnings Before Interest, Taxes, Depreciation, and Amortization.
        growth_ebitda_ratio : Optional[float]
            Growth rate of EBITDA as a percentage of revenue.
        growth_operating_income : Optional[float]
            Growth rate of operating income.
        growth_operating_income_ratio : Optional[float]
            Growth rate of operating income as a percentage of revenue.
        growth_total_other_income_expenses_net : Optional[float]
            Growth rate of net total other income and expenses.
        growth_income_before_tax : Optional[float]
            Growth rate of income before taxes.
        growth_income_before_tax_ratio : Optional[float]
            Growth rate of income before taxes as a percentage of revenue.
        growth_income_tax_expense : Optional[float]
            Growth rate of income tax expenses.
        growth_net_income : Optional[float]
            Growth rate of net income.
        growth_net_income_ratio : Optional[float]
            Growth rate of net income as a percentage of revenue.
        growth_eps : Optional[float]
            Growth rate of Earnings Per Share (EPS).
        growth_eps_diluted : Optional[float]
            Growth rate of diluted Earnings Per Share (EPS).
        growth_weighted_average_shs_out : Optional[float]
            Growth rate of weighted average shares outstanding.
        growth_weighted_average_shs_out_dil : Optional[float]
            Growth rate of diluted weighted average shares outstanding."""

        inputs = filter_inputs(
            provider_choices={
                "provider": provider,
            },
            standard_params={
                "symbol": ",".join(symbol) if isinstance(symbol, list) else symbol,
                "limit": limit,
                "period": period,
            },
            extra_params=kwargs,
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/income_growth",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def ins(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for."),
        ],
        transactionType: Annotated[
            Optional[
                List[
                    Literal[
                        "A-Award",
                        "C-Conversion",
                        "D-Return",
                        "E-ExpireShort",
                        "F-InKind",
                        "G-Gift",
                        "H-ExpireLong",
                        "I-Discretionary",
                        "J-Other",
                        "L-Small",
                        "M-Exempt",
                        "O-OutOfTheMoney",
                        "P-Purchase",
                        "S-Sale",
                        "U-Tender",
                        "W-Will",
                        "X-InTheMoney",
                        "Z-Trust",
                    ]
                ]
            ],
            OpenBBCustomParameter(description="Type of the transaction."),
        ] = ["P-Purchase"],
        reportingCik: Annotated[
            Optional[int],
            OpenBBCustomParameter(description="CIK of the reporting owner."),
        ] = None,
        companyCik: Annotated[
            Optional[int],
            OpenBBCustomParameter(description="CIK of the company owner."),
        ] = None,
        page: Annotated[
            Optional[int],
            OpenBBCustomParameter(description="Page number of the data to fetch."),
        ] = 0,
        chart: bool = False,
        provider: Optional[Literal["fmp"]] = None,
        **kwargs
    ) -> OBBject[List]:
        """Stock Insider Trading.

        Parameters
        ----------
        symbol : Union[str, List[str]]
            Symbol to get data for.
        transactionType : Optional[List[Literal['A-Award', 'C-Conversion', 'D-Return', 'E-ExpireShort', 'F-InKind', 'G-Gift', 'H-ExpireLong', 'I-Discretionary', 'J-Other', 'L-Small', 'M-Exempt', 'O-OutOfTheMoney', 'P-Purchase', 'S-Sale', 'U-Tender', 'W-Will', 'X-InTheMoney', 'Z-Trust']]]
            Type of the transaction.
        reportingCik : Optional[int]
            CIK of the reporting owner.
        companyCik : Optional[int]
            CIK of the company owner.
        page : Optional[int]
            Page number of the data to fetch.
        chart : bool
            Whether to create a chart or not, by default False.
        provider : Optional[Literal['fmp']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.

        Returns
        -------
        OBBject
            results : List[StockInsiderTrading]
                Serializable results.
            provider : Optional[Literal['fmp']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            error : Optional[Error]
                Caught exceptions.
            chart : Optional[Chart]
                Chart object.

        StockInsiderTrading
        -------------------
        symbol : Optional[str]
            Symbol to get data for.
        filing_date : Optional[datetime]
            Filing date of the stock insider trading.
        transaction_date : Optional[date]
            Transaction date of the stock insider trading.
        reporting_cik : Optional[int]
            Reporting CIK of the stock insider trading.
        transaction_type : Optional[str]
            Transaction type of the stock insider trading.
        securities_owned : Optional[int]
            Securities owned of the stock insider trading.
        company_cik : Optional[int]
            Company CIK of the stock insider trading.
        reporting_name : Optional[str]
            Reporting name of the stock insider trading.
        type_of_owner : Optional[str]
            Type of owner of the stock insider trading.
        acquistion_or_disposition : Optional[str]
            Acquistion or disposition of the stock insider trading.
        form_type : Optional[str]
            Form type of the stock insider trading.
        securities_transacted : Optional[float]
            Securities transacted of the stock insider trading.
        price : Optional[float]
            Price of the stock insider trading.
        security_name : Optional[str]
            Security name of the stock insider trading.
        link : Optional[str]
            Link of the stock insider trading."""

        inputs = filter_inputs(
            provider_choices={
                "provider": provider,
            },
            standard_params={
                "symbol": ",".join(symbol) if isinstance(symbol, list) else symbol,
                "transactionType": transactionType,
                "reportingCik": reportingCik,
                "companyCik": companyCik,
                "page": page,
            },
            extra_params=kwargs,
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/ins",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def ins_own(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for."),
        ],
        include_current_quarter: Annotated[
            bool, OpenBBCustomParameter(description="Include current quarter data.")
        ] = False,
        date: Annotated[
            Optional[datetime.date],
            OpenBBCustomParameter(description="A specific date to get data for."),
        ] = None,
        chart: bool = False,
        provider: Optional[Literal["fmp"]] = None,
        **kwargs
    ) -> OBBject[List]:
        """Institutional Ownership.

        Parameters
        ----------
        symbol : Union[str, List[str]]
            Symbol to get data for.
        include_current_quarter : bool
            Include current quarter data.
        date : Optional[datetime.date]
            A specific date to get data for.
        chart : bool
            Whether to create a chart or not, by default False.
        provider : Optional[Literal['fmp']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.

        Returns
        -------
        OBBject
            results : List[InstitutionalOwnership]
                Serializable results.
            provider : Optional[Literal['fmp']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            error : Optional[Error]
                Caught exceptions.
            chart : Optional[Chart]
                Chart object.

        InstitutionalOwnership
        ----------------------
        symbol : Optional[str]
            Symbol to get data for.
        cik : Optional[str]
            CIK of the company.
        date : Optional[date]
            The date of the data.
        investors_holding : Optional[int]
            Number of investors holding the stock.
        last_investors_holding : Optional[int]
            Number of investors holding the stock in the last quarter.
        investors_holding_change : Optional[int]
            Change in the number of investors holding the stock.
        number_of_13f_shares : Optional[int]
            Number of 13F shares.
        last_number_of_13f_shares : Optional[int]
            Number of 13F shares in the last quarter.
        number_of_13f_shares_change : Optional[int]
            Change in the number of 13F shares.
        total_invested : Optional[float]
            Total amount invested.
        last_total_invested : Optional[float]
            Total amount invested in the last quarter.
        total_invested_change : Optional[float]
            Change in the total amount invested.
        ownership_percent : Optional[float]
            Ownership percent.
        last_ownership_percent : Optional[float]
            Ownership percent in the last quarter.
        ownership_percent_change : Optional[float]
            Change in the ownership percent.
        new_positions : Optional[int]
            Number of new positions.
        last_new_positions : Optional[int]
            Number of new positions in the last quarter.
        new_positions_change : Optional[int]
            Change in the number of new positions.
        increased_positions : Optional[int]
            Number of increased positions.
        last_increased_positions : Optional[int]
            Number of increased positions in the last quarter.
        increased_positions_change : Optional[int]
            Change in the number of increased positions.
        closed_positions : Optional[int]
            Number of closed positions.
        last_closed_positions : Optional[int]
            Number of closed positions in the last quarter.
        closed_positions_change : Optional[int]
            Change in the number of closed positions.
        reduced_positions : Optional[int]
            Number of reduced positions.
        last_reduced_positions : Optional[int]
            Number of reduced positions in the last quarter.
        reduced_positions_change : Optional[int]
            Change in the number of reduced positions.
        total_calls : Optional[int]
            Total number of call options contracts traded for Apple Inc. on the specified date.
        last_total_calls : Optional[int]
            Total number of call options contracts traded for Apple Inc. on the previous reporting date.
        total_calls_change : Optional[int]
            Change in the total number of call options contracts traded between the current and previous reporting dates.
        total_puts : Optional[int]
            Total number of put options contracts traded for Apple Inc. on the specified date.
        last_total_puts : Optional[int]
            Total number of put options contracts traded for Apple Inc. on the previous reporting date.
        total_puts_change : Optional[int]
            Change in the total number of put options contracts traded between the current and previous reporting dates.
        put_call_ratio : Optional[float]
            Put-call ratio, which is the ratio of the total number of put options to call options traded on the specified date.
        last_put_call_ratio : Optional[float]
            Put-call ratio on the previous reporting date.
        put_call_ratio_change : Optional[float]
            Change in the put-call ratio between the current and previous reporting dates.
        """

        inputs = filter_inputs(
            provider_choices={
                "provider": provider,
            },
            standard_params={
                "symbol": ",".join(symbol) if isinstance(symbol, list) else symbol,
                "include_current_quarter": include_current_quarter,
                "date": date,
            },
            extra_params=kwargs,
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/ins_own",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def key(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        inputs = filter_inputs(
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/key",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def metrics(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for."),
        ],
        period: Annotated[
            Literal["annually", "quarterly"],
            OpenBBCustomParameter(description="Period of the data to return."),
        ] = "annually",
        limit: Annotated[
            Optional[int],
            OpenBBCustomParameter(description="The number of data entries to return."),
        ] = 100,
        chart: bool = False,
        provider: Optional[Literal["fmp"]] = None,
        **kwargs
    ) -> OBBject[List]:
        """Key Metrics.

        Parameters
        ----------
        symbol : Union[str, List[str]]
            Symbol to get data for.
        period : Literal['annually', 'quarterly']
            Period of the data to return.
        limit : Optional[int]
            The number of data entries to return.
        chart : bool
            Whether to create a chart or not, by default False.
        provider : Optional[Literal['fmp']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.

        Returns
        -------
        OBBject
            results : List[KeyMetrics]
                Serializable results.
            provider : Optional[Literal['fmp']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            error : Optional[Error]
                Caught exceptions.
            chart : Optional[Chart]
                Chart object.

        KeyMetrics
        ----------
        symbol : Optional[str]
            Symbol to get data for.
        date : Optional[date]
            The date of the data.
        period : Optional[str]
            Period of the data.
        revenue_per_share : Optional[float]
            Revenue per share
        net_income_per_share : Optional[float]
            Net income per share
        operating_cash_flow_per_share : Optional[float]
            Operating cash flow per share
        free_cash_flow_per_share : Optional[float]
            Free cash flow per share
        cash_per_share : Optional[float]
            Cash per share
        book_value_per_share : Optional[float]
            Book value per share
        tangible_book_value_per_share : Optional[float]
            Tangible book value per share
        shareholders_equity_per_share : Optional[float]
            Shareholders equity per share
        interest_debt_per_share : Optional[float]
            Interest debt per share
        market_cap : Optional[float]
            Market capitalization
        enterprise_value : Optional[float]
            Enterprise value
        pe_ratio : Optional[float]
            Price-to-earnings ratio (P/E ratio)
        price_to_sales_ratio : Optional[float]
            Price-to-sales ratio
        pocf_ratio : Optional[float]
            Price-to-operating cash flow ratio
        pfcf_ratio : Optional[float]
            Price-to-free cash flow ratio
        pb_ratio : Optional[float]
            Price-to-book ratio
        ptb_ratio : Optional[float]
            Price-to-tangible book ratio
        ev_to_sales : Optional[float]
            Enterprise value-to-sales ratio
        enterprise_value_over_ebitda : Optional[float]
            Enterprise value-to-EBITDA ratio
        ev_to_operating_cash_flow : Optional[float]
            Enterprise value-to-operating cash flow ratio
        ev_to_free_cash_flow : Optional[float]
            Enterprise value-to-free cash flow ratio
        earnings_yield : Optional[float]
            Earnings yield
        free_cash_flow_yield : Optional[float]
            Free cash flow yield
        debt_to_equity : Optional[float]
            Debt-to-equity ratio
        debt_to_assets : Optional[float]
            Debt-to-assets ratio
        net_debt_to_ebitda : Optional[float]
            Net debt-to-EBITDA ratio
        current_ratio : Optional[float]
            Current ratio
        interest_coverage : Optional[float]
            Interest coverage
        income_quality : Optional[float]
            Income quality
        dividend_yield : Optional[float]
            Dividend yield
        payout_ratio : Optional[float]
            Payout ratio
        sales_general_and_administrative_to_revenue : Optional[float]
            Sales general and administrative expenses-to-revenue ratio
        research_and_development_to_revenue : Optional[float]
            Research and development expenses-to-revenue ratio
        intangibles_to_total_assets : Optional[float]
            Intangibles-to-total assets ratio
        capex_to_operating_cash_flow : Optional[float]
            Capital expenditures-to-operating cash flow ratio
        capex_to_revenue : Optional[float]
            Capital expenditures-to-revenue ratio
        capex_to_depreciation : Optional[float]
            Capital expenditures-to-depreciation ratio
        stock_based_compensation_to_revenue : Optional[float]
            Stock-based compensation-to-revenue ratio
        graham_number : Optional[float]
            Graham number
        roic : Optional[float]
            Return on invested capital
        return_on_tangible_assets : Optional[float]
            Return on tangible assets
        graham_net_net : Optional[float]
            Graham net-net working capital
        working_capital : Optional[float]
            Working capital
        tangible_asset_value : Optional[float]
            Tangible asset value
        net_current_asset_value : Optional[float]
            Net current asset value
        invested_capital : Optional[float]
            Invested capital
        average_receivables : Optional[float]
            Average receivables
        average_payables : Optional[float]
            Average payables
        average_inventory : Optional[float]
            Average inventory
        days_sales_outstanding : Optional[float]
            Days sales outstanding
        days_payables_outstanding : Optional[float]
            Days payables outstanding
        days_of_inventory_on_hand : Optional[float]
            Days of inventory on hand
        receivables_turnover : Optional[float]
            Receivables turnover
        payables_turnover : Optional[float]
            Payables turnover
        inventory_turnover : Optional[float]
            Inventory turnover
        roe : Optional[float]
            Return on equity
        capex_per_share : Optional[float]
            Capital expenditures per share"""

        inputs = filter_inputs(
            provider_choices={
                "provider": provider,
            },
            standard_params={
                "symbol": ",".join(symbol) if isinstance(symbol, list) else symbol,
                "period": period,
                "limit": limit,
            },
            extra_params=kwargs,
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/metrics",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def mgmt(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for."),
        ],
        chart: bool = False,
        provider: Optional[Literal["fmp"]] = None,
        **kwargs
    ) -> OBBject[List]:
        """Key Executives.

        Parameters
        ----------
        symbol : Union[str, List[str]]
            Symbol to get data for.
        chart : bool
            Whether to create a chart or not, by default False.
        provider : Optional[Literal['fmp']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.

        Returns
        -------
        OBBject
            results : List[KeyExecutives]
                Serializable results.
            provider : Optional[Literal['fmp']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            error : Optional[Error]
                Caught exceptions.
            chart : Optional[Chart]
                Chart object.

        KeyExecutives
        -------------
        title : Optional[str]
            Designation of the key executive.
        name : Optional[str]
            Name of the key executive.
        pay : Optional[int]
            Pay of the key executive.
        currency_pay : Optional[str]
            Currency of the pay.
        gender : Optional[str]
            Gender of the key executive.
        year_born : Optional[str]
            Birth year of the key executive.
        title_since : Optional[int]
            Date the tile was held since."""

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
            "/stocks/fa/mgmt",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def mktcap(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Obtain the market capitalization or enterprise value."""

        inputs = filter_inputs(
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/mktcap",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def news(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        inputs = filter_inputs(
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/news",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def overview(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for."),
        ],
        chart: bool = False,
        provider: Optional[Literal["fmp"]] = None,
        **kwargs
    ) -> OBBject[BaseModel]:
        """Company Overview.

        Parameters
        ----------
        symbol : Union[str, List[str]]
            Symbol to get data for.
        chart : bool
            Whether to create a chart or not, by default False.
        provider : Optional[Literal['fmp']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.

        Returns
        -------
        OBBject
            results : List[CompanyOverview]
                Serializable results.
            provider : Optional[Literal['fmp']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            error : Optional[Error]
                Caught exceptions.
            chart : Optional[Chart]
                Chart object.

        CompanyOverview
        ---------------
        symbol : Optional[str]
            Symbol to get data for.
        price : Optional[float]
            Price of the company.
        beta : Optional[float]
            Beta of the company.
        vol_avg : Optional[int]
            Volume average of the company.
        mkt_cap : Optional[int]
            Market capitalization of the company.
        last_div : Optional[float]
            Last dividend of the company.
        range : Optional[str]
            Range of the company.
        changes : Optional[float]
            Changes of the company.
        company_name : Optional[str]
            Company name of the company.
        currency : Optional[str]
            Currency of the company.
        cik : Optional[str]
            CIK of the company.
        isin : Optional[str]
            ISIN of the company.
        cusip : Optional[str]
            CUSIP of the company.
        exchange : Optional[str]
            Exchange of the company.
        exchange_short_name : Optional[str]
            Exchange short name of the company.
        industry : Optional[str]
            Industry of the company.
        website : Optional[str]
            Website of the company.
        description : Optional[str]
            Description of the company.
        ceo : Optional[str]
            CEO of the company.
        sector : Optional[str]
            Sector of the company.
        country : Optional[str]
            Country of the company.
        full_time_employees : Optional[str]
            Full time employees of the company.
        phone : Optional[str]
            Phone of the company.
        address : Optional[str]
            Address of the company.
        city : Optional[str]
            City of the company.
        state : Optional[str]
            State of the company.
        zip : Optional[str]
            Zip of the company.
        dcf_diff : Optional[float]
            Discounted cash flow difference of the company.
        dcf : Optional[float]
            Discounted cash flow of the company.
        image : Optional[str]
            Image of the company.
        ipo_date : Optional[date]
            IPO date of the company.
        default_image : Optional[bool]
            If the image is the default image.
        is_etf : Optional[bool]
            If the company is an ETF.
        is_actively_trading : Optional[bool]
            If the company is actively trading.
        is_adr : Optional[bool]
            If the company is an ADR.
        is_fund : Optional[bool]
            If the company is a fund."""

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
            "/stocks/fa/overview",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def own(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for."),
        ],
        date: Annotated[
            Optional[datetime.date],
            OpenBBCustomParameter(description="A specific date to get data for."),
        ] = None,
        page: Annotated[
            Optional[int],
            OpenBBCustomParameter(description="Page number of the data to fetch."),
        ] = 0,
        chart: bool = False,
        provider: Optional[Literal["fmp"]] = None,
        **kwargs
    ) -> OBBject[List]:
        """Stock Ownership.

        Parameters
        ----------
        symbol : Union[str, List[str]]
            Symbol to get data for.
        date : Optional[datetime.date]
            A specific date to get data for.
        page : Optional[int]
            Page number of the data to fetch.
        chart : bool
            Whether to create a chart or not, by default False.
        provider : Optional[Literal['fmp']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.

        Returns
        -------
        OBBject
            results : List[StockOwnership]
                Serializable results.
            provider : Optional[Literal['fmp']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            error : Optional[Error]
                Caught exceptions.
            chart : Optional[Chart]
                Chart object.

        StockOwnership
        --------------
        date : Optional[date]
            The date of the data.
        cik : Optional[int]
            Cik of the stock ownership.
        filing_date : Optional[date]
            Filing date of the stock ownership.
        investor_name : Optional[str]
            Investor name of the stock ownership.
        symbol : Optional[str]
            Symbol of the stock ownership.
        security_name : Optional[str]
            Security name of the stock ownership.
        type_of_security : Optional[str]
            Type of security of the stock ownership.
        security_cusip : Optional[str]
            Security cusip of the stock ownership.
        shares_type : Optional[str]
            Shares type of the stock ownership.
        put_call_share : Optional[str]
            Put call share of the stock ownership.
        investment_discretion : Optional[str]
            Investment discretion of the stock ownership.
        industry_title : Optional[str]
            Industry title of the stock ownership.
        weight : Optional[float]
            Weight of the stock ownership.
        last_weight : Optional[float]
            Last weight of the stock ownership.
        change_in_weight : Optional[float]
            Change in weight of the stock ownership.
        change_in_weight_percentage : Optional[float]
            Change in weight percentage of the stock ownership.
        market_value : Optional[int]
            Market value of the stock ownership.
        last_market_value : Optional[int]
            Last market value of the stock ownership.
        change_in_market_value : Optional[int]
            Change in market value of the stock ownership.
        change_in_market_value_percentage : Optional[float]
            Change in market value percentage of the stock ownership.
        shares_number : Optional[int]
            Shares number of the stock ownership.
        last_shares_number : Optional[int]
            Last shares number of the stock ownership.
        change_in_shares_number : Optional[float]
            Change in shares number of the stock ownership.
        change_in_shares_number_percentage : Optional[float]
            Change in shares number percentage of the stock ownership.
        quarter_end_price : Optional[float]
            Quarter end price of the stock ownership.
        avg_price_paid : Optional[float]
            Average price paid of the stock ownership.
        is_new : Optional[bool]
            Is the stock ownership new.
        is_sold_out : Optional[bool]
            Is the stock ownership sold out.
        ownership : Optional[float]
            How much is the ownership.
        last_ownership : Optional[float]
            Last ownership amount.
        change_in_ownership : Optional[float]
            Change in ownership amount.
        change_in_ownership_percentage : Optional[float]
            Change in ownership percentage.
        holding_period : Optional[int]
            Holding period of the stock ownership.
        first_added : Optional[date]
            First added date of the stock ownership.
        performance : Optional[float]
            Performance of the stock ownership.
        performance_percentage : Optional[float]
            Performance percentage of the stock ownership.
        last_performance : Optional[float]
            Last performance of the stock ownership.
        change_in_performance : Optional[float]
            Change in performance of the stock ownership.
        is_counted_for_performance : Optional[bool]
            Is the stock ownership counted for performance."""

        inputs = filter_inputs(
            provider_choices={
                "provider": provider,
            },
            standard_params={
                "symbol": ",".join(symbol) if isinstance(symbol, list) else symbol,
                "date": date,
                "page": page,
            },
            extra_params=kwargs,
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/own",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def pt(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for."),
        ],
        chart: bool = False,
        provider: Optional[Literal["fmp"]] = None,
        **kwargs
    ) -> OBBject[BaseModel]:
        """Price Target Consensus.

        Parameters
        ----------
        symbol : Union[str, List[str]]
            Symbol to get data for.
        chart : bool
            Whether to create a chart or not, by default False.
        provider : Optional[Literal['fmp']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.

        Returns
        -------
        OBBject
            results : List[PriceTargetConsensus]
                Serializable results.
            provider : Optional[Literal['fmp']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            error : Optional[Error]
                Caught exceptions.
            chart : Optional[Chart]
                Chart object.

        PriceTargetConsensus
        --------------------
        symbol : Optional[str]
            Symbol to get data for.
        target_high : Optional[float]
            High target of the price target consensus.
        target_low : Optional[float]
            Low target of the price target consensus.
        target_consensus : Optional[float]
            Consensus target of the price target consensus.
        target_median : Optional[float]
            Median target of the price target consensus."""

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
            "/stocks/fa/pt",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def pta(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for."),
        ],
        chart: bool = False,
        provider: Optional[Literal["fmp"]] = None,
        **kwargs
    ) -> OBBject[List]:
        """Price Target.

        Parameters
        ----------
        symbol : Union[str, List[str]]
            Symbol to get data for.
        chart : bool
            Whether to create a chart or not, by default False.
        provider : Optional[Literal['fmp']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.
        with_grade : bool
            Include upgrades and downgrades in the response. (provider: fmp)

        Returns
        -------
        OBBject
            results : List[PriceTarget]
                Serializable results.
            provider : Optional[Literal['fmp']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            error : Optional[Error]
                Caught exceptions.
            chart : Optional[Chart]
                Chart object.

        PriceTarget
        -----------
        symbol : Optional[str]
            Symbol to get data for.
        published_date : Optional[datetime]
            Published date of the price target.
        news_url : Optional[str]
            News URL of the price target.
        news_title : Optional[str]
            News title of the price target.
        analyst_name : Optional[str]
            Analyst name.
        analyst_company : Optional[str]
            Analyst company.
        price_target : Optional[float]
            Price target.
        adj_price_target : Optional[float]
            Adjusted price target.
        price_when_posted : Optional[float]
            Price when posted.
        news_publisher : Optional[str]
            News publisher of the price target.
        news_base_url : Optional[str]
            News base URL of the price target.
        newGrade : Optional[str]
            None
        previousGrade : Optional[str]
            None
        gradingCompany : Optional[str]
            None"""

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
            "/stocks/fa/pta",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def rating(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Analyst prices and ratings over time of the company."""

        inputs = filter_inputs(
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/rating",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def ratios(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for."),
        ],
        period: Annotated[
            Literal["annually", "quarterly"],
            OpenBBCustomParameter(description="Period of the data to return."),
        ] = "annually",
        limit: Annotated[
            Optional[pydantic.types.NonNegativeInt],
            OpenBBCustomParameter(description="The number of data entries to return."),
        ] = 12,
        chart: bool = False,
        provider: Optional[Literal["fmp"]] = None,
        **kwargs
    ) -> OBBject[List]:
        """Extensive set of ratios over time.

        Parameters
        ----------
        symbol : Union[str, List[str]]
            Symbol to get data for.
        period : Literal['annually', 'quarterly']
            Period of the data to return.
        limit : Optional[pydantic.types.NonNegativeInt]
            The number of data entries to return.
        chart : bool
            Whether to create a chart or not, by default False.
        provider : Optional[Literal['fmp']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.

        Returns
        -------
        OBBject
            results : List[FinancialRatios]
                Serializable results.
            provider : Optional[Literal['fmp']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            error : Optional[Error]
                Caught exceptions.
            chart : Optional[Chart]
                Chart object.

        FinancialRatios
        ---------------
        symbol : Optional[str]
            Symbol of the company.
        date : Optional[str]
            Date of the financial ratios.
        period : Optional[str]
            Period of the financial ratios.
        current_ratio : Optional[float]
            Current ratio.
        quick_ratio : Optional[float]
            Quick ratio.
        cash_ratio : Optional[float]
            Cash ratio.
        days_of_sales_outstanding : Optional[float]
            Days of sales outstanding.
        days_of_inventory_outstanding : Optional[float]
            Days of inventory outstanding.
        operating_cycle : Optional[float]
            Operating cycle.
        days_of_payables_outstanding : Optional[float]
            Days of payables outstanding.
        cash_conversion_cycle : Optional[float]
            Cash conversion cycle.
        gross_profit_margin : Optional[float]
            Gross profit margin.
        operating_profit_margin : Optional[float]
            Operating profit margin.
        pretax_profit_margin : Optional[float]
            Pretax profit margin.
        net_profit_margin : Optional[float]
            Net profit margin.
        effective_tax_rate : Optional[float]
            Effective tax rate.
        return_on_assets : Optional[float]
            Return on assets.
        return_on_equity : Optional[float]
            Return on equity.
        return_on_capital_employed : Optional[float]
            Return on capital employed.
        net_income_per_ebt : Optional[float]
            Net income per EBT.
        ebt_per_ebit : Optional[float]
            EBT per EBIT.
        ebit_per_revenue : Optional[float]
            EBIT per revenue.
        debt_ratio : Optional[float]
            Debt ratio.
        debt_equity_ratio : Optional[float]
            Debt equity ratio.
        long_term_debt_to_capitalization : Optional[float]
            Long term debt to capitalization.
        total_debt_to_capitalization : Optional[float]
            Total debt to capitalization.
        interest_coverage : Optional[float]
            Interest coverage.
        cash_flow_to_debt_ratio : Optional[float]
            Cash flow to debt ratio.
        company_equity_multiplier : Optional[float]
            Company equity multiplier.
        receivables_turnover : Optional[float]
            Receivables turnover.
        payables_turnover : Optional[float]
            Payables turnover.
        inventory_turnover : Optional[float]
            Inventory turnover.
        fixed_asset_turnover : Optional[float]
            Fixed asset turnover.
        asset_turnover : Optional[float]
            Asset turnover.
        operating_cash_flow_per_share : Optional[float]
            Operating cash flow per share.
        free_cash_flow_per_share : Optional[float]
            Free cash flow per share.
        cash_per_share : Optional[float]
            Cash per share.
        payout_ratio : Optional[float]
            Payout ratio.
        operating_cash_flow_sales_ratio : Optional[float]
            Operating cash flow sales ratio.
        free_cash_flow_operating_cash_flow_ratio : Optional[float]
            Free cash flow operating cash flow ratio.
        cash_flow_coverage_ratios : Optional[float]
            Cash flow coverage ratios.
        short_term_coverage_ratios : Optional[float]
            Short term coverage ratios.
        capital_expenditure_coverage_ratio : Optional[float]
            Capital expenditure coverage ratio.
        dividend_paid_and_capex_coverage_ratio : Optional[float]
            Dividend paid and capex coverage ratio.
        dividend_payout_ratio : Optional[float]
            Dividend payout ratio.
        price_book_value_ratio : Optional[float]
            Price book value ratio.
        price_to_book_ratio : Optional[float]
            Price to book ratio.
        price_to_sales_ratio : Optional[float]
            Price to sales ratio.
        price_earnings_ratio : Optional[float]
            Price earnings ratio.
        price_to_free_cash_flows_ratio : Optional[float]
            Price to free cash flows ratio.
        price_to_operating_cash_flows_ratio : Optional[float]
            Price to operating cash flows ratio.
        price_cash_flow_ratio : Optional[float]
            Price cash flow ratio.
        price_earnings_to_growth_ratio : Optional[float]
            Price earnings to growth ratio.
        price_sales_ratio : Optional[float]
            Price sales ratio.
        dividend_yield : Optional[float]
            Dividend yield.
        enterprise_value_multiple : Optional[float]
            Enterprise value multiple.
        price_fair_value : Optional[float]
            Price fair value."""

        inputs = filter_inputs(
            provider_choices={
                "provider": provider,
            },
            standard_params={
                "symbol": ",".join(symbol) if isinstance(symbol, list) else symbol,
                "period": period,
                "limit": limit,
            },
            extra_params=kwargs,
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/ratios",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def revfc(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Earning Estimate by Analysts - Revenue."""

        inputs = filter_inputs(
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/revfc",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def revgeo(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for."),
        ],
        period: Annotated[
            Literal["annually", "quarterly"],
            OpenBBCustomParameter(description="Period of the data to return."),
        ] = "annually",
        structure: Annotated[
            Literal["hierarchical", "flat"],
            OpenBBCustomParameter(description="Structure of the returned data."),
        ] = "flat",
        chart: bool = False,
        provider: Optional[Literal["fmp"]] = None,
        **kwargs
    ) -> OBBject[List]:
        """Revenue Geographic.

        Parameters
        ----------
        symbol : Union[str, List[str]]
            Symbol to get data for.
        period : Literal['annually', 'quarterly']
            Period of the data to return.
        structure : Literal['hierarchical', 'flat']
            Structure of the returned data.
        chart : bool
            Whether to create a chart or not, by default False.
        provider : Optional[Literal['fmp']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.

        Returns
        -------
        OBBject
            results : List[RevenueGeographic]
                Serializable results.
            provider : Optional[Literal['fmp']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            error : Optional[Error]
                Caught exceptions.
            chart : Optional[Chart]
                Chart object.

        RevenueGeographic
        -----------------
        date : Optional[date]
            The date of the data.
        geographic_segment : Optional[Mapping[str, int]]
            Day level data containing the revenue of the geographic segment.
        americas : Optional[int]
            Revenue from the the American segment.
        europe : Optional[int]
            Revenue from the the European segment.
        greater_china : Optional[int]
            Revenue from the the Greater China segment.
        japan : Optional[int]
            Revenue from the the Japan segment.
        rest_of_asia_pacific : Optional[int]
            Revenue from the the Rest of Asia Pacific segment."""

        inputs = filter_inputs(
            provider_choices={
                "provider": provider,
            },
            standard_params={
                "symbol": ",".join(symbol) if isinstance(symbol, list) else symbol,
                "period": period,
                "structure": structure,
            },
            extra_params=kwargs,
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/revgeo",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def revseg(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for."),
        ],
        period: Annotated[
            Literal["annually", "quarterly"],
            OpenBBCustomParameter(description="Period of the data to return."),
        ] = "annually",
        structure: Annotated[
            Literal["hierarchical", "flat"],
            OpenBBCustomParameter(description="Structure of the returned data."),
        ] = "flat",
        chart: bool = False,
        provider: Optional[Literal["fmp"]] = None,
        **kwargs
    ) -> OBBject[List]:
        """Revenue Business Line.

        Parameters
        ----------
        symbol : Union[str, List[str]]
            Symbol to get data for.
        period : Literal['annually', 'quarterly']
            Period of the data to return.
        structure : Literal['hierarchical', 'flat']
            Structure of the returned data.
        chart : bool
            Whether to create a chart or not, by default False.
        provider : Optional[Literal['fmp']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.

        Returns
        -------
        OBBject
            results : List[RevenueBusinessLine]
                Serializable results.
            provider : Optional[Literal['fmp']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            error : Optional[Error]
                Caught exceptions.
            chart : Optional[Chart]
                Chart object.

        RevenueBusinessLine
        -------------------
        date : Optional[date]
            The date of the data.
        business_line : Optional[Mapping[str, int]]
            Day level data containing the revenue of the business line."""

        inputs = filter_inputs(
            provider_choices={
                "provider": provider,
            },
            standard_params={
                "symbol": ",".join(symbol) if isinstance(symbol, list) else symbol,
                "period": period,
                "structure": structure,
            },
            extra_params=kwargs,
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/revseg",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def rot(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Number of analyst ratings over time on a monthly basis."""

        inputs = filter_inputs(
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/rot",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def score(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Value investing scores for any time period."""

        inputs = filter_inputs(
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/score",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def sec(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        inputs = filter_inputs(
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/sec",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def shares(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        inputs = filter_inputs(
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/shares",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def shrs(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for."),
        ],
        chart: bool = False,
        provider: Optional[Literal["fmp"]] = None,
        **kwargs
    ) -> OBBject[List]:
        """Share Statistics.

        Parameters
        ----------
        symbol : Union[str, List[str]]
            Symbol to get data for.
        chart : bool
            Whether to create a chart or not, by default False.
        provider : Optional[Literal['fmp']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.

        Returns
        -------
        OBBject
            results : List[ShareStatistics]
                Serializable results.
            provider : Optional[Literal['fmp']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            error : Optional[Error]
                Caught exceptions.
            chart : Optional[Chart]
                Chart object.

        ShareStatistics
        ---------------
        symbol : Optional[str]
            Symbol to get data for.
        date : Optional[date]
            A specific date to get data for.
        free_float : Optional[float]
            Percentage of unrestricted shares of a publicly-traded company.
        float_shares : Optional[float]
            Number of shares available for trading by the general public.
        outstanding_shares : Optional[float]
            Total number of shares of a publicly-traded company.
        source : Optional[str]
            Source of the received data."""

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
            "/stocks/fa/shrs",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def split(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for."),
        ],
        chart: bool = False,
        provider: Optional[Literal["fmp"]] = None,
        **kwargs
    ) -> OBBject[List]:
        """Historical Stock Splits.

        Parameters
        ----------
        symbol : Union[str, List[str]]
            Symbol to get data for.
        chart : bool
            Whether to create a chart or not, by default False.
        provider : Optional[Literal['fmp']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.

        Returns
        -------
        OBBject
            results : List[HistoricalStockSplits]
                Serializable results.
            provider : Optional[Literal['fmp']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            error : Optional[Error]
                Caught exceptions.
            chart : Optional[Chart]
                Chart object.

        HistoricalStockSplits
        ---------------------
        date : Optional[date]
            The date of the data.
        label : Optional[str]
            Label of the historical stock splits.
        numerator : Optional[float]
            Numerator of the historical stock splits.
        denominator : Optional[float]
            Denominator of the historical stock splits."""

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
            "/stocks/fa/split",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def supplier(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """List of suppliers of the company."""

        inputs = filter_inputs(
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/supplier",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def transcript(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for."),
        ],
        year: Annotated[
            int,
            OpenBBCustomParameter(description="Year of the earnings call transcript."),
        ],
        quarter: Annotated[
            Literal[1, 2, 3, 4],
            OpenBBCustomParameter(
                description="Quarter of the earnings call transcript."
            ),
        ] = 1,
        chart: bool = False,
        provider: Optional[Literal["fmp"]] = None,
        **kwargs
    ) -> OBBject[List]:
        """Earnings Call Transcript.

        Parameters
        ----------
        symbol : Union[str, List[str]]
            Symbol to get data for.
        year : int
            Year of the earnings call transcript.
        quarter : Literal[1, 2, 3, 4]
            Quarter of the earnings call transcript.
        chart : bool
            Whether to create a chart or not, by default False.
        provider : Optional[Literal['fmp']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.

        Returns
        -------
        OBBject
            results : List[EarningsCallTranscript]
                Serializable results.
            provider : Optional[Literal['fmp']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            error : Optional[Error]
                Caught exceptions.
            chart : Optional[Chart]
                Chart object.

        EarningsCallTranscript
        ----------------------
        symbol : Optional[str]
            Symbol to get data for.
        quarter : Optional[int]
            Quarter of the earnings call transcript.
        year : Optional[int]
            Year of the earnings call transcript.
        date : Optional[datetime]
            The date of the data.
        content : Optional[str]
            Content of the earnings call transcript."""

        inputs = filter_inputs(
            provider_choices={
                "provider": provider,
            },
            standard_params={
                "symbol": ",".join(symbol) if isinstance(symbol, list) else symbol,
                "year": year,
                "quarter": quarter,
            },
            extra_params=kwargs,
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/fa/transcript",
            **inputs,
        ).output

        return filter_output(o)