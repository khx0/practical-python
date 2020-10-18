# pcost.py
#
# Exercise 1.32

import csv

def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename) as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            try:
                n_stocks, price = int(row[1]), float(row[2])
                total_cost += n_stocks * price
            except ValueError:
                print(f'ValueError while reading {filename}. Could not parse row: {row}')

    return total_cost

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)    
