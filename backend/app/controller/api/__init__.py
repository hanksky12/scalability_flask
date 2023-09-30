from flask import Blueprint

from .upload import upload_bp
from .crawler import crawler_bp

# for 模組區分

api_bp = Blueprint('api', __name__)

api_bp.register_blueprint(upload_bp, url_prefix='/upload')

api_bp.register_blueprint(crawler_bp, url_prefix='/crawler')
