# pcost.py
#
# Exercise 1.33

import csv
import sys

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

if (len(sys.argv) == 2):
    filename = sys.argv[1]
else:
    filename = 'Work/Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost', round(cost, 2))
