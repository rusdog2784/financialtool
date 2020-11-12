"""
File containing the Ratio class.

Author:         Scott Russell
Date Created:   11/12/2020
"""
import math


class Ratio(object):
    """
    Class containing a series of functions meant to calculate popular financial
    ratios for a given stock ticker.
    """
    def __init__(self, stock_info: dict) -> None:
        """
        Initializer.

        Args: 
            stock_info (dict): Ticker.info object (from python package, yfinance).
        """
        self.stock_info = stock_info

    def get_inventory_turnover(self) -> float:
        """
        Calculates the inventory turnover value (annual) for a stock. Inventory
        turnover if the ratio showing how many times a company's inventory is
        sold and replaced over a period of time. It is calculated by taking the
        cost of revenue, or sales, for a period of time (last 4 quarters) and
        dividing it by the average inventory, which is the sum of inventory at
        the beginning plus the inventory at the end divided by 2. A higher ratio
        implies either strong sales and/or large discounts, whereas a low ratio
        implies weak sales and excess inventory. Typically, the higher the
        ratio, the better.

        Returns: 
            float: Calculated inventory turnover.
        """
        return 0.0

    def get_working_capital_turnover(self) -> float:
        """
        Calculates the working capital turnover value (annual) for a stock.
        Working capital turnover is used to analyze the relationship between the
        money that funds operations and the sales generated from these
        operations. It is calculated by taking the total revenue over a period
        of time (last 4 quarters) and dividing it by the average working
        capital, which is the difference between the total current assets at the
        beginning minus the total current liabilities at the beginning plus
        total current assets at the end minus total current liabilities at end
        all divided by 2. A higher ratio shows that management is being very
        efficient in using a company's short-term assets and liabilities for
        supporting sales. A lower ratio shows that a business is investing in
        too many accounts receivable and inventory assets to support its sales.
        Typically, the higher the ratio, the better.

        Returns: 
            float: Calculated working capital turnover.
        """
        return 0.0

    def get_current_ratio(self) -> float:
        """
        Calculates the current ratio value (most recent quarter) for a stock.
        The current ratio is a liquidity ratio that measures a company's ability
        to pay short-term and long-term obligations. It is calculated by taking
        the total current assets and dividing by the total current liabilities.
        The higher the ratio, the more capable a company is of paying its
        obligations. A ratio under 1 indicates that a company's liabilities are
        greater than its assets and suggests that the company in question would
        be unable to pay off its obligations. Typically, the higher the ratio,
        the better, and a ratio of 2:1 is really good.

        Returns: 
            float: Calculated current ratio.
        """
        return 0.0

    def get_quick_ratio(self) -> float:
        """
        Calculates the quick ratio value (most recent quarter) for a stock. The
        quick ratio is a measure of a company's ability to meet its short-term
        obligations with its most liquid assets. It is calculated by taking the
        total current assets, subtracting inventory, then dividing by the total
        current liabilities. The higher the quick ratio, the better the
        company's liquidity position. A ratio of less than 1 is bad.

        Returns: 
            float: Calculated quick ratio.
        """
        return 0.0

    def get_debt_ratio(self) -> float:
        """
        Calculates the debt ratio value (most recent quarter) for a stock. The
        debt ratio measures the extent of a company's or consumer's leverage,
        which is another word for debt. It is calculated by taking the total
        debt and dividing it by the total assets. The higher this ratio, the
        more leveraged, or the more debt, the company is/has, implying greater
        financial risk. In this case, the lower the ratio, the better. 

        Returns: 
            float: Calculated debt ratio.
        """
        return 0.0

    def get_financial_leverage_ratio(self) -> float:
        """
        Calculates the financial leverage ratio value (most recent quarter) for
        a stock. The financial leverage ratio looks at how much capital comes in
        the form of debt (loans), OR it helps to assess the ability of a company
        to meet financial obligations. It is calculated by taking the total debt
        and dividing by the total equity. A ratio greater than 2.0 indicates a
        risky scenario for the investor, however this threshold can vary based
        on industry. In this case, the lower the ratio, the better.

        Returns: 
            float: Calculated financial leverage ratio.
        """
        return 0.0

    def get_net_profit_margin(self) -> float:
        """
        Calculates the net profit margin value (annual) for a stock. Net profit
        margin is a ratio of net profits to revenues for a company or business
        segment. It is calculated by taking the net income and dividing by total
        revenue. The higher the ratio, the better, however, a low profit margin
        doesn't necessarily equate to low profits.

        Returns: 
            float: Calculated net profit margin as a percentage.
        """
        return 0.0

    def get_return_on_equity(self) -> float:
        """
        Calculates the return on equity value (annual) for a stock. The return
        on equity ratio measures a corporation's profitability by revealing how
        much profit a company generates with the monty shareholders have
        invested. It is calculated by taking the net income and dividing by the
        total equity. This ratio is useful for comparing the profitability of a
        company to that of another firm within the same industry. Typically, the
        higher the ratio, the better.

        Returns: 
            float: Calculated return on equity as a percentage.
        """
        return 0.0

    def get_earnings_per_share_ratio(self) -> float:
        """
        Calculates the earnings per share value (annual) for a stock. The
        earnings per share ratio represents the company's profit allocated to
        each outstanding share of common stock. It is calculated by taking the
        net income and dividing by shares outstanding. Typically, the higher the
        ratio, the better. If the ratio is negative, then the company is losing
        money. Now, if two companies generated the same earnings per share, but
        one did so with less equity (investment) then that company might be
        considered more efficient at using its capital to generate income.

        Returns: 
            float: Calculated earnings per share ratio.
        """
        return 0.0

    def get_price_to_earnings_ratio(self) -> float:
        """
        Calculates the price to earnings value (current) for a stock. The price
        to earnings ratio can be used to value a company who measures its
        current share price relative to its per-share earnings. It is calculated
        by taking the current market price and dividing it by the earnings per
        share ratio value. A high price to earnings ratio suggests that
        investors are expecting higher earnings growth in the near future
        compared to other companies with a lower price to earnings in the same
        industry. A low price to earnings can indicate either that a company may
        be undervalued or that a company is doing exceptionally well relative to
        its past trends. Neither a high nor a low ratio is good or bad. It
        depends on other factors.

        Returns: 
            float: Calculated price to earnings ratio.
        """
        return 0.0
