from pydantic_settings import BaseSettings, SettingsConfigDict

from config.db import DatabasePostgres
from config.http_server import HTTPServer


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=('.env.example', '.env'), # каждый последующий перегружает предыдущий
        case_sensitive=False,
        env_nested_delimiter='__',
        env_prefix='APP_CONFIG__'
    )
    api_prefix: str = '/api'

    http_server: HTTPServer = HTTPServer()
    db: DatabasePostgres


settings = Settings()
print(settings)