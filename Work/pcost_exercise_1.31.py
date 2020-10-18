# pcost.py
#
# Exercise 1.31

def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename, 'rt') as f:
        header = next(f)
        for line in f:
            try:
                row = line.split(',')
                n_stocks, price = int(row[1]), float(row[2])
                total_cost += n_stocks * price
            except ValueError:
                line = line.strip()
                print(f'ValueError while reading {filename}. Could not parse line: {line}')

    return total_cost

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)    
