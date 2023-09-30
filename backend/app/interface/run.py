from abc import ABC, abstractmethod


class IRun(ABC):

    @abstractmethod
    def run(self):
        """執行"""
        pass
