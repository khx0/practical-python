# exercise_2.6.py

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

# prices = read_prices('Data/prices.csv')
# from pprint import pprint
# pprint(prices)
