from .....utils.web.api import ApiDecoratorUtils
from .....utils.web.response import ResponseUtils

from .....services.topic1.sub_topic1.services1 import Services1
from .....services.topic1.sub_topic1.services2 import Services2
from .....schemas.schemas import CheckSchema, EmptySchema, MessageSchema
from ..base import AbstractBaseMethodResource


# 組合出特殊需求的schema for 單一api
class ServicesSchema(CheckSchema, MessageSchema):
    pass


class SubTopic1Api(AbstractBaseMethodResource):
    @ApiDecoratorUtils.integrate(
        tags_list=AbstractBaseMethodResource.tags_list,
        request_schema=CheckSchema,
        response_schema=MessageSchema,
    )
    def put(self, **kwargs):
        # 藉由schema 做驗證 且 可取得內部對應的參數值
        services = Services1(**kwargs)
        msg_dto = services.run()
        return ResponseUtils.process_msg_dto(msg_dto)

    ###################################################################################
    @ApiDecoratorUtils.integrate(
        tags_list=AbstractBaseMethodResource.tags_list,
        request_schema=EmptySchema,
        response_schema=ServicesSchema,
        http_method='get',
        to_table=True
    )
    def get(self, **kwargs):
        services = Services2(**kwargs)
        table_dto = services.run()
        return ResponseUtils.process_table_dto(table_dto)
