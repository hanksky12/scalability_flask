import os

from flask import Flask
from flask_apispec.extension import FlaskApiSpec

from utils.db import SqlUtil
from utils.log import LogUtil
from utils.config import ConfigUtil

from config.config import DevelopmentConfig, TestConfig, ProductionConfig, DockerConfig


class FlaskApp:
    @classmethod
    def create(cls):
        cls.app = Flask(__name__)


class Extension:

    def __init__(self):
        ConfigUtil.init(
            env_path=os.path.join(os.path.abspath(os.path.dirname(__file__)), "config", '.env'), # 由 run_app 的地方決定
            development=DevelopmentConfig,
            docker=DockerConfig,
            test=TestConfig,
            production=ProductionConfig,
        )
        self.__config = ConfigUtil.get()

    def log_init(self):
        LogUtil.init(
            level=self.__config.DEBUG,
            log_path=self.__config.LOG_PATH,
            log_name="web"
        )

    def sql_init(self):
        SqlUtil.init(
            user=self.__config.SQL_USER,
            password=self.__config.SQL_PASSWORD,
            host=self.__config.SQL_HOST,
            port=self.__config.SQL_PORT,
            db=self.__config.SQL_DB)


    def generate_flaskapispec(self):
        docs = FlaskApiSpec()
        return docs
