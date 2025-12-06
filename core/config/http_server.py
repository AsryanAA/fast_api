from pydantic import BaseModel


class HTTPServer(BaseModel):
    host: str = '0.0.0.0'
    port: int = 8080