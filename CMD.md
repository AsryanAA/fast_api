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

poetry add --group dev black
```

Инициализация асинхронного alembic и его команды
```shell

alembic init -t async migrations

alembic revision --autogenerate -m 'create table users'
alembic upgrade head
alembic downgrade -1
alembic downgrade base
```