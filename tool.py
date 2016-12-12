import requests, os, re
from bs4 import BeautifulSoup
from selenium import webdriver

#Variable declaration and setup
ticker_symbol = 'JCP'
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

#Getting Income Statement Data
income_statement = {}
quarterly_button.click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table', {'class':'Lh(1.7)'})
for tr in table.find_all('tr'):
    td = tr.find_all('td')
    if len(td) > 1:
        income_statement[td[0].text] = []
        print td[0].text + ':'
        for i in range(1, len(td)):
            if td[i].text != '-' and '/' not in td[i].text:
                print "\tFloat"
                income_statement[td[0].text].append(float(td[i].text.replace(',', '')))
            else:
                print "\tText"
                income_statement[td[0].text].append(td[i].text)
#End

#Getting Cash Flow Statement Data
cash_flow = {}
cash_flow_button.click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table', {'class':'Lh(1.7)'})
for tr in table.find_all('tr'):
    td = tr.find_all('td')
    if len(td) > 1:
        cash_flow[td[0].text] = []
        print td[0].text + ':'
        for i in range(1, len(td)):
            if td[i].text != '-' and '/' not in td[i].text:
                print "\tFloat"
                cash_flow[td[0].text].append(float(td[i].text.replace(',', '')))
            else:
                print "\tText"
                cash_flow[td[0].text].append(td[i].text)
#End

#Getting Balance Sheet Statement Data
balance_sheet = {}
balance_sheet_button.click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table', {'class':'Lh(1.7)'})
for tr in table.find_all('tr'):
    td = tr.find_all('td')
    if len(td) > 1:
        balance_sheet[td[0].text] = []
        print td[0].text + ':'
        for i in range(1, len(td)):
            if td[i].text != '-' and '/' not in td[i].text:
                print "\tFloat"
                balance_sheet[td[0].text].append(float(td[i].text.replace(',', '')))
            else:
                print "\tText"
                balance_sheet[td[0].text].append(td[i].text)
#End

#Getting Shares Outstanding Data
shares_outstanding = ''
driver.get(url2)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
div = soup.find('div', {'class':'Pstart(20px)'})
table = div.find_all('table')[1]
tr = table.find_all('tr')[2]
shares_outstanding = tr.find_all('td')[1].text
if 'M' in shares_outstanding:
    shares_outstanding = float(shares_outstanding[:-1]) * 1000000
elif 'B' in statistic:
    shares_outstanding = float(shares_outstanding[:-1]) * 1000000000
#End

driver.quit()

avg_inventory = (float(balance_sheet['Inventory'][0]) + float(balance_sheet['Inventory'][3])) / 2.0
cogs = 0
for value in income_statement['Cost of Revenue']:
    cogs += value
inventory_turnover = cogs / avg_inventory
print 'Inventory Turnover: ' + str(inventory_turnover)
