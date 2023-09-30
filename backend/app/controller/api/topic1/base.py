from flask_apispec import MethodResource


class AbstractBaseMethodResource(MethodResource):
    tags_list = ["topic1"]
    pass
