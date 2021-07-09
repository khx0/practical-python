# run_exercise_3.2.py
#
# Exercise 3.2 call script

from report_exercise_3_2 import portfolio_report

files = ['Data/portfolio.csv', 'Data/portfolio2.csv']

print()

for name in files:

    print(f'{name:-^43s}')
    portfolio_report(name, 'Data/prices.csv')

    print()
