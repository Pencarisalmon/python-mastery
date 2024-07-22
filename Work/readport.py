import csv
from pprint import pprint


def read_portfolio(filename):
    portfolio = []
    with open(filename, "r") as f:
        print(f)
        rows = csv.reader(f)
        print(rows)
        headers = next(rows)
        print(headers)

        for row in rows:
            pprint(row)
            record = {"name": row[0], "shares": int(row[1]), "price": float(row[2])}
            portfolio.append(record)
    return portfolio
