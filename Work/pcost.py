# pcost.py
#
# Exercise 1.27

filename = 'Data/portfolio.csv'

total_cost = 0.0

with open(filename, 'rt') as f:
    header = next(f)
    for line in f:
        row = line.split(',')
        n_stocks, price = int(row[1]), float(row[2])
        total_cost += n_stocks * price

print(f'Total cost {total_cost:5.2f}')    
