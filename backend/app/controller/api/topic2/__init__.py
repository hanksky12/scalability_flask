from flask import Blueprint
from flask_restful import Api

from ....create_app import docs

topic2_bp = Blueprint('topic2', __name__)
api = Api(topic2_bp)

api_dict = {
}

for route, api_resource in api_dict.items():
    api.add_resource(api_resource, route)
    docs.register(api_resource, blueprint=topic2_bp.name)
