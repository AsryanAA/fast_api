from pydantic import BaseModel


class DatabasePostgres(BaseModel):
    host: str
    port: int
    user: str
    password: str
    name: str
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10