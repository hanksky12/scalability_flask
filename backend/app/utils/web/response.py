from ...dto.response import ResponseDto
from ...dto.message import MessageDto
from ...dto.table import TableDto


class ResponseUtils:
    """
    ＃基本定義:
    200:請求成功 & 執行成功
    201:請求成功 & 執行失敗
    其他:請求失敗
    ~~~~~~~~~~~~~~~~~~~~~
    """

    @classmethod
    def process_msg_dto(cls, message_dto: MessageDto):
        if message_dto.success:
            return cls.success(data={"message": message_dto.message})
        return cls.handling_failed(message=message_dto.message)

    @classmethod
    def process_table_dto(cls, table_dto: TableDto):
        return cls.success_to_table(data_list=table_dto.data_list, total=table_dto.total)

    @classmethod
    def success(cls, message="請求成功", data=None):
        return ResponseDto.get(
            code=200,
            message=message,
            data=data)

    @classmethod
    def success_to_table(cls, data_list, total):
        # data_list 與 total 為必傳參數，前端bootstrap table才能生成
        return ResponseDto.get(
            code=200,
            message="查詢成功",
            data=data_list,
            total=total)

    @classmethod
    def handling_failed(cls, message):
        return ResponseDto.get(
            code=201,
            message=message)
