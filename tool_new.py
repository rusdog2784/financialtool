import json
import urllib.request as ur
from bs4 import BeautifulSoup
from yfinance import Ticker
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pprint
pp = pprint.PrettyPrinter(indent=2)


INCOME_STATEMENT_VARIABLE_NAMES = [
    'Cost of Revenue',
    'Total Revenue',
    'Net Income Common Stockholders'
]
BALANCE_SHEET_VARIABLE_NAMES = [
    'Inventory',
    'Current Assets',
    'Current Liabilities',
    'Long Term Debt',
    'Current Debt',
    'Total Assets',
    'Total Liabilities Net Minority Interest',
    "Stockholders' Equity"
]


TICKER = input("Enter company ticker: ")


URL_INCOME_STATEMENT = f"https://finance.yahoo.com/quote/{TICKER}/financials?p={TICKER}"
URL_BALANCE_SHEET = f"https://finance.yahoo.com/quote/{TICKER}/balance-sheet?p={TICKER}"
URL_CASH_FLOW = f"https://finance.yahoo.com/quote/{TICKER}/cash-flow?p={TICKER}"


#######################################################################
# INCOME STATEMENT ####################################################
read_data = ur.urlopen(URL_INCOME_STATEMENT).read()
soup = BeautifulSoup(read_data, 'lxml')
all_spans = list()
for span in soup.find_all('span'):
    all_spans.append(span.string) if span.string not in ('Operating Expenses', 'Non-recurring Events') else None
filtered_spans = list(filter(None, all_spans))

income_statement_values = list()
for i in range(0, len(filtered_spans)):
    if filtered_spans[i] in INCOME_STATEMENT_VARIABLE_NAMES:
        income_statement_values.append(tuple(filtered_spans[i:i+6]))
pp.pprint(income_statement_values)
#######################################################################
#######################################################################


#######################################################################
# BALANCE SHEET #######################################################
read_data = ur.urlopen(URL_BALANCE_SHEET).read()
soup = BeautifulSoup(read_data, 'lxml')
# all_spans = list()
# for span in soup.find_all('span'):
#     all_spans.append(span.string) if span.string not in ('Operating Expenses', 'Non-recurring Events') else None
# filtered_spans = list(filter(None, all_spans))

for script in soup.find_all('script'):
    if '/* -- Data -- */' in str(script.string):
        print("Found it")
        start = '"balanceSheetHistory":'
        end = '"cashflowStatementHistoryQuarterly"'
        long_string = str(script.string)
        json_string = long_string[long_string.index(start) + len(start):long_string.index(end) - 1]
        json_data = json.loads(json_string)
        print(type(json_data))
        with open('temp_out.json', 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)

# balance_sheet_values = list()
# for i in range(0, len(filtered_spans)):
#     if filtered_spans[i] in BALANCE_SHEET_VARIABLE_NAMES:
#         balance_sheet_values.append(tuple(filtered_spans[i:i+6]))
# pp.pprint(balance_sheet_values)
#######################################################################
#######################################################################