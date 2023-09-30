import datetime
import os
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin

from .mysql import Development as MysqlDevelopment
from .mysql import Docker as MysqlDocker
from .mysql import Test as MysqlTest
from .mysql import Production as MysqlProduction


basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SQL_DB = 'db'
    APISPEC_SPEC = APISpec(
        title='Api文件',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    )
    APISPEC_SWAGGER_URL = '/apispec_json/'  # URI to access API Doc JSON
    APISPEC_SWAGGER_UI_URL = '/apispec/'  # URI to access UI of API Doc

    JWT_TOKEN_LOCATION = ['cookies']


class DevelopmentConfig(BaseConfig, MysqlDevelopment):
    DEBUG = True
    LOG_PATH = os.path.join(basedir, 'test_logs', 'dev', '')


class DockerConfig(BaseConfig, MysqlDocker):
    DEBUG = True
    LOG_PATH = os.path.join(basedir, 'test_logs', 'dev', '')


class TestConfig(BaseConfig, MysqlTest):
    DEBUG = True
    LOG_PATH = ""


class ProductionConfig(BaseConfig, MysqlProduction):
    DEBUG = False
    LOG_PATH = ""

