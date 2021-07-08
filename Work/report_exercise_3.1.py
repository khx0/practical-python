# report.py
#
# Exercise 3.1

import csv

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
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

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                name, price = row[0], float(row[1])
                prices[name] = price
            except IndexError:
                pass

    return prices

def make_report(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    rows = []
    for holding in portfolio:
        current_price = prices[holding['name']]
        change = current_price - holding['price']
        summary = (holding['name'], holding['shares'], current_price, change)
        rows.append(summary)
    return rows

def get_report(portfolio_file, prices_file) -> list:
    '''
    Creates a report from a portfolio and a prices list.
    Returns a report in form of a list
    '''
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)
    report = make_report(portfolio, prices)

    return report

def print_report(report: list):
    '''
    Print report in a formatted way to the screen.
    '''
    headers = ('Name', 'Shares', 'Price', 'Change')
    header_str = ' '.join([f'{h:>10s}' for h in headers])
    print(header_str)
    lstring = 10 * '-'
    print(f'{lstring:>10s} {lstring:>10s} {lstring:>10s} {lstring:>10s}')

    for name, shares, price, change in report:
        price_str = f'${round(price, 2)}'
        print(f'{name:>10s} {shares:>10d} {price_str:>10s} {change:>10.2f}')

report = get_report('Data/portfolio.csv', 'Data/prices.csv')
print_report(report)
