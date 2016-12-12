    #!/usr/bin/python

import ratios
import requests, os, re
from bs4 import BeautifulSoup
from selenium import webdriver
from yahoo_finance import Share

def get_financial_data(ticker):
    data = {}
    financial_statements = {}
    
    #Variable declaration and setup
    yahoo = Share(ticker)
    url1 = 'http://finance.yahoo.com/quote/%s/financials?p=%s' % (ticker, ticker)
    url2 = 'http://finance.yahoo.com/quote/%s/key-statistics?p=%s' % (ticker, ticker)
    chromedriver = '/Users/Scott/chromedriver'
    os.environ['webdriver.chrome.driver'] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.get(url1)
    #End
    
    #Setting button links
    quarterly_button = None
    cash_flow_button = None
    balance_sheet_button = None
    similar_companies = []
    div = driver.find_element_by_xpath("//div[@class='Mt(18px) Mb(14px)']")
    all_buttons = div.find_elements_by_tag_name("button")
    for button in all_buttons:
        if button.text == 'Quarterly':
            quarterly_button = button
        elif button.text == 'Cash Flow':
            cash_flow_button = button
        else:
                balance_sheet_button = button
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    links_div = soup.find('div', {'id':'rec-by-symbol'})
    for a in links_div.find_all('a'):
        similar_companies.append(a.text)
    data['similar_companies'] = similar_companies
    #End

    #Getting Income Statement Data
    quarterly_button.click()
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', {'class':'Lh(1.7)'})
    for tr in table.find_all('tr'):
        td = tr.find_all('td')
        if len(td) > 1:
            #print td[0].text + ':'
            financial_statements[td[0].text] = []
            for i in range(1, len(td)):
                #print '\t' + td[i].text
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
            #print td[0].text + ':'
            financial_statements[td[0].text] = []
            for i in range(1, len(td)):
                #print '\t' + td[i].text
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
            #print td[0].text + ':'
            financial_statements[td[0].text] = []
            for i in range(1, len(td)):
                #print '\t' + td[i].text
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
        return {}

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

    print "\tInventory Turnover: " + str(ratios.get_inventory_turnover(cost_of_revenue, inventory))
    data['inventory_turnover_ratio'] = ratios.get_inventory_turnover(cost_of_revenue, inventory)
    print "\tWorking Capital Turnover: " + str(ratios.get_working_capital_turnover(total_revenue, current_assets, current_liabilities))
    data['working_capital_ratio'] = ratios.get_working_capital_turnover(total_revenue, current_assets, current_liabilities)
    print "\tCurrent Ratio: " + str(ratios.get_current_ratio(current_assets, current_liabilities))
    data['current_ratio'] = ratios.get_current_ratio(current_assets, current_liabilities)
    print "\tQuick Ratio: " + str(ratios.get_quick_ratio(current_assets, inventory, current_liabilities))
    data['quick_ratio'] = ratios.get_quick_ratio(current_assets, inventory, current_liabilities)
    print "\tDebt Ratio: " + str(ratios.get_debt_ratio(long_term_debt, short_term_debt, total_assets))
    data['debt_ratio'] = ratios.get_debt_ratio(long_term_debt, short_term_debt, total_assets)
    print "\tFinancial Leverage Ratio: " + str(ratios.get_financial_leverage_ratio(long_term_debt, short_term_debt, total_shareholder_equity))
    data['financial_leverage_ratio'] = ratios.get_financial_leverage_ratio(long_term_debt, short_term_debt, total_shareholder_equity)
    print "\tNet Profit Margin: " + str(ratios.get_net_profit_margin(net_income, total_revenue))
    data['net_profit_margin'] = ratios.get_net_profit_margin(net_income, total_revenue)
    print "\tReturn on Equity: " + str(ratios.get_return_on_equity(net_income, total_shareholder_equity))
    data['return_on_equity'] = ratios.get_return_on_equity(net_income, total_shareholder_equity)
    print "\tEarnings per Share: " + str(ratios.get_earnings_per_share(net_income, shares_outstanding))
    data['earnings_per_share'] = ratios.get_earnings_per_share(net_income, shares_outstanding)
    print "\tPrice to Earnings Ratio: " + str(ratios.get_price_to_earnings_ratio(market_price, ratios.get_earnings_per_share(net_income, shares_outstanding)))
    data['price_to_earnings_ratio'] = ratios.get_price_to_earnings_ratio(market_price,data['earnings_per_share'])

    return dict(data)


#Start of Program
companies = []
company = {}
ticker = raw_input("Enter company ticker: ")
print "\nGathering information for " + ticker + "..."
company['ticker'] = ticker
company['data'] = get_financial_data(ticker)
companies.append(dict(company))
company = {}
for ticker in companies[0]['data']['similar_companies']:
    print "\nGathering information for " + ticker + "..."
    company['ticker'] = ticker
    company['data'] = get_financial_data(ticker)
    companies.append(dict(company))
    company = {}
print "\n\nALL DATA HAS BEEN COLLECTED.\n"

for comp in companies:
    print "\nCompany: " + comp['ticker']
    data = comp['data']
    print "\tInventory Turnover: " + str(data['inventory_turnover_ratio'])
    print "\tWorking Capital Turnover: " + str(data['working_capital_ratio'])
    print "\tCurrent Ratio: " + str(data['current_ratio'])
    print "\tQuick Ratio: " + str(data['quick_ratio'])
    print "\tDebt Ratio: " + str(data['debt_ratio'])
    print "\tFinancial Leverage Ratio: " + str(data['financial_leverage_ratio'])
    print "\tNet Profit Margin: " + str(data['net_profit_margin'])
    print "\tReturn on Equity: " + str(data['return_on_equity'])
    print "\tEarnings per Share: " + str(data['earnings_per_share'])
    print "\tPrice to Earnings Ratio: " + str(data['price_to_earnings_ratio'])
    print "\tSimilar Companies: " + str(data['similar_companies'])
    print "==========================================================================="

#End of Program











