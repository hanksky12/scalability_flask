import logging
from flask_jwt_extended import jwt_required
from flask_apispec import use_kwargs, marshal_with, doc
from marshmallow import Schema, fields

from .response import ResponseUtils, ResponseDto


class ApiDecoratorUtils:

    @staticmethod
    def integrate(tags_list,
                  request_schema,
                  response_schema,
                  http_method="not_get",
                  no_jwt_protection=False,
                  to_table=False
                  ):
        """
        tags_list:  apidoc tag
        request_schema(partial): check input condition ex:partial= True partial=["server"] partial=("server",)
        response_schema: filter output condition
        no_jwt_protection: close jwt authentication
        """

        def outer_wrapper(f):
            @doc(tags=tags_list)
            @use_kwargs(request_schema,
                        location=("querystring" if http_method.upper() == "GET" else 'json'))  # 需求的篩選與驗證 失敗就不會進到期下路由
            @marshal_with(ApiDecoratorUtils.combination_resp_schema(response_schema, is_list=to_table))
            def wrapper(*args, **kwargs):
                try:
                    return f(*args, **kwargs)
                except Exception as e:
                    logging.exception(e)
                    return ResponseUtils.inside_error()

            if no_jwt_protection or to_table:
                return wrapper
            else:
                # logging.info(f"add jwt_required to {f}")
                return jwt_required()(wrapper)

        return outer_wrapper

    @staticmethod
    def combination_resp_schema(schema, is_list=False):
        return Schema.from_dict(
            ResponseDto.get(
                code=fields.Int(),
                message=fields.Str(),
                total=fields.Int(),
                data=fields.List(fields.Nested(schema)) if is_list else fields.Nested(schema)))
