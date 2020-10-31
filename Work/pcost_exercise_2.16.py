# pcost.py
#
# Exercise 2.16

import sys
import csv

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    total_cost = 0.0

    with open(filename) as f:
        rows = csv.reader(f)
        header = next(rows)
        for rowno, row in enumerate(rows, start = 1):
            record = dict(zip(header, row))
            try:
                n_shares = int(record['shares'])
                price = float(record['price'])
                total_cost += n_shares * price
            # This catches errors in int() and float() conversions above.
            except ValueError:
                print(f"Row {rowno}: Couldn't convert: {row}")

    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfoliodate.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)  
