# report.py
#
# Exercise 2.7

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
        headers = next(rows)
        for row in rows:
            holding = {
                'name':row[0], \
                'shares': int(row[1]), \
                'price': float(row[2])
            }
            portfolio.append(holding)

    return portfolio

def compute_loss(portfolio, prices, print_items = False):

    old_total = 0.0
    new_total = 0.0

    for holding in portfolio:
        old_value = holding['shares'] * holding['price']
        new_value = holding['shares'] * prices[holding['name']]
        diff = new_value - old_value
        if print_items:
            print(f"{holding['name']:<8s} {old_value:10.2f} {new_value:10.2f} {diff:10.2f}")
        old_total += old_value
        new_total += new_value

    diff_total = new_total - old_total
    return old_total, new_total, diff_total

prices = read_prices('Data/prices.csv')
portfolio = read_portfolio('Data/portfolio.csv')
old_total, new_total, diff_total = compute_loss(portfolio, prices, print_items = True)

print(f"Old Total:  {old_total:10.2f}")
print(f"New Total:  {new_total:10.2f}")
print(f"Difference: {diff_total:10.2f}")
