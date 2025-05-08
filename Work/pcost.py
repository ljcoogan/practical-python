# pcost.py
#
# Exercise 1.32

import csv

def portfolio_cost(filename):
    f = open(filename)
    rows = csv.reader(f)
    next(f)

    sum = 0
    for row in rows:
        try:
            sum += int(row[1]) * float(row[2])
        except ValueError:
            print("Error: Line in file is missing necessary fields.")

    f.close()
    return sum

cost = portfolio_cost('Work/Data/missing.csv')
print('Total cost', round(cost, 2))
