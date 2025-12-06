from pydantic_settings import BaseSettings

from config.http_server import HTTPServer


class Settings(BaseSettings):
    api_prefix: str = '/api'

    http_server: HTTPServer = HTTPServer()

settings = Settings()