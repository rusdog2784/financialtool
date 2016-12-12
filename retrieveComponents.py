import csv
import os

os.system('table2csv http://slickcharts.com/sp500 >> Data/sp500.txt')
os.system('table2csv http://slickcharts.com/nasdaq100 >> Data/nasdaq.txt')

sp500 = []
nasdaq = []

with open('Data/sp500.txt') as theFile:
    for line in theFile:
        row = {}
        lineArray = line.split('|')
        if '=' in lineArray[2]:
            row['name'] = lineArray[0]
            row['ticker'] = lineArray[2].split('=')[1].replace('\n', '')
            sp500.append(dict(row))

with open('Data/nasdaq.txt') as theFile:
    for line in theFile:
        row = {}
        lineArray = line.split('|')
        if '=' in lineArray[2]:
            row['name'] = lineArray[0]
            row['ticker'] = lineArray[2].split('=')[1].replace('\n', '')
            nasdaq.append(dict(row))

for row in nasdaq:
    print 'Company: ' + row['name'] + ' (' + row['ticker'] + ')'
