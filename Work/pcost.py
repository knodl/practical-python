import csv
import sys


def portfolio_cost(filename: str) -> float:
    """Returns the total cost of the portfolio"""
    
    with open(filename, 'rt') as f:
        total_cost = 0
        rows = csv.reader(f)
        headers = next(rows)
        for idx, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                total_cost += int(record['shares']) * float(record['price'])
            except ValueError:
                print(f'Row {idx}: Couldn\'t convert: {row}')

    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'


cost = portfolio_cost(filename)
print(f'Total cost: {cost}')
