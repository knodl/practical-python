#!/usr/bin/env python3

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


def main(argv):
    import sys
    if len(sys.argv) == 2:
        cost = portfolio_cost(sys.argv[1])
        print(f'Total cost: {cost}')
    else:
        raise SystemExit('Usage: %s portfile' % sys.argv[0])


if __name__ == "__main__":
    main(sys.argv)
