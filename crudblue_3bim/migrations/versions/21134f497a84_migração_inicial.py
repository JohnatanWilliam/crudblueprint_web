"""Migração Inicial

Revision ID: 21134f497a84
Revises: 
Create Date: 2024-11-21 16:59:58.143206

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21134f497a84'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('loja',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=True),
    sa.Column('localizacao', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('produto',
    sa.Column('id_produto', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=True),
    sa.Column('id_loja', sa.Integer(), nullable=True),
    sa.Column('preco', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.ForeignKeyConstraint(['id_loja'], ['loja.id'], ),
    sa.PrimaryKeyConstraint('id_produto')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('produto')
    op.drop_table('loja')
    # ### end Alembic commands ###
