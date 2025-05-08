# mortgage.py
#
# Exercise 1.8

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

while principal > 0:
    month = month + 1
    current_payment = payment
    if month <= 12:
        current_payment = current_payment + 1000
    principal = principal * (1+rate/12) - current_payment
    total_paid = total_paid + current_payment
    

print('Total paid', total_paid)
print('Total months', month)
