# pcost.py
#
# Exercise 1.27

f = open('Work/Data/portfolio.csv')
next(f)

sum = 0
for line in f:
    row = line.split(',')
    sum += int(row[1]) * float(row[2])

f.close()

print('Total cost', round(sum, 2))
