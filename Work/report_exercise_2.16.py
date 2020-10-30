# report.py
#
# Exercise 2.16

import csv

def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                name, price = row[0], float(row[1])
                prices[name] = price
            except: pass
    return prices

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            holding = dict(zip(header, row))
            try: 
                holding['price'] = float(holding['price'])
                holding['shares'] = int(holding['shares'])
            except: pass
            portfolio.append(holding)
    return portfolio

def make_report(portfolio, prices):
    report = []
    for holding in portfolio:
        new_price = prices[holding['name']]
        change = new_price - holding['price']
        holding = (holding['name'], holding['shares'], new_price, change)
        report.append(holding)
    return report

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')
header_str = ' '.join([f'{h:>10s}' for h in headers])
print(header_str)
lstring = 10 * '-'
print(f'{lstring:>10s} {lstring:>10s} {lstring:>10s} {lstring:>10s}')

for name, shares, price, change in report:
    price_str = f'${round(price, 2)}'
    print(f'{name:>10s} {shares:>10d} {price_str:>10s} {change:>10.2f}')
