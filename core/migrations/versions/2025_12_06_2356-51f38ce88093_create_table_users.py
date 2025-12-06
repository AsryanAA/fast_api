"""create table users

Revision ID: 51f38ce88093
Revises:
Create Date: 2025-12-06 23:56:00.240202

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "51f38ce88093"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('username', sa.String(), nullable=False),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('username'),
    )


def downgrade() -> None:
    op.drop_table('users')
