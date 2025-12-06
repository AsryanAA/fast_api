import uvicorn
from fastapi import FastAPI
from api import router as api_router
from config.config import settings

app = FastAPI()
app.include_router(api_router, prefix=settings.api_prefix)

if __name__ == '__main__':
    uvicorn.run('main:app', host=settings.http_server.host, port=settings.http_server.port, reload=True)