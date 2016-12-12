#!/usr/bin/python

import ratios
import requests, os, re
from bs4 import BeautifulSoup
from selenium import webdriver
from yahoo_finance import Share

#Variable declaration and setup
ticker_symbol = 'KSS'
yahoo = Share(ticker_symbol)
url1 = 'http://finance.yahoo.com/quote/%s/financials?p=%s' % (ticker_symbol, ticker_symbol)
url2 = 'http://finance.yahoo.com/quote/%s/key-statistics?p=%s' % (ticker_symbol, ticker_symbol)
chromedriver = '/Users/Scott/chromedriver'
os.environ['webdriver.chrome.driver'] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get(url1)
#End

#Setting button links
quarterly_button = None
cash_flow_button = None
balance_sheet_button = None
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
div = driver.find_element_by_xpath("//div[@class='Mt(18px) Mb(14px)']")
all_buttons = div.find_elements_by_tag_name("button")
for button in all_buttons:
    if button.text == 'Quarterly':
        quarterly_button = button
    elif button.text == 'Cash Flow':
        cash_flow_button = button
    else:
        balance_sheet_button = button
#End

financial_statements = {}

#Getting Income Statement Data
quarterly_button.click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table', {'class':'Lh(1.7)'})
for tr in table.find_all('tr'):
    td = tr.find_all('td')
    if len(td) > 1:
        print td[0].text + ':'
        financial_statements[td[0].text] = []
        for i in range(1, len(td)):
            print '\t' + td[i].text
            if td[i].text != '-' and '/' not in td[i].text:
                financial_statements[td[0].text].append(float(td[i].text.replace(',', '')))
            else:
                financial_statements[td[0].text].append(td[i].text)
#End

#Getting Cash Flow Statement Data
cash_flow_button.click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table', {'class':'Lh(1.7)'})
for tr in table.find_all('tr'):
    td = tr.find_all('td')
    if len(td) > 1:
        print td[0].text + ':'
        financial_statements[td[0].text] = []
        for i in range(1, len(td)):
            print '\t' + td[i].text
            if td[i].text != '-' and '/' not in td[i].text:
                financial_statements[td[0].text].append(float(td[i].text.replace(',', '')))
            else:
                financial_statements[td[0].text].append(td[i].text)
#End

#Getting Balance Sheet Statement Data
balance_sheet_button.click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table', {'class':'Lh(1.7)'})
for tr in table.find_all('tr'):
    td = tr.find_all('td')
    if len(td) > 1:
        print td[0].text + ':'
        financial_statements[td[0].text] = []
        for i in range(1, len(td)):
            print '\t' + td[i].text
            if td[i].text != '-' and '/' not in td[i].text:
                financial_statements[td[0].text].append(float(td[i].text.replace(',', '')))
            else:
                financial_statements[td[0].text].append(td[i].text)
#End

#Getting Shares Outstanding Data
driver.get(url2)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
div = soup.find('div', {'class':'Pstart(20px)'})
table = div.find_all('table')[1]
tr = table.find_all('tr')[2]
shares_out = tr.find_all('td')[1].text
if 'M' in shares_out:
    financial_statements['Shares Outstanding'] = float(shares_out[:-1]) * 1000
elif 'B' in shares_out:
    financial_statements['Shares Outstanding'] = float(shares_out[:-1]) * 1000000
#End

if len(financial_statements) == 0:
    print "\nI'm sorry, but there are no financial statements available for %s.\n" % ticker_symbol
    driver.quit()
    exit()

driver.quit()


#Variables needed from financial statements:
cost_of_revenue = financial_statements['Cost of Revenue']
inventory = financial_statements['Inventory']
total_revenue = financial_statements['Total Revenue']
current_assets = financial_statements['Total Current Assets']
current_liabilities = financial_statements['Total Current Liabilities']
long_term_debt = financial_statements['Long Term Debt']
short_term_debt = financial_statements['Short/Current Long Term Debt']
total_assets = financial_statements['Total Assets']
total_liabilities = financial_statements['Total Liabilities']
total_shareholder_equity = financial_statements['Total Stockholder Equity']
net_income = financial_statements['Net Income']
shares_outstanding = financial_statements['Shares Outstanding']
market_price = float(yahoo.get_price())

print "Inventory Turnover: " + str(ratios.get_inventory_turnover(cost_of_revenue, inventory))
print "\nWorking Capital Turnover: " + str(ratios.get_working_capital_turnover(total_revenue, current_assets, current_liabilities))
print "\nCurrent Ratio: " + str(ratios.get_current_ratio(current_assets, current_liabilities))
print "\nQuick Ratio: " + str(ratios.get_quick_ratio(current_assets, inventory, current_liabilities))
print "\nDebt Ratio: " + str(ratios.get_debt_ratio(long_term_debt, short_term_debt, total_assets))
print "\nFinancial Leverage Ratio: " + str(ratios.get_financial_leverage_ratio(long_term_debt, short_term_debt, total_shareholder_equity))
print "\nNet Profit Margin: " + str(ratios.get_net_profit_margin(net_income, total_revenue))
print "\nReturn on Equity: " + str(ratios.get_return_on_equity(net_income, total_shareholder_equity))
print "\nEarnings per Share: " + str(ratios.get_earnings_per_share(net_income, shares_outstanding))
print "\nPrice to Earnings Ratio: " + str(ratios.get_price_to_earnings_ratio(market_price, ratios.get_earnings_per_share(net_income, shares_outstanding)))












