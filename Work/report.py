import csv
import sys
from pprint import pprint
from fileparse import parse_csv


def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    return parse_csv(filename, select=['name','shares','price'], types=[str,int,float])


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


def print_report(report: list, headers: tuple) -> None:
    """Prints pretty report"""
    if len(headers) != 4:
        raise ValueError(f'Headers have wrong length ({len(headers)}). Should be 4.')
    headers_string =  '%10s %10s %10s %10s' % headers
    
    dashes = ' '.join(['----------']*len(headers))

    print(headers_string)
    print(dashes)
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')


def portfolio_report(portfolio_filename: str, prices_filename: str) -> None:
    """
    Creates and prints report on portfolio of a given assets.
    """
    headers = ('Name', 'Shares', 'Price', 'Change')

    portfolio = parse_csv(portfolio_filename, select=['name','shares','price'], types=[str,int,float])
    prices = dict(parse_csv(prices_filename, types=[str,float], has_headers=False))

    report = make_report(portfolio, prices)
    print_report(report, headers)
