"""add content column to posts table

Revision ID: a7fad83a395d
Revises: 8a98eca83b60
Create Date: 2022-04-19 11:38:08.739403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7fad83a395d'
down_revision = '8a98eca83b60'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('post', 'content')
    pass
