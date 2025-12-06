from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel

class User(BaseModel):
    username: Mapped[str] = mapped_column('username', unique=True)

    # foo: Mapped[int]
    # bar: Mapped[int]

    # __table_args__ = (
        # UniqueConstraint('foo', 'bar'),
    # )