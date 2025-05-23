"""add full_name, language, country, last_login to user

Revision ID: 0496bc299a6a
Revises: 1771172be9dc
Create Date: 2025-05-14 21:57:07.989379

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0496bc299a6a'
down_revision: Union[str, None] = '1771172be9dc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('full_name', sa.String(), nullable=True))
    op.add_column('user', sa.Column('language', sa.String(), nullable=True))
    op.add_column('user', sa.Column('country', sa.String(), nullable=True))
    op.add_column('user', sa.Column('last_login', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_login')
    op.drop_column('user', 'country')
    op.drop_column('user', 'language')
    op.drop_column('user', 'full_name')
    # ### end Alembic commands ###
