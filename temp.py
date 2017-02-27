#!/usr/bin/python

import ratios
import requests, os, re, csv, pandas, selenium
from bs4 import BeautifulSoup
from selenium import webdriver
from yahoo_finance import Share

def getFinancialInfo(ticker):
    #Setting up necessary variables
    financials = {}
    data = {}
    url = 'https://www.google.com/finance?q=JCP&fstype=ii'
    url2 = 'https://www.google.com/finance/url?sa=T&ct=fs_type&cd=bal&url=&ei=JBhXWLHaMNfKUcqalbAM'
    #yahoo = Share(ticker)
    chromedriver = '/Users/Scott/chromedriver'
    os.environ['webdriver.chrome.driver'] = chromedriver
    similar_companies = []
    #End
    
    #Getting market price from Yahoo API
    #data['Market Price'] = float(yahoo.get_price())
    #End

    #Saving data from Income Statement, Cash Flow Statement, and Balance Sheet Statement
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    table = soup.find('table', {'id':'fs-table'})
    for tr in table.find_all('tr'):
        td_title = tr.find('td', {'class':'lft'})
        if td_title != None:
            title = td_title.text.replace('\n', '')
            print "Title: " + title
            values = []
            tds = tr.find_all('td', {'class':'r'})
            if len(tds) > 0:
                for td in tds:
                    if td.get('class') != 'td_genTable' and td.text != '':
                        value = td.text.replace(',', '')
                        value = value.replace('$', '')
                        value = value.replace('(', '-')
                        value = value.replace(')', '')
                        #values.append(float(value))
                        print "\tValue: " + value
        #financials[title] = values
        #print "================================="
    if 'Inventory' not in financials.keys():
        financials['Inventory'] = 0.0
        print "\tCompany has no inventory..."
    #End

    #Getting Shares Outstanding Data and similar companies
    yahoo_url = 'http://finance.yahoo.com/quote/%s/key-statistics?p=%s' % (ticker, ticker)
    driver = webdriver.Chrome(chromedriver)
    driver.get(yahoo_url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find('div', {'class':'Pstart(20px)'})
    if div != None:
        tables = div.find_all('table')
        if len(tables) >= 2:
            table = tables[1]
            tr = table.find_all('tr')[2]
            shares_out = tr.find_all('td')[1].text
            if 'M' in shares_out:
                financials['Shares Outstanding'] = float(shares_out[:-1]) * 1000
            elif 'B' in shares_out:
                financials['Shares Outstanding'] = float(shares_out[:-1]) * 1000000
        else:
            print "\tCould not gather Shares Outstanding..."
            financials['Shares Oustanding'] = 0.0
            driver.quit()
    else:
        print "\tCould not gather Shares Outstanding..."
        financials['Shares Oustanding'] = 0.0
        driver.quit()
    links_div = soup.find('div', {'id':'rec-by-symbol'})
    for a in links_div.find_all('a'):
        similar_companies.append(a.text)
    data['Similar Companies'] = similar_companies
    driver.quit()
    #End

    #Variables needed from financial statements:
    cost_of_revenue = financials['Cost of Revenue']
    inventory = financials['Inventory']
    total_revenue = financials['Total Revenue']
    current_assets = financials['Total Current Assets']
    current_liabilities = financials['Total Current Liabilities']
    long_term_debt = financials['Long-Term Debt']
    short_term_debt = financials['Short-Term Debt / Current Portion of Long-Term Debt']
    total_assets = financials['Total Assets']
    total_liabilities = financials['Total Liabilities']
    total_shareholder_equity = financials['Total Equity']
    net_income = financials['Net Income']
    shares_outstanding = financials['Shares Outstanding']
    market_price = data['Market Price']

    print "\tInventory Turnover: " + str(ratios.get_inventory_turnover(cost_of_revenue, inventory))
    data['Inventory Turnover'] = ratios.get_inventory_turnover(cost_of_revenue, inventory)
    print "\tWorking Capital Turnover: " + str(ratios.get_working_capital_turnover(total_revenue, current_assets, current_liabilities))
    data['Working Capital Ratio'] = ratios.get_working_capital_turnover(total_revenue, current_assets, current_liabilities)
    print "\tCurrent Ratio: " + str(ratios.get_current_ratio(current_assets, current_liabilities))
    data['Current Ratio'] = ratios.get_current_ratio(current_assets, current_liabilities)
    print "\tQuick Ratio: " + str(ratios.get_quick_ratio(current_assets, inventory, current_liabilities))
    data['Quick Ratio'] = ratios.get_quick_ratio(current_assets, inventory, current_liabilities)
    print "\tDebt Ratio: " + str(ratios.get_debt_ratio(long_term_debt, short_term_debt, total_assets))
    data['Debt Ratio'] = ratios.get_debt_ratio(long_term_debt, short_term_debt, total_assets)
    print "\tFinancial Leverage Ratio: " + str(ratios.get_financial_leverage_ratio(long_term_debt, short_term_debt, total_shareholder_equity))
    data['Financial Leverage Ratio'] = ratios.get_financial_leverage_ratio(long_term_debt, short_term_debt, total_shareholder_equity)
    print "\tNet Profit Margin: " + str(ratios.get_net_profit_margin(net_income, total_revenue))
    data['Net Profit Margin'] = ratios.get_net_profit_margin(net_income, total_revenue)
    print "\tReturn on Equity: " + str(ratios.get_return_on_equity(net_income, total_shareholder_equity))
    data['Return on Equity'] = ratios.get_return_on_equity(net_income, total_shareholder_equity)
    print "\tEarnings per Share: " + str(ratios.get_earnings_per_share(net_income, shares_outstanding))
    data['EPS'] = ratios.get_earnings_per_share(net_income, shares_outstanding)
    print "\tPrice to Earnings Ratio: " + str(ratios.get_price_to_earnings_ratio(market_price, ratios.get_earnings_per_share(net_income, shares_outstanding)))
    data['P/E Ratio'] = ratios.get_price_to_earnings_ratio(market_price,data['EPS'])
    
    return dict(data)
    #End


#Main Execution
ticker = raw_input("Enter company ticker: ")
print "Ticker: " + ticker
data = getFinancialInfo(ticker)
