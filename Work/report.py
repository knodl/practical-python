import csv
import sys
from pprint import pprint


def read_portfolio(filename: str) -> list:
    """Reads the portfolio files"""
    
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)  # skip the header
        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                 'name': record['name'],
                 'shares': int(record['shares']),
                 'price': float(record['price'])
            }
            try:
                portfolio.append(stock)
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


def compute_investment_results(portfolio: list, prices: dict) -> str:
    """Computes wheather portfolio makes money or losses"""

    result = 0.0
    for asset in portfolio:
        try:
            result += int(asset['shares']) * (float(prices[asset['name']])  - float(asset['price']))
        except KeyError:
            print('no asset in given prices', asset['name'])

    if result > 0:
        return f'Investments are success! Total profit = {result}'
    return f'Investments are failure! Total profit = {result}'


def make_report(portfolio: list, prices: dict) -> list:
    """Create the report on portfolio value change"""
    report = []
    for asset in portfolio:
        try:
            report.append((
                asset['name'],
                int(asset['shares']),
                float(prices[asset['name']]), 
                float(prices[asset['name']])  - float(asset['price'])
                ))
        except KeyError:
            print('no asset in given prices', asset['name'])

    return report


def prettify_report(report: list, headers: tuple) -> None:
    """Prints pretty report"""
    if len(headers) != 4:
        raise ValueError(f'Headers have wrong length ({len(headers)}). Should be 4.')
    headers_string =  '%10s %10s %10s %10s' % headers
    
    dashes = ' '.join(['----------']*len(headers))

    print(headers_string)
    print(dashes)
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfoliodate.csv'

prices = read_prices('Data/prices.csv')
portfolio = read_portfolio(filename)
report = make_report(portfolio, prices)
headers = ('Name', 'Shares', 'Price', 'Change')

prettify_report(report, headers)
