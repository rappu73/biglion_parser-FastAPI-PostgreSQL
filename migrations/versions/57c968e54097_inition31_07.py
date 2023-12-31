"""Inition31/07

Revision ID: 57c968e54097
Revises: 
Create Date: 2023-07-31 10:48:08.961884

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57c968e54097'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cat', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('link',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_link', sa.String(), nullable=False),
    sa.Column('city_id', sa.Integer(), nullable=True),
    sa.Column('cat_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cat_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['city_id'], ['cities.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('link')
    op.drop_table('cities')
    op.drop_table('category')
    # ### end Alembic commands ###
