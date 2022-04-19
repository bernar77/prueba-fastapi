"""add fkey to post table

Revision ID: 579020354f17
Revises: 68b80ee2ade8
Create Date: 2022-04-19 13:00:27.583523

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '579020354f17'
down_revision = '68b80ee2ade8'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fkey', source_table='posts', referent_table='users', 
                            local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fkey', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
