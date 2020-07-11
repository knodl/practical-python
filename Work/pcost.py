import csv
import sys
from report import read_portfolio


def portfolio_cost(filename: str) -> float:
    """Returns the total cost of the portfolio"""
    
    portfolio = read_portfolio(filename)
    total_cost = 0
    for asset in portfolio:
            total_cost += asset['shares'] * asset['price']
    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'


cost = portfolio_cost(filename)
print(f'Total cost: {cost}')
