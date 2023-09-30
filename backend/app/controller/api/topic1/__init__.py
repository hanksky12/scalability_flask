from flask import Blueprint
from flask_restful import Api

from ....create_app import docs
from .sub_topic1.sub_topic1 import SubTopic1Api

topic1_bp = Blueprint('topic1', __name__)
api = Api(topic1_bp)

api_dict = {
    "/sub_topic1": SubTopic1Api,
}

for route, api_resource in api_dict.items():
    api.add_resource(api_resource, route)
    docs.register(api_resource, blueprint=topic1_bp.name)
