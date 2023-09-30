from marshmallow import fields
from .base import AbstractBaseSchema



class MessageSchema(AbstractBaseSchema):
    message = fields.Str()
