import csv
import sys
from pprint import pprint


def read_portfolio(filename: str) -> list:
    """Reads the portfolio files"""
    
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)  # skip the header
        for row in rows:
            try:
                portfolio.append({'name': row[0], 'shares': int(row[1]), 'price': float(row[2])})
            except ValueError:
                print('broken line', row)

    return portfolio


def read_prices(filename: str) -> dict:
    """Reads the file with assets prices"""

    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[str(row[0])] = float(row[1])
            except (ValueError, IndexError):
                print('broken line', row)
    
    return prices


def compute_investment_results(portfolio: dict, prices: dict) -> str:
    """Computes wheather portfolio makes money or losses"""

    result = 0.0
    for asset in portfolio:
        try:
            result += asset['shares'] * (prices[asset['name']]  - asset['price'])
        except KeyError:
            print('no asset', asset['name'])

    if result > 0:
        return f'Investments are success! Total profit = {result}'
    return f'Investments are failure! Total profit = {result}'


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

prices = read_prices('Data/prices.csv')
portfolio = read_portfolio('Data/portfolio.csv')
result = compute_investment_results(portfolio, prices)
print(result)
