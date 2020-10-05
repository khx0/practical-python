# mortgage.py
#
# Exercise 1.11

principal = 500000.0
rate = 0.05
payment = 2684.11

extra_payment_start_month = 61 # 49
extra_payment_end_month = 108  # 49 + 4 * 12
extra_payment = 1000.0

total_paid = 0.0
months = 0

while principal > 0:

    months += 1
    principal = principal * (1.0 + rate / 12.0) - payment
    total_paid += payment

    if months >= extra_payment_start_month and \
       months <= extra_payment_end_month:
       principal  -= extra_payment
       total_paid += extra_payment

    if principal < 0:
        total_paid -= abs(principal)
        principal  += abs(principal)

    print(months, round(total_paid, 2), round(principal, 2))

print('Total paid', round(total_paid, 2))
print('Months', months)
