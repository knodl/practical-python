import csv
import sys


def portfolio_cost(filename: str) -> float:
    """Returns the total cost of the portfolio"""
    
    with open(filename, 'rt') as f:
        total_cost = 0
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            try:
                total_cost += int(row[1]) * float(row[2])
            except ValueError:
                print('broken line', row)

    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'


cost = portfolio_cost(filename)
print(f'Total cost: {cost}')
