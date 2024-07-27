import sys
import inspect


class Structure:
    _fields = ()

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError("Expected %d arguments" % len(self._fields))
        for name, arg in zip(self._fields, args):
            setattr(self, name, arg)

    def __repr__(self):
        return f"{type(self).__name__}({', '.join(repr(getattr(self,name)) for name in self._fields)})"

    def __setattr__(self, name, value):
        if name not in self._fields or name.startswith("_"):
            raise AttributeError
        super().__setattr__(name, value)

    @classmethod
    def creat_init(cls):
        argstr = ",".join(cls._fields)
        code = f"def __init__(self,{argstr}):\n"
        self_attribute = [f"    self.{name} = {name}" for name in cls._fields]
        code += "\n".join(self_attribute)
        locs = {}
        exec(code, locs)
        cls.__init__ = locs["__init__"]


if __name__ == "__main__":

    class Stock(Structure):
        _fields = ("name", "shares", "price")
