from marshmallow import Schema
import warnings

warnings.filterwarnings(
    "ignore",
    message="Multiple schemas resolved to the name "
)


class AbstractBaseSchema(Schema):
    default_error_messages = dict(required="缺少必要參數", type="數據類型錯誤", null="數據不能為空",
                                  validator_failed="驗證錯誤")
