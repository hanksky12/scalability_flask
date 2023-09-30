from .base import AbstractBaseException


class UserException(AbstractBaseException):
    def __init__(self, message):
        super().__init__(message)
