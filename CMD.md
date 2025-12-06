Создание виртуального окружения
```shell

python3 -m venv venv42

source venv42/bin/activate

uvicorn main:app --reload --port=8044
```

Установка зависимостей
```shell

pip install black

pip freeze -> requirements.txt
```

```shell

poetry add fastapi 'uvicorn[standard]' 'pydantic[email]' 'sqlalchemy[asyncio]' pydantic-settings asyncpg
```