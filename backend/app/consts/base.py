import inspect
from enum import Enum


class AbstractBase(Enum):

    def __init__(self, number, chinese_name, code=None):
        self.__number = number
        self.__chinese_name = chinese_name
        self.__code = code

    """
    function name : must be one of the following:
        XXX_to_XXX
        XXX = chinese_name | number | code
        不做參數化
    """

    @classmethod
    def chinese_name_to_code(cls, value, many=False):
        return cls.__convert(value, inspect.currentframe().f_code.co_name, many=many)

    @classmethod
    def code_to_chinese_name(cls, value, many=False):
        return cls.__convert(value, inspect.currentframe().f_code.co_name, many=many)


    @property
    def code(self):
        return self.__code

    @property
    def chinese_name(self):
        return self.__chinese_name

    @property
    def number(self):
        return self.__number

    @classmethod
    def __convert(cls, value, func_name, many):
        source_value, target_value = func_name.split("_to_")
        result = []
        for item in cls.__members__.values():
            if many:
                if getattr(item, source_value) == value:
                    result.append(getattr(item, target_value))
            else:
                if getattr(item, source_value) == value:
                    return getattr(item, target_value)
        return result if many else None
