# report.py
#
# Exercise 2.8

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

    print(f"{'Name':>10s} {'Shares':>10s} {'Price':>10s} {'Change':>10s}")
    lstring = 10 * '-'
    print(f"{lstring:>10s} {lstring:>10s} {lstring:>10s} {lstring:>10s}")

    for holding in portfolio:
        old_value = holding['shares'] * holding['price']
        new_value = holding['shares'] * prices[holding['name']]
        diff = new_value - old_value
        diff_price = prices[holding['name']] - holding['price']
        if print_items:
            print(f"{holding['name']:>10s} {holding['shares']:>10d} {prices[holding['name']]:>10.2f} {diff_price:>10.2f}")
        old_total += old_value
        new_total += new_value

    diff_total = new_total - old_total
    return old_total, new_total, diff_total

prices = read_prices('Data/prices.csv')
portfolio = read_portfolio('Data/portfolio.csv')

old_total, new_total, diff_total = compute_loss(portfolio, prices, print_items = True)

# print(f"Old Total:  {old_total:10.2f}")
# print(f"New Total:  {new_total:10.2f}")
# print(f"Difference: {diff_total:10.2f}")

## TODO still working on exercise 2.8 to bring it into the format as specifiec by the exercise.
