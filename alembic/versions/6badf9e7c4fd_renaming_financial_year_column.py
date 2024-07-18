"""Renaming financial_year column

Revision ID: 6badf9e7c4fd
Revises: 8eac8169dfd0
Create Date: 2024-07-18 09:03:27.218633

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6badf9e7c4fd'
down_revision: Union[str, None] = '8eac8169dfd0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('forecasts', sa.Column('financial_year', sa.String(), nullable=True))
    op.drop_index('ix_forecasts_org_id', table_name='forecasts')
    op.drop_column('forecasts', 'finacial_year')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('forecasts', sa.Column('finacial_year', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.create_index('ix_forecasts_org_id', 'forecasts', ['org_id'], unique=False)
    op.drop_column('forecasts', 'financial_year')
    # ### end Alembic commands ###