"""add comment order column

Revision ID: 4e40a7fb1603
Revises: 6dda8f40947d
Create Date: 2023-10-30 18:47:09.518631

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4e40a7fb1603'
down_revision: Union[str, None] = '6dda8f40947d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('order_links', sa.Column('order_comment', sa.String(255), nullable=True))


def downgrade() -> None:
    op.drop_column("order_links", "order_comment")
