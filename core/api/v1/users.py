from typing import Sequence, Annotated

from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from client import postgresql_client
from models import User
from schemas.user import UserBase, UserCreate, UserRead

router = APIRouter(
    prefix='/users',
    tags=['users']
)

@router.get('', response_model=list[UserBase])
async def get_list(
        session: AsyncSession = Depends(postgresql_client.session_getter)
) -> Sequence[User]:
    stmt = select(User).order_by(User.id)
    result = await session.scalars(stmt)
    return result.all()

@router.post('', response_model=UserRead)
async def create(
    session: Annotated[AsyncSession, Depends(postgresql_client.session_getter)],
    data: UserCreate
) -> User:
    user = User(**data.model_dump())
    session.add(user)
    await session.commit()
    # await session.refresh(user)
    return user
