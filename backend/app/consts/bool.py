
from .base import AbstractBase


class Bool(AbstractBase):
    Yes = (1, "是", True)
    No = (0, "否", False)

    def __init__(self, number, chinese_name, code):
        super().__init__(number, chinese_name, code)

