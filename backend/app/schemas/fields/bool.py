from marshmallow import fields

from ...consts.bool import Bool
from ...utils.web.marshmallow import MarshmallowUtils


class BoolField(fields.Field):

    def _serialize(self, value, attr, data, **kwargs):
        return MarshmallowUtils.convert(
            value,
            Bool.code_to_chinese_name,
            "Bool code 不在選項內")

    def _deserialize(self, value, attr, data, **kwargs):  # load
        return MarshmallowUtils.convert(
            value,
            Bool.chinese_name_to_code,
            "Bool chinese_name 不在選項內")
