"""v_02

Revision ID: 1c795dc1be73
Revises: 340313378448
Create Date: 2024-04-17 11:16:48.312837

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1c795dc1be73'
down_revision: Union[str, None] = '340313378448'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Blog', sa.Column('name', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Blog', 'name')
    # ### end Alembic commands ###
