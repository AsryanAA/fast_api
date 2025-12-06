from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr
from sqlalchemy.testing.schema import mapped_column

from utils import camel_case_to_snake_case


class BaseModel(DeclarativeBase):
    __abstract__ = True # не обязательно указывать

    @declared_attr.directive
    def __tablename__(self) -> str:
        return f'{camel_case_to_snake_case(self.__name__)}s'

    id = Mapped[int] = mapped_column('id', primary_key=True)