# mortgage.py
#
# Exercise 1.8

principal = 500000.0
rate = 0.05
payment_base = 2684.11
total_paid = 0.0

months = 0
while principal > 0:
    if months < 12:
        payment = payment_base + 1000.0
    else:
        payment = payment_base
    principal = principal * (1.0 + rate / 12.0) - payment
    total_paid += payment
    months += 1

print('Total paid', total_paid)
print('Months =', months)
