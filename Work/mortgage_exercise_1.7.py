# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

months = 0
while principal > 0:
    principal = principal * (1.0 + rate / 12.0) - payment
    total_paid += payment
    months += 1

print('Total paid', total_paid)
print('Months =', months)
