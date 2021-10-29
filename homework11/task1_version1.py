""" Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.
from enum import Enum
class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"
class SizesEnum(Enum):
    XL = "XL"
    L = "L"
    M = "M"
    S = "S"
    XS = "XS"
Should become:
class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")
class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")
assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
"""


from enum import EnumMeta, Enum

class SimplifiedEnum(EnumMeta):
    def __new__(meta, cls, EnumMeta, classdict):
        keys_list = classdict.get(f'_{cls}__keys', [])
        cls_main = super().__new__(meta, cls, EnumMeta, classdict)
        for v in keys_list:
            setattr(cls_main, v, v)
        return cls_main



class ColorsEnum(Enum, metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(Enum, metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


print(ColorsEnum.RED)
print(SizesEnum.XL)

# assert ColorsEnum.RED == "RED"
