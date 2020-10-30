#o
# Exercise 2.15

import sys
import csv

def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename) as f:
        rows = csv.reader(f)
        header = next(rows)
        for rowno, row in enumerate(rows, start = 1):
            try:
                n_stocks, price = int(row[1]), float(row[2])
                total_cost += n_stocks * price
            except ValueError:
                print(f"Row {rowno}: Couldn't convert: {row}")

    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/missing.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)    
