from marshmallow import fields, ValidationError


class MarshmallowUtils:

    @staticmethod
    def convert(value, func, validation_failed_str):
        try:
            # func 可能是藉由const 轉換，也可以是自定義，不適合更複雜化
            _convert_value = func(value)
        except KeyError:
            raise ValidationError("column KEY ERROR")
        if _convert_value is None:
            raise ValidationError(validation_failed_str)
        return _convert_value
