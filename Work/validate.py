class Validator:
    def __init__(self, name=None):
        self.name = name

    def __set_name__(self, cls, name):
        self.name = name

    @classmethod
    def check(cls, value):
        return value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)


class Typed(Validator):
    expected_type = object

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f"Expected {cls.expected_type.__name__}")
        return super().check(value)


class NonEmpty(Validator):
    @classmethod
    def check(cls, value):
        if len(value) == 0:
            raise ValueError("Value must be non-empty")
        return super().check(value)


class Integer(Typed):
    expected_type = int


class Float(Typed):
    expected_type = float


class String(Typed):
    expected_type = str


class Postive(Validator):
    @classmethod
    def check(cls, value):
        if value < 0:
            raise ValueError("Expected Positive")
        return super().check(value)


class PositiveInteger(Integer, Postive):
    pass


class PositiveFloat(Float, Postive):
    pass


class NonEmptyString(String, NonEmpty):
    pass
