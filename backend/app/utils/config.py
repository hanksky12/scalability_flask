import logging
import os

from dotenv import get_key


class ConfigUtil:
    config = None
    env_config = None

    """
    make .env file in config folder under execution project

    .env file example:
    CONFIG=development(or test, production, docker)
    """

    @classmethod
    def init(cls, env_path, **kwargs):
        # print(f"env_path: {env_path} kwargs: {kwargs}")
        cls.env_path = env_path
        cls.config = kwargs

    @classmethod
    def get_env_config(cls):
        if os.path.exists(cls.env_path):
            return get_key(cls.env_path, "CONFIG")
        return os.environ.get('CONFIG')

    @classmethod
    def get(cls):
        if cls.env_config is None:
            cls.env_config = cls.get_env_config()
            # print(f"env_config: {cls.env_config}")
        return cls.config.get(cls.env_config)