import os
from logging import config as logging_config

from pydantic import BaseSettings, Field

from core.logger import LOGGING

logging_config.dictConfig(LOGGING)


class Settings(BaseSettings):
    debug: str = Field('False', env='DEBUG')
    api_version: str = Field('v1', env='API_VERSION')
    jwt_secret: str = Field('qwerty', env='JWT_SECRET')
    jwt_algorithm: str = Field('HS256', env='JWT_ALGORITHM')
    project_name: str = Field('ugc_api', env='PROJECT_NAME')

    kafka_host: str = Field('kafka', env='KAFKA_HOST')
    kafka_port: int = Field(9092, env='KAFKA_PORT')

    base_dir: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


settings = Settings()
