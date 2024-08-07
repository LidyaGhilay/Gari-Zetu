"""first initialization

Revision ID: b93a3611ba0c
Revises: 
Create Date: 2024-07-13 12:31:01.802095

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b93a3611ba0c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('addcatalogues',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.Text(), nullable=False),
    sa.Column('brand', sa.Text(), nullable=False),
    sa.Column('model', sa.Text(), nullable=False),
    sa.Column('category', sa.Text(), nullable=False),
    sa.Column('price', sa.Text(), nullable=False),
    sa.Column('rating', sa.Text(), nullable=False),
    sa.Column('release_date', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_addcatalogues'))
    )
    op.create_table('catalogues',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.Text(), nullable=False),
    sa.Column('brand', sa.Text(), nullable=False),
    sa.Column('model', sa.Text(), nullable=False),
    sa.Column('category', sa.Text(), nullable=False),
    sa.Column('price', sa.Text(), nullable=False),
    sa.Column('rating', sa.Text(), nullable=False),
    sa.Column('release_date', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_catalogues'))
    )
    op.create_table('news',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.Text(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('ticket_price', sa.Text(), nullable=False),
    sa.Column('date', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_news'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('news')
    op.drop_table('catalogues')
    op.drop_table('addcatalogues')
    # ### end Alembic commands ###
