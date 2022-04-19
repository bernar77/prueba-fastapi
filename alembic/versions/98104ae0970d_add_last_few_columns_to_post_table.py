"""add last few columns to post table

Revision ID: 98104ae0970d
Revises: 579020354f17
Create Date: 2022-04-19 13:08:45.844848

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98104ae0970d'
down_revision = '579020354f17'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column( 'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column( 'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
