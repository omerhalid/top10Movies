"""release date changed to integer

Revision ID: 9ce14ff4856b
Revises: 68d2dd92d812
Create Date: 2023-11-18 23:12:42.766495

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '9ce14ff4856b'
down_revision: Union[str, None] = '68d2dd92d812'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('movies', 'release_date',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.Integer(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('movies', 'release_date',
               existing_type=sa.Integer(),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=True)
    # ### end Alembic commands ###