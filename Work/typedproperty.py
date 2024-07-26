def typedproperty(name, expected_type):
    private_name = "+" + name

    def __set_name__(self, cls, name):
        self.name = name

    @property
    def value(self):
        return getattr(self, private_name)

    @value.setter
    def value(self, val):
        if not isinstance(value, expected_type):
            raise TypeError(f"Expected {expected_type.__name__}")
        setattr(self, private_name, val)

    return value


String = lambda name: typedproperty(name, str)
Integer = lambda name: typedproperty(name, int)
Float = lambda name: typedproperty(name, float)

if __name__ == "__main__":

    class Stock:
        name = String("name")
        shares = Integer("shares")
        price = Float("price")

        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price
