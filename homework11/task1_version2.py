from enum import Enum

class SimplifiedEnum(Enum):
    def __new__(meta, cls, Enum, classdict):
        keys_list = classdict.get(f'_{cls}__keys', [])
        cls_main = super().__new__(meta, cls, Enum, classdict)
        for v in keys_list:
            setattr(cls_main, v, v)
        return cls_main



class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


print(ColorsEnum.RED)
print(SizesEnum.XL)
