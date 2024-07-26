import csv


class Stock:
    __slots__ = ("name", "_shares", "_price")
    _types = (str, int, float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f"Stock({self.name!r}, {self.shares!r}, {self.price!r})"

    def __eq__(self, other):
        return isinstance(other, Stock) and (
            (self.name, self.shares, self.price)
            == (other.name, other.shares, other.price)
        )

    @property
    def shares(self):
        return self._shares

    @property
    def price(self):
        return self._price

    @shares.setter
    def shares(self, value):
        if isinstance(value, self._types[1]):
            if value < 0:
                raise ValueError(f"Expected non-negative {self._types[1].__name__}")
            self._shares = value
        else:
            raise TypeError(f"Expected {self._types[1].__name__}")

    @price.setter
    def price(self, value):
        if isinstance(value, self._types[2]):
            if value < 0:
                raise ValueError(f"Expected non-negative {self._types[2].__name__}")
            self._price = value
        else:
            raise TypeError(f"Expected {self._types[2].__name__}")

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, share):
        self.shares -= share
        return self.shares

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)


def print_portfolio(portfolio):
    headers = ["name", "shares", "price"]
    print(f"{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s}")
    print((("-" * 10) + " ") * 3)
    for data in portfolio:
        print(f"{data.name:>10s} {data.shares:>10d} {data.price:>10.2f}")
