#!/usr/bin/python
import math

#INVENTORY TURNOVER (annual):
#   high ratio = good
def get_inventory_turnover(cost_of_revenue, inventory):
    #print '\tCost of Revenue: ' + str(cost_of_revenue)
    #print '\tInventory: ' + str(inventory)
    inventory_turnover = -0.0
    if cost_of_revenue[0] != '-' and inventory[0] != '-':
        cogs = 0
        for value in cost_of_revenue:
            cogs += value
        avg_inventory = (float(inventory[0]) + float(inventory[len(inventory) - 1])) / 2.0
        inventory_turnover = cogs / avg_inventory
    else:
        print "\t\tCompany has no revenue or inventory...   "
    return round(inventory_turnover, 4)
#END

#WORKING CAPITAL TURNOVER (annual):
#   high ratio = good
def get_working_capital_turnover(total_revenue, current_assets, current_liabilities):
    #print '\tTotal Revenue: ' + str(total_revenue)
    #print '\tCurrent Assets: ' + str(current_assets)
    #print '\tCurrent Liabilities: ' + str(current_liabilities)
    working_capital_turnover = -0.0
    if total_revenue[0] != '-' and current_assets[0] != '-' and current_liabilities[0] != '-':
        revenue = 0
        for value in total_revenue:
            revenue += value
        avg_working_capital = ((current_assets[0] - current_liabilities[0]) + (current_assets[len(current_liabilities) - 1] - current_liabilities[len(current_liabilities) - 1])) / 2.0
        working_capital_turnover = revenue / avg_working_capital
        #working_capital_turnover = avg_working_capital / revenue
    else:
        print "\t\tCompany has no total revenue, current assets, or current liabilities..."
    return round(working_capital_turnover, 4)
#END

#CURRENT RATIO (most recent quarter):
#   too high = bad
#   2:1 = good
#   ratio < 1 = bad
def get_current_ratio(current_assets, current_liabilities):
    #print '\tCurrent Assets: ' + str(current_assets)
    #print '\tCurrent Liabilities: ' + str(current_liabilities)
    current_ratio = -0.0
    if current_assets[0] != '-' and current_liabilities != '-':
        current_ratio = current_assets[0] / current_liabilities[0]
    else:
        print "\t\tCompany has no current assets or current liabilities..."
    return round(current_ratio, 4)
#END

#QUICK RATIO (most recent quarter):
#   high = good
#   ratio < 1 = bad
def get_quick_ratio(current_assets, inventory, current_liabilities):
    #print '\tCurrent Assets: ' + str(current_assets)
    #print '\tCurrent Liabilities: ' + str(current_liabilities)
    #print '\tInventory: ' + str(inventory)
    quick_ratio = -0.0
    if current_assets[0] != '-' and current_liabilities[0] != '-' and inventory[0] != '-':
        quick_ratio = (current_assets[0] - inventory[0]) / current_liabilities[0]
    else:
        print "\t\tCompany has no current assets, current liabilities, or inventory..."
    return round(quick_ratio, 4)
#END

#DEBT RATIO (most recent quarter):
#   high = bad
#   ratio > .40 = bad
def get_debt_ratio(long_term_debt, short_term_debt, total_assets):
    #print '\tLong Term Debt: ' + str(long_term_debt)
    #print '\tShort Term Debt: ' + str(short_term_debt)
    #print '\tTotal Assets: ' + str(total_assets)
    debt_ratio = -0.0
    if long_term_debt[0] != '-' and short_term_debt[0] != '-' and total_assets[0] != '-':
        debt_ratio = (long_term_debt[0] + short_term_debt[0]) / total_assets[0]
    else:
        print "\t\tCompany has no long term debt, short term debt, or total assets..."
    return round(debt_ratio, 4)
#END

#FINANCIAL LEVERAGE RATIO (most recent quarter):
#   low = good
def get_financial_leverage_ratio(long_term_debt, short_term_debt, total_shareholder_equity):
    #print '\tLong Term Debt: ' + str(long_term_debt)
    #print '\tShort Term Debt: ' + str(short_term_debt)
    #print '\tTotal Stockholder Equity: ' + str(total_shareholder_equity)
    financial_leverage_ratio = -0.0
    if long_term_debt[0] != '-' and short_term_debt[0] != '-' and total_shareholder_equity[0] != '-':
        financial_leverage_ratio = (long_term_debt[0] + short_term_debt[0]) / total_shareholder_equity[0]
    else:
        print "\t\tCompany has no long term debt, short term debt, or total shareholder equity..."
    return round(financial_leverage_ratio, 4)
#END

#NET PROFIT MARGIN (annual):
#   high = good
#   low isn't bad as long as they have lots of revenue
def get_net_profit_margin(net_income, total_revenue):
    #print '\tNet Income: ' + str(net_income)
    #print '\tTotal Revenue: ' + str(total_revenue)
    net_profit_margin = -0.0
    if net_income[0] != '-' and total_revenue[0] != '-':
        income = 0.0
        for value in net_income:
            income += value
        revenue = 0.0
        for value in total_revenue:
            revenue += value
        net_profit_margin = (income / revenue) * 100.0
    else:
        print "\t\tCompany has no net income or total revenue..."
    return round(net_profit_margin, 4)
#END

#RETURN ON EQUITY (annual):
#   high = good
def get_return_on_equity(net_income, total_shareholder_equity):
    #print '\tNet Income: ' + str(net_income)
    #print '\tTotal Stockholder Equity: ' + str(total_shareholder_equity)
    return_on_equity = -0.0
    if net_income[0] != '-' and total_shareholder_equity[0] != '-':
        income = 0.0
        for value in net_income:
            income += value
        return_on_equity = income / total_shareholder_equity[0]
    else:
        print "\t\tCompany has no net income or total shareholder equity..."
    return round(return_on_equity, 4)
#END

#EARNINGS PER SHARE (annual):
#   high = good
#   negative = losing money
def get_earnings_per_share(net_income, shares_outstanding):
    #print '\tNet Income: ' + str(net_income)
    #print '\tShares Outstanding: ' + str(shares_outstanding)
    eps = -0.0
    if net_income[0] != '-' and shares_outstanding != '-':
        income = 0.0
        for value in net_income:
            income += value
        eps = income / shares_outstanding
    else:
        print "\t\tCompany has no net income or shares outstanding..."
    return round(eps, 4)
#END

#PRICE TO EARNINGS RATIO (current):
#   low = good
#   ratio > 0 = good
#   N/A = losses
def get_price_to_earnings_ratio(market_value, eps):
    #print '\tMarket Value: ' + str(market_value)
    #print '\tEPS: ' + str(eps)
    pe_ratio = -0.0
    pe_ratio = market_value / eps
    return round(pe_ratio, 4)
#END






















