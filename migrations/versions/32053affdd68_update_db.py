"""update db

Revision ID: 32053affdd68
Revises: 42317fb34fa8
Create Date: 2020-05-02 14:48:41.887975

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32053affdd68'
down_revision = '42317fb34fa8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_users_email', table_name='users')
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.create_index('ix_users_email', 'users', ['email'], unique=False)
    # ### end Alembic commands ###
