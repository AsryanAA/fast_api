from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from api import router as api_router
from client import postgresql_client
from config.config import settings
# from models import BaseModel


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    # async with postgresql_client.engine.begin() as pg_client:
        # await pg_client.run_sync(BaseModel.metadata.drop_all)
    yield
    # shutdown
    print('dispose engine')
    await postgresql_client.dispose()

main_app = FastAPI(
    lifespan=lifespan
)
main_app.include_router(api_router, prefix=settings.api_prefix)

if __name__ == '__main__':
    uvicorn.run('main:main_app', host=settings.http_server.host, port=settings.http_server.port, reload=True)