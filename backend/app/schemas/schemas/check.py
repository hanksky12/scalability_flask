from .base import AbstractBaseSchema
from ..fields.bool import BoolField


class CheckSchema(AbstractBaseSchema):
    outside_exist_check = BoolField(required=True, attribute="inside_exist_check")
